from api.commons.unused import Unused

from .access_requests.access_requests import AccessRequests


class Logs(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "access/logs"
    _endpoint3 = None

    @property
    def access_requests(self):
        return AccessRequests()
