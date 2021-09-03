from api.commons.auth import Auth


class Preview(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/load_balancers/pools"
    _endpoint2 = "preview"
    _endpoint3 = None
