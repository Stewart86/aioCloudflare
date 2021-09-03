from api.commons.auth import Auth


class Websockets(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/websockets"
    _endpoint3 = None
