from typing import List
import pytest

from lib.utils.primes import is_prime, get_nth_prime, PrimeFactors


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
    (28, [2, 7]),
    (39, [3, 13]),
    (13195, [5, 7, 13, 29]),
    (111111, [3, 7, 11, 13, 37]),
    (600851475143, [71, 839, 1471, 6857])
])
def test_get_prime_factors(num: int, correct_factors: List[int]):
    predicted_factors = PrimeFactors.get_prime_factors(num)
    assert predicted_factors == correct_factors


@pytest.mark.parametrize('n, prime', [
    (6, 13),
    (100, 541)
])
def test_get_nth_prime(n, prime):
    assert prime == get_nth_prime(n)


@pytest.mark.parametrize('n, factors, exponents', [
    (28, [2, 7], [2, 1]),
    (76576500, [2, 3, 5, 7, 11, 13, 17], [2, 2, 3, 1, 1, 1, 1])
])
def test_prime_factorization(n, factors, exponents):
    predicted_factors, predicted_exponents = PrimeFactors.prime_factorization(n)
    assert predicted_factors == factors
    assert predicted_exponents == exponents
