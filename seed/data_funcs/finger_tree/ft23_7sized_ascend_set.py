#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_ascend_set.py
view ../../python3_src/seed/data_funcs/finger_tree/ft23_7types.py
view ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_seq.py

seed.data_funcs.finger_tree.ft23_7sized_ascend_set
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.ft23_7sized_ascend_set -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.ft23_7sized_ascend_set:__doc__ -ht # -ff -df
#######

[[
index
index_gt_
]]


'#'; __doc__ = r'#'
>>> AscendSet()
AscendSet()
>>> AscendSet([99, 44, 11, 33, 55, 22, True, 1])
AscendSet([1, 11, 22, 33, 44, 55, 99])
>>> AscendSet([0,1,2], unordered_vs_ascend_vs_descend=1)
AscendSet([0, 1, 2])
>>> AscendSet([2,1,0], unordered_vs_ascend_vs_descend=2)
AscendSet([0, 1, 2])
>>> len(AscendSet([0,1,2]))
3
>>> [*iter(AscendSet([0,1,2]))]
[0, 1, 2]
>>> [*reversed(AscendSet([0,1,2]))]
[2, 1, 0]



>>> AscendSet([0,11,22]).index(11)
1
>>> AscendSet([0,11,22]).index_eq_(11)
1
>>> AscendSet([0,11,22]).find_eq_(11)
1
>>> AscendSet([0,11,22]).index_ge_(11)
1
>>> AscendSet([0,11,22]).index_gt_(11)
2

>>> ([0,22]).index(11)
Traceback (most recent call last):
    ...
ValueError: 11 is not in list
>>> AscendSet([0,22]).index(11)
Traceback (most recent call last):
    ...
ValueError: 11
>>> AscendSet([0,22]).index_eq_(11)
Traceback (most recent call last):
    ...
ValueError: 11
>>> AscendSet([0,22]).find_eq_(11)
-1
>>> AscendSet([0,22]).index_ge_(11)
1
>>> AscendSet([0,22]).index_gt_(11)
1


>>> AscendSet([0,11,22]).index_eq_(11, -2, -1)
1
>>> AscendSet([0,11,22]).find_eq_(11, -2, -1)
1
>>> AscendSet([0,11,22]).index_eq_(11, 0, 1)
Traceback (most recent call last):
    ...
ValueError: 11
>>> AscendSet([0,11,22]).find_eq_(11, 0, 1)
-1




>>> AscendSet([11,22,33]).iputs_at_(1, AscendSet([12,13]))
AscendSet([11, 12, 13, 22, 33])
>>> AscendSet([11,22,33]).iputs_at_(1, AscendSet([11]))
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> AscendSet([11,22,33]).iputs_at_(-1, AscendSet([]))
Traceback (most recent call last):
    ...
IndexError: -1
>>> AscendSet([11,22,33]).iputs_at_(4, AscendSet([]))
Traceback (most recent call last):
    ...
IndexError: 4

>>> AscendSet([11,22,33]).iput_at_(1, 12)
AscendSet([11, 12, 22, 33])
>>> AscendSet([11,22,33]).iput_at_(1, 11)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> AscendSet([11,22,33]).iput_at_(1, 22)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> AscendSet([11,22,33]).iput_at_(4, 22)
Traceback (most recent call last):
    ...
IndexError: 4


>>> AscendSet([11,22,33]).ipop_at_(1)
AscendSet([11, 33])
>>> AscendSet([11,22,33]).vpop_at_(1)
(22, AscendSet([11, 33]))
>>> AscendSet([]).vpop_at_(0)
Traceback (most recent call last):
    ...
IndexError: 0
>>> AscendSet([11,22,33]).ipop_between_ge_lt_(1, 2)
AscendSet([11, 33])
>>> AscendSet([11,22,33]).vpop_between_ge_lt_(1, 2)
(AscendSet([22]), AscendSet([11, 33]))

>>> AscendSet([11, 22, 33, 44, 55, 66]).splits_at_()
(AscendSet([11, 22, 33, 44, 55, 66]),)
>>> AscendSet([11, 22, 33, 44, 55, 66]).splits_at_(2)
(AscendSet([11, 22]), AscendSet([33, 44, 55, 66]))
>>> AscendSet([11, 22, 33, 44, 55, 66]).splits_at_(2,3,5)
(AscendSet([11, 22]), AscendSet([33]), AscendSet([44, 55]), AscendSet([66]))

>>> AscendSet([11, 22, 33, 44, 55, 66]).split_at_(2)
(AscendSet([11, 22]), AscendSet([33, 44, 55, 66]))



