import os
import json
from collections import defaultdict
from copy import copy
from pathlib import Path
from typing import Union

import black

# constants
IMPORT_CHILDREN = "from .{}.{} import {}"

AUTH_CLASS = {
    "VOID": "from api.commons.unused import Unused",
    "OPEN": "from api.commons.no_auth import NoAuth",
    "AUTH": "from api.commons.auth import Auth",
    "CERT": "from api.commons.cert_auth import CertAuth",
    "AUTH_UNWRAPPED": "from api.commons.auth_unwrapped import AuthUnwrapped",
}


class CodeGen:
    def __init__(self, data: list[dict[str, list[list[str]]]]):
        self._data = data

    def build_tree(self):
        result: list[
            dict[str, Union[str, list[dict[str, Union[str, list[str], bool, None]]]]]
        ] = []

        for module in self._data:
            back_ref = self.__build_backref(module)
            root_: dict[
                str, Union[str, list[dict[str, Union[str, list[str], bool, None]]]]
            ] = {}
            for root, endpoints in module.items():
                root_["root"] = root

                classes_: list[dict[str, Union[str, list[str], bool, None]]] = []
                for endpoint in endpoints:
                    # combined endpoints split by "/" e.g. ["zones","settings","waf"]
                    combined_path = self.__split_clean_path(endpoint)
                    path = copy(combined_path)
                    combined_path.reverse()
                    class_ = {
                        "name": combined_path[0],
                        "auth": endpoint[0],
                        "props": back_ref[
                            f"{combined_path[0]}"
                            if len(combined_path) <= 2
                            else f"{combined_path[0]}{combined_path[1]}"
                        ],
                        "destination": not bool(len(back_ref[combined_path[0]])),
                        "path": path,
                    }
                    class_ = class_ | self.__set_endpoints(endpoint)
                    classes_.append(class_)
                root_["classes"] = classes_
            result.append(root_)

        self._tree = result
        # return result for debug print statement
        return result

    def build_file(self):
        for root in self._tree:
            main_directory: Path = Path(__file__).parent.parent / "api"
            for class_ in root["classes"]:
                # assign directory
                directory = None
                clean_path = [i.split("::")[1] for i in class_["path"]]  # type: ignore

                if len(clean_path) == 1 and clean_path[0] == root["root"]:  # type: ignore
                    directory = main_directory / clean_path[0]  # type: ignore

                else:
                    # To avoid conflicting class names, all nested properties
                    # are contained within its parent folder
                    directory = main_directory
                    for i, _ in enumerate(clean_path):
                        directory = directory / clean_path[i]  # type: ignore

                # imports
                to_file = []
                all_auths = [AUTH_CLASS[class_["auth"]]]
                to_file.extend(["\n".join(all_auths)])
                imports = []
                for child in class_["props"]:  # type: ignore
                    clean_child = child.split("::")[1]
                    imports.append(
                        IMPORT_CHILDREN.format(
                            clean_child, clean_child, self.__class_name(clean_child)
                        )
                    )
                to_file.append("\n".join(imports))

                # class
                to_file.extend(
                    self.__build_class(
                        str(class_["name"]).split("::")[1],
                        class_["auth"],
                        class_["props"],
                        class_["endpoint1"],
                        class_["endpoint2"],
                        class_["endpoint3"],
                    )
                )

                # write
                if directory is not None:
                    self.__write_to_file(
                        directory,
                        f"{str(class_['name']).split('::')[1]}.py",
                        "\n\n".join(to_file),
                    )
                directory = None

    def __build_class(
        self,
        name: str,
        auth: str,
        props: list[str],
        endpoint1: str,
        endpoint2: str,
        endpoint3: str,
    ) -> list[str]:
        to_file: list[str] = []
        ep1: str = f'"{e}"' if (e := endpoint1) else e
        ep2: str = f'"{e}"' if (e := endpoint2) else e
        ep3: str = f'"{e}"' if (e := endpoint3) else e
        class_boiler = [
            f"class {self.__class_name(name)}({self.__get_super_class(auth)}):",
            f'    _AUTH = "{auth}"',
            f"    _endpoint1 = {ep1}",
            f"    _endpoint2 = {ep2}",
            f"    _endpoint3 = {ep3}",
        ]

        properties: list[str] = []
        for prop in props:
            properties.append(f"\n{self.__add_property(prop.split('::')[1])}\n")

        to_file.append("\n".join(class_boiler))
        to_file.append("\n".join(properties))

        return to_file

    def __add_property(self, prop_name: str) -> str:
        return "\n".join(
            [
                "    @property",
                f"    def {prop_name}(self):",
                f"        return {self.__class_name(prop_name)}(self._config, self._session)",
            ]
        )

    def __get_super_class(self, auth: str) -> str:
        return AUTH_CLASS[auth].split(" ")[3]

    def __class_name(self, name: str) -> str:
        # special case for import, should not remove "_"
        if name == "import_":
            return "Import_"
        title = name.replace("_", " ").title()
        return title.replace(" ", "")

    def __build_backref(
        self, module: dict[str, list[list[str]]]
    ) -> defaultdict[str, list[str]]:
        back_ref: defaultdict[str, list[str]] = defaultdict(lambda: list())
        for endpoints in module.values():
            for i, endpoint in enumerate(endpoints):
                # combined endpoints split by "/" e.g. ["zones","settings","waf"]
                combined_path = self.__split_clean_path(endpoint)
                combined_path.reverse()

                # loop combined path  in reverse e.g. ["waf","settings","zones"]
                for i, c in enumerate(combined_path):
                    # to be as unique as possible to avoid common names
                    # could add more condition if needed
                    if len(combined_path) > i + 2:
                        # waf settings zones
                        if (
                            c
                            not in back_ref[
                                f"{combined_path[i + 1]}{combined_path[i + 2]}"
                            ]
                        ):
                            back_ref[
                                f"{combined_path[i + 1]}{combined_path[i + 2]}"
                            ].append(c)

                    elif len(combined_path) > i + 1:
                        if c not in back_ref[combined_path[i + 1]]:
                            back_ref[combined_path[i + 1]].append(c)
        return back_ref

    def __set_endpoints(self, endpoint: list[str]) -> dict[str, Union[str, None]]:
        result: dict[str, Union[str, None]] = {}
        # endpoints check length to add data
        if len(endpoint) == 1:
            raise ValueError("endpoints length cannot be 1")

        elif len(endpoint) == 2:
            result["endpoint1"] = endpoint[1]
            result["endpoint2"] = None
            result["endpoint3"] = None

        elif len(endpoint) == 3:
            result["endpoint1"] = endpoint[1]
            result["endpoint2"] = endpoint[2]
            result["endpoint3"] = None

        elif len(endpoint) == 4:
            result["endpoint1"] = endpoint[1]
            result["endpoint2"] = endpoint[2]
            result["endpoint3"] = endpoint[3]

        else:
            raise ValueError("Unexpected number of parameters")
        return result

    def __write_to_file(self, directory: Path, filename, python_code: str) -> None:
        if not os.path.exists(directory):
            self.__setup_api_dir(directory)

        with open(directory / filename, "w") as f:
            f.write(python_code)

    def __setup_api_dir(self, dir_: Path):
        os.mkdir(dir_)
        with open(dir_ / "__init__.py", "w") as f:
            f.write("")

    def __split_clean_path(self, endpoint):
        combined = "/".join(endpoint[1:]).split("/")
        result = []
        for i, d in enumerate(combined):
            if d == "import":
                result.append(f"{i}::import_")
            elif d == "0rtt":
                result.append(f"{i}::ortt")
            else:
                result.append(f"{i}::{d}")
        return result


if "__main__" == __name__:
    data = None
    with open("scripts/api_v4_v2.json", "r") as f:
        data = json.load(f)

    code_gen: CodeGen = CodeGen(data)
    print(json.dumps(code_gen.build_tree(), indent=2))
    code_gen.build_file()

    try:
        black.main(args=("api",))
    # black  raise SystemExit is unnessary here. catch this to exit gracfully
    except SystemExit:
        pass
