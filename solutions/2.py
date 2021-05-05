"""Plan of attack:
    v1: (0.000028 seconds)
        Generate every Fibonacci number up until the given limit and add all the even occurrences.
    v2: (0.000025 seconds)
        Avoid testing for even numbers by observing that every 3rd number in the sequence is even.
"""
import sys

import _init_paths
from lib.sequence_generators import FibonacciSequenceGenerator
from lib.utils.generic import Timer


def generate_numbers():
    generator = FibonacciSequenceGenerator(1, 2)
    return generator.generate(4000000)


@Timer(name='decorator')
def execute_v1():
    fib_seq = generate_numbers()
    print(sum([i for i in fib_seq if i % 2 == 0]))


@Timer(name='decorator')
def execute_v2():
    fib_seq = generate_numbers()
    print(sum(fib_seq[1::3]))


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v2"
    if plan_of_attack == "v1":
        execute_v1()
    else:
        execute_v2()
