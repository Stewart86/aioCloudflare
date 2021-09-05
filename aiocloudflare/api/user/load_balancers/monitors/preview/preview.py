from aiocloudflare.commons.auth import Auth


class Preview(Auth):
    _endpoint1 = "user/load_balancers/monitors"
    _endpoint2 = "preview"
    _endpoint3 = None
