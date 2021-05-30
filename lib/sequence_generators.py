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
        prime_numbers, candidates = [2], list(range(3, upper_bound + 1, 2))
        check_limit = sqrt(upper_bound + 1)
        next_candidate = candidates[0]
        while next_candidate <= check_limit:
            prime_numbers.append(next_candidate)
            candidates = [i for i in candidates if i % next_candidate != 0]
            next_candidate = candidates[0]
        prime_numbers += candidates
        return prime_numbers
