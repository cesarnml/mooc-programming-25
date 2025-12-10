# Write your solution here
number = int(input("How many items: "))

a_list = []
for i in range(number):
    a_list.append(int(input(f"Item {i + 1}: ")))
print(a_list)
