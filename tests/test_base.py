import pytest
from httpx import AsyncClient

from aiocloudflare.commons.base import BaseClient
from aiocloudflare.commons.config import Config


@pytest.mark.parametrize(
    ["endpoints", "args", "expected"],
    [
        [("zone", None, None), (None,), "zone"],
        [("zone", "settings", None), ("id1",), "zone/id1/settings"],
        [("zone", "settings", None), ("id1", "id2"), "zone/id1/settings/id2"],
        [("zone", "a/b/c", None), ("id1",), "zone/id1/a/b/c"],
        [("zone", "settings", "hello"), ("id1",), "zone/id1/settings/hello"],
        [("zone", "a/b/c", "rule"), ("id1", "id2"), "zone/id1/a/b/c/id2/rule"],
        [
            ("zone", "a/b/c", "rule"),
            ("id1", "id2", "id3"),
            "zone/id1/a/b/c/id2/rule/id3",
        ],
    ],
)
def test_base_build_endpoint(endpoints, args, expected):
    config = Config()
    session = AsyncClient()
    base = BaseClient(config, session)

    base._endpoint1, base._endpoint2, base._endpoint3 = endpoints

    args = [i for i in [*args] if i is not None]

    result = base.build_endpoint("get", *args)
    assert result == expected


def test_base_build_endpoint_with_data():
    config = Config()
    session = AsyncClient()
    base = BaseClient(config, session)

    base._endpoint1, base._endpoint2, base._endpoint3 = "zone", "settings", None

    args = [i for i in ["id1"] if i is not None]

    result = base.build_endpoint("get", *args, data={"a": "b"})
    assert result == "zone/id1/settings"


def test_base_build_endpoint_with_raises():
    config = Config()
    session = AsyncClient()
    base = BaseClient(config, session)

    base._endpoint1, base._endpoint2, base._endpoint3 = "zone", "settings", None

    args = [i for i in [] if i is not None]

    with pytest.raises(ValueError) as raises:
        base.build_endpoint("get", *args)
        assert raises.errisinstance(ValueError)
        assert raises.value == "args cannot be None"
