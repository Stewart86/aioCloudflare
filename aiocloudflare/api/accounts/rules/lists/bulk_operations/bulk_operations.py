from aiocloudflare.commons.auth import Auth


class BulkOperations(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "rules/lists/bulk_operations"
    _endpoint3 = None
