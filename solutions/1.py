"""Plan of attack:
    v1: (0.000072 seconds)
        Go through all the numbers between 1 and 1000 and add the ones divisible by 3 or 5.
    v2: (0.000015 seconds)
        The desired sum (S) can be represented as the sum of all numbers divisible by 3 (S3) added with sum of all
        numbers divisible by 5 (S5) minus the sum of all numbers divisible by 15 (S15) in the given range. The latter
        because the numbers divisible by 15 will be counted twice.
        Therefore S = S3 + S5 - S15

        S3 = 3 + 6 + 9 + 12 + ... + 999 = 3 * (1 + 2 + 3 + 4 + ... + 333)
        S5 = 5 * (1 + 2 + 3 + ... + 199)
        S15 = 15 * (1 + 2 + 3 + ... + 66)
"""

import sys

import _init_paths
from lib.utils.generic import Timer
from lib.utils.numeric import sum_of_natural_numbers


@Timer(name='decorator')
def execute_v1():
    print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))


@Timer(name='decorator')
def execute_v2():
    print(3 * sum_of_natural_numbers(333) + 5 * sum_of_natural_numbers(199) - 15 * sum_of_natural_numbers(66))


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v2"
    if plan_of_attack == "v1":
        execute_v1()
    else:
        execute_v2()
