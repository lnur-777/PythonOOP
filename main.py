from transaction import Transaction
from income import Income
from expense import Expense
from subscription import Subscription
from wallet import Wallet


if __name__ == "__main__":
    wallet = Wallet("Alex", "4169-XXXX-XXXX-1234")

    t1 = Income("Salary", 2000)
    t2 = Expense("Groceries", 150, "Food")
    t3 = Subscription.from_yearly("Netflix Annual Plan", 120)

    wallet.add_transaction(t1)
    wallet.add_transaction(t2)
    wallet.add_transaction(t3)

    print(f"\n--- Wallet for {wallet.owner} (Card: {wallet.card.card_number}) ---")
    for tx in wallet.transactions:
        print(tx)

    print(f"\nTotal transactions: {len(wallet)}")
    print(f"Is Salary greater than Groceries? {t1 > t2}")
    print(f"Final Balance: {wallet.get_balance():.2f} {Transaction.currency}")
