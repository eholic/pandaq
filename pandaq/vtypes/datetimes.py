from pandaq.vtypes.base import ValueType
from pandaq import utils


class DateTimes(ValueType):
    def to_str(self) -> str:
        return f"{self.k}=={utils.dtime_to_str(self.v)}"
