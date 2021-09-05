from aiocloudflare.commons.auth import Auth


class Http3(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/http3"
    _endpoint3 = None
