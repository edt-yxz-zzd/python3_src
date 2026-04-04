#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_eqv_set.py
    slow:__contains__:O(N)
view ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_ascend_set.py

seed.data_funcs.finger_tree.ft23_7sized_eqv_set
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.ft23_7sized_eqv_set -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.ft23_7sized_eqv_set:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.finger_tree.ft23_7sized_eqv_set:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######

[[
slow:__contains__:O(N)
SlowSet used in HashSet:
    [HashSet{k} == (sz, AscendMap{hash{k}:SlowSet{k}})]
    [SlowMap{k:v} == SlowSet{HashEqOnlyFst(k,v)}]
SlowMap used in HashMap:
    [HashMap{k:v} == (sz, AscendMap{hash{k}:SlowMap{k:v}})]
]]


'#'; __doc__ = r'#'
>>> SlowSet()
SlowSet()
>>> SlowSet([1, 2])
SlowSet([1, 2])
>>> SlowSet([1, True, 2])
SlowSet([True, 2])


>>> len(SlowSet([1, 2]))
2
>>> [*iter(SlowSet([1, 2]))]
[1, 2]
>>> [*reversed(SlowSet([1, 2]))]
[2, 1]

>>> SlowSet([1, 4, 5, False]).find(5)
2
>>> SlowSet([1, 4, 5, False]).find(3)
-1
>>> SlowSet([1, 4, 5, False]).find_ex(0)
(3, False)
>>> SlowSet([1, 4, 5, False]).find_ex(5)
(2, 5)
>>> SlowSet([1, 4, 5, False]).find_ex(3)
(-1, None)


ipop
vpop
iput
vput
iremove
vremove
idiscard
vdiscard
wdiscard

>>> SlowSet([1, 4, 5, False]).ipop()
SlowSet([4, 5, False])
>>> SlowSet([1, 4, 5, False]).vpop()
(1, SlowSet([4, 5, False]))
>>> SlowSet().ipop()
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23.EmptyError
>>> SlowSet().vpop()
Traceback (most recent call last):
    ...
seed.data_funcs.finger_tree.ft23.EmptyError

>>> SlowSet([1, 4, 5, False]).vput(5)
((5,), SlowSet([1, 4, 5, False]))
>>> SlowSet([1, 4, 5, False]).vput(0)
((False,), SlowSet([1, 4, 5, 0]))
>>> SlowSet([1, 4, 5, False]).vput(0, no_overwrite=True)
((False,), SlowSet([1, 4, 5, False]))
>>> SlowSet([1, 4, 5, False]).vput(3)
((), SlowSet([3, 1, 4, 5, False]))

>>> SlowSet([1, 4, 5, False]).iremove(5)
SlowSet([1, 4, False])
>>> SlowSet([1, 4, 5, False]).iremove(0)
SlowSet([1, 4, 5])
>>> SlowSet([1, 4, 5, False]).iremove(3)
Traceback (most recent call last):
    ...
LookupError: 3

>>> SlowSet([1, 4, 5, False]).vremove(5)
(5, SlowSet([1, 4, False]))
>>> SlowSet([1, 4, 5, False]).vremove(0)
(False, SlowSet([1, 4, 5]))
>>> SlowSet([1, 4, 5, False]).vremove(3)
Traceback (most recent call last):
    ...
LookupError: 3

>>> SlowSet([1, 4, 5, False]).idiscard(5)
SlowSet([1, 4, False])
>>> SlowSet([1, 4, 5, False]).idiscard(0)
SlowSet([1, 4, 5])
>>> SlowSet([1, 4, 5, False]).idiscard(3)
SlowSet([1, 4, 5, False])

>>> SlowSet([1, 4, 5, False]).vdiscard(5)
((5,), SlowSet([1, 4, False]))
>>> SlowSet([1, 4, 5, False]).vdiscard(0)
((False,), SlowSet([1, 4, 5]))
>>> SlowSet([1, 4, 5, False]).vdiscard(3)
((), SlowSet([1, 4, 5, False]))

