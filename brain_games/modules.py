import prompt


def is_check_result(answer:str, result_game:str|int) -> bool:
    return answer == str(result_game)


def starting_game(text_game:str, game:function) -> None:
    print("Welcome to the Brain Games!")
    name_player = prompt.string("May I have your name? ")
    print(f"Hello, {name_player}")
    print(text_game)
    question_count = 3
    while question_count > 0:
        result_game = game()
        answer = prompt.string("Your answer: ")
        if is_check_result(answer, result_game):
            print('Correct!')
            question_count -= 1
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result_game}'.")
            print(f"Let's try again, {name_player}!")
            break
    if question_count == 0:
        print(f"Congratulations, {name_player}!")