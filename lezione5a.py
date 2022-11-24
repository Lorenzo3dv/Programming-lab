class CSVFile():
    def __init__(self, name):
        self.name = name
        
    def get_data(self):
        try:
            my_file = open(self.name)
            my_list = []
            for line in my_file:
                elements = line.split(',')
                if elements[1] != 'Sales\n':
                    my_list.append(elements)
            return my_list
        except FileNotFoundError:
            print ('Errore, il file che si vuole usare non esiste.')

file = CSVFile ('file')
print (file.get_data())