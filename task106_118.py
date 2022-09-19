def input_num():
    num = int(input("Enter number: "))
    print_nums(num)


def print_nums(number):
    try:
        for num in range(number):
            if num + 1 < number:
                print(num + 1)
    except ValueError:
        print(ValueError)


if __name__ == '__main__':
    input_num()

