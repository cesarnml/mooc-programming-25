class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (
            f"BallPlayer(name={self.name}, number={self.number}, "
            f"goals={self.goals}, passes={self.passes}, minutes={self.minutes})"
        )


def most_goals(players: list):
    return max(players, key=lambda p: p.goals).name


def most_points(players: list):
    best = max(players, key=lambda p: p.goals + p.passes)
    return (best.name, best.number)


def least_minutes(players: list):
    return min(players, key=lambda p: p.minutes)
