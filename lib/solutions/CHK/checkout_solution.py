import dataclasses
import math
import operator
from collections import Counter
from typing import List, Optional, Tuple


@dataclasses.dataclass
class SpecialOfferQuantity:
    min_quantity: int = 0
    offer_price: int = 0


@dataclasses.dataclass
class SpecialOfferFree:
    min_quantity: int = 0
    free_item: Optional[str] = None


@dataclasses.dataclass
class Item:
    name: str
    value: int
    special_offer_quantity: List[SpecialOfferQuantity] = dataclasses.field(
        default_factory=list
    )
    special_offer_free: List[SpecialOfferFree] = dataclasses.field(default_factory=list)


STOCK = {
    "A": Item(
        name="A",
        value=50,
        special_offer_quantity=[
            SpecialOfferQuantity(min_quantity=3, offer_price=130),
            SpecialOfferQuantity(min_quantity=5, offer_price=200),
        ],
    ),
    "B": Item(
        name="B",
        value=30,
        special_offer_quantity=[SpecialOfferQuantity(min_quantity=2, offer_price=45)],
    ),
    "C": Item(
        name="C",
        value=20,
    ),
    "D": Item(
        name="D",
        value=15,
    ),
    "E": Item(
        name="E",
        value=40,
        special_offer_free=[SpecialOfferFree(min_quantity=2, free_item="B")],
    ),
}

ALLOWED_ITEMS = set(STOCK.keys())
PROCESS_ITEMS_ORDER = ("E", "A", "B", "C", "D")


def all_items_allowed(items: set) -> bool:
    """Make sure all items are allowed."""
    return len(items - ALLOWED_ITEMS) == 0


def process_quantity_offer(
    special_offer: SpecialOfferQuantity,
    count: int,
) -> Tuple[int, int]:
    # Get number of discounted items if there's an offer
    discounted_items = math.floor(count / special_offer.min_quantity)
    discounted_price = discounted_items * special_offer.offer_price

    # number of items outside of the discount
    remaining_items = count - (discounted_items * special_offer.min_quantity)

    return discounted_price, remaining_items


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

        # initial value, no discount
        value = product.value * count

        # check special offers
        if product.special_offer_quantity:
            value = 0
            remaining_items = count

            quantities = sorted(
                [item for item in product.special_offer_quantity],
                key=operator.attrgetter("min_quantity"),
            )

            for min_quantity in quantities:
                discount_price, remaining_items = process_quantity_offer(
                        special_offer=special_offer,
                        count=remaining_items,
                )

            value = int(value)

        if product.special_offer_free:
            if special_offer.free_item:
                free_item_count = grouped_items.get(special_offer.free_item)
                free_items = math.floor(count / special_offer.quantity)

                new_count = free_item_count - free_items if free_item_count else 0
                grouped_items[special_offer.free_item] = new_count if new_count > 0 else 0

        total += value
    return total



