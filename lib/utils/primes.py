from math import sqrt
from typing import List, Set

from lib.sequence_generators import PrimeNumberSequenceGenerator


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
    """Returns a set of factors excluding 1 and the number itself."""
    upper_bound = int(sqrt(num))
    factors = []
    for i in range(2, upper_bound + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num / i)
    return set([factor for factor in factors if is_prime(factor)])


def get_primes(upper_bound: int) -> List[int]:
    return PrimeNumberSequenceGenerator.generate(upper_bound)
