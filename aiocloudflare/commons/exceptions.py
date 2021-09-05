class AuthenticationError(Exception):
    """Authentication related errors"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
