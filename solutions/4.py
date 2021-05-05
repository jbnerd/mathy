"""Plan of attack:
    v1: (0.299868 seconds)
        The problem can essentially be solved using a search on the search space. The most obvious search method is to
        use brute force. 111111 = 143 * 777 can be used as the baseline number because it is a known palindromic number
        with two three-digit factors.
    v2: (0.152263 seconds)
        To avoid double checks, we can add a restriction that one of the factors must be greater than or equal to the
        other factor.
    v3: (0.001408 seconds)
        Alternatively, we can start searching the factors from largest candidate value to smallest instead of the other
        way round. This will ensure that the largest palindromic number is found early and as soon as a candidate
        product is less than the current palindromic candidate, we can preempt the search for the second factor.
    v4: (0.000501 seconds)
        Let the largest number we have to find be P. P must be 6 digit because 111111 is the baseline.
        P = 100000x + 10000y + 1000z + 100z + 10y + x = 11 * (9091x + 910y + 100z)
        Therefore at least one of the factors of P must be divisible by 11. We can exploit this fact in our search.
"""
import sys

import _init_paths
from lib.utils.strings import is_palindrome_number
from lib.utils.generic import Timer


@Timer(name='decorator')
def execute_v1():
    max_palindrome = 111111
    for i in range(100, 1000):
        for j in range(100, 1000):
            candidate = i * j
            if is_palindrome_number(candidate) and candidate > max_palindrome:
                max_palindrome = candidate
    print(max_palindrome)


@Timer(name='decorator')
def execute_v2():
    max_palindrome = 111111
    for i in range(100, 1000):
        for j in range(i, 1000):
            candidate = i * j
            if is_palindrome_number(candidate) and candidate > max_palindrome:
                max_palindrome = candidate
    print(max_palindrome)


@Timer(name='decorator')
def execute_v3():
    max_palindrome = 111111
    for i in range(1000, 100, -1):
        for j in range(1000, i, -1):
            candidate = i * j
            if candidate < max_palindrome:
                break
            elif is_palindrome_number(candidate) and candidate > max_palindrome:
                max_palindrome = candidate
    print(max_palindrome)


@Timer(name='decorator')
def execute_v4():
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
