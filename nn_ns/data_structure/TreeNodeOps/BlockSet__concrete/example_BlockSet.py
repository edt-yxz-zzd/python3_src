
r'''
>>> from ..OtherOps.TotalOrderingOps import python_total_key_ops
>>> from .BlockSet import BlockSet
>>> This = BlockSet

>>> from ..BlockDictOps__concrete.theUInt_as_BlockDictKeyOps import theUInt_as_BlockDictKeyOps
>>> UIntBlockSet = lambda *args, **kwargs: This(theUInt_as_BlockDictKeyOps, *args, **kwargs)
>>> block_dict_key_ops = theUInt_as_BlockDictKeyOps
>>> block_key2uint_pair = lambda bk: (bk[0][1], bk[1][1])
>>> ls = lambda s: [*s.iter_block_keys()]
>>> show = lambda s: [*map(block_key2uint_pair, s.iter_block_keys())]

>>> the0 = block_dict_key_ops.mkTheKey(0)
>>> the1 = block_dict_key_ops.mkTheKey(1)
>>> the2 = block_dict_key_ops.mkTheKey(2)
>>> the3 = block_dict_key_ops.mkTheKey(3)
>>> the4 = block_dict_key_ops.mkTheKey(4)
>>> the5 = block_dict_key_ops.mkTheKey(5)
>>> the6 = block_dict_key_ops.mkTheKey(6)
>>> the7 = block_dict_key_ops.mkTheKey(7)
>>> the8 = block_dict_key_ops.mkTheKey(8)


>>> empty = UIntBlockSet()
>>> s = UIntBlockSet([1, 3, 4, 5, 0, 7])
>>> p = UIntBlockSet([1, 4, 5, 0])
>>> q = UIntBlockSet([1, 3, 7])

>>> s.block_dict_key_ops is s.get_block_dict_key_ops()
True
>>> s.block_key2block_keys((the1, the3)) == [(the1, the1), (the3, the3)]
True
>>> s.block_key2block_keys((the1, the3), reverse=True) == [(the3, the3), (the1, the1)]
True

>>> empty.block_key2block_keys((the1, the5))
[]

__bool__
>>> s.get_num_block_keys()
3
>>> bool(s)
True
>>> empty.get_num_block_keys()
0
>>> bool(empty)
False


>>> empty # doctest: +ELLIPSIS
BlockSet(<...>)
>>> s # doctest: +ELLIPSIS
BlockSet(<...>, [((<KeyExCase.TheKey: 2>, 0), (<KeyExCase.TheKey: 2>, 1)), ((<KeyExCase.TheKey: 2>, 3), (<KeyExCase.TheKey: 2>, 5)), ((<KeyExCase.TheKey: 2>, 7), (<KeyExCase.TheKey: 2>, 7))], is_block_keys = True)


__contains__
>>> 3 in empty
False
>>> 3 in s
True
>>> 2 in s
False

__eq__
>>> empty == empty
True
>>> empty == s
False
>>> s == s.copy()
True
>>> s != s
False


__ge__
__gt__
__le__
__lt__
>>> empty < s
True
>>> s < s
False
>>> s <= s
True
>>> s >= p >= empty < p < s > q > empty <= q <= s
True
>>> empty <= p <= s >= q >= empty
True
>>> empty <= p <= s
True
>>> empty < q < s
True
>>> empty <= q <= s
True
>>> q <= p or p <= q or q < p or p < q
False
>>> empty >= p or empty > p or p <= empty or p < empty
False

>>> q >= s or q > s or s <= q or s < q
False



__and__
__iand__
>>> empty & q == empty
True
>>> q & s == q and p == s & p
True
>>> show(q & p)
[(1, 1)]
>>> t = s.copy()
>>> t &= q
>>> t == q
True


__or__
__ior__
>>> p|s == s == s|q == p|q == s|empty
True
>>> t = q.copy()
>>> t |= empty
>>> t == q
True
>>> t |= s
>>> t == s
True


__sub__
__isub__
>>> p - empty == p
True
>>> p - s == empty == q - q
True
>>> show(p - q)
[(0, 0), (4, 5)]
>>> show(q - p)
[(3, 3), (7, 7)]
>>> t = s.copy()
>>> t -= q
>>> t == s - q
True
>>> show(t)
[(0, 0), (4, 5)]


__xor__
__ixor__
>>> empty ^ p == p == s ^ q ^ q ^ s ^ p
True
>>> p ^ q == q ^ p
True
>>> show(p ^ q)
[(0, 0), (3, 5), (7, 7)]
>>> show(s ^ q)
[(0, 0), (4, 5)]
>>> show(s ^ p)
[(3, 3), (7, 7)]
>>> t = s.copy()
>>> t ^= q
>>> t == (q ^ s)
True




add
add_block_key
add_dict_key
>>> t = s.copy()
>>> t.add(1)
>>> t == s
True
>>> t.add(6)
>>> t > s
True
>>> show(t)
[(0, 1), (3, 7)]





block_dict_key_ops
>>> s.block_dict_key_ops is block_dict_key_ops
True

assign
>>> t = s.copy()
>>> t.assign(q)
>>> s != t == q
True
>>> t.assign(empty)
>>> q != t == empty
True



block_key2block_keys
block_key2iter_block_keys
>>> s.block_key2block_keys((the4, the7)) == [(the4, the5), (the7, the7)]
True
>>> s.block_key2block_keys((the4, the7), reverse=True) == [(the7, the7), (the4, the5)]
True
>>> s.block_key2block_keys((the2, the4)) == [*s.block_key2iter_block_keys((the2, the4))]
True
>>> s.block_key2block_keys((the2, the4), reverse=True) == [*s.block_key2iter_block_keys((the2, the4), reverse=True)]
True



clear
>>> t = s.copy()
>>> t.clear()
>>> not t
True


copy
>>> t = s.copy()
>>> t == s
True

del_dict_key
>>> t = s.copy()
>>> t.del_dict_key(1)
>>> t.del_dict_key(4)
>>> show(t)
[(0, 0), (3, 3), (5, 5), (7, 7)]
>>> t.del_dict_key(4)
Traceback (most recent call last):
    ...
KeyError: 4


dict_key2block_keys
>>> s.dict_key2block_keys(2)
[]
>>> s.dict_key2block_keys(1) == [(the1, the1)]
True


discard
>>> t = s.copy()
>>> t.discard(2)
>>> t.discard(10)
>>> t == s
True
>>> t.discard(7)
>>> t.discard(0)
>>> show(t)
[(1, 1), (3, 5)]

discard_block_key
>>> t = s.copy()
>>> t.discard_block_key((the4, the6))
>>> show(t)
[(0, 1), (3, 3), (7, 7)]
>>> t.discard_block_key((the1, the3))
>>> show(t)
[(0, 0), (7, 7)]

discard_dict_key
>>> t = s.copy()
>>> t.discard_dict_key(2)
>>> t.discard_dict_key(20)
>>> t == s
True
>>> t.discard_dict_key(3)
>>> t.discard_dict_key(4)
>>> t.discard_dict_key(0)
>>> show(t)
[(1, 1), (5, 5), (7, 7)]


pop_block_key
>>> t = s.copy()
>>> t.pop_block_key() == (the7, the7)
True
>>> t.pop_block_key() == (the3, the5)
True
>>> t.pop_block_key() == (the0, the1)
True
>>> not t
True

pop_block_key_of_dict_key
>>> t = s.copy()
>>> t.pop_block_key_of_dict_key(2)
Traceback (most recent call last):
    ...
KeyError: 2
>>> t == s
True
>>> t.pop_block_key_of_dict_key(4) == (the4, the4)
True
>>> t.get_num_block_keys()
4
>>> t.pop_block_key_of_dict_key(1) == (the1, the1)
True
>>> t.get_num_block_keys()
4
>>> show(t)
[(0, 0), (3, 3), (5, 5), (7, 7)]

pop_block_keys_of_block_key
>>> t = s.copy()
>>> t.pop_block_keys_of_block_key((the4, the7)) == [(the4, the5), (the7, the7)]
True
>>> t.get_num_block_keys()
2
>>> t.pop_block_keys_of_block_key((the0, the7)) == [(the0, the1), (the3, the3)]
True

pop_block_keys_of_dict_key
>>> t = s.copy()
>>> t.pop_block_keys_of_dict_key(2)
[]
>>> t == s
True
>>> t.pop_block_keys_of_dict_key(4) == [(the4, the4)]
True
>>> t.get_num_block_keys()
4
>>> t.pop_block_keys_of_dict_key(1) == [(the1, the1)]
True
>>> t.get_num_block_keys()
4
>>> show(t)
[(0, 0), (3, 3), (5, 5), (7, 7)]


pop_left_block_key
>>> t = s.copy()
>>> t.pop_left_block_key() == (the0, the1)
True
>>> t.pop_left_block_key() == (the3, the5)
True
>>> t.pop_left_block_key() == (the7, the7)
True
>>> t == empty
True

pop_left_or_right_block_key
>>> t = s.copy()
>>> t.pop_left_or_right_block_key(False) == (the0, the1)
True
>>> t.pop_left_or_right_block_key(True) == (the7, the7)
True
>>> show(t)
[(3, 5)]

pop_right_block_key
>>> t = s.copy()
>>> t.pop_right_block_key() == (the7, the7)
True
>>> t.pop_right_block_key() == (the3, the5)
True
>>> t.pop_right_block_key() == (the0, the1)
True
>>> not t
True


remove
>>> t = s.copy()
>>> t.remove(8)
Traceback (most recent call last):
    ...
KeyError: 8
>>> t == s
True
>>> t.remove(1)
>>> 0 in t
True
>>> t.remove(0)
>>> 0 in t
False
>>> show(t)
[(3, 5), (7, 7)]


swap
>>> t = s.copy()
>>> p_ = p.copy()
>>> q_ = q.copy()
>>> p_.swap(q_)
>>> p_ == q and q_ == p
True


update
>>> t = q.copy()
>>> t.update(empty)
>>> t == q
True
>>> t.update(q)
>>> t == q
True
>>> t.update(p)
>>> t == s
True
>>> t.update([2, 6])
>>> show(t)
[(0, 7)]


update_from_block_keys
>>> t = q.copy()
>>> t.update_from_block_keys([(the4, the5), (the2, the3)])
>>> show(t)
[(1, 5), (7, 7)]

update_from_dict_keys
>>> t = s.copy()
>>> t.update_from_dict_keys([1,2,3,6, 10])
>>> show(t)
[(0, 7), (10, 10)]




get_block_dict_key_ops
>>> s.get_block_dict_key_ops() is block_dict_key_ops
True


get_num_block_keys
>>> s.get_num_block_keys()
3
>>> p.get_num_block_keys()
2
>>> q.get_num_block_keys()
3


>>> s.get_total_dict_key_ops() is block_dict_key_ops.total_key_ops
True
>>> s.get_total_dict_key_ops() is s.total_dict_key_ops
True


is_exactly_block_key
>>> s.is_exactly_block_key((the3, the5))
True
>>> s.is_exactly_block_key((the3, the4))
False
>>> s.is_exactly_block_key((the3, the6))
False
>>> s.is_exactly_block_key((the1, the1))
False
>>> s.is_exactly_block_key((the7, the7))
True

is_one_piece_block_key
>>> s.is_one_piece_block_key((the3, the5))
True
>>> s.is_one_piece_block_key((the3, the4))
True
>>> s.is_one_piece_block_key((the3, the6))
False
>>> s.is_one_piece_block_key((the1, the1))
True
>>> s.is_one_piece_block_key((the7, the7))
True


isdisjoint
>>> empty.isdisjoint(p)
True
>>> s.isdisjoint(empty)
True
>>> q.isdisjoint(p)
False
>>> q.isdisjoint(s-q)
True


self_make_block_set_from_block_keys
self_make_block_set_from_dict_keys
self_make_block_set_from_iterable
self_make_empty_block_set
>>> s.self_make_empty_block_set() == empty
True
>>> show(s.self_make_block_set_from_dict_keys([0,3,2,1,5]))
[(0, 3), (5, 5)]
>>> show(s.self_make_block_set_from_iterable([0,3,2,1,5], False))
[(0, 3), (5, 5)]
>>> show(s.self_make_block_set_from_iterable(s.iter_block_keys(), is_block_keys=True))
[(0, 1), (3, 5), (7, 7)]
>>> s.self_make_block_set_from_block_keys(p.iter_block_keys()) == p
True



>>> s == UIntBlockSet([1, 3, 4, 5, 0, 7])
True
>>> s.index_block_key_at(0) == (the0, the1)
True
>>> s.index_block_key_at(1) == (the3, the5)
True
>>> s.index_block_key_at(2) == (the7, the7)
True
>>> s.index_block_key_at(3)
Traceback (most recent call last):
    ...
IndexError
>>> s.index_block_key_at(2) == s.index_block_key_at(-1)
True
>>> s.index_block_key_at(1) == s.index_block_key_at(-2)
True
>>> s.index_block_key_at(0) == s.index_block_key_at(-3)
True
>>> s.index_block_key_at(-4)
Traceback (most recent call last):
    ...
IndexError



>>> s.get_first_block_key() == s.index_block_key_at(0)
True
>>> s.get_first_block_key() == s.get_first_or_last_block_key(False)
True
>>> s.get_last_block_key() == s.index_block_key_at(-1)
True
>>> s.get_last_block_key() == s.get_first_or_last_block_key(True)
True


>>> empty.get_first_or_last_block_key(True)
Traceback (most recent call last):
    ...
IndexError
>>> empty.get_first_or_last_block_key(False)
Traceback (most recent call last):
    ...
IndexError
>>> empty.get_first_block_key()
Traceback (most recent call last):
    ...
IndexError
>>> empty.get_last_block_key()
Traceback (most recent call last):
    ...
IndexError



>>> whole = s.self_make_whole_block_set()
>>> whole.get_num_block_keys()
1
>>> whole == empty.self_make_whole_block_set()
True
>>> the_inf = block_dict_key_ops.getTheMaxKeyEx()
>>> ls(whole) == [(the0, the_inf)]
True
>>> whole == empty.self_make_whole_block_set()
True


>>> whole == empty.self_make_complement_block_set()
True
>>> -s == whole - s == s.self_make_complement_block_set()
True

>>> s == UIntBlockSet([1, 3, 4, 5, 0, 7])
True
>>> ls(-s) == [(the2, the2), (the6, the6), (the8, the_inf)]
True


>>> empty.is_empty()
True
>>> whole.is_empty()
False
>>> s.is_empty()
False

>>> empty.is_whole_set()
False
>>> whole.is_whole_set()
True
>>> s.is_whole_set()
False


############ before
>>> s == UIntBlockSet([1, 3, 4, 5, 0, 7])
True
>>> p == UIntBlockSet([1, 4, 5, 0])
True
>>> q == UIntBlockSet([1, 3, 7])
True

>>> empty.before__le(whole)
True
>>> empty.before__lt(whole)
True
>>> empty.before__le(empty)
True
>>> empty.before__lt(empty)
False
>>> s.before__lt(p)
True
>>> s.before__le(s.copy())
True
>>> s.before__lt(s.copy())
False

# empty ~<~ s ~<~ p ~<~ whole ~<~ q
>>> empty.before__lt(s)
True
>>> s.before__lt(p)
True
>>> p.before__lt(whole)
True
>>> whole.before__lt(q)
True

>>> empty.before__lt(empty.copy())
False
>>> s.before__lt(s.copy())
False
>>> p.before__lt(p.copy())
False
>>> whole.before__lt(whole.copy())
False
>>> q.before__lt(q.copy())
False

>>> whole.before__le(s)
False
>>> q.before__le(p)
False
>>> whole.before__lt(s)
False
>>> q.before__lt(p)
False

>>> p.block_set_cmp(p.copy())
0
>>> p.block_set_cmp(q)
-1
>>> p.block_set_cmp(s)
1
>>> p.before(p.copy(), False)
True
>>> p.before(p.copy(), True)
False
>>> p.before(q, False)
True
>>> p.before(q, True)
True
>>> p.before(s, False)
False
>>> p.before(s, True)
False

>>> p.after(q, False)
False
>>> p.after(q, True)
False
>>> p.after(s, False)
True
>>> p.after(s, True)
True
>>> p.after(p.copy(), False)
True
>>> p.after(p.copy(), True)
False
>>> p.after__ge(p.copy())
True
>>> p.after__gt(p.copy())
False
>>> p.after__ge(s)
True
>>> p.after__gt(q)
False



to test:
    issubset
    issuperset
    iter_all_touch_or_overlap_block_keys
    iter_block_keys
    list_all_touch_or_overlap_block_keys
    make_empty_block_set
    mkSingletonRange
    total_dict_key_ops



new_methods:
        __slots__
        __init__
        _get_block_dict_key_ops_
        copy
        get_num_block_keys
        iter_block_keys
        self_make_block_set_from_block_keys
        self_make_block_set_from_dict_keys
        self_make_empty_block_set
        make_empty_block_set
        iter_all_touch_or_overlap_block_keys
        add_block_key
        pop_block_keys_of_block_key
        discard_block_key
        pop_left_or_right_block_key
        clear
        swap
'''

if __name__ == "__main__":
    import doctest
    doctest.testmod()

