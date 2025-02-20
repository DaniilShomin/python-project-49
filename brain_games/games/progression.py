from random import randint

import prompt

from brain_games.modules import was_correct_answer


def progression(name):
    print("What number is missing in the progression?")
    question_num = 0
    while question_num < 3:
        start_prog = randint(1, 15)
        step_prog = randint(2, 5)
        heden_num_prog = randint(0, 9)
        progression = []
        progression.append(start_prog)
        while len(progression) < 10:
            progression.append(progression[-1] + step_prog)
        result, progression[heden_num_prog] = progression[heden_num_prog], '..'
        print("Question: ", end='')
        for value in progression:
            print(value, end=' ')
        print()
        answer = prompt.string("Your answer: ")
        if int(answer) == result:
            print('Correct!')
            question_num += 1
        else:
            was_correct_answer(False, name, answer, str(result))
            break
    if question_num == 3:
        was_correct_answer(True, name)