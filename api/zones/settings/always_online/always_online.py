from api.commons.auth import Auth


class AlwaysOnline(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/always_online"
    _endpoint3 = None
