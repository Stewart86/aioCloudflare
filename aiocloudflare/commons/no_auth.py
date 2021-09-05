from .base import BaseClient
from .base import Get


class NoAuth(BaseClient, Get):
    def __repr__(self) -> str:
        return f"derived from: NoAuth, class: {self.__class__.__name__}"
