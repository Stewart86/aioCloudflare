from aiocloudflare.commons.auth import Auth


class ChallengeTtl(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/challenge_ttl"
    _endpoint3 = None
