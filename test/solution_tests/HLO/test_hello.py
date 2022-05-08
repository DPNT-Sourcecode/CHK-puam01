import pytest

from solutions.HLO import hello_solution


@pytest.mark.parametrize(
    "friend_name, expected",
    (
        ("Craftsman", "Hello, World!"),  # normal case
        ("Mr. X", "Hello, World!"),
    )
)
def test_sum(friend_name: str, expected: str):
    assert hello_solution.hello(friend_name) == expected


