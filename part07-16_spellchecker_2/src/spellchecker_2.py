# Write your solution here

from difflib import get_close_matches

phrase = input("write text: ")

dictionary = []
with open("wordlist.txt", "r") as file:
    for line in file:
        dictionary.append(line.strip())

new_phrase = ""
misspelled = []
for word in phrase.split(" "):
    if not word.lower() in dictionary:
        misspelled.append(word)
        word = f"*{word}*"

    new_phrase += f" {word}"
print(new_phrase)
print("suggestions:")
for word in misspelled:
    print(f"{word}: {', '.join(get_close_matches(word, dictionary))}")
