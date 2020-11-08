import operator
from functools import reduce
from typing import Iterable


def prod(iterable: Iterable[int], start_val=1) -> int:
    return reduce(operator.mul, iterable, start_val)
