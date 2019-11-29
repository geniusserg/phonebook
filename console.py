'''
Console module
Describes the console behavior
'''
import database
import os
import sys
import re

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
            print(record[0][:12], " "*(14-len(record[0])), record[1][:12]," "*(16-len(record[1])), record[2], " "*(15-len(record[2])),record[3])


def check(args):
    if 'name' in args:
        with args['name'] as name:
            if (re.search(r'[^a-zA-Z0-9\s]]', name)):
                print("Error in name argument <%s> - use only latin literals, spaces and figures".format(name))
                return 1
            name[0].upper()
    if 'surname' in args:
        with args['surname'] as name:
            if (re.search(r'[^a-zA-Z0-9\s]]', name)):
                print("Error in surname argument <%s> - use only latin literals, spaces and figures".format(name))
                return 1
            name[0].upper()
    if 'phone' in args:
        with args['phone'] as phone:
            if (phone[0] == '+' and phone[1] == '7'):
                phone[1] = '8'+phone[2:]
            if (len(phone) != 11 or re.search(r'[^0-9]]', phone)):
                print("Error in phone argument <%s> - use only figures, a length should be 11".format(phone))
                return 1
    if 'birthday' in args and 'birthday' != '':
        with args['birthday'] as bday:
            result = 0
            if len(bday) != 10:
                result |= 1
            else:
                for i in [j for j in range(10) if j != 2 and j != 5]:
                    result |= re.search(r'[^0-9]', bday[i])
            if result == 1:
                print("Error in phone argument <%s> - date should be in format DD.MM.YYYY".format(bday))
                return 1
    return 0


def append(string):
    args = {'name': '', 'surname': '', 'phone': '', 'birthday': ''}
    for field in string:
        part = field.split('=')
        if part[0] not in args.keys():
            print("Unknown argument", part[0], ". Type 'help append' for more information")
        if len(part) != 2:
            print("Incorrect sintaxys", part, ". Type 'help append' for more information")
        args[part[0]] = part[1]
    ret_code = check(args)
    if (ret_code == 0):
        if (len(database.search_db(args)) != 0):
            print("Record with the same name and surname is already in phonebook.")
            for part in database.search_db(args):
                print(part, end = ' ')
            print()
            print("You can change the value of current field with 'update' command. Type 'help update'")
        else:
            database.append_db(args)
    else:
        return


def search(string):
    args = {'name': '', 'surname': '', 'phone': '', 'birthday': ''}
    for field in string:
        part = field.split('=')
        if part[0] not in args.keys():
            print("Unknown argument", part[0], ". Type 'help search' for more information")
        if len(part) != 2:
            print("Incorrect sintaxys", part, ". Type 'help search' for more information")
        args[part[0]] = part[1]
    ret_code = check(args)
    if (ret_code == 0):
        output = database.search_db()
        if (len(output) == 0):
            print("Nothing searched on your call")
        else:
            print("..................................................................")
            print("     Name     :     Family     :     Phone     :     Birthday     ")
            print("..................................................................")
            for record in output:
                print(record[0][:12], " " * (14 - len(record[0])), record[1][:12], " " * (16 - len(record[1])), record[2]," " * (15 - len(record[2])), record[3])


def delete(args):
    pass


def update(args):
    pass


def execute(str):
    str = [i for i in str.split(' ') if i != '']
    if len(str)==0:
        return
    elif str[0] == "output":
        output()
    elif str[0] == "append":
        append(str)
    elif str[0] == "find":
        search(str)
    elif str[0] == "delete":
        delete(str)
    elif str[0] == "update":
        pass
    elif str[0] == "age":
        pass
    else:
        print("Incorrect syntaxis of the command: ", str[0], ". Type help for tips")




