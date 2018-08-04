
'''
sort huge uint
    sort bit length first
    for each len:
        encode to bytes
        same bit length ==>> same byte length ==>> radix sort

'''

__all__ = '''
    sparse_big_uints2iter_groups
    sparse_big_ints2iter_groups
    '''.split()
from seed.int_tools.uint2iter_bits import (
    uint2iter_bits
    ,uint2bytes

    ,uint2bit_length
    ,uint2byte_length
    )


from seed.tiny import echo, fst, snd
from itertools import chain
from .classify import classify
from seed.math.floor_ceil import ceil_div

class Tmp:
    def __init__(self, key, obj):
        self.obj = obj
        self.u = u = key(obj)
        self.bit_length = uint2bit_length(u)
        self.bits = None # iterator
        self.remain_u = None

        self.offseted_bit_length = None # -= min bit_length


    def get_offseted_bit_length(self):
        return self.offseted_bit_length
    def get_bit_length(self):
        return self.bit_length
    def get_uint(self):
        return self.u
    def get_remain_uint(self):
        return self.remain_u
    pass
echo

def tmps2objs(tmps):
    # Iter Tmp -> [Obj]
    return list(t.obj for t in tmps)

def group_at_most_2(sized_container, *, key, reverse, with_key):
    # (a->Int) -> [a]{..2} -> [[a]]
    # len(objs) <= 2
    objs = sized_container
    L = len(objs)
    if L < 2:
        if L == 0:
            return []
        return [list(objs)]

    #ls = sorted([(key(a), a), (key(b),b)], key=fst, reverse=reverse)
    a, b = objs
    ka, kb = key(a), key(b)
    cmp = ka-kb
    #bug:if a == b:
    if not cmp:
        return [(ka, [a,b])] if with_key else [[a,b]]

    ra, rb = [a], [b]
    if with_key:
        ra = ka, ra
        rb = kb, rb

    #bug:if a < b:
    #if bool(ka < kb) == (not reverse):
    if bool(cmp < 0) != bool(reverse):
        return [ra, rb]
    return [rb, ra]

def sparse_big_ints2iter_groups(sized_container
        , *, key=None, with_key=False, reverse=False
        , __base_case_bit_length_hint=None):
    ''':: [a] -> (a->Int) -> (Iter [a] | Iter (Int, [a]))

see: sparse_big_uints2iter_groups
example:
    >>> this_ = sparse_big_ints2iter_groups
    >>> this = lambda *args, **kwargs: this_(*args, __base_case_bit_length_hint=-1, **kwargs)
    >>> list_this = lambda *args, **kwargs: list(this(*args, **kwargs))
    >>> list_this([-111111111, -3223423, -111111111, 3223423, -1, 334535, -111111112, -111111114, -111111102, -111111104, 353454, 334536, 334534])
    [[-111111114], [-111111112], [-111111111, -111111111], [-111111104], [-111111102], [-3223423], [-1], [334534], [334535], [334536], [353454], [3223423]]
    >>> list_this([-111111112, -111111114, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
    [[-111111114], [-111111112], [0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
'''
    if key is None:
        key = echo
    old_key = key; del key
    pairs = ((old_key(obj), obj) for obj in sized_container)
    new_key = fst

    negs, poss = classify(2, pairs, lambda x: bool(0 <= new_key(x)))
    del new_key

    neg_key = lambda pair: -fst(pair)
    pos_key = fst
    it1 = sparse_big_uints2iter_groups(negs
            , key=neg_key, reverse=not reverse, with_key=False
            , __base_case_bit_length_hint=__base_case_bit_length_hint)
    it2 = sparse_big_uints2iter_groups(poss
            , key=pos_key, reverse=reverse, with_key=False
            , __base_case_bit_length_hint=__base_case_bit_length_hint)

    # pairs is not empty
    pairs2objs = _pairs2snds
    pairs2keyed = _nonempty_pairs2keyed_group
    f = pairs2keyed if with_key else pairs2objs
    return map(f, chain(it1, it2))
_pairs2snds = lambda pairs: [*map(snd, pairs)]
def _nonempty_pairs2keyed_group(g):
    # assert g
    return (fst(g[0]), _pairs2snds(g))

