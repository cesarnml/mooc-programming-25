# Write your solution here
a_list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    value = int(input("New value: "))
    a_list[index] = value
    print(a_list)
