from collections import Iterable
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


def first_true(iterable, default=False, predicate=None):
    """Returns the first true value in the iterable.

    If no true value is found, returns *default*

    If *predicate* is not None, returns the first item
    for which predicate(item) is true.
    """
    return next(filter(predicate, iterable), default)


def str_product(a, b):
    """Concatenates every item from a with every item from b.
    """
    return map(partial(str.join, ''), product(a, b))


def flatten(iterable, max_depth=None):
    """Flattens an iterable by expanding any iterable elements.
    If max_depth is provided, only the iterables with nesting
    level less than max_depth are expanded.
    """

    def _flatten(_iterable, _depth):
        for element in _iterable:
            if (max_depth is None or _depth < max_depth) and isinstance(element, Iterable) and not isinstance(element, (str, bytes)):
                yield from _flatten(element, _depth + 1)
            else:
                yield element

    yield from _flatten(iterable, 0)
