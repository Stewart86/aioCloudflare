from api.commons.unused import Unused

from .rules.rules import Rules


class AccessRules(Unused):
    _endpoint1 = "user/firewall/access_rules"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def rules(self):
        return Rules(self._config, self._session)
