"""Plan of attack:
    v1: (0.057841 seconds)
        The upper bound of nth prime is given by n(logn + loglogn) for all n >= 6.
"""
import _init_paths
from lib.utils.primes import get_nth_prime
from lib.utils.generic import Timer


@Timer(name='decorator')
def execute_v1():
    print(get_nth_prime(10001))


if __name__ == "__main__":
    execute_v1()
