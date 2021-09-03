from api.commons.auth import Auth


class ResponseBuffering(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/response_buffering"
    _endpoint3 = None
