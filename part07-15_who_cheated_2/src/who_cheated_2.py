# Write your solution here
import csv
from datetime import datetime, timedelta


def final_points():
    start_data = {}
    end_data = {}

    with open("start_times.csv", "r") as file:
        for line in csv.reader(file, delimiter=";"):
            time = line[1]
            start_data[line[0]] = datetime.strptime(time, "%H:%M")
    with open("submissions.csv", "r") as file:
        for line in csv.reader(file, delimiter=";"):
            name = line[0]
            task = line[1]
            points = line[2]
            time = datetime.strptime(line[3], "%H:%M")
            new_task = {"task": task, "points": points, "time": time}
            if not name in end_data:
                end_data[name] = [new_task]
            else:
                end_data[name].append(new_task)

    output = {}
    for name, start_time in start_data.items():
        tasks = end_data[name]
        task_points_for_name = {}
        for task in tasks:
            task_no = task["task"]
            task_points = task["points"]
            task_time = task["time"]
            if task_time - start_time > timedelta(hours=3):
                continue
            else:
                if not task_no in task_points_for_name:
                    task_points_for_name[task_no] = task_points
                else:
                    if task_points > task_points_for_name[task_no]:
                        task_points_for_name[task_no] = task_points
        score = 0
        for point in task_points_for_name.values():
            score += int(point)
        output[name] = score
    return output
