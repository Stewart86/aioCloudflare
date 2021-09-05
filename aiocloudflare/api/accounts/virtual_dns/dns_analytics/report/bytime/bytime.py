from aiocloudflare.commons.auth import Auth


class Bytime(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "virtual_dns"
    _endpoint3 = "dns_analytics/report/bytime"
