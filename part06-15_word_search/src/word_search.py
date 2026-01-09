# Write your solution here
def read_file(filename: str) -> list[str]:
    dictionary = []
    with open(filename, "r") as file:
        for line in file:
            dictionary.append(line.strip())
    return dictionary


def find_words(search_term: str):
    dictionary = read_file("words.txt")
    found = []
    if search_term.startswith("*"):
        search_base = search_term[1:]
        for word in dictionary:
            if word.endswith(search_base):
                found.append(word)
    elif search_term.endswith("*"):
        search_base = search_term[:-1]
        for word in dictionary:
            if word.startswith(search_base):
                found.append(word)
    elif "." in search_term:
        for word in dictionary:
            if len(word) != len(search_term):
                continue
            else:
                flag = True
                for i in range(len(search_term)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        flag = False
            if flag:
                found.append(word)
    else:
        for word in dictionary:
            if word == search_term:
                found.append(word)
    return found
