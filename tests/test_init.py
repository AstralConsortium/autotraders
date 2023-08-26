# import time

import pytest

from autotraders import get_status
from autotraders.agent import Agent
from autotraders.error import SpaceTradersException
from autotraders.faction import Faction
from autotraders.session import AutoTradersSession


@pytest.fixture
def session():
    s = AutoTradersSession("TEST")
    s.b_url = "https://stoplight.io/mocks/spacetraders/spacetraders/96627693/"  # Use http://127.0.0.1:4010/ for local mocking
    s.headers.update({"Prefer": "dynamic=true"})
    return s


def test_invalid_api_key():
    s = AutoTradersSession("INVALID TOKEN")
    try:
        Agent(s)
        assert False  # shouldn't complete successfully
    except Exception as e:
        assert type(e) is SpaceTradersException


def test_get_status():
    status = get_status()
    assert status.version == "v2"


# def test_rate_limiter(session):
#     t1 = time.time()
#     for i in range(20):
#         get_status()
#     t2 = time.time()
#     assert t2 - t1 < 100


def test_agent(session):
    Agent(session)


def test_faction(session):
    Faction.all(session)
