"""
Average execution times:
    v1: (0.006092 seconds)
Answer: 2000000
"""
import _init_paths
from euler.utils.primes import nth_prime
from euler.utils.generic import Timer


@Timer()
def execute_v1():
    """The upper bound of nth prime is given by n(logn + loglogn) for all n >= 6."""
    print(nth_prime(10001))


if __name__ == "__main__":
    execute_v1()