>>> AscendSet([0,11,22]).partition_at_key_(11)
(AscendSet([0]), (11,), AscendSet([22]))
>>> AscendSet([0,11,22]).partition_at_key_(12)
(AscendSet([0, 11]), (), AscendSet([22]))
>>> AscendSet([0,11,22]).split_at_key_(11)
(AscendSet([0, 11]), AscendSet([22]))
>>> AscendSet([0,22]).split_at_key_(11)
(AscendSet([0]), AscendSet([22]))
>>> AscendSet([0,11,22]).split_at_(1)
(AscendSet([0]), AscendSet([11, 22]))
>>> AscendSet([0,22]).split_at_(1)
(AscendSet([0]), AscendSet([22]))

>>> AscendSet([0,11,22])[::]
AscendSet([0, 11, 22])
>>> AscendSet([0,11,22])[1:]
AscendSet([11, 22])
>>> AscendSet([0,11,22])[:-1]
AscendSet([0, 11])
>>> AscendSet([0,11,22])[1:-1]
AscendSet([11])
>>> AscendSet([0,11,22])[1]
11
>>> AscendSet([0,11,22])[-1]
22


>>> AscendSet([0,11,22]).ipopX(atL_vs_atR=False)
AscendSet([11, 22])
>>> AscendSet([0,11,22]).ipopL()
AscendSet([11, 22])
>>> AscendSet([0,11,22]).ipopR()
AscendSet([0, 11])
>>> AscendSet([0,11,22]).vpopX(atL_vs_atR=False)
(0, AscendSet([11, 22]))
>>> AscendSet([0,11,22]).vpopX(atL_vs_atR=True)
(22, AscendSet([0, 11]))
>>> AscendSet([0,11,22]).vpopL()
(0, AscendSet([11, 22]))
>>> AscendSet([0,11,22]).vpopR()
(22, AscendSet([0, 11]))
>>> AscendSet([]).vpopR()
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23.EmptyError


>>> AscendSet([0,11,22]).ipushX(-11, atL_vs_atR=False)
AscendSet([-11, 0, 11, 22])
>>> AscendSet([0,11,22]).ipushX(33, atL_vs_atR=True)
AscendSet([0, 11, 22, 33])

>>> AscendSet([0,11,22]).ipushL(-11)
AscendSet([-11, 0, 11, 22])
>>> AscendSet([0,11,22]).ipushR(33)
AscendSet([0, 11, 22, 33])

>>> AscendSet([0,11,22]).ipushL(5)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> AscendSet([0,11,22]).ipushR(5)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> AscendSet([0,11,22]).ipushL(0)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> AscendSet([0,11,22]).ipushR(22)
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError

>>> AscendSet([0,11,22]).iput(5)
AscendSet([0, 5, 11, 22])
>>> AscendSet([0,True,22]).iput(1, no_overwrite=True)
AscendSet([0, True, 22])
>>> AscendSet([0,11,22]).vput(5)
((), AscendSet([0, 5, 11, 22]))
>>> AscendSet([0,True,22]).vput(1)
((True,), AscendSet([0, 1, 22]))
>>> AscendSet([0,True,22]).vput(1, no_overwrite=True)
((True,), AscendSet([0, True, 22]))

>>> AscendSet([0,11,22]).idiscard(5)
AscendSet([0, 11, 22])
>>> AscendSet([0,11,22]).idiscard(11)
AscendSet([0, 22])
>>> AscendSet([0,11,22]).vdiscard(5)
((), AscendSet([0, 11, 22]))
>>> AscendSet([0,11,22]).vdiscard(11)
((11,), AscendSet([0, 22]))
>>> AscendSet([0,True,22]).vdiscard(1)
((True,), AscendSet([0, 22]))
>>> AscendSet([0,True,22]).wdiscard(1)
((True,), 1, AscendSet([0, 22]))
>>> AscendSet([0,11,22]).wdiscard(5)
((), 1, AscendSet([0, 11, 22]))

>>> AscendSet([0,True,22]).iremove(22)
AscendSet([0, True])
>>> AscendSet([0,22]).iremove(1)
Traceback (most recent call last):
    ...
LookupError: 1
>>> AscendSet([0,True,22]).vremove(22)
(22, AscendSet([0, True]))
>>> AscendSet([0,True,22]).vremove(1)
(True, AscendSet([0, 22]))
>>> AscendSet([0,22]).vremove(1)
Traceback (most recent call last):
    ...
LookupError: 1

#__contains__
>>> 5 in AscendSet([0,11,22])
False
>>> 11 in AscendSet([0,11,22])
True

