# WRITE YOUR SOLUTION HERE:


class Car:
    def __init__(self):
        self.__tank = 0
        self.__odometer = 0

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__tank} litres"

    def fill_up(self):
        self.__tank = 60

    def drive(self, km: int):
        can_drive = min(self.__tank, km)
        self.__odometer += can_drive
        self.__tank -= can_drive
