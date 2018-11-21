# 10001st prime (Problem 7) 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def n_primes(n):
    '''finds the first n primes'''

    if n < 1:
        return []
    if n == 1:
        return [2]
    if n == 2:
        return [2, 3]

    counter = 3
    primes = [2, 3]


    while True:
        counter+= 2
        max_possible = int(math.sqrt(counter) + 1)

        if len(primes) >= n:
            return primes
        for prime in primes:
            if prime >= max_possible:
                primes.append(counter)
                break
            if counter % prime == 0:
                break

        else: 
            primes.append(counter)

print(n_primes(10001)[-1])