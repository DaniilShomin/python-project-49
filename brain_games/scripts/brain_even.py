from brain_games.games.even import parity_check
from brain_games.modules import welcome_user


def main():
    name = welcome_user()  
    parity_check(name)


if __name__ == '__main__':
    main()