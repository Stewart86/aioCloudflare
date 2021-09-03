from api.commons.auth import Auth


class ServiceTokens(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "access/service_tokens"
    _endpoint3 = None
