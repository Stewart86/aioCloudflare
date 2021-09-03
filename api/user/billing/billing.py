from api.commons.unused import Unused

from .history.history import History
from .profile.profile import Profile
from .subscriptions.subscriptions import Subscriptions


class Billing(Unused):
    _AUTH = "VOID"
    _endpoint1 = "user/billing"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def history(self):
        return History()

    @property
    def profile(self):
        return Profile()

    @property
    def subscriptions(self):
        return Subscriptions()
