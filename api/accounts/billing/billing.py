from api.commons.unused import Unused

from .profile.profile import Profile


class Billing(Unused):
    _AUTH = "VOID"
    _endpoint1 = "accounts"
    _endpoint2 = "billing"
    _endpoint3 = None

    @property
    def profile(self):
        return Profile()
