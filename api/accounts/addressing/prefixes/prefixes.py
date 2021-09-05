from api.commons.auth import Auth

from .bgp.bgp import Bgp
from .delegations.delegations import Delegations


class Prefixes(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "addressing/prefixes"
    _endpoint3 = None

    @property
    def bgp(self):
        return Bgp(self._config, self._session)

    @property
    def delegations(self):
        return Delegations(self._config, self._session)
