import sys


def main_menu():
    functions_nums = ("1", "2", "3", "4", "5")
    while True:
        print("1) Show names   2) Add name   3) Delete name   4) Edit name   5) Close program")
        user_choose = input("Enter number: ")
        if user_choose == functions_nums[0]:
            show()
        elif user_choose == functions_nums[1]:
            add()
        elif user_choose == functions_nums[2]:
            delete()
        elif user_choose == functions_nums[3]:
            edit()
        elif user_choose == functions_nums[4]:
            close()


def improved_menu():
    choices = {
        "1": show,
        "2": add,
        "3": delete,
        "4": edit,
        "5": close
    }
    while True:
        print("1) Show names   2) Add name   3) Delete name   4) Edit name   5) Close program")
        user_choose = input("Enter number: ")
        choices[user_choose]()


def show():
    with open("names.txt") as file:
        print(file.read())


def add():
    with open("names.txt", "a") as file:
        file.write(input("Enter name to add: ") + "\n")


def delete():
    name_to_del = input("Enter name to delete: ")
    with open("names.txt") as file:
        names = file.readlines()
    with open("names.txt", "w") as file:
        for name in names:
            if not name_to_del == name.strip():
                file.write(name)


def edit():
    old_name = input("Enter name to edit: ")
    new_name = input("Enter new name: ")
    with open("names.txt") as file:
        names = file.readlines()
    for name in names:
        if old_name == name.strip():
            names[names.index(name)] = new_name + "\n"
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name)


def close():
    sys.exit()


if __name__ == '__main__':
    improved_menu()
