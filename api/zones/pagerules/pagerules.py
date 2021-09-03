from api.commons.auth import Auth

from .settings.settings import Settings


class Pagerules(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "pagerules"
    _endpoint3 = None

    @property
    def settings(self):
        return Settings()
