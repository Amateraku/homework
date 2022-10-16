import sqlite3


def main():
    functions = {
        "1": view_phones,
        "2": add,
        "3": search_surname,
        "4": delete,
        "5": close
    }
    print('''1) View phone book  2) Add to phone book  3) Search for surname  
4) Delete person from phone book  5) Quit\n''')
    while True:
        selection = input("Enter number: ")
        for function in functions:
            if selection == function:
                functions[function]()


def view_phones():
    with sqlite3.connect("phonebook.db") as db:
        cursor = db.cursor()
        rows = cursor.execute("SELECT * FROM Names")
        for row in rows.fetchall():
           print(row)


def add():
    with sqlite3.connect("phonebook.db") as db:
        cursor = db.cursor()
        new_id = input("Enter id: ")
        new_name = input("Enter first name: ")
        new_second_name = input("Enter surname: ")
        new_phone_number = input("Enter phone number: ")
        cursor.execute(f''' INSERT INTO Names(id, first_name, second_name, phone_number)
VALUES (?, ?, ?, ?)''', (new_id, new_name, new_second_name, new_phone_number))
        db.commit()


def search_surname():
    with sqlite3.connect("phonebook.db") as db:
        cursor = db.cursor()
        select_surname = input("Enter a surname: ")
        cursor.execute("SELECT * FROM Names WHERE second_name = ?", [select_surname])
        for row in cursor.fetchall():
            print(row)


def delete():
    with sqlite3.connect("phonebook.db") as db:
        cursor = db.cursor()
        select_id = int(input("Enter id: "))
        cursor.execute("DELETE FROM Names WHERE id = ?", [select_id])
        cursor.execute("SELECT * FROM Names")
        for row in cursor.fetchall():
            print(row)
        db.commit()


def close():
    quit()


if __name__ == '__main__':
    main()
