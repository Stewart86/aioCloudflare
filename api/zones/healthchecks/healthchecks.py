from api.commons.auth import Auth


class Healthchecks(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "healthchecks"
    _endpoint3 = None
