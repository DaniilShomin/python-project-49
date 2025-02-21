from random import randint


def parity_check():
    number = randint(1, 99)
    print(f"Question: {number}")
    parity = number % 2
    if parity == 0:
        result = 'yes'
        return [parity, result]
    elif parity != 0:
        result = 'no'
        return [parity, result]