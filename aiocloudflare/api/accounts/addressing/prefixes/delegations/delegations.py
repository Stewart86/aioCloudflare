from aiocloudflare.commons.auth import Auth


class Delegations(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "addressing/prefixes"
    _endpoint3 = "delegations"
