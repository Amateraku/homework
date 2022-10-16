import sqlite3


def task144_142():
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Authors")
        for row in cursor.fetchall():
            print(row)
        location = input("Enter a place of birth: ")
        cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
        FROM Books,Authors WHERE Authors.Name = Books.Author AND Authors.Place_of_Birth = ?
        """, [location])
        for row in cursor.fetchall():
            print(row)


if __name__ == '__main__':
    task144_142()
