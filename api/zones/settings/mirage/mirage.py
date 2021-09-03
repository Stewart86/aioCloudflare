from api.commons.auth import Auth


class Mirage(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/mirage"
    _endpoint3 = None
