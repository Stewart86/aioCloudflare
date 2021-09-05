from aiocloudflare.commons.auth import Auth


class TrueClientIpHeader(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/true_client_ip_header"
    _endpoint3 = None
