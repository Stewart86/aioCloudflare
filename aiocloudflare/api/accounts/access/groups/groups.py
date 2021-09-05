from aiocloudflare.commons.auth import Auth


class Groups(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "access/groups"
    _endpoint3 = None
