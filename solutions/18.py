"""
[Maximum path sum I](https://projecteuler.net/problem=18)

Median execution times over 5 runs:
    v1: 0.006270 seconds
    v2: 0.000101 seconds
Answer: 1074
"""
import sys

import _init_paths
from euler.utils.generic import Timer


def read_data():
    with open('solutions/data/18.txt') as infile:
        data = infile.read().strip().split('\n')
    data = [[int(item) for item in line.split()] for line in data]
    return data


def recursive_max_add(data, depth, idx):
    if depth == len(data) - 1:
        return data[depth][idx]
    candidate1 = data[depth][idx] + recursive_max_add(data, depth + 1, idx)
    candidate2 = data[depth][idx] + recursive_max_add(data, depth + 1, idx + 1)
    return max(candidate1, candidate2)


@Timer()
def execute_v1():
    """Recursively traverse all possible paths"""
    data = read_data()
    print(recursive_max_add(data, 0, 0))


@Timer()
def execute_v2():
    """Memoize solutions of sub-problems"""
    data = read_data()
    for depth in range(len(data) - 2, -1, -1):
        for idx, _ in enumerate(data[depth]):
            data[depth][idx] += max(data[depth+1][idx], data[depth+1][idx+1])
    print(data[0][0])


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v2"
    if plan_of_attack == "v1":
        execute_v1()
    else:
        execute_v2()
