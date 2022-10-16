import sqlite3


def authors():
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS authors(
        Name text PRIMARY KEY,
        Place_of_Birth text''')
        cursor.execute('''INSERT INTO Authors(Name, Place_of_Birth)
        VALUES("Agatha Christie", "Torquay")''')
        cursor.execute('''INSERT INTO Authors(Name, Place_of_Birth)
        VALUES("Cecilia Ahern", "Dublin")''')
        cursor.execute('''INSERT INTO Authors(Name, Place_of_Birth)
        VALUES("J.K.Rowling", "Bristol")''')
        cursor.execute('''INSERT INTO Authors(Name, Place_of_Birth)
        VALUES("Oscar Wilde", "Dublin")''')


def books():
    with sqlite3.connect("BookInfo.db") as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS books(
        ID integer PRIMARY KEY,
        Title text,
        Author text,
        DataPublished integer)''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("1", "De Profundis", "Oscar Wilde", "1905")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("2", "Harry Potter and the chamber of secrets", "J.K.Rowling", "1998")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("3","Harry Potter and the prisoner of Azkaban", "J.K.Rowling", "1999")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("4", "Lyrebird", "Cecilia Ahern", "2017")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("5", "Murder on the Orient Express", "Agatha Christie", "1934")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("6", "Perfect", "Cecilia Ahern", "2017")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("7", "The marble collector", "Cecilia Ahern", "2016")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("8", "The murder on the links", "Agatha Christie", "1923")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("9", "The picture of Dorian Gray", "Oscar Wilde", "1890")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("10", "The secret adversary", "Agatha Christie", "1921")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("11", "The seven dials mystery", "Agatha Christie", "1929")''')
        cursor.execute('''INSERT INTO Books(ID, Title, Author, DatePublished)
        VALUES("12", "The year I met you", "Cecilia Ahern", "2014")''')
        db.commit()


def start():
    authors()
    books()


if __name__ == '__main__':
    start()
