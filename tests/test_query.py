import datetime as dt

import pandas as pd
import pytest

from pandaq import Q


@pytest.fixture(scope="session")
def titanic():
    return pd.read_csv("tests/data/titanic.csv")


@pytest.fixture(scope="session")
def air():
    return pd.read_csv("tests/data/air_quality_no2.csv")


@pytest.mark.parametrize(
    "qdict,expected",
    [
        ({"PassengerId": 1}, 1),
        ({"Survived": 1}, 342),
        ({"Pclass": [1, 2]}, 400),
        ({"Name": "?James"}, 24),
        ({"Name": "?James", "Sex": "female"}, 4),
        ({"Name": "?James", "Sex": "!female"}, 20),
        ({"Name": "?James", "Sex": "!female", "Age": (">", 50)}, 3),
        ({"Name": "?James", "Sex": "!female", "Fare": (">", 20)}, 6),
        ({"Name": "?James", "Sex": "!female", "Fare": (">", 20, "<=", 26)}, 3),
        ({"Fare": [(">", 500), ("<", 5)]}, 19),
        ({"Name": "/Birkhardt|Johnston"}, 4),
        ({"Cabin": ["C70", "C124"]}, 3),
    ],
)
def test_q_titanic(qdict, expected, titanic):
    query = Q().q(**qdict)
    assert titanic.query(query).shape[0] == expected

    query = Q().q(qdict)
    assert titanic.query(query).shape[0] == expected


def test_q_wrong_arg():
    with pytest.raises(Exception):
        Q().q(1)

    with pytest.raises(Exception):
        Q().q(1, 1)


@pytest.mark.parametrize(
    "qdict,expected",
    [
        ({"datetime": ("<", dt.date(2019, 5, 8))}, 22),
        ({"datetime": (
            "<", dt.date(2019, 5, 8),
            ">", dt.datetime(2019, 5, 7, 20, 0, 0))}, 3),
    ]
)
def test_q_air(qdict, expected, air):
    query = Q().q(**qdict)
    assert air.query(query).shape[0] == expected

    query = Q().q(qdict)
    assert air.query(query).shape[0] == expected
