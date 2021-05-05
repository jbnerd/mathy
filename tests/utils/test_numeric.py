from typing import List
import pytest

from lib.utils.numeric import least_common_multiple


@pytest.mark.parametrize('numbers, correct_lcm', [
    ([i for i in range(1, 6)], 60),
    ([i for i in range(1, 11)], 2520)
])
def test_least_common_multiple(numbers: List[int], correct_lcm: int):
    predicted_lcm = least_common_multiple(numbers)
    assert predicted_lcm == correct_lcm
