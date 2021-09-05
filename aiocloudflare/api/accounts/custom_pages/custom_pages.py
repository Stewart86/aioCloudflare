from aiocloudflare.commons.auth import Auth


class CustomPages(Auth):
    _endpoint1 = "accounts"
    _endpoint2 = "custom_pages"
    _endpoint3 = None
