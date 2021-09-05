from aiocloudflare.commons.auth import Auth


class ServiceTokens(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "access/service_tokens"
    _endpoint3 = None
