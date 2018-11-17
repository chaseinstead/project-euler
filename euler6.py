def sum_of_squares(upto):
	return sum([number ** 2 for number in range(1, upto +1)])

def square_of_sum(upto):
	return sum([number for number in range(1, upto +1)]) **2

upto = 100
solution = square_of_sum(upto) - sum_of_squares(upto)

print("Solution to Euler #6 is: {}".format(solution))