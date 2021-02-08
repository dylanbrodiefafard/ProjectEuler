import operator
from functools import reduce


def prod(iterable, start_val=1):
    return reduce(operator.mul, iterable, start_val)