__hash__
>>> {AscendSet([0,11,22])} #hash
{AscendSet([0, 11, 22])}

__eq__
>>> AscendSet([0,11,22]) == AscendSet([0,11,22])
True
>>> AscendSet([0,11,22]) != AscendSet([0,11,22])
False
>>> AscendSet([0,11,22]) <= AscendSet([0,11,22])
True
>>> AscendSet([0,11,22]) >= AscendSet([0,11,22])
True
>>> AscendSet([0,11,22]) > AscendSet([0,11,22])
False
>>> AscendSet([0,11,22]) < AscendSet([0,11,22])
False

>>> AscendSet([0,22]) == AscendSet([0,11,22])
False
>>> AscendSet([0,22]) != AscendSet([0,11,22])
True
>>> AscendSet([0,22]) <= AscendSet([0,11,22])
True
>>> AscendSet([0,22]) >= AscendSet([0,11,22])
False
>>> AscendSet([0,22]) > AscendSet([0,11,22])
False
>>> AscendSet([0,22]) < AscendSet([0,11,22])
True


>>> AscendSet([0,11,33]) == AscendSet([0,11,22])
False
>>> AscendSet([0,11,33]) != AscendSet([0,11,22])
True
>>> AscendSet([0,11,33]) <= AscendSet([0,11,22])
False
>>> AscendSet([0,11,33]) >= AscendSet([0,11,22])
False
>>> AscendSet([0,11,33]) > AscendSet([0,11,22])
False
>>> AscendSet([0,11,33]) < AscendSet([0,11,22])
False


__add__
>>> AscendSet([0,11,22]) + AscendSet([])
AscendSet([0, 11, 22])
>>> AscendSet([0,11,22]) + AscendSet([33,44])
AscendSet([0, 11, 22, 33, 44])
>>> AscendSet([0,11,22]) + AscendSet([22])
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError
>>> AscendSet([0,11,22]) + AscendSet([21])
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23_7sized_ascend_set.NotAscendError

>>> (s:=AscendSet([0,11,22])).copy() is s
True

>>> AscendSet([0,11,22]).issubset(AscendSet([0,11,21]))
False
>>> AscendSet([0,11,22]).issubset(AscendSet([0,11]))
False
>>> AscendSet([0,11,22]).issubset(AscendSet([0,11,22]))
True
>>> AscendSet([0,11,22]).issubset(AscendSet([0,11,22,23]))
True

>>> AscendSet([0,11,22]).issuperset(AscendSet([0,11,21]))
False
>>> AscendSet([0,11,22]).issuperset(AscendSet([0,11]))
True
>>> AscendSet([0,11,22]).issuperset(AscendSet([0,11,22]))
True
>>> AscendSet([0,11,22]).issuperset(AscendSet([0,11,22,23]))
False

>>> AscendSet([0,11,22]).ascend_chain(AscendSet([33,44]), AscendSet([55]))
AscendSet([0, 11, 22, 33, 44, 55])

>>> AscendSet([0,11,22]).difference(AscendSet([11,44]), AscendSet([55]))
AscendSet([0, 22])
>>> AscendSet([0,11,22]).difference(AscendSet([11,44]), AscendSet([0]))
AscendSet([22])

>>> AscendSet([0,11,22]).intersection(AscendSet([11,44]), AscendSet([55]))
AscendSet()
>>> AscendSet([0,11,22]).intersection(AscendSet([11,44]))
AscendSet([11])

>>> AscendSet([0,11,22]).symmetric_difference(AscendSet([11,22,44]), AscendSet([22,55]))
AscendSet([0, 22, 44, 55])

>>> AscendSet([0,11,22]).union(AscendSet([11,44]), AscendSet([55]))
AscendSet([0, 11, 22, 44, 55])


#overwrite:lhs:
>>> AscendSet([True]) & AscendSet([1])
AscendSet([1])
>>> AscendSet([True]) | AscendSet([1])
AscendSet([1])
>>> AscendSet([1]) & AscendSet([True])
AscendSet([True])
>>> AscendSet([1]) | AscendSet([True])
AscendSet([True])


>>> AscendSet([0,11,22]) & AscendSet([11,44])
AscendSet([11])
>>> AscendSet([0,11,22]) | AscendSet([11,44])
AscendSet([0, 11, 22, 44])
>>> AscendSet([0,11,22]) ^ AscendSet([11,44])
AscendSet([0, 22, 44])
>>> AscendSet([0,11,22]) - AscendSet([11,44])
AscendSet([0, 22])

>>> AscendSet([0,11,22]).isdisjoint(AscendSet([11,44]))
False
>>> AscendSet([0,11,22]).isdisjoint(AscendSet([33,44]))
True

