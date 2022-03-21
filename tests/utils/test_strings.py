import pytest

from euler.utils.strings import is_palindrome_number, NumToWord


@pytest.mark.parametrize('num, word', [
    (6, 'Six'),
    (20, 'Twenty'),
    (56, 'Fifty-Six'),
    (100, 'One Hundred'),
    (556, 'Five Hundred and Fifty-Six'),
    (1000, 'One Thousand')
])
def test_num_to_word_acceptable_range(num, word):
    predicted_word = NumToWord.convert(num)
    assert predicted_word == word


@pytest.mark.parametrize('num', [
    0, -10, 1001, 10000
])
def test_num_to_word_out_of_acceptable_range(num):
    with pytest.raises(ValueError) as exc:
        _ = NumToWord.convert(num)
    assert str(exc.value) == 'Only integers in [1, 1000] are supported for word representation.'


@pytest.mark.parametrize('palindrome', [
    9, 101, 9119, 12344321, 8769678,
])
def test_is_palindrome(palindrome):
    assert is_palindrome_number(palindrome)


@pytest.mark.parametrize('non_palindrome', [
    10, 193401
])
def test_not_is_palindrome(non_palindrome):
    assert not is_palindrome_number(non_palindrome)
