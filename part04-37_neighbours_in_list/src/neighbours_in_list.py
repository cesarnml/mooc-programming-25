def longest_series_of_neighbours(numbers):
    longest = 1
    longest_so_far = 1
    length = len(numbers)
    for i in range(length - 1):
        if abs(numbers[i] - numbers[i + 1]) == 1:
            longest_so_far += 1
            if longest_so_far > longest:  # Only update when we find a longer series
                longest = longest_so_far
        else:
            longest_so_far = 1  # Reset to 1, not 0
    return longest
