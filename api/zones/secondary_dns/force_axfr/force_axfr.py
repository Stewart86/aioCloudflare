from api.commons.auth import Auth


class ForceAxfr(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "secondary_dns/force_axfr"
    _endpoint3 = None
