def input_num():
    try:
        num = int(input("Enter number: "))
        print_nums(num)
    except ValueError as err:
        print(err)


def print_nums(number):
    for num in range(number):
        print(num + 1)


if __name__ == '__main__':
    input_num()

