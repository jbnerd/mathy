"""
[Longest Collatz sequence](https://projecteuler.net/problem=14)

Median execution times over 5 runs:
    v1: 1.255132 seconds
Answer: 837799
"""
from euler.utils.sequence_generators import CollatzSequenceGenerator
from euler.utils.generic import Timer


@Timer()
def execute_v1():
    print(CollatzSequenceGenerator.longest_sequence_seed(1000000))


if __name__ == "__main__":
    execute_v1()

