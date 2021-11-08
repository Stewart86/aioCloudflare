from aiocloudflare.commons.unused import Unused

from .history.history import History
from .profile.profile import Profile
from .subscriptions.subscriptions import Subscriptions


class Billing(Unused):
    _endpoint1 = "user/billing"
    _endpoint2 = None
    _endpoint3 = None

    @property
    def history(self) -> History:
        return History(self._config, self._session)

    @property
    def profile(self) -> Profile:
        return Profile(self._config, self._session)

    @property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._config, self._session)
