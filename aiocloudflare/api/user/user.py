from aiocloudflare.commons.auth import Auth

from .audit_logs.audit_logs import AuditLogs
from .billing.billing import Billing
from .firewall.firewall import Firewall
from .invites.invites import Invites
from .load_balancers.load_balancers import LoadBalancers
from .load_balancing_analytics.load_balancing_analytics import LoadBalancingAnalytics
from .organizations.organizations import Organizations
from .subscriptions.subscriptions import Subscriptions
from .tokens.tokens import Tokens
from .workers.workers import Workers


class User(Auth):
    _endpoint1 = "user"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def billing(self) -> Billing:
        return Billing(self._config, self._session)

    @property
    def firewall(self) -> Firewall:
        return Firewall(self._config, self._session)

    @property
    def invites(self) -> Invites:
        return Invites(self._config, self._session)

    @property
    def organizations(self) -> Organizations:
        return Organizations(self._config, self._session)

    @property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._config, self._session)

    @property
    def load_balancers(self) -> LoadBalancers:
        return LoadBalancers(self._config, self._session)

    @property
    def workers(self) -> Workers:
        return Workers(self._config, self._session)

    @property
    def audit_logs(self) -> AuditLogs:
        return AuditLogs(self._config, self._session)

    @property
    def load_balancing_analytics(self) -> LoadBalancingAnalytics:
        return LoadBalancingAnalytics(self._config, self._session)

    @property
    def tokens(self) -> Tokens:
        return Tokens(self._config, self._session)
