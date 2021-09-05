from aiocloudflare.commons.auth import Auth


class IpGeolocation(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/ip_geolocation"
    _endpoint3 = None
