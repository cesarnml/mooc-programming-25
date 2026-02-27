class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


# Write your solution here:
def sort_by_length(routes: list[ClimbingRoute]):
    def order_by_length(route: ClimbingRoute):
        return route.length

    return sorted(routes, key=order_by_length, reverse=True)


def sort_by_difficulty(routes: list[ClimbingRoute]):
    return sorted(routes, key=lambda r: (r.grade, r.length), reverse=True)
