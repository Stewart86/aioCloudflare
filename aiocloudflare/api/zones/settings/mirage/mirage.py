from aiocloudflare.commons.auth import Auth


class Mirage(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/mirage"
    _endpoint3 = None
