from aiocloudflare.commons.auth import Auth


class Events(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "security/events"
    _endpoint3 = None
