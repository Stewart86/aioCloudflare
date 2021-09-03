from api.commons.auth import Auth


class Delegations(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "addressing/prefixes"
    _endpoint3 = "delegations"
