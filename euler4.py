# Largest palindrome product (Problem 4)
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def multiply_all_3_digit_numbers():
    '''multiplies all numbers between 100 and 999 with each other'''
    all_3_digits = []
    for number1 in range(100, 999 + 1):
        for number2 in range (100, 999 + 1):
            all_3_digits.append(number1 * number2)
    return sorted(all_3_digits)


def find_palindromes(products): ## takes 2 seconds: not optimal. see below for better solution
    '''finds all palindromes in a list of "products". only works for three digit multiples'''
    palindrome_list = []
    for number in products:
        b = str(number)
        if len(b) == 5:
            if b[:2] == ''.join(reversed(b[3:])):
                palindrome_list.append(number)
        if len(b) == 6:
            if b[:3] == ''.join(reversed(b[3:])):
                palindrome_list.append(number)
    return sorted(palindrome_list)


a = multiply_all_3_digit_numbers()
#euler4_list = find_palindromes(a)
#print("Solution to Euler #4: {}".format(euler4_list[-1]))



# more efficient solution using string reversals:

def find_palindromes(products): ## 1,2 seconds
    '''finds all palindromes in a list'''
    palindrome_list = []
    for number in products:
        b = str(number)
        if b == b[::-1]:
            palindrome_list.append(number)
    return sorted(palindrome_list)


euler4_list = find_palindromes(a)
print("Solution to Euler #4: {}".format(euler4_list[-1]))