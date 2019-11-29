import sqlite3
import os

cursor = object()
db = object()

def init_db(name):
    global cursor
    global db

    db = sqlite3.connect(name)
    if os.path.exists(name):
        cursor = db.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS phonebook(
                    name   TEXT,
                    surname TEXT,
                    phone   TEXT,
                    birthday    TEXT
                )""")
        return 0
    else:
        return 1


def insert_db(name, surname, phone, birthday):
    try:
        cursor.executemany("INSERT INTO phonebook VALUES (?,?,?,?)", [(name, surname, phone, birthday)])
        db.commit()
    except:
        print("WARN: Unexpected error when inserting into database. Restart app and try it again")


def output_db():
    try:
        cursor.execute("SELECT * FROM phonebook")
        return cursor.fetchall()
    except:
        print("Unexpected error when output database. Restart app and try it again")

