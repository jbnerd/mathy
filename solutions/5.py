"""Plan of attack:
    v1: (0.000051 seconds)
        The question essentially asks you to compute the least common multiple (LCM) of the given list of numbers. LCM
        can be computed by having the list of collective prime factors of the set and their corresponding frequencies.
        Prime numbers can be computed efficiently with the Sieve of Eratosthenes. Frequencies need not be computed,
        instead the prime numbers can be used as taught in the primary grade LCM computation procedure.
    v2: (0.000030 seconds)
        Optimized method of computing LCM for first N natural numbers.
"""
import sys

import _init_paths
from lib.utils.numeric import least_common_multiple, least_common_multiple_first_n_natural_numbers
from lib.utils.generic import Timer


@Timer(name='decorator')
def execute_v1():
    print(least_common_multiple([i for i in range(1, 21)]))


@Timer(name='decorator')
def execute_v2():
    print(least_common_multiple_first_n_natural_numbers(20))


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v2"
    if plan_of_attack == "v1":
        execute_v1()
    else:
        execute_v2()
