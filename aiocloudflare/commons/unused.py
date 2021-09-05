from aiocloudflare.commons.base import BaseClient


class Unused(BaseClient):
    def __repr__(self) -> str:
        return f"derived from: Unused, class: {self.__class__.__name__}"
