from api.commons.auth import Auth

from .activation_check.activation_check import ActivationCheck
from .available_plans.available_plans import AvailablePlans
from .available_rate_plans.available_rate_plans import AvailableRatePlans
from .custom_certificates.custom_certificates import CustomCertificates
from .custom_hostnames.custom_hostnames import CustomHostnames
from .custom_pages.custom_pages import CustomPages
from .dns_records.dns_records import DnsRecords
from .filters.filters import Filters
from .healthchecks.healthchecks import Healthchecks
from .keyless_certificates.keyless_certificates import KeylessCertificates
from .pagerules.pagerules import Pagerules
from .purge_cache.purge_cache import PurgeCache
from .railguns.railguns import Railguns
from .rulesets.rulesets import Rulesets
from .security.security import Security
from .subscription.subscription import Subscription
from .settings.settings import Settings
from .analytics.analytics import Analytics
from .firewall.firewall import Firewall
from .rate_limits.rate_limits import RateLimits
from .dns_analytics.dns_analytics import DnsAnalytics
from .amp.amp import Amp
from .logpush.logpush import Logpush
from .logs.logs import Logs
from .argo.argo import Argo
from .dnssec.dnssec import Dnssec
from .spectrum.spectrum import Spectrum
from .ssl.ssl import Ssl
from .origin_tls_client_auth.origin_tls_client_auth import OriginTlsClientAuth
from .workers.workers import Workers
from .load_balancers.load_balancers import LoadBalancers
from .secondary_dns.secondary_dns import SecondaryDns
from .media.media import Media
from .access.access import Access
from .waiting_rooms.waiting_rooms import WaitingRooms


class Zones(Auth):
    _endpoint1 = "zones"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def activation_check(self):
        return ActivationCheck(self._config, self._session)

    @property
    def available_plans(self):
        return AvailablePlans(self._config, self._session)

    @property
    def available_rate_plans(self):
        return AvailableRatePlans(self._config, self._session)

    @property
    def custom_certificates(self):
        return CustomCertificates(self._config, self._session)

    @property
    def custom_hostnames(self):
        return CustomHostnames(self._config, self._session)

    @property
    def custom_pages(self):
        return CustomPages(self._config, self._session)

    @property
    def dns_records(self):
        return DnsRecords(self._config, self._session)

    @property
    def filters(self):
        return Filters(self._config, self._session)

    @property
    def healthchecks(self):
        return Healthchecks(self._config, self._session)

    @property
    def keyless_certificates(self):
        return KeylessCertificates(self._config, self._session)

    @property
    def pagerules(self):
        return Pagerules(self._config, self._session)

    @property
    def purge_cache(self):
        return PurgeCache(self._config, self._session)

    @property
    def railguns(self):
        return Railguns(self._config, self._session)

    @property
    def rulesets(self):
        return Rulesets(self._config, self._session)

    @property
    def security(self):
        return Security(self._config, self._session)

    @property
    def subscription(self):
        return Subscription(self._config, self._session)

    @property
    def settings(self):
        return Settings(self._config, self._session)

    @property
    def analytics(self):
        return Analytics(self._config, self._session)

    @property
    def firewall(self):
        return Firewall(self._config, self._session)

    @property
    def rate_limits(self):
        return RateLimits(self._config, self._session)

    @property
    def dns_analytics(self):
        return DnsAnalytics(self._config, self._session)

    @property
    def amp(self):
        return Amp(self._config, self._session)

    @property
    def logpush(self):
        return Logpush(self._config, self._session)

    @property
    def logs(self):
        return Logs(self._config, self._session)

    @property
    def argo(self):
        return Argo(self._config, self._session)

    @property
    def dnssec(self):
        return Dnssec(self._config, self._session)

    @property
    def spectrum(self):
        return Spectrum(self._config, self._session)

    @property
    def ssl(self):
        return Ssl(self._config, self._session)

    @property
    def origin_tls_client_auth(self):
        return OriginTlsClientAuth(self._config, self._session)

    @property
    def workers(self):
        return Workers(self._config, self._session)

    @property
    def load_balancers(self):
        return LoadBalancers(self._config, self._session)

    @property
    def secondary_dns(self):
        return SecondaryDns(self._config, self._session)

    @property
    def media(self):
        return Media(self._config, self._session)

    @property
    def access(self):
        return Access(self._config, self._session)

    @property
    def waiting_rooms(self):
        return WaitingRooms(self._config, self._session)
