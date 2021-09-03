from api.commons.auth import Auth


class Profile(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "billing/profile"
    _endpoint3 = None
