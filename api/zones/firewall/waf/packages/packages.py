from api.commons.auth import Auth

from .groups.groups import Groups
from .rules.rules import Rules


class Packages(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf/packages"
    _endpoint3 = None

    @property
    def groups(self):
        return Groups(self._config, self._session)

    @property
    def rules(self):
        return Rules(self._config, self._session)
