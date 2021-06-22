from functools import reduce
from math import log, sqrt
from typing import Iterable, List, Tuple

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


class LargeNumberOpsHelper:
    """
    Logic for computing sums of large numbers.

    TODO: Add checks for memory constraints.
    """

    @classmethod
    def _pad_split_and_reverse(cls, num: str, chunk_size: int) -> List[str]:
        """
        Pads the given string in the beginning to target_len with zeroes and splits the string in chunks each of size
        chunk_size.
        """
        target_len = cls.compute_divisible_len(len(num), chunk_size)
        num = num.zfill(target_len)
        chunks = [num[i:i+chunk_size] for i in range(0, target_len, chunk_size)]
        return chunks[::-1]

    @staticmethod
    def compute_divisible_len(str_len: int, chunk_size: int) -> int:
        quotient = int(str_len / chunk_size)
        return (quotient + 1) * chunk_size

    @classmethod
    def large_number_pow(cls, num: str, exp: str) -> str:
        return reduce(lambda num1, num2: cls.large_number_mul(num1, num2), [num] * int(exp))

    @classmethod
    def large_number_mul(cls, a: str, b: str) -> str:
        """
        Word size of the machine's register is assumed to be 64 bits.
        For 64-bit registers the safe number of digits in an integer is 9.
        """
        chunk_size = 9
        digit_wise_res = [cls._mul_with_one_digit(b, int(digit), chunk_size) for digit in a[::-1]]
        digit_wise_res = [item + i * '0' for i, item in enumerate(digit_wise_res)]
        return reduce(lambda num1, num2: LargeNumberAddOpUtils.add(num1, num2), digit_wise_res)

    @classmethod
    def _mul_with_one_digit(cls, num: str, digit: int, chunk_size: int) -> str:
        chunks = cls._pad_split_and_reverse(num, chunk_size)
        c, carry, mod = [], 0, 10 ** chunk_size
        for chunk in chunks:
            chunk_res = int(chunk) * digit + carry
            c.append(str(chunk_res % mod).zfill(chunk_size))
            carry = int(chunk_res / mod)
        c = ''.join(c[::-1])
        return (str(carry) + c).lstrip('0')


class LargeNumberFirstDegreeOpUtils:
    """
        Utilities for addition and subtraction operations of large numbers represented as strings. Assuming that the
        machine's register word-size is 64 bits, the safe number of digits for using first degree ops on integers is 18.
    """

    _chunk_size: int = 18
    _mod: int = 10 ** _chunk_size

    @classmethod
    def operate(cls, a: str, b: str) -> str:
        a, b = cls._make_chunks(a, b)
        result = [cls._op_chunks(chunk1, chunk2) for chunk1, chunk2 in zip(a, b)]
        totals, carries = [item[0] for item in result] + [0], [0] + [item[1] for item in result]
        c = [str(total + carry).zfill(cls._chunk_size) for total, carry in zip(totals, carries)]
        return ''.join(c[::-1]).lstrip('0')

    @classmethod
    def _make_chunks(cls, a: str, b: str) -> Tuple[Iterable[int], Iterable[int]]:
        a, b = a.lstrip('0'), b.lstrip('0')
        target_len = cls._compute_target_len(len(a), len(b))
        a, b = cls._pad_split_and_reverse(a, target_len), cls._pad_split_and_reverse(b, target_len)
        return map(int, a), map(int, b)

    @classmethod
    def _compute_target_len(cls, len_a: int, len_b: int) -> int:
        max_len = max(len_a, len_b)
        return LargeNumberOpsHelper.compute_divisible_len(max_len, cls._chunk_size)

    @classmethod
    def _pad_split_and_reverse(cls, num: str, target_len: int) -> List[str]:
        num = num.zfill(target_len)
        chunks = [num[i:i + cls._chunk_size] for i in range(0, target_len, cls._chunk_size)]
        return chunks[::-1]

    @classmethod
    def _op_chunks(cls, chunk1: int, chunk2: int) -> Tuple[int, int]:
        raise NotImplementedError


class LargeNumberAddOpUtils(LargeNumberFirstDegreeOpUtils):

    @classmethod
    def add(cls, a: str, b: str) -> str:
        return cls.operate(a, b)

    @classmethod
    def _op_chunks(cls, chunk1: int, chunk2: int) -> Tuple[int, int]:
        total = chunk1 + chunk2
        carry = int(total / cls._mod)
        total = total % cls._mod
        return total, carry


class LargeNumberSubtractOpUtils(LargeNumberFirstDegreeOpUtils):

    @classmethod
    def subtract(cls, a: str, b: str) -> str:
        cls._check_non_negative(a)
        cls._check_non_negative(b)
        if cls._is_smaller(a, b):
            return '-' + cls.operate(b, a)
        else:
            return cls.operate(a, b)

    @staticmethod
    def _check_non_negative(num: str):
        if num.startswith('-'):
            raise ValueError("Provide positive numbers in the subtraction routine.")

    @staticmethod
    def _is_smaller(a: str, b: str) -> bool:
        a, b = a.lstrip('0'), b.lstrip('0')
        if len(b) > len(a) or (len(a) == len(b) and int(b[0]) > int(a[0])):
            return True
        else:
            return False

    @classmethod
    def _op_chunks(cls, chunk1: int, chunk2: int) -> Tuple[int, int]:
        carry = 0
        if chunk1 < chunk2:
            chunk1 += 10 ** cls._chunk_size
            carry = -1
        return chunk1 - chunk2, carry


def large_number_sum(a: str, b: str) -> str:
    return LargeNumberAddOpUtils.add(a, b)


def large_number_diff(a: str, b: str) -> str:
    return LargeNumberSubtractOpUtils.subtract(a, b)


def large_number_mul(a: str, b: str) -> str:
    return LargeNumberOpsHelper.large_number_mul(a, b)


def large_number_pow(num: str, exp: str) -> str:
    return LargeNumberOpsHelper.large_number_pow(num, exp)


def num_combinations(n: int, r: int) -> int:
    numerator = reduce(lambda a, b: a * b, range(n-r+1, n+1))
    denominator = reduce(lambda a, b: a * b, range(1, r+1))
    return int(numerator / denominator)
