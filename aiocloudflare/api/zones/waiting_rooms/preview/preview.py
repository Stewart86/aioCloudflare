from aiocloudflare.commons.auth import Auth


class Preview(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "waiting_rooms/preview"
    _endpoint3 = None
