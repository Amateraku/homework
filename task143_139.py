import sqlite3


def task143_139():
    with sqlite3.connect("phonebook.db") as db:
        cursor = db.cursor()
        cmd = '''CREATE TABLE IF NOT EXISTS names(
                id integer PRIMARY KEY,
                first_name text NOT NULL,
                second_name text NOT NULL,
                phone_number integer NOT NULL);'''
        cursor.execute(cmd)
        for _id in range(1, 5):
            cursor.execute(f'''INSERT INTO names(id, first_name, second_name, phone_number)
            VALUES({_id}, "Bob{_id}", "Howels{_id}", "+038410401{_id * 12}32")''')
        db.commit()


if __name__ == '__main__':
    task143_139()
