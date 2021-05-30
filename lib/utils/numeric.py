from math import log, sqrt
from typing import List, Tuple

from lib.utils.primes import get_primes


def sum_of_natural_numbers(n: int) -> int:
    return int(n * (n + 1) / 2)


def sum_of_squares_of_natural_numbers(n: int) -> int:
    return int(n * (n + 1) * (2 * n + 1) / 6)


def least_common_multiple(numbers: List[int]) -> int:
    primes, lcm = get_primes(max(numbers)), 1
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
    primes = get_primes(upper_bound)
    for prime in primes:
        exponent = int(log(upper_bound) / log(prime)) if prime <= limit else 1
        lcm *= prime ** exponent
    return lcm


def get_factors(num: int) -> List[int]:
    """Returns a sorted list of proper factors."""
    upper_bound = int(sqrt(num))
    factors = set()
    for i in range(2, upper_bound + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(int(num / i))
    return sorted(list(factors))


class LargeNumberSumUtils:
    """Logic for computing sums of large numbers."""

    @classmethod
    def large_number_sum(cls, a: str, b: str, word_size: int = 32) -> str:
        """Returns the sum of two large numbers in string format.
            word_size is the number of bits upon which the processor can perform an add operation in one clock cycle.
        """
        word_size_to_len_str_map = {8: 2, 16: 4, 24: 6, 32: 9, 64: 19}
        try:
            chunk_size = word_size_to_len_str_map[word_size]
        except KeyError:
            raise ValueError('Provide the word_size from the following list [16, 32, 64]')
        a, b = cls.pad_split_and_reverse(a, chunk_size), cls.pad_split_and_reverse(b, chunk_size)
        a, b = cls._adjust_lens(a, b, chunk_size)
        c, carry, mod = [], 0, 10 ** chunk_size
        for chunk1, chunk2 in zip(a, b):
            temp_sum = int(chunk1) + int(chunk2) + carry
            c.append(str(temp_sum % mod).zfill(chunk_size))
            carry = int(temp_sum / mod)
        c = ''.join(c[::-1])
        return str(carry) + c.lstrip('0') if carry != 0 else c.lstrip('0')

    @classmethod
    def pad_split_and_reverse(cls, num: str, chunk_size: int) -> List[str]:
        """Pads the given string in the beginning to target_len with zeroes and splits the string in chunks each of
            size str_word_size.
        """
        target_len = cls._compute_target_len(len(num), chunk_size)
        num = num.zfill(target_len)
        chunks = [num[i:i+chunk_size] for i in range(0, target_len, chunk_size)]
        return chunks[::-1]

    @staticmethod
    def _compute_target_len(str_len: int, chunk_size: int) -> int:
        quotient = int(str_len / chunk_size)
        return (quotient + 1) * chunk_size

    @staticmethod
    def _adjust_lens(a: List[str], b: List[str], chunk_size: int) -> Tuple[List[str], List[str]]:
        appendage = [chunk_size * '0']
        if len(a) > len(b):
            b = b + (len(a) - len(b)) * appendage
        elif len(a) < len(b):
            a = a + (len(b) - len(a)) * appendage
        return a, b


def large_number_sum(a: str, b: str, word_size: int = 32) -> str:
    return LargeNumberSumUtils.large_number_sum(a, b, word_size)
