import typing
from typing import Any
from typing import Optional

from aiocloudflare.commons.config import Config
from httpx import AsyncClient
from httpx import Headers
from httpx import USE_CLIENT_DEFAULT
from httpx._client import UseClientDefault
from httpx._models import Response
from httpx._types import AuthTypes
from httpx._types import CookieTypes
from httpx._types import HeaderTypes
from httpx._types import QueryParamTypes
from httpx._types import RequestContent
from httpx._types import RequestFiles
from httpx._types import TimeoutTypes

RequestData = dict[Any, Any]


class BaseClient:
    _endpoint1: str = ""
    _endpoint2: Optional[str] = None
    _endpoint3: Optional[str] = None

    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config

        headers = Headers({"User-Agent": self._config.USER_AGENT})
        self._session.headers = headers

    def debug_print(
        self, method: str, *args: str, data: Optional[dict[str, Any]] = None
    ) -> None:
        endpoint = self.build_endpoint(method, *args, data=data)
        self._config.LOGGER.debug(
            f"Request starts.. Method: {method.upper()}, {self}, path: /{endpoint}"
        )

    def build_endpoint(
        self, method: str, *args: str, data: Optional[dict[Any, Any]] = None
    ) -> str:
        url = []
        if self._endpoint2 or (data and method == "get"):
            if len(args) == 0:
                raise ValueError("args cannot be None")

            if len(args) == 1 and self._endpoint2:
                url.append(self._endpoint1)
                url.append(args[0])
                url.append(self._endpoint2)
            elif len(args) == 2 and self._endpoint2:
                url.append(self._endpoint1)
                url.append(args[0])
                url.append(self._endpoint2)
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


class Get:
    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config

        headers = Headers({"User-Agent": self._config.USER_AGENT})
        self._session.headers = headers

    async def get(
        self,
        *args: str,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        if self._config.DEBUG:
            getattr(self, "debug_print")("get", *args)
        request = getattr(self, "_session").build_request(
            "get",
            getattr(self, "build_endpoint")("get", *args),
            params=params,
            headers=headers,
            cookies=cookies,
        )
        return await self._session.send(
            request=request, auth=auth, allow_redirects=allow_redirects, timeout=timeout
        )


class Post:
    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config

        headers = Headers({"User-Agent": self._config.USER_AGENT})
        self._session.headers = headers

    async def post(
        self,
        *args: str,
        content: Optional[RequestContent] = None,
        data: Optional[RequestData] = None,
        files: Optional[RequestFiles] = None,
        json: typing.Any = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        if self._config.DEBUG:
            getattr(self, "debug_print")("post", *args, data=data)
        request = getattr(self, "_session").build_request(
            "post",
            getattr(self, "build_endpoint")("post", *args),
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


class Put:
    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config

        headers = Headers({"User-Agent": self._config.USER_AGENT})
        self._session.headers = headers

    async def put(
        self,
        *args: str,
        content: Optional[RequestContent] = None,
        data: Optional[RequestData] = None,
        files: Optional[RequestFiles] = None,
        json: typing.Any = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        if self._config.DEBUG:
            getattr(self, "debug_print")("put", *args, data=data)
        request = getattr(self, "_session").build_request(
            "put",
            getattr(self, "build_endpoint")("put", *args),
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


class Patch:
    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config

        headers = Headers({"User-Agent": self._config.USER_AGENT})
        self._session.headers = headers

    async def patch(
        self,
        *args: str,
        content: Optional[RequestContent] = None,
        data: Optional[RequestData] = None,
        files: Optional[RequestFiles] = None,
        json: typing.Any = None,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        if self._config.DEBUG:
            getattr(self, "debug_print")("patch", *args, data=data)
        request = getattr(self, "_session").build_request(
            "patch",
            getattr(self, "build_endpoint")("patch", *args),
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


class Delete:
    def __init__(self, config: Config, session: AsyncClient) -> None:
        self._session = session
        self._config = config

        headers = Headers({"User-Agent": self._config.USER_AGENT})
        self._session.headers = headers

    async def delete(
        self,
        *args: str,
        params: Optional[QueryParamTypes] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: typing.Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        if self._config.DEBUG:
            getattr(self, "debug_print")("delete", *args)
        request = getattr(self, "_session").build_request(
            "delete",
            getattr(self, "build_endpoint")("delete", *args),
            cookies=cookies,
            headers=headers,
            params=params,
        )
        return await self._session.send(
            request=request, auth=auth, allow_redirects=allow_redirects, timeout=timeout
        )