>>> SlowSet([1, 4, 5, False]).wdiscard(5)
((5,), 2, SlowSet([1, 4, False]))
>>> SlowSet([1, 4, 5, False]).wdiscard(0)
((False,), 3, SlowSet([1, 4, 5]))
>>> SlowSet([1, 4, 5, False]).wdiscard(3)
((), -1, SlowSet([1, 4, 5, False]))


__contains__
__hash__
__eq__
__le__
>>> 5 in SlowSet([1, 4, 5, False])
True
>>> 0 in SlowSet([1, 4, 5, False])
True
>>> 3 in SlowSet([1, 4, 5, False])
False

>>> hash(SlowSet([1, 4, 5, False])) #doctest: +SKIP
-822104621371385620
>>> hash(SlowSet([1, 4, 5, False])) == hash(SlowSet([0, 4, True, 5]))
True
>>> {SlowSet([1, 4, 5, False])}
{SlowSet([1, 4, 5, False])}
>>> SlowSet([0, 4, True, 5]) in {SlowSet([1, 4, 5, False])}
True

>>> SlowSet([1, 4, 5, False]) == SlowSet([0, 4, True, 5])
True
>>> SlowSet([1, 4, 5, False]) == SlowSet([0, 4, True, 6])
False
>>> SlowSet([1, 4, 5, False]) == SlowSet([0, 4, True])
False


>>> SlowSet([1, 4, 5, False]) <= SlowSet([0, 4, True, 5])
True
>>> SlowSet([1, 4, 5, False]) >= SlowSet([0, 4, True, 5])
True
>>> SlowSet([1, 4, 5, False]) < SlowSet([0, 4, True, 5])
False
>>> SlowSet([1, 4, 5, False]) > SlowSet([0, 4, True, 5])
False

>>> SlowSet([1, 4, 5, False]) <= SlowSet([0, 4, True])
False
>>> SlowSet([1, 4, 5, False]) < SlowSet([0, 4, True])
False
>>> SlowSet([1, 4, 5, False]) >= SlowSet([0, 4, True])
True
>>> SlowSet([1, 4, 5, False]) > SlowSet([0, 4, True])
True

>>> SlowSet([1, 4, 5, False]) <= SlowSet([0, 4, True, 6])
False
>>> SlowSet([1, 4, 5, False]) >= SlowSet([0, 4, True, 6])
False
>>> SlowSet([1, 4, 5, False]) < SlowSet([0, 4, True, 6])
False
>>> SlowSet([1, 4, 5, False]) > SlowSet([0, 4, True, 6])
False




__and__
__or__
__xor__
__sub__
>>> SlowSet([1, 4, 5, False]) & SlowSet([0, 4, True, 6])
SlowSet([0, 4, True])
>>> SlowSet([1, 4, 5, False]) | SlowSet([0, 4, True, 6])
SlowSet([5, 0, 4, True, 6])
>>> SlowSet([1, 4, 5, False]) ^ SlowSet([0, 4, True, 6])
SlowSet([5, 6])
>>> SlowSet([1, 4, 5, False]) - SlowSet([0, 4, True, 6])
SlowSet([5])



copy
issubset
issuperset
difference
intersection
symmetric_difference
union
isdisjoint
>>> s=SlowSet([1, 4, 5, False]); s.copy() is s
True

>>> SlowSet([1, 4, 5, False]).issubset(SlowSet([0, 4, True]))
False
>>> SlowSet([1, 4, 5, False]).issubset(SlowSet([1, 4, 5, False]))
True
>>> SlowSet([0, 4, True]).issubset(SlowSet([1, 4, 5, False]))
True

>>> SlowSet([1, 4, 5, False]).issuperset(SlowSet([0, 4, True]))
True
>>> SlowSet([1, 4, 5, False]).issuperset(SlowSet([1, 4, 5, False]))
True
>>> SlowSet([0, 4, True]).issuperset(SlowSet([1, 4, 5, False]))
False


>>> SlowSet([1, 4, 5, False]).intersection(SlowSet([0, 4, True, 6]))
SlowSet([0, 4, True])
>>> SlowSet([1, 4, 5, False]).union(SlowSet([0, 4, True, 6]))
SlowSet([5, 0, 4, True, 6])
>>> SlowSet([1, 4, 5, False]).symmetric_difference(SlowSet([0, 4, True, 6]))
SlowSet([5, 6])
>>> SlowSet([1, 4, 5, False]).difference(SlowSet([0, 4, True, 6]))
SlowSet([5])


