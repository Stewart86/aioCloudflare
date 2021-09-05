from aiocloudflare.commons.auth import Auth


class RevokeUser(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "access/organizations/revoke_user"
    _endpoint3 = None
