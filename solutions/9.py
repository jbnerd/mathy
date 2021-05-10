"""Plan of attack:
    v1: (9.379466 seconds)
        Brute force search. Use the condition a < b < c.
    v2: (0.085179 seconds)
        Use the constraint a + b + c = 1000 to reduce the search space. Since a < b => 2b > 1000 - c.
    v3: (0.011305 seconds)
        By using the triangular inequality, we have a < b < c < 500.
    v4: (0.000048 seconds)
        Use the following generator for Pythagorean triplets: a = m**2 - n**2, b = 2mn, c = m**2 + n**2.
        a > 0 => m**2 > n**2 and a + b + c = 1000 => 2m(m + n) = 1000. --(1)
        As we know from v3 c < 500 => m**2 < 500 - n**2. --(2)
        From (1) and (2) we get n < 5 * sqrt(10).
"""
import sys
from math import sqrt

import _init_paths
from lib.utils.generic import Timer


@Timer(name='decorator')
def execute_v1():
    for c in range(1000, 0, -1):
        for b in range(c, 0, -1):
            for a in range(b, 0, -1):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print(a * b * c)


@Timer(name='decorator')
def execute_v2():
    for c in range(1000, 0, -1):
        for b in range(c, int(500 - c/2), -1):
            if b + c < 1000:
                a = 1000 - b - c
                if a ** 2 + b ** 2 == c ** 2:
                    print(a * b * c)


@Timer(name='decorator')
def execute_v3():
    for c in range(500, 0, -1):
        for b in range(c, int(500 - c / 2), -1):
            if b + c < 1000:
                a = 1000 - b - c
                if a ** 2 + b ** 2 == c ** 2:
                    print(a * b * c)


@Timer(name='decorator')
def execute_v4():
    for n in range(int(5 * sqrt(10))):
        m = (-n + sqrt(n**2 + 2000)) / 2
        if int(m) == m:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            print(int(a * b * c))


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
