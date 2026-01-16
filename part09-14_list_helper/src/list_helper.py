# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list[int]):
        if not my_list:
            return None

        count = my_list.count(my_list[0])
        most_common = my_list[0]
        for num in my_list:
            if my_list.count(num) > count:
                count = my_list.count(num)
                most_common = num
        return most_common

    @classmethod
    def doubles(cls, my_list: list[int]):
        count = 0
        seen = []
        for num in my_list:
            if my_list.count(num) >= 2 and not num in seen:
                count += 1
            seen.append(num)

        return count
