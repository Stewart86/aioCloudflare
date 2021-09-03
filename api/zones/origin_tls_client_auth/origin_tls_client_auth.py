from api.commons.auth import Auth

from .hostnames.hostnames import Hostnames
from .settings.settings import Settings


class OriginTlsClientAuth(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "origin_tls_client_auth"
    _endpoint3 = None

    @property
    def hostnames(self):
        return Hostnames()

    @property
    def settings(self):
        return Settings()
