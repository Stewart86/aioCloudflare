from api.commons.auth import Auth

from .certificates.certificates import Certificates


class Hostnames(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "origin_tls_client_auth/hostnames"
    _endpoint3 = None

    @property
    def certificates(self):
        return Certificates()
