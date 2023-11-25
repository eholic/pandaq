from dataclasses import dataclass, fields

from pandaq import config
from pandaq.vtypes.base import ValueType


class String(ValueType):
    def to_str(self) -> str:
        prefix = config.str_prefix or StringPrefix()
        pfx, text = prefix.splitprefix(self.v)

        # Map prefixes to their corresponding string formats
        prefix_map = {
            prefix.neq: f'{self.k}!="{text}"',
            prefix.regex: f'{self.k}.str.contains("{text}", regex=True, na=False)',
            prefix.partial: f'{self.k}.str.contains("{text}", regex=False, na=False)',
            prefix.neq_partial: f'not {self.k}.str.contains("{text}", regex=False, na=False)',
        }

        # Return the string format for the given prefix, or the default format if the prefix is not recognized
        return prefix_map.get(pfx, f'{self.k}=="{text}"')


@dataclass
class StringPrefix:
    """Class for handling string prefixes."""

    neq: str = "!"
    regex: str = "/"
    partial: str = "?"
    neq_partial: str = "!?"

    def _prefixes(self):
        """Get a list of all prefixes."""
        pfxs = [getattr(self, f.name) for f in fields(self)]
        if len(pfxs) != len(set(pfxs)):
            msg = "prefixes must be unique."
            raise Exception(msg)
        return pfxs

    def splitprefix(self, text: str):
        """Split a text into a prefix and the remaining text.

        This method splits a text into a prefix and the remaining text.
        If the text does not start with a prefix, it returns None for the prefix.

        Args:
            text: The text to split.

        Returns:
            A tuple containing the prefix and the remaining text.
        """
        pfxs = self._prefixes()
        pfxs.sort(key=len, reverse=True)
        for prefix in pfxs:
            if text.startswith(prefix):
                return prefix, text.removeprefix(prefix)
        return None, text
