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

def delete_db(args):
    try:
        runner = "DELETE FROM phonebook WHERE "
        array = []
        for field in args:
            if args[field] != '':
                runner += field + '=? AND '
                array.append(args[field])
        runner = runner[:-4]
        cursor.execute(runner, tuple(array))
        db.commit()
        return 0
    except:
        print("WARN: Unexpected error when deleting into database. Restart app and try it again")
        return 1

def update_db(args, args_to_update):
    try:
        runner = "UPDATE phonebook SET "
        array = []
        for field in args_to_update:
            if args_to_update[field] != '':
                runner += field + '=? AND '
                array.append(args_to_update[field])
        runner = runner[:-4]
        runner += ' WHERE '
        for field in args:
            if args[field] != '':
                runner += field + '=? AND '
                array.append(args[field])
        runner = runner[:-4]
        cursor.execute(runner, tuple(array))
        db.commit()
        return 0
    except:
        print("WARN: Unexpected error when updating database. Restart app and try it again")
        return 1