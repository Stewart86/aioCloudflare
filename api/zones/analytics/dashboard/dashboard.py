from api.commons.auth import Auth


class Dashboard(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "analytics/dashboard"
    _endpoint3 = None
