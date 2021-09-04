import typing

from httpx import USE_CLIENT_DEFAULT, AsyncClient, Auth
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

from api.commons.config import Config
from api.commons.exceptions import AuthenticationError

from .base import BaseClient


class _Auth(Auth):
    def __init__(self, email: str, token: str) -> None:
        if email is None and token is None:
            raise AuthenticationError("Email and token cannot be None.")

        if token is None:
            raise AuthenticationError("Token is required.")

        self._email = email
        self._token = token

    def auth_flow(self, request: Request) -> typing.Generator[Request, Response, None]:
        if self._email is None:
            request.headers["Authorization"] = f"Bearer {self._token}"
            yield request

        request.headers["X-Auth-Email"] = self._email
        request.headers["X-Auth-Key"] = self._token
        yield request


class Auth(BaseClient):
    def __init__(self, config: Config, session: AsyncClient) -> None:
        super().__init__(config, session)
        self._auth = _Auth(self._config.EMAIL, self._config.TOKEN)

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
