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


if __name__ == '__main__':
    task87_99()