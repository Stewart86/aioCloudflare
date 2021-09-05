from aiocloudflare.commons.auth import Auth


class ServerSideExclude(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/server_side_exclude"
    _endpoint3 = None
