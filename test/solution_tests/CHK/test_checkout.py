import pytest

from solutions.CHK import checkout_solution


@pytest.mark.parametrize(
    "skus, expected",
    (
        ("", 0),  # no product
        ("x", -1),  # invalid
        ("a", 50),
        ("b", 30),
        ("c", 20),
        ("d", 15),
        ("e", 40),
        ("ab", 80),  # two items
        ("aa", 100),  # a discount
        ("aaa", 130),  # a discount
        ("aaaa", 180),  # 4 items, no discount?
        ("aaaaaa", 260),  # a discount
        ("bb", 45),  # b discount
        ("aaabb", 175),
        ("aabb", 145),
    )
)
def test_sum(skus: str, expected: int):
    assert checkout_solution.checkout(skus) == expected


@pytest.mark.parametrize(
    "allowed, received, expected",
    (
        ({"A", "B", "C"}, {"A", "B", "C"}, True),  # no product
        ({"A", "B", "C"}, {"A", "B"}, True),
        ({"A", "B", "C"}, {"x", "B", "C"}, False),
    )
)
def test_allowed_keys(skus: str, expected: int):
    assert checkout_solution.checkout(skus) == expected


