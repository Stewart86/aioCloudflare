from api.commons.auth import Auth


class PrivacyPass(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/privacy_pass"
    _endpoint3 = None
