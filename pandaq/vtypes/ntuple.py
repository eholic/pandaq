from pandaq.vtypes.base import ValueType
from pandaq import utils

import datetime as dt


class NTuple(ValueType):
    def to_str(self) -> str:
        n_pairs, remain = divmod(len(self.v), 2)
        if n_pairs == 0 or remain == 1:
            raise ValueError(
                "Tuple argument must be pairs of `operator` and `value`. "
                "(`opr`, `val`, `opr`, `val`, ...) "
                "e.g. ('>=', 1, '<' 5)"
            )

        res = []
        for i in range(n_pairs):
            opr = self.v[2 * i]
            val = self.v[2 * i + 1]
            if isinstance(val, (dt.date, dt.datetime)):
                val = utils.dtime_to_str(val)
            res.append(f"{self.k}{opr}{val}")

        return utils.join_and(res)
