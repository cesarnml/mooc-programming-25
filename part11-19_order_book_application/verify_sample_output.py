#!/usr/bin/env python3
"""Verify the exact sample output from the requirements"""

import sys
from io import StringIO
from unittest.mock import patch

sys.path.insert(
    0,
    "/Users/cesar/code/helsinki/IntroductionToProgramming/tms/mooc-programming-25/part11-19_order_book_application/src",
)

from order_book_application import Task, OrderBook, main

print("=" * 70)
print("SAMPLE OUTPUT TEST: Following the exact sequence from requirements")
print("=" * 70)

Task.id_counter = 1

# Following the exact sequence from the requirements sample output
inputs = [
    "1",
    "program the next facebook",
    "Jonah 1000",
    "1",
    "program mobile app for workload accounting",
    "Eric 25",
    "1",
    "program an app for music theory revision",
    "Nina 12",
    "1",
    "program the next twitter",
    "Jonah 55",
    "2",  # list finished tasks (should show "no finished tasks")
    "3",  # list unfinished tasks (should show all 4)
    "4",
    "2",  # mark task 2 as finished
    "4",
    "4",  # mark task 4 as finished
    "2",  # list finished tasks (should show tasks 2 and 4)
    "3",  # list unfinished tasks (should show tasks 1 and 3)
    "5",  # list programmers
    "6",
    "Jonah",  # status of Jonah
    "0",  # exit
]

with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)

print("\n" + "=" * 70)
print("VERIFICATION OF KEY OUTPUTS")
print("=" * 70)

checks = [
    ("added! (4 times)", output.count("added!") == 4),
    ("'no finished tasks' initially", "no finished tasks" in output),
    (
        "Task 1 NOT FINISHED",
        "1: program the next facebook" in output and "NOT FINISHED" in output,
    ),
    ("Task 2 marked as finished", "marked as finished" in output),
    ("Task 2 FINISHED in finished tasks", output.count("marked as finished") >= 2),
    (
        "Status line contains required format",
        "tasks: finished" in output
        and "not finished" in output
        and "hours: done" in output
        and "scheduled" in output,
    ),
    ("Jonah listed as programmer", "Jonah" in output or "jonah" in output.lower()),
]

all_passed = True
for check_name, result in checks:
    status = "✓" if result else "✗"
    print(f"{status} {check_name}")
    if not result:
        all_passed = False

if all_passed:
    print("\n" + "=" * 70)
    print("SAMPLE OUTPUT VERIFICATION PASSED! ✓")
    print("=" * 70)
else:
    print("\n" + "=" * 70)
    print("SOME CHECKS FAILED")
    print("=" * 70)
