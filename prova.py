my_file = open('shampoo_sales.csv')
my_list = []
for line in my_file:
    elements = line.split(',')
    if elements[1] != 'Sales\n':
        my_list.append(elements) 
print (my_list)