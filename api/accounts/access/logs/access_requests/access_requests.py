from api.commons.auth import Auth


class AccessRequests(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "access/logs/access_requests"
    _endpoint3 = None
