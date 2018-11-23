"""
Factorial digit sum
Problem 20 
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import math

factorial_100 = [int(i) for i in list(str(math.factorial(100)))]
solution = sum(factorial_100)

print("Solution to Euler # 20: {}".format(solution))