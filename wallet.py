from card import VirtualCard


class Wallet:
    def __init__(self, owner, card_number):
        self.owner = owner
        self.card = VirtualCard(card_number)
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        transaction.print_log()

    def get_balance(self):
        total = 0
        for tx in self.transactions:
            total += tx.get_impact()
        return total

    def __len__(self):
        return len(self.transactions)
