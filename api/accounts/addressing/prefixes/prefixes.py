from api.commons.auth import Auth

from .bgp.bgp import Bgp
from .delegations.delegations import Delegations


class Prefixes(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "addressing/prefixes"
    _endpoint3 = None

    @property
    def bgp(self):
        return Bgp()

    @property
    def delegations(self):
        return Delegations()
