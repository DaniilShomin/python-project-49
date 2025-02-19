from random import choice, randint

import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name


def was_correct_answer(correct: bool, name: str, answer='', result=''):
    if correct:
        print(f"Congratulations, {name}!")
    elif not correct:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")


def parity_check(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = 0
    while question_num < 3:
        number = randint(1, 99)
        print(f"Question: {number}")
        parity = number % 2
        answer = input("Your answer: ")
        if (parity == 0 and answer == 'yes'):
            print('Correct!')
            question_num += 1
        elif (parity != 0 and answer == 'no'):
            print('Correct!')
            question_num += 1
        elif parity == 0 and answer != 'yes':
            was_correct_answer(False, name, answer, 'yes')
            break
        elif parity != 0 and answer != 'no':
            was_correct_answer(False, name, answer, 'no')
            break
    if question_num == 3:
        was_correct_answer(True, name)


def calc(name):
    print('What is the result of the expression?')
    operations = ['+', '-', '*']
    question_num = 0
    while question_num < 3:
        number_one = randint(1, 99)
        number_two = randint(1, 99)
        operation = choice(operations)
        print(f"Question: {number_one} {operation} {number_two}")
        answer = input("Your answer: ")
        match operation:
            case '+':
                result = number_one + number_two
            case '-':
                result = number_one - number_two
            case '*':
                result = number_one * number_two
        if int(answer) == result:
            print('Correct!')
            question_num += 1
        else:
            was_correct_answer(False, name, answer, str(result))
            break
    if question_num == 3:
        was_correct_answer(True, name)


def gcd(name):
    print("Find the greatest common divisor of given numbers.")
    question_num = 0
    while question_num < 3:
        number_one = randint(1, 99)
        number_two = randint(1, 99)
        print(f"Question: {number_one} {number_two}")
        answer = input("Your answer: ")
        if number_one < number_two:
            number_one, number_two = number_two, number_one
        if number_one % number_two != 0:
            for result in range(int(number_two / 2), 0, -1):
                if number_one % result == 0 and number_two % result == 0:
                    break
            if int(answer) == result:
                print('Correct!')
                question_num += 1
            else:
                was_correct_answer(False, name, answer, str(result))
                break
        else:
            result = number_two
            if int(answer) == result:
                print('Correct!')
                question_num += 1
    if question_num == 3:
        was_correct_answer(True, name)