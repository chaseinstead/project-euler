'''
Circular primes
Problem 35 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import math
from eulerlibrary import *

maxnumber = 1000000
primes = set(primes_to(maxnumber))


def rotate_number(number):
	a = str(number)
	return [a[i:] + a[:i] for i in range(len(a))]


def is_circular_prime(number):
	return all([int(x) in primes for x in rotate_number(str(number))])


circular_primes_found = 0

for number in primes:
	if is_circular_prime(number):
		circular_primes_found += 1


print(circular_primes_found)