>>> SlowSet([1, 4, 5, False]).isdisjoint(SlowSet([0, 4, True]))
False
>>> SlowSet([1, 4, 5, False]).isdisjoint(SlowSet([0, 44]))
False
>>> SlowSet([1, 4, 5]).isdisjoint(SlowSet([0, 44]))
True

>>> print('\n'.join(vars(SlowSet).keys()))
__module__
__doc__
___no_slots_ok___
__new__
from_iterable
from_iterable7no_dup
_sz
__repr__
__len__
__iter__
__reversed__
find
find_ex
ipop
vpop
iput
vput
iremove
vremove
idiscard
vdiscard
wdiscard
__contains__
_hash
__hash__
__eq__
__ne__
__le__
__lt__
__gt__
__ge__
copy
issubset
issuperset
difference
intersection
symmetric_difference
union
__and__
__or__
__xor__
__sub__
isdisjoint
__dict__
__weakref__
__abstractmethods__
_abc_impl


py_adhoc_call   seed.data_funcs.finger_tree.ft23_7sized_eqv_set   @f
]]]'''#'''
__all__ = r'''
SlowSet
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from collections.abc import Set as ISet
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.data_funcs.finger_tree.ft23_7sized_seq import Seq, xorhash5ft_seq_
    from seed.helper.repr_input import repr_helper
    from functools import cached_property
    #.from seed.seq_tools.find import find7seq_
    from seed.seq_tools.force_reversed import force_reversed as _force_reversed
___end_mark_of_excluded_global_names__0___ = ...


__all__










class SlowSet(ISet):
    'slow:__contains__:O(N)'
    ___no_slots_ok___ = True
    def __new__(cls, xs=None, /, *, no_dup=False):
        if cls is type(xs):
            sf = xs
            return sf

        if xs is None:
            no_dup = True
            xs = ()
        elif isinstance(xs, __class__):
            no_dup = True
            xs = xs._zs

        if not no_dup:
            ys = []
            dup = False
            #.for x in xs:
            #.    if not -1 == (j:=find7seq_(ys, x)):
            #.        dup = True
            #.        ys[j] = x
            #.    else:
            #.        ys.append(x)
            #.dup, ys
            for x in _force_reversed(xs):
                if x in ys:
                    dup = True
                else:
                    ys.append(x)
            else:
                ys.reverse()
            dup, ys
        else:
            dup = False
            ys = xs
        dup, ys

        if not dup and isinstance(xs, Seq):
            zs = xs
        else:
            zs = Seq(ys)
        zs

        if not zs and cls is __class__:
            try:
                return _empty_set
            except NameError:
                pass


        sf = super(__class__, cls).__new__(cls)
        sf._zs = zs
        return sf
    @classmethod
    def from_iterable(cls, xs, /, *, no_dup=False):
        return cls(xs, no_dup=no_dup)
    @classmethod
    def from_iterable7no_dup(cls, xs, /):
        return cls.from_iterable(xs, no_dup=True)
    @cached_property
    def _sz(sf, /):
        return len(sf._zs)
    def __repr__(sf, /):
        xs = [*sf]
        if xs:
            return repr_helper(sf, xs)
        return repr_helper(sf)
    def __len__(sf, /):
        return sf._sz
    def __iter__(sf, /):
        return iter(sf._zs)
    def __reversed__(sf, /):
        return reversed(sf._zs)
    #.def __getitem__(sf, k, /):
    #.    'used by SlowMap'
    #.    match sf.find_ex(k):
    #.        case (-1, None):
    #.            raise KeyError(k)
    #.        case (j, _k):
    #.            return _k
    def find(sf, k, /):
        'O(N) => k -> imay_idx'
        return sf.find_ex(k)[0]
    def find_ex(sf, k, /):
        'O(N) => k -> (imay_idx, may_k) #used by SlowMap'
        ks = [k]
        for j, _k in enumerate(sf):
            if _k in ks:
                return (j, _k)
        return (-1, None)
    def ipop(sf, /):
        '-> set | ^EmptyError'
        return sf.vpop()[1]
    def vpop(sf, /):
        '-> (k, set) | ^EmptyError'
        k, zs = sf._zs.vpopL()
            # ^EmptyError
        ot = type(sf).from_iterable7no_dup(zs)
        return (k, ot)
    def iput(sf, x, /, *, no_overwrite=False):
        '-> set'
        return sf.vput(x, no_overwrite=no_overwrite)[1]
    def vput(sf, x, /, *, no_overwrite=False):
        '-> (tmay_hit, set)'
        match sf.find_ex(x):
            case (-1, None):
                zs = sf._zs.ipushL(x)
                ot = type(sf).from_iterable7no_dup(zs)
                tmay_hit = ()
            case (j, _k):
                tmay_hit = (_k,)
                if no_overwrite or x is _k:
                    ot = sf
                else:
                    zs = sf._zs.isetitem_(j, x)
                    ot = type(sf).from_iterable7no_dup(zs)
                ot
        return (tmay_hit, ot)
    def iremove(sf, x, /):
        '-> set | ^LookupError'
        return sf.vremove(x)[1]
    def vremove(sf, x, /):
        '-> (old_x, set) | ^LookupError'
        (tmay_hit, ot) = sf.vdiscard(x)
        if not tmay_hit:
            raise LookupError(x)
        [old_x] = tmay_hit
        return (old_x, ot)
    def idiscard(sf, x, /):
        '-> set # see:iremove()'
        return sf.vdiscard(x)[1]
    def vdiscard(sf, x, /):
        '-> (tmay_hit, set) # see:vremove()'
        (tmay_hit, imay_j, ot) = sf.wdiscard(x)
        return (tmay_hit, ot)
    def wdiscard(sf, x, /):
        '-> (tmay_hit, imay_idx, set) # see:vremove()'
        match sf.find_ex(x):
            case (-1, None):
                ot = sf
                tmay_hit = ()
                imay_j = -1
            case (j, _k):
                imay_j = j
                tmay_hit = (_k,)
                zs = sf._zs.ipop_at_(j)
                ot = type(sf).from_iterable7no_dup(zs)
        return (tmay_hit, imay_j, ot)
    def __contains__(sf, x, /):
        'O(N) => k -> bool'
        return not -1 == sf.find(x)
    @cached_property
    def _hash(sf, /):
        #bug:h = hash(sf._zs)
        h = xorhash5ft_seq_(sf._zs)
        return hash((type(sf), h))
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
        #xxx:return all(a == b for a, b in zip(sf, ot))
        return all(b in sf for b in ot)
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

    def copy(sf, /):
        return sf
    def issubset(sf, ot, /):
        return sf <= ot
    def issuperset(sf, ot, /):
        return sf >= ot
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
        if 0:
            if len(ot) > len(sf):
                sf, ot = ot, sf
            assert len(ot) <= len(sf)
        commonR = (x for x in ot if x in sf)
        return type(sf).from_iterable7no_dup(commonR)
    def __or__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        #onlyL = (x for x in sf if not x in ot)
        onlyL = sf -ot
        #ot._zs.ipushsL(onlyL, reverse=False)
        return _add_(onlyL, ot)
        return onlyL | ot
        return onlyL + ot
    def __xor__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        onlyL = sf -ot
        onlyR = ot -sf
        return _add_(onlyL, onlyR)
        return onlyL | onlyR
        return onlyL + onlyR
    def __sub__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        for x in ot:
            sf = sf.idiscard(x)
        return sf
    def isdisjoint(sf, ot, /):
        if not type(ot) is type(sf): raise TypeError(type(ot), type(sf))
        if not (sf and ot):
            return True
        return not any(x in sf for x in ot)
_empty_set = SlowSet()

def _add_(sf, ot, /):
    'preconditon: [sf&ot == {/}]'
    #__add__
    if not type(ot) is type(sf):
        return NotImplemented

    if not ot:
        return sf
    if not sf:
        return ot
    zs = sf._zs + ot._zs
    return type(sf).from_iterable7no_dup(zs)










__all__
from seed.data_funcs.finger_tree.ft23_7sized_eqv_set import SlowSet
from seed.data_funcs.finger_tree.ft23_7sized_eqv_set import *
