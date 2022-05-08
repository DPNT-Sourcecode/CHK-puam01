import pytest

from solutions.HLO import hello


@pytest.mark.parametrize(
    "friend_name, expected",
    (
        (1, 2, 3),  # normal case
        (0, 100, 100),  # boundary 0, 100
        (100, 0, 100),  # boundary 100, 0
    )
)
def test_sum(x: int, y: int, expected: int):
    assert hello.compute(x, y) == expected
