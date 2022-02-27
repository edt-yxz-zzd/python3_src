r'''
py -m seed.types.RopeOps
from seed.types.RopeOps import RopeOps

e ../../python3_src/seed/types/RopeOps.py


conceptual:
    rope = (seq_tail, may rope)
    where
        seq is immutable seq, may be subclass of tuple

#'''

__all__ = '''
    RopeOps
    '''.split()

import itertools #chain
from seed.tiny import check_type_is, check_uint
from seed.tiny import MapView
from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttr#, DictKeyAsObjAttrAndAsMapping

r'''[[[[[
import itertools #chain
from seed.tiny.import check_type_is, check_uint
class RopeOps:
    'Rope = (size, num_skips, seq, may Rope)'
    empty_rope = (0, 0, (), None)
    def len(rope, /):
        return rope[0]
    def to_tuple(rope, /):
        it = RopeOps.iter(rope)
        return tuple(it)
    def iter(rope, /):
        check_type_is(tuple, rope)
        n = RopeOps.len(rope)
        while not rope is None:
            #(size, num_skips, seq, may_rope) = rope
            (size, num_skips, seq, rope) = rope
            assert n==size
            ls = seq[num_skips:]
            yield from ls
            n -= len(ls)
        if not n==0: raise logic-err
        return#

    def mk(num_skips, seq, may_rope, /):
        if may_rope is None:
            r = RopeOps.mk1(num_skips, seq)
        else:
            rope = may_rope
            r = RopeOps.mk2(num_skips, seq, may_rope)
        return r
    def mk1(num_skips, seq, /):
        check_uint(num_skips)
        size = len(seq) - num_skips
        check_uint(size)
        if not size:
            return RopeOps.empty_rope
        return (size, num_skips, seq, None)
    def mk2(num_skips, seq, rope, /):
        h_rope = RopeOps.mk1(num_skips, seq)
            # check and get size
        check_type_is(tuple, rope)
        if not len(rope)==4: raise TypeError

        sz0 = h_rope[0] #RopeOps.len
        if sz0 == 0:
            return rope

        sz1 = rope[0] #RopeOps.len
        if sz1 == 0:
            return h_rope

        size = sz0 + sz1
        return (size, num_skips, seq, rope)
    def split_at(n, rope, /):
        '-> (initial_seq, tail_rope)'
        check_uint(n)
        check_type_is(tuple, rope)
        if n == 0:
            return (), rope

        size = rope[0]
        if not 0 <= n <= size: raise ValueError
        N = n
        L = size
        lss = []
        while n > 0:
            (size, num_skips, seq, rope) = rope
            end = num_skips+n
            ls = seq[num_skips:end]
            lss.append(ls)
            n -= len(ls)
        if not n == 0: raise logic-err
        #bug:tail_rope = RopeOps.mk(num_skips+n, seq, rope)
        tail_rope = RopeOps.mk(end, seq, rope)
        it = itertools.chain.from_iterable(lss)
        initial_seq = (*it,)
        assert len(initial_seq) == N
        assert L == N + tail_rope[0]
        return initial_seq, tail_rope

#]]]]]'''

