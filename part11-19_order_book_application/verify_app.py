#!/usr/bin/env python3
"""Simple test to verify OrderBookApplication works correctly"""

import sys
from io import StringIO
from unittest.mock import patch

# Add the source directory to the path
sys.path.insert(
    0,
    "/Users/cesar/code/helsinki/IntroductionToProgramming/tms/mooc-programming-25/part11-19_order_book_application/src",
)

from order_book_application import Task, OrderBook, main

print("=" * 70)
print("TEST 1: Basic add order and list unfinished")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code new facebook", "jonas 10", "3", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "added!" in output, "Expected 'added!' in output"
assert "code new facebook" in output, "Expected task in output"
assert "jonas" in output, "Expected programmer in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 2: Mark finished and list finished tasks")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code new facebook", "jonas 10", "4", "1", "2", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "marked as finished" in output, "Expected 'marked as finished' in output"
assert "FINISHED" in output, "Expected 'FINISHED' in output"
assert "no finished tasks" not in output, "Should have finished tasks"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 3: Programmers list")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas 10", "1", "code twitter", "brian 20", "5", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "brian" in output.lower(), "Expected 'brian' in output"
assert "jonas" in output.lower(), "Expected 'jonas' in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 4: Status of programmer")
print("=" * 70)

Task.id_counter = 1
inputs = [
    "1",
    "code facebook",
    "jonas 10",
    "1",
    "code twitter",
    "jonas 95",
    "4",
    "1",
    "6",
    "jonas",
    "0",
]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert (
    "tasks: finished 1 not finished 1, hours: done 10 scheduled 95" in output
), f"Expected status message in output.\nOutput was:\n{output}"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 5: Error handling - invalid workload")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas x", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "erroneous input" in output, "Expected 'erroneous input' in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 6: Error handling - missing workload")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "erroneous input" in output, "Expected 'erroneous input' in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 7: Error handling - invalid task ID")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas 10", "4", "100", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "erroneous input" in output, "Expected 'erroneous input' in output"
assert "marked as finished" not in output, "Should not have marked as finished"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 8: Error handling - non-integer task ID")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas 10", "4", "xx", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "erroneous input" in output, "Expected 'erroneous input' in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 9: Error handling - unknown programmer")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas 10", "6", "brian", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "erroneous input" in output, "Expected 'erroneous input' in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 10: Recovery from error - add after error")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas", "1", "code facebook", "jonas 10", "3", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "erroneous input" in output, "Expected 'erroneous input' for first attempt"
assert "added!" in output, "Expected 'added!' for second attempt"
assert (
    "code new facebook" in output or "code facebook" in output
), "Expected task in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 11: No finished tasks message")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas 10", "2", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "no finished tasks" in output, "Expected 'no finished tasks' in output"
print("✓ PASSED\n")

print("=" * 70)
print("TEST 12: No unfinished tasks message")
print("=" * 70)

Task.id_counter = 1
inputs = ["1", "code facebook", "jonas 10", "4", "1", "3", "0"]
with patch("builtins.input", side_effect=inputs):
    with patch("sys.stdout", new=StringIO()) as fake_out:
        main()
        output = fake_out.getvalue()

print(output)
assert "no unfinished tasks" in output, "Expected 'no unfinished tasks' in output"
print("✓ PASSED\n")

print("=" * 70)
print("ALL TESTS PASSED! ✓")
print("=" * 70)
