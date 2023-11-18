from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ValueType(ABC):
    def __init__(self, k: str, v: Any):
        self.k = k
        self.v = v

    @abstractmethod
    def to_str(self) -> str:
        pass
