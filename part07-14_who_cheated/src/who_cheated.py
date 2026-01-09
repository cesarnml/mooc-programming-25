# Write your solution here
import csv
from datetime import datetime, timedelta


def cheaters():
    start_data = {}
    end_data = {}
    cheaters = []
    with open("start_times.csv", "r") as file:
        for line in csv.reader(file, delimiter=";"):
            time = line[1].split(":")
            start_data[line[0]] = datetime(1999, 1, 1, int(time[0]), int(time[1]))
    with open("submissions.csv", "r") as file:
        for line in csv.reader(file, delimiter=";"):
            name = line[0]
            time = line[3].split(":")
            new_time = datetime(1999, 1, 1, int(time[0]), int(time[1]))
            if not name in end_data.keys():
                end_data[name] = new_time
            else:
                old_time = end_data[name]
                if new_time > old_time:
                    end_data[name] = new_time
    for key in start_data.keys():
        elapsed_time = (end_data[key] - start_data[key]).seconds
        if elapsed_time > 3 * 60 * 60:
            cheaters.append(key)
    return cheaters
