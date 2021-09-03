from api.commons.auth import Auth


class HotlinkProtection(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/hotlink_protection"
    _endpoint3 = None
