from aiocloudflare.commons.auth import Auth


class Groups(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "access/groups"
    _endpoint3 = None
