from api.commons.auth import Auth

from .revoke_user.revoke_user import RevokeUser


class Organizations(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "access/organizations"
    _endpoint3 = None

    @property
    def revoke_user(self):
        return RevokeUser()
