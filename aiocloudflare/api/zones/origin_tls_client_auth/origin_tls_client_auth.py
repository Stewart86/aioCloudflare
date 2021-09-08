from aiocloudflare.commons.auth import Auth

from .hostnames.hostnames import Hostnames
from .settings.settings import Settings


class OriginTlsClientAuth(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "origin_tls_client_auth"
    _endpoint3 = None

    @property
    def hostnames(self) -> Hostnames:
        return Hostnames(self._config, self._session)

    @property
    def settings(self) -> Settings:
        return Settings(self._config, self._session)
