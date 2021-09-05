from aiocloudflare.commons.auth import Auth


class OpportunisticOnion(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/opportunistic_onion"
    _endpoint3 = None
