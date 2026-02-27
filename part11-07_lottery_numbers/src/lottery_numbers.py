# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week: int, lotto: list[int]):
        self.week = week
        self.lotto = lotto

    def number_of_hits(self, numbers: list[int]):
        return sum([1 if number in self.lotto else 0 for number in numbers])

    def hits_in_place(self, numbers: list[int]):
        return [num if num in self.lotto else -1 for num in numbers]
