def task91_109():
    file_subjects = open("Subjects.txt", "r")
    file_subjects.close()
    choose_answer = input("Choose a selection (1, 2, 3): ")
    if choose_answer == "1":
        file_subjects = open("Subjects.txt", "w")
        name_of_subject = input("Enter name of subject: ")
        file_subjects.write(f"{name_of_subject}\n")
    elif choose_answer == "2":
        file_subjects = open("Subjects.txt", "r")
        print(file_subjects.read())
    elif choose_answer == "3":
        file_subjects = open("Subjects.txt", "a")
        name_of_subject = input("Enter name of subject: ")
        file_subjects.write(f"{name_of_subject}\n")
    else:
        print("Enter right number.")


if __name__ == '__main__':
    task91_109()
