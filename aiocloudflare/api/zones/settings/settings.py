from aiocloudflare.commons.auth import Auth

from .advanced_ddos.advanced_ddos import AdvancedDdos
from .always_online.always_online import AlwaysOnline
from .always_use_https.always_use_https import AlwaysUseHttps
from .automatic_https_rewrites.automatic_https_rewrites import AutomaticHttpsRewrites
from .brotli.brotli import Brotli
from .browser_cache_ttl.browser_cache_ttl import BrowserCacheTtl
from .browser_check.browser_check import BrowserCheck
from .cache_level.cache_level import CacheLevel
from .challenge_ttl.challenge_ttl import ChallengeTtl
from .ciphers.ciphers import Ciphers
from .development_mode.development_mode import DevelopmentMode
from .email_obfuscation.email_obfuscation import EmailObfuscation
from .h2_prioritization.h2_prioritization import H2Prioritization
from .hotlink_protection.hotlink_protection import HotlinkProtection
from .http2.http2 import Http2
from .http3.http3 import Http3
from .image_resizing.image_resizing import ImageResizing
from .ip_geolocation.ip_geolocation import IpGeolocation
from .ipv6.ipv6 import Ipv6
from .min_tls_version.min_tls_version import MinTlsVersion
from .minify.minify import Minify
from .mirage.mirage import Mirage
from .mobile_redirect.mobile_redirect import MobileRedirect
from .opportunistic_encryption.opportunistic_encryption import OpportunisticEncryption
from .opportunistic_onion.opportunistic_onion import OpportunisticOnion
from .origin_error_page_pass_thru.origin_error_page_pass_thru import (
    OriginErrorPagePassThru,
)
from .ortt.ortt import Ortt
from .polish.polish import Polish
from .prefetch_preload.prefetch_preload import PrefetchPreload
from .privacy_pass.privacy_pass import PrivacyPass
from .pseudo_ipv4.pseudo_ipv4 import PseudoIpv4
from .response_buffering.response_buffering import ResponseBuffering
from .rocket_loader.rocket_loader import RocketLoader
from .security_header.security_header import SecurityHeader
from .security_level.security_level import SecurityLevel
from .server_side_exclude.server_side_exclude import ServerSideExclude
from .sort_query_string_for_cache.sort_query_string_for_cache import (
    SortQueryStringForCache,
)
from .ssl.ssl import Ssl
from .tls_1_3.tls_1_3 import Tls13
from .tls_client_auth.tls_client_auth import TlsClientAuth
from .true_client_ip_header.true_client_ip_header import TrueClientIpHeader
from .waf.waf import Waf
from .webp.webp import Webp
from .websockets.websockets import Websockets


class Settings(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings"
    _endpoint3 = None

    @property
    def sort_query_string_for_cache(self) -> SortQueryStringForCache:
        return SortQueryStringForCache(self._config, self._session)

    @property
    def always_online(self) -> AlwaysOnline:
        return AlwaysOnline(self._config, self._session)

    @property
    def http3(self) -> Http3:
        return Http3(self._config, self._session)

    @property
    def webp(self) -> Webp:
        return Webp(self._config, self._session)

    @property
    def ipv6(self) -> Ipv6:
        return Ipv6(self._config, self._session)

    @property
    def browser_cache_ttl(self) -> BrowserCacheTtl:
        return BrowserCacheTtl(self._config, self._session)

    @property
    def privacy_pass(self) -> PrivacyPass:
        return PrivacyPass(self._config, self._session)

    @property
    def brotli(self) -> Brotli:
        return Brotli(self._config, self._session)

    @property
    def rocket_loader(self) -> RocketLoader:
        return RocketLoader(self._config, self._session)

    @property
    def browser_check(self) -> BrowserCheck:
        return BrowserCheck(self._config, self._session)

    @property
    def ssl(self) -> Ssl:
        return Ssl(self._config, self._session)

    @property
    def security_header(self) -> SecurityHeader:
        return SecurityHeader(self._config, self._session)

    @property
    def always_use_https(self) -> AlwaysUseHttps:
        return AlwaysUseHttps(self._config, self._session)

    @property
    def minify(self) -> Minify:
        return Minify(self._config, self._session)

    @property
    def ciphers(self) -> Ciphers:
        return Ciphers(self._config, self._session)

    @property
    def opportunistic_encryption(self) -> OpportunisticEncryption:
        return OpportunisticEncryption(self._config, self._session)

    @property
    def pseudo_ipv4(self) -> PseudoIpv4:
        return PseudoIpv4(self._config, self._session)

    @property
    def response_buffering(self) -> ResponseBuffering:
        return ResponseBuffering(self._config, self._session)

    @property
    def tls_client_auth(self) -> TlsClientAuth:
        return TlsClientAuth(self._config, self._session)

    @property
    def polish(self) -> Polish:
        return Polish(self._config, self._session)

    @property
    def challenge_ttl(self) -> ChallengeTtl:
        return ChallengeTtl(self._config, self._session)

    @property
    def ortt(self) -> Ortt:
        return Ortt(self._config, self._session)

    @property
    def advanced_ddos(self) -> AdvancedDdos:
        return AdvancedDdos(self._config, self._session)

    @property
    def origin_error_page_pass_thru(self) -> OriginErrorPagePassThru:
        return OriginErrorPagePassThru(self._config, self._session)

    @property
    def ip_geolocation(self) -> IpGeolocation:
        return IpGeolocation(self._config, self._session)

    @property
    def mobile_redirect(self) -> MobileRedirect:
        return MobileRedirect(self._config, self._session)

    @property
    def true_client_ip_header(self) -> TrueClientIpHeader:
        return TrueClientIpHeader(self._config, self._session)

    @property
    def hotlink_protection(self) -> HotlinkProtection:
        return HotlinkProtection(self._config, self._session)

    @property
    def automatic_https_rewrites(self) -> AutomaticHttpsRewrites:
        return AutomaticHttpsRewrites(self._config, self._session)

    @property
    def min_tls_version(self) -> MinTlsVersion:
        return MinTlsVersion(self._config, self._session)

    @property
    def opportunistic_onion(self) -> OpportunisticOnion:
        return OpportunisticOnion(self._config, self._session)

    @property
    def prefetch_preload(self) -> PrefetchPreload:
        return PrefetchPreload(self._config, self._session)

    @property
    def waf(self) -> Waf:
        return Waf(self._config, self._session)

    @property
    def cache_level(self) -> CacheLevel:
        return CacheLevel(self._config, self._session)

    @property
    def email_obfuscation(self) -> EmailObfuscation:
        return EmailObfuscation(self._config, self._session)

    @property
    def mirage(self) -> Mirage:
        return Mirage(self._config, self._session)

    @property
    def tls_1_3(self) -> Tls13:
        return Tls13(self._config, self._session)

    @property
    def http2(self) -> Http2:
        return Http2(self._config, self._session)

    @property
    def h2_prioritization(self) -> H2Prioritization:
        return H2Prioritization(self._config, self._session)

    @property
    def development_mode(self) -> DevelopmentMode:
        return DevelopmentMode(self._config, self._session)

    @property
    def websockets(self) -> Websockets:
        return Websockets(self._config, self._session)

    @property
    def security_level(self) -> SecurityLevel:
        return SecurityLevel(self._config, self._session)

    @property
    def image_resizing(self) -> ImageResizing:
        return ImageResizing(self._config, self._session)

    @property
    def server_side_exclude(self) -> ServerSideExclude:
        return ServerSideExclude(self._config, self._session)
