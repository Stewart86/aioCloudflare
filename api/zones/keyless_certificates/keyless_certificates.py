from api.commons.auth import Auth


class KeylessCertificates(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "keyless_certificates"
    _endpoint3 = None
