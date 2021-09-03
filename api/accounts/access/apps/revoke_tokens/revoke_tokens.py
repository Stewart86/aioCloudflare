from api.commons.auth import Auth


class RevokeTokens(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "access/apps"
    _endpoint3 = "revoke_tokens"
