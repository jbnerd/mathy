"""Plan of attack:
    v1: (0.000034 seconds)
        The number of lattice paths in an m x n grid is given by C(m+n, n) or C(m+n, m). Where C(a, b) represents the
        number of ways in which b distinct objects can be selected from a distinct objects.
"""
import _init_paths
from lib.utils.generic import Timer
from lib.utils.numeric import num_combinations


@Timer(name='decorator')
def execute_v1():
    print(num_combinations(40, 20))


if __name__ == "__main__":
    execute_v1()
