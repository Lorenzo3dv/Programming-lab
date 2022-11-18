def sum_list(my_list):
    somma = 0
    for i in my_list:
        somma+=i
    return somma

my_list = [1,2,3,4,5]
print ('la somma è:', sum_list(my_list))