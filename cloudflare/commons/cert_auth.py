from .base import BaseClient


class CertAuth(BaseClient):
    def __repr__(self) -> str:
        return f"derived from: CertAuth, class: {self.__class__.__name__}"
