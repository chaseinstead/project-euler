'''
Square digit chains
Problem 92 
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

import math

found = 0
leads_to_89 = set([89])
leads_to_1 = set([1])

def add_sq_of_digit(number):
	return sum([int(n) ** 2 for n in list(str(number))])


def arrives_at_89(number):

	if number in leads_to_89:
		return True
	if number in leads_to_1:
		return False

	path = [number]

	while True:
		path.append(add_sq_of_digit(path[-1]))
		if path[-1] in leads_to_89:
			leads_to_89.update(path)
			return True
		if path[-1] in leads_to_1:
			leads_to_1.update(path)
			return False


for number in range (10 ** 7, 2, -1):
	#print("testing:", number)
	#print(len(leads_to_1), len(leads_to_89))
	arrives_at_89(number)

print(len(leads_to_89))