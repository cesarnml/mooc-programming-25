#!/usr/bin/env python3
"""Simple test to verify Task and OrderBook implementation"""

import sys

sys.path.insert(
    0,
    "/Users/cesar/code/helsinki/IntroductionToProgramming/tms/mooc-programming-25/part11-18_order_book/src",
)

from order_book import Task, OrderBook

print("=" * 60)
print("Testing Task class")
print("=" * 60)

# Reset the ID counter for consistent testing
Task.id_counter = 1

# Test 1: Task creation and attributes
t1 = Task("program hello world", "Eric", 3)
print(
    f"Test 1 - Task creation: id={t1.id}, description={t1.description}, programmer={t1.programmer}, workload={t1.workload}"
)
assert t1.id == 1
assert t1.description == "program hello world"
assert t1.programmer == "Eric"
assert t1.workload == 3
print("✓ PASSED")

# Test 2: is_finished method
print(f"\nTest 2 - is_finished (should be False): {t1.is_finished()}")
assert t1.is_finished() == False
print("✓ PASSED")

# Test 3: mark_finished method
t1.mark_finished()
print(f"Test 3 - After mark_finished (should be True): {t1.is_finished()}")
assert t1.is_finished() == True
print("✓ PASSED")

# Test 4: String representation
print(f"\nTest 4 - String representation:\n{t1}")
expected_str = "1: program hello world (3 hours), programmer Eric FINISHED"
assert str(t1) == expected_str, f"Expected: {expected_str}\nGot: {str(t1)}"
print("✓ PASSED")

# Test 5: Multiple tasks with incrementing IDs
print(f"\nTest 5 - Multiple tasks with incrementing IDs:")
t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(f"t1.id = {t1.id}, t2.id = {t2.id}, t3.id = {t3.id}")
assert t1.id == 1
assert t2.id == 2
assert t3.id == 3
print("✓ PASSED")

print("\n" + "=" * 60)
print("Testing OrderBook class")
print("=" * 60)

# Reset for OrderBook tests
Task.id_counter = 1
orders = OrderBook()

# Test 1: add_order and all_orders
print("\nTest 1 - add_order and all_orders:")
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

all_tasks = orders.all_orders()
print(f"Total orders: {len(all_tasks)}")
for task in all_tasks:
    print(f"  {task}")
assert len(all_tasks) == 3
print("✓ PASSED")

# Test 2: programmers method
print("\nTest 2 - programmers method:")
programmers = sorted(orders.programmers())
print(f"Programmers: {programmers}")
assert len(programmers) == 2
assert "Adele" in programmers
assert "Eric" in programmers
print("✓ PASSED")

# Test 3: mark_finished method
print("\nTest 3 - mark_finished:")
orders.mark_finished(1)
orders.mark_finished(2)
for task in orders.all_orders():
    print(f"  {task}")
assert orders.all_orders()[0].is_finished()
assert orders.all_orders()[1].is_finished()
assert not orders.all_orders()[2].is_finished()
print("✓ PASSED")

# Test 4: mark_finished with invalid ID (should raise ValueError)
print("\nTest 4 - mark_finished with invalid ID (should raise ValueError):")
try:
    orders.mark_finished(999)
    print("✗ FAILED - Should have raised ValueError")
    sys.exit(1)
except ValueError as e:
    print(f"  Caught expected error: {e}")
    print("✓ PASSED")

# Test 5: finished_orders and unfinished_orders
print("\nTest 5 - finished_orders and unfinished_orders:")
finished = orders.finished_orders()
unfinished = orders.unfinished_orders()
print(f"Finished orders ({len(finished)}):")
for task in finished:
    print(f"  {task}")
print(f"Unfinished orders ({len(unfinished)}):")
for task in unfinished:
    print(f"  {task}")
assert len(finished) == 2
assert len(unfinished) == 1
print("✓ PASSED")

# Test 6: status_of_programmer
print("\nTest 6 - status_of_programmer:")
Task.id_counter = 1
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(f"Adele's status: {status}")
assert status == (2, 1, 35, 100), f"Expected (2, 1, 35, 100), got {status}"
print("✓ PASSED")

# Test 7: status_of_programmer with nonexistent programmer (should raise ValueError)
print("\nTest 7 - status_of_programmer with nonexistent programmer:")
try:
    orders.status_of_programmer("NonExistent")
    print("✗ FAILED - Should have raised ValueError")
    sys.exit(1)
except ValueError as e:
    print(f"  Caught expected error: {e}")
    print("✓ PASSED")

print("\n" + "=" * 60)
print("ALL TESTS PASSED! ✓")
print("=" * 60)
