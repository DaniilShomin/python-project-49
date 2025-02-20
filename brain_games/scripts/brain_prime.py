from brain_games.modules import prime, welcome_user


def main():
    name = welcome_user()  
    prime(name)


if __name__ == '__main__':
    main()