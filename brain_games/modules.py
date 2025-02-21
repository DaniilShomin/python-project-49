import prompt

from brain_games.games.calc import calc
from brain_games.games.even import parity_check
from brain_games.games.gcd import gcd
from brain_games.games.prime import prime
from brain_games.games.progression import progression


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


def checking_result(name_game, answer, result, name, number):
    if name_game == 'even':
        if number == 0 and answer == 'yes':
            return True
        elif number != 0 and answer == 'no':
            return True
    elif name_game == 'prime' and number == 1 and answer == 'no':
        return True
    elif answer == str(result):
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. ", end='')
        print(f"Correct answer was '{result}'.")
        print(f"Let's try again, {name}!")
        return False


def starting_game(name_game, text_game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(text_game)
    question_num = 0
    while question_num < 3:
        number = 0
        match name_game:
            case 'calc':
                result = calc()
            case 'even':
                items = parity_check()
                number = items[0]
                result = items[1]
            case 'gcd':
                result = gcd()
            case 'prime':
                items = prime()
                number = items[0]
                result = items[1]
            case 'progression':
                result = progression()
        answer = prompt.string("Your answer: ")
        if checking_result(name_game, answer, result, name, number):
            print('Correct!')
            question_num += 1
        else:
            break
    if question_num == 3:
        print(f"Congratulations, {name}!")