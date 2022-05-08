import pytest

from solutions.HLO import hello


@pytest.mark.parametrize(
    "friend_name, expected",
    (
        ("Craftsman", "Hello, World!"),  # normal case
        ("Mr. X", "Hello, World!"),
    )
)
def test_sum(x: int, y: int, expected: int):
    assert hello.compute(x, y) == expected

