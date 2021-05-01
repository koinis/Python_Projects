capital = eval(input('Initial capital: '))
rates = input('Interest rates (%) for the coming years separated by commas: ')

rate = [eval(x) for x in rates.split(',')]
print('Initial capital =',capital)

for i in range(len(rate)):
    capital += capital*rate[i]/100
    print('Capital after year',i+1,'=',capital)
