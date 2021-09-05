from aiocloudflare.commons.auth import Auth


class CustomPages(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "custom_pages"
    _endpoint3 = None
