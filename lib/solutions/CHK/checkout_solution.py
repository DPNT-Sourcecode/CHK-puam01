import dataclasses
from collections import Counter
from typing import Optional


@dataclasses.dataclass
class SpecialOffer:
    quantity: int = 0
    offer: int = 0


@dataclasses.dataclass
class Item:
    name: str
    value: int
    special_offer: Optional[SpecialOffer] = None


STOCK = {
    "A": Item(
        name="A",
        value=50,
        special_offer=SpecialOffer(quantity=3, offer=130),
    ),
    "B": Item(
        name="A",
        value=30,
        special_offer=SpecialOffer(quantity=2, offer=45),
    ),
    "C": Item(
        name="A",
        value=20,
        special_offer=None,
    ),
    "D": Item(
        name="A",
        value=15,
        special_offer=None,
    ),
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    total = 0

    # Counter will give the count of each item
    grouped_items = Counter(skus)

    for item_name, count in grouped_items:
        try:
            product = STOCK[item_name]
        except KeyError:
            return -1

        # check special offers
        total += product.value
    return total





