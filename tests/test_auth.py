import httpx
import pytest

from aiocloudflare.cloudflare import Cloudflare
from aiocloudflare.commons.auth import _Auth
from aiocloudflare.commons.config import Config
from aiocloudflare.commons.exceptions import AuthenticationError


def test__auth():
    email = "test@gmail.com"
    token = "abcde"  # noqa # for testing only
    _auth = _Auth(email, token)

    assert _auth._email == email
    assert _auth._token == token


@pytest.mark.asyncio
async def test_auth_init(respx_mock):
    respx_mock.get("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.delete("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.put("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.post("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.patch("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    base_url = "https://api.doesnotmatter.com"
    config = Config(base_url=base_url)
    config.EMAIL = "test@test.com"
    config.TOKEN = None
    async with Cloudflare(config=config) as cf:
        with pytest.raises(AuthenticationError) as error:
            await cf.zones.get()
            assert error.errisinstance(AuthenticationError)
            assert error.value("Token is required.")

    config.EMAIL = None
    async with Cloudflare(config=config) as cf:
        with pytest.raises(AuthenticationError) as error:
            await cf.zones.get()
            assert error.errisinstance(AuthenticationError)
            assert error.value("Email and token cannot be None.")

    config.TOKEN = "abc"
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.get()
        assert result.status_code == 200

    config.EMAIL = "abc@def.com"
    config.TOKEN = "abc"
    async with Cloudflare(config=config) as cf:
        result = await cf.zones.get()
        assert result.status_code == 200


@pytest.mark.asyncio
async def test_auth(respx_mock, config):
    respx_mock.get("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.delete("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.put("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.post("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    respx_mock.patch("https://api.doesnotmatter.com/zones").mock(
        return_value=httpx.Response(200)
    )
    async with Cloudflare(config=config) as cf:

        result = await cf.zones.get()
        assert result.status_code == 200

        result = await cf.zones.post()
        assert result.status_code == 200

        result = await cf.zones.patch()
        assert result.status_code == 200

        result = await cf.zones.put()
        assert result.status_code == 200

        result = await cf.zones.delete()
        assert result.status_code == 200
