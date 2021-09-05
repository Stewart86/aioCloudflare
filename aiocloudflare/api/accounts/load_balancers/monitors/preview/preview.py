from aiocloudflare.commons.auth import Auth


class Preview(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers/monitors"
    _endpoint3 = "preview"
