from api.commons.auth import Auth

from .access.access import Access
from .addressing.addressing import Addressing
from .audit_logs.audit_logs import AuditLogs
from .billing.billing import Billing
from .custom_pages.custom_pages import CustomPages
from .diagnostics.diagnostics import Diagnostics
from .firewall.firewall import Firewall
from .load_balancers.load_balancers import LoadBalancers
from .members.members import Members
from .railguns.railguns import Railguns
from .registrar.registrar import Registrar
from .roles.roles import Roles
from .rules.rules import Rules
from .rulesets.rulesets import Rulesets
from .secondary_dns.secondary_dns import SecondaryDns
from .storage.storage import Storage
from .stream.stream import Stream
from .subscriptions.subscriptions import Subscriptions
from .tunnels.tunnels import Tunnels
from .virtual_dns.virtual_dns import VirtualDns
from .workers.workers import Workers


class Accounts(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def billing(self):
        return Billing(self._config, self._session)

    @property
    def custom_pages(self):
        return CustomPages(self._config, self._session)

    @property
    def members(self):
        return Members(self._config, self._session)

    @property
    def railguns(self):
        return Railguns(self._config, self._session)

    @property
    def registrar(self):
        return Registrar(self._config, self._session)

    @property
    def roles(self):
        return Roles(self._config, self._session)

    @property
    def rules(self):
        return Rules(self._config, self._session)

    @property
    def rulesets(self):
        return Rulesets(self._config, self._session)

    @property
    def storage(self):
        return Storage(self._config, self._session)

    @property
    def subscriptions(self):
        return Subscriptions(self._config, self._session)

    @property
    def tunnels(self):
        return Tunnels(self._config, self._session)

    @property
    def virtual_dns(self):
        return VirtualDns(self._config, self._session)

    @property
    def workers(self):
        return Workers(self._config, self._session)

    @property
    def addressing(self):
        return Addressing(self._config, self._session)

    @property
    def audit_logs(self):
        return AuditLogs(self._config, self._session)

    @property
    def load_balancers(self):
        return LoadBalancers(self._config, self._session)

    @property
    def firewall(self):
        return Firewall(self._config, self._session)

    @property
    def secondary_dns(self):
        return SecondaryDns(self._config, self._session)

    @property
    def stream(self):
        return Stream(self._config, self._session)

    @property
    def access(self):
        return Access(self._config, self._session)

    @property
    def diagnostics(self):
        return Diagnostics(self._config, self._session)
