import pytest

from aiocloudflare.commons.config import Config


@pytest.fixture
def config():
    base_url = "https://api.doesnotmatter.com"
    return Config(email="test@test.com", token="token", base_url=base_url)  # noqa
