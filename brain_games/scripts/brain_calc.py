from brain_games.modules import calc, welcome_user


def main():    
    name = welcome_user()  
    calc(name)


if __name__ == '__main__':
    main()