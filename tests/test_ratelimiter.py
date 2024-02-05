from datetime import datetime

from pytest_httpx import HTTPXMock

from autotraders import AutoTradersSession
from autotraders.agent import Agent

dummy_json = {
    "data": {
        "accountId": "string",
        "symbol": "string",
        "headquarters": "string",
        "credits": -9007199254740991,
        "startingFaction": "string",
        "shipCount": 0
    }
}


def test_ratelimiter_longspan(httpx_mock: HTTPXMock):
    httpx_mock.add_response(json=dummy_json)
    session = AutoTradersSession()

    start = datetime.now()
    for i in range(30):
        Agent(session)
    total = datetime.now() - start
    assert total.total_seconds() < 10


def test_ratelimiter_shortspan(httpx_mock: HTTPXMock):
    httpx_mock.add_response(json=dummy_json)
    session = AutoTradersSession()

    start = datetime.now()
    for i in range(12):
        Agent(session)
    total = datetime.now() - start
    assert total.total_seconds() < 1
