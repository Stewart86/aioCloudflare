from api.commons.auth import Auth

from .captions.captions import Captions
from .copy.copy import Copy
from .direct_upload.direct_upload import DirectUpload
from .embed.embed import Embed
from .keys.keys import Keys
from .preview.preview import Preview
from .watermarks.watermarks import Watermarks
from .webhook.webhook import Webhook


class Stream(Auth):
    _AUTH = "AUTH"
    _endpoint1 = "accounts"
    _endpoint2 = "stream"
    _endpoint3 = None

    @property
    def captions(self):
        return Captions()

    @property
    def copy(self):
        return Copy()

    @property
    def direct_upload(self):
        return DirectUpload()

    @property
    def embed(self):
        return Embed()

    @property
    def keys(self):
        return Keys()

    @property
    def preview(self):
        return Preview()

    @property
    def watermarks(self):
        return Watermarks()

    @property
    def webhook(self):
        return Webhook()
