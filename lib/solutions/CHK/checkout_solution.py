import math
import operator
from collections import Counter
from typing import Dict, List, Optional, Tuple

from .models import Item, SpecialOfferQuantity, SpecialOfferFree
from .database import STOCK


ALLOWED_ITEMS = set(STOCK.keys())


def items_process_order(items: Dict[str, Item]) -> Tuple[str]:
    """Order the items into the processing order.

    Some items need to be processed earlier as they the result will
    affect other processing.

    The order is:

    - Special item free
    - Special item quantity
    - Normal items

    Group items are excluded from this order as they will have their own
    processing.
    """
    items_with_free_offer = []
    items_with_quantity_offer = []
    normal_items = []
    for item in items.values():
        if item.special_offer_free:
            items_with_free_offer.append(item.name)
        elif item.special_offer_quantity:
            items_with_quantity_offer.append(item.name)
        elif not item.group_item:
            normal_items.append(item.name)

    return tuple(items_with_free_offer + items_with_quantity_offer + normal_items)


PROCESS_ITEMS_ORDER = items_process_order(STOCK)


GROUP_ITEMS = tuple([item.name for item in STOCK.values() if item.group_item])


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
    items_count_by_name = Counter(skus)

    # Make sure all items are alloed
    items = set(items_count_by_name.keys())
    if not all_items_allowed(items):
        return -1

    # We need to process the items that have free special offer first,
    # so the order is import
    for item_name in PROCESS_ITEMS_ORDER:
        # Get the count of this item if any
        count = items_count_by_name.get(item_name)
        if not count:
            continue

        try:
            product = STOCK[item_name]
        except KeyError:
            return -1

        # Process free special offers. Bear in mind that you can have special
        # offers that will give a free product when you buy x amount of the
        # same item, so it must be processed before the quantities
        if product.special_offer_free:
            for special_offer in product.special_offer_free:
                # There's a requirement of a minimum basket items
                if count < special_offer.basket_quantity:
                    continue

                item_to_discount = items_count_by_name.get(special_offer.free_item)

                # If we have minimum basket items, check how many
                # of them fits in count, otherwise use the min_quantity
                free_items = (
                    math.floor(count / special_offer.basket_quantity)
                    if special_offer.basket_quantity
                    else math.floor(count / special_offer.min_quantity)
                )

                new_count = item_to_discount - free_items if item_to_discount else 0
                items_count_by_name[special_offer.free_item] = (
                    new_count if new_count > 0 else 0
                )

        # Refresh count
        count = items_count_by_name[item_name]

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

    for item_name in GROUP_ITEMS:
        # Get the count from grouped items and process if any
        count = items_count_by_name.get(item_name)
        if not count:
            continue

        try:
            product = STOCK[item_name]
        except KeyError:
            return -1

        # initial value, no discount
        value = product.price * count
        total += value

    return total


