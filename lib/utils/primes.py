from math import ceil, log, sqrt
from typing import List, Set

from lib.sequence_generators import PrimeNumberSequenceGenerator
from lib.utils.numeric import generate_factors


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    else:
        if num % 2 == 0:
            return False
        upper_bound = int(sqrt(num))
        for i in range(3, upper_bound + 1, 2):
            if num % i == 0:
                return False
        return True


def get_prime_factors(num: int) -> Set[int]:
    """Returns a set of prime factors."""
    return set([factor for factor in generate_factors(num) if is_prime(factor)])


def get_primes(upper_bound: int) -> List[int]:
    return PrimeNumberSequenceGenerator.generate(upper_bound)


def get_nth_prime(n: int) -> int:
    """One of the upper bounds on nth prime number is given by n(logn + loglogn) for all n >= 6"""
    if n < 1:
        raise ValueError('0th or negative prime is not possible. Enter a positive number.')
    elif 1 <= n <= 6:
        return [2, 3, 5, 7, 11, 13][n - 1]
    else:
        upper_bound = ceil(n * (log(n) + log(log(n))))
        return PrimeNumberSequenceGenerator.generate(upper_bound)[n - 1]
