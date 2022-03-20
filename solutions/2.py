"""
[Even Fibonacci numbers](https://projecteuler.net/problem=2)

Median execution times over 5 runs:
    v1: 0.000028 seconds
    v2: 0.000024 seconds
Answer: 4613732
"""
import sys

import _init_paths
from euler.sequence_generators import FibonacciSequenceGenerator
from euler.utils.generic import Timer


def generate_numbers():
    generator = FibonacciSequenceGenerator(1, 2)
    return generator.generate(4000000)


@Timer()
def execute_v1():
    """Generate every Fibonacci number up until the given limit and add all the even occurrences."""
    fib_seq = generate_numbers()
    print(sum([i for i in fib_seq if i % 2 == 0]))


@Timer()
def execute_v2():
    """Avoid testing for even numbers by observing that every 3rd number in the sequence is even."""
    fib_seq = generate_numbers()
    print(sum(fib_seq[1::3]))


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v2"
    if plan_of_attack == "v1":
        execute_v1()
    else:
        execute_v2()
