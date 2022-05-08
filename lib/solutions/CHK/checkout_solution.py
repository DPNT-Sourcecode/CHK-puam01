import dataclasses
import math
from collections import Counter
from typing import Optional


@dataclasses.dataclass
class SpecialOffer:
    quantity: int = 0
    offer: int = 0
    free_item: Optional[str] = None


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
    "E": Item(
        name="E",
        value=40,
        special_offer=SpecialOffer(free_item="B"),
    ),
}

ALLOWED_ITEMS = set(STOCK.keys())
PROCESS_ITEMS_ORDER = ("E", "A", "B", "C", "D")


def all_items_allowed(items: set) -> bool:
    """Make sure all items are allowed."""
    return len(items - ALLOWED_ITEMS) == 0


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    total = 0

    # Counter will give the count of each item
    grouped_items = Counter(skus)

    # Make sure all items are alloed
    items = set(grouped_items.keys())
    if not all_items_allowed(items):
        return -1

    # We need to process the items that have free special offer first,
    # so the order is import
    for item_name in PROCESS_ITEMS_ORDER:
        # Get the count from grouped items and process if any
        count = grouped_items.get(item_name)
        if not count:
            continue

        try:
            product = STOCK[item_name]
        except KeyError:
            return -1

        count = grouped_items[item_name]
        special_offer = product.special_offer
        # check special offers
        if special_offer:
            if special_offer.free_item:
                free_item_count = grouped_items.get(special_offer.free_item)
                new_count = free_item_count - count if free_item_count else 0
                grouped_items[special_offer.free_item] = new_count if new_count > 0 else 0

            if special_offer.quantity:
                discounted_items = math.floor(count / special_offer.quantity)

                # number of items outside of the discount
                remaining_products = count - (discounted_items * special_offer.quantity)

                items_without_offer = remaining_products * product.value
                items_with_offer = discounted_items * special_offer.offer
                value = int(items_with_offer + items_without_offer)
            else:
                value = product.value * count

        else:
            value = product.value * count
        total += value
    return total







