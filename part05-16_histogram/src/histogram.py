# Write your solution here
def histogram(word: str):
    my_dict = {}
    for char in word:
        if not char in my_dict:
            my_dict[char] = 1
        else:
            my_dict[char] += 1
    for key, value in my_dict.items():
        print(f"{key} {value * '*'}")
