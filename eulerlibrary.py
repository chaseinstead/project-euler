import math

def is_prime(n):
    '''evaluates whether a given number is prime'''
    if n % 2 == 0:
        return False
    for number in range(3, int(math.sqrt(n)) +1, 2):
        if n % number == 0:
            return False
    return True


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


def primes_to(n):
    '''finds all primes up to n. see prime_generator(n) for a more efficient solution'''
    primes = [2]
    for i in range(3, n + 1, 2):
        last_possible = int(math.sqrt(i) + 1)
        for test in primes:
            if test > last_possible:
                primes.append(i)
                break
            if i % test == 0:
                break
        else:
            primes.append(i)
    return primes


def prime_generator(n):
    '''finds all primes up to n, more efficient'''
    number = 1
    while number < (n + 1):
        number += 1
        if is_prime(number):
            yield number


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


def prime_factors(max):
    prime_factor_list = []
    max = 128
    if max <= 1:
        return prime_factor_list
    while max % 2 == 0:
        prime_factor_list.append(2)
        max = max // 2
    for number in range(3, max, 2):
        if max % number == 0:
            yield number
            print(number)
        yield max // number
        if number >= max:
            return prime_factor_list