from functools import reduce
from math import log, sqrt
from typing import List, Tuple

from lib.sequence_generators import PrimeNumberSequenceGenerator


def sum_of_natural_numbers(n: int) -> int:
    if n < 0:
        raise ValueError("Provide a non-negative natural number.")
    return int(n * (n + 1) / 2)


def sum_of_squares_of_natural_numbers(n: int) -> int:
    if n < 0:
        raise ValueError("Provide a non-negative natural number.")
    return int(n * (n + 1) * (2 * n + 1) / 6)


def least_common_multiple(numbers: List[int]) -> int:
    if any([number <= 0 for number in numbers]):
        raise ValueError("Provide positive integers only.")
    primes, lcm = PrimeNumberSequenceGenerator.generate(max(numbers)), 1
    for prime in primes:
        if not any([number != 1 for number in numbers]):
            break
        while any([number % prime == 0 for number in numbers]):
            lcm *= prime
            numbers = [number / prime if number % prime == 0 else number for number in numbers]
    return lcm


def least_common_multiple_of_natural_numbers(n: int) -> int:
    """
    Let the least common multiple of first n natural numbers be denoted by LCM(n). The exponent of any prime number in
    the prime factorization of LCM(n) is its greatest perfect power less than n. For example, the power of 2 in LCM(20)
    is 4 = log(16) / log(2).
    """
    if n <= 0:
        raise ValueError("Provide positive integers only.")
    lcm, limit = 1, sqrt(n)
    primes = PrimeNumberSequenceGenerator.generate(n)
    for prime in primes:
        exponent = int(log(n) / log(prime))
        lcm *= prime ** exponent
    return lcm


def get_factors(num: int) -> List[int]:
    """Returns a sorted list of proper factors."""
    if num < 0:
        raise ValueError("Provide a natural number.")
    upper_bound = int(sqrt(num))
    factors = set()
    for i in range(2, upper_bound + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(int(num / i))
    return sorted(list(factors))


class LargeNumberSumHelper:
    """Logic for computing sums of large numbers."""

    @classmethod
    def large_number_sum(cls, a: str, b: str, word_size: int = 32) -> str:
        """
        Returns the sum of two large numbers a and b represented as strings.
        word_size is the word size of the register that the computer uses.
        """
        chunk_size = cls._get_chunk_size(word_size)
        a, b = cls._adjust_lens(a, b)
        a, b = cls._pad_split_and_reverse(a, chunk_size), cls._pad_split_and_reverse(b, chunk_size)
        c, carry, mod = [], 0, 10 ** chunk_size
        for chunk1, chunk2 in zip(a, b):
            total, carry = cls._add_chunks(chunk1, chunk2, carry, chunk_size, mod)
            c.append(total)
        c = ''.join(c[::-1])
        return (str(carry) + c).lstrip('0')

    @staticmethod
    def _get_chunk_size(word_size: int) -> int:
        word_size_to_len_str_map = {8: 2, 16: 4, 24: 6, 32: 9, 64: 19}
        try:
            chunk_size = word_size_to_len_str_map[word_size]
        except KeyError:
            raise ValueError("Provide the word_size from the following list [16, 32, 64]")
        return chunk_size

    @staticmethod
    def _adjust_lens(a: str, b: str) -> Tuple[str, str]:
        return (a, b.zfill(len(a))) if len(a) > len(b) else (a.zfill(len(b)), b)

    @classmethod
    def _pad_split_and_reverse(cls, num: str, chunk_size: int) -> List[str]:
        """
        Pads the given string in the beginning to target_len with zeroes and splits the string in chunks each of size
        chunk_size.
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
    def _add_chunks(chunk_a: str, chunk_b: str, carry: int, chunk_size: int, mod: int) -> Tuple[str, int]:
        temp_total = int(chunk_a) + int(chunk_b) + carry
        total = str(temp_total % mod).zfill(chunk_size)
        carry = int(temp_total / mod)
        return total, carry


def large_number_sum(a: str, b: str, word_size: int = 32) -> str:
    return LargeNumberSumHelper.large_number_sum(a, b, word_size)


def num_combinations(n: int, r: int) -> int:
    numerator = reduce(lambda a, b: a * b, range(n-r+1, n+1))
    denominator = reduce(lambda a, b: a * b, range(1, r+1))
    return int(numerator / denominator)
