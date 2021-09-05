from aiocloudflare.commons.auth import Auth

# Extracted this from python-cloudflare but not sure that it really do
# skipping it for now and any call with use will be the same as `Auth`


class AuthUnwrapped(Auth):
    def __repr__(self) -> str:
        return f"derived from: AuthUnwrapped, class: {self.__class__.__name__}"
