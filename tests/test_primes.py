from typing import List

import pytest

from euler.primes import is_prime, nth_prime, prime_factors, prime_factorization


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


@pytest.mark.parametrize('n, prime', [
    (1, 2),
    (10, 29),
    (100, 541),
    (10000, 104729),
    (200000, 2750159)
])
def test_nth_prime(n, prime):
    assert prime == nth_prime(n)


def test_nth_prime_given_negative_n():
    with pytest.raises(ValueError) as exc:
        _ = nth_prime(-1)
    assert str(exc.value) == "Provide a positive number."


@pytest.mark.parametrize('n, correct_factors, correct_exponents', [
    (1, [], []),
    (2, [2], [1]),
    (13, [13], [1]),
    (28, [2, 7], [2, 1]),
    (32, [2], [5]),
    (100, [2, 5], [2, 2]),
    (9085, [5, 23, 79], [1, 1, 1]),
    (76576500, [2, 3, 5, 7, 11, 13, 17], [2, 2, 3, 1, 1, 1, 1])
])
def test_prime_factorization(n, correct_factors, correct_exponents):
    predicted_factors, predicted_exponents = prime_factorization(n)
    assert predicted_factors == correct_factors
    assert predicted_exponents == correct_exponents


def test_prime_factorization_given_negative_number():
    with pytest.raises(ValueError) as exc:
        prime_factorization(-1)
    assert str(exc.value) == "Provide a positive integer for factorization."


@pytest.mark.parametrize('num, correct_factors', [
    (1, []),
    (2, [2]),
    (13, [13]),
    (39, [3, 13]),
    (100, [2, 5]),
    (13195, [5, 7, 13, 29]),
    (111111, [3, 7, 11, 13, 37]),
    (600851475143, [71, 839, 1471, 6857])
])
def test_prime_factors(num: int, correct_factors: List[int]):
    predicted_factors = prime_factors(num)
    assert predicted_factors == correct_factors


def test_prime_factors_given_negative_number():
    with pytest.raises(ValueError) as exc:
        prime_factors(-1)
    assert str(exc.value) == "Provide a positive integer for factorization."
