from api.commons.auth import Auth


class Analyze(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "ssl/analyze"
    _endpoint3 = None
