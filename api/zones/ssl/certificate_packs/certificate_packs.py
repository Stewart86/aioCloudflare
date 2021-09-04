from api.commons.auth import Auth

from .order.order import Order
from .quota.quota import Quota


class CertificatePacks(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "ssl/certificate_packs"
    _endpoint3 = None

    @property
    def order(self):
        return Order(self._config, self._session)

    @property
    def quota(self):
        return Quota(self._config, self._session)