>>> [*AscendSet([0,True,11,22]).reversed_iter_match_parts_of_(AscendSet([1,11,44]))]
[(1, AscendSet([44])), (0, AscendSet([22])), (2, (AscendSet([True, 11]), AscendSet([1, 11]))), (0, AscendSet([0]))]






>>> AscendSet([0,11,22,23])
AscendSet([0, 11, 22, 23])
















py_adhoc_call   seed.data_funcs.finger_tree.ft23_7sized_ascend_set   @f
]]]'''#'''
__all__ = r'''
AscendSet

NotAscendError
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import pairwise #islice
from functools import cached_property
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt
from collections.abc import Set as ISet

from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_rightmost7echo, check_ops4ascend_finger_tree_, tmay_rightmost5ascend_finger_tree_, split_ascend_finger_tree_

from seed.data_funcs.finger_tree.ft23_7types import Ops4FingerTree, Ops4Auto6FingerTree, ops4attr_len, check_ops4sized_finger_tree_, len5sized_finger_tree_, split_sized_finger_tree_, ops4attr_hash, check_ops4hashable_finger_tree_, hash5hashable_finger_tree_


___end_mark_of_excluded_global_names__0___ = ...

#>>> dir(frozenset)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']

def _unique_(xs, /):
    xs = sorted(xs)
    if not xs:
        return xs
    i = 0
    x = xs[i]
    for j in range(1, len(xs)):
        y = xs[j]
        if y == x:
            # y:overwrite:x
            xs[i] = x = y
        else:
            # append:y
            i += 1
            x = y
            if not i == j:
                xs[i] = x
    del xs[i+1:]
    return xs

_ops = Ops4FingerTree(Ops4Auto6FingerTree([ops4attr_len, ops4attr_hash, ops4attr_rightmost7echo]))
_empty_tree = _ops.mk_empty_tree_(0)
def _leaf2attr6auto_(key6auto, leaf, /):
    auto = _ops.get_auto5node_(depth:=0, leaf)
    attr6auto = auto[key6auto]
    return attr6auto#NOTE:maybe 『tmay』
_leaf2data_ = _ops.get_data5leaf_
_leaf5data_ = _ops.mk_node7leaf_
#.def _leaf2ord_key_(leaf, /):
#.    [k] = _leaf2attr6auto_('rightmost', leaf, /)
#.    return k
_leaf2ord_key_ = _leaf2data_
class NotAscendError(Exception):pass
class AscendSet(ISet):
    ___no_slots_ok___ = True
    #.def __init__(sf, xs=None, /, *, unordered_vs_ascend_vs_descend=0, _tree=None):
    def __new__(cls, xs=None, /, *, unordered_vs_ascend_vs_descend=0, _tree=None):
        check_int_ge_lt(0, 3, unordered_vs_ascend_vs_descend)
        if cls is type(xs) and not 2 == unordered_vs_ascend_vs_descend and _tree is None:
            sf = xs
            return sf
        sf = super(__class__, cls).__new__(cls)
        if not _tree is None:
            if not xs is None:raise TypeError
            if not unordered_vs_ascend_vs_descend == 0:raise TypeError
            tree = _tree
        elif xs is None:
            tree = _empty_tree
        elif type(xs) is __class__:
            ot = xs
            tree = ot._t
        else:
            match unordered_vs_ascend_vs_descend:
                case 0:
                    xs = _unique_(xs)
                    leafs = map(_leaf5data_, xs)
                    #leafs = sorted(leafs, key=_leaf2ord_key_)
                    #if not all(a < b for a, b in pairwise(map(_leaf2ord_key_, leafs))):raise TypeError
                    tree = _ops.mk_tree5leafs_(leafs, reverse=False)
                case 1:
                    tree = _ops.mk_tree5datas_(xs, reverse=False)
                case 2:
                    tree = _ops.mk_tree5datas_(xs, reverse=True)
                case _:
                    raise TypeError(unordered_vs_ascend_vs_descend)
                #case
            tree
            it = _ops.iter_datas5tree_(depth:=0, tree, reverse=False)
            if not all(a < b for a, b in pairwise(it)):raise NotAscendError
            tree
        tree
        sf._t = tree
        if not sf:
            try:
                sf = _empty_set
            except NameError:
                sf._t = _empty_tree
            sf
        return sf
    @cached_property
    def _sz(sf, /):
        return len5sized_finger_tree_(_ops, depth:=0, sf._t, _no_check=True)
    def __repr__(sf, /):
        xs = [*sf]
        return f'AscendSet({xs})' if xs else f'AscendSet()'
    def __len__(sf, /):
        return sf._sz
    def __iter__(sf, /):
        return _ops.iter_datas5tree_(depth:=0, sf._t, reverse=False)
    def __reversed__(sf, /):
        return _ops.iter_datas5tree_(depth:=0, sf._t, reverse=True)
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
    def find_eq_(sf, v, begin=None, end=None, /):
        (i, j, _sf_) = sf.cut_(begin, end)
        vs = [v]
        for k, x in enumerate(_sf_, i):
            if x in vs:
                return k
        return -1
    def index_eq_(sf, v, begin=None, end=None, /):
        if not -1 == (j:=sf.find_eq_(v, begin, end)):
            return j
        raise ValueError(v)

    def index(sf, v, begin=None, end=None, /):
        return sf.index_eq_(v, begin, end)
    #.def index(sf, x, /):
    #.    return sf.index_eq_(x)
    #.def index_eq_(sf, x, /):
    #.    if not -1 == (j:=sf.find_eq_(x)):
    #.        return j
    #.    #.raise IndexError(x)
    #.    #@20260401:
    #.    raise ValueError(x)
    #.def find_eq_(sf, x, /):
    #.    '-> imay idx'
    #.    (setL, setR) = sf.split_at_key_(x)
    #.    if setL and setL[-1] == x:
    #.        return -1+len(setL)
    #.    return -1
    def index_gt_(sf, x, /):
        (setL, setR) = sf.split_at_key_(x)
        return len(setL)
    def index_ge_(sf, x, /):
        (setL, setR) = sf.split_at_key_(x)
        if setL and setL[-1] == x:
            return -1+len(setL)
        return len(setL)
    #.def iinsert_at_(sf, j, v, /):
    #.    'j -> AscendSet | ^IndexError'
    #.    return sf.iput_at_(j, v)
    def iputs_at_(sf, j, setM, /):
        'j -> setM -> AscendSet | ^IndexError | ^NotAscendError'
        if not 0 <= j <= len(sf):raise IndexError(j)
        check_type_is(AscendSet, setM)
        #setM = AscendSet(setM)
        if not setM:
            return sf
        (setL, setR) = sf.split_at_(j)
        return (setL + setM + setR)
            # ^NotAscendError
    def iput_at_(sf, j, vM, /):
        'j -> vM -> AscendSet | ^IndexError | ^NotAscendError'
        if not 0 <= j <= len(sf):raise IndexError(j)
        if j == 0:
            return sf.ipushL(vM)
                # ^NotAscendError
        if j == len(sf):
            return sf.ipushR(vM)
                # ^NotAscendError
        setM = AscendSet([vM])
        return sf.iputs_at_(j, setM)
                # ^NotAscendError
    #.def idelete_at_(sf, j, /):
    #.    '-> setL_R | ^IndexError'
    #.    return sf.ipop_at_(j)
    def ipop_at_(sf, j, /):
        'j -> setL_R | ^IndexError'
        return sf.vpop_at_(j)[1]
    def vpop_at_(sf, j, /):
        'j -> (vM, setL_R) | ^IndexError'
        if not 0 <= j < len(sf):raise IndexError(j)
        setL, setR = sf.split_at_(j)
        (vM, _setR) = setR.vpopL()
        return (vM, setL+_setR)
    def ipop_between_ge_lt_(sf, i, j, /):
        'i -> j -> setL_R | ^IndexError'
        return sf.vpop_between_ge_lt_(i, j)[1]
    #def vpop_between_(sf, i, j, /):
    def vpop_between_ge_lt_(sf, i, j, /):
        'i -> j -> (setM, setL_R) | ^IndexError'
        if not 0 <= i <= j <= len(sf):raise IndexError(i, j, len(sf))
        if i == j:
            return (_empty_set, sf)
        (setL, setM, setR) = sf.splits_at_(i, j)
        return (setM, setL+setR)
    def splits_at_(sf, /, *js):
        '(*js{ascend}) -> [AscendSet]{len==1+len(js)} | ^IndexError'
        if not js:
            return (sf,)
        if not 0 <= js[0]:raise IndexError(js[0])
        if not js[-1] <= len(sf):raise IndexError(js[-1])
        if not all(i <= j for i, j in pairwise(js)):raise IndexError(js)
        ls = []#reversed
        for j in reversed(js):
            (sf, setR) = sf.split_at_(j)
            ls.append(setR)
        ls.append(sf)
        return tuple(reversed(ls))

    def partition_at_key_(sf, k, /):
        'k -> (setL, tmay vM, setR) # [sf == (setL ++ tmay_vM ++ setR)][[kL:<-setL] -> [kL < k]][[vM:<-tmay_vM] -> [k == vM]][[kR:<-setR] -> [k < kR]]'
        (setLM, setR) = sf.split_at_key_(k)
        if setLM and setLM[-1] == k:
            (vM, setL) = setLM.vpopR()
            tmay_vM = (vM,)
        else:
            setL = setLM
            tmay_vM = ()
        return (setL, tmay_vM, setR)
    def split_at_key_(sf, k, /):
        'k -> (setL, setR) # [sf == (setL ++ setR)][[kL:<-setL] -> [kL <= k]][[kR:<-setR] -> [k < kR]]'
        (treeL, treeR) = split_ascend_finger_tree_(_ops, depth:=0, k, sf._t, _no_check=True)
        setL = AscendSet(_tree=treeL)
        setR = AscendSet(_tree=treeR)
        return (setL, setR)
    def split_at_(sf, j, /):
        'j -> (setL, setR) | ^IndexError # [[len(setL) == j]or[len(setL) == len(sf) < j]][sf == (setL ++ setR)]'
        if not 0 <= j <= len(sf):raise IndexError(j)
        (treeL, treeR) = split_sized_finger_tree_(_ops, depth:=0, j, sf._t, _no_check=True)
        setL = AscendSet(_tree=treeL)
        setR = AscendSet(_tree=treeR)
        return (setL, setR)
    def __getitem__(sf, z, /):
        y = range(L:=len(sf))[z]
        #if type(z) is slice:
        if type(y) is range:
            rng = y
            if not rng:
                return _empty_set
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
            (setL, setR) = sf.split_at_(j)
            for x in iter(setR):
                return x
            raise 000

    def ipopX(sf, /, *, atL_vs_atR:bool):
        '-> setY{atL_vs_atR} | ^EmptyError'
        return sf.vpopX(atL_vs_atR=atL_vs_atR)[1]
    def ipopL(sf, /):
        '-> setR | ^EmptyError'
        return sf.vpopL()[1]
    def ipopR(sf, /):
        '-> setL | ^EmptyError'
        return sf.vpopR()[1]
    def vpopX(sf, /, *, atL_vs_atR:bool):
        '-> (kX, setY){atL_vs_atR} | ^EmptyError'
        (leafX, treeY) = _ops.mk_tree7pop_(depth:=0, sf._t, atL_vs_atR=atL_vs_atR)
            # ^EmptyError
        kX = _leaf2data_(leafX)
        setY = AscendSet(_tree=treeY)
        return (kX, setY)
    def vpopL(sf, /):
        '-> (kL, setR) | ^EmptyError'
        return sf.vpopX(atL_vs_atR=False)
    def vpopR(sf, /):
        '-> (kR, setL) | ^EmptyError'
        return sf.vpopX(atL_vs_atR=True)
    def ipushL(sf, x, /):
        '-> AscendSet | ^NotAscendError'
        return sf.ipushX(x, atL_vs_atR=False)
    def ipushR(sf, x, /):
        '-> AscendSet | ^NotAscendError'
        return sf.ipushX(x, atL_vs_atR=True)
    def ipushX(sf, x, /, *, atL_vs_atR:bool):
        '-> AscendSet | ^NotAscendError # see:vput()'
        if not atL_vs_atR:
            if sf and not x < sf[0]: raise NotAscendError
        else:
            if sf and not sf[-1] < x: raise NotAscendError
        leaf = _leaf5data_(x)
        tree = _ops.mk_tree7push_(depth:=0, leaf, sf._t, atL_vs_atR=atL_vs_atR)
        return AscendSet(_tree=tree)
    def iput(sf, x, /, *, no_overwrite=False):
        '-> AscendSet # see:ipushX()'
        return sf.vput(x, no_overwrite=no_overwrite)[1]
    def vput(sf, x, /, *, no_overwrite=False):
        '-> (tmay_hit, AscendSet) # see:ipushX()'
        (setL, setR) = sf.split_at_key_(x)
        if setL and (hit:=setL[-1]) == x:
            tmay_hit = (hit,)
            if no_overwrite:
                return (tmay_hit, sf)
            (_, setL) = setL.vpopR()
        else:
            tmay_hit = ()
        tmay_hit
        #setL = setL.ipushR(x)
        leafM = _leaf5data_(x)
        tree = _ops.mk_tree7chainLMR_(depth:=0, setL._t, [leafM], setR._t)
        return (tmay_hit, AscendSet(_tree=tree))
    def iremove(sf, x, /):
        '-> AscendSet | ^LookupError'
        return sf.vremove(x)[1]
    def vremove(sf, x, /):
        '-> (old_x, AscendSet) | ^LookupError'
        (setL, setR) = sf.split_at_key_(x)
        if setL and setL[-1] == x:
            (y, setL) = setL.vpopR()
            return (y, setL + setR)
        raise LookupError(x)
    def idiscard(sf, x, /):
        '-> AscendSet # see:iremove()'
        return sf.vdiscard(x)[1]
    def vdiscard(sf, x, /):
        '-> (tmay_hit, AscendSet) # see:vremove()'
        (tmay_hit, j, ot) = sf.wdiscard(x)
        return (tmay_hit, ot)
    def wdiscard(sf, x, /):
        '-> (tmay_hit, idx, AscendSet) # see:vremove()'
        (setLM, setR) = sf.split_at_key_(x)
        if setLM and (hit:=setLM[-1]) == x:
            (_hit, setL) = setLM.vpopR()
            assert _hit is hit
            tmay_hit = (hit,)
            ot = setL + setR
        else:
            setL = setLM
            tmay_hit = ()
            ot = sf
        j = len(setL)
        return (tmay_hit, j, ot)
    def __contains__(sf, x, /):
        (setL, setR) = sf.split_at_key_(x)
        return setL and setL[-1] == x
    @cached_property
    def _hash(sf, /):
        return hash((type(sf), hash5hashable_finger_tree_(_ops, depth:=0, sf._t, _no_check=True)))
    def __hash__(sf, /):
        return sf._hash
    def __eq__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        if not len(sf) == len(ot):
            return False
        if '_hash' in vars(sf) and '_hash' in vars(ot):
            if not hash(sf) == hash(ot):
                return False
        return all(a == b for a, b in zip(sf, ot))
    def __ne__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        return not sf == ot
    def __le__(sf, ot, /):
        'set.(|<=|) or seq.(<=)'
        if not type(ot) is type(sf):
            return NotImplemented
        if not len(sf) <= len(ot):
            return False
        return all(x in ot for x in sf)
    def __lt__(sf, ot, /):
        'set.(|<|) or seq.(<)'
        if not type(ot) is type(sf):
            return NotImplemented
        if not len(sf) < len(ot):
            return False
        return sf <= ot
    def __gt__(sf, ot, /):
        'set.(|>|) or seq.(>)'
        if not type(ot) is type(sf):
            return NotImplemented
        return ot < sf
    def __ge__(sf, ot, /):
        'set.(|>=|) or seq.(>=)'
        if not type(ot) is type(sf):
            return NotImplemented
        return ot <= sf

    def __add__(sf, ot, /):
        '-> AscendSet | ^NotAscendError'
        if not type(ot) is type(sf):
            return NotImplemented
        #def mk_tree7chainLMR_(sf, depth, treeL, nodesM, treeR, /):
        if not ot:
            return sf
        if not sf:
            return ot
        if not sf[-1] < ot[0]:raise NotAscendError
        tree = _ops.mk_tree7chainLMR_(depth:=0, sf._t, '', ot._t)
        return AscendSet(_tree=tree)
    def copy(sf, /):
        return sf
    def issubset(sf, ot, /):
        return sf <= ot
    def issuperset(sf, ot, /):
        return sf >= ot
    def ascend_chain(sf, /, *ots):
        return sum(ots, sf) #sf + ot
    def difference(sf, /, *ots):
        for ot in ots:
            sf -= ot
        return sf
    def intersection(sf, /, *ots):
        for ot in ots:
            sf &= ot
        return sf
    def symmetric_difference(sf, /, *ots):
        for ot in ots:
            sf ^= ot
        return sf
    def union(sf, /, *ots):
        for ot in ots:
            sf |= ot
        return sf
    def __and__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        it = sf.reversed_iter_match_parts_of_(ot)
        commonsR = [payload[1] for case, payload in it if case == 2]
        777;commonsR.reverse()
        return sum(commonsR, _empty_set)
    def __or__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        it = sf.reversed_iter_match_parts_of_(ot)
        setsR = [(payload[1] if case == 2 else payload) for case, payload in it]
        777;setsR.reverse()
        return sum(setsR, _empty_set)
    def __xor__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        it = sf.reversed_iter_match_parts_of_(ot)
        noncommons = [payload for case, payload in it if not case == 2]
        777;noncommons.reverse()
        return sum(noncommons, _empty_set)
    def __sub__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        it = sf.reversed_iter_match_parts_of_(ot)
        left_onlys = [payload for case, payload in it if case == 0]
        777;left_onlys.reverse()
        return sum(left_onlys, _empty_set)
    def isdisjoint(sf, ot, /):
        if not type(ot) is type(sf): raise TypeError(type(ot), type(sf))
        if not (sf and ot):
            return True
        if sf[0] == ot[0]:
            return False
        if len(sf) == 1 == len(ot):
            return True
        it = sf._reversed_iter_match_parts_of_(ot, _isdisjoint__iter_common_suffix_)
        return not any(case==2 for (case, _) in it)
    def reversed_iter_match_parts_of_(sf, ot, /):
        '-> reversed-Iter part # [part == (left_only|common|right_only)][left_only == (0, set6sf)][right_only == (0, set6ot)][common == (2, (set6sf,set6ot))]'
        return sf._reversed_iter_match_parts_of_(ot, _default__iter_common_suffix_)
    def _reversed_iter_match_parts_of_(sf, ot, _iter_common_suffix_, /):
        if not type(ot) is type(sf): raise TypeError(type(ot), type(sf))
        #.(sz, tmay_common, sf, ot) = _cut_lcp(sf, ot, reverse=True)
        #.777;yield from tmay_common
        (sz, sf, ot) = yield from _iter_common_suffix_(sf, ot)
        777;case = 0
            # 0 - unknown nonempty, known no commom_suffix
            # 1 - known nonempty, bT_lt_aT
            # 2 - known nonempty, bT_gt_aT
        while 1:
          match case:
            case 0:
                # 0 - unknown nonempty, known no commom_suffix
                if not ot:
                    if sf:
                        yield (0, sf)
                    return
                elif not sf:
                    yield (1, ot)
                    return
                # [sf[-1] =!= ot[-1]]
                aT = sf[-1]
                bT = ot[-1]
                # [aT =!= bT]
                # known nonempty
                # known nonempty, known bT_ne_aT
                case = 1 if bT < aT else 2
                continue
            case 1:
                # 1 - known nonempty, bT_lt_aT
                # [bT < aT]
                (sf, sfR) = sf.split_at_key_(bT)
                777;del aT
                777;assert sfR
                777;yield (0, sfR)
                777;del sfR

                if not sf:
                    yield (1, ot)
                    break
                # [sf[-1] <= bT]
                (sz, sf, ot) = yield from _iter_common_suffix_(sf, ot)
                if sz:
                    case = 0
                    continue
                aT = sf[-1]
                # [aT < bT]
                777;case = 2
                continue
            case 2:
                # 2 - known nonempty, bT_gt_aT
                # [aT < bT]
                (ot, otR) = ot.split_at_key_(aT)
                777;del bT
                777;assert otR
                777;yield (1, otR)
                777;del otR

                if not ot:
                    yield (0, sf)
                    break
                # [ot[-1] <= aT]
                (sz, sf, ot) = yield from _iter_common_suffix_(sf, ot)
                if sz:
                    case = 0
                    continue
                bT = ot[-1]
                # [bT < aT]
                777;case = 1
                continue
            case _:
                raise 000
            #case
        #end-while 1:
        return
_empty_set = AscendSet()



def _isdisjoint__iter_common_suffix_(sf, ot, /):
    if sf and ot:
        aT = sf[-1]
        bT = ot[-1]
        if aT == bT:
            yield (2, ((sf, ot), (aT,bT)))
            raise 000
    return (0, sf, ot)
def _default__iter_common_suffix_(sf, ot, /):
    (sz, tmay_common, sf, ot) = _cut_lcp(sf, ot, reverse=True)
    777;yield from tmay_common
    return (sz, sf, ot)
def _len_lcp(lsA, lsB, /, *, reverse):
    f = reversed if reverse else iter
    itA = f(lsA)
    itB = f(lsB)
    sz = 0
    for a, b in zip(itA, itB):
        if not a == b:
            break
        sz += 1
    return sz
def _cut_lcp(lsA, lsB, /, *, reverse):
    sz = _len_lcp(lsA, lsB, reverse=reverse)
    if sz:
        if reverse:
            def f(sz, ls, /):
                return ls.split_at_(len(ls)-sz)[::-1]
            f
        else:
            def f(sz, ls, /):
                return ls.split_at_(sz)
            f
        f
        (cmA, lsA) = f(sz, lsA)
        (cmB, lsB) = f(sz, lsB)
        tmay_common  = [(2, (cmA, cmB))]
    else:
        tmay_common  = []
    tmay_common
    return (sz, tmay_common, lsA, lsB)


__all__
from seed.data_funcs.finger_tree.ft23_7sized_ascend_set import AscendSet, NotAscendError
from seed.data_funcs.finger_tree.ft23_7sized_ascend_set import *
