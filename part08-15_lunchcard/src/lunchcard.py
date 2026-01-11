# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_lunch(self):
        lunch_cost = 2.60
        if self.balance >= lunch_cost:
            self.balance -= lunch_cost

    def eat_special(self):
        special_cost = 4.60
        if self.balance >= special_cost:
            self.balance -= special_cost

    def deposit_money(self, amount: int):
        if amount < 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        else:
            self.balance += amount


peter_card = LunchCard(20)
grace_card = LunchCard(30)
peter_card.eat_special()
grace_card.eat_lunch()
print(f"Peter: {peter_card}")
print(f"Grace: {grace_card}")
peter_card.deposit_money(20)
grace_card.eat_special()
print(f"Peter: {peter_card}")
print(f"Grace: {grace_card}")
peter_card.eat_lunch()
peter_card.eat_lunch()
grace_card.deposit_money(50)
print(f"Peter: {peter_card}")
print(f"Grace: {grace_card}")
