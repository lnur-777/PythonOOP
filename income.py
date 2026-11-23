from transaction import Transaction


class Income(Transaction):
    def get_impact(self):
        return self.amount
