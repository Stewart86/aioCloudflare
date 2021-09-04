from api.commons import auth

# Extracted this from python-cloudflare but not sure that it really do
# skipping it for now and any call with use will be the same as `Auth`


class AuthUnwrapped(auth):
    def __repr__(self) -> str:
        return f"derived from: AuthUnwrapped, class: {self.__class__.__name__}"
