from random import randint

import prompt

from brain_games.modules import was_correct_answer


def gcd(name):
    print("Find the greatest common divisor of given numbers.")
    question_num = 0
    while question_num < 3:
        number_one = randint(1, 99)
        number_two = randint(1, 99)
        print(f"Question: {number_one} {number_two}")
        answer = prompt.string("Your answer: ")
        if number_one < number_two:
            number_one, number_two = number_two, number_one
        if number_one % number_two != 0:
            for result in range(int(number_two / 2), 0, -1):
                if number_one % result == 0 and number_two % result == 0:
                    break
            if answer == str(result):
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