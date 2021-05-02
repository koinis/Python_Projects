n = int(input('Please enter a natural number greater than 1: '))

primes = []
for tested in range(2,n+1):
    for p in primes:
        if not tested % p: # exact division by p
            break
    else:
        primes.append(tested)

print(primes)