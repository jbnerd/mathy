"""
Average execution times:
    v1: 0.052077 seconds
Answer: 6857
"""
import _init_paths
from lib.utils.primes import prime_factors
from lib.utils.generic import Timer


@Timer()
def execute_v1():
    """Generate all prime factors and find the max."""
    print(max(prime_factors(600851475143)))


if __name__ == "__main__":
    execute_v1()
