#!/usr/bin/env python3
"""Final comprehensive test of the order book application"""

import sys
from io import StringIO
from unittest.mock import patch

sys.path.insert(
    0,
    "/Users/cesar/code/helsinki/IntroductionToProgramming/tms/mooc-programming-25/part11-19_order_book_application/src",
)

from order_book_application import Task, OrderBook, main

print("=" * 80)
print("FINAL COMPREHENSIVE TEST: All Requirements")
print("=" * 80)

test_cases = [
    {
        "name": "Menu display",
        "inputs": ["0"],
        "checks": [
            ("commands:", True),
            ("0 exit", True),
            ("1 add order", True),
            ("2 list finished tasks", True),
            ("3 list unfinished tasks", True),
            ("4 mark task as finished", True),
            ("5 programmers", True),
            ("6 status of programmer", True),
        ],
    },
    {
        "name": "Add order - single task",
        "inputs": ["1", "test task", "alice 5", "0"],
        "checks": [
            ("added!", True),
        ],
    },
    {
        "name": "List unfinished - single task",
        "inputs": ["1", "test task", "alice 5", "3", "0"],
        "checks": [
            ("test task", True),
            ("alice", True),
            ("NOT FINISHED", True),
        ],
    },
    {
        "name": "No finished tasks message",
        "inputs": ["1", "test task", "alice 5", "2", "0"],
        "checks": [
            ("no finished tasks", True),
        ],
    },
    {
        "name": "Mark task as finished",
        "inputs": ["1", "test task", "alice 5", "4", "1", "0"],
        "checks": [
            ("marked as finished", True),
        ],
    },
    {
        "name": "List finished tasks",
        "inputs": ["1", "test task", "alice 5", "4", "1", "2", "0"],
        "checks": [
            ("test task", True),
            ("FINISHED", True),
        ],
    },
    {
        "name": "Programmers list",
        "inputs": ["1", "task1", "alice 5", "1", "task2", "bob 10", "5", "0"],
        "checks": [
            ("alice", True),
            ("bob", True),
        ],
    },
    {
        "name": "Status of programmer",
        "inputs": [
            "1",
            "task1",
            "alice 5",
            "1",
            "task2",
            "alice 10",
            "4",
            "1",
            "6",
            "alice",
            "0",
        ],
        "checks": [
            ("tasks: finished 1 not finished 1, hours: done 5 scheduled 10", True),
        ],
    },
    {
        "name": "Error - invalid workload (non-integer)",
        "inputs": ["1", "task", "alice abc", "0"],
        "checks": [
            ("erroneous input", True),
        ],
    },
    {
        "name": "Error - missing workload",
        "inputs": ["1", "task", "alice", "0"],
        "checks": [
            ("erroneous input", True),
        ],
    },
    {
        "name": "Error - invalid task ID (non-integer)",
        "inputs": ["1", "task", "alice 5", "4", "abc", "0"],
        "checks": [
            ("erroneous input", True),
        ],
    },
    {
        "name": "Error - non-existent task ID",
        "inputs": ["1", "task", "alice 5", "4", "999", "0"],
        "checks": [
            ("erroneous input", True),
        ],
    },
    {
        "name": "Error - unknown programmer",
        "inputs": ["1", "task", "alice 5", "6", "unknown", "0"],
        "checks": [
            ("erroneous input", True),
        ],
    },
    {
        "name": "Recovery - add order after error",
        "inputs": ["1", "task", "alice", "1", "task2", "alice 5", "3", "0"],
        "checks": [
            ("erroneous input", True),
            ("added!", True),
            ("task2", True),
        ],
    },
]

passed = 0
failed = 0

for test_case in test_cases:
    Task.id_counter = 1  # Reset for each test

    with patch("builtins.input", side_effect=test_case["inputs"]):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()

    all_checks_passed = True
    for check_text, should_exist in test_case["checks"]:
        is_present = check_text in output
        if is_present != should_exist:
            all_checks_passed = False
            break

    if all_checks_passed:
        print(f"✓ {test_case['name']}")
        passed += 1
    else:
        print(f"✗ {test_case['name']}")
        print(f"  Output:\n{output[:200]}...")
        failed += 1

print("\n" + "=" * 80)
print(f"Results: {passed} passed, {failed} failed")
if failed == 0:
    print("ALL TESTS PASSED! ✓")
print("=" * 80)
