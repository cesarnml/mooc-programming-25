# write your solution here
def read_fruits():
    my_dict = {}
    with open("./fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            name, price = line.split(";")
            my_dict[name] = float(price)
    return my_dict
