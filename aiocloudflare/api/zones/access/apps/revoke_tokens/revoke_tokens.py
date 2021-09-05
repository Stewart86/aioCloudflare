from aiocloudflare.commons.auth import Auth


class RevokeTokens(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "access/apps"
    _endpoint3 = "revoke_tokens"
