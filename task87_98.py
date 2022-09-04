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


if __name__ == '__main__':
    task87_98()
