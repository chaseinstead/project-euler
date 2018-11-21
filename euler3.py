''''Largest prime factor (Problem 3)
"The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?'''

import math
from eulerlibrary import prime_generator


def prime_factors(n):
    '''finds all prime factors of a given number n'''
    prime_factors = []
    prime_numbers = prime_generator(n)
    max_possible = int(math.sqrt(n) + 1)

    if n < 2: 
    	return []
    
    while n % 2 == 0:
       prime_factors.append(2)
       n = n // 2

    for prime in prime_numbers:
        while n % prime == 0:
            prime_factors.append(prime)
            n = n // prime
        
        if n == 1:
            return prime_factors


print("Solution to Euler #3: {}".format(prime_factors(600851475143)[-1]))