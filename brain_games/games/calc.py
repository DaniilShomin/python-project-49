from random import choice, randint

import prompt

from brain_games.modules import was_correct_answer


def calc(name):
    print('What is the result of the expression?')
    operations = ['+', '-', '*']
    question_num = 0
    while question_num < 3:
        number_one = randint(1, 99)
        number_two = randint(1, 99)
        operation = choice(operations)
        print(f"Question: {number_one} {operation} {number_two}")
        answer = prompt.string("Your answer: ")
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