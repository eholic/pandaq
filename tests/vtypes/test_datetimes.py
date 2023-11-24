import datetime as dt

from pandaq import utils
from pandaq.vtypes import DateTimes


def test_to_str():
    dtime = dt.date(1970, 1, 1)
    assert DateTimes("a", dtime).to_str() == f"a=={utils.dtime_to_str(dtime)}"
