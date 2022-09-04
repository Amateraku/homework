def task87_96():
    list_of_numbers = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
    print(list_of_numbers)


def task87_98():
    try:
        list_of_numbers = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
        print(list_of_numbers)
        string_to_add = int(input("Enter number of string: "))
        number_to_add = int(input("Enter number to add: "))
        list_of_numbers[string_to_add - 1].append(number_to_add)
        print(list_of_numbers)
    except ValueError:
        print(ValueError)


def task87_99():
    try:
        list_of_numbers = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
        print(list_of_numbers)
        string = int(input("Enter number of string: "))
        print(list_of_numbers[string - 1])
        column = int(input("Enter number of column: "))
        remove_or_not = input("Remove number? Yes or no: ")
        if remove_or_not == "yes":
            number = int(input("Enter number: "))
            list_of_numbers[string - 1][column - 1] = number
            print(list_of_numbers)
    except ValueError:
        print(ValueError)


def task87_102():
    list_of_settings = {}
    for i in range(4):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        shoe = int(input("Enter shoe size: "))
        list_of_settings[name] = {"Age": age, "Shoe size": shoe}
    ask = input("Enter a name: ")
    print(f"Age: {list_of_settings[ask]['Age']}, shoe size: {list_of_settings[ask]['Shoe size']}")


def task87_103():
    list_of_settings = {}
    for i in range(4):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        shoe = int(input("Enter shoe size: "))
        list_of_settings[name] = {"Age": age, "Shoe size": shoe}
    for i in list_of_settings:
        print(f"Name: {i}, shoe size: {list_of_settings[i]['Age']}")
        print(f"Name: {i}, shoe size: {list_of_settings[i]['Age']}")


if __name__ == '__main__':
    task87_103()
