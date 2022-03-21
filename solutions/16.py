"""
[Power digit sum](https://projecteuler.net/problem=16)

Median execution times over 5 runs:
    v1: 0.353439 seconds
Answer: 1366
"""
from functools import reduce

from euler.utils.generic import Timer
from euler.numeric import large_number_pow


@Timer()
def execute_v1():
    print(reduce(lambda char1, char2: int(char1) + int(char2), large_number_pow('2', '1000')))


if __name__ == "__main__":
    execute_v1()
