def task91_108():
    file_numbers = open("Names.txt", "a")
    name = input("Enter your name: ")
    file_numbers.write(f"{name}\n")
    file_numbers.close()
    file_numbers = open("Names.txt", "r")
    print(file_numbers.read())
    file_numbers.close()


if __name__ == '__main__':
    task91_108()
