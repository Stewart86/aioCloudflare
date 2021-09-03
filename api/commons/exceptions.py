class CloudflareMethodNotAvailable(Exception):
    """HTTP method not available for this endpoint"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)
