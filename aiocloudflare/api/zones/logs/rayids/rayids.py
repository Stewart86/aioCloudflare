from aiocloudflare.commons.auth_unwrapped import AuthUnwrapped


class Rayids(AuthUnwrapped):
    _endpoint1 = "zones"
    _endpoint2 = "logs/rayids"
    _endpoint3 = None
