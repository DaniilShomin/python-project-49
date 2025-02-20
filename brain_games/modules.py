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


def check_number_prime(number):    
    if number == 1:
        return 'no'
    for divider in range(2, number):
        if number % divider == 0:
            return 'no'  
    return 'yes'