from aiocloudflare.commons.auth import Auth


class Verification(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "ssl/verification"
    _endpoint3 = None
