from pandaq.vtypes.base import ValueType
from pandaq import config
from dataclasses import dataclass, fields


class String(ValueType):
    def to_str(self) -> str:
        prefix = config.str_prefix or StringPrefix()
        pfx, text = prefix.splitprefix(self.v)

        if pfx == prefix.neq:
            return f'{self.k}!="{text}"'
        elif pfx == prefix.regex:
            return f'{self.k}.str.contains("{text}", regex=True, na=False)'
        elif pfx == prefix.partial:
            return f'{self.k}.str.contains("{text}", regex=False, na=False)'
        elif pfx == prefix.neq_partial:
            return f'not {self.k}.str.contains("{text}", regex=False, na=False)'
        else:
            return f'{self.k}=="{text}"'


@dataclass
class StringPrefix:
    neq: str = "!"
    regex: str = "/"
    partial: str = "?"
    neq_partial: str = "!?"

    def _prefixes(self):
        pfxs = [getattr(self, f.name) for f in fields(self)]
        if len(pfxs) != len(set(pfxs)):
            raise Exception("prefixes must be unique.")
        return pfxs

    def splitprefix(self, text: str):
        pfxs = self._prefixes()
        pfxs.sort(key=len, reverse=True)
        for prefix in pfxs:
            if text.startswith(prefix):
                return prefix, text.removeprefix(prefix)
        return None, text
