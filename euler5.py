# Smallest multiple (Problem 5)
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# This solution works, but is very inefficient. To Do: Find a better solution.

import math

n = 11 * 13 * 17 * 19 * 20 - 1

while True:
	n += 1
	for divisor in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
		if not n % divisor == 0:
			break
	else: 
		print(n)
		break

