import csv


def task98_112():
    books = open("books.csv", "w")
    records = ("To kill a Mockingbird, Harper Lee, 1960", "A Brief History of Time, Stephen Hawking, 1988",
               "A Brief History of Time, Stephen Hawking, 1988", "The Great Gatsby, F. Scott Fitzgerald, 1922",
               "Pride and Prejudice, Jane Austen, 1813")
    for record in records:
        books.write(record + "\n")
    new_record = input("Enter name of book, author and graduation year (bb, aa, yy): ")
    books.write(new_record + "\n")
    books.close()
    books = open("books.csv")
    for line in books.readlines():
        print(line)


if __name__ == '__main__':
    task98_112()
