from api.commons.auth import Auth


class CustomCertificates(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "custom_certificates"
    _endpoint3 = None
