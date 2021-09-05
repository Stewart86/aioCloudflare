from api.commons.unused import Unused

from .overrides.overrides import Overrides
from .packages.packages import Packages


class Waf(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf"
    _endpoint3 = None

    @property
    def overrides(self):
        return Overrides(self._config, self._session)

    @property
    def packages(self):
        return Packages(self._config, self._session)
