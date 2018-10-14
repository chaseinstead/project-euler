import math

def is_prime(n):
    prime_meter = True
    for number in range(2, n):
        if n % number == 0:
            prime_meter = False
    return prime_meter

def primes_to(n):
    """ findet alle primzahlen bis n """
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

def n_primes(n):
    """ die ersten n primzahlen finden"""
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
    """ findet alle primzahlen bis n """
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

def PrimesTo(n):
    ''' findet alle primzahlen bis n, generator = effizienter'''
    number = 1
    while number < (n + 1):
        number += 1
        if is_prime(number):
            yield number

primz = PrimesTo(128)

# for p in primz:
 #   print(p)


def prime_factors(n):
    prime_factors = []
    prime_numbers = PrimesTo(n)
    max_possible = int(math.sqrt(n) + 1)
    
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2

    for prime in prime_numbers:
        while n % prime == 0:
            prime_factors.append(prime)
            n = n // prime
    if prime >= max_possible:
        return prime_factors

b = prime_factors(10000)
print(b)



def simple_generator_function():
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11

#for value in simple_generator_function():
#    print(value)




our_generator = simple_generator_function()


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

a = prime_factors(128)

#    if 128 % number == 0:
 #       prime_factor_list.append(number)
  #      number = 128 // number
   #     continue
 #   next(our_generator)
  #  if number >= 128 // 2 + 1:
   #     break
#print(prime_factor_list)

def factors(n):
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i 
    else:
        i = next(prime) ## nächste primzahl holen
    return factors