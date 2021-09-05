from aiocloudflare.commons.auth import Auth


class Order(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "ssl/certificate_packs/order"
    _endpoint3 = None
