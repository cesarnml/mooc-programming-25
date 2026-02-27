class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name

    def grade(self):
        return self.__grade

    def credits(self):
        return self.__credits

    def update(self, grade: int, credits: int):
        if grade > self.__grade:
            self.__grade = grade
        self.__credits = credits


class CourseRegister:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
            return
        self.__courses[name].update(grade, credits)

    def get_course(self, name: str):
        return self.__courses.get(name)

    def all_courses(self):
        return list(self.__courses.values())


class CourseRecordsApplication:
    def __init__(self):
        self.__register = CourseRegister()

    def help(self):
        print("1 add course 2 get course data 3 statistics 0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__register.add_course(name, grade, credits)

    def get_course(self):
        name = input("course: ")
        course = self.__register.get_course(name)
        if course is None:
            print("no entry for this course")
            return
        print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")

    def _format_mean(self, value: float):
        rounded = round(value, 1)
        if rounded == int(rounded):
            return str(int(rounded))
        return f"{rounded:.1f}"

    def statistics(self):
        courses = self.__register.all_courses()
        count = len(courses)
        total_credits = sum(course.credits() for course in courses)
        mean = 0.0
        if count > 0:
            mean = sum(course.grade() for course in courses) / count

        print(f"{count} completed courses, a total of {total_credits} credits")
        print(f"mean {self._format_mean(mean)}")
        print("grade distribution")

        grades = {grade: 0 for grade in range(1, 6)}
        for course in courses:
            grades[course.grade()] += 1

        for grade in range(5, 0, -1):
            print(f"{grade}: " + "x" * grades[grade])

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.statistics()
            else:
                self.help()


application = CourseRecordsApplication()
application.execute()
