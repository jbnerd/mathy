from typing import List
import pytest

from lib.utils.numeric import least_common_multiple, least_common_multiple_first_n_natural_numbers
from lib.utils.numeric import get_factors


@pytest.mark.parametrize('numbers, correct_lcm', [
    ([2, 3, 5, 7], 210),
    ([i for i in range(1, 6)], 60),
    ([i for i in range(1, 11)], 2520)
])
def test_least_common_multiple(numbers: List[int], correct_lcm: int):
    predicted_lcm = least_common_multiple(numbers)
    assert predicted_lcm == correct_lcm


@pytest.mark.parametrize('upper_bound, correct_lcm', [
    (5, 60),
    (10, 2520)
])
def test_least_common_multiple_first_n_natural_numbers(upper_bound, correct_lcm):
    predicted_lcm = least_common_multiple_first_n_natural_numbers(upper_bound)
    assert predicted_lcm == correct_lcm


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
