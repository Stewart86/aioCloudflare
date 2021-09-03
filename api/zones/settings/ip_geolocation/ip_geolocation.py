from api.commons.auth import Auth


class IpGeolocation(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/ip_geolocation"
    _endpoint3 = None
