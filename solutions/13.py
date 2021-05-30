"""Plan of attack:
    v1: (0.000726 seconds)
        Use addition of large numbers using string representation and optimize on word-size of the processor for
        maximum performance.
"""
from functools import reduce

import _init_paths
from lib.utils.generic import Timer
from lib.utils.numeric import large_number_sum


@Timer(name='decorator')
def execute_v1():
    with open('solutions/data/13.txt') as infile:
        data = infile.read().strip().split('\n')
    print(reduce(lambda a, b: large_number_sum(a, b, 64), data)[:10])


if __name__ == "__main__":
    execute_v1()
