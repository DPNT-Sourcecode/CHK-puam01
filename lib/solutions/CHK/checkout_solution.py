import dataclasses
import math
from collections import Counter
from typing import List, Optional


@dataclasses.dataclass
class SpecialOffer:
    quantity: int = 0
    offer: int = 0
    free_item: Optional[str] = None


@dataclasses.dataclass
class Item:
    name: str
    value: int
    special_offer: List[SpecialOffer] = dataclasses.field(default_factory=list)


STOCK = {
    "A": Item(
        name="A",
        value=50,
        special_offer=[
            SpecialOffer(quantity=3, offer=130),
            SpecialOffer(quantity=5, offer=200),
        ],
    ),
    "B": Item(
        name="A",
        value=30,
        special_offer=[SpecialOffer(quantity=2, offer=45)],
    ),
    "C": Item(
        name="A",
        value=20,
    ),
    "D": Item(
        name="A",
        value=15,
    ),
    "E": Item(
        name="E",
        value=40,
        special_offer=[SpecialOffer(quantity=2, free_item="B")],
    ),
}

ALLOWED_ITEMS = set(STOCK.keys())
PROCESS_ITEMS_ORDER = ("E", "A", "B", "C", "D")


def all_items_allowed(items: set) -> bool:
    """Make sure all items are allowed."""
    return len(items - ALLOWED_ITEMS) == 0


def process_special_offer(
    special_offer: SpecialOffer, product: Item, count: int, grouped_items: Counter
) -> int:
    if special_offer.free_item:
        free_item_count = grouped_items.get(special_offer.free_item)
        free_items = math.floor(count / special_offer.quantity)

        new_count = free_item_count - free_items if free_item_count else 0
        grouped_items[special_offer.free_item] = new_count if new_count > 0 else 0

    # Get number of discounted items if there's an offer
    discounted_items = (
        math.floor(count / special_offer.quantity) if special_offer.offer else 0
    )
    items_with_offer = discounted_items * special_offer.offer

    # number of items outside of the discount
    remaining_products = count - (discounted_items * special_offer.quantity)

    items_without_offer = remaining_products * product.value
    return int(items_with_offer + items_without_offer)


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
        special_offers = product.special_offer
        # check special offers
        if special_offers:
            value = math.inf

            for special_offer in special_offers:
                value = min(
                    value,
                    process_special_offer(
                        special_offer=special_offer,
                        count=count,
                        product=product,
                        grouped_items=grouped_items,
                    ),
                )

            value = int(value)

        else:
            value = product.value * count
        total += value
    return total





