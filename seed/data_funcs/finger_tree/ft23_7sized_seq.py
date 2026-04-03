#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_seq.py

seed.data_funcs.finger_tree.ft23_7sized_seq
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.ft23_7sized_seq -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.ft23_7sized_seq:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> Seq()
Seq()
>>> Seq(range(10, 20))
Seq([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
>>> len(Seq(range(10, 20)))
10
>>> Seq(range(10, 20)) * 2
Seq([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
>>> Seq(range(10, 13)) * 5
Seq([10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12, 10, 11, 12])
>>> Seq(range(10, 20))[0]
10
>>> Seq(range(10, 20))[5]
15
>>> Seq(range(10, 20))[-5]
15
>>> Seq(range(10, 20))[-1]
19
>>> Seq(range(10, 20))[1:-1]
Seq([11, 12, 13, 14, 15, 16, 17, 18])
>>> [*iter(Seq(range(10, 13)))]
[10, 11, 12]
>>> [*reversed(Seq(range(10, 13)))]
[12, 11, 10]




>>> Seq()
Seq()
>>> Seq([11, 22, 33])
Seq([11, 22, 33])
>>> len(Seq([11, 22, 33]))
3
>>> [*iter(Seq([11, 22, 33]))]
[11, 22, 33]
>>> [*reversed(Seq([11, 22, 33]))]
[33, 22, 11]
>>> Seq([11, 22, 33]).iputs_at_(1, Seq([66, 77]))
Seq([11, 66, 77, 22, 33])
>>> Seq([11, 22, 33]).iput_at_(1, 66)
Seq([11, 66, 22, 33])
>>> Seq([11, 22, 33]).ipop_at_(1)
Seq([11, 33])
>>> Seq([11, 22, 33]).vpop_at_(1)
(22, Seq([11, 33]))
>>> Seq([11, 22, 33, 44, 55, 66]).vpop_between_ge_lt_(1, 4)
(Seq([22, 33, 44]), Seq([11, 55, 66]))
>>> Seq([11, 22, 33, 44, 55, 66]).ipop_between_ge_lt_(1, 4)
Seq([11, 55, 66])

>>> Seq([11, 22, 33, 44, 55, 66]).splits_at_()
(Seq([11, 22, 33, 44, 55, 66]),)
>>> Seq([11, 22, 33, 44, 55, 66]).splits_at_(2)
(Seq([11, 22]), Seq([33, 44, 55, 66]))
>>> Seq([11, 22, 33, 44, 55, 66]).splits_at_(2,3,5)
(Seq([11, 22]), Seq([33]), Seq([44, 55]), Seq([66]))

>>> Seq([11, 22, 33, 44, 55, 66]).split_at_(2)
(Seq([11, 22]), Seq([33, 44, 55, 66]))

__getitem__
>>> Seq([11, 22, 33, 44, 55, 66])[3]
44
>>> Seq([11, 22, 33, 44, 55, 66])[3:5]
Seq([44, 55])


>>> Seq([11, 22, 33]).ipopX(atL_vs_atR=False)
Seq([22, 33])
>>> Seq([11, 22, 33]).ipopX(atL_vs_atR=True)
Seq([11, 22])
>>> Seq([11, 22, 33]).ipopL()
Seq([22, 33])
>>> Seq([11, 22, 33]).ipopR()
Seq([11, 22])
>>> Seq([]).ipopR()
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23.EmptyError

>>> Seq([11, 22, 33]).vpopX(atL_vs_atR=False)
(11, Seq([22, 33]))
>>> Seq([11, 22, 33]).vpopX(atL_vs_atR=True)
(33, Seq([11, 22]))
>>> Seq([11, 22, 33]).vpopL()
(11, Seq([22, 33]))
>>> Seq([11, 22, 33]).vpopR()
(33, Seq([11, 22]))
>>> Seq([]).vpopL()
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23.EmptyError

>>> Seq([11, 22, 33]).ipushX(999, atL_vs_atR=False)
Seq([999, 11, 22, 33])
>>> Seq([11, 22, 33]).ipushX(999, atL_vs_atR=True)
Seq([11, 22, 33, 999])
>>> Seq([11, 22, 33]).ipushL(999)
Seq([999, 11, 22, 33])
>>> Seq([]).ipushR(999)
Seq([999])

__add__
>>> Seq([11, 22, 33]) + Seq([44, 55])
Seq([11, 22, 33, 44, 55])

__mul__
>>> Seq([11, 22, 33]) * 5
Seq([11, 22, 33, 11, 22, 33, 11, 22, 33, 11, 22, 33, 11, 22, 33])

__rmul__
>>> 5 * Seq([11, 22, 33])
Seq([11, 22, 33, 11, 22, 33, 11, 22, 33, 11, 22, 33, 11, 22, 33])









@20260401:++cut_, find, index
>>> Seq([11, 22, 33]).cut_(5, 6)
(3, 3, Seq())
>>> Seq([11, 22, 33]).cut_(6, 5)
(3, 3, Seq())
>>> Seq([11, 22, 33]).cut_(3, -1)
(3, 3, Seq())
>>> Seq([11, 22, 33]).cut_(2, -1)
(2, 2, Seq())
>>> Seq([11, 22, 33]).cut_(1, -1)
(1, 2, Seq([22]))
>>> Seq([11, 22, 33]).cut_(-3, -1)
(0, 2, Seq([11, 22]))

>>> Seq([11, 22, 33]).find(22)
1
>>> Seq([11, 22, 33]).find(24)
-1
>>> Seq([11, 22, 33]).find(22, 1, 2)
1
>>> Seq([11, 22, 33]).find(22, 2, 3)
-1


>>> Seq([11, 22, 33]).index(22)
1
>>> Seq([11, 22, 33]).index(24)
Traceback (most recent call last):
    ...
ValueError: 24


>>> Seq([11, 22, 33]).index(22, 1, 2)
1
>>> Seq([11, 22, 33]).index(22, 2, 3)
Traceback (most recent call last):
    ...
ValueError: 22



>>> Seq([11, 22, 33]).isetitem_(1, 66)
Seq([11, 66, 33])
>>> Seq([11, 22, 33]).isetitem_(-1, 66)
Seq([11, 22, 66])
>>> Seq([11, 22, 33]).isetitem_(-3, 66)
Seq([66, 22, 33])
>>> Seq([11, 22, 33]).isetitem_(-4, 66)
Traceback (most recent call last):
    ...
IndexError: -4
>>> Seq([11, 22, 33]).isetitem_(2, 66)
Seq([11, 22, 66])
>>> Seq([11, 22, 33]).isetitem_(3, 66)
Traceback (most recent call last):
    ...
IndexError: 3



>>> Seq([44, 33]) == Seq([44, 33])
True
>>> Seq([44, 33]) <= Seq([44, 33])
True
>>> Seq([44, 33]) >= Seq([44, 33])
True
>>> Seq([44, 33]) != Seq([44, 33])
False
>>> Seq([44, 33]) < Seq([44, 33])
False
>>> Seq([44, 33]) > Seq([44, 33])
False

>>> Seq([44]) == Seq([44, 33])
False
>>> Seq([44]) <= Seq([44, 33])
True
>>> Seq([44]) >= Seq([44, 33])
False
>>> Seq([44]) != Seq([44, 33])
True
>>> Seq([44]) < Seq([44, 33])
True
>>> Seq([44]) > Seq([44, 33])
False

>>> Seq([33, 44]) == Seq([44, 33])
False
>>> Seq([33, 44]) <= Seq([44, 33])
True
>>> Seq([33, 44]) >= Seq([44, 33])
False
>>> Seq([33, 44]) != Seq([44, 33])
True
>>> Seq([33, 44]) < Seq([44, 33])
True
>>> Seq([33, 44]) > Seq([44, 33])
False



__hash__
_ops = _ops7lazy if 1 else _ops7strict
>>> _ops.ops4auto._Auto.Nothing is default_Nothing
True
>>> _ops.ops4auto._strict
False

>>> {Seq()}
{Seq()}
>>> {Seq([33])}
{Seq([33])}
>>> {Seq([33, 44])}
{Seq([33, 44])}
>>> {Seq([33, 44, 55])}
{Seq([33, 44, 55])}
>>> {Seq([33, 44, 55, []])}
Traceback (most recent call last):
    ...
TypeError: some elems are unhashable
>>> hash(Seq([33, 44, 55, []]))
Traceback (most recent call last):
    ...
TypeError: some elems are unhashable
>>> hash(Seq([[]]))
Traceback (most recent call last):
    ...
TypeError: some elems are unhashable


>>> ft_seq = Seq([33, 44, 55])
>>> _show_tmay_properties6auto_(ft_seq)
len: (3,)
may_hash: ()
>>> h = hash(ft_seq)
>>> h #doctest: +SKIP
-6623189263665364036
>>> _show_tmay_properties6auto_(ft_seq)
len: (3,)
may_hash: (1100,)
>>> ((33*5+ 44)*5+ 55)
1100

>>> ft_seq = Seq(range(100_00))
>>> _show_tmay_properties6auto_(ft_seq)
len: (10000,)
may_hash: ()
>>> h = hash(ft_seq)
>>> _show_tmay_properties6auto_(ft_seq) #doctest: +ELLIPSIS
len: (10000,)
may_hash: (...,)
>>> _show_tmay_properties6auto_(ft_seq)
len: (10000,)
may_hash: (665014891999583672,)











py_adhoc_call   seed.data_funcs.finger_tree.ft23_7sized_seq   @f
]]]'''#'''
__all__ = r'''
    Seq
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property
from itertools import pairwise#islice
from seed.tiny_.check import check_type_is, check_int_ge
from collections.abc import Sequence
from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_len, check_ops4sized_finger_tree_, len5sized_finger_tree_, split_sized_finger_tree_
from seed.data_funcs.finger_tree.ft23_7types import default_Nothing, ops4attr_may_hash, check_ops4mhashable_finger_tree_, may_hash5mhashable_finger_tree_
___end_mark_of_excluded_global_names__0___ = ...

def _show_tmay_properties6auto_(ft_seq, /):
    for k, v in _iter_keyed_tmay_properties6auto_(ft_seq):
        print(k, v, sep=': ')
def _iter_keyed_tmay_properties6auto_(ft_seq, /):
    from seed.data_funcs.finger_tree.ft23 import Wrapper4ft_tree
    ops4ft = _ops
    tree = ft_seq._t
    wrp = Wrapper4ft_tree(ops4ft, depth:=0, tree)
    auto = wrp.auto
    for key6auto in sorted(ops4ft.available_keys6auto):
        tmay_property6auto = ops4ft.tmay_property5auto_and_key6auto_(auto, key6auto)
        yield (key6auto, tmay_property6auto)

_ops__ver0 = Ops4FingerTree(Ops4Auto6FingerTree([ops4attr_len]))
    # hash(tuple(Seq...))
_ops7strict = Ops4FingerTree(Ops4Auto6FingerTree([ops4attr_len, ops4attr_may_hash]))
    #pass doctest
_ops7lazy = Ops4FingerTree(Ops4Auto6FingerTree([ops4attr_len], default_Nothing, [ops4attr_may_hash]))
    #may_hash5mhashable_finger_tree_(_ops, depth:=0, sf._t, _no_check=True)
    #len5sized_finger_tree_(_ops, depth:=0, sf._t, _no_check=True)
_ops = _ops7lazy if 1 else _ops7strict
_empty_tree = _ops.mk_empty_tree_(0)
_leaf2data_ = _ops.get_data5leaf_
_leaf5data_ = _ops.mk_node7leaf_
class Seq(Sequence):
    ___no_slots_ok___ = True
    #.def __init__(sf, xs=None, /, *, reverse=False, _tree=None):
    def __new__(cls, xs=None, /, *, reverse=False, _tree=None):
        if cls is type(xs) and not reverse and _tree is None:
            sf = xs
            return sf
        sf = super(__class__, cls).__new__(cls)
        if not _tree is None:
            if not xs is None:raise TypeError
            if reverse:raise TypeError
            tree = _tree
        elif xs is None:
            tree = _empty_tree
        elif type(xs) is __class__:
            ot = xs
            tree = ot._t
        else:
            tree = _ops.mk_tree5datas_(xs, reverse=reverse)
        sf._t = tree
        if not sf:
            try:
                sf = _empty_seq
            except NameError:
                sf._t = _empty_tree
            sf
        return sf
    @cached_property
    def _sz(sf, /):
        return len5sized_finger_tree_(_ops, depth:=0, sf._t, _no_check=True)
    def __repr__(sf, /):
        xs = [*sf]
        return f'Seq({xs})' if xs else f'Seq()'
    #.@property
    #.def _args4hash(sf, /):
    #.    return (type(sf), len(sf), sf._t)
    #.@cached_property
    #.def _hash(sf, /):
    #.    return hash(sf._args4hash)
    #.def __hash__(sf, /):
    #.    return sf._hash
    #.def __eq__(sf, ot, /):
    #.    if sf is ot:
    #.        return True
    #.    if not type(sf) is type(ot):
    #.        return NotImplemented
    #.    return sf._args4hash == ot._args4hash

    if 0x00000:
        @cached_property
        def _hash(sf, /):
            # !! 『TypeError: unhashable type: 'Seq'』
            # => should be 『hash5hashable_finger_tree_(_ops, depth:=0, sf._t, _no_check=True)』
            # => simplified as 『hash(tuple(sf))』
            return hash((type(sf), tuple(sf)))
        def __hash__(sf, /):
            'slow hash#not delta algo'
            return sf._hash
    def __hash__(sf, /):
        if not None is (h:=sf._mh):
            return h
        raise TypeError('some elems are unhashable')
    @cached_property
    def _mh(sf, /):
        mh = may_hash5mhashable_finger_tree_(_ops, depth:=0, sf._t, _no_check=True)
        if mh is default_Nothing:raise 000
        if not None is mh:
            mh = hash((type(sf), mh))
        return mh
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not type(sf) is type(ot):
            return NotImplemented
        if not len(sf) == len(ot):
            return False
        if 0x00000:
            if '_hash' in vars(sf) and '_hash' in vars(ot):
                if not hash(sf) == hash(ot):
                    return False
        nm = '_mh'
        if nm in vars(sf) and nm in vars(ot):
                if not vars(sf)[nm] == vars(ot)[nm]:
                    return False
        return all(a==b for a, b in zip(sf, ot))
    def __le__(sf, ot, /):
        if sf is ot:
            return True
        if not isinstance(ot, Sequence):
            return NotImplemented
        for a, b in zip(sf, ot):
            if a == b:
                continue
            return a < b
        return len(sf) <= len(ot)
    def __lt__(sf, ot, /):
        if sf is ot:
            return False
        if not isinstance(ot, Sequence):
            return NotImplemented
        for a, b in zip(sf, ot):
            if a == b:
                continue
            return a < b
        return len(sf) < len(ot)
    def __ne__(sf, ot, /):
        b = type(sf).__eq__(sf, ot)
        if b is NotImplemented:
            return b
        return not b
    def __gt__(sf, ot, /):
        b = type(sf).__le__(sf, ot)
        if b is NotImplemented:
            return b
        return not b
    def __ge__(sf, ot, /):
        b = type(sf).__lt__(sf, ot)
        if b is NotImplemented:
            return b
        return not b

    def __len__(sf, /):
        return sf._sz
    def __iter__(sf, /):
        return _ops.iter_datas5tree_(depth:=0, sf._t, reverse=False)
    def __reversed__(sf, /):
        return _ops.iter_datas5tree_(depth:=0, sf._t, reverse=True)
    #.def iinsert_at_(sf, j, v, /):
    #.    'j -> Seq | ^IndexError'
    #.    return sf.iput_at_(j, v)
    def iputs_at_(sf, j, seqM, /):
        'j -> seqM -> Seq | ^IndexError'
        if not 0 <= j <= len(sf):raise IndexError(j)
        check_type_is(Seq, seqM)
        #seqM = Seq(seqM)
        if not seqM:
            return sf
        (seqL, seqR) = sf.split_at_(j)
        return (seqL + seqM + seqR)
    def iput_at_(sf, j, vM, /):
        'j -> vM -> Seq | ^IndexError'
        if not 0 <= j <= len(sf):raise IndexError(j)
        if j == 0:
            return sf.ipushL(vM)
        if j == len(sf):
            return sf.ipushR(vM)
        seqM = Seq([vM])
        return sf.iputs_at_(j, seqM)
    #.def idelete_at_(sf, j, /):
    #.    '-> seqL_R | ^IndexError'
    #.    return sf.ipop_at_(j)
    def ipop_at_(sf, j, /):
        'j -> seqL_R | ^IndexError'
        return sf.vpop_at_(j)[1]
    def vpop_at_(sf, j, /):
        'j -> (vM, seqL_R) | ^IndexError'
        if not 0 <= j < len(sf):raise IndexError(j)
        seqL, seqR = sf.split_at_(j)
        (vM, _seqR) = seqR.vpopL()
        return (vM, seqL+_seqR)
    def ipop_between_ge_lt_(sf, i, j, /):
        'i -> j -> seqL_R | ^IndexError'
        return sf.vpop_between_ge_lt_(i, j)[1]
    #def vpop_between_(sf, i, j, /):
    def vpop_between_ge_lt_(sf, i, j, /):
        'i -> j -> (seqM, seqL_R) | ^IndexError'
        if not 0 <= i <= j <= len(sf):raise IndexError(i, j, len(sf))
        if i == j:
            return (_empty_seq, sf)
        (seqL, seqM, seqR) = sf.splits_at_(i, j)
        return (seqM, seqL+seqR)
    def splits_at_(sf, /, *js):
        '(*js{ascend}) -> [Seq]{len==1+len(js)} | ^IndexError'
        if not js:
            return (sf,)
        if not 0 <= js[0]:raise IndexError(js[0])
        if not js[-1] <= len(sf):raise IndexError(js[-1])
        if not all(i <= j for i, j in pairwise(js)):raise IndexError(js)
        ls = []#reversed
        for j in reversed(js):
            (sf, seqR) = sf.split_at_(j)
            ls.append(seqR)
        ls.append(sf)
        return tuple(reversed(ls))
    def split_at_(sf, j, /):
        'j -> (seqL, seqR) | ^IndexError # [[len(seqL) == j]or[len(seqL) == len(sf) < j]][sf == (seqL ++ seqR)]'
        if not 0 <= j <= len(sf):raise IndexError(j)
        (treeL, treeR) = split_sized_finger_tree_(_ops, depth:=0, j, sf._t, _no_check=True)
        seqL = Seq(_tree=treeL)
        seqR = Seq(_tree=treeR)
        return (seqL, seqR)
    #def __delitem__(sf, z, /):
    #def __setitem__(sf, z, v, /):
    def isetitem_(sf, j, v, /):
        '-> Seq | ^IndexError'
        L = len(sf)
        if j < 0:
            if not j >= -L:raise IndexError(j)
            j += L
        if not 0 <= j < L:raise IndexError(j)
        sf_, _v_, _sf = sf.splits_at_(j, j+1)
        ot = sf_.ipushR(v) + _sf
        return ot
    def __getitem__(sf, z, /):
        y = range(L:=len(sf))[z]
        #if type(z) is slice:
        if type(y) is range:
            rng = y
            if not rng:
                return _empty_seq
            if rng.step == 1:
                sf_, _ = sf.split_at_(1+rng[-1])
                _, _sf_ = sf_.split_at_(rng[0])
                return _sf_
            if not rng.step == 1: raise NotImplementedError
            raise NotImplementedError
        else:
            j = y
            if j == 0:
                for x in iter(sf):
                    return x
                raise 000
            if j == L-1:
                for x in reversed(sf):
                    return x
                raise 000
            if not j < L: raise 000
            (seqL, seqR) = sf.split_at_(j)
            for x in iter(seqR):
                return x
            raise 000
    def cut_(sf, begin=None, end=None, /):
        '-> (begin, end, Seq)'
        if not sf:
            return (0, 0, sf)
        (i, j, _1) = slice(begin, end, 1).indices(len(sf))
        if not i < j:
            j = i
            _sf_ = sf[:0]
        elif i == 0 and j == len(sf):
            _sf_ = sf
        else:
            #_sf_ = sf[i:j]
            (_, _sf_, _) = sf.splits_at_(i, j)
        _sf_
        return (i, j, _sf_)
    def find(sf, v, begin=None, end=None, /):
        (i, j, _sf_) = sf.cut_(begin, end)
        vs = [v]
        for k, x in enumerate(_sf_, i):
            if x in vs:
                return k
        return -1
    def index(sf, v, begin=None, end=None, /):
        if not -1 == (j:=sf.find(v, begin, end)):
            return j
        raise ValueError(v)
    def ipopX(sf, /, *, atL_vs_atR:bool):
        '-> seqY{atL_vs_atR} | ^EmptyError'
        return sf.vpopX(atL_vs_atR=atL_vs_atR)[1]
    def ipopL(sf, /):
        '-> seqR | ^EmptyError'
        return sf.vpopL()[1]
    def ipopR(sf, /):
        '-> seqL | ^EmptyError'
        return sf.vpopR()[1]
    def vpopX(sf, /, *, atL_vs_atR:bool):
        '-> (vX, seqY){atL_vs_atR} | ^EmptyError'
        (leafX, treeY) = _ops.mk_tree7pop_(depth:=0, sf._t, atL_vs_atR=atL_vs_atR)
            # ^EmptyError
        vX = _leaf2data_(leafX)
        seqY = Seq(_tree=treeY)
        return (vX, seqY)
    def vpopL(sf, /):
        '-> (vL, seqR) | ^EmptyError'
        return sf.vpopX(atL_vs_atR=False)
    def vpopR(sf, /):
        '-> (vR, seqL) | ^EmptyError'
        return sf.vpopX(atL_vs_atR=True)
    def ipushL(sf, x, /):
        '-> Seq'
        return sf.ipushX(x, atL_vs_atR=False)
    def ipushR(sf, x, /):
        '-> Seq'
        return sf.ipushX(x, atL_vs_atR=True)
    def ipushX(sf, x, /, *, atL_vs_atR:bool):
        '-> Seq'
        leaf = _leaf5data_(x)
        tree = _ops.mk_tree7push_(depth:=0, leaf, sf._t, atL_vs_atR=atL_vs_atR)
        return Seq(_tree=tree)
    def __add__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        #def mk_tree7chainLMR_(sf, depth, treeL, nodesM, treeR, /):
        tree = _ops.mk_tree7chainLMR_(depth:=0, sf._t, '', ot._t)
        return Seq(_tree=tree)
    def __rmul__(sf, ot, /):
        if not type(ot) is int:
            return NotImplemented
        return sf*ot
    def __mul__(sf, ot, /):
        if not type(ot) is int:
            return NotImplemented
        k = ot
        if not k > 0:
            return _empty_seq
        if k == 1 or not sf:
            return sf
        s = bin(k)
        assert s[:3] == '0b1'
        s = s[3:]
        ot = sf
        for b in s:
            ot += ot
            if b == '1':
                ot += sf
        return ot
_empty_seq = Seq()


__all__
from seed.data_funcs.finger_tree.ft23_7sized_seq import Seq
from seed.data_funcs.finger_tree.ft23_7sized_seq import *
