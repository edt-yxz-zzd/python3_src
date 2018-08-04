
__all__ = '''
    bucket_sort
    '''.split()
from seed.special_funcs import identity
from itertools import chain
from collections.abc import Iterable, Iterator

def __iter_bucket_sort(N, ls, *, key=None):
    'ls::[Int] is a sequence; all(0 <= i < N for i in map(key, ls))'
    if key is None:
        key = identity

    assert not isinstance(ls, Iterator)
    assert isinstance(ls, Iterable)
    assert all(0 <= i < N for i in map(key, ls))

    i2count = [[] for _ in range(N)]
    for i in ls:
        i2count[key(i)].append(i)

    return chain.from_iterable(i2count)


def bucket_sort(N, ls, *, key=None):
    return list(__iter_bucket_sort(N, ls, key=key))



