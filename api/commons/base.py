from typing import Any, Optional

from api.commons.config import Config
from httpx import AsyncClient


class BaseClient:
    _BASE_URL = "http://www.stewartwong.com"
    _AUTH = None
    _endpoint1 = ""
    _endpoint2 = None
    _endpoint3 = None

    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config

    async def get(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)
        resp = await self._session.get(
            self.build_endpoint("get", *args, data),
            **{"params": params},
        )
        print(resp.status_code)
        return resp.text

    def post(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    def put(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    def delete(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    def patch(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    def __test_print(
        self, method: str, *args: str, data: Optional[dict[str, Any]] = None
    ):
        endpoint = self.build_endpoint(method, *args, data=data)
        print(
            f"{method.upper()}: AuthMethod = {self._AUTH}, class name = {self}, endpoint = {endpoint}"
        )

    def build_endpoint(
        self, method: str, *args: str, data: Optional[dict[Any, Any]] = None
    ):
        url = [self._BASE_URL]
        print(
            "build_endpoint:: ",
            url,
            self._endpoint1,
            self._endpoint2,
            self._endpoint3,
            args,
        )
        if self._endpoint2 or (data and method == "get"):
            if len(args) == 0:
                raise ValueError("args cannot be None")

            if len(args) == 1 and self._endpoint2:
                url.append(self._endpoint1)
                if args[0] is not None:
                    url.append(args[0])
                url.append(self._endpoint2)
            elif len(args) == 2 and self._endpoint2:
                url.append(self._endpoint1)
                if args[0] is not None:
                    url.append(args[0])
                url.append(self._endpoint2)
                if args[1] is not None:
                    url.append(args[1])
        else:
            if len(args) == 0:
                url.append(self._endpoint1)
            else:
                url.append(self._endpoint1)
                if args[0] is not None:
                    url.append(args[0])

        if self._endpoint3:
            url.append(self._endpoint3)
        elif len(args) == 3:
            if args[2] is not None:
                url.append(args[2])

        return "/".join(url)
