"""Patch pandas DataFrame with the new method `q`.

Example:
    >>> import pandas as pd
    >>> from pandaq import Q
    >>> df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    >>> df.q(a=1)
       a  b
    0  1  4
"""
from pandas import DataFrame

from pandaq.query import Q


def _q(self: DataFrame, *args, **kwargs):
    """Pass args as the query string of pd.DataFrame.query."""
    return self.query(Q().q(*args, **kwargs))


# Add the new method `q` to the pandas DataFrame class.
DataFrame.q = _q
