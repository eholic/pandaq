"""pandaq: An easy pandas query builder."""
from __future__ import annotations

import datetime as dt
from typing import Any

from pandaq import utils, vtypes


class Q(str):
    """A class used to build a query string from a list of conditions.

    Attributes:
        _qlist (list): A list of conditions to be joined into a query string.
    """

    def __new__(cls, qlist: list[str] | None = None):
        """Constructs a new Query instance by joining the conditions in qlist into a query string.

        Args:
            qlist: A list of conditions to be joined into a query string. Defaults to None, which implies an empty list.
        """
        _qlist = qlist or []
        query = utils.join_and(_qlist, no_paren=True)
        self = str.__new__(cls, query)
        self._qlist = _qlist
        return self

    def __init__(self, _: list[str] | None = None):
        super().__init__()
        self._qlist: list[str]

    def q(self, *args, **kwargs) -> str:
        """Converts args to the query string of pd.DataFrame.query.

        Args:
            *args: Single dict on behalf of keyword arguments.
            **kwargs: Keyword arguments.

        Returns:
            A query string of pd.DataFrame.query.
        """
        if len(args) == 0:
            qdict = kwargs
        elif len(args) == 1 and isinstance(args[0], dict):
            arg_dict = {}
            for k, v in args[0].items():
                arg_dict[f"`{k}`"] = v
            qdict = {**arg_dict, **kwargs}
        else:
            msg = "argument must be single dict or keyword arguments."
            raise TypeError(msg)
        self._qlist.append(self._qdict_to_str(qdict))
        return Q(self._qlist)

    @staticmethod
    def _qdict_to_str(qdict: dict) -> str:
        """Converts a dictionary to a query string.

        Args:
            qdict (dict): A dictionary of conditions to be converted into a query string.

        Returns:
            A query string.
        """
        qlist = []
        for k, v in qdict.items():
            qlist.append(Q._qval_to_query(k, v))
        return utils.join_and(qlist)

    @staticmethod
    def _qval_to_query(k: str, v: Any) -> str:
        """Converts a key-value pair to a query string.

        Args:
            k: The key of the condition.
            v: The value of the condition.

        Returns:
            A query string.
        """
        if isinstance(v, list):
            return utils.join_or([Q._qval_to_query(k, _v) for _v in v])

        type_to_class = {
            str: vtypes.String,
            bool: vtypes.Boolean,
            int: vtypes.Number,
            float: vtypes.Number,
            dt.date: vtypes.DateTimes,
            dt.datetime: vtypes.DateTimes,
            tuple: vtypes.NTuple,
        }
        return type_to_class[type(v)](k, v).to_str()
