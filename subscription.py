from expense import Expense


class Subscription(Expense):
    def __init__(self, title, monthly_amount):
        super().__init__(title, monthly_amount, category="Subscription")

    @classmethod
    def from_yearly(cls, title, yearly_amount):
        return cls(title, yearly_amount / 12)
