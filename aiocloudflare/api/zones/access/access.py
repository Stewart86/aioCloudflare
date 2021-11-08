from aiocloudflare.commons.unused import Unused

from .apps.apps import Apps
from .certificates.certificates import Certificates
from .groups.groups import Groups
from .identity_providers.identity_providers import IdentityProviders
from .organizations.organizations import Organizations
from .service_tokens.service_tokens import ServiceTokens


class Access(Unused):
    _endpoint1 = "zones"
    _endpoint2 = "access"
    _endpoint3 = None

    @property
    def identity_providers(self) -> IdentityProviders:
        return IdentityProviders(self._config, self._session)

    @property
    def organizations(self) -> Organizations:
        return Organizations(self._config, self._session)

    @property
    def groups(self) -> Groups:
        return Groups(self._config, self._session)

    @property
    def service_tokens(self) -> ServiceTokens:
        return ServiceTokens(self._config, self._session)

    @property
    def certificates(self) -> Certificates:
        return Certificates(self._config, self._session)

    @property
    def apps(self) -> Apps:
        return Apps(self._config, self._session)
