def sum_csv(file_name):
    my_file = open(file_name, 'r')
    somma = 0
    for line in my_file:
        elements = line.split(',')
        if elements[1] != 'Sales\n':
            numeri = float(elements[1])
            somma +=numeri
    return somma