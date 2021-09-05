from aiocloudflare.commons.auth import Auth


class Quota(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "ssl/certificate_packs/quota"
    _endpoint3 = None
