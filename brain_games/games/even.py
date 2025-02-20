from random import randint

import prompt

from brain_games.modules import was_correct_answer


def parity_check(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = 0
    while question_num < 3:
        number = randint(1, 99)
        print(f"Question: {number}")
        parity = number % 2
        answer = prompt.string("Your answer: ")
        if parity == 0 and answer == 'yes':
            print('Correct!')
            question_num += 1
        elif parity != 0 and answer == 'no':
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