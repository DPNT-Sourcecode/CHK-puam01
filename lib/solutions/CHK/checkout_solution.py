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
    basket_quantity: int = 0
    free_item: str = ""


@dataclasses.dataclass
class Item:
    name: str
    price: int
    special_offer_quantity: List[SpecialOfferQuantity] = dataclasses.field(
        default_factory=list
    )
    special_offer_free: List[SpecialOfferFree] = dataclasses.field(default_factory=list)


STOCK = {
    "A": Item(
        name="A",
        price=50,
        special_offer_quantity=[
            SpecialOfferQuantity(min_quantity=3, offer_price=130),
            SpecialOfferQuantity(min_quantity=5, offer_price=200),
        ],
    ),
    "B": Item(
        name="B",
        price=30,
        special_offer_quantity=[SpecialOfferQuantity(min_quantity=2, offer_price=45)],
    ),
    "C": Item(
        name="C",
        price=20,
    ),
    "D": Item(
        name="D",
        price=15,
    ),
    "E": Item(
        name="E",
        price=40,
        special_offer_free=[SpecialOfferFree(min_quantity=2, free_item="B")],
    ),
    "F": Item(
        name="F",
        price=10,
        special_offer_free=[
            SpecialOfferFree(min_quantity=2, basket_quantity=3, free_item="F")
        ],
    ),
}

ALLOWED_ITEMS = set(STOCK.keys())
PROCESS_ITEMS_ORDER = ("F", "E", "A", "B", "C", "D")


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

        if product.special_offer_free:
            for special_offer in product.special_offer_free:
                # There's a requirement of a minimum basket items
                if count < special_offer.basket_quantity:
                    continue

                free_item_count = grouped_items.get(special_offer.free_item)

                free_items = math.floor(count / special_offer.min_quantity)

                new_count = free_item_count - free_items if free_item_count else 0
                grouped_items[special_offer.free_item] = (
                    new_count if new_count > 0 else 0
                )

        # initial value, no discount
        value = product.price * count

        # check quantity special offers
        if product.special_offer_quantity:
            value = 0
            remaining_items = count

            # sort the quantities by min quantity. The idea here is to fit
            # the maximum amount of the largest min quantity, then we move
            # on to the next quantity
            sorted_offers = sorted(
                [item for item in product.special_offer_quantity],
                key=operator.attrgetter("min_quantity"),
                reverse=True,
            )

            for special_offer in sorted_offers:
                discount_price, remaining_items = process_quantity_offer(
                    special_offer=special_offer,
                    count=remaining_items,
                )
                value += int(discount_price)

            # If there are remaining items without discount, we add them with
            # the full price
            if remaining_items:
                value += remaining_items * product.price

        total += value
    return total


