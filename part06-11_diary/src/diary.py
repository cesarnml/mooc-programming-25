# Write your solution here
while True:
    print("1 - add entry, 2 - read entries, 0 - quit")
    option = int(input("Function: "))
    if option == 0:
        print("Bye now!")
        break
    elif option == 2:
        print("Entries:")
        with open("diary.txt", "r") as file:
            for line in file:
                print(line.strip())
    else:
        addendum = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(addendum + "\n")
        print("Diary saved.")
