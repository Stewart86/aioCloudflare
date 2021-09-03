from api.commons.auth import Auth


class Subscription(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "subscription"
    _endpoint3 = None
