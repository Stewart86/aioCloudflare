from aiocloudflare.commons.auth import Auth


class Bulk(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "storage/kv/namespaces"
    _endpoint3 = "bulk"
