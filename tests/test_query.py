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


@pytest.fixture(scope="session")
def sample():
    return pd.DataFrame({
        'A': range(6),
        'B B': [i*0.1 for i in range(6)],
        'C': [True, True, True, False, False, False],
        'D': pd.DatetimeIndex(["1977-05-25", "1980-05-21", "1983-05-25", "1999-05-19", "2002-05-16", "2005-05-19"]),
        'E': ["May", "the", "force", "be", "with", "you."],
    })


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
        ({"datetime": dt.datetime(2019, 5, 7, 2, 0, 0)}, 1),
    ]
)
def test_q_air(qdict, expected, air):
    query = Q().q(**qdict)
    assert air.query(query).shape[0] == expected

    query = Q().q(qdict)
    assert air.query(query).shape[0] == expected


@pytest.mark.parametrize(
    "qdict,expected",
    [
        ({"C": True}, 3),
        ({"C": False}, 3),
        ({"C": False}, 3),
    ],
)
def test_q_sample(qdict, expected, sample):
    query = Q().q(**qdict)
    assert sample.query(query).shape[0] == expected

    query = Q().q(qdict)
    assert sample.query(query).shape[0] == expected
