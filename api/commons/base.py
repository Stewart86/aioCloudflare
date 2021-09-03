from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseClient(ABC):
    _BASE_URL = "www.stewartwong.com"
    _AUTH = None
    _endpoint1 = ""
    _endpoint2 = None
    _endpoint3 = None

    @abstractmethod
    def get(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    @abstractmethod
    def post(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    @abstractmethod
    def put(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    @abstractmethod
    def delete(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        self.__test_print("get", *args, data=data)

    @abstractmethod
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
        endpoint = self.__build_endpoint(method, *args, data=data)
        print(
            f"{method.upper()}: AuthMethod = {self._AUTH}, class name = {self}, endpoint = {endpoint}"
        )

    def __build_endpoint(
        self, method: str, *args: str, data: Optional[dict[Any, Any]] = None
    ):
        url = [self._BASE_URL]
        if self._endpoint2 or (data and method == "get"):
            if len(args) == 0:
                raise ValueError("args cannot be None")

            if len(args) == 1 and self._endpoint2:
                url.append(self._endpoint1)
                url.append(args[0])
                url.append(self._endpoint2)
            elif len(args) == 2 and self.endpoint2:
                url.append(self._endpoint1)
                url.append(args[0])
                url.append(self._endpoint2)
                url.append(args[1])
        else:
            if len(args) == 0:
                url.append(self._endpoint1)
            else:
                url.append(self._endpoint1)
                url.append(args[0])

        if self._endpoint3:
            url.append(self._endpoint3)
        elif len(args) == 3:
            url.append(args[2])

        return "/".join(url)
