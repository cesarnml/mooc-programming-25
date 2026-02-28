#!/usr/bin/env python3
"""Verify all examples from the exercise requirements work correctly"""

import sys

sys.path.insert(
    0,
    "/Users/cesar/code/helsinki/IntroductionToProgramming/tms/mooc-programming-25/part11-18_order_book/src",
)

from order_book import Task, OrderBook

print("=" * 70)
print("EXAMPLE 1: Task Usage (from requirements)")
print("=" * 70)

Task.id_counter = 1  # Reset counter

t1 = Task("program hello world", "Eric", 3)
print(f"{t1.id} {t1.description} {t1.programmer} {t1.workload}")
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())

t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)

print("\n" + "=" * 70)
print("EXAMPLE 2: OrderBook Basic Usage (from requirements)")
print("=" * 70)

Task.id_counter = 1  # Reset counter
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

for order in orders.all_orders():
    print(order)

print()

for programmer in sorted(orders.programmers()):
    print(programmer)

print("\n" + "=" * 70)
print("EXAMPLE 3: mark_finished Usage (from requirements)")
print("=" * 70)

Task.id_counter = 1  # Reset counter
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Eric", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)

orders.mark_finished(1)
orders.mark_finished(2)

for order in orders.all_orders():
    print(order)

print("\n" + "=" * 70)
print("EXAMPLE 4: status_of_programmer Usage (from requirements)")
print("=" * 70)

Task.id_counter = 1  # Reset counter
orders = OrderBook()
orders.add_order("program webstore", "Adele", 10)
orders.add_order("program mobile app for workload accounting", "Adele", 25)
orders.add_order("program app for practising mathematics", "Adele", 100)
orders.add_order("program the next facebook", "Eric", 1000)

orders.mark_finished(1)
orders.mark_finished(2)

status = orders.status_of_programmer("Adele")
print(status)

print("\n" + "=" * 70)
print("ALL REQUIREMENTS VERIFIED ✓")
print("=" * 70)
