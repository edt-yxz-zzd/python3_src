#__all__:goto
r'''[[[
e ../../python3_src/seed/types/mapping/symbolize.py
used in:
    view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py
        to symbolize exconfigpack

seed.types.mapping.symbolize
py -m nn_ns.app.debug_cmd   seed.types.mapping.symbolize -x
py -m nn_ns.app.doctest_cmd seed.types.mapping.symbolize:__doc__ -ht


[[
symbolize ~ tokenize
no word:『symbolify』
    # ~ sympify@sympy # vs simplify(<--simple)

]]
[[
intent:
    using a symbol(token) to stand for big frozen hashable obj
        persistent_singleton_checked_standardized_hashable
]]
[[
]]


######################
>>> from weakref import ref


######################
######################
>>> wd = WeakSymbolizeRegister()
>>> wd #doctest: +ELLIPSIS
WeakSymbolizeRegister(<WeakKeyDictionary at 0x...>, <WeakValueDictionary at 0x...>)
>>> k = wd.symbolize([])
>>> wd.lookup(k)
()
>>> k is wd.symbolize([])
True

>>> v = _Symbol()
>>> k = wd.symbolize(v)
>>> k is not v
True
>>> wd.lookup(k) is v
True
>>> k is wd.symbolize(v)
True
>>> wv = ref(v)
>>> del v
>>> wv() is not None
True
>>> del k
>>> wv() is None
True


######################
######################
>>> pd = PersistentSymbolizeRegister()
>>> pd
PersistentSymbolizeRegister({}, {})
>>> k = pd.symbolize([])
>>> pd.lookup(k)
()
>>> k is pd.symbolize([])
True

>>> v = _Symbol()
>>> k = pd.symbolize(v)
>>> k is not v
True
>>> pd.lookup(k) is v
True
>>> k is pd.symbolize(v)
True
>>> wv = ref(v)
>>> del v
>>> wv() is not None
True
>>> del k
>>> wv() is not None #diff vs:wd
True





######################
######################
>>> class SymbolizeRegister__subset__int_only(ISymbolizeRegister__subset):
...     ___no_slots_ok___ = True
...     @override
...     def _check_value__more_(sf, val, /):
...         '[backgroud_symbolizer checked]=>val/hashable -> None|^Exception'
...         check_type_is(int, val)

>>> pd = PersistentSymbolizeRegister()
>>> jpd = SymbolizeRegister__subset__int_only(pd)
>>> jpd
SymbolizeRegister__subset__int_only(PersistentSymbolizeRegister({}, {}))

>>> len_ = lambda jpd:len(jpd._s)


#fg-new:999
>>> jpd.backgroud_symbolizer
PersistentSymbolizeRegister({}, {})
>>> len_(jpd)
0
>>> k999 = jpd.symbolize(999)
>>> len_(jpd)
1
>>> pd  #doctest: +ELLIPSIS
PersistentSymbolizeRegister({<seed.types.mapping.symbolize._Symbol object at 0x...>: 999}, {999: <seed.types.mapping.symbolize._Symbol object at 0x...>})
>>> k999 is jpd.symbolize(999)
True
>>> 999 == jpd.lookup(k999)
True
>>> len_(jpd)
1
>>> 999 == pd.lookup(k999)
True
>>> k999 is pd.symbolize(999)
True

#new5bg:666
>>> len_(jpd)
1
>>> k666 = pd.symbolize(666)
>>> len_(jpd)
1
>>> k666 is pd.symbolize(666)
True
>>> 666 == pd.lookup(k666)
True
>>> len_(jpd)
1
>>> 666 == jpd.lookup(k666) #new5bg 333:_inv_lookup_() after lookup()
True
>>> len_(jpd)
2
>>> k666 is jpd.symbolize(666)
True
>>> len_(jpd)
2

#new5bg:333
>>> len_(jpd)
2
>>> k333 = pd.symbolize(333)
>>> len_(jpd)
2
>>> k333 is jpd.symbolize(333) #new5bg 333:_inv_lookup_() before lookup()
True
>>> len_(jpd)
3
>>> 333 == jpd.lookup(k333)
True
>>> len_(jpd)
3



#fg-bad:'000'
>>> v000 = '000'
>>> len_(jpd)
3
>>> jpd.symbolize(v000)
Traceback (most recent call last):
    ...
TypeError: <class 'str'>
>>> len_(jpd)
3


#bad5bg:'111'
>>> v111 = '111'
>>> k111 = pd.symbolize(v111)
>>> v111 == pd.lookup(k111)
True
>>> len_(jpd)
3
>>> jpd.lookup(k111) # _inv_lookup_() after lookup()
Traceback (most recent call last):
    ...
TypeError: <class 'str'>
>>> len_(jpd)
3
>>> jpd.symbolize(v111)
Traceback (most recent call last):
    ...
TypeError: <class 'str'>
>>> len_(jpd)
3

#bad5bg:b'222'
>>> v222 = b'222'
>>> k222 = pd.symbolize(v222)
>>> v222 == pd.lookup(k222)
True
>>> k222 is pd.symbolize(bytearray(v222))
True
>>> len_(jpd)
3
>>> jpd.symbolize(v222) # _inv_lookup_() before lookup()
Traceback (most recent call last):
    ...
TypeError: <class 'bytes'>
>>> len_(jpd)
3
>>> jpd.lookup(k222)
Traceback (most recent call last):
    ...
TypeError: <class 'bytes'>
>>> len_(jpd)
3



######################
######################


#]]]'''
__all__ = r'''

default_standardize_
WeakSymbolizeRegister
PersistentSymbolizeRegister
ISymbolizeRegister__subset













default_standardize_
ISymbolizeRegister
    ISymbolizeRegister__subset
    ISymbolizeRegister__using_default_standardize
    ISymbolizeRegister__typed
        IWeakSymbolizeRegister
            WeakSymbolizeRegister
        IPersistentSymbolizeRegister
            PersistentSymbolizeRegister
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from weakref import WeakKeyDictionary, WeakValueDictionary, WeakSet



from seed.tiny_.std_mk_hashable_ import std_mk_hashable_
from seed.tiny_.check import check_type_is, check_type_le
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...


class ISymbolizeRegister(ABC):
    'persistent_singleton_checked_standardized_hashable'
    __slots__ = ()
    @property
    @abstractmethod
    def whether_weakref(sf, /):
        '-> bool #whether cache only weakref of sym: WeakKeyDictionary<sym,val>, WeakValueDictionary<val,sym>'
    @abstractmethod
    def _standardize_(sf, obj, /):
        'obj -> val/hashable{unchecked yet} #eg: set->frozenset #eg:default_standardize_()'
    @abstractmethod
    def _check_value_(sf, val, /):
        'val/hashable -> None|^Exception'
    @abstractmethod
    def _inv_lookup_(sf, val, /):
        'val -> sym|^LookupError'
    @abstractmethod
    def _register_(sf, val, /):
        '[after ._check_value_(val)]=>val -> sym #not existed yet'
    @abstractmethod
    def lookup(sf, sym, /):
        'sym -> val/hashable|^LookupError'
    def symbolize(sf, obj, /):
        'obj -> sym #ie:register'
        val = sf._standardize_(obj)
        try:
            return sf._inv_lookup_(val)
        except LookupError:
            pass
        sf._check_value_(val)
        return sf._register_(val)

class ISymbolizeRegister__subset(ISymbolizeRegister):
    '_check_value__more_:to ensure subset #depend on a global backgroud ISymbolizeRegister'
    __slots__ = ()
    @abstractmethod
    def _check_value__more_(sf, val, /):
        '[backgroud_symbolizer checked]=>val/hashable -> None|^Exception'

    def __init__(sf, backgroud_symbolizer, /):
        check_type_le(ISymbolizeRegister, backgroud_symbolizer)
        sf._bg = bg = backgroud_symbolizer
        sf._ww = ww = bg.whether_weakref
        sf._s = set() if not ww else WeakSet()
            # :: {sym}
    def __repr__(sf, /):
        return repr_helper(sf, sf._bg)
    @property
    def backgroud_symbolizer(sf, /):
        '-> ISymbolizeRegister'
        return sf._bg

    @property
    @override
    def whether_weakref(sf, /):
        '-> bool #whether cache only weakref of sym: WeakKeyDictionary<sym,val>, WeakValueDictionary<val,sym>'
        return sf._ww
        return sf._bg.whether_weakref
    @property
    @override
    def _standardize_(sf, /):
        '-> (obj -> val/hashable{unchecked yet}) #eg: set->frozenset #eg:default_standardize_()'
            # <<== 'obj -> val/hashable{unchecked yet} #eg: set->frozenset #eg:default_standardize_()'
        return sf._bg._standardize_
    @override
    def _check_value_(sf, val, /):
        'val/hashable -> None|^Exception'
        sf._bg._check_value_(val)
        sf._check_value__more_(val)
    @override
    def _inv_lookup_(sf, val, /):
        'val -> sym|^LookupError'
        sym = sf._bg._inv_lookup_(val)
            # ^LookupError
        sf.__on_new(sym, val)
        return sym
    def __on_new(sf, sym, val, /):
        'not yet _check_value__more_'
        if not sym in sf._s:
            sf._check_value__more_(val)
            sf._s.add(sym)
    @override
    def _register_(sf, val, /):
        '[after ._check_value_(val)]=>val -> sym #not existed yet'
        sym = sf._bg._register_(val)
        sf._s.add(sym)
        return sym
    @override
    def lookup(sf, sym, /):
        'sym -> val/hashable|^LookupError'
        val = sf._bg.lookup(sym)
            # ^LookupError
        sf.__on_new(sym, val)
        return val











class ISymbolizeRegister__using_default_standardize(ISymbolizeRegister):
    'using default_standardize_()'
    __slots__ = ()
    @override
    def _standardize_(sf, obj, /):
        'obj -> val/hashable{unchecked yet} #eg: set->frozenset #eg:default_standardize_()'
        return default_standardize_(obj)
class _Symbol:pass
class ISymbolizeRegister__typed(ISymbolizeRegister):
    ___no_slots_ok___ = True
    @property
    @abstractmethod
    def _type4sym2val_(sf, /):
        '-> type(sym2val)'
    @property
    @abstractmethod
    def _type4val2sym_(sf, /):
        '-> type(val2sym)'
    def __repr__(sf, /):
        return repr_helper(sf, sf._s2v, sf._v2s)
    def __init__(sf, sym2val=None, val2sym=None, /):
        if not (sym2val is None) is (val2sym is None):raise TypeError
        if sym2val is None:
            sym2val = sf._type4sym2val_()
            val2sym = sf._type4val2sym_()
        check_type_is(sf._type4sym2val_, sym2val)
        check_type_is(sf._type4val2sym_, val2sym)
        assert len(sym2val) == len(val2sym)
        sf._s2v = sym2val
        sf._v2s = val2sym
    @override
    def _check_value_(sf, val, /):
        'val/hashable -> None|^Exception'
        pass
    @override
    def _inv_lookup_(sf, val, /):
        'val -> sym|^LookupError'
        return sf._v2s[val]
    @override
    def _register_(sf, val, /):
        '[after ._check_value_(val)]=>val -> sym #not existed yet'
        sym = _Symbol()
        sf._v2s[val] = sym
        sf._s2v[sym] = val
        return sym
    @override
    def lookup(sf, sym, /):
        'sym -> val/hashable|^LookupError'
        return sf._s2v[sym]


def default_standardize_(x, /):
    return std_mk_hashable_(x)















class IWeakSymbolizeRegister(ISymbolizeRegister__typed):
    #@override
    whether_weakref = True
    #@override
    _type4sym2val_ = WeakKeyDictionary
    #@override
    _type4val2sym_ = WeakValueDictionary

class WeakSymbolizeRegister(IWeakSymbolizeRegister, ISymbolizeRegister__using_default_standardize):pass
WeakSymbolizeRegister()




class IPersistentSymbolizeRegister(ISymbolizeRegister__typed):
    #@override
    whether_weakref = False
    #@override
    _type4sym2val_ = dict
    #@override
    _type4val2sym_ = dict

class PersistentSymbolizeRegister(IPersistentSymbolizeRegister, ISymbolizeRegister__using_default_standardize):pass
PersistentSymbolizeRegister()






















__all__
from seed.types.mapping.symbolize import default_standardize_, ISymbolizeRegister
from seed.types.mapping.symbolize import WeakSymbolizeRegister, PersistentSymbolizeRegister, ISymbolizeRegister__subset
from seed.types.mapping.symbolize import ISymbolizeRegister__typed, ISymbolizeRegister__using_default_standardize
from seed.types.mapping.symbolize import IWeakSymbolizeRegister, IPersistentSymbolizeRegister

from seed.types.mapping.symbolize import *
