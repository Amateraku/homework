def task91_110():
    file = open("names.txt")
    names = [x.strip() for x in file.readlines()]
    file.close()
    user_name = input("Enter name to delete: ")
    if user_name not in names:
        print("Invalid name.")
    else:
        names.remove(user_name)
        new_file = open("new_names.txt", "w")
        for name in names:
            new_file.write(f"{name}\n")
        new_file.close()


if __name__ == '__main__':
    task91_110()
