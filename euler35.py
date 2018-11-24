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

def prepare_primes_for_circular_test(primes):
	primestrings = []
	for number in primes:
		primestrings.append(str(number))
	return primestrings

primestrings = prepare_primes_for_circular_test(primes)

def rotate_number(number):
	a = number
	rotates = [int(number)]
	for i in range(len(a) -1):
		b = a[1:] + a[0]
		rotates.append(int(b))
		a = b
	return rotates

solution_list = []

for number in primes:
	rotated_nums = rotate_number(str(number))

	if all([int(x) in primes for x in rotated_nums]): #lieber gucken ob zahl in der prime list ist!
		solution_list.append(number)

print(len(solution_list))
"""
def circular_prime_test(rotates):

	for number in rotates:

		number_len = len(number)

		if number_len == 1:
			newnumbers.append(number)
		if number_len > 1 < 3:
			if is_prime(int(number[::-1])):
				newnumbers.append(number)
				continue

	return newnumbers
"""

#c = circular_prime_test(primestrings)
#print(c)