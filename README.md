# Personal Finance & Subscription Tracker (Pure Python OOP)

A modular, pure-Python personal finance and subscription tracking application designed to demonstrate core and Python-specific Object-Oriented Programming (OOP) principles.

## Project Structure

```text
oop_finance_tracker/
├── main.py                # Application entry point
└── tracker/               # Core package
    ├── __init__.py        # Public package exports
    ├── mixins.py          # AuditMixin (Multiple Inheritance)
    ├── base.py            # Transaction (Abstraction, Encapsulation, Dunder methods)
    ├── models.py          # Income, Expense, SubscriptionExpense (Inheritance & Polymorphism)
    ├── storage.py         # StorageBackend (ABC) & JsonStorage
    └── ledger.py          # FinanceLedger (Composition, Aggregation, Container Dunders)
```

## OOP Concepts Demonstrated

- **Abstraction**: `Transaction` and `StorageBackend` inherit from `abc.ABC` and define required `@abstractmethod` interfaces.
- **Encapsulation**: Protected (`_title`) and private (`__amount`) attributes with validation enforced through `@property` getters and setters.
- **Inheritance**:
  - *Single & Multilevel Inheritance*: `Transaction` -> `Expense` -> `SubscriptionExpense`
  - *Multiple Inheritance (Mixin)*: `Transaction(AuditMixin, ABC)`
- **Polymorphism**: Subclasses override `net_impact()`, `annual_projection()`, `to_dict()`, and `__str__()`.
- **Class & Static Methods**:
  - `@staticmethod`: `Transaction.is_valid_currency()`
  - `@classmethod`: `SubscriptionExpense.from_annual_plan()` alternative constructor
- **Magic / Dunder Methods**:
  - Representation & sorting: `__str__`, `__repr__`, `__lt__`
  - Container protocol on `FinanceLedger`: `__len__`, `__iter__`, `__getitem__`
- **Composition & Aggregation**: `FinanceLedger` is composed of a `StorageBackend` and aggregates `Transaction` instances.

## Usage

Run the application with Python 3.8+:

```bash
python main.py
```
