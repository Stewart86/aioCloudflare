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
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def activation_check(self):
        return ActivationCheck()

    @property
    def available_plans(self):
        return AvailablePlans()

    @property
    def available_rate_plans(self):
        return AvailableRatePlans()

    @property
    def custom_certificates(self):
        return CustomCertificates()

    @property
    def custom_hostnames(self):
        return CustomHostnames()

    @property
    def custom_pages(self):
        return CustomPages()

    @property
    def dns_records(self):
        return DnsRecords()

    @property
    def filters(self):
        return Filters()

    @property
    def healthchecks(self):
        return Healthchecks()

    @property
    def keyless_certificates(self):
        return KeylessCertificates()

    @property
    def pagerules(self):
        return Pagerules()

    @property
    def purge_cache(self):
        return PurgeCache()

    @property
    def railguns(self):
        return Railguns()

    @property
    def rulesets(self):
        return Rulesets()

    @property
    def security(self):
        return Security()

    @property
    def subscription(self):
        return Subscription()

    @property
    def settings(self):
        return Settings()

    @property
    def analytics(self):
        return Analytics()

    @property
    def firewall(self):
        return Firewall()

    @property
    def rate_limits(self):
        return RateLimits()

    @property
    def dns_analytics(self):
        return DnsAnalytics()

    @property
    def amp(self):
        return Amp()

    @property
    def logpush(self):
        return Logpush()

    @property
    def logs(self):
        return Logs()

    @property
    def argo(self):
        return Argo()

    @property
    def dnssec(self):
        return Dnssec()

    @property
    def spectrum(self):
        return Spectrum()

    @property
    def ssl(self):
        return Ssl()

    @property
    def origin_tls_client_auth(self):
        return OriginTlsClientAuth()

    @property
    def workers(self):
        return Workers()

    @property
    def load_balancers(self):
        return LoadBalancers()

    @property
    def secondary_dns(self):
        return SecondaryDns()

    @property
    def media(self):
        return Media()

    @property
    def access(self):
        return Access()

    @property
    def waiting_rooms(self):
        return WaitingRooms()
