"""
[Largest product in a grid](https://projecteuler.net/problem=11)

Median execution times over 5 runs:
    v1: 0.001040 seconds
Answer: 70600674
"""
from functools import reduce

import _init_paths
from euler.utils.generic import Timer


def read_data():
    with open('solutions/data/11.txt') as infile:
        data = infile.read().strip().split('\n')
    data = [item.strip().split() for item in data]
    data = [[int(item) for item in line] for line in data]
    return data


def right_prod(data, i, j):
    return reduce(lambda a, b: a * b, data[i][j:j+4])


def right_down_prod(data, i, j):
    return reduce(lambda a, b: a * b, [data[i+k][j+k] for k in range(4)])


def down_prod(data, i, j):
    return reduce(lambda a, b: a * b, [data[i+k][j] for k in range(4)])


def left_down_prod(data, i, j):
    return reduce(lambda a, b: a * b, [data[i+k][j-k] for k in range(4)])


@Timer()
def execute_v1():
    """Iterate over valid elements and compute the product 4-element wise."""
    data = read_data()
    max_prod = 0
    for i in range(17):
        for j in range(17):
            max_prod = max(max_prod, right_prod(data, i, j))
            max_prod = max(max_prod, right_down_prod(data, i, j))
            max_prod = max(max_prod, down_prod(data, i, j))

    for i in range(17):
        for j in range(3, 20):
            max_prod = max(max_prod, left_down_prod(data, i, j))

    print(max_prod)


if __name__ == "__main__":
    execute_v1()
