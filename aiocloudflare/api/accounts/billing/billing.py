from aiocloudflare.commons.unused import Unused

from .profile.profile import Profile


class Billing(Unused):
    _endpoint1 = "accounts"
    _endpoint2 = "billing"
    _endpoint3 = None

    @property
    def profile(self) -> Profile:
        return Profile(self._config, self._session)
