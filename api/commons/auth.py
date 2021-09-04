from typing import Any, Optional

from .base import BaseClient


class Auth(BaseClient):
    async def __aenter(self):
        await self._session._request

    def __repr__(self) -> str:
        return f"derived from: Auth, class: {self.__class__.__name__}"

    async def get(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        return await super().get(*args, params=params, data=data, files=files)

    def post(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        return super().post(*args, params=params, data=data, files=files)

    def put(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        return super().put(*args, params=params, data=data, files=files)

    def delete(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        return super().delete(*args, params=params, data=data, files=files)

    def patch(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        return super().patch(*args, params=params, data=data, files=files)
