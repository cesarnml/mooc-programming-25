# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, owner: str, account_no: str, balance: float):
        self.__owner = owner
        self.__account_no = account_no
        self.__balance = 0
        if balance > 0:
            self.__balance = balance
        else:
            ValueError("balance cannot be negative")

    def __service_charge(self):
        fee = self.__balance * 0.01
        self.__balance -= fee

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        if amount >= 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("deposit amount must be positive")

    def withdraw(self, amount: float):
        if self.__balance > amount:
            self.__balance -= amount
            self.__service_charge()
        else:
            ValueError("balance insufficient")
