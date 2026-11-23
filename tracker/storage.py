"""
Storage abstraction and JSON implementation for persisting ledger reports.
"""

from abc import ABC, abstractmethod
import json
from pathlib import Path
from typing import Any, Dict


class StorageBackend(ABC):
    """Abstract interface for persisting ledger data."""

    @abstractmethod
    def save(self, payload: Dict[str, Any]) -> None:
        """Persists the given dictionary payload."""
        pass


class JsonStorage(StorageBackend):
    """Concrete storage backend that writes ledger reports to a JSON file."""

    def __init__(self, file_path: Path) -> None:
        self.file_path: Path = file_path

    def save(self, payload: Dict[str, Any]) -> None:
        self.file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
