# Write your solution here
def distinct_numbers(nums: list):
    unique = []
    for num in sorted(nums):
        if not num in unique:
            unique.append(num)
    return unique
