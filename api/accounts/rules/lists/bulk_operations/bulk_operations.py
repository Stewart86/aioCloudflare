from api.commons.auth import Auth


class BulkOperations(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "rules/lists/bulk_operations"
    _endpoint3 = None
