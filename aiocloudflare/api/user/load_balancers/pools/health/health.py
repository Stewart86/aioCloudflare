from aiocloudflare.commons.auth import Auth


class Health(Auth):
    _endpoint1 = "user/load_balancers/pools"
    _endpoint2 = "health"
    _endpoint3 = None
