# Write your solution here
def even_numbers(nums: list):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens
