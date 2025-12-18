def calculate_grade(exam_points, exercise_points):
    # Exam cutoff: less than 10 exam points = automatic fail
    if exam_points < 10:
        return 0

    total = exam_points + exercise_points

    if total >= 28:
        return 5
    elif total >= 24:
        return 4
    elif total >= 21:
        return 3
    elif total >= 18:
        return 2
    elif total >= 15:
        return 1
    else:
        return 0


# Collect input
results = []

while True:
    line = input("Exam points and exercises completed: ")
    if line == "":
        break
    parts = line.split()
    exam_points = int(parts[0])
    exercises = int(parts[1])
    results.append((exam_points, exercises))

# Calculate statistics
grades = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
total_points = 0
passed = 0

for exam_points, exercises in results:
    # Convert exercises to exercise points (10% = 1 point, max 10)
    exercise_points = exercises // 10

    total = exam_points + exercise_points
    total_points += total

    grade = calculate_grade(exam_points, exercise_points)
    grades[grade] += 1

    if grade > 0:
        passed += 1

# Print statistics
print("Statistics:")
average = total_points / len(results)
print(f"Points average: {average:.1f}")

pass_percentage = (passed / len(results)) * 100
print(f"Pass percentage: {pass_percentage:.1f}")

print("Grade distribution:")
for grade in range(5, -1, -1):
    stars = "*" * grades[grade]
    print(f"  {grade}: {stars}")
