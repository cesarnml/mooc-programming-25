# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    output = int(input("Function:"))
    if output == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        with open("dictionary.txt", "a") as file:
            file.write(f"{finnish} - {english}\n")
            print("Dictionary entry added")
    if output == 2:
        search = input("Search term: ")
        with open("dictionary.txt", "r") as file:
            for line in file:
                if search in line:
                    print(line)
    if output == 3:
        print("Bye!")
        break
