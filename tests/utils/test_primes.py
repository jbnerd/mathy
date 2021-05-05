from typing import List
import pytest

from lib.utils.primes import is_prime, get_prime_factors


@pytest.mark.parametrize('num', [
    2, 3, 5, 7, 17, 31, 101, 37
])
def test_is_prime(num: int):
    assert is_prime(num)


@pytest.mark.parametrize('num', [
    1, 49, 36, 50, -10, 10, 200000
])
def test_not_is_prime(num: int):
    assert not is_prime(num)


@pytest.mark.parametrize('num, correct_factors', [
    (39, [3, 13]),
    (13195, [5, 7, 13, 29]),
    (111111, [3, 7, 11, 13, 37]),
    (600851475143, [71, 839, 1471, 6857])
])
def test_get_prime_factors(num: int, correct_factors: List[int]):
    predicted_factors = get_prime_factors(num)
    assert predicted_factors == set(correct_factors)
