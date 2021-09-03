from api.commons.auth import Auth


class Certificates(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "access/certificates"
    _endpoint3 = None
