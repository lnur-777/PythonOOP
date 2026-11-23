from abc import ABC, abstractmethod
from log_mixin import LogMixin


class Transaction(ABC, LogMixin):
    currency = "USD"

    def __init__(self, title, amount):
        self._title = title
        self.__amount = 0
        self.amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if not self.is_valid_amount(value):
            raise ValueError("Amount must be greater than zero.")
        self.__amount = value

    @staticmethod
    def is_valid_amount(value):
        return value > 0

    @classmethod
    def change_currency(cls, new_currency):
        cls.currency = new_currency

    @abstractmethod
    def get_impact(self):
        pass

    def __str__(self):
        sign = "+" if self.get_impact() > 0 else "-"
        return f"{self._title}: {sign}{self.amount:.2f} {self.currency}"

    def __gt__(self, other):
        return self.amount > other.amount
