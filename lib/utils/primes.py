from math import ceil, log, sqrt
from typing import List, Tuple

from lib.sequence_generators import PrimeNumberSequenceGenerator


class PrimeFactorizationHelper:
    """
    Helper class for prime factorization of numbers. The main logic of this class uses a cache of prime numbers which
    are generated before computing the factorization.
    """

    _primes: List[int] = []
    curr_upper_bound: int = -1

    @classmethod
    def update_prime_cache(cls, upper_bound: int):
        cls.curr_upper_bound = upper_bound
        cls._prepare_prime_cache(upper_bound)

    @classmethod
    def _prepare_prime_cache(cls, num: int):
        cls.curr_upper_bound = int(sqrt(num) + 1)
        cls._primes = PrimeNumberSequenceGenerator.generate(cls.curr_upper_bound)

    @classmethod
    def prime_factorization(cls, num: int) -> Tuple[List[int], List[int]]:
        """
        The search space is pruned by using the fact that there can only be one prime factor greater than the square
        root of the number.
        """
        if cls.curr_upper_bound < int(sqrt(num) + 1):
            cls._prepare_prime_cache(num)

        factors, exponents, limit = [], [], sqrt(num)
        for prime in cls._primes:
            if prime > limit:
                if num != 1:
                    factors.append(int(num))
                    exponents.append(1)
                break
            num, exponent = cls._process_one_iteration(num, prime)
            if exponent != 0:
                factors.append(prime)
                exponents.append(exponent)
        return factors, exponents

    @staticmethod
    def _process_one_iteration(num: int, prime: int) -> Tuple[int, int]:
        exponent = 0
        while num % prime == 0:
            exponent, num = exponent + 1, num / prime
        return num, exponent


def prime_factorization(num: int) -> Tuple[List[int], List[int]]:
    """A safe upper bound for the cache of prime numbers to factorize a 32-bit integer is 2^16."""
    if num < 1:
        raise ValueError("Provide a positive integer for factorization.")
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


def nth_prime(n: int) -> int:
    """One of the upper bounds on nth prime number is given by n(log(n) + log(log(n))) for all n >= 6"""
    if n < 1:
        raise ValueError("Provide a positive number.")
    elif 1 <= n <= 6:
        return [2, 3, 5, 7, 11, 13][n - 1]
    else:
        upper_bound = ceil(n * (log(n) + log(log(n))))
        return PrimeNumberSequenceGenerator.generate(upper_bound)[n - 1]
