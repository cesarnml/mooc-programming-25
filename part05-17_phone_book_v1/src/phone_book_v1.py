# Write your solution here
phone_book = {}
while True:
    cmd = int(input("command (1 search, 2 add, 3 quit): "))
    if cmd == 3:
        print("quitting...")
        break
    if cmd == 2:
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
    if cmd == 1:
        name = input("name: ")
        if not name in phone_book:
            print("no number")
        else:
            print(phone_book[name])
