import prompt  # type: ignore


def welcome_user() -> str:
    print("Welcome to the Brain Game!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name
