import pytest

from pandaq.vtypes import NTuple


def test_to_str():
    assert NTuple("a", (">=", 1)).to_str() == "a>=1"
    assert NTuple("a", (">=", 1, "<", 2)).to_str() == "(a>=1 & a<2)"


def test_to_str_raise():
    with pytest.raises(ValueError):
        NTuple("a", (">=",)).to_str()

    with pytest.raises(ValueError):
        NTuple("a", (">=", 1, "<")).to_str()
