"""
This file provides utilities for operations on numbers represented as strings.
"""

import functools


class NumToWord:
    """Converts a natural number into its english representation"""

    _num_to_word = {
        1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
        11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
        70: 'Seventy', 80: 'Eighty', 90: 'Ninety'
    }

    @classmethod
    def convert(cls, num: int) -> str:
        if num <= 0 or num > 1000:
            raise ValueError('Only integers in [1, 1000] are supported for word representation.')
        elif num <= 99:
            return cls._handle_till_tens(num)
        elif num <= 999:
            return cls._handle_till_hundreds(num)
        else:
            return 'One Thousand'

    @classmethod
    def _handle_till_tens(cls, num: int) -> str:
        if num == 0:
            return ''
        elif num <= 20:
            return cls._num_to_word[num]
        else:
            tens = cls._num_to_word[num - (num % 10)]
            ones = cls._num_to_word.get(num % 10, '')
            return '-'.join([tens, ones])

    @classmethod
    def _handle_till_hundreds(cls, num: int) -> str:
        hundreds = cls._handle_hundreds_digit(num)
        tens = cls._handle_till_tens(num % 100)
        return ' and '.join([hundreds, tens]) if tens != '' else hundreds

    @classmethod
    def _handle_hundreds_digit(cls, num: int) -> str:
        return cls._num_to_word[int(num / 100)] + ' Hundred'


def is_palindrome_number(num: int) -> bool:
    num = str(num)
    return num == num[::-1]


def character_wise_product(string: str) -> int:
    return functools.reduce(lambda a, b: int(a) * int(b), string)
