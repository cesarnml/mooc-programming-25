from xml.dom import minicompat


class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours + 1
                if self.hours == 23:
                    self.hours = 0

    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0
