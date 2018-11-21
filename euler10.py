# Summation of primes (Problem 10) 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below 2000000.

import math
from eulerlibrary import *

maxi = 2000000
solution = sum(primes_to(maxi))
print("Solution to Euler # 10: {}".format(solution)) # takes 4,3 seconds