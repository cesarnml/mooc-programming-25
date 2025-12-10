# Write your solution
a_list = []
entry = 0
while True:
    print(f"The list is now {a_list}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "x":
        break
    if command == "d":
        entry += 1
        a_list.append(entry)
    if command == "r":
        entry -= 1
        a_list.pop()
print("Bye!")
