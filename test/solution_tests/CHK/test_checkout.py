import pytest

from solutions.CHK import checkout_solution


@pytest.mark.parametrize(
    "skus, expected",
    (
        ("", 0),  # no product
        ("-", -1),  # invalid
        ("A", 50),
        ("B", 30),
        ("C", 20),
        ("D", 15),
        ("E", 40),
        ("AB", 80),  # two items
        ("AA", 100),  # A discount
        ("AAA", 130),
        ("AAAA", 180),  # 4 items with discount
        ("AAAAA", 200),  # 5 items
        ("AAAAAA", 250),  # A 5 items discount + 1
        ("AAAAAAAA", 330),  # 5 then 3
        ("AAAAAAAAA", 380),  # 5 - 3 - 1
        ("AAAAAAAAAAA", 450),  # 5 - 5 - 1
        ("BB", 45),  # B discount
        ("AAABB", 175),
        ("AABB", 145),
        ("EB", 70),
        ("EBB", 85),
        ("EEB", 80),
        ("EEBB", 110),  # discount on B
        ("ABCDE", 155),
        ("AAAAAEEBAAABB", 455),
        ("F", 10),
        ("FF", 20),
        ("FFF", 20),  # 1 free item
        ("FFFF", 30),
        ("FFFFF", 40),
        ("FFFFFF", 40),  # not a multiple of 3, so only 1 item is free
        ("G", 20),
        ("H", 10),
        ("HHHHH", 45),  # 5 discount H
        ("HHHHHH", 55),  # 5 discount + 1 H
        ("HHHHHHHHHH", 80),  # 10 discount H
        ("HHHHHHHHHHH", 90),  # 10 discount H
        ("HHHHHHHHHHHHHHH", 125),  # 10 + 5 discount H
        ("I", 35),
        ("J", 60),
        ("K", 70),
        ("KK", 120),  # Discount K
        ("KKK", 190),
        ("L", 90),
        ("M", 15),
        ("N", 40),
        ("MN", 55),
        ("MNN", 95),
        ("MNNN", 120),  # Free M
        ("O", 10),
        ("P", 50),
        ("PPPPP", 200),  # Discount P
        ("PPPPPP", 250),  # Discount P + 1
        ("PPPPPPPPPP", 400),  # p Discount P
        ("Q", 30),
        ("QQQ", 80),  # Discount Q
        ("QQQQ", 110),  # Discount Q + 1
        ("R", 50),
        ("RRRQ", 150),  # Free Q
        ("RRRQQQQ", 230),  # Free Q and Discount Q
        ("S", 20),
        ("T", 20),
        ("U", 40),
        ("UUU", 120),
        ("UUUU", 120),  # Free U
        ("V", 50),
        ("VV", 90),  # Discount 2 V
        ("VVV", 130),  # Discount 3 V
        ("VVVV", 180),  # 2 Discount 2 V
        ("VVVVVV", 260),  # 2 Discount 2 V
        ("W", 20),
        ("X", 17),
        ("Y", 20),
        ("Z", 21),
        ("YZ", 41),
        ("YZZ", 45),
        ("YZZST", 85),
        ("YZZSX", 82),
        ("YZZSXT", 90),
        ("XXXY", 62),
        ("YYZZZZ", 90),
        ("XXYYZZZZ", 124),
    )
)
def test_checkout(skus: str, expected: int):
    assert checkout_solution.checkout(skus) == expected


@pytest.mark.parametrize(
    "items, expected",
    (
        (checkout_solution.ALLOWED_ITEMS, True),
        ({"A", "B"}, True),
        ({"x", "B", "C"}, False),
    )
)
def test_allowed_keys(items, expected):
    assert checkout_solution.all_items_allowed(items) == expected



