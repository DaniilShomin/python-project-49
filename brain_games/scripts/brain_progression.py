from brain_games.modules import progression, welcome_user


def main():
    name = welcome_user()  
    progression(name)


if __name__ == '__main__':
    main()