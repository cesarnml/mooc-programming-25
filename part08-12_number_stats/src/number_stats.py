# Write your solution here!
class NumberStats:
    def __init__(self):
        self.count = 0
        self.total = 0

    def add_number(self, number: int):
        self.count += 1
        self.total += number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.total

    def average(self):
        if self.count == 0:
            return 0
        return self.total / self.count


stats = NumberStats()
numbers = NumberStats()
evens = NumberStats()
odds = NumberStats()

print("Please type in integer numbers:")
while True:
    num = int(input())
    if num == -1:
        break
    numbers.add_number(num)
    if num % 2 == 0:
        evens.add_number(num)
    else:
        odds.add_number(num)

print(
    f"Sum of numbers: {numbers.get_sum()} Mean of numbers: {numbers.average()} Sum of even numbers: {evens.get_sum()} Sum of odd numbers: {odds.get_sum()}"
)
