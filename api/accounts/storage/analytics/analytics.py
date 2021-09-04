from api.commons.auth import Auth

from .stored.stored import Stored


class Analytics(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "storage/analytics"
    _endpoint3 = None

    @property
    def stored(self):
        return Stored(self._config, self._session)
