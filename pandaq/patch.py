from pandas import DataFrame
from pandaq.query import Q


def _q(self, *args, **kwargs):
    return self.query(Q().q(*args, **kwargs))


DataFrame.q = _q
