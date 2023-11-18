import datetime as dt

from pandaq import utils


def test_join_and():
    assert utils.join_and(["a"]) == "a"
    assert utils.join_and(["a", "b"]) == "(a & b)"
    assert utils.join_and(["a", "b"], no_paren=True) == "a & b"


def test_join_or():
    assert utils.join_or(["a"]) == "a"
    assert utils.join_or(["a", "b"]) == "(a | b)"
    assert utils.join_or(["a", "b"], no_paren=True) == "a | b"


def test_dtime_to_str():
    assert utils.dtime_to_str(dt.date(1970, 1, 2)) == '"1970-01-02"'
    assert (
        utils.dtime_to_str(dt.datetime(1970, 1, 2, 3, 4, 5)) == '"1970-01-02 03:04:05"'
    )
    assert (
        utils.dtime_to_str(dt.datetime(1970, 1, 2, 3, 4, 5, 6000))
        == '"1970-01-02 03:04:05.006000"'
    )
