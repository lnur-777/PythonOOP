"""
Ledger container demonstrating Composition, Aggregation, and Container Magic Methods.
"""

from typing import Iterator, List

from tracker.base import Transaction
from tracker.storage import StorageBackend


class FinanceLedger:
    """
    Aggregates Transaction objects and uses Composition with a StorageBackend.
    Implements container magic methods (__len__, __iter__, __getitem__).
    """

    def __init__(self, owner: str, storage: StorageBackend) -> None:
        self.owner: str = owner
        self._storage: StorageBackend = storage        # Composition (HAS-A storage engine)
        self._transactions: List[Transaction] = []     # Aggregation (HAS-MANY transactions)

    def add(self, transaction: Transaction) -> None:
        """Adds a transaction to the ledger."""
        self._transactions.append(transaction)

    @property
    def current_balance(self) -> float:
        """Calculates current net balance using polymorphic net_impact()."""
        return round(sum(tx.net_impact() for tx in self._transactions), 2)

    @property
    def projected_annual_expenses(self) -> float:
        """Calculates total projected annual expenses across one-time and recurring items."""
        return round(
            sum(
                abs(tx.annual_projection())
                for tx in self._transactions
                if tx.net_impact() < 0
            ),
            2,
        )

    def export_report(self) -> None:
        """Exports the current ledger state through the configured storage backend."""
        payload = {
            "owner": self.owner,
            "current_balance": self.current_balance,
            "projected_annual_expenses": self.projected_annual_expenses,
            "transaction_count": len(self),
            "transactions": [tx.to_dict() for tx in self._transactions],
        }
        self._storage.save(payload)

    # Container Magic Methods
    def __len__(self) -> int:
        return len(self._transactions)

    def __iter__(self) -> Iterator[Transaction]:
        return iter(self._transactions)

    def __getitem__(self, index: int) -> Transaction:
        return self._transactions[index]
