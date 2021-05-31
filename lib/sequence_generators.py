from math import sqrt

from typing import List, Iterable


class FibonacciSequenceGenerator:
    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

    def generate(self, upper_bound: int = 0, num_terms: int = 0) -> List[int]:
        """Generates the Fibonacci sequence starting from first and second.

        upper_bound is exclusive
        """
        sequence = []
        for i, next_term in enumerate(self._next_num()):
            if upper_bound == 0 and num_terms == 0:
                raise ValueError("Either provide a positive upper_bound for the sequence or the (positive) num_terms "
                                 "to be generated.")
            if 0 < upper_bound <= next_term:
                break
            elif 0 < num_terms <= i:
                break
            else:
                sequence.append(next_term)
        return sequence

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
    """Produces prime numbers with the method of Sieve of Eratosthenes."""

    @classmethod
    def generate(cls, upper_bound: int) -> List[int]:
        """upper_bound is inclusive."""
        sieve_bound, cross_limit = int((upper_bound - 1) / 2), int((int(sqrt(upper_bound)) - 1) / 2)
        sieve = [True for _ in range(sieve_bound + 1)]
        for i in range(1, cross_limit + 1):
            if sieve[i]:
                for j in range(2*i*(i+1), sieve_bound + 1, 2*i+1):
                    sieve[j] = False
        return [2] + [2*i+1 for i, _ in enumerate(sieve) if sieve[i]][1:]


class CollatzSequenceGenerator:
    """Produces a collatz sequence until the end given a starting number."""

    @classmethod
    def generate(cls, num: int) -> List[int]:
        sequence = [num]
        while num != 1:
            num = int(num / 2) if num % 2 == 0 else 3*num + 1
            sequence.append(num)
        return sequence

    @classmethod
    def longest_sequence_seed(cls, upper_bound: int) -> int:
        seq_len = {1: 1}
        max_count, max_count_seed = 1, 1
        for i in range(1, upper_bound + 1):
            count, num, sequence = 1, i, [i]
            while num != 1:
                if num in seq_len:
                    count += seq_len[num]
                    break
                else:
                    count += 1
                    num = int(num / 2) if num % 2 == 0 else 3 * num + 1
                    sequence.append(num)
            max_count, max_count_seed = (count, i) if max_count < count else (max_count, max_count_seed)
            for item in sequence:
                seq_len[item] = count
                count -= 1
        return max_count_seed
