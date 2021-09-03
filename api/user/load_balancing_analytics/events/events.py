from api.commons.auth import Auth


class Events(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "user/load_balancing_analytics/events"
    _endpoint2 = None
    _endpoint3 = None
