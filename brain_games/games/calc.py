from random import choice, randint


def perform_operation(num_one:int, num_two:int, operator:list[str]) -> int:
    match operator:
        case '+':
            return num_one + num_two
        case '-':
            return num_one - num_two
        case '*':
            return num_one * num_two


def calc() -> int:
    operations = ['+', '-', '*']
    number_one = randint(1, 99)
    number_two = randint(1, 99)
    operation = choice(operations)
    print(f"Question: {number_one} {operation} {number_two}")
    return perform_operation(number_one, number_two, operation)
