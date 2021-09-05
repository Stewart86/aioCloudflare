from aiocloudflare.commons.auth import Auth

from .health.health import Health
from .preview.preview import Preview
from .references.references import References


class Pools(Auth):
    _endpoint1 = "user/load_balancers/pools"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def health(self) -> Health:
        return Health(self._config, self._session)

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)

    @property
    def references(self) -> References:
        return References(self._config, self._session)
