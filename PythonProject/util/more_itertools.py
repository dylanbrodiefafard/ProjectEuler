def exactly_n(iterable, n: int):
    assert n >= 0
    count = 0
    for _ in iterable:
        count += 1
        if count > n:
            return False
    return count == n
