from typing import List

from lib.sequence_generators import PrimeNumberSequenceGenerator


def sum_of_natural_numbers(n: int) -> int:
    return int(n * (n + 1) / 2)


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
