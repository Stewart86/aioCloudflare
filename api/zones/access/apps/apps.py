from api.commons.auth import Auth

from .ca.ca import Ca
from .policies.policies import Policies
from .revoke_tokens.revoke_tokens import RevokeTokens


class Apps(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "access/apps"
    _endpoint3 = None

    @property
    def policies(self):
        return Policies(self._config, self._session)

    @property
    def revoke_tokens(self):
        return RevokeTokens(self._config, self._session)

    @property
    def ca(self):
        return Ca(self._config, self._session)