def sparse_big_uints2iter_groups(sized_container
        , *, key=None, with_key=False, reverse=False
        , __base_case_bit_length_hint = None):
    ''':: [a] -> (a->UInt) -> (Iter [a] | Iter (UInt, [a]))

example:
    >>> this_ = sparse_big_uints2iter_groups
    >>> this = lambda *args, **kwargs: this_(*args, __base_case_bit_length_hint=-1, **kwargs)
    >>> list_this = lambda *args, **kwargs: list(this(*args, **kwargs))
    >>> list_this([[], ()], key=len, reverse=True, with_key=True)
    [(0, [[], ()])]
    >>> list_this([])
    []
    >>> list_this([1])
    [[1]]
    >>> list_this([1,2])
    [[1], [2]]
    >>> list_this([2,1])
    [[1], [2]]
    >>> list_this([10000000])
    [[10000000]]
    >>> list_this([10000000, 2000000, 2000001, 2000000, 2000002, 2000004, 2000004, 2000005])
    [[2000000, 2000000], [2000001], [2000002], [2000004, 2000004], [2000005], [10000000]]
    >>> list_this([0]*4)
    [[0, 0, 0, 0]]
    >>> list_this([1]*4)
    [[1, 1, 1, 1]]
    >>> list_this([2]*4)
    [[2, 2, 2, 2]]

    >>> list_this([0,0,0], with_key=True)
    [(0, [0, 0, 0])]
    >>> list_this([0,1,1,2,3,4], with_key=True)
    [(0, [0]), (1, [1, 1]), (2, [2]), (3, [3]), (4, [4])]
    >>> list_this([0,1,1,2,3,4], with_key=True, reverse=True)
    [(4, [4]), (3, [3]), (2, [2]), (1, [1, 1]), (0, [0])]

    >>> list_this([0,1,1,2,3,4], key=lambda i: i+1000, with_key=True)
    [(1000, [0]), (1001, [1, 1]), (1002, [2]), (1003, [3]), (1004, [4])]
    >>> list_this([0,1,1,2,3,4], key=lambda i: i+1000, with_key=True, reverse=True)
    [(1004, [4]), (1003, [3]), (1002, [2]), (1001, [1, 1]), (1000, [0])]

'''
    with_key = bool(with_key)
    reverse = bool(reverse)
    if key is None:
        key = echo
    objs = sized_container
    L = len(objs)
    if L <= 2:
        yield from group_at_most_2(objs
                , key=key, reverse=reverse, with_key=with_key)
        return

    if with_key:
        def tmps2may_keyed_objs(tmps):
            return (tmps[0].u, tmps2objs(tmps))
    else:
        tmps2may_keyed_objs = tmps2objs
    del with_key


    tmps = [Tmp(key, obj) for obj in objs]

    # L >= 3
    # DONOT eval(max(uints)) # since assume they are big
    #       but max(bit_lengths) is ok
    #
    #       input_uint = 2^(2^64*2^3)
    #       input_uint.bit_length = 2^67
    #       input_uint.bit_length.bit_length = 67
    #       input_uint.bit_length.bit_length.bit_length = 7
    #       input_uint.bit_length.bit_length.bit_length.bit_length = 3
    #       recur depth may be 4
    #max_bit_length = max(t.bit_length for t in tmps)
        # 0.bit_length = 0
        # 1.bit_length = 1
        # 2.bit_length = 2
        # 3.bit_length = 2
        # 4.bit_length = 3
    min_bit_length = min(t.bit_length for t in tmps)
    for t in tmps:
        t.offseted_bit_length = t.bit_length - min_bit_length
    max_offseted_bit_length = max(t.offseted_bit_length for t in tmps)

    # tmpss = group by bit_length
    #if max_bit_length > 3:
    #if max_bit_length > min(1024, max(3, L)):
    #if max_bit_length > (3 if TESTING else max(3, min(1024, L))):
    assert L >= 3
    if __base_case_bit_length_hint is None:
        __base_case_bit_length_hint = 1024
    #if max_offseted_bit_length > min(max(3, __base_case_bit_length_hint), L):
    if max_offseted_bit_length > max(3, min(__base_case_bit_length_hint, L)):
        # recur this
        tmpss = sparse_big_uints2iter_groups(tmps
                , key=Tmp.get_bit_length, reverse=reverse, with_key=False)
    else:
    #elif max_bit_length <= 3:
    #elif max_offseted_bit_length <= 3:
        assert max_offseted_bit_length <= L
        #if max_bit_length == 0:
        if max_offseted_bit_length == 0 and min_bit_length <= 1:
            # max_bit_length == min_bit_length == (0 | 1)
            # all keys are 0
            # or all keys are 1

            #bug: yield tmps2objs(tmps)
            #   should consider with_key
            yield tmps2may_keyed_objs(tmps)
            return
        tmpss = _ibucket_group(max_offseted_bit_length+1, tmps
                , key=Tmp.get_offseted_bit_length
                , reverse=reverse)

    for tmps in tmpss:
        assert tmps
        # all uints have same bit_length
        it = map(tmps2may_keyed_objs, _igroup_tmps_by_bits(tmps, reverse=reverse))
            # group_uints_by_bits(tmps))
        yield from it
    return
