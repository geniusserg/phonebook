'''
Core module
Danilov Sergey 18PI2 6th Group IAD
'''
import database
import os
import re
import time


def open():
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
    print("""
    HELP
    """)


def output( arg, id = False ):
    output = arg
    __id = -1
    if (len(output) == 0):
        print("Nothing to show!")
    else:
        print("..................................................................")
        print("     Name     :     Family     :     Phone     :     Birthday     ")
        print("..................................................................")
        for record in output:
            if (id):
                __id += 1
            else:
                __id = ''
            print(__id,':',record[0][:12], " "*(10-len(record[0])), record[1][:12]," "*(16-len(record[1])), record[2], " "*(15-len(record[2])),record[3])


def check(args, strong = True):
    def check_name(kind):
        name = args[kind]
        if (len(name) == 0):
            if strong:
                print("Error: You should write {}!".format(kind))
                return 1
            else:
                return 0
        if (re.match(r'[^a-zA-Z0-9\s]', name)):
            print("Error in {} argument <{}> - use only latin literals, spaces and figures".format(kind, name))
            return 1
        try:
            int(name[0])
        except:
            if (name[0] != ' '):
                name = name[0].upper() + name[1:]
        args[kind] = name

    ret_name = 0
    if 'name' in args:
        ret_name = check_name('name')
    if 'surname' in args:
        ret_name = check_name('surname')

    if (ret_name == 1):
        return 1


    def phone_check():
        phone = args['phone']
        if (len(phone) == 0):
            if strong:
                print("Error: You should write phone!")
                return 1
            else:
                return 0
        if (phone[0] == '+' and phone[1] == '7'):
            phone = '8' + phone[2:]
        d = re.match(r'[0-9]{11}', phone)
        if (len(phone) == 11 and d):
            args['phone'] = phone
        else:
            print("Error in phone argument <{}> - use only figures and length should be 11 figures".format(phone))
            return 1

    ret_phone = 0
    if 'phone' in args:
        ret_phone = phone_check()
    if (ret_phone == 1):
        return 1

    expression_for_test="append name=Ir surname=Kl phone=78687790898"
    if 'birthday' in args and args['birthday'] != '':
            date = args['birthday']
            try:
                valid_date = time.strptime(date, '%d.%m.%Y')
            except ValueError:
                try:
                    valid_date = time.strptime(date, '%d.%m')
                except ValueError:
                    print("Error in phone argument {} - date should be in format DD.MM.YYYY or DD.MM".format(date))
                    return 1
            args['birthday'] = date
    return 0


def separate(string, args):
    for field in string:
        part = field.split('=')
        if part[0] not in args.keys():
            print("Unknown argument", part[0], ". Type 'help' for more information")
            return 1
        if len(part) != 2:
            print("Incorrect sintaxys", part, ". Type 'help' for more information")
            return 1
        args[part[0]] = part[1]
    return args


def append(string):
    string = string[1:]
    args = {'name': '', 'surname': '', 'phone': '', 'birthday': ''}
    args = separate(string, args)
    if args == 1:
        return 1
    ret_code = check(args)
    if (ret_code == 0):
        if (len(database.search_db({'name':args['name'], 'surname':args['surname']})) != 0):
            print("Record with the same name and surname is already in phonebook.")
            output(database.search_db({'name':args['name'], 'surname':args['surname']}))
            print()
            print("You can change the value of current field with 'update' command. Type 'help' for more information")
        else:
            database.append_db(args)
    else:
        return


def search(string):
    string = string[1:]
    args = {'name': '', 'surname': '', 'phone': '', 'birthday': ''}
    args = separate(string, args)
    if args == 1:
        return 1
    ret_code = check(args, strong = False)
    if ret_code == 0:
        result = []
        if (args['birthday'] != '' and len(args['birthday'].split('.')) == 2):
            birthday = args['birthday']
            args['birthday'] = ''
            out = database.search_db(args)
            for item in out:
                try:
                    if item[3].index(birthday) == 0:
                        result.append(item)
                except:
                    pass
        output(result)


def delete(string):
    string = string[1:]
    args = {'name': '', 'surname': '', 'phone':''}
    args = separate(string, args)
    if args == 1:
        return 1
    if args['name'] == '' and args['surname'] == '' and args['phone'] != '':
        ret_code = check(args, strong=False)
    else:
        args['phone'] == ''
        ret_code = check(args, strong=True)
    if ret_code == 0:
        dbsearchres = database.search_db(args)
        if len(dbsearchres) != 0:
            if (len(dbsearchres) != 1):
                print("we found {} records with the same parameters, which currently do you want to delete now? Type here the id of the chosen record".format(len(dbsearchres)))
                output(dbsearchres, id=True)
                chosen_id = int(input())
                if (chosen_id >= 0 and chosen_id < len(dbsearchres)):
                    chosenrecord = dbsearchres[chosen_id]
                    ret_code = database.delete_db({'name': chosenrecord[0], 'surname': chosenrecord[0], 'phone': chosenrecord[2], 'birthday': chosenrecord[3]})
                else:
                    print("Chose right id of record. Try again!")
                    return 0
            ret_code = database.delete_db(args)
            if ret_code == 0:
                print("Record deleted sucessfully!")
            else:
                pass
        else:
            print("We can not find the record with the same name and surname.")


def update(string):
    string = string[1:]
    args = {'name': '', 'surname': ''}
    args = separate(string, args)
    if args == 1:
        return 1
    ret_code = check(args, strong=True)
    if ret_code == 0:
        if len(database.search_db(args)) != 0:
            args_to_update = {'name': '', 'surname': '', 'phone': '', 'birthday': ''}
            print("Now input your changes:")
            changes = [part for part in input().split(' ') if part != '']
            args_to_update = separate(changes,  args_to_update)
            if args_to_update == 1:
                return 1
            ret_code = check(args_to_update, strong=False)
            if ret_code == 1:
                return 1
            ret_code = database.update_db(args, args_to_update)
            if ret_code == 0:
                print("Record updated sucessfully!")
            else:
                pass
        else:
            print("We can not find the record with the same name and surname.")


def execute(str):
    str = [i for i in str.split(' ') if i != '']
    if len(str)==0:
        return
    elif str[0] == "output":
        output( database.output_db() )
    elif str[0] == "append":
        append(str)
    elif str[0] == "search":
        search(str)
    elif str[0] == "delete":
        delete(str)
    elif str[0] == "update":
        update(str)
    else:
        print("Incorrect syntaxis of the command: ", str[0], ". Type help for tips")




