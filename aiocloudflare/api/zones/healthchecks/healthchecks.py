from aiocloudflare.commons.auth import Auth


class Healthchecks(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "healthchecks"
    _endpoint3 = None
