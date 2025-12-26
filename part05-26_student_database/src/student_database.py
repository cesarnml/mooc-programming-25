# Write your solution here
def add_student(students: dict, name: str):
    record = {}
    record["name"] = name
    record["courses"] = []
    students[name] = record


def print_student(students: dict, name: str):
    if not name in students:
        print(f"{name}: no such person in the database")
    else:
        record = students[name]
        courses = record["courses"]
        completed_courses = [course for course in courses if course[1] > 0]
        print(f"{name}:")
        if len(completed_courses) == 0:
            print(f" no completed courses")
        else:
            print(f" {len(completed_courses)} completed courses:")
            total = 0
            for course in completed_courses:
                total += course[1]
                print(f"  {course[0]} {course[1]}")
            if len(completed_courses) > 0:
                print(f" average grade {total/len(completed_courses):.1f}")


def add_course(students: dict, name: str, new_course: tuple):
    record = students[name]
    courses = record["courses"]
    course_names = [course[0] for course in courses]

    if not new_course[0] in course_names:
        courses.append(new_course)
    for i in range(len(courses)):
        course = courses[i]
        if course[0] == new_course[0] and course[1] < new_course[1]:
            courses[i] = new_course


def summary(students: dict):
    print(f"students {len(students)}")
    most_courses = 0
    most_name = ""
    avg_num = 0
    avg_name = ""
    for student in students:
        courses = students[student]["courses"]
        completed_courses = [course for course in courses if course[1] > 0]
        if len(completed_courses) > most_courses:
            most_courses = len(completed_courses)
            most_name = students[student]["name"]
        avg = 0
        for course in completed_courses:
            avg += course[1]
        avg = avg / len(completed_courses)
        if avg > avg_num:
            avg_num = avg
            avg_name = students[student]["name"]

    print(f"most courses completed {most_courses} {most_name}")
    print(f"best average grade {avg_num:.1f} {avg_name}")
