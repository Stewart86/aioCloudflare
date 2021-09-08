from aiocloudflare.commons.auth import Auth

from .settings.settings import Settings


class Pagerules(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "pagerules"
    _endpoint3 = None

    @property
    def settings(self) -> Settings:
        return Settings(self._config, self._session)
