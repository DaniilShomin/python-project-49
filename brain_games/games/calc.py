from random import choice, randint


def calc():
    operations = ['+', '-', '*']
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    operation = choice(operations)
    print(f"Question: {number_one} {operation} {number_two}")
    match operation:
        case '+':
            result = number_one + number_two
            return result
        case '-':
            result = number_one - number_two
            return result
        case '*':
            result = number_one * number_two
            return result
