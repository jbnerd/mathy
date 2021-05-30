"""Plan of attack:
    v1: (2.416296 seconds)
        Generate triangular numbers using the sum of natural numbers formula and check the first number that has more
        than 500 divisors.
    v2: (0.119317 seconds)
        When the prime factorization of a number is produced the total number of divisors are given by
        D(num) = (a_1 + 1) * (a_2 + 1) * (a_3 + 1) ... (a_k + 1) where a_i's are the exponents of the prime factors.
        The required number is expected to be stored in a 32-bit integer, hence a list of prime numbers up to 65500
        should be sufficient to construct the prime factorization of triangular numbers in the search space.
    v3: (0.056504 seconds)
        Since a triangular number is given by n * (n + 1) / 2 and since n, (n + 1) must be co-primes:
        D(num) = D(n/2) * D(n+1) if n is even
               = D(n) * D((n+1)/2) otherwise.
        In this case the prime table constructed up to 1000 is sufficient.
"""
import sys
from functools import reduce

import _init_paths
from lib.utils.generic import Timer
from lib.utils.numeric import sum_of_natural_numbers, get_factors
from lib.utils.primes import get_primes, PrimeFactors


@Timer(name='decorator')
def execute_v1():
    i = 1
    while True:
        triangular_num = sum_of_natural_numbers(i)
        if len(get_factors(triangular_num)) > 498:
            print(triangular_num)
            break
        i += 1


def total_divisors(num, prime_table):
    factors, exponents = PrimeFactors.prime_factorization(num, prime_table)
    exponents = [exp + 1 for exp in exponents]
    return reduce(lambda a, b: a * b, exponents)


@Timer(name='decorator')
def execute_v2():
    prime_table = get_primes(65500)
    i = 4
    while True:
        triangular_num = sum_of_natural_numbers(i)
        if total_divisors(triangular_num, prime_table) > 500:
            print(triangular_num)
            break
        i += 1


@Timer(name='decorator')
def execute_v3():
    prime_table = get_primes(1000)
    n = 3
    while True:
        if n % 2 == 0:
            num_divisors = total_divisors(n/2, prime_table) * total_divisors(n+1, prime_table)
        else:
            num_divisors = total_divisors((n+1)/2, prime_table) * total_divisors(n, prime_table)
        if num_divisors > 500:
            print(int(n * (n+1) / 2))
            break
        n += 1


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v3"
    if plan_of_attack == "v1":
        execute_v1()
    elif plan_of_attack == "v2":
        execute_v2()
    else:
        execute_v3()
