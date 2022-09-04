def task87_103():
    list_of_settings = {}
    for i in range(4):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        shoe = int(input("Enter shoe size: "))
        list_of_settings[name] = {"Age": age, "Shoe size": shoe}
    for i in list_of_settings:
        print(f"Name: {i}, age: {list_of_settings[i]['Age']}")


if __name__ == '__main__':
    task87_103()
