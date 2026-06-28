import random


def select_random_items(items: list, count: int) -> list:
    """
    Selects a specified number of random items from a list.
    """

    if len(items) <= count:
        return items

    return random.sample(items, count)
