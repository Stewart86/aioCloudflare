from aiocloudflare.commons.auth import Auth

from .revoke_user.revoke_user import RevokeUser


class Organizations(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "access/organizations"
    _endpoint3 = None

    @property
    def revoke_user(self) -> RevokeUser:
        return RevokeUser(self._config, self._session)
