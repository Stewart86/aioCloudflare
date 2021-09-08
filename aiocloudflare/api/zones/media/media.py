from aiocloudflare.commons.auth import Auth

from .embed.embed import Embed
from .preview.preview import Preview


class Media(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "media"
    _endpoint3 = None

    @property
    def preview(self) -> Preview:
        return Preview(self._config, self._session)

    @property
    def embed(self) -> Embed:
        return Embed(self._config, self._session)
