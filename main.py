"""
Application entry point for the Personal Finance & Subscription Tracker.
"""

from pathlib import Path

from tracker import (
    Expense,
    FinanceLedger,
    Income,
    JsonStorage,
    SubscriptionExpense,
)


def main() -> None:
    report_path = Path(__file__).parent / "finance_report.json"
    storage = JsonStorage(report_path)
    ledger = FinanceLedger(owner="Alex Morgan", storage=storage)

    # Add polymorphic transactions
    ledger.add(Income("Software Engineering Salary", 3500.00, "USD"))
    ledger.add(Income("Freelance Consulting", 600.00, "USD"))
    ledger.add(Expense("Grocery Shopping", 185.50, category="Food"))
    ledger.add(Expense("Mechanical Keyboard", 140.00, category="Hardware"))
    ledger.add(SubscriptionExpense("Cloud Server Hosting", 25.00))

    # Using @classmethod alternative constructor
    ledger.add(SubscriptionExpense.from_annual_plan("JetBrains IDE License", 144.00))

    print(f"=== Financial Ledger for {ledger.owner} ===")
    print(f"Total Transactions: {len(ledger)}\n")

    # Sorting works automatically thanks to Transaction.__lt__
    for tx in sorted(ledger, reverse=True):
        print(f"  {tx:<52} {tx.get_audit_log()}")

    print("\n--- Summary ---")
    print(f"Current Balance           : {ledger.current_balance:.2f} USD")
    print(f"Projected Annual Expenses : {ledger.projected_annual_expenses:.2f} USD")

    ledger.export_report()
    print(f"\nReport exported to: {report_path.name}")


if __name__ == "__main__":
    main()
