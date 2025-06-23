from random import randint


def divisor_two_numbers(number_one:int, number_two:int) -> int:
    if number_one < number_two:
        number_one, number_two = number_two, number_one
    if number_one % number_two != 0:
        for result in range(number_two // 2, 0, -1):
            if number_one % result == 0 and number_two % result == 0:
                break
        return result
    else:
        result = number_two
        return result


def gcd() -> int:
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    print(f"Question: {number_one} {number_two}")
    return divisor_two_numbers(number_one, number_two)