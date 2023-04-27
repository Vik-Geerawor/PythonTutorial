from random import randint

"""
static methods are ordinary functions grouped in a class
they don't take 'self' or 'cls' as their first arg
their classes are not instantiated
they are called like class methods
"""


class StandardPolicy:
    @staticmethod
    def deposit(account, amount):
        account.balance += amount

    @staticmethod
    def withdraw(account, amount):
        account.balance -= amount

    @staticmethod
    def inquiry(account):
        return account.balance


class EvilPolicy(StandardPolicy):
    def __init__(self, deposit_factor, inquiry_factor):
        self.deposit_factor = deposit_factor
        self.inquiry_factor = inquiry_factor

    def deposit(self, account, amount):
        account.balance += self.deposit_factor * amount

    def inquiry(self, account):
        if randint(0, 4) == 1:
            return self.inquiry_factor * account.balance
        else:
            return account.balance


class Account:
    def __init__(self, owner, balance, *, policy=StandardPolicy):
        self.owner = owner
        self.balance = balance
        self.policy = policy

    def __repr__(self):
        return f'Account({self.policy}, {self.owner!r}, {self.balance!r})'

    def deposit(self, amount):
        self.policy.deposit(self, amount)

    def withdraw(self, amount):
        self.policy.withdraw(self, amount)

    def inquiry(self):
        return self.policy.inquiry(self)


if __name__ == '__main__':
    a = Account('Tom', 1000.0)
    print(f"{a.policy}")

    a.deposit(500)
    print(f"{a.inquiry()}")

    a.policy = EvilPolicy(0.95, 1.10)
    a.deposit(500)
    print(f"{a.inquiry()}")
