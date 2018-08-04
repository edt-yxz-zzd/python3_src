
__all__ = '''
    list_direct_product
    direct_product
    direct_product_view
    '''.split()

from seed.types.View import SeqView
from itertools import product
#from .null_iter import null_iter

def list_direct_product(fiters):
    return list(direct_product(fiters))
def direct_product(fiters):
    return map(tuple, direct_product_view(fiters))

def is_empty_fiter(fiter):
    for _ in fiter: return False
    return True
def direct_product_view(fiters):
    '''like itertools.product, but input are different

fiters :: Iter (()->Iter object)
1) fiter should be stable, i.e. f() == f(); used to test whether empty
2-1) fiters is finite
    if some fiter is infinite, then donot enumerate all direct_products
        since the result is in dictionary order
2-2) or fiters is infinite and some fiter() is empty
example:
    map(tuple, direct_product_view(ls.__iter__ for ls in lsls))
'''
    # ??empty??
    # if test_empty and any(map(is_empty_fiter, fiters)): return
    iters = []
    values = []
    fiters, iter_fiters = [], iter(fiters)
    nothing = fiters
        # "next(it, nothing)"
        # "xx is nothing"
    for fiter in iter_fiters:
        it = iter(fiter()) # new iter
        for head in it:break
        else: return # empty fiter()
        fiters.append(fiter)
        iters.append(it)
        values.append(head)


    L = len(fiters)
    output = SeqView(values)
    # few input
    if L < 2:
        yield output
        if L == 0: return
        # L == 1
        [it] = iters
        for v in it:
            values[-1] = v
            yield output
        return




    # direct product
    # len(values) == len(iters) == L: yield
    # len(values) == len(iters) < L: new iter
    # len(values) +1 == len(iters): next value
    while True:
        # len(values) == len(iters):
        if len(iters) != L:
            # len(values) == len(iters) < L: new iter
            iters.append(iter(fiters[len(iters)]())) ###### iter result
            # len(values) +1 == len(iters)
        else:
            # len(values) == len(iters) == L: yield
            yield output
            for v in iters[-1]:
                values[-1] = v
                yield output
            values.pop()
            iters.pop()
            values.pop()
            # len(values) +1 == len(iters) == L-1

        # len(values) +1 == len(iters): next value
        head = next(iters[-1], nothing)
        while head is nothing:
            iters.pop()
            # len(values) == len(iters)
            if len(iters) == 0:
                # will exit outer while
                #   head is nothing
                #   len(values) == len(iters)

                # exit of inner while
                break
            values.pop()
            # len(values) +1 == len(iters): next value
            head = next(iters[-1], nothing)

        if head is nothing:
            # exit of outer while
            # len(value) == len(iters)
            break
        # len(values) +1 == len(iters)
        values.append(head)
        # len(values) == len(iters)
    pass # end of while


def test():
    def null(): return ''
    def iter_12(): return 1,2
    def iter_34(): return 3,4

    assert list_direct_product() == [()]
    assert list_direct_product(null) == []
    assert list_direct_product(iter_12, null) == []
    assert list_direct_product(iter_12, iter_34, null) == []
    assert list_direct_product(iter_12) == [(1,), (2,)]
    assert list_direct_product(iter_12, iter_34) == [(1,3), (1,4), (2,3), (2,4]
test(); del test


