from pandaq import utils
from pandaq.vtypes.base import ValueType


class DateTimes(ValueType):
    def to_str(self) -> str:
        return f"{self.k}=={utils.dtime_to_str(self.v)}"
