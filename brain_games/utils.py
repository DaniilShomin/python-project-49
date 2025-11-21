from random import randint


def get_random_number(min: int = 1, max: int = 100) -> int:
    return randint(min, max)
