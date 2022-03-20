"""
[Summation of primes](https://projecteuler.net/problem=10)

Median execution times over 5 runs:
    v1: 0.124481 seconds
Answer: 142913828922
"""
from functools import reduce

import _init_paths
from euler.utils.generic import Timer
from euler.sequence_generators import PrimeNumberSequenceGenerator


@Timer()
def execute_v1():
    """Generate the primes using sieve and add."""
    print(reduce(lambda a, b: a + b, PrimeNumberSequenceGenerator.generate(2000000)))


if __name__ == "__main__":
    execute_v1()
