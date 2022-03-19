"""
Average execution times:
    v1: (2.416296 seconds)
    v2: (0.173168 seconds)
    v3: (0.089309 seconds)
Answer: 76576500
"""
import sys
from functools import reduce

import _init_paths
from euler.utils.generic import Timer
from euler.utils.numeric import sum_of_natural_numbers, get_factors
from euler.utils.primes import prime_factorization


@Timer(name='decorator')
def execute_v1():
    """Brute force approach - triangular numbers are generated using the formula."""
    i = 1
    while True:
        triangular_num = sum_of_natural_numbers(i)
        if len(get_factors(triangular_num)) > 498:
            print(triangular_num)
            break
        i += 1


def total_divisors(num):
    factors, exponents = prime_factorization(num)
    exponents = [exp + 1 for exp in exponents]
    return reduce(lambda a, b: a * b, exponents)


@Timer()
def execute_v2():
    """
    Let the prime factorization of a number, pf(n) = p_1^a_1 * p_2^a_2 * ... * p_k^a_k. Then the total number of
    divisors D(n) = (a_1 + 1) * (a_2 + 1) * ... * (a_k + 1).
    """
    i = 4
    while True:
        triangular_num = sum_of_natural_numbers(i)
        if total_divisors(triangular_num) > 500:
            print(triangular_num)
            break
        i += 1


@Timer()
def execute_v3():
    """
    Since a triangular number is given by n * (n + 1) / 2 and since n, (n + 1) must be co-primes:
        D(num) = D(n/2) * D(n+1) if n is even
               = D(n) * D((n+1)/2) otherwise.
    """
    n = 3
    while True:
        if n % 2 == 0:
            num_divisors = total_divisors(n / 2) * total_divisors(n + 1)
        else:
            num_divisors = total_divisors((n+1) / 2) * total_divisors(n)
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
