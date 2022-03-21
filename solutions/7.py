"""
[10001st prime](https://projecteuler.net/problem=7)

Median execution times over 5 runs:
    v1: 0.006567 seconds
Answer: 104743
"""
from euler.utils.generic import Timer
from euler.primes import nth_prime


@Timer()
def execute_v1():
    """The upper bound of nth prime is given by n(logn + loglogn) for all n >= 6."""
    print(nth_prime(10001))


if __name__ == "__main__":
    execute_v1()
