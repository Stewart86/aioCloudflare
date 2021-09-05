from aiocloudflare.commons.auth import Auth


class Regions(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers/regions"
    _endpoint3 = None
