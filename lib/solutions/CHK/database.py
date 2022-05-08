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
    "H": Item(
        name="H",
        price=10,
        special_offer_quantity=[
            SpecialOfferQuantity(min_quantity=5, offer_price=45),
            SpecialOfferQuantity(min_quantity=10, offer_price=80),
        ],
    ),
    "I": Item(
        name="I",
        price=35,
    ),
    "J": Item(
        name="J",
        price=60,
    ),
    "K": Item(
        name="K",
        price=80,
        special_offer_quantity=[
            SpecialOfferQuantity(min_quantity=2, offer_price=150),
        ],
    ),
    "L": Item(
        name="L",
        price=90,
    ),
    "M": Item(
        name="M",
        price=15,
    ),
    "N": Item(
        name="N",
        price=40,
        special_offer_free=[SpecialOfferFree(min_quantity=3, free_item="M")],
    ),
    "O": Item(
        name="O",
        price=10,
    ),
    "P": Item(
        name="P",
        price=50,
        special_offer_quantity=[
            SpecialOfferQuantity(min_quantity=5, offer_price=200),
        ],
    ),
    "Q": Item(
        name="Q",
        price=30,
        special_offer_quantity=[
            SpecialOfferQuantity(min_quantity=3, offer_price=80),
        ],
    ),
    "R": Item(
        name="R",
        price=50,
        special_offer_free=[SpecialOfferFree(min_quantity=3, free_item="Q")],
    ),
    "S": Item(
        name="S",
        price=30,
    ),
    "T": Item(
        name="T",
        price=20,
    ),
    "U": Item(
        name="U",
        price=40,
        special_offer_free=[
            SpecialOfferFree(min_quantity=3, basket_quantity=4, free_item="U")
        ],
    ),
    "V": Item(
        name="V",
        price=50,
        special_offer_quantity=[
            SpecialOfferQuantity(min_quantity=2, offer_price=90),
            SpecialOfferQuantity(min_quantity=3, offer_price=130),
        ],
    ),
    "W": Item(
        name="W",
        price=20,
    ),
    "X": Item(
        name="X",
        price=90,
    ),
    "Y": Item(
        name="Y",
        price=10,
    ),
    "Z": Item(
        name="Z",
        price=50,
    ),
}
