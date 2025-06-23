from random import randint


def is_parity(number:int) -> bool:
    return number % 2 == 0


def parity_check() -> str:
    number = randint(1, 99)
    print(f"Question: {number}")
    return 'yes' if is_parity(number) else 'no'