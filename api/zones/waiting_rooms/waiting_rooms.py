from api.commons.auth import Auth


class WaitingRooms(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "waiting_rooms"
    _endpoint3 = None
