from pandaq.vtypes.base import ValueType


class Number(ValueType):
    def to_str(self) -> str:
        return f"{self.k}=={self.v}"
