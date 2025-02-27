from random import randint


def is_parity(num):
    return True if num % 2 == 0 else False


def parity_check():
    number = randint(1, 99)
    print(f"Question: {number}")
    return 'yes' if is_parity(number) else 'no'