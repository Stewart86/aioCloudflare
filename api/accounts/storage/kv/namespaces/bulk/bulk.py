from api.commons.auth import Auth


class Bulk(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "storage/kv/namespaces"
    _endpoint3 = "bulk"
