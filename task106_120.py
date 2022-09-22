import random


def main_menu():
    print(" 1) Addition\n", "2) Subtraction\n")
    user_choose = input("Enter number: ")
    if user_choose == "1":
        addition()
    elif user_choose == "2":
        subtraction()
    else:
        print("Enter correct number.")


def addition():
    try:
        rand_num1 = random.randint(5, 20)
        rand_num2 = random.randint(5, 20)
        user_num = int(input(f"{rand_num1} + {rand_num2} = "))
        correct_num = rand_num1 + rand_num2
        comp_num(user_num, correct_num)
    except ValueError as err:
        print(err)


def subtraction():
    try:
        rand_num1 = random.randint(25, 50)
        rand_num2 = random.randint(1, 25)
        user_num = int(input(f"{rand_num1} - {rand_num2} = "))
        correct_num = rand_num1 - rand_num2
        comp_num(user_num, correct_num)
    except ValueError as err:
        print(err)


def comp_num(user_num, correct_num):
    if user_num == correct_num:
        print("Correct.")
    else:
        print(f"Incorrect, the answer is {correct_num}")


if __name__ == '__main__':
    main_menu()
