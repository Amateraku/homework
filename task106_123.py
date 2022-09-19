def main_menu():
    print("\n 1) Add to file\n", "2) View all records\n", "3) Delete a record\n", "4) Quit program\n")
    user_choose = input("Enter number of function: ")
    if user_choose == "1":
        add()
    elif user_choose == "2":
        show()
    elif user_choose == "3":
        delete()
    elif user_choose == "4":
        close()
    else:
        print("Enter correct number.")
        main_menu()


def add():
    file = open("salaries.csv", "a")
    user_add = input("Enter name and salary(nn, ss): ")
    file.write(user_add + "\n")
    file.close()
    main_menu()


def show():
    print("")
    file = open("salaries.csv")
    for line in file.readlines():
        print(line.strip())
    file.close()
    main_menu()


def delete():
    try:
        file = open("salaries.csv")
        lines = file.readlines()
        file.close()
        line_to_delete = int(input("Enter number of line to delete: "))
        lines.pop(line_to_delete - 1)
        file = open("salaries.csv", "w")
        for line in lines:
            file.write(line)
        file.close()
        main_menu()
    except ValueError:
        print("Enter number.")
        main_menu()


def close():
    pass


if __name__ == '__main__':
    main_menu()
