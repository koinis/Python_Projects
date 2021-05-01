x = int(input('enter a number: '))
d = int(input('enter a number: '))

z = x*10
for i in range(10):
    if (z+i) % d == 0:
        print(z+i)