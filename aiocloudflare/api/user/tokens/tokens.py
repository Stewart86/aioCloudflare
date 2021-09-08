from aiocloudflare.commons.auth import Auth

from .permission_groups.permission_groups import PermissionGroups
from .value.value import Value
from .verify.verify import Verify


class Tokens(Auth):
    _endpoint1 = "user/tokens"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def value(self) -> Value:
        return Value(self._config, self._session)

    @property
    def verify(self) -> Verify:
        return Verify(self._config, self._session)

    @property
    def permission_groups(self) -> PermissionGroups:
        return PermissionGroups(self._config, self._session)
