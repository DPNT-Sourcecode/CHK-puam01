from .models import Item, SpecialOfferQuantity, SpecialOfferFree

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
    "G": Item(
        name="G",
        price=20,
    ),
}


