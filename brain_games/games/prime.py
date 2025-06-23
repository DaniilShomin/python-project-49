from random import randint


def is_number_prime(number:int) -> bool:    
    if number == 1:
        return False
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True


def prime() -> str:
    number = randint(1, 99)
    print(f"Question: {number}")
    return 'yes' if is_number_prime(number) else 'no'