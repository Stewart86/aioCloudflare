from api.commons.auth import Auth


class Bytime(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "spectrum/analytics/events/bytime"
    _endpoint3 = None
