import pytest

from lib.utils.strings import is_palindrome_number


@pytest.mark.parametrize("palindrome", [
    9, 101, 9119, 12344321, 8769678,
])
def test_is_palindrome(palindrome):
    assert is_palindrome_number(palindrome)


@pytest.mark.parametrize("non_palindrome", [
    10, 193401
])
def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome_number(non_palindrome)
