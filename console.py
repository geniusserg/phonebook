'''
Console module
Describes the console behavior
'''
import database
import os
import sys

def open_db():
    ret_code = 2
    while ret_code:
        if (ret_code == 1):
            print("Something went wrong while opening database. Try again!")
        if not (os.path.exists("phonebook.db")) or ret_code == 1:
            print("Enter the name of phonebook you want to use or leave it empty to create new. To close program type here command - exit")
            user_input = input()
            if (user_input == ""):
                ret_code = database.init_db("phonebook.db")
            else:
                ret_code = database.init_db(user_input)
        else:
            ret_code = database.init_db("phonebook.db")


def print_help():
    print("HELP")

def output():
    output = database.output_db()
    if (len(output) == 0):
        print("PhoneBook is empty yet. Add the first contact!")
    else:
        print("..................................................................")
        print("     Name     :     Family     :     Phone     :     Birthday     ")
        print("..................................................................")
        for record in output:
            print(record[0][:12], " "*(14-len(record[0])), record[1][:12]," "*(16-len(record[0])), record[2], " "*(15-len(record[0])),record[3])


def execute(str):
    str = [i for i in str.split(' ') if i != '']
    if str[0] == "output":
        output()
    if str[0] == "append":
        pass
    if str[0] == "find":
        pass
    if str[0] == "delete":




