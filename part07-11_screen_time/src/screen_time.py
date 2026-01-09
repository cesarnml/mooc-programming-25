# Write your solution here
from datetime import datetime, timedelta

filename = input("Filename: ")
start = input("Starting date: ")
start_date = datetime.strptime(start, "%d.%m.%Y")
no_days = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile): ")

screentime = []
for i in range(no_days):
    date = start_date + timedelta(days=i)
    screen = input(f"Screen time {date.strftime('%d.%m.%Y') }: ")
    time = [int(x) for x in screen.split(" ")]
    screentime.append(time)
with open(filename, "w") as file:
    file.write(
        f"Time period: {start_date.strftime('%d.%m.%Y')}-{(start_date + timedelta(days=no_days - 1)).strftime('%d.%m.%Y')}\n"
    )
    file.write(f"Total minutes: {sum([sum(x) for x in screentime])}\n")
    file.write(f"Average minutes: {sum([sum(x) for x in screentime]) / no_days}\n")
    for i in range(no_days):
        file.write(
            f"{(start_date + timedelta(days=i)).strftime('%d.%m.%Y')}: {'/'.join([str(x) for x in screentime[i]])}\n"
        )
print(f"Data stored in file {filename}")
