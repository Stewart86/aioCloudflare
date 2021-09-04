import typing
from typing import Any, Optional

from httpx import USE_CLIENT_DEFAULT, AsyncClient
from httpx._client import UseClientDefault
from httpx._models import Response
from httpx._types import (
    AuthTypes,
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestFiles,
    TimeoutTypes,
)

from api.commons.config import Config


class BaseClient:
    _BASE_URL = "http://www.stewartwong.com"
    _AUTH = None
    _endpoint1 = ""
    _endpoint2 = None
    _endpoint3 = None

    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config
        self._session.headers = {b"User-Agent": self._config.USER_AGENT}

    async def get(
        self,
        *args: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        if self._config.DEBUG:
            self.__debug_print("get", *args)
        request = self._session.build_request(
            "get",
            self.build_endpoint("get", *args),
            params=params,
            headers=headers,
            cookies=cookies,
        )
        return await self._session.send(
            request=request, auth=auth, allow_redirects=allow_redirects, timeout=timeout
        )

    async def post(
        self,
        *args: str,
        content: RequestContent = None,
        data: RequestData = None,
        files: RequestFiles = None,
        json: typing.Any = None,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        if self._config.DEBUG:
            self.__debug_print("post", *args, data=data)
        request = self._session.build_request(
            "post",
            self.build_endpoint("post", *args),
            params=params,
            headers=headers,
            cookies=cookies,
            files=files,
            json=json,
            content=content,
        )
        return await self._session.send(
            request=request, auth=auth, allow_redirects=allow_redirects, timeout=timeout
        )

    async def put(
        self,
        *args: str,
        content: RequestContent = None,
        data: RequestData = None,
        files: RequestFiles = None,
        json: typing.Any = None,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ):
        if self._config.DEBUG:
            self.__debug_print("put", *args, data=data)
        request = self._session.build_request(
            "put",
            self.build_endpoint("put", *args),
            content=content,
            cookies=cookies,
            files=files,
            headers=headers,
            json=json,
            params=params,
        )
        return await self._session.send(
            request=request, auth=auth, allow_redirects=allow_redirects, timeout=timeout
        )

    async def patch(
        self,
        *args: str,
        content: RequestContent = None,
        data: RequestData = None,
        files: RequestFiles = None,
        json: typing.Any = None,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ):
        if self._config.DEBUG:
            self.__debug_print("patch", *args, data=data)
        request = self._session.build_request(
            "patch",
            self.build_endpoint("patch", *args),
            content=content,
            cookies=cookies,
            files=files,
            headers=headers,
            json=json,
            params=params,
        )
        return await self._session.send(
            request=request, auth=auth, allow_redirects=allow_redirects, timeout=timeout
        )

    async def delete(
        self,
        *args: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ):
        if self._config.DEBUG:
            self.__debug_print("delete", *args)
        request = self._session.build_request(
            "delete",
            self.build_endpoint("delete", *args),
            cookies=cookies,
            headers=headers,
            params=params,
        )
        return await self._session.send(
            request=request, auth=auth, allow_redirects=allow_redirects, timeout=timeout
        )

    def __debug_print(
        self, method: str, *args: str, data: Optional[dict[str, Any]] = None
    ):
        endpoint = self.build_endpoint(method, *args, data=data)
        self._config.LOGGER.debug(
            f"Request starts.. Method: {method.upper()}, {self}, path: {endpoint}"
        )

    def build_endpoint(
        self, method: str, *args: str, data: Optional[dict[Any, Any]] = None
    ):
        url = []
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
