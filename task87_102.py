def task87_102():
    list_of_settings = {}
    for i in range(4):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        shoe = int(input("Enter shoe size: "))
        list_of_settings[name] = {"Age": age, "Shoe size": shoe}
    ask = input("Enter a name: ")
    print(f"Age: {list_of_settings[ask]['Age']}, shoe size: {list_of_settings[ask]['Shoe size']}")


if __name__ == '__main__':
    task87_102()
