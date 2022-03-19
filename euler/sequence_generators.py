from math import sqrt

from typing import Dict, Iterable, List, Optional


class FibonacciSequenceGenerator:
    OptionalIntArg = Optional[int]

    def __init__(self, first: int, second: int):
        self._seed_checks(first, second)
        self.first = first
        self.second = second

    @staticmethod
    def _seed_checks(first: int, second: int):
        if first < 0 or second < 0:
            raise ValueError("Provide non-negative seeds.")

    def generate(self, upper_bound: OptionalIntArg = None, num_terms: OptionalIntArg = None) -> List[int]:
        """
        Generates the Fibonacci sequence starting from first and second.
        Note: upper_bound is excluded.
        """
        self._stop_condition_checks(upper_bound, num_terms)
        sequence = []
        for i, next_term in enumerate(self._next_num()):
            if upper_bound is not None and 0 <= upper_bound <= next_term:
                break
            elif num_terms is not None and 0 <= num_terms <= i:
                break
            else:
                sequence.append(next_term)
        return sequence

    @staticmethod
    def _stop_condition_checks(upper_bound: OptionalIntArg, num_terms: OptionalIntArg):
        if upper_bound is None and num_terms is None:
            raise ValueError("Provide appropriate value for one of upper_bound or num_terms.")
        elif upper_bound is not None and num_terms is not None:
            raise ValueError("Provide appropriate value for only one of upper_bound or num_terms.")
        elif upper_bound is not None and upper_bound < 0:
            raise ValueError("Provide non-negative upper_bound.")
        elif num_terms is not None and num_terms < 0:
            raise ValueError("Provide non-negative num_terms.")

    def _next_num(self) -> Iterable[int]:
        first, second, i = self.first, self.second, 1
        while True:
            if i == 1:
                yield first
            elif i == 2:
                yield second
            else:
                third = first + second
                first, second = second, third
                yield third
            i += 1


class PrimeNumberSequenceGenerator:
    """Generate prime numbers with the Sieve of Eratosthenes."""

    @classmethod
    def generate(cls, upper_bound: int) -> List[int]:
        """
        Optimizations to the standard sieve algorithm:
            1) Consider only odd values to halve the search space and save on memory usage:
                    The sieve list consists of boolean values corresponding to every odd number less than upper_bound.
                    Thus every ith element in sieve represents the prime number status of the number 2i+1.
            2) The search need only be done till the sqrt(upper_bound):
                    cross_limit defines this limit.
            3) For every prime number p, the crossing out need only begin from p^2 because all multiples of p before p^2
               would also be a multiple of a number smaller than p; hence must've already been crossed out:
                    The index of 2i+1 is i, so the index of (2i+1))^2 would be 2i(i+1).
        """
        if upper_bound < 2:
            return []
        sieve_bound, cross_limit = int((upper_bound - 1) / 2), int((int(sqrt(upper_bound)) - 1) / 2)
        sieve = [True for _ in range(sieve_bound + 1)]
        for i in range(1, cross_limit + 1):
            if sieve[i]:
                for j in range(2*i*(i+1), sieve_bound + 1, 2*i+1):
                    sieve[j] = False
        return [2] + [2*i+1 for i, _ in enumerate(sieve) if sieve[i]][1:]


class CollatzSequenceGenerator:
    """Produces a collatz sequence until the end given a starting number."""

    _seq_len: Dict[int, int] = {1: 1}

    @classmethod
    def generate(cls, num: int) -> List[int]:
        sequence = [num]
        while num != 1:
            num = int(num / 2) if num % 2 == 0 else 3*num + 1
            sequence.append(num)
        return sequence

    @classmethod
    def longest_sequence_seed(cls, upper_bound: int) -> int:
        """Solutions to repeating sub-problems are memoized in cls._seq_len"""
        max_count, max_count_seed = 1, 1
        for i in range(1, upper_bound + 1):
            count = cls._count_num_steps(i)
            max_count, max_count_seed = (count, i) if max_count < count else (max_count, max_count_seed)
        return max_count_seed

    @classmethod
    def _count_num_steps(cls, num: int) -> int:
        count, sequence = 1, [num]
        while num != 1:
            if num in cls._seq_len:
                count += cls._seq_len[num]
                break
            else:
                num = int(num / 2) if num % 2 == 0 else 3 * num + 1
                sequence.append(num)
                count += 1
        for i, item in enumerate(sequence):
            cls._seq_len[item] = count - i
        return count
