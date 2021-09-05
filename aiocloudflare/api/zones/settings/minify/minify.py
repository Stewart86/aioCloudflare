from aiocloudflare.commons.auth import Auth


class Minify(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/minify"
    _endpoint3 = None
