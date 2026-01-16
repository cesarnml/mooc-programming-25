# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

    def weight(self):
        return self.__weight

    def name(self):
        return self.__name


class Suitcase:
    def __init__(self, max_weight: int):
        self.__items: list[Item] = []
        self.__max_weight = max_weight

    @property
    def max_weight(self):
        return self.__max_weight

    @max_weight.setter
    def max_weight(self, max_weight):
        self.__max_weight = max_weight

    def weight(self):
        if len(self.__items) == 0:
            return 0
        return sum([item.weight() for item in self.__items])

    def add_item(self, item: Item):
        current_weight = self.weight()
        if current_weight + item.weight() < self.__max_weight:
            self.__items.append(item)

    def heaviest_item(self):
        if len(self.__items) == 0:
            return None
        max_weight = 0
        max_item = None
        for item in self.__items:
            if item.weight() > max_weight:
                max_weight = item.weight()
                max_item = item
        return max_item

    def print_items(self):

        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)")

    def __str__(self):
        current_weight = self.weight()
        item_no = len(self.__items)
        return f"{item_no} item{'s' if item_no != 1 else ''} ({current_weight} kg)"


class CargoHold:
    def __init__(self, max_weight: int):
        self.__suitcases: list[Suitcase] = []
        self.__max_weight = max_weight

    def add_suitcase(self, suitcase: Suitcase):
        current_weight = sum([suitcase.weight() for suitcase in self.__suitcases])
        if current_weight + suitcase.weight() < self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        suitcase_no = len(self.__suitcases)
        current_weight = sum([suitcase.weight() for suitcase in self.__suitcases])
        return f"{suitcase_no} suitcase{'s' if suitcase_no != 1 else ''}, space for {self.__max_weight - current_weight} kg"
