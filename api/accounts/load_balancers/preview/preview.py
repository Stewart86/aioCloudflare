from api.commons.auth import Auth


class Preview(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers/preview"
    _endpoint3 = None
