from aiocloudflare.commons.auth import Auth


class ImageResizing(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/image_resizing"
    _endpoint3 = None