def _ibucket_group(alphabet_size, objs
        , *, key, reverse=False):
    #:: upper_bound -> Iter a -> (a->UInt) -> Iter [a]
    if len(objs) <= 1 or alphabet_size <= 1:
        return filter(None, [objs])
    table = [[] for _ in range(alphabet_size)]
    for x in objs:
        k = key(x)
        table[k].append(x)
    f = reversed if reverse else echo
    return filter(None, f(table))

def _igroup_tmps_by_bits(tmps, *, reverse):
    #:: [Tmp] -> Iter [Tmp]
    # all have same bit_length
    assert tmps

    reverse = bool(reverse)
    if len(tmps) <= 2:
        # to avoid eval bits
        yield from group_at_most_2(tmps
                    , key=Tmp.get_uint, reverse=reverse, with_key=False)
        return

    bit_length = tmps[0].bit_length
    if bit_length <= 1:
        # 0.bit_length = 0
        # 1.bit_length = 1
        # 2.bit_length = 2
        yield tmps
        return

    if reverse:
        not_ = lambda bit: not bit
        def f(bits):
            return map(not_, bits)
    else:
        f = echo
    try:
        for tmp in tmps:
            assert tmp.bit_length == bit_length
            assert tmp.bits is None
            tmp.bits = it = f(uint2iter_bits(True, tmp.u)) # big-endian
            next(it) # drop the heading 1
    except StopIteration:
        raise logic-error
    del f, it, tmp #, reverse


    stack = [(bit_length-1, tmps)]
    try:
        while stack:
            remain_bit_length, tmps = stack.pop()
            assert remain_bit_length > 0
            assert tmps

            if len(tmps) <= 2:
                #bug:yield from group_at_most_2(tmps
                #       , key=Tmp.get_uint, reverse=False, with_key=False)
                # 1) spend more time: should cmp the remain bits
                # 2) reverse = reverse nor False
                #
                yield from _group_at_most_2__via_remain_bytes(
                            remain_bit_length, tmps, reverse=reverse)
                continue
                yield from _group_at_most_2__via_remain_bits(tmps)
                continue

            table = zeros, ones = [], []
            for tmp in tmps:
                MSB = next(tmp.bits) # should not raise
                table[MSB].append(tmp)

            remain_bit_length -= 1
            if remain_bit_length == 0:
                yield from filter(None, table)
                continue
            stack.extend((remain_bit_length, tmps)
                            for tmps in reversed(table) if tmps)
    except StopIteration:
        raise logic-error
    return

def _group_at_most_2__via_remain_bytes(remain_bit_length, tmps, *, reverse):
    # remain_bytes -> [Tmp]{1..2} -> [[Tmp]]
    # since cmp uint directly, need "reverse"
    #
    # has same remain bits
    # assert tmps
    if len(tmps) == 1:
        return [tmps]
    a, b = tmps
    remain_bytes = ceil_div(remain_bit_length, 8)
    for t in tmps:
        bs = uint2bytes(True, t.u, length=remain_bytes) # big-endian
        t.remain_u = int.from_bytes(bs, 'big')
    return group_at_most_2(tmps
                , key=Tmp.get_remain_uint, reverse=reverse, with_key=False)
ceil_div
def _group_at_most_2__via_remain_bits(tmps):
    # [Tmp]{1..2} -> [[Tmp]]
    # since cmp flipped bits , need not "reverse"
    #
    # has same remain bits
    # assert tmps
    if len(tmps) == 1:
        return [tmps]
    a, b = tmps
    for lhs, rhs in zip(a.bits, b.bits):
        if lhs != rhs:
            if lhs < rhs:
                return [[a], [b]]
            return [[b], [a]]
    return [tmps]




TESTING = False

if __name__ == "__main__":
    TESTING = True
    ls = [(-111111111, -111111111), (-3223423, -3223423), (-111111111, -111111111), (-1, -1), (-111111112, -111111112), (-111111114, -111111114), (-111111102, -111111102), (-111111104, -111111104)]
    ls = _pairs2snds(ls)
    ls = [-x for x in ls]
    [*r] = sparse_big_uints2iter_groups(ls, reverse=True)

    r = sparse_big_ints2iter_groups([-111111111, -3223423, -111111111, 3223423, -1, 334535, -111111112, -111111114, -111111102, -111111104, 353454, 334536, 334534])
    import doctest
    doctest.testmod()



