from api.commons.auth import Auth

from .ca.ca import Ca
from .policies.policies import Policies
from .revoke_tokens.revoke_tokens import RevokeTokens


class Apps(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "access/apps"
    _endpoint3 = None

    @property
    def ca(self):
        return Ca()

    @property
    def policies(self):
        return Policies()

    @property
    def revoke_tokens(self):
        return RevokeTokens()
