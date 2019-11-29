import core
import sys

if __name__ == "__main__":
    print("PhoneBook v1.0, Danilov Sergey. 6th Group IAD. ")
    core.open()
    print("Database has been loaded sucessfully")
    core.print_help()
    while True:
        print(">>> ", end = '')
        command = input()
        if command == "quit" or command == "q":
            sys.exit(0)
        else:
            core.execute(command)


