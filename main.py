import console
import sys

if __name__ == "__main__":
    print("PhoneBook v1.0, Danilov Sergey. 6th Group IAD. ")
    console.open_db()
    print("Database has been loaded sucessfully")
    console.print_help()
    while True:
        print(">>> ", end = '')
        command = input()
        if command == "quit" or command == "q":
            sys.exit(0)
        else:
            console.execute(command)


