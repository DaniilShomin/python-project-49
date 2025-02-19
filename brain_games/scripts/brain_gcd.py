from brain_games.modules import gcd, welcome_user


def main():
    name = welcome_user()  
    gcd(name)


if __name__ == '__main__':
    main()