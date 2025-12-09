# Write your solution here
while True:
    editor = input("Editor: ").lower()
    if editor == "word" or editor == "notepad":
        print("awful")
    elif editor == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")
