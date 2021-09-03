from api.commons.auth import Auth

from .groups.groups import Groups
from .rules.rules import Rules


class Packages(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "firewall/waf/packages"
    _endpoint3 = None

    @property
    def groups(self):
        return Groups()

    @property
    def rules(self):
        return Rules()
