from random import randint

import prompt

from brain_games.modules import check_number_prime, was_correct_answer


def prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question_num = 0
    while question_num < 3:
        number = randint(1, 99)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        result = check_number_prime(number)
        if number == 1 and answer == 'no':
            print('Correct!')
            question_num += 1
        elif result == answer:
            print('Correct!')
            question_num += 1
        else:
            was_correct_answer(False, name, answer, result)
            break
    if question_num == 3:
        was_correct_answer(True, name)