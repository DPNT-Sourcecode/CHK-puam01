import pytest

from solutions.SUM import sum_solution


@pytest.mark.parametrize(
    "x, y, expected",
    (
        (1, 2, 3),
        (1, 2, 4),
    )
)
def test_sum(x: int, y: int, expected: int):
    assert sum_solution.compute(x, y) == expected

