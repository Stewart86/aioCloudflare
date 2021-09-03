from api.commons.auth import Auth

from .health.health import Health
from .preview.preview import Preview
from .references.references import References


class Pools(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/load_balancers/pools"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def health(self):
        return Health()

    @property
    def preview(self):
        return Preview()

    @property
    def references(self):
        return References()
