STOCK = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    total = 0
    for product in skus:
        try:
            value = STOCK[product]
        except KeyError:
            return -1
        total += value
    return total