def ___tmp_env():
    __doc__ = 'Rope = (size, num_skips, seq, may Rope)'
    import itertools #chain
    from seed.tiny import check_type_is, check_uint
    from seed.tiny import MapView
    empty_rope = (0, 0, (), None)
    def _len_(rope, /):
        return rope[0]
    def to_tuple(rope, /):
        it = _iter_(rope)
        return tuple(it)
    def _iter_(rope, /):
        check_type_is(tuple, rope)
        n = _len_(rope)
        while not rope is None:
            #(size, num_skips, seq, may_rope) = rope
            (size, num_skips, seq, rope) = rope
            assert n==size
            ls = seq[num_skips:]
            yield from ls
            n -= len(ls)
        if not n==0: raise logic-err
        return#

    def mk(num_skips, seq, may_rope, /):
        if may_rope is None:
            r = mk1(num_skips, seq)
        else:
            rope = may_rope
            r = mk2(num_skips, seq, may_rope)
        return r
    def mk1(num_skips, seq, /):
        check_uint(num_skips)
        size = len(seq) - num_skips
        check_uint(size)
        if not size:
            return empty_rope
        return (size, num_skips, seq, None)
    def mk2(num_skips, seq, rope, /):
        h_rope = mk1(num_skips, seq)
            # check and get size
        check_type_is(tuple, rope)
        if not len(rope)==4: raise TypeError

        sz0 = h_rope[0] #RopeOps._len_
        if sz0 == 0:
            return rope

        sz1 = rope[0] #RopeOps._len_
        if sz1 == 0:
            return h_rope

        size = sz0 + sz1
        return (size, num_skips, seq, rope)
    def split_at(n, rope, /):
        '-> (initial_seq, tail_rope)'
        check_uint(n)
        check_type_is(tuple, rope)
        if n == 0:
            return (), rope

        size = rope[0]
        if not 0 <= n <= size: raise ValueError
        N = n
        L = size
        lss = []
        while n > 0:
            (size, num_skips, seq, rope) = rope
            end = num_skips+n
            ls = seq[num_skips:end]
            lss.append(ls)
            n -= len(ls)
        if not n == 0: raise logic-err
        #bug:tail_rope = RopeOps.mk(num_skips+n, seq, rope)
        tail_rope = mk(end, seq, rope)
        it = itertools.chain.from_iterable(lss)
        initial_seq = (*it,)
        assert len(initial_seq) == N
        assert L == N + tail_rope[0]
        return initial_seq, tail_rope

#]
    return (empty_rope, _len_, _iter_, to_tuple, mk, mk1, mk2, split_at)
    return (__doc__, empty_rope, _len_, _iter_, to_tuple, mk, mk1, mk2, split_at)
    return {**locals()}
#_d  = MapView(___tmp_env())
#RopeOps = DictKeyAsObjAttr(MapView(dict(zip('__doc__ empty_rope len iter to_tuple mk mk1 mk2 split_at'.split(), ___tmp_env())))); del ___tmp_env
RopeOps = DictKeyAsObjAttr(MapView(dict(zip('empty_rope len iter to_tuple mk mk1 mk2 split_at'.split(), ___tmp_env())))); del ___tmp_env
#print(dir(RopeOps))
#assert dir(RopeOps) == ['__doc__', 'empty_rope', 'iter', 'len', 'mk', 'mk1', 'mk2', 'split_at', 'to_tuple']
assert dir(RopeOps) == ['empty_rope', 'iter', 'len', 'mk', 'mk1', 'mk2', 'split_at', 'to_tuple']
#help(RopeOps)

def _t():
    ops = RopeOps
    assert 0 == ops.len(ops.empty_rope)
    assert [] == [*ops.iter(ops.empty_rope)]
    assert () == ops.to_tuple(ops.empty_rope)
    ts = (1, 2, 3)
    rope1 = ops.mk(2, ts, None)
    rope2 = ops.mk(1, ts, rope1)
    rope3 = ops.mk(0, ts, rope2)
    rope4 = ops.mk(3, ts, rope3)
    assert rope4 is rope3
    assert rope3 == (6, 0, ts, rope2)
    assert rope2 == (3, 1, ts, rope1)
    assert rope1 == (1, 2, ts, None)
    assert rope1 == ops.mk2(2, ts, ops.empty_rope)
    assert rope1 == ops.mk1(2, ts)
    assert ops.to_tuple(rope1) == (3,)
    assert ops.to_tuple(rope2) == (2, 3, 3)
    assert ops.to_tuple(rope3) == (1, 2, 3, 2, 3, 3)
    assert ops.len(rope3) == 6
    rs = ops.empty_rope, rope1, rope2, rope3
    for rope in rs:
        for i in range(1+ops.len(rope)):
            ls = ops.to_tuple(rope)
            hs_, _ts = ops.split_at(i, rope)
            assert hs_ == ls[:i]
            assert ops.to_tuple(_ts) == ls[i:]
_t()
from seed.types.RopeOps import RopeOps

