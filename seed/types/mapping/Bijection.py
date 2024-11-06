#__all__:goto
r'''[[[
e ../../python3_src/seed/types/mapping/Bijection.py
bijection bimapping
view ../../python3_src/seed/types/mapping/BidirectionReferenceManager.py

seed.types.mapping.Bijection
py -m nn_ns.app.debug_cmd   seed.types.mapping.Bijection -x
py -m nn_ns.app.doctest_cmd seed.types.mapping.Bijection:__doc__ -ht


[[
fwd:
    d[k]
bwd:
    d[:k]
d.fwd
d.bwd
    d(.bwd|.fwd)*
    -d
    +d

d.inv
    d(.inv)*
    ~d

]]




######################
######################
>>> d = Bijection({2:666}, {666:2})
>>> d
Bijection({2: 666}, {666: 2})
>>> bool(d)
True
>>> len(d)
1
>>> [*iter(d)]
[2]
>>> d.keys()
dict_keys([2])
>>> d.values()
dict_keys([666])
>>> d.items()
ItemsView(Bijection({2: 666}, {666: 2}))
>>> 1 in d
False
>>> 2 in d
True
>>> slice(None,666,None) in d
True
>>> slice(None,999,None) in d
False
>>> d[2]
666
>>> d[3]
Traceback (most recent call last):
    ...
KeyError: 3
>>> d[:666]
2
>>> d[:777]
Traceback (most recent call last):
    ...
KeyError: 777
>>> +d
_FwdBwdAble({2: 666}, {666: 2})
>>> -d
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> ~d
_BijectionInv(Bijection({2: 666}, {666: 2}))
>>> d.fwd
_FwdBwdAble({2: 666}, {666: 2})
>>> d.bwd
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> d.inv
_BijectionInv(Bijection({2: 666}, {666: 2}))
>>> d.fwd_keys()
dict_keys([2])
>>> d.bwd_keys()
dict_keys([666])




######################
######################
#>>> d.fwd_keys().remove(2)
#>>> d.bwd_keys().remove(666)
#>>> del d.fwd[2]
#>>> del d.bwd[666]
#>>> del d[2]
#>>> del d[:666]
#>>> del d.inv[:2]
#>>> del d.inv[666]

#
#>>> d.fwd_keys().add(3)
#>>> d.bwd_keys().add(999)
#>>> d.fwd[3] = 777
#>>> d.bwd[999] = 5
#>>> d[3] = 777
#>>> d[:999] = 5
#>>> d.inv[:3] = 777
#>>> d.inv[999] = 5


>>> d.fwd_keys().remove(2)
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'remove'
>>> d.bwd_keys().remove(666)
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'remove'
>>> del d.fwd[2]
Traceback (most recent call last):
    ...
TypeError: '_FwdBwdAble' object doesn't support item deletion
>>> del d.bwd[666]
Traceback (most recent call last):
    ...
TypeError: '_FwdBwdAbleInv' object doesn't support item deletion
>>> del d[2]
Traceback (most recent call last):
    ...
TypeError: 'Bijection' object doesn't support item deletion
>>> del d[:666] #'
Traceback (most recent call last):
    ...
TypeError: 'Bijection' object does not support item deletion
>>> del d.inv[:2]
Traceback (most recent call last):
    ...
TypeError: '_BijectionInv' object does not support item deletion
>>> del d.inv[666]
Traceback (most recent call last):
    ...
TypeError: '_BijectionInv' object doesn't support item deletion

>>> d.fwd_keys().add(3) #'
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'add'
>>> d.bwd_keys().add(999)
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'add'
>>> d.fwd[3] = 777
Traceback (most recent call last):
    ...
TypeError: '_FwdBwdAble' object does not support item assignment
>>> d.bwd[999] = 5
Traceback (most recent call last):
    ...
TypeError: '_FwdBwdAbleInv' object does not support item assignment
>>> d[3] = 777
Traceback (most recent call last):
    ...
TypeError: 'Bijection' object does not support item assignment
>>> d[:999] = 5
Traceback (most recent call last):
    ...
TypeError: 'Bijection' object does not support item assignment
>>> d.inv[:3] = 777
Traceback (most recent call last):
    ...
TypeError: '_BijectionInv' object does not support item assignment
>>> d.inv[999] = 5
Traceback (most recent call last):
    ...
TypeError: '_BijectionInv' object does not support item assignment






######################
######################
>>> d = Bijection({2:666}, {666:2})
>>> d.inv
_BijectionInv(Bijection({2: 666}, {666: 2}))
>>> bool(d.inv)
True
>>> len(d.inv)
1
>>> [*iter(d.inv)]
[666]
>>> d.inv.keys()
dict_keys([666])
>>> d.inv.values()
dict_keys([2])
>>> d.inv.items()
ItemsView(_BijectionInv(Bijection({2: 666}, {666: 2})))
>>> 999 in d.inv
False
>>> 666 in d.inv
True
>>> slice(None,2,None) in d.inv
True
>>> slice(None,1,None) in d.inv
False
>>> d.inv[666]
2
>>> d.inv[777]
Traceback (most recent call last):
    ...
KeyError: 777
>>> d.inv[:2]
666
>>> d.inv[:3]
Traceback (most recent call last):
    ...
KeyError: 3
>>> +d.inv
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> -d.inv
_FwdBwdAble({2: 666}, {666: 2})
>>> ~d.inv
Bijection({2: 666}, {666: 2})
>>> d.inv.fwd
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> d.inv.bwd
_FwdBwdAble({2: 666}, {666: 2})
>>> d.inv.inv
Bijection({2: 666}, {666: 2})
>>> d.inv.fwd_keys()
dict_keys([666])
>>> d.inv.bwd_keys()
dict_keys([2])






######################
######################
>>> d = Bijection({2:666}, {666:2})
>>> d.fwd
_FwdBwdAble({2: 666}, {666: 2})
>>> bool(d.fwd)
True
>>> len(d.fwd)
1
>>> [*iter(d.fwd)]
[2]
>>> d.fwd.keys()
dict_keys([2])
>>> d.fwd.values()
dict_keys([666])
>>> d.fwd.items()
ItemsView(_FwdBwdAble({2: 666}, {666: 2}))
>>> 1 in d.fwd
False
>>> 2 in d.fwd
True
>>> slice(None,666,None) in d.fwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'

>>> slice(None,999,None) in d.fwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'

>>> d.fwd[2]
666
>>> d.fwd[3]
Traceback (most recent call last):
    ...
KeyError: 3
>>> d.fwd[:666]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.fwd[:777]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> +d.fwd
_FwdBwdAble({2: 666}, {666: 2})
>>> -d.fwd
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> ~d.fwd
Traceback (most recent call last):
    ...
TypeError: bad operand type for unary ~: '_FwdBwdAble'
>>> d.fwd.fwd
_FwdBwdAble({2: 666}, {666: 2})
>>> d.fwd.bwd
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> d.fwd.inv
Traceback (most recent call last):
    ...
AttributeError: '_FwdBwdAble' object has no attribute 'inv'
>>> d.fwd.fwd_keys()
dict_keys([2])
>>> d.fwd.bwd_keys()
dict_keys([666])







######################
######################
>>> d = Bijection({2:666}, {666:2})
>>> d.bwd
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> bool(d.bwd)
True
>>> len(d.bwd)
1
>>> [*iter(d.bwd)]
[666]
>>> d.bwd.keys()
dict_keys([666])
>>> d.bwd.values()
dict_keys([2])
>>> d.bwd.items()
ItemsView(_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2})))
>>> 999 in d.bwd
False
>>> 666 in d.bwd
True
>>> slice(None,2,None) in d.bwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> slice(None,1,None) in d.bwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.bwd[666]
2
>>> d.bwd[777]
Traceback (most recent call last):
    ...
KeyError: 777
>>> d.bwd[:2]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.bwd[:3]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> +d.bwd
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> -d.bwd
_FwdBwdAble({2: 666}, {666: 2})
>>> ~d.bwd
Traceback (most recent call last):
    ...
TypeError: bad operand type for unary ~: '_FwdBwdAbleInv'
>>> d.bwd.fwd
_FwdBwdAbleInv(_FwdBwdAble({2: 666}, {666: 2}))
>>> d.bwd.bwd
_FwdBwdAble({2: 666}, {666: 2})
>>> d.bwd.inv
Traceback (most recent call last):
    ...
AttributeError: '_FwdBwdAbleInv' object has no attribute 'inv'
>>> d.bwd.fwd_keys()
dict_keys([666])
>>> d.bwd.bwd_keys()
dict_keys([2])



######################
######################
######################
######################
######################
######################
######################
######################
######################



######################
######################
>>> d = MutableBijection({2:666}, {666:2})
>>> d
MutableBijection({2: 666}, {666: 2})
>>> bool(d)
True
>>> len(d)
1
>>> [*iter(d)]
[2]
>>> d.keys()
dict_keys([2])
>>> d.values()
dict_keys([666])
>>> d.items()
ItemsView(MutableBijection({2: 666}, {666: 2}))
>>> 1 in d
False
>>> 2 in d
True
>>> slice(None,666,None) in d
True
>>> slice(None,999,None) in d
False
>>> d[2]
666
>>> d[3]
Traceback (most recent call last):
    ...
KeyError: 3
>>> d[:666]
2
>>> d[:777]
Traceback (most recent call last):
    ...
KeyError: 777
>>> +d
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> -d
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> ~d
_MutableBijectionInv(MutableBijection({2: 666}, {666: 2}))
>>> d.fwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> d.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> d.inv
_MutableBijectionInv(MutableBijection({2: 666}, {666: 2}))
>>> d.fwd_keys()
dict_keys([2])
>>> d.bwd_keys()
dict_keys([666])




######################
######################
#>>> d.fwd_keys().remove(2)
#>>> d.bwd_keys().remove(666)
#>>> del d.fwd[2]
#>>> del d.bwd[666]
#>>> del d[2]
#>>> del d[:666]
#>>> del d.inv[:2]
#>>> del d.inv[666]

#
#>>> d.fwd_keys().add(3)
#>>> d.bwd_keys().add(999)
#>>> d.fwd[3] = 777
#>>> d.bwd[999] = 5
#>>> d[3] = 777
#>>> d[:999] = 5
#>>> d.inv[:3] = 777
#>>> d.inv[999] = 5


>>> d.fwd_keys().remove(2)
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'remove'
>>> d.bwd_keys().remove(666)
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'remove'
>>> d = MutableBijection({2:666}, {666:2})
>>> d
MutableBijection({2: 666}, {666: 2})
>>> del d.fwd[2]
>>> d
MutableBijection({}, {})
>>> d = MutableBijection({2:666}, {666:2})
>>> del d.bwd[666]
>>> d
MutableBijection({}, {})
>>> d = MutableBijection({2:666}, {666:2})
>>> del d[2]
>>> d
MutableBijection({}, {})
>>> d = MutableBijection({2:666}, {666:2})
>>> del d[:666]
>>> d
MutableBijection({}, {})
>>> d = MutableBijection({2:666}, {666:2})
>>> del d.inv[:2]
>>> d
MutableBijection({}, {})
>>> d = MutableBijection({2:666}, {666:2})
>>> del d.inv[666]
>>> d
MutableBijection({}, {})
>>> d = MutableBijection({2:666}, {666:2})

>>> d.fwd_keys().add(3)
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'add'
>>> d.bwd_keys().add(999)
Traceback (most recent call last):
    ...
AttributeError: 'dict_keys' object has no attribute 'add'
>>> d.fwd[3] = 777
>>> d.bwd[999] = 5
>>> d[3] = 777
>>> d[:999] = 5
>>> d.inv[:3] = 777
>>> d.inv[999] = 5
>>> d == MutableBijection({2: 666, 3: 777, 5: 999}, {666: 2, 777: 3, 999: 5})
True
>>> del d[5]
>>> del d[:777]
>>> d
MutableBijection({2: 666}, {666: 2})





######################
######################
>>> d = MutableBijection({2:666}, {666:2})
>>> d.inv
_MutableBijectionInv(MutableBijection({2: 666}, {666: 2}))
>>> bool(d.inv)
True
>>> len(d.inv)
1
>>> [*iter(d.inv)]
[666]
>>> d.inv.keys()
dict_keys([666])
>>> d.inv.values()
dict_keys([2])
>>> d.inv.items()
ItemsView(_MutableBijectionInv(MutableBijection({2: 666}, {666: 2})))
>>> 999 in d.inv
False
>>> 666 in d.inv
True
>>> slice(None,2,None) in d.inv
True
>>> slice(None,1,None) in d.inv
False
>>> d.inv[666]
2
>>> d.inv[777]
Traceback (most recent call last):
    ...
KeyError: 777
>>> d.inv[:2]
666
>>> d.inv[:3]
Traceback (most recent call last):
    ...
KeyError: 3
>>> +d.inv
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> -d.inv
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> ~d.inv
MutableBijection({2: 666}, {666: 2})
>>> d.inv.fwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> d.inv.bwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> d.inv.inv
MutableBijection({2: 666}, {666: 2})
>>> d.inv.fwd_keys()
dict_keys([666])
>>> d.inv.bwd_keys()
dict_keys([2])






######################
######################
>>> d = MutableBijection({2:666}, {666:2})
>>> d.fwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> bool(d.fwd)
True
>>> len(d.fwd)
1
>>> [*iter(d.fwd)]
[2]
>>> d.fwd.keys()
dict_keys([2])
>>> d.fwd.values()
dict_keys([666])
>>> d.fwd.items()
ItemsView(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> 1 in d.fwd
False
>>> 2 in d.fwd
True
>>> slice(None,666,None) in d.fwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'

>>> slice(None,999,None) in d.fwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'

>>> d.fwd[2]
666
>>> d.fwd[3]
Traceback (most recent call last):
    ...
KeyError: 3
>>> d.fwd[:666]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.fwd[:777]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> +d.fwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> -d.fwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> ~d.fwd
Traceback (most recent call last):
    ...
TypeError: bad operand type for unary ~: '_MutableFwdBwdAble'
>>> d.fwd.fwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> d.fwd.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> d.fwd.inv
Traceback (most recent call last):
    ...
AttributeError: '_MutableFwdBwdAble' object has no attribute 'inv'
>>> d.fwd.fwd_keys()
dict_keys([2])
>>> d.fwd.bwd_keys()
dict_keys([666])







######################
######################
>>> d = MutableBijection({2:666}, {666:2})
>>> d.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> bool(d.bwd)
True
>>> len(d.bwd)
1
>>> [*iter(d.bwd)]
[666]
>>> d.bwd.keys()
dict_keys([666])
>>> d.bwd.values()
dict_keys([2])
>>> d.bwd.items()
ItemsView(_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2})))
>>> 999 in d.bwd
False
>>> 666 in d.bwd
True
>>> slice(None,2,None) in d.bwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> slice(None,1,None) in d.bwd
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.bwd[666]
2
>>> d.bwd[777]
Traceback (most recent call last):
    ...
KeyError: 777
>>> d.bwd[:2]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.bwd[:3]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> +d.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> -d.bwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> ~d.bwd
Traceback (most recent call last):
    ...
TypeError: bad operand type for unary ~: '_MutableFwdBwdAbleInv'
>>> d.bwd.fwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({2: 666}, {666: 2}))
>>> d.bwd.bwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> d.bwd.inv
Traceback (most recent call last):
    ...
AttributeError: '_MutableFwdBwdAbleInv' object has no attribute 'inv'
>>> d.bwd.fwd_keys()
dict_keys([666])
>>> d.bwd.bwd_keys()
dict_keys([2])












######################
######################

>>> d = MutableBijection({}, {})
>>> d
MutableBijection({}, {})
>>> d[2] = 666
>>> d
MutableBijection({2: 666}, {666: 2})
>>> d[:777] = 3
>>> d
MutableBijection({2: 666, 3: 777}, {666: 2, 777: 3})
>>> d[:666] = 3
>>> d
MutableBijection({3: 666}, {666: 3})
>>> del d[3]
>>> d
MutableBijection({}, {})
>>> d[:666] = 3
>>> d
MutableBijection({3: 666}, {666: 3})
>>> del d[:666]
>>> d
MutableBijection({}, {})


######################
######################

>>> d = MutableBijection({}, {})
>>> d.inv
_MutableBijectionInv(MutableBijection({}, {}))
>>> d.inv[2] = 666
>>> d.inv
_MutableBijectionInv(MutableBijection({666: 2}, {2: 666}))
>>> d.inv[:777] = 3
>>> d.inv
_MutableBijectionInv(MutableBijection({666: 2, 777: 3}, {2: 666, 3: 777}))
>>> d.inv[:666] = 3
>>> d.inv
_MutableBijectionInv(MutableBijection({666: 3}, {3: 666}))
>>> del d.inv[3]
>>> d.inv
_MutableBijectionInv(MutableBijection({}, {}))
>>> d.inv[:666] = 3
>>> d.inv
_MutableBijectionInv(MutableBijection({666: 3}, {3: 666}))
>>> del d.inv[:666]
>>> d.inv
_MutableBijectionInv(MutableBijection({}, {}))


######################
######################

>>> d = MutableBijection({}, {})
>>> d.fwd
_MutableFwdBwdAble({}, {})
>>> d.fwd[2] = 666
>>> d.fwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> d.fwd[:777] = 3
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.fwd
_MutableFwdBwdAble({2: 666}, {666: 2})
>>> del d.fwd[2]
>>> d.fwd
_MutableFwdBwdAble({}, {})


######################
######################

>>> d = MutableBijection({}, {})
>>> d.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({}, {}))
>>> d.bwd[2] = 666
>>> d.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({666: 2}, {2: 666}))
>>> d.bwd[:777] = 3
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> d.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({666: 2}, {2: 666}))
>>> del d.bwd[2]
>>> d.bwd
_MutableFwdBwdAbleInv(_MutableFwdBwdAble({}, {}))



######################
######################

py_adhoc_call   seed.types.mapping.Bijection   @f
#]]]'''
__all__ = r'''
Bijection
    MutableBijection
explain_hyperkey







IFwdBwdAble
    IMutableFwdBwdAble
    IBijection
        explain_hyperkey
        Bijection
        IMutableBijection
            MutableBijection
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from weakref import ref as wref_# WeakKeyDictionary as WkeyD, WeakValueDictionary as WvalD
from collections.abc import Mapping, MutableMapping
from seed.tiny_.check import check_type_is, check_type_le, check_non_ABC, check_int_ge, check_int_ge_lt
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper

___end_mark_of_excluded_global_names__0___ = ...


class IFwdBwdAble(Mapping, ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def fwd(sf, /):
        '-> IFwdBwdAble'
    @property
    @abstractmethod
    def bwd(sf, /):
        '-> IFwdBwdAble'
    def __pos__(sf, /):
        '-> IFwdBwdAble'
        return sf.fwd
    def __neg__(sf, /):
        '-> IFwdBwdAble'
        return sf.bwd
    def fwd_keys(sf, /):
        '-> view {fk}'
        return sf.fwd.keys()
    def bwd_keys(sf, /):
        '-> view {bk}'
        return sf.bwd.keys()
class IMutableFwdBwdAble(MutableMapping, IFwdBwdAble):
    __slots__ = ()

class IBijection(IFwdBwdAble):
    __slots__ = ()
    @property
    @abstractmethod
    def inv(sf, /):
        '-> IBijection'
    def __invert__(sf, /):
        '-> IBijection'
        return sf.inv
    #def fwd_get(sf, fk, /):
    #    'fk -> bk|^KeyError'
    #    return sf.fwd[fk]
    #def bwd_get(sf, bk, /):
    #    'bk -> fk|^KeyError'
    #    return sf.bwd[bk]
    #def fwd_keys(sf, /):
    #    '-> view {fk}'
    #    return sf.fwd.keys()
    #def bwd_keys(sf, /):
    #    '-> view {bk}'
    #    return sf.bwd.keys()

    @override
    def __iter__(sf, /):
        '-> view {fk}'
        return iter(sf.fwd)
    @override
    def __len__(sf, /):
        '-> view {fk}'
        return len(sf.fwd)
    @override
    def keys(sf, /):
        '-> view {fk}'
        return sf.fwd_keys()
    @override
    def values(sf, /):
        '-> view {bk}'
        return sf.bwd_keys()
    @override
    def __contains__(sf, k, /):
        '(fk|slice(None,bk,None)) -> bool'
        (fk_vs_bk, fk_or_bk) = explain_hyperkey(k)
        if fk_vs_bk:
            bk = fk_or_bk
            return bk in sf.bwd
        else:
            fk = fk_or_bk
            return fk in sf.fwd
    @override
    def __getitem__(sf, k, /):
        '(fk|slice(None,bk,None)) -> (bk|fk)'
        (fk_vs_bk, fk_or_bk) = explain_hyperkey(k)
        if fk_vs_bk:
            bk = fk_or_bk
            return sf.bwd[bk]
        else:
            fk = fk_or_bk
            return sf.fwd[fk]
def explain_hyperkey(k, /):
    '(fk|slice(None,bk,None)) -> (fk_vs_bk, (fk|bk))'
    if type(k) is slice:
        if not k.start is None:raise Exception
        if not k.step is None:raise Exception
        bk = k.stop
        fk_vs_bk = True#is_bwd_key
        fk_or_bk = bk
    else:
        fk = k
        fk_vs_bk = False#not is_bwd_key
        fk_or_bk = fk
    return (fk_vs_bk, fk_or_bk)


class IMutableBijection(IMutableFwdBwdAble, IBijection):
    __slots__ = ()
    @override
    def __delitem__(sf, k, /):
        '(fk|slice(None,bk,None)) -> None'
        (fk_vs_bk, fk_or_bk) = explain_hyperkey(k)
        if fk_vs_bk:
            bk = fk_or_bk
            #_delitem1(sf.bwd, sf.fwd, bk)
            del sf.bwd[bk]
                # since bwd known fwd
        else:
            fk = fk_or_bk
            #_delitem1(sf.fwd, sf.bwd, fk)
            del sf.fwd[fk]
                # since fwd known bwd
    @override
    def __setitem__(sf, k, v, /):
        '(fk|slice(None,bk,None)) -> (bk|fk) -> None'
        (fk_vs_bk, fk_or_bk) = explain_hyperkey(k)
        if fk_vs_bk:
            bk = fk_or_bk
            fk = v
        else:
            fk = fk_or_bk
            bk = v
        #bug:_setitem2(sf.fwd, sf.bwd, fk, bk)
        #   since fwd known bwd
        sf.fwd[fk] = bk

class _FwdBwdAbleInv(IFwdBwdAble):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._inv)
    def __init__(sf, fwbw, /):
        sf._inv = fwbw
    @property
    @override
    def fwd(sf, /):
        '-> IFwdBwdAble'
        return sf
    @property
    @override
    def bwd(sf, /):
        '-> IFwdBwdAble'
        return sf._inv
    @override
    def keys(sf, /):
        '-> view {fk}'
        return sf._inv.values()
    @override
    def values(sf, /):
        '-> view {bk}'
        return sf._inv.keys()
    @override
    def __contains__(sf, fk, /):
        'fk -> bool'
        return fk in sf._inv._bd
    @override
    def __getitem__(sf, fk, /):
        'fk -> bk'
        return sf._inv._bd[fk]
    @override
    def __iter__(sf, /):
        '-> view {fk}'
        return iter(sf._inv._bd)
    @override
    def __len__(sf, /):
        return len(sf._inv)
check_non_ABC(_FwdBwdAbleInv)


class _FwdBwdAble(IFwdBwdAble):
    ___no_slots_ok___ = True
    _InvT_ = _FwdBwdAbleInv
    def __repr__(sf, /):
        return repr_helper(sf, sf._fd, sf._bd)
    def __init__(sf, fd, bd, /):
        sf._fd = fd
        sf._bd = bd
        sf._winv = None
            #weakref
    @property
    @override
    def fwd(sf, /):
        '-> IFwdBwdAble'
        return sf
    @property
    @override
    def bwd(sf, /):
        '-> IFwdBwdAble'
        if sf._winv:
            m = sf._winv()
            if not m is None:
                return m
        inv = type(sf)._InvT_(sf)
        sf._winv = wref_(inv)
        return inv
    @override
    def keys(sf, /):
        '-> view {fk}'
        return sf._fd.keys()
    @override
    def values(sf, /):
        '-> view {bk}'
        return sf._bd.keys()
    @override
    def __contains__(sf, fk, /):
        'fk -> bool'
        return fk in sf._fd
    @override
    def __getitem__(sf, fk, /):
        'fk -> bk'
        return sf._fd[fk]
    @override
    def __iter__(sf, /):
        '-> view {fk}'
        return iter(sf._fd)
    @override
    def __len__(sf, /):
        return len(sf._fd)
check_non_ABC(_FwdBwdAble)

class _BijectionInv(IBijection):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, sf._bi)
    def __init__(sf, bijection, /):
        sf._bi = bijection
    @property
    @override
    def inv(sf, /):
        '-> IBijection'
        return sf._bi
    @property
    @override
    def fwd(sf, /):
        '-> IFwdBwdAble'
        return sf._bi.bwd
    @property
    @override
    def bwd(sf, /):
        '-> IFwdBwdAble'
        return sf._bi.fwd
check_non_ABC(_BijectionInv)

class Bijection(IBijection):
    ___no_slots_ok___ = True
    _InvT_ = _BijectionInv
    _FwdT_ = _FwdBwdAble
    def __repr__(sf, /):
        return repr_helper(sf, sf._fd, sf._bd)
    def __init__(sf, fd, bd, /):
        sf._fd = fd
        sf._bd = bd
        sf._wf = sf._wb = sf._winv = None
            #weakref
        sf.bwd
        assert sf._wf
        assert sf._wb
    @property
    @override
    def inv(sf, /):
        '-> IBijection'
        if sf._winv:
            m = sf._winv()
            if not m is None:
                return m
        inv = type(sf)._InvT_(sf)
        sf._winv = wref_(inv)
        return inv
    @property
    @override
    def fwd(sf, /):
        '-> IFwdBwdAble'
        if sf._wf:
            m = sf._wf()
            if not m is None:
                return m
        fw = type(sf)._FwdT_(sf._fd, sf._bd)
        sf._wf = wref_(fw)
        return fw

    @property
    @override
    def bwd(sf, /):
        '-> IFwdBwdAble'
        if sf._wb:
            m = sf._wb()
            if not m is None:
                return m
        bw = sf.fwd.bwd
        sf._wb = wref_(bw)
        return bw

check_non_ABC(Bijection)




class _MutableFwdBwdAbleInv(_FwdBwdAbleInv, IMutableFwdBwdAble):
    ___no_slots_ok___ = True
    @override
    def __delitem__(sf, fk, /):
        'fk -> None'
        bk = sf[fk]
        del sf._inv[bk]
    @override
    def __setitem__(sf, fk, bk, /):
        'fk -> bk -> None'
        sf._inv[bk] = fk
class _MutableFwdBwdAble(_FwdBwdAble, IMutableFwdBwdAble):
    ___no_slots_ok___ = True
    _InvT_ = _MutableFwdBwdAbleInv
    @override
    def __delitem__(sf, fk, /):
        'fk -> None'
        _delitem1(sf._fd, sf._bd, fk)
    @override
    def __setitem__(sf, fk, bk, /):
        'fk -> bk -> None'
        _setitem2(sf._fd, sf._bd, fk, bk)
def _delitem1(fd, bd, fk, /):
    bk = fd.pop(fk)
    del bd[bk]
def _setitem2(fd, bd, fk, bk, /):
    _discard2(fd, bd, fk, bk)
    fd[fk] = bk
    bd[bk] = fk
def _discard2(fd, bd, fk, bk, /):
    _discard1(fd, bd, fk)
    _discard1(bd, fd, bk)
def _discard1(fd, bd, fk, /):
    try:
        bk = fd.pop(fk)
    except KeyError:
        pass
    else:
        _fk = bd.pop(bk)
        assert _fk == fk



class _MutableBijectionInv(_BijectionInv, IMutableBijection):
    ___no_slots_ok___ = True
class MutableBijection(Bijection, IMutableBijection):
    ___no_slots_ok___ = True
    _InvT_ = _MutableBijectionInv
    _FwdT_ = _MutableFwdBwdAble




__all__
from seed.types.mapping.Bijection import Bijection, MutableBijection
from seed.types.mapping.Bijection import explain_hyperkey
from seed.types.mapping.Bijection import *
