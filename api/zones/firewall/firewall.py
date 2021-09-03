from api.commons.unused import Unused

from .access_rules.access_rules import AccessRules
from .lockdowns.lockdowns import Lockdowns
from .rules.rules import Rules
from .ua_rules.ua_rules import UaRules
from .waf.waf import Waf


class Firewall(Unused):
    _AUTH = "VOID"
    _endpoint1 = "zones"
    _endpoint2 = "firewall"
    _endpoint3 = None

    @property
    def access_rules(self):
        return AccessRules()

    @property
    def lockdowns(self):
        return Lockdowns()

    @property
    def rules(self):
        return Rules()

    @property
    def ua_rules(self):
        return UaRules()

    @property
    def waf(self):
        return Waf()
