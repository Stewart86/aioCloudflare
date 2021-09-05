from aiocloudflare.commons.auth import Auth


class AlwaysOnline(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/always_online"
    _endpoint3 = None
