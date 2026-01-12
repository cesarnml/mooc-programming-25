# Write your solution here:

from numbers import Real


class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, other: "RealProperty"):
        return self.square_metres > other.square_metres

    def price_difference(self, other: "RealProperty"):
        return abs(
            self.price_per_sqm * self.square_metres
            - other.square_metres * other.price_per_sqm
        )

    def more_expensive(self, other: "RealProperty"):
        difference = (
            self.price_per_sqm * self.square_metres
            - other.square_metres * other.price_per_sqm
        )
        return difference > 0
