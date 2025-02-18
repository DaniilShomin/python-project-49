import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name

def parity_check(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question_num = 0
    while question_num < 3:
        number = randint(1, 99)
        print(f"Question: {number}")
        parity = number % 2
        answer = input("Your answer: ")
        if (parity == 0 and answer == 'yes') or (parity != 0 and answer == 'no'):
            print('Correct!')
            question_num += 1
        elif parity == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif parity != 0 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
        if question_num == 3:
            print(f"Congratulations, {name}!")