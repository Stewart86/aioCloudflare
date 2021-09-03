from api.commons.auth import Auth

from .ortt.ortt import Ortt
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
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings"
    _endpoint3 = None

    @property
    def ortt(self):
        return Ortt()

    @property
    def advanced_ddos(self):
        return AdvancedDdos()

    @property
    def always_online(self):
        return AlwaysOnline()

    @property
    def always_use_https(self):
        return AlwaysUseHttps()

    @property
    def automatic_https_rewrites(self):
        return AutomaticHttpsRewrites()

    @property
    def brotli(self):
        return Brotli()

    @property
    def browser_cache_ttl(self):
        return BrowserCacheTtl()

    @property
    def browser_check(self):
        return BrowserCheck()

    @property
    def cache_level(self):
        return CacheLevel()

    @property
    def challenge_ttl(self):
        return ChallengeTtl()

    @property
    def ciphers(self):
        return Ciphers()

    @property
    def development_mode(self):
        return DevelopmentMode()

    @property
    def email_obfuscation(self):
        return EmailObfuscation()

    @property
    def h2_prioritization(self):
        return H2Prioritization()

    @property
    def hotlink_protection(self):
        return HotlinkProtection()

    @property
    def http2(self):
        return Http2()

    @property
    def http3(self):
        return Http3()

    @property
    def image_resizing(self):
        return ImageResizing()

    @property
    def ip_geolocation(self):
        return IpGeolocation()

    @property
    def ipv6(self):
        return Ipv6()

    @property
    def min_tls_version(self):
        return MinTlsVersion()

    @property
    def minify(self):
        return Minify()

    @property
    def mirage(self):
        return Mirage()

    @property
    def mobile_redirect(self):
        return MobileRedirect()

    @property
    def opportunistic_encryption(self):
        return OpportunisticEncryption()

    @property
    def opportunistic_onion(self):
        return OpportunisticOnion()

    @property
    def origin_error_page_pass_thru(self):
        return OriginErrorPagePassThru()

    @property
    def polish(self):
        return Polish()

    @property
    def prefetch_preload(self):
        return PrefetchPreload()

    @property
    def privacy_pass(self):
        return PrivacyPass()

    @property
    def pseudo_ipv4(self):
        return PseudoIpv4()

    @property
    def response_buffering(self):
        return ResponseBuffering()

    @property
    def rocket_loader(self):
        return RocketLoader()

    @property
    def security_header(self):
        return SecurityHeader()

    @property
    def security_level(self):
        return SecurityLevel()

    @property
    def server_side_exclude(self):
        return ServerSideExclude()

    @property
    def sort_query_string_for_cache(self):
        return SortQueryStringForCache()

    @property
    def ssl(self):
        return Ssl()

    @property
    def tls_1_3(self):
        return Tls13()

    @property
    def tls_client_auth(self):
        return TlsClientAuth()

    @property
    def true_client_ip_header(self):
        return TrueClientIpHeader()

    @property
    def waf(self):
        return Waf()

    @property
    def webp(self):
        return Webp()

    @property
    def websockets(self):
        return Websockets()
