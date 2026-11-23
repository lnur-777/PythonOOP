from transaction import Transaction


class Expense(Transaction):
    def __init__(self, title, amount, category):
        super().__init__(title, amount)
        self.category = category

    def get_impact(self):
        return -self.amount

    def __str__(self):
        return f"{super().__str__()} ({self.category})"
