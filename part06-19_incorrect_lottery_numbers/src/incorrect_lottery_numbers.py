# Write your solution here
def filter_incorrect():
    open("correct_numbers.csv", "w").close()
    with open("lottery_numbers.csv", "r") as file:
        for line in file:
            line = line.strip()
            try:
                week, numbers = line.split(";")
            except ValueError:
                continue

            week_no = week[5:]
            try:
                int(week_no)
            except ValueError:
                continue

            nums = numbers.split(",")
            if len(nums) != 7:
                continue

            try:
                nums = [int(n) for n in nums]
            except ValueError:
                continue

            if any(n < 1 or n > 39 for n in nums):
                continue
            if len(set(nums)) != 7:
                continue

            with open("correct_numbers.csv", "a") as outfile:
                outfile.write(f"{line}\n")
