"""
[Sum square difference](https://projecteuler.net/problem=6)

Median execution times over 5 runs:
    v1: 0.000014 seconds
Answer: 25164150
"""
from euler.utils.generic import Timer
from euler.numeric import sum_of_natural_numbers, sum_of_squares_of_natural_numbers


@Timer()
def execute_v1():
    print(sum_of_natural_numbers(100) ** 2 - sum_of_squares_of_natural_numbers(100))


if __name__ == "__main__":
    execute_v1()
