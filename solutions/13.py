"""
[Large sum](https://projecteuler.net/problem=13)

Median execution times over 5 runs:
    v1: 0.000815 seconds
Answer: 5537376230
"""
from functools import reduce

import _init_paths
from euler.utils.generic import Timer
from euler.utils.numeric import large_number_sum


@Timer()
def execute_v1():
    """
    Logic for addition of large numbers using string representation is used. Optimization is done based on the word-size
    of the processor for maximum performance.
    """
    with open('solutions/data/13.txt') as infile:
        data = infile.read().strip().split('\n')
    print(reduce(lambda a, b: large_number_sum(a, b), data)[:10])


if __name__ == "__main__":
    execute_v1()
