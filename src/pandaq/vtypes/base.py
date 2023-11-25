from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ValueType(ABC):
    """Abstract base class for value types.

    This class defines the interface for value types in the pandaq package.
    Each value type must implement the `to_str` method.

    Attributes:
        k: The key associated with the value.
        v: The value.

    Methods:
        to_str: Convert the value to a string. This method must be implemented by subclasses.
    """

    def __init__(self, k: str, v: Any):
        self.k = k
        self.v = v

    @abstractmethod
    def to_str(self) -> str:  # pragma: no cover
        """Convert the instance to a string.

        This method must be implemented by subclasses.

        Returns:
            The value as a string.
        """
        pass
