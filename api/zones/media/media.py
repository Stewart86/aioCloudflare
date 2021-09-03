from api.commons.auth import Auth

from .embed.embed import Embed
from .preview.preview import Preview


class Media(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "zones"
    _endpoint2 = "media"
    _endpoint3 = None

    @property
    def embed(self):
        return Embed()

    @property
    def preview(self):
        return Preview()
