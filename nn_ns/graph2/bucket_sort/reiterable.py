
__all__ = '''
    is_reiterable
    make_reiterable

    is_sorted
    is_seq
    is_sorted_seq
    make_seq
    make_tuple
    '''.split()

from collections.abc import Sized, Iterable, Iterator, Sequence
def is_reiterable(obj):
    return isinstance(obj, Iterable) and not isinstance(obj, Iterator)
def make_reiterable(iterable):
    # iterable->reiterable
    if is_reiterable(iterable):
        return iterable
    return list(iterable)



def is_sorted(iterable, key=None):
    if key is not None: iterable = map(key, iterable)
    else: iterable = iter(iterable)

    for pre in iterable: break
    else: return True

    for x in iterable:
        if pre <= x:
            pre = x
            continue
        return False
    return True

def is_seq(seq):
    return isinstance(seq, Sequence)

def is_sorted_seq(seq, key=None):
    return is_seq(seq) and is_sorted(seq, key)


def make_seq(iterable):
    # iterable->seq
    if isinstance(iterable, Sequence):
        return iterable
    return tuple(iterable)
def make_tuple(iterable):
    # iterable->tuple
    if isinstance(iterable, tuple):
        return iterable
    return tuple(iterable)


