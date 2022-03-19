"""
Average execution times:
    v1: (0.296354 seconds)
    v2: (0.147609 seconds)
    v3: (0.001563 seconds)
    v4: (0.000402 seconds)
Answer: 906609

The problem is solved by searching on the appropriate search  space. For example 111111 = 143 * 777 is one of the first
palindromic number that comes to mind and has two three-digit factors. Hence, it can be used as a baseline number for
searching a larger number.
"""
import sys

import _init_paths
from euler.utils.strings import is_palindrome_number
from euler.utils.generic import Timer


@Timer()
def execute_v1():
    """Brute force search against the established baseline."""
    max_palindrome = 111111
    for i in range(100, 1000):
        for j in range(100, 1000):
            candidate = i * j
            if is_palindrome_number(candidate) and candidate > max_palindrome:
                max_palindrome = candidate
    print(max_palindrome)


@Timer()
def execute_v2():
    """
    To avoid checking a case twice, a restriction that one of the factors must be greater than or equal to the other
    factor is added - effectively reducing the search space by half.
    """
    max_palindrome = 111111
    for i in range(100, 1000):
        for j in range(i, 1000):
            candidate = i * j
            if is_palindrome_number(candidate) and candidate > max_palindrome:
                max_palindrome = candidate
    print(max_palindrome)


@Timer()
def execute_v3():
    """
    Instead of searching the candidates from the small to large, the loop can be reversed to find the desired number
    early. The search is pruned by preempting the search for the second factor as soon as the generated candidate gets
    smaller than the available max_palindrome.
    """
    max_palindrome = 111111
    for i in range(1000, 100, -1):
        for j in range(1000, i, -1):
            candidate = i * j
            if candidate < max_palindrome:
                break
            elif is_palindrome_number(candidate) and candidate > max_palindrome:
                max_palindrome = candidate
    print(max_palindrome)


@Timer()
def execute_v4():
    """
    Let the largest number we have to find be P. P must be 6 digit because 111111 is the baseline and P must be greater
    than the baseline. Thus,
        P = 100000x + 10000y + 1000z + 100z + 10y + x = 11 * (9091x + 910y + 100z)
    Since P is divisible by 11, at least one of the factors of P must be divisible by 11. This fact is leveraged to
    prune the search space even further.
    """
    max_palindrome = 111111
    a = 999
    while a >= 100:
        b, delta_b = (999, 1) if a % 11 == 0 else (990, 11)
        while b >= a:
            candidate = a * b
            if a * b <= max_palindrome:
                break
            elif is_palindrome_number(candidate) and candidate > max_palindrome:
                max_palindrome = candidate
            b -= delta_b
        a -= 1
    print(max_palindrome)


if __name__ == "__main__":
    plan_of_attack = sys.argv[1] if len(sys.argv) == 2 else "v4"
    if plan_of_attack == "v1":
        execute_v1()
    elif plan_of_attack == "v2":
        execute_v2()
    elif plan_of_attack == "v3":
        execute_v3()
    else:
        execute_v4()
