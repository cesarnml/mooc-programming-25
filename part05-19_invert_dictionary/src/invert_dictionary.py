# Write your solution here
def invert(dictionary: dict):
    temp_dict = {}
    for key, value in dictionary.items():
        temp_dict[value] = key
    dictionary.clear()
    for key, value in temp_dict.items():
        dictionary[key] = value
