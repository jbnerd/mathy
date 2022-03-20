"""
This file provides utilities for operations on numbers represented as strings.
"""

import functools


def is_palindrome_number(num: int) -> bool:
    num = str(num)
    return num == num[::-1]


def character_wise_product(string: str) -> int:
    return functools.reduce(lambda a, b: int(a) * int(b), string)
