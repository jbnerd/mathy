"""
[Largest product in a series](https://projecteuler.net/problem=8)

Median execution times over 5 runs:
    v1: 0.002258 seconds
Answer: 23514624000
"""
import _init_paths
from euler.utils.generic import Timer
from euler.utils.strings import character_wise_product


def read_data():
    with open('solutions/data/8.txt') as infile:
        data = ''.join(infile.read().strip().split('\n'))
    return data


@Timer()
def execute_v1():
    """Collect digits window-wise and keep a track of the maximum product."""
    data = read_data()
    max_prod = 0
    for i, _ in enumerate(data[:-13]):
        max_prod = max(max_prod, character_wise_product(data[i:i+13]))
    print(max_prod)


if __name__ == "__main__":
    execute_v1()
