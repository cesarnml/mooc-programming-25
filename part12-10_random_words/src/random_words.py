import random


def word_generator(characters: str, length: int, amount: int):
    return (
        "".join(random.choice(characters) for _ in range(length)) for i in range(amount)
    )
