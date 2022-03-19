"""
Average execution times:
    v1: (1.479060 seconds)
Answer: 1366
"""
from functools import reduce

import _init_paths
from euler.utils.generic import Timer
from euler.utils.numeric import large_number_pow


@Timer(name='decorator')
def execute_v1():
    print(reduce(lambda char1, char2: int(char1) + int(char2), large_number_pow('2', '1000')))


if __name__ == "__main__":
    execute_v1()
