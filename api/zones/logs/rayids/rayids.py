from api.commons.auth_unwrapped import AuthUnwrapped


class Rayids(AuthUnwrapped):
    _AUTH = "AUTH_UNWRAPPED"
    _endpoint1 = "zones"
    _endpoint2 = "logs/rayids"
    _endpoint3 = None
