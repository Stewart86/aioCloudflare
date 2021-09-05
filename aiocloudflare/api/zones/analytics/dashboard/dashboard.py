from aiocloudflare.commons.auth import Auth


class Dashboard(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "analytics/dashboard"
    _endpoint3 = None
