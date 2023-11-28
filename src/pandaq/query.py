"""pandaq: An easy pandas query builder."""
from __future__ import annotations

import datetime as dt
from typing import Any

from pandaq import utils, vtypes


class Q(str):
    """A class used to build a query string from a list of conditions.

    Attributes:
        _qchain (list): A list of conditions to be joined into a query string.
    """

    def __new__(cls, qchain: list[str] | None = None):
        """Constructs a new Query instance by joining the conditions in qchain into a query string.

        Args:
            qchain: A list of conditions to be joined into a query string. Defaults to None, which implies an empty list.
        """
        _qchain = qchain or []
        query = utils.join_and(_qchain, no_paren=True)
        self = str.__new__(cls, query)
        self._qchain = _qchain
        return self

    def __init__(self, _: list[str] | None = None):
        super().__init__()
        self._qchain: list[str]

    def q(self, *args, **kwargs) -> str:
        """Converts args to the query string of pd.DataFrame.query.

        Args:
            *args: Single dict on behalf of keyword arguments.
            **kwargs: Keyword arguments.

        Returns:
            A query string of pd.DataFrame.query.
        """
        if len(args) == 0:
            self._qchain.append(self._qdict_to_str(kwargs))
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                # Just pass through the string to pd.DataFrame.query
                self._qchain.append(arg)
            elif isinstance(arg, dict):
                qdict = {f"`{k}`": v for k, v in arg.items()}
                qdict.update(kwargs)
                self._qchain.append(self._qdict_to_str(qdict))
            else:
                raise TypeError("Single argument must be a q-string or dict.")
        else:
            msg = "Argument must be a q-string or single dict or keyword arguments."
            raise TypeError(msg)

        return Q(self._qchain)

    @staticmethod
    def _qdict_to_str(qdict: dict) -> str:
        """Converts a dictionary to a query string.

        Args:
            qdict (dict): A dictionary of conditions to be converted into a query string.

        Returns:
            A query string.
        """
        qchain = []
        for k, v in qdict.items():
            qchain.append(Q._qval_to_query(k, v))
        return utils.join_and(qchain)

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
