# WRITE YOUR SOLUTION HERE:
# typo
class WeatherStation:
    def __init__(self, name):
        self.__name = name
        self.__observations: list[str] = []

    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        if len(self.__observations) > 0:
            return self.__observations[-1]
        else:
            return ""

    def number_of_observations(self):
        return len(self.__observations)
