from api.commons.auth import Auth

from .policies.policies import Policies
from .revoke_tokens.revoke_tokens import RevokeTokens
from .ca.ca import Ca


class Apps(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "access/apps"
    _endpoint3 = None

    @property
    def policies(self):
        return Policies()

    @property
    def revoke_tokens(self):
        return RevokeTokens()

    @property
    def ca(self):
        return Ca()
