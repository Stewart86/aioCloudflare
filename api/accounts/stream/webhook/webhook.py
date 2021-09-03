from api.commons.auth import Auth


class Webhook(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "stream/webhook"
    _endpoint3 = None
