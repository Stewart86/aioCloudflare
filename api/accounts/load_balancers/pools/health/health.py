from api.commons.auth import Auth


class Health(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers/pools"
    _endpoint3 = "health"
