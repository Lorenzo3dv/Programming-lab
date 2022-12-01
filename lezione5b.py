class CSVFile():
    def __init__(self, name):
        self.name = name
        self.can_read = True 
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False 
            print ('Errore in apertura del file:"{}"'.format(e))
        
    def get_data(self):
        if self.can_read != True:
            print ('Errore, non esiste il file')
            
            return None
            
        else: 
            my_file = open(self.name)
            my_list = []
            for line in my_file:
                elements = line.split(',')
                if elements[1] != 'Sales\n':
                    my_list.append(elements)
            return my_list


class NumericalCSVFile (CSVFile):
    lista_dati = super().get_data()
    lista_valori = []
    
    