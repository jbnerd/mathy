from math import ceil, log, sqrt
from typing import List, Tuple

from lib.sequence_generators import PrimeNumberSequenceGenerator


class PrimeFactorizationHelper:
    """Utilities related to prime factors and prime factorization of numbers."""

    _primes: List[int] = []
    curr_upper_bound: int = -1

    @classmethod
    def update_prime_cache(cls, upper_bound: int):
        cls.curr_upper_bound = upper_bound
        cls._primes = cls._prepare_prime_table(upper_bound)

    @staticmethod
    def _prepare_prime_table(num: int) -> List[int]:
        upper_bound = int(sqrt(num) + 1)
        return PrimeNumberSequenceGenerator.generate(upper_bound)

    @classmethod
    def prime_factorization(cls, num: int) -> Tuple[List[int], List[int]]:
        if cls.curr_upper_bound < int(sqrt(num) + 1):
            cls._primes = cls._prepare_prime_table(num)

        factors, exponents, limit = [], [], sqrt(num)
        for prime in cls._primes:
            if prime >= sqrt(num):
                break
            exponent = 0
            while num % prime == 0:
                exponent, num = exponent + 1, num / prime
            if exponent != 0:
                factors.append(prime)
                exponents.append(exponent)

        # There can only be one prime factor greater than the sqrt of the number.
        if num != 1:
            factors.append(int(num))
            exponents.append(1)

        return factors, exponents


def prime_factorization(num: int) -> Tuple[List[int], List[int]]:
    """A safe upper bound for the cache of prime numbers to factorize a 32-bit integer is 2^16."""
    if PrimeFactorizationHelper.curr_upper_bound < 0:
        PrimeFactorizationHelper.update_prime_cache(2 ** 16)
    return PrimeFactorizationHelper.prime_factorization(num)


def prime_factors(num: int) -> List[int]:
    return prime_factorization(num)[0]


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


def get_primes(upper_bound: int) -> List[int]:
    return PrimeNumberSequenceGenerator.generate(upper_bound)


def get_nth_prime(n: int) -> int:
    """One of the upper bounds on nth prime number is given by n(log(n) + log(log(n))) for all n >= 6"""
    if n < 1:
        raise ValueError('0th or negative prime is not possible. Enter a positive number.')
    elif 1 <= n <= 6:
        return [2, 3, 5, 7, 11, 13][n - 1]
    else:
        upper_bound = ceil(n * (log(n) + log(log(n))))
        return get_primes(upper_bound)[n - 1]
