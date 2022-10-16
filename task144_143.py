import sqlite3


def task144_143():
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        selected_year = int(input("Enter a year: "))
        cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
        FROM Books WHERE DatePublished > ? ORDER BY DatePublished """, [selected_year])
        for row in cursor.fetchall():
            print(row)


if __name__ == '__main__':
    task144_143()
