def sum_csv(file_name):
    my_file = open(file_name, 'r')
    valori = []
    for line in my_file:
        elements = line.split(',')
        if elements[1] != 'Sales\n':
            valori.append(float(elements[1]))
        somma = sum(valori)
    my_file.close()
    return somma
