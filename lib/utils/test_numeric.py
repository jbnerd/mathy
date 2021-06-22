from functools import reduce
from typing import List
import json

import pytest

from lib.utils.numeric import get_factors
from lib.utils.numeric import sum_of_natural_numbers, sum_of_squares_of_natural_numbers, least_common_multiple, \
    least_common_multiple_of_natural_numbers, large_number_sum, large_number_mul, large_number_pow


@pytest.mark.parametrize('num, correct_sum', [
    (0, 0),
    (10, 55),
    (100, 5050)
])
def test_sum_of_natural_numbers(num, correct_sum):
    predicted_sum = sum_of_natural_numbers(num)
    assert predicted_sum == correct_sum


def test_sum_of_natural_numbers_given_negative_num():
    with pytest.raises(ValueError) as exc:
        _ = sum_of_natural_numbers(-1)
    assert str(exc.value) == "Provide a non-negative natural number."


@pytest.mark.parametrize('num, correct_sum', [
    (0, 0),
    (10, 385),
    (100, 338350)
])
def test_sum_of_squares_of_natural_numbers(num, correct_sum):
    predicted_sum = sum_of_squares_of_natural_numbers(num)
    assert predicted_sum == correct_sum


def test_sum_of_squares_of_natural_numbers_given_negative_number():
    with pytest.raises(ValueError) as exc:
        _ = sum_of_squares_of_natural_numbers(-1)
    assert str(exc.value) == "Provide a non-negative natural number."


@pytest.mark.parametrize('numbers, correct_lcm', [
    ([2, 3, 5, 7], 210),
    ([3, 5, 7, 15], 105),
    ([1, 4, 6, 792, 936, 10296], 10296),
    ([i for i in range(1, 6)], 60),
    ([i for i in range(1, 11)], 2520)
])
def test_least_common_multiple(numbers: List[int], correct_lcm: int):
    predicted_lcm = least_common_multiple(numbers)
    assert predicted_lcm == correct_lcm


@pytest.mark.parametrize('numbers', [
    ([-1, 2, 3, 4, 5]),
    ([1, -2, -3, 4, 5]),
    ([1, 2, 3, -4, 5]),
    ([1, 2, 3, 4, -5]),
    ([-1, -2, -3, -4, -5])
])
def test_least_common_multiple_given_negative_numbers(numbers):
    with pytest.raises(ValueError) as exc:
        _ = least_common_multiple(numbers)
    assert str(exc.value) == "Provide positive integers only."


@pytest.mark.parametrize('upper_bound, correct_lcm', [
    (5, 60),
    (10, 2520),
    (15, 360360),
    (20, 232792560),
    (23, 5354228880)
])
def test_least_common_multiple_of_natural_numbers(upper_bound, correct_lcm):
    predicted_lcm = least_common_multiple_of_natural_numbers(upper_bound)
    assert predicted_lcm == correct_lcm


def test_least_common_multiple_of_natural_numbers_given_negative_number():
    with pytest.raises(ValueError) as exc:
        _ = least_common_multiple_of_natural_numbers(-1)
    assert str(exc.value) == "Provide positive integers only."


@pytest.mark.parametrize('num, factors', [
    (1, []),
    (3, []),
    (6, [2, 3]),
    (10, [2, 5]),
    (28, [2, 4, 7, 14]),
    (100, [2, 4, 5, 10, 20, 25, 50])
])
def test_get_factors(num, factors):
    predicted_factors = get_factors(num)
    assert predicted_factors == factors


def test_get_factors_given_negative_number():
    with pytest.raises(ValueError) as exc:
        _ = get_factors(-1)
    assert str(exc.value) == "Provide a natural number."


@pytest.fixture()
def large_number_sum_data():
    with open('lib/test_data/50_large_numbers.txt') as infile:
        data = infile.read().strip().split('\n')
    return data


@pytest.mark.parametrize('data, correct_total', [
    ['large_number_sum_data', '5537376230390876637302048746832985971773659831892672']
])
def test_large_number_sum(data, correct_total, request):
    data = request.getfixturevalue(data)
    predicted_total = reduce(lambda a, b: large_number_sum(a, b), data)
    assert predicted_total == correct_total


@pytest.mark.parametrize('num1, num2, correct_product', [
    (4154, 51454, 213739916),
    (654154154151454545415415454, 63516561563156316545145146514654,
     41549622603955309777243716069997997007620439937711509062916)
])
def test_large_number_mul(num1, num2, correct_product):
    predicted_product = large_number_mul(str(num1), str(num2))
    assert predicted_product == str(correct_product)


@pytest.fixture()
def large_powers_data():
    with open('lib/test_data/large_powers.json') as infile:
        data = json.load(infile)
    return data


@pytest.mark.parametrize('data, test_case_number', [
    ('large_powers_data', 1)
])
def test_large_number_power(data, test_case_number, request):
    data = request.getfixturevalue(data)
    base, exp, correct_result = data[str(test_case_number)]
    predicted_result = large_number_pow(str(base), str(exp))
    assert predicted_result == str(correct_result)
