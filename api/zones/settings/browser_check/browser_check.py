from api.commons.auth import Auth


class BrowserCheck(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "settings/browser_check"
    _endpoint3 = None
