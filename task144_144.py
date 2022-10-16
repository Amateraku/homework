import sqlite3


def task144_144():
    file = open("BooksList.txt", "w")
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        select_author = input("Enter an author’s name: ")
        cursor.execute('''SELECT * FROM books WHERE Author = ?''', [select_author])


if __name__ == '__main__':
    task144_144()
