import pytest

from solutions.SUM import sum_solution


@pytest.mark.parametrize(
    "x, y, expected",
    (
        (1, 2, 3),  # normal case
        (0, 100, 100),
        (100, 0, 100),
    )
)
def test_sum(x: int, y: int, expected: int):
    assert sum_solution.compute(x, y) == expected


