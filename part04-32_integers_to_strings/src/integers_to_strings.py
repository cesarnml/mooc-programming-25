# Write your solution here
def formatted(nums: list):
    formatted = []
    for num in nums:
        formatted.append(f"{num:.2f}")
    return formatted
