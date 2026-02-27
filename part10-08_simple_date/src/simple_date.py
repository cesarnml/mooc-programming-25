# WRITE YOUR SOLUTION HERE:


class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other: "SimpleDate"):
        return (
            self.day == other.day
            and self.month == other.month
            and self.year == other.year
        )

    def __ne__(self, other: "SimpleDate"):
        return not self.__eq__(other)

    def __lt__(self, other: "SimpleDate"):
        return (
            self.day + self.month * 30 + self.year * 360
            < other.day + other.month * 30 + other.year * 360
        )

    def __gt__(self, other):
        return (
            self.day + self.month * 30 + self.year * 360
            > other.day + other.month * 30 + other.year * 360
        )

    def __add__(self, add_days: int):
        n_days = add_days % 30
        n_months = (add_days // 30) % 12
        n_years = add_days // 360

        days = (self.day + n_days) % 30
        months = (self.month + n_months + (self.day + n_days) // 30) % 12
        years = (
            self.year
            + n_years
            + (self.month + n_months + (self.day + n_days) // 30) // 12
        )
        return SimpleDate(days, months, years)

    def __sub__(self, other: "SimpleDate"):
        return abs(
            self.year * 360
            + self.month * 30
            + self.day
            - other.year * 360
            - other.month * 30
            - other.day
        )
