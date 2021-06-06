"""
Average execution times:
    v1: (0.000020 seconds)
Answer: 232792560
"""
import _init_paths
from lib.utils.numeric import sum_of_natural_numbers, sum_of_squares_of_natural_numbers
from lib.utils.generic import Timer


@Timer()
def execute_v1():
    print(sum_of_natural_numbers(100) ** 2 - sum_of_squares_of_natural_numbers(100))


if __name__ == "__main__":
    execute_v1()
