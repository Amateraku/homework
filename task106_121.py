def main_menu():
    functions_nums = ("1", "2", "3", "4", "5")
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


def show():
    file = open("names.txt")
    print(file.read())
    file.close()
    main_menu()


def add():
    file = open("names.txt", "a")
    file.write(input("Enter name to add: ") + "\n")
    file.close()
    main_menu()


def delete():
    file = open("names.txt")
    names = file.readlines()
    file.close()
    name_to_del = input("Enter name to delete: ")
    file = open("names.txt", "w")
    for name in names:
        if not name_to_del == name.strip():
            file.write(name)
    file.close()
    main_menu()


def edit():
    file = open("names.txt")
    names = file.readlines()
    file.close()
    name_to_remove = input("Enter name to edit: ")
    new_name = input("Enter new name: ")
    for name in names:
        if name_to_remove == name.strip():
            names[names.index(name)] = new_name + "\n"
    file = open("names.txt", "w")
    for name in names:
        file.write(name)
    file.close()
    main_menu()


def close():
    pass


if __name__ == '__main__':
    main_menu()
