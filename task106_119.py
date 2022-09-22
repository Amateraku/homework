import random


def random_num():
    try:
        min_num = int(input("Enter min number: "))
        max_num = int(input("Enter max number: "))
        rand_num = random.randint(min_num, max_num)
        guess(rand_num)
    except ValueError as err:
        print(err)


def guess(rand_num):
    print("I am thinking of a number...")
    user_num = int(input("Guess the number: "))
    right_or_incorrect(rand_num, user_num)


def right_or_incorrect(rand_num, user_num):
    try:
        if rand_num == user_num:
            print("Congratulations, you guessed.")
        else:
            if rand_num > user_num:
                print("Too small")
            elif rand_num < user_num:
                print("too big")
            guess(rand_num)
    except ValueError as err:
        print(err)
        guess(rand_num)


if __name__ == '__main__':
    random_num()
