from typing import List
import pytest

from lib.utils.numeric import least_common_multiple, least_common_multiple_first_n_natural_numbers


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
