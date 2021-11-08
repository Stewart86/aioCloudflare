from aiocloudflare.commons.unused import Unused

from .access_rules.access_rules import AccessRules
from .lockdowns.lockdowns import Lockdowns
from .rules.rules import Rules
from .ua_rules.ua_rules import UaRules
from .waf.waf import Waf


class Firewall(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "firewall"
    _endpoint3 = None

    @property
    def waf(self) -> Waf:
        return Waf(self._config, self._session)

    @property
    def rules(self) -> Rules:
        return Rules(self._config, self._session)

    @property
    def ua_rules(self) -> UaRules:
        return UaRules(self._config, self._session)

    @property
    def access_rules(self) -> AccessRules:
        return AccessRules(self._config, self._session)

    @property
    def lockdowns(self) -> Lockdowns:
        return Lockdowns(self._config, self._session)
