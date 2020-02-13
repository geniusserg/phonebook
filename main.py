import core
import sys
import os

if __name__ == "__main__":
    print("LabWork_1_PhoneBook. Danilov Sergey. 6th Group IAD")  
    if (os.environ["TEST_PY"]):
        core.print_help()
        sys.exit(0)
    core.init()
    print("Database has been loaded sucessfully")
    print("Type 'help' to open instruction of all functions of the program or 'quit' to exit. Have fun!")
    while True:
        print(">>> ", end = '')
        command = input()
        if command == "quit" or command == "q":
            sys.exit(0)
        else:
            try:
                core.execute(command)
            except:
                print("Unexpected error while executing '{}' command. Please, send respond about error on issues page in git repository")



