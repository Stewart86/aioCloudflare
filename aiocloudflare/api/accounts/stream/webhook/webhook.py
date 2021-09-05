from aiocloudflare.commons.auth import Auth


class Webhook(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "stream/webhook"
    _endpoint3 = None
