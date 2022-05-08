import dataclasses
import math
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

    for item_name in grouped_items:
        try:
            product = STOCK[item_name]
        except KeyError:
            return -1

        count = grouped_items[item_name]
        # check special offers
        if product.special_offer and count >= product.special_offer.quantity:
            discounted_items = math.floor(count / product.special_offer.quantity)

            # number of items outside of the discount
            remaining_products = count - (discounted_items * product.special_offer.quantity)

            items_without_offer = remaining_products * product.value
            items_with_offer = discounted_items * product.special_offer.offer
            value = int(items_with_offer + items_without_offer)
        else:
            value = product.value * count
        total += value
    return total






