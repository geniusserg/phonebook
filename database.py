import sqlite3
import os

cursor = object()
db = object()

def init_db(name):
    global cursor
    global db

    if os.path.exists(name):
        try:
            db = sqlite3.connect(name)
        except(Exception):
            return 1
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


def append_db(args, args_db = []):
    if args_db == []:
        global db
        global cursor
    else:
        db = args_db[0]
        cursor = args_db[1]

    try:
        list_to_append = [args[i] for i in args]
        query = tuple(list_to_append)
        cursor.execute("INSERT INTO phonebook VALUES (?,?,?,?)", query)
        db.commit()
    except:
        return 1
    return 0

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