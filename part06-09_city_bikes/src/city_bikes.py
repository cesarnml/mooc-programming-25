# tee ratkaisu tänne
# Write your solution here
import math


def get_station_data(filename: str):
    stations = {}
    with open(filename) as file:
        for line in file:
            temp = line.split(";")
            if temp[0] == "Longitude":
                continue
            stations[temp[3]] = (float(temp[0]), float(temp[1]))
    return stations


def distance(stations: dict, station1: str, station2: str):
    x_factor = 55.26
    y_factor = 111.2

    station_one = stations[station1]
    station_two = stations[station2]

    x_km = (station_one[0] - station_two[0]) * x_factor
    y_km = (station_one[1] - station_two[1]) * y_factor

    return math.sqrt(x_km**2 + y_km**2)


def greatest_distance(stations: dict):
    farthest = 0
    output = ()
    for station1 in stations:
        for station2 in stations:
            dist = distance(stations, station1, station2)
            if dist > farthest:
                farthest = dist
                output = (station1, station2, dist)
    return output


# stations = get_station_data("stations1.csv")
# print(greatest_distance(stations))
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
