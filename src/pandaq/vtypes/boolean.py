from pandaq.vtypes.base import ValueType


class Boolean(ValueType):
    def to_str(self) -> str:
        v = "True" if self.v else "False"

        return f"{self.k}=={v}"
