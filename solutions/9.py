"""
Average execution times:
    v1: (9.379466 seconds)
    v2: (0.085179 seconds)
    v3: (0.011305 seconds)
    v4: (0.000048 seconds)
Answer: 31875000
"""
import sys
from math import sqrt

import _init_paths
from lib.utils.generic import Timer


@Timer()
def execute_v1():
    """Brute force search using the condition a < b < c."""
    for c in range(1000, 0, -1):
        for b in range(c, 0, -1):
            for a in range(b, 0, -1):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print(a * b * c)


@Timer()
def execute_v2():
    """Search is pruned using the constraint a + b + c = 1000. Since a < b, hence 2b > 1000 - c."""
    for c in range(1000, 0, -1):
        for b in range(c, int(500 - c/2), -1):
            if b + c < 1000:
                a = 1000 - b - c
                if a ** 2 + b ** 2 == c ** 2:
                    print(a * b * c)


@Timer()
def execute_v3():
    """Search is further pruned using the triangular inequality. We have a < b < c < 500."""
    for c in range(500, 0, -1):
        for b in range(c, int(500 - c / 2), -1):
            if b + c < 1000:
                a = 1000 - b - c
                if a ** 2 + b ** 2 == c ** 2:
                    print(a * b * c)


@Timer()
def execute_v4():
    """
    A basic Pythagorean triplet generator is used: a = m**2 - n**2, b = 2mn, c = m**2 + n**2.
        a > 0 => m**2 > n**2. --(1)
        As we know from v3 c < 500 => m**2 < 500 - n**2. --(2)
        From (1) and (2) we get n < 5 * sqrt(10).
        Also, a + b + c = 1000 => m(m + n) = 500 => m = (-n + sqrt(n^2 + 2000)) / 2
    """
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
