from aiocloudflare.commons.auth import Auth


class Masters(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "secondary_dns/masters"
    _endpoint3 = None
