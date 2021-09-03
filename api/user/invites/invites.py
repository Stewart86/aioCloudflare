from api.commons.auth import Auth


class Invites(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/invites"
    _endpoint2 = None
    _endpoint3 = None
