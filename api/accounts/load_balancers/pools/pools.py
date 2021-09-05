from api.commons.auth import Auth

from .health.health import Health
from .preview.preview import Preview
from .references.references import References


class Pools(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers/pools"
    _endpoint3 = None

    @property
    def health(self):
        return Health(self._config, self._session)

    @property
    def preview(self):
        return Preview(self._config, self._session)

    @property
    def references(self):
        return References(self._config, self._session)
