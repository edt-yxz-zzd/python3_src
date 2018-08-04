
__all__ = '''
    pointwise
    iter_accumulate
    iter_accumulate_chain
    foldl
    repeat_binary_op
    iter_repeat_binary_op
    assoc_op_with_pint
    assoc_op_with_uint
    '''.split()

from itertools import islice, chain
from .head_tail import unlist_fdefault
from .null_iter import null_iter

def pointwise(op, *vectors, container=tuple):
    if not vectors:
        r = op()
    else:
        X = vectors[0]
        L = len(X)
        assert all(L == len(X) for X in vectors)
        r = map(op, *vectors)
    return container(r)
def iter_accumulate_chain(op, *iterables):
    it = chain.from_iterable(iterables)
    return unlist_fdefault(it, null_iter, iter_accumulate, op)


def iter_accumulate(op, start, iterable):
    yield start
    for x in iterable:
        start = op(start, x)
        yield start
def foldl(op, start, iterable):
    for x in iterable:
        start = op(start, x)
    return start
def repeat_binary_op(op, start, x, L, container=tuple):
    # repeat_binary_op op start x = iter_accumulate(op, start, repeat(x))[:L]
    return container(islice(iter_repeat_binary_op(op, start, x), L))
def iter_repeat_binary_op(op, start, x):
    # iter_repeat_binary_op op start x = iter_accumulate(op, start, repeat(x))
    r = start
    while True:
        yield r
        r = op(r, x)
def assoc_op_with_pint(op, x, exp):
    # op should be associatve
    # assoc_op_with_pint op x exp = ((`op` x)^(exp-1)) x
    assert exp > 0
    return assoc_op_with_uint(op, x, x, exp-1)
def assoc_op_with_uint(op, start, x, exp):
    # op should be associatve
    # assoc_op_with_uint op start x exp = ((`op` x)^exp) start
    # assoc_op_with_uint op start x exp = start `op` x `op` x ...
    assert type(exp) is int
    assert exp >= 0
    r = start
    weight = x
    while exp:
        if exp & 1:
            r = op(r, weight)
        weight = op(weight, weight)
        exp >>= 1
    return r


