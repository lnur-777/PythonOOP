"""
Concrete transaction models demonstrating Inheritance, Polymorphism, and @classmethod.
"""

from typing import Any, Dict

from tracker.base import Transaction


class Income(Transaction):
    """Represents money coming into the account."""

    def net_impact(self) -> float:
        return self.amount

    def annual_projection(self) -> float:
        return self.amount


class Expense(Transaction):
    """Represents a one-time expense."""

    def __init__(
        self,
        title: str,
        amount: float,
        category: str = "General",
        currency: str = "USD",
    ) -> None:
        super().__init__(title, amount, currency)
        self.category: str = category

    def net_impact(self) -> float:
        return -self.amount

    def annual_projection(self) -> float:
        return -self.amount

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["category"] = self.category
        return data

    def __str__(self) -> str:
        return f"{super().__str__()} [{self.category}]"


class SubscriptionExpense(Expense):
    """
    Multilevel Inheritance: Transaction -> Expense -> SubscriptionExpense.
    Represents a recurring monthly subscription.
    """

    def __init__(self, title: str, monthly_fee: float, currency: str = "USD") -> None:
        super().__init__(title, monthly_fee, category="Subscription", currency=currency)

    # Polymorphism: overrides annual_projection to account for 12 monthly payments
    def annual_projection(self) -> float:
        return -(self.amount * 12)

    # Class method: alternative constructor from an annual price
    @classmethod
    def from_annual_plan(
        cls,
        title: str,
        annual_cost: float,
        currency: str = "USD",
    ) -> "SubscriptionExpense":
        monthly_equivalent = round(annual_cost / 12, 2)
        return cls(title=title, monthly_fee=monthly_equivalent, currency=currency)
