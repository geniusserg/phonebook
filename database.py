class DataBase:
    __list = [] #list of filelds Field
    counter = 0
    def __init__(self, file):
        self.dbfile = open(file, 'r')

        while True:
            string = self.dbfile.readline()
            field = {}

            if string == '':
                break
            else:
                field = parse(string)

            ret_code = self.addField(field)



    def addField(self, args):
        field = {}
        self.counter += 1
        field['id'] = self.counter

        for i in args:
            check_result = check(i, args[i])
            if (check_result == ''):
                field[i] = args[i]
            else:
                return check_result

        self.__list.append(field)



def parse(string):
    records = string.split('|')
    field = dict()
    field['name'] = records[0]
    field['family'] = records[1]
    field['phone'] = records[2]
    field['type'] = records[3]
    field['birthday'] = records[4]
    return field


def check(type, value):
    return ''