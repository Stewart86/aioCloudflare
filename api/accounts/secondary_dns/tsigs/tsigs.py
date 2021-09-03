from api.commons.auth import Auth


class Tsigs(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "secondary_dns/tsigs"
    _endpoint3 = None
