"""Plan of attack:
    v1: (0.000025 seconds)
        Directly use the formula to compute the sum of squares of first N natural numbers.
"""
import _init_paths
from lib.utils.numeric import sum_of_natural_numbers, sum_of_squares_of_natural_numbers
from lib.utils.generic import Timer


@Timer(name='decorator')
def execute_v1():
    print(sum_of_natural_numbers(100) ** 2 - sum_of_squares_of_natural_numbers(100))


if __name__ == "__main__":
    execute_v1()
