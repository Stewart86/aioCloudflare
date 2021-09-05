from aiocloudflare.commons.auth import Auth

from .bulk_operations.bulk_operations import BulkOperations
from .items.items import Items


class Lists(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "rules/lists"
    _endpoint3 = None

    @property
    def items(self) -> Items:
        return Items(self._config, self._session)

    @property
    def bulk_operations(self) -> BulkOperations:
        return BulkOperations(self._config, self._session)
