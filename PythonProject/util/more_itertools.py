from functools import partial
from itertools import product


def exactly_n(iterable, n):
    """Returns whether or not the iterable has exactly n items.
    This will iterate over the iterable up to n + 1 times.
    """
    assert n >= 0
    count = 0
    for _ in iterable:
        count += 1
        if count > n:
            return False
    return count == n


def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *pred* is not None, returns the first item
    for which pred(item) is true.
    """
    return next(filter(pred, iterable), default)


def str_product(a, b):
    """Concatenates every item from a with every item from b.
    """
    return map(partial(str.join, ''), product(a, b))
