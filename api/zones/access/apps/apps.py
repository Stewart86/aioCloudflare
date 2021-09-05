from api.commons.auth import Auth

from .policies.policies import Policies
from .revoke_tokens.revoke_tokens import RevokeTokens
from .ca.ca import Ca


class Apps(Auth):
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
