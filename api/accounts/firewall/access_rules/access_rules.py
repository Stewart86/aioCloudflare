from api.commons.unused import Unused

from .rules.rules import Rules


class AccessRules(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "firewall/access_rules"
    _endpoint3 = None

    @property
    def rules(self):
        return Rules()
