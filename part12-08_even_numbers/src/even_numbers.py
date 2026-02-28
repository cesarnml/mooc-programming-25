def even_numbers(beginning: int, maximum: int):
    current = beginning if beginning % 2 == 0 else beginning + 1
    while current <= maximum:
        yield current
        current += 2
