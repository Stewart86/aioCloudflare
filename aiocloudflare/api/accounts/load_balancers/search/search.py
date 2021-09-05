from aiocloudflare.commons.auth import Auth


class Search(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "load_balancers/search"
    _endpoint3 = None
