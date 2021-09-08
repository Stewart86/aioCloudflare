from aiocloudflare.commons.unused import Unused

from .access_rules.access_rules import AccessRules


class Firewall(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "firewall"
    _endpoint3 = None

    @property
    def access_rules(self) -> AccessRules:
        return AccessRules(self._config, self._session)
