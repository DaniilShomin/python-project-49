from brain_games.games.calc import calc
from brain_games.modules import welcome_user


def main():    
    name = welcome_user()  
    calc(name)


if __name__ == '__main__':
    main()