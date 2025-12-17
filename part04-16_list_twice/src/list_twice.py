# Write your solution here
items = []
while True:
    item = int(input("New item: "))
    if item == 0:
        break
    else:
        items.append(item)
    print(f"The list now: {items}")
    print(f"The list in order: {sorted(items)}")
print("Bye!")
