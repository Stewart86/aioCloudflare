from api.commons.auth import Auth

from .items.items import Items
from .bulk_operations.bulk_operations import BulkOperations


class Lists(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "rules/lists"
    _endpoint3 = None

    @property
    def items(self):
        return Items()

    @property
    def bulk_operations(self):
        return BulkOperations()
