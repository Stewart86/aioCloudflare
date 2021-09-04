import typing

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

from api.commons.exceptions import CloudflareMethodNotAvailable

from .base import BaseClient


class NoAuth(BaseClient):
    def __repr__(self) -> str:
        return f"derived from: NoAuth, class: {self.__class__.__name__}"

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
        """Method is not available
        ---
        """
        raise CloudflareMethodNotAvailable("Method is not available for the endpoint.")

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
        """Method is not available
        ---
        """
        raise CloudflareMethodNotAvailable("Method is not available for the endpoint.")

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
        """Method is not available
        ---
        """
        raise CloudflareMethodNotAvailable("Method is not available for the endpoint.")

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
        """Method is not available
        ---
        """
        raise CloudflareMethodNotAvailable("Method is not available for the endpoint.")
