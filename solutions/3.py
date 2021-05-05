"""Plan of attack:
    v1: (0.052573 seconds)
        Generate all prime factors and find the max.
"""
import sys

import _init_paths
from lib.utils.primes import get_prime_factors
from lib.utils.generic import Timer


@Timer(name='decorator')
def execute_v1():
    print(max(get_prime_factors(600851475143)))


if __name__ == "__main__":
    execute_v1()
