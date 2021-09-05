from cloudflare.commons.auth import Auth

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
    def billing(self):
        return Billing(self._config, self._session)

    @property
    def firewall(self):
        return Firewall(self._config, self._session)

    @property
    def invites(self):
        return Invites(self._config, self._session)

    @property
    def organizations(self):
        return Organizations(self._config, self._session)

    @property
    def subscriptions(self):
        return Subscriptions(self._config, self._session)

    @property
    def load_balancers(self):
        return LoadBalancers(self._config, self._session)

    @property
    def workers(self):
        return Workers(self._config, self._session)

    @property
    def audit_logs(self):
        return AuditLogs(self._config, self._session)

    @property
    def load_balancing_analytics(self):
        return LoadBalancingAnalytics(self._config, self._session)

    @property
    def tokens(self):
        return Tokens(self._config, self._session)
