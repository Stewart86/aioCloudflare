from api.commons.auth import Auth


class Prioritize(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "custom_certificates/prioritize"
    _endpoint3 = None
