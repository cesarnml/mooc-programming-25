# Write your solution here

import json
import math
import urllib


def retrieve_all():
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    data = urllib.request.urlopen(address).read()
    courses = json.loads(data)
    enabled_courses = []
    for course in courses:
        if course["enabled"]:
            enabled_courses.append(
                (
                    course["fullName"],
                    course["name"],
                    course["year"],
                    sum(course["exercises"]),
                )
            )
    return enabled_courses


def retrieve_course(course_name: str):
    address = (
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )
    data = urllib.request.urlopen(address).read()
    course_stats = json.loads(data)
    weeks = len(course_stats)
    students = 0
    hours = 0
    exercises = 0
    for course_stat in course_stats.values():
        hours += course_stat["hour_total"]
        exercises += course_stat["exercise_total"]
        if course_stat["students"] > students:
            students = course_stat["students"]
    hours_average = math.floor(hours / students)
    exercises_average = math.floor(exercises / students)
    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average,
    }
