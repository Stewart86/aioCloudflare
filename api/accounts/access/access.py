from api.commons.unused import Unused

from .certificates.certificates import Certificates
from .groups.groups import Groups
from .identity_providers.identity_providers import IdentityProviders
from .organizations.organizations import Organizations
from .service_tokens.service_tokens import ServiceTokens
from .logs.logs import Logs
from .apps.apps import Apps


class Access(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "access"
    _endpoint3 = None

    @property
    def certificates(self):
        return Certificates()

    @property
    def groups(self):
        return Groups()

    @property
    def identity_providers(self):
        return IdentityProviders()

    @property
    def organizations(self):
        return Organizations()

    @property
    def service_tokens(self):
        return ServiceTokens()

    @property
    def logs(self):
        return Logs()

    @property
    def apps(self):
        return Apps()
