from api.commons.auth import Auth

from .permission_groups.permission_groups import PermissionGroups
from .verify.verify import Verify
from .value.value import Value


class Tokens(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/tokens"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def permission_groups(self):
        return PermissionGroups()

    @property
    def verify(self):
        return Verify()

    @property
    def value(self):
        return Value()
