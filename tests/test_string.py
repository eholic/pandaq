import pytest

from pandaq import config
from pandaq.vtypes.string import StringPrefix
from pandaq.vtypes import String


def test_to_str():
    assert String("a", "text").to_str() == 'a=="text"'
    assert String("a", "!text").to_str() == 'a!="text"'
    assert String("a", "/text").to_str() == 'a.str.contains("text", regex=True, na=False)'
    assert String("a", "?text").to_str() == 'a.str.contains("text", regex=False, na=False)'
    assert String("a", "!?text").to_str() == 'not a.str.contains("text", regex=False, na=False)'


def test_prefix_duplicated():
    config.str_prefix = StringPrefix(regex="!")
    with pytest.raises(Exception):
        String("a", "text").to_str()
