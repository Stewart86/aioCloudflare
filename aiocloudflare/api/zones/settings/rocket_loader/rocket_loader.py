from aiocloudflare.commons.auth import Auth


class RocketLoader(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/rocket_loader"
    _endpoint3 = None
