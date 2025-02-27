import prompt


def is_check_result(answer, result):
    return True if answer == str(result) else False


def starting_game(text_game, game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    print(text_game)
    question_num = 0
    while question_num < 3:
        result_game = game()
        answer = prompt.string("Your answer: ")
        if is_check_result(answer, result_game):
            print('Correct!')
            question_num += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result_game}'.")
            print(f"Let's try again, {name}!")
            break
    if question_num == 3:
        print(f"Congratulations, {name}!")