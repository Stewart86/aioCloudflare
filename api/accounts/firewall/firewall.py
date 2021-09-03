from api.commons.unused import Unused

from .access_rules.access_rules import AccessRules


class Firewall(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "firewall"
    _endpoint3 = None

    @property
    def access_rules(self):
        return AccessRules()
