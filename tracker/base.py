"""
Abstract base classes and encapsulation logic for financial transactions.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict

from tracker.mixins import AuditMixin


class Transaction(AuditMixin, ABC):
    """
    Abstract base class representing a financial transaction.
    Demonstrates Multiple Inheritance (AuditMixin + ABC), Abstraction,
    Encapsulation (@property), Static Methods, and Magic Methods.
    """

    # Class attribute shared across all instances
    SUPPORTED_CURRENCIES = ("USD", "EUR", "AZN")

    def __init__(self, title: str, amount: float, currency: str = "USD") -> None:
        super().__init__()
        if not self.is_valid_currency(currency):
            raise ValueError(f"Unsupported currency: {currency}")

        self._title: str = title.strip()          # Protected attribute
        self.__amount: float = 0.0                # Private attribute (name-mangled)
        self.amount = amount                      # Validated via @amount.setter
        self.currency: str = currency.upper()

    # Encapsulation: Read-only property for protected attribute
    @property
    def title(self) -> str:
        return self._title

    # Encapsulation: Getter for private __amount
    @property
    def amount(self) -> float:
        return self.__amount

    # Encapsulation: Setter with validation logic
    @amount.setter
    def amount(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Transaction amount must be strictly positive.")
        self.__amount = round(float(value), 2)

    # Static method: utility helper independent of class or instance state
    @staticmethod
    def is_valid_currency(currency: str) -> bool:
        return currency.upper() in Transaction.SUPPORTED_CURRENCIES

    # Abstract methods: subclasses MUST implement these
    @abstractmethod
    def net_impact(self) -> float:
        """Returns the signed impact on the account balance."""
        pass

    @abstractmethod
    def annual_projection(self) -> float:
        """Projects the impact of this transaction over 12 months."""
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the transaction to a dictionary."""
        return {
            "type": self.__class__.__name__,
            "title": self.title,
            "amount": self.amount,
            "currency": self.currency,
            "created_at": self.created_at,
        }

    # Magic / Dunder methods for string representation and comparison
    def __str__(self) -> str:
        sign = "+" if self.net_impact() >= 0 else "-"
        return f"{sign}{self.amount:.2f} {self.currency} | {self.title}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title={self.title!r}, amount={self.amount})"

    def __lt__(self, other: "Transaction") -> bool:
        """Enables sorting transactions by their absolute amount."""
        if not isinstance(other, Transaction):
            return NotImplemented
        return self.amount < other.amount
