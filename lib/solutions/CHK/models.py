import dataclasses
from typing import List


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
