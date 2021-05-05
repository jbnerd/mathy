from math import sqrt
from typing import Set


def is_prime(num: int) -> bool:
    if num < 2:
        return False
    else:
        upper_bound = int(sqrt(num))
        for i in range(2, upper_bound + 1):
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
