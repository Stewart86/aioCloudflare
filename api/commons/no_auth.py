from typing import Any, Optional

from .base import BaseClient


class NoAuth(BaseClient):
    def __repr__(self) -> str:
        return f"derived from: NoAuth, class: {self.__class__.__name__}"

    def get(
        self,
        *args: str,
        params: Optional[dict[str, Any]] = None,
        data: Optional[dict[str, Any]] = None,
        files: Optional[str] = None,
    ):
        return super().get(*args, params=params, data=data, files=files)

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
