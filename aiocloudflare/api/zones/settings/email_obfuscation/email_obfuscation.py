from aiocloudflare.commons.auth import Auth


class EmailObfuscation(Auth):
    _endpoint1 = "zones"
    _endpoint2 = "settings/email_obfuscation"
    _endpoint3 = None
