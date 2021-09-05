from aiocloudflare.commons.auth import Auth


class SecurityLevel(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/security_level"
    _endpoint3 = None
