from aiocloudflare.commons.auth import Auth

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
    _endpoint1 = "accounts"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def billing(self) -> Billing:
        return Billing(self._config, self._session)

    @property
    def custom_pages(self) -> CustomPages:
        return CustomPages(self._config, self._session)

    @property
    def members(self) -> Members:
        return Members(self._config, self._session)

    @property
    def railguns(self) -> Railguns:
        return Railguns(self._config, self._session)

    @property
    def registrar(self) -> Registrar:
        return Registrar(self._config, self._session)

    @property
    def roles(self) -> Roles:
        return Roles(self._config, self._session)

    @property
    def rules(self) -> Rules:
        return Rules(self._config, self._session)

    @property
    def rulesets(self) -> Rulesets:
        return Rulesets(self._config, self._session)

    @property
    def storage(self) -> Storage:
        return Storage(self._config, self._session)

    @property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._config, self._session)

    @property
    def tunnels(self) -> Tunnels:
        return Tunnels(self._config, self._session)

    @property
    def virtual_dns(self) -> VirtualDns:
        return VirtualDns(self._config, self._session)

    @property
    def workers(self) -> Workers:
        return Workers(self._config, self._session)

    @property
    def addressing(self) -> Addressing:
        return Addressing(self._config, self._session)

    @property
    def audit_logs(self) -> AuditLogs:
        return AuditLogs(self._config, self._session)

    @property
    def load_balancers(self) -> LoadBalancers:
        return LoadBalancers(self._config, self._session)

    @property
    def firewall(self) -> Firewall:
        return Firewall(self._config, self._session)

    @property
    def secondary_dns(self) -> SecondaryDns:
        return SecondaryDns(self._config, self._session)

    @property
    def stream(self) -> Stream:
        return Stream(self._config, self._session)

    @property
    def access(self) -> Access:
        return Access(self._config, self._session)

    @property
    def diagnostics(self) -> Diagnostics:
        return Diagnostics(self._config, self._session)
