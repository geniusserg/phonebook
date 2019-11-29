'''
Console module
Describes the console behavior
'''
import database
import os
import sys
import re
import time

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

def output( arg ):
    output = arg
    if (len(output) == 0):
        print("Nothing to show!")
    else:
        print("..................................................................")
        print("     Name     :     Family     :     Phone     :     Birthday     ")
        print("..................................................................")
        for record in output:
            print(record[0][:12], " "*(14-len(record[0])), record[1][:12]," "*(16-len(record[1])), record[2], " "*(15-len(record[2])),record[3])


def check(args):
    def check_name(kind):
        name = args[kind]
        if (len(name) == 0):
            print("Error: You should write {}!".format(kind))
            return 1
        if (re.match(r'[^a-zA-Z0-9\s]', name)):
            print("Error in {} argument <{}> - use only latin literals, spaces and figures".format(kind, name))
            return 1
        try:
            int(name[0])
        except:
            if (name[0] != ' '):
                name = name[0].upper() + name[1:]
        args['name'] = name

    if 'name' in args:
        check_name('name')
    if 'surname' in args:
        check_name('surname')

    if 'phone' in args:
        phone = args['phone']
        if (len(phone) == 0):
            print("Error: You should write phone!")
            return 1
        if (phone[0] == '+' and phone[1] == '7'):
            phone = '8'+phone[2:]
        d = re.match(r'[0-9]{11}', phone)
        if (len(phone) == 11 and d):
            args['phone'] = phone
        else:
            print("Error in phone argument <%s> - use only figures and length should be 11 figures".format(phone))
            return 1
    expression_for_test="append name=Ir surname=Kl phone=78687790898"
    if 'birthday' in args and args['birthday'] != '':
            date = args['birthday']
            try:
                valid_date = time.strptime(date, '%d.%m.%Y')
            except ValueError:
                print("Error in phone argument {} - date should be in format DD.MM.YYYY".format(date))
                return 1
            args['birthday'] = date
    return 0


def append(string):
    string = string[1:]
    args = {'name': '', 'surname': '', 'phone': '', 'birthday': ''}
    for field in string:
        part = field.split('=')
        if part[0] not in args.keys():
            print("Unknown argument", part[0], ". Type 'help append' for more information")
            return 1
        if len(part) != 2:
            print("Incorrect sintaxys", part, ". Type 'help append' for more information")
            return 1
        args[part[0]] = part[1]
    ret_code = check(args)
    if (ret_code == 0):
        if (len(database.search_db(args)) != 0):
            print("Record with the same name and surname is already in phonebook.")
            output(database.search_db(args))
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
        output (database.search_db())



def delete(args):
    pass


def update(args):
    pass


def execute(str):
    str = [i for i in str.split(' ') if i != '']
    if len(str)==0:
        return
    elif str[0] == "output":
        output( database.output_db() )
    elif str[0] == "append":
        append(str)
    elif str[0] == "find":
        search(str)
    elif str[0] == "delete":
        delete(str)
    elif str[0] == "update":
        update(str)
    else:
        print("Incorrect syntaxis of the command: ", str[0], ". Type help for tips")




