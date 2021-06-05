"""
Average execution times:
    v1: 0.117498 seconds
Answer: 142913828922
"""
from functools import reduce

import _init_paths
from lib.utils.generic import Timer
from lib.utils.primes import get_primes


@Timer(name='decorator')
def execute_v1():
    """Generate the primes using sieve and add."""
    print(reduce(lambda a, b: a + b, get_primes(2000000)))


if __name__ == "__main__":
    execute_v1()
