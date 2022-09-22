import csv


def task98_112():
    # create_csv_file()
    user_input = input("Enter name of book, author and graduation year (bb,aa,yy): ")
    with open("books.csv", "a") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(user_input.split(","))


def create_csv_file():
    records = (
        "To kill a Mockingbird,Harper Lee,1960",
        "A Brief History of Time,Stephen Hawking,1988",
        "The Great Gatsby,F. Scott Fitzgerald,1922",
        "Pride and Prejudice,Jane Austen,1813"
    )
    with open("books.csv", "w") as file:
        for record in records:
            file.write(record + "\n")


if __name__ == '__main__':
    task98_112()
