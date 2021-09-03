from api.commons.auth import Auth


class Events(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "security/events"
    _endpoint3 = None
