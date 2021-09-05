from aiocloudflare.commons.auth import Auth


class SecurityHeader(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/security_header"
    _endpoint3 = None
