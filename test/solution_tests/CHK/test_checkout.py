import pytest

from solutions.CHK import checkout_solution


@pytest.mark.parametrize(
    "skus, expected",
    (
        ("", 0),  # no product
        ("X", -1),  # invalid
        ("A", 50),  # one product
        ("AB", 80),  # one product
    )
)
def test_sum(skus: str, expected: int):
    assert checkout_solution.checkout(skus) == expected


