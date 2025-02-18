from brain_games.modules import welcome_user, parity_check


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()  
    parity_check(name)

if __name__ == '__main__':
    main()