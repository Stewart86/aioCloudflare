from aiocloudflare.commons.auth import Auth


class Profile(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "billing/profile"
    _endpoint3 = None
