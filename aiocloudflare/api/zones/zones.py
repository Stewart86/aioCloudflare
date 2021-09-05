from aiocloudflare.commons.auth import Auth

from .access.access import Access
from .activation_check.activation_check import ActivationCheck
from .amp.amp import Amp
from .analytics.analytics import Analytics
from .argo.argo import Argo
from .available_plans.available_plans import AvailablePlans
from .available_rate_plans.available_rate_plans import AvailableRatePlans
from .custom_certificates.custom_certificates import CustomCertificates
from .custom_hostnames.custom_hostnames import CustomHostnames
from .custom_pages.custom_pages import CustomPages
from .dns_analytics.dns_analytics import DnsAnalytics
from .dns_records.dns_records import DnsRecords
from .dnssec.dnssec import Dnssec
from .filters.filters import Filters
from .firewall.firewall import Firewall
from .healthchecks.healthchecks import Healthchecks
from .keyless_certificates.keyless_certificates import KeylessCertificates
from .load_balancers.load_balancers import LoadBalancers
from .logpush.logpush import Logpush
from .logs.logs import Logs
from .media.media import Media
from .origin_tls_client_auth.origin_tls_client_auth import OriginTlsClientAuth
from .pagerules.pagerules import Pagerules
from .purge_cache.purge_cache import PurgeCache
from .railguns.railguns import Railguns
from .rate_limits.rate_limits import RateLimits
from .rulesets.rulesets import Rulesets
from .secondary_dns.secondary_dns import SecondaryDns
from .security.security import Security
from .settings.settings import Settings
from .spectrum.spectrum import Spectrum
from .ssl.ssl import Ssl
from .subscription.subscription import Subscription
from .waiting_rooms.waiting_rooms import WaitingRooms
from .workers.workers import Workers


class Zones(Auth):
    _endpoint1 = "zones"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def activation_check(self) -> ActivationCheck:
        return ActivationCheck(self._config, self._session)

    @property
    def available_plans(self) -> AvailablePlans:
        return AvailablePlans(self._config, self._session)

    @property
    def available_rate_plans(self) -> AvailableRatePlans:
        return AvailableRatePlans(self._config, self._session)

    @property
    def custom_certificates(self) -> CustomCertificates:
        return CustomCertificates(self._config, self._session)

    @property
    def custom_hostnames(self) -> CustomHostnames:
        return CustomHostnames(self._config, self._session)

    @property
    def custom_pages(self) -> CustomPages:
        return CustomPages(self._config, self._session)

    @property
    def dns_records(self) -> DnsRecords:
        return DnsRecords(self._config, self._session)

    @property
    def filters(self) -> Filters:
        return Filters(self._config, self._session)

    @property
    def healthchecks(self) -> Healthchecks:
        return Healthchecks(self._config, self._session)

    @property
    def keyless_certificates(self) -> KeylessCertificates:
        return KeylessCertificates(self._config, self._session)

    @property
    def pagerules(self) -> Pagerules:
        return Pagerules(self._config, self._session)

    @property
    def purge_cache(self) -> PurgeCache:
        return PurgeCache(self._config, self._session)

    @property
    def railguns(self) -> Railguns:
        return Railguns(self._config, self._session)

    @property
    def rulesets(self) -> Rulesets:
        return Rulesets(self._config, self._session)

    @property
    def security(self) -> Security:
        return Security(self._config, self._session)

    @property
    def subscription(self) -> Subscription:
        return Subscription(self._config, self._session)

    @property
    def settings(self) -> Settings:
        return Settings(self._config, self._session)

    @property
    def analytics(self) -> Analytics:
        return Analytics(self._config, self._session)

    @property
    def firewall(self) -> Firewall:
        return Firewall(self._config, self._session)

    @property
    def rate_limits(self) -> RateLimits:
        return RateLimits(self._config, self._session)

    @property
    def dns_analytics(self) -> DnsAnalytics:
        return DnsAnalytics(self._config, self._session)

    @property
    def amp(self) -> Amp:
        return Amp(self._config, self._session)

    @property
    def logpush(self) -> Logpush:
        return Logpush(self._config, self._session)

    @property
    def logs(self) -> Logs:
        return Logs(self._config, self._session)

    @property
    def argo(self) -> Argo:
        return Argo(self._config, self._session)

    @property
    def dnssec(self) -> Dnssec:
        return Dnssec(self._config, self._session)

    @property
    def spectrum(self) -> Spectrum:
        return Spectrum(self._config, self._session)

    @property
    def ssl(self) -> Ssl:
        return Ssl(self._config, self._session)

    @property
    def origin_tls_client_auth(self) -> OriginTlsClientAuth:
        return OriginTlsClientAuth(self._config, self._session)

    @property
    def workers(self) -> Workers:
        return Workers(self._config, self._session)

    @property
    def load_balancers(self) -> LoadBalancers:
        return LoadBalancers(self._config, self._session)

    @property
    def secondary_dns(self) -> SecondaryDns:
        return SecondaryDns(self._config, self._session)

    @property
    def media(self) -> Media:
        return Media(self._config, self._session)

    @property
    def access(self) -> Access:
        return Access(self._config, self._session)

    @property
    def waiting_rooms(self) -> WaitingRooms:
        return WaitingRooms(self._config, self._session)
