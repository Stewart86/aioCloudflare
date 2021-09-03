from api.commons.auth import Auth


class OpportunisticEncryption(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/opportunistic_encryption"
    _endpoint3 = None
