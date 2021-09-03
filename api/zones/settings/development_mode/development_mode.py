from api.commons.auth import Auth


class DevelopmentMode(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/development_mode"
    _endpoint3 = None
