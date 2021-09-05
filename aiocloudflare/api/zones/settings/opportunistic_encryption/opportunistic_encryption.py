from aiocloudflare.commons.auth import Auth


class OpportunisticEncryption(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/opportunistic_encryption"
    _endpoint3 = None
