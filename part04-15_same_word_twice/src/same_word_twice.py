# Write your solution here
a_list = []
while True:
    word = input("Word: ")
    if word in a_list:
        break
    else:
        a_list.append(word)
print(f"You typed in {len(a_list)} different words")
