# write your solution here
phrase = input("Write text: ")

words: list = []
with open("wordlist.txt") as file:
    for line in file:
        word = line.replace("\n", "")
        words.append(word)

output = ""
for chunk in phrase.split(" "):
    if chunk.lower() in words:
        output += f"{chunk} "
    else:
        output += f"*{chunk}* "
print(output.rstrip())
