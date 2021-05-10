"""Plan of attack:
    v1: (0.002185 seconds)
        Collect digits window-wise and keep a track of the maximum product.
"""
import _init_paths
from lib.utils.strings import character_wise_product
from lib.utils.generic import Timer


@Timer(name='decorator')
def execute_v1():
    with open('solutions/data/8.txt') as infile:
        data = ''.join(infile.read().strip().split('\n'))

    max_prod = 0
    for i, _ in enumerate(data[:-13]):
        max_prod = max(max_prod, character_wise_product(data[i:i+13]))
    print(max_prod)


if __name__ == "__main__":
    execute_v1()
