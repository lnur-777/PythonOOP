"""
Mixins module providing reusable cross-cutting functionality via Multiple Inheritance.
"""

from datetime import datetime
from typing import Any


class AuditMixin:
    """Provides creation timestamp functionality to any class that inherits it."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_audit_log(self) -> str:
        """Returns a formatted creation timestamp string."""
        return f"[Created at {self.created_at}]"
