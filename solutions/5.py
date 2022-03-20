"""
[Smallest multiple](https://projecteuler.net/problem=5)

Median execution times over 5 runs:
    v1: 0.000087 seconds
    v2: 0.000031 seconds
Answer: 232792560
"""
import sys

import _init_paths
from euler.utils.generic import Timer
from euler.utils.numeric import least_common_multiple, least_common_multiple_of_natural_numbers


@Timer()
def execute_v1():
    print(least_common_multiple([i for i in range(1, 21)]))


@Timer()
def execute_v2():
    """Presence of all natural numbers up till n is leveraged by directly computing the largest exponent."""
    print(least_common_multiple_of_natural_numbers(20))


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v2"
    if plan_of_attack == "v1":
        execute_v1()
    else:
        execute_v2()
