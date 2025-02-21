from random import randint


def check_number_prime(number):    
    if number == 1:
        return 'no'
    for divider in range(2, number):
        if number % divider == 0:
            return 'no'  
    return 'yes'


def prime():
    number = randint(1, 99)
    print(f"Question: {number}")
    result = check_number_prime(number)
    return [number, result]