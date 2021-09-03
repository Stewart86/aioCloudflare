from api.commons.unused import Unused

from .overrides.overrides import Overrides
from .packages.packages import Packages


class Waf(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf"
    _endpoint3 = None

    @property
    def overrides(self):
        return Overrides()

    @property
    def packages(self):
        return Packages()
