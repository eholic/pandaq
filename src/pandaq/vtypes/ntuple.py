import datetime as dt

from pandaq import utils
from pandaq.vtypes.base import ValueType


class NTuple(ValueType):
    def to_str(self) -> str:
        n_pairs, remain = divmod(len(self.v), 2)
        if n_pairs == 0 or remain == 1:
            msg = (
                "Tuple argument must be pairs of `operator` and `value`. "
                "(`opr`, `val`, `opr`, `val`, ...) "
                "e.g. ('>=', 1, '<' 5)"
            )
            raise ValueError(msg)

        res = []
        for opr, val in zip(self.v[::2], self.v[1::2]):
            if isinstance(val, (dt.date, dt.datetime)):
                val = utils.dtime_to_str(val)
            res.append(f"{self.k}{opr}{val}")

        return utils.join_and(res)
