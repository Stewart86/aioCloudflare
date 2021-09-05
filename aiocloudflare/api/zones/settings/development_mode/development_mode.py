from aiocloudflare.commons.auth import Auth


class DevelopmentMode(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/development_mode"
    _endpoint3 = None
