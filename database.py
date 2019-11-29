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


def append_db(args):
    try:
        list_to_append = tuple([args[i] for i in args])
        cursor.execute("INSERT INTO phonebook VALUES (?,?,?,?)", list_to_append)
        db.commit()
    except:
        print("WARN: Unexpected error when inserting into database. Restart app and try it again")

def search_db(args):
    try:
        runner = "SELECT * FROM phonebook WHERE "
        array = []
        for field in args:
            if args[field] != '':
                runner += field + '=? AND '
                array.append(args[field])
        runner = runner[:-4]
        cursor.execute(runner, tuple(array))
        return cursor.fetchall()
    except:
        print("WARN: Unexpected error when searching into database. Restart app and try it again")
        return []

def output_db():
    try:
        cursor.execute("SELECT * FROM phonebook")
        return cursor.fetchall()
    except:
        print("Unexpected error when output database. Restart app and try it again")

