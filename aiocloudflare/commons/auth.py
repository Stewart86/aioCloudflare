import typing
from typing import Any, Optional, Union

from httpx import USE_CLIENT_DEFAULT
from httpx import Auth as XAuth
from httpx._client import UseClientDefault
from httpx._models import Request, Response
from httpx._types import (
    AuthTypes,
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestContent,
    RequestFiles,
    TimeoutTypes,
)

from aiocloudflare.commons.exceptions import AuthenticationError

from .base import BaseClient, Delete, Get, Patch, Post, Put

RequestData = dict[Any, Any]


class _Auth(XAuth):
    def __init__(self, email: Optional[str], token: str) -> None:
        self._email = email
        self._token = token

    def auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
        if self._email is None:
            request.headers["Authorization"] = f"Bearer {self._token}"
            yield request

        if self._email is not None and self._token is not None:
            request.headers["X-Auth-Email"] = self._email
            request.headers["X-Auth-Key"] = self._token
            yield request


class Auth(BaseClient, Get, Post, Put, Delete, Patch):
    def __repr__(self) -> str:
        return f"Derived from: Auth, class: {self.__class__.__name__}"

    async def get(
        self,
        *args: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,  # type: ignore[assignment]
        cookies: CookieTypes = None,  # type: ignore[assignment]
        auth: Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        """GET method with AUTH"""
        self.__auth_init()
        return await super().get(
            *args,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=self._auth,
            allow_redirects=allow_redirects
            if allow_redirects is not None
            else USE_CLIENT_DEFAULT,
            timeout=timeout if timeout is not None else USE_CLIENT_DEFAULT,
        )

    async def post(
        self,
        *args: str,
        content: RequestContent = None,  # type: ignore[assignment]
        data: RequestData = None,  # type: ignore[assignment]
        files: RequestFiles = None,  # type: ignore[assignment]
        json: typing.Any = None,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,  # type: ignore[assignment]
        cookies: CookieTypes = None,  # type: ignore[assignment]
        auth: Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        self.__auth_init()
        return await super().post(
            *args,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=self._auth,
            allow_redirects=allow_redirects
            if allow_redirects is not None
            else USE_CLIENT_DEFAULT,
            timeout=timeout if timeout is not None else USE_CLIENT_DEFAULT,
        )

    async def put(
        self,
        *args: str,
        content: RequestContent = None,  # type: ignore[assignment]
        data: RequestData = None,  # type: ignore[assignment]
        files: RequestFiles = None,  # type: ignore[assignment]
        json: typing.Any = None,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,  # type: ignore[assignment]
        cookies: CookieTypes = None,  # type: ignore[assignment]
        auth: Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        self.__auth_init()
        return await super().put(
            *args,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=self._auth,
            allow_redirects=allow_redirects
            if allow_redirects is not None
            else USE_CLIENT_DEFAULT,
            timeout=timeout if timeout is not None else USE_CLIENT_DEFAULT,
        )

    async def delete(
        self,
        *args: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,  # type: ignore[assignment]
        cookies: CookieTypes = None,  # type: ignore[assignment]
        auth: Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        self.__auth_init()
        return await super().delete(
            *args,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=self._auth,
            allow_redirects=allow_redirects
            if allow_redirects is not None
            else USE_CLIENT_DEFAULT,
            timeout=timeout if timeout is not None else USE_CLIENT_DEFAULT,
        )

    async def patch(
        self,
        *args: str,
        content: RequestContent = None,  # type: ignore[assignment]
        data: RequestData = None,  # type: ignore[assignment]
        files: RequestFiles = None,  # type: ignore[assignment]
        json: Any = None,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,  # type: ignore[assignment]
        cookies: CookieTypes = None,  # type: ignore[assignment]
        auth: Union[AuthTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
        allow_redirects: Union[bool, UseClientDefault] = USE_CLIENT_DEFAULT,
        timeout: Union[TimeoutTypes, UseClientDefault] = USE_CLIENT_DEFAULT,
    ) -> Response:
        self.__auth_init()
        return await super().patch(
            *args,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=self._auth,
            allow_redirects=allow_redirects
            if allow_redirects is not None
            else USE_CLIENT_DEFAULT,
            timeout=timeout if timeout is not None else USE_CLIENT_DEFAULT,
        )

    def __auth_init(self) -> None:
        if self._config.EMAIL is None and self._config.TOKEN is None:
            raise AuthenticationError("Email and token cannot be None.")

        if self._config.TOKEN is None:
            raise AuthenticationError("Token is required.")

        self._auth = _Auth(self._config.EMAIL, self._config.TOKEN)
