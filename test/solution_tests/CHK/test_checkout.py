import pytest

from solutions.CHK import checkout_solution


@pytest.mark.parametrize(
    "skus, expected",
    (
        ("X", -1),  # invalid
    )
)
def test_sum(skus: str, expected: int):
    assert checkout_solution.checkout(skus) == expected
