"""pandaq: An alternative pandas query."""
from __future__ import annotations

import datetime as dt
from typing import Any, Optional

from pandaq import utils, vtypes


class Q(str):
    """Query string builder."""
    def __new__(cls, qlist: Optional[list] = None):
        _qlist = qlist or []
        query = utils.join_and(_qlist, no_paren=True)
        self = str.__new__(cls, query)
        self._qlist = _qlist
        return self

    def __init__(self, _: Optional[list] = None):
        super().__init__()
        self._qlist: list[str]

    def q(self, *args, **kwargs):
        """Convert args to the query string of pd.DataFrame.query

        Args:
            *args:
            **kwargs:
        """
        if len(args) == 0:
            qdict = kwargs
        elif len(args) == 1 and isinstance(args[0], dict):
            arg_dict = {}
            for k, v in args[0].items():
                arg_dict[f"`{k}`"] = v
            qdict = {**arg_dict, **kwargs}
        else:
            raise Exception("argument must be single dict or keyword arguments.")
        self._qlist.append(self._qdict_to_str(qdict))
        return Q(self._qlist)

    @staticmethod
    def _qdict_to_str(qdict: dict):
        qlist = []
        for k, v in qdict.items():
            qlist.append(Q._qval_to_query(k, v))
        return utils.join_and(qlist)

    @staticmethod
    def _qval_to_query(k: str, v: Any):
        if isinstance(v, str):
            return vtypes.String(k, v).to_str()
        elif isinstance(v, bool):
            return vtypes.Boolean(k, v).to_str()
        elif isinstance(v, (int, float)):
            return vtypes.Number(k, v).to_str()
        elif isinstance(v, (dt.date, dt.datetime)):
            return vtypes.DateTimes(k, v).to_str()
        elif isinstance(v, tuple):
            return vtypes.NTuple(k, v).to_str()
        elif isinstance(v, list):
            return utils.join_or([Q._qval_to_query(k, _v) for _v in v])
