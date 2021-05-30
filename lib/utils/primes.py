from math import ceil, log, sqrt
from typing import List, Tuple

from lib.sequence_generators import PrimeNumberSequenceGenerator


class PrimeFactors:
    """Utilities related to prime factors and prime factorization of numbers."""

    @classmethod
    def get_prime_factors(cls, num: int) -> List[int]:
        """Returns a list of prime factors."""
        return cls.prime_factorization(num)[0]

    @classmethod
    def prime_factorization(cls, num: int, primes: List[int] = None) -> Tuple[List[int], List[int]]:
        if primes is None:
            primes = cls._prepare_prime_table(num)

        factors, exponents, limit = [], [], sqrt(num)
        for prime in primes:
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

    @staticmethod
    def _prepare_prime_table(num: int) -> List[int]:
        upper_bound = int(sqrt(num) + 1)
        return get_primes(upper_bound)


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
