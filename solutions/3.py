"""
[Largest prime factor](https://projecteuler.net/problem=3)

Median execution times over 5 runs:
    v1: 0.046619 seconds
Answer: 6857
"""
from euler.utils.generic import Timer
from euler.primes import prime_factors


@Timer()
def execute_v1():
    """Generate all prime factors and find the max."""
    print(max(prime_factors(600851475143)))


if __name__ == "__main__":
    execute_v1()
