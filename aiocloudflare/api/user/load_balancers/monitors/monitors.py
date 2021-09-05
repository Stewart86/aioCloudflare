from aiocloudflare.commons.auth import Auth

from .preview.preview import Preview
from .references.references import References


class Monitors(Auth):
    _endpoint1 = "user/load_balancers/monitors"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)

    @property
    def references(self) -> References:
        return References(self._config, self._session)
