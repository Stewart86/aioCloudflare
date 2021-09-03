from api.commons.auth import Auth

from .billing.billing import Billing
from .custom_pages.custom_pages import CustomPages
from .members.members import Members
from .railguns.railguns import Railguns
from .registrar.registrar import Registrar
from .roles.roles import Roles
from .rules.rules import Rules
from .rulesets.rulesets import Rulesets
from .storage.storage import Storage
from .subscriptions.subscriptions import Subscriptions
from .tunnels.tunnels import Tunnels
from .virtual_dns.virtual_dns import VirtualDns
from .workers.workers import Workers
from .addressing.addressing import Addressing
from .audit_logs.audit_logs import AuditLogs
from .load_balancers.load_balancers import LoadBalancers
from .firewall.firewall import Firewall
from .secondary_dns.secondary_dns import SecondaryDns
from .stream.stream import Stream
from .access.access import Access
from .diagnostics.diagnostics import Diagnostics


class Accounts(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def billing(self):
        return Billing()

    @property
    def custom_pages(self):
        return CustomPages()

    @property
    def members(self):
        return Members()

    @property
    def railguns(self):
        return Railguns()

    @property
    def registrar(self):
        return Registrar()

    @property
    def roles(self):
        return Roles()

    @property
    def rules(self):
        return Rules()

    @property
    def rulesets(self):
        return Rulesets()

    @property
    def storage(self):
        return Storage()

    @property
    def subscriptions(self):
        return Subscriptions()

    @property
    def tunnels(self):
        return Tunnels()

    @property
    def virtual_dns(self):
        return VirtualDns()

    @property
    def workers(self):
        return Workers()

    @property
    def addressing(self):
        return Addressing()

    @property
    def audit_logs(self):
        return AuditLogs()

    @property
    def load_balancers(self):
        return LoadBalancers()

    @property
    def firewall(self):
        return Firewall()

    @property
    def secondary_dns(self):
        return SecondaryDns()

    @property
    def stream(self):
        return Stream()

    @property
    def access(self):
        return Access()

    @property
    def diagnostics(self):
        return Diagnostics()
