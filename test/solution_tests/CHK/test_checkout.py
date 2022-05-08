import pytest

from solutions.CHK import checkout_solution


@pytest.mark.parametrize(
    "skus, expected",
    (
        ("", 0),  # no product
        ("X", -1),  # invalid
        ("A", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("E", 40),
        ("AB", 80),  # two items
        ("AA", 100),  # A discount
        ("AAA", 130),  # A discount
        ("AAAA", 180),  # 4 items, no discount?
        ("AAAAAA", 260),  # A discount
        ("BB", 45),  # B discount
        ("AAABB", 175),
        ("AABB", 145),
    )
)
def test_sum(skus: str, expected: int):
    assert checkout_solution.checkout(skus) == expected

