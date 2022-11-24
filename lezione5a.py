class CSVFile():
    def __init__(self, name):
        self.name = name
        try:
            my_file = open(name)
        except FileNotFoundError:
            print ('Errore, il file che si sta usando non esiste.')

    def get_data(self):
        my_file = open(self.name)
        my_list = []
        for line in my_file:
            elements = line.split(',')
            if elements[1] != 'Sales\n':
                my_list.append(elements)
        return my_list


