from api.commons.auth import Auth


class Regions(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers/regions"
    _endpoint3 = None
