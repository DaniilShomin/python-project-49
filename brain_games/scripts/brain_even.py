from brain_games.games.even import even
from brain_games.modules import welcome_user


def main():
    name = welcome_user()  
    even(name)


if __name__ == '__main__':
    main()