from aiocloudflare.commons.auth import Auth


class LoadBalancers(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "load_balancers"
    _endpoint3 = None
