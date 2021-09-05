from aiocloudflare.commons.auth import Auth


class Bindings(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "workers/script/bindings"
    _endpoint3 = None
