"""
[Number letter counts](https://projecteuler.net/problem=17)

Median execution times over 5 runs:
    v1: 0.001469 seconds
Answer: 21124
"""
import _init_paths
from euler.utils.generic import Timer
from euler.utils.strings import NumToWord


@Timer()
def execute_v1():
    total_count = 0
    for i in range(1, 1001):
        word = NumToWord.convert(i)
        word = ''.join(word.split())
        word = ''.join(word.split('-'))
        total_count += len(word)
    print(total_count)


if __name__ == "__main__":
    execute_v1()
