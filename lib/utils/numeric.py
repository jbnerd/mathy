from math import log, sqrt
from typing import List, Set

from lib.sequence_generators import PrimeNumberSequenceGenerator


def sum_of_natural_numbers(n: int) -> int:
    return int(n * (n + 1) / 2)


def sum_of_squares_of_natural_numbers(n: int) -> int:
    return int(n * (n + 1) * (2 * n + 1) / 6)


def least_common_multiple(numbers: List[int]) -> int:
    primes, lcm = PrimeNumberSequenceGenerator.generate(max(numbers)), 1
    for prime in primes:
        exhausted = False
        while not exhausted:
            exhausted = True
            for i, number in enumerate(numbers):
                if number % prime == 0:
                    numbers[i] /= prime
                    exhausted = False
            if not exhausted:
                numbers = [number for number in numbers if number != 1]
                lcm *= prime
    return lcm


def least_common_multiple_first_n_natural_numbers(upper_bound: int) -> int:
    """ The exponent of a prime number in the prime factorization of the LCM is its greatest perfect power less than the
        upper bound. For example power of 2 in LCM(1...20) is 4 = log(16, 2). We can further observe that the exponent
        of a prime number greater than sqrt(upper_bound) is 1.

        upper_bound is inclusive
    """
    lcm, limit = 1, sqrt(upper_bound)
    primes = PrimeNumberSequenceGenerator.generate(upper_bound)
    for prime in primes:
        exponent = int(log(upper_bound) / log(prime)) if prime <= limit else 1
        lcm *= prime ** exponent
    return lcm


def generate_factors(num: int) -> Set[int]:
    """Generates proper factors of the given number."""
    upper_bound = int(sqrt(num))
    factors = []
    for i in range(2, upper_bound + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    return set(factors)


def get_factors(num: int) -> List[int]:
    """Returns a sorted list of proper factors.
        TODO: Merge this function with generate_factors function once the other dependencies are removed.
    """
    return sorted(list(generate_factors(num)))
