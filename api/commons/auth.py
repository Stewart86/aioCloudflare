import typing

from httpx import USE_CLIENT_DEFAULT, Auth
from httpx._client import UseClientDefault
from httpx._models import Request, Response
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

from api.commons.exceptions import AuthenticationError

from .base import BaseClient, Delete, Get, Patch, Post, Put


class _Auth(Auth):
    def __init__(self, email: str, token: str) -> None:
        self._email = email
        self._token = token

    def auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
        if self._email is None:
            request.headers["Authorization"] = f"Bearer {self._token}"
            yield request

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
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
    ) -> Response:
        """GET method with AUTH"""
        self.__auth_init()
        return await super().get(
            *args,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=self._auth,
            allow_redirects=False,
            timeout=USE_CLIENT_DEFAULT,
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
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        allow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
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
            allow_redirects=allow_redirects,
            timeout=timeout,
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
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        allow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
    ):
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
            allow_redirects=allow_redirects,
            timeout=timeout,
        )

    async def delete(
        self,
        *args: str,
        params: QueryParamTypes = None,
        headers: HeaderTypes = None,
        cookies: CookieTypes = None,
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        allow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
    ):
        self.__auth_init()
        return await super().delete(
            *args,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=self._auth,
            allow_redirects=allow_redirects,
            timeout=timeout,
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
        auth: typing.Union[AuthTypes, UseClientDefault] = None,
        allow_redirects: typing.Union[bool, UseClientDefault] = None,
        timeout: typing.Union[TimeoutTypes, UseClientDefault] = None,
    ):
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
            allow_redirects=allow_redirects,
            timeout=timeout,
        )

    def __auth_init(self):
        if self._config.EMAIL is None and self._config.TOKEN is None:
            raise AuthenticationError("Email and token cannot be None.")

        if self._config.TOKEN is None:
            raise AuthenticationError("Token is required.")

        self._auth = _Auth(self._config.EMAIL, self._config.TOKEN)
