"""
Average execution times:
    v1: (0.000080 seconds)
    v2: (0.000030 seconds)
Answer: 232792560
"""
import sys

import _init_paths
from lib.utils.numeric import least_common_multiple, least_common_multiple_of_natural_numbers
from lib.utils.generic import Timer


@Timer()
def execute_v1():
    """
    LCM of natural numbers is computed by creating an appropriate cache of prime numbers. The cache is used to compute
    the highest power of the prime that is present as a factor of all numbers in the list.
    """
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
