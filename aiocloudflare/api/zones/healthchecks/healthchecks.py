from aiocloudflare.commons.auth import Auth

from .preview.preview import Preview


class Healthchecks(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "healthchecks"
    _endpoint3 = None

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)
