from aiocloudflare.commons.auth import Auth


class Certificates(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "access/certificates"
    _endpoint3 = None
