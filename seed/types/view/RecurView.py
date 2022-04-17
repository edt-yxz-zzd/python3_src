
r'''

py -m seed.types.view.RecurView
py -m nn_ns.app.debug_cmd   seed.types.view.RecurView

from seed.types.view.RecurView import default_cfg4RecurView
from seed.types.view.RecurView import IConfig4RecurView, IRecurView, default_cfg4RecurView, default_slice
from seed.types.view.RecurView import Config4RecurView, default_cfg4RecurView, RecurView4Seq, RecurView4Mapping, asif_RecurView4bytearray, asif_RecurView4Set

e ../../python3_src/seed/types/view/RecurView.py


>>> from seed.types.view.RecurView import IConfig4RecurView, IRecurView, default_cfg4RecurView, default_slice

>>> from seed.types.view.RecurView import Config4RecurView, default_cfg4RecurView, RecurView4Seq, RecurView4Mapping, asif_RecurView4bytearray, asif_RecurView4Set

>>> cfg = default_cfg4RecurView

>>> vw = cfg.to_view({...:[{4}]})

#mapping
>>> vw
RecurView4Mapping(None, {Ellipsis: [{4}]})
>>> vw[0]
Traceback (most recent call last):
    ...
KeyError: 0
>>> vw[...]
RecurView4Seq(None, [{4}])

#seq
>>> vw[...][1]
Traceback (most recent call last):
    ...
IndexError: list index out of range
>>> vw[...][0]
SetView({4})
>>> vw[...][:1]
RecurView4Seq(None, [{4}])
>>> vw[...][:0]
RecurView4Seq(None, [])

#set
>>> 0 in vw[...][0]
False
>>> 1 in vw[...][0]
False
>>> 4 in vw[...][0]
True
>>> len(vw[...][0])
1



#IRecurView.get_type_of_wrapped_obj
>>> vw[...][:0].get_type_of_wrapped_obj()
<class 'list'>
>>> vw[...][0].get_type_of_wrapped_obj()
Traceback (most recent call last):
    ...
AttributeError: 'SetView' object has no attribute 'get_type_of_wrapped_obj'
>>> vw[...].get_type_of_wrapped_obj()
<class 'list'>
>>> vw.get_type_of_wrapped_obj()
<class 'dict'>


#Config4RecurView.get_view__xxx
>>> cfg.get_view__immutable_types()     #doctest: +ELLIPSIS
SetView({<class '...'>})
>>> cfg.get_view__type2RecurViewType()  #doctest: +ELLIPSIS
mappingproxy({<class '...'>})
>>> cfg.get_view__immutable_basetypes()
SeqView([<class 'numbers.Number'>])
>>> cfg.get_view__basetype_RecurViewType_pairs()
SeqView([(<class 'collections.abc.Sequence'>, <class 'seed.types.view.RecurView.RecurView4Seq'>), (<class 'collections.abc.Mapping'>, <class 'seed.types.view.RecurView.RecurView4Mapping'>), (<class 'collections.abc.Set'>, <class 'seed.types.view.RecurView.asif_RecurView4Set'>)])
>>> cfg.get_view__fallback_RecurViewTypes()
SeqView([])

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

#'''

__all__ = '''
    IConfig4RecurView
        Config4RecurView
    IRecurView
        RecurView4Seq
        RecurView4Mapping

    default_cfg4RecurView
        cfg2may_cfg4RecurView
        cfg5may_cfg4RecurView
        asif_RecurView4bytearray
        asif_RecurView4Set

    default_slice
        slc2may_slice
        slc5may_slice
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.view.View import MapView, SetView, SeqView
from seed.abc.abc__ver0 import ABC, abstractmethod, override
from seed.tiny import check_tmay, check_pair, check_uint
___end_mark_of_excluded_global_names__0___ = ...

class IConfig4RecurView(ABC):
    __slots__ = ()

    @abstractmethod
    def try_view(sf8cfg, obj, /):
        '{{sf/cfg4RecurView/IConfig4RecurView}} -> obj -> tmay IRecurView<cfg4RecurView, obj>'
        sf = cfg4RecurView = sf8cfg
        return ()

    def to_view(sf8cfg, obj, /):
        'sf/cfg4RecurView/IConfig4RecurView -> obj -> IRecurView<cfg4RecurView, obj>|raise TypeError'
        tmay_view = sf8cfg.try_view(obj)
        if not tmay_view:
            cls4obj = type(obj)
            raise TypeError('type(obj)={cls4obj.__qualname__}; cfg4RecurView={sf8cfg!r}')
        [view] = tmay_view
        return view



class IRecurView(ABC):
    r'''
    IRecurView<cfg4RecurView/IConfig4RecurView, obj>
    #'''
    __slots__ = ()

    @classmethod
    @abstractmethod
    def try_view_(cls, cfg4RecurView, obj, /):
        '{{cls/IRecurView}} -> cfg4RecurView/IConfig4RecurView -> obj -> tmay IRecurView<cfg4RecurView, obj>'
    @abstractmethod
    def get_type_of_wrapped_obj(sf, /):
        '{{sf/IRecurView<cfg4RecurView, obj>}} -> type<obj>'





























class Config4RecurView(IConfig4RecurView):
    r'''
    .immutable_types
        #for int/str not for tuple!!!
    .type2RecurViewType
    .immutable_basetypes
    .basetype_RecurViewType_pairs
    .fallback_RecurViewTypes
    #'''
    def __init__(sf, immutable_types, type2RecurViewType, immutable_basetypes, basetype_RecurViewType_pairs, fallback_RecurViewTypes, /):
        sf._immutable_types = {*immutable_types}

        sf._type2RecurViewType = {**type2RecurViewType}

        sf._immutable_basetypes = [*immutable_basetypes]
        sf._basetype_RecurViewType_pairs = [
            (basecls, RecurViewType) for basecls, RecurViewType in basetype_RecurViewType_pairs
            ]

        sf._fallback_RecurViewTypes = [*fallback_RecurViewTypes]
    def __repr__(sf, /):
        return repr_helper(sf
        ,sf._immutable_types
        ,sf._type2RecurViewType
        ,sf._immutable_basetypes
        ,sf._basetype_RecurViewType_pairs
        ,sf._fallback_RecurViewTypes
        )
    #MapView, SetView, SeqView


    def get_view__immutable_types(sf, /):
        return SetView(sf._immutable_types)
    def get_view__type2RecurViewType(sf, /):
        return MapView(sf._type2RecurViewType)
    def get_view__immutable_basetypes(sf, /):
        return SeqView(sf._immutable_basetypes)
    def get_view__basetype_RecurViewType_pairs(sf, /):
        return SeqView(sf._basetype_RecurViewType_pairs)
    def get_view__fallback_RecurViewTypes(sf, /):
        return SeqView(sf._fallback_RecurViewTypes)



    @override
    def try_view(sf8cfg, obj, /):
        '{{sf/cfg4RecurView/IConfig4RecurView}} -> obj -> tmay IRecurView<cfg4RecurView, obj>'
        sf = cfg4RecurView = sf8cfg
        cls = type(obj)
        ######################
        if cls in sf._immutable_types:
            #for int not for tuple!!!
            return (obj,)
        ######################
        #may_RecurViewType = None
        if cls in sf._type2RecurViewType:
            RecurViewType = sf._type2RecurViewType[cls]
            may_RecurViewType = RecurViewType
        else:
            ######################
            for basecls in sf._immutable_basetypes:
                if issubclass(cls, basecls):
                    return (obj,)
            ######################
            for basecls, RecurViewType in sf._basetype_RecurViewType_pairs:
                if issubclass(cls, basecls):
                    may_RecurViewType = RecurViewType
                    break
            else:
                may_RecurViewType = None
        ######################
        if may_RecurViewType is None:
            RecurViewTypes = sf._fallback_RecurViewTypes
        else:
            RecurViewType = may_RecurViewType
            RecurViewTypes = [RecurViewType]
                #fail then return () instead of raise
                #   since levels of tryings...
        ######################
        cfg4RecurView = sf8cfg
        for RecurViewType in RecurViewTypes:
            tmay_view = RecurViewType.try_view_(cfg4RecurView, obj)
            check_tmay(tmay_view)
            if tmay_view:
                [view] = tmay_view
                break
                return tmay_view
        else:
            return ()
        return tmay_view

































___begin_mark_of_excluded_global_names__1___ = ...
from collections.abc import Set, Sequence, Mapping, ByteString
from seed.helper.repr_input import repr_helper
#from seed.abc.IReprHelper import IReprHelper

from seed.tiny_.slice2triple import slice2triple_, fix_slice_by_len_, fix_slice_by_len_of_
from seed.tiny_.slice2triple import slice2triple, range2triple, convert_triple_as_, range2triple_, slice2triple_

from seed.tiny import echo_key
from seed.tiny import check_type_is
import operator
___end_mark_of_excluded_global_names__1___ = ...


default_slice = echo_key[:]


def slc2may_slice(slc, /):
    if slc == default_slice:
        may_slc = None
    else:
        may_slc = slc
    return may_slc
def slc5may_slice(may_slc, /):
    if may_slc is None:
        slc = default_slice
    else:
        slc = may_slc

    if not isinstance(slc, IConfig4RecurView): raise TypeError
    return slc


#view ../../python3_src/seed/types/view/SeqSliceView.py
#view ../../python3_src/seed/types/view/SeqTransformView.py
class RecurView4Seq(IRecurView, Sequence):
    'immutable; .__s/.__cfg should not be assigned again!'
    #__slots__ = ('__s', '__cfg', '__slc', '__weakref__')

    @classmethod
    @override
    def try_view_(cls, cfg4RecurView, obj, /):
        '{{cls/IRecurView}} -> cfg4RecurView/IConfig4RecurView -> obj -> tmay IRecurView<cfg4RecurView, obj>'
        if not isinstance(obj, Sequence):
            return ()
        return (cls(cfg4RecurView, obj),)
    @override
    def get_type_of_wrapped_obj(sf, /):
        '{{sf/IRecurView<cfg4RecurView, obj>}} -> type<obj>'
        return type(sf.__s)



    r'''
    def __init__(sf, may_cfg4RecurView, seq, may_slice=None, /):
        cfg4RecurView = cfg5may_cfg4RecurView(may_cfg4RecurView)
        sf.__cfg = cfg4RecurView
        slice_ = slc5may_slice(may_slice)
        sf.__slc = slice_

        if not isinstance(seq, Sequence): raise TypeError('not a seq')
        if isinstance(seq, __class__):
            seq = seq.__s
            assert not isinstance(seq, __class__)
        sf.__s = seq

    def __repr__(sf, /):
        cfg4RecurView = sf.__cfg
        may_cfg4RecurView = cfg2may_cfg4RecurView(cfg4RecurView)

        slice_ = sf.__slc
        may_slice = slc2may_slice(slice_)
        if may_slice is None:

            return repr_helper(sf, may_cfg4RecurView, sf.__s)
        else:
            return repr_helper(sf, may_cfg4RecurView, sf.__s, may_slice)
            # ?why not list(sf.__s)?
            #   view is not to hide info!!
    #'''
    def __init__(sf, may_cfg4RecurView, seq, /):
        cfg4RecurView = cfg5may_cfg4RecurView(may_cfg4RecurView)
        sf.__cfg = cfg4RecurView

        if not isinstance(seq, Sequence): raise TypeError('not a seq')
        if isinstance(seq, __class__):
            seq = seq.__s
            assert not isinstance(seq, __class__)
        sf.__s = seq

    def __repr__(sf, /):
        cfg4RecurView = sf.__cfg
        may_cfg4RecurView = cfg2may_cfg4RecurView(cfg4RecurView)

        return repr_helper(sf, may_cfg4RecurView, sf.__s)
            # ?why not list(sf.__s)?
            #   view is not to hide info!!

    #xxx @classmethod
    def from_sequence(sf, seq, /):
        cls = type(sf)
        return cls(sf.__cfg, seq)
    def __getitem__(sf, i, /):
        def i2v(i, /):
            check_type_is(int, i)
            v = sf.__s[i]
            return sf.__cfg.to_view(v)

        t = type(i)
        if t is int or hasattr(t, '__index__'):
            i = operator.__index__(i)
            v = i2v(i)
            return v

        if t is slice:
            slice_ = i
            rng = fix_slice_by_len_of_(range, sf, slice_)
                #check may int!!!!
            slice_ = range2triple_(slice, rng)
            seq = sf.__s[slice_]
            return sf.from_sequence(seq)
        if t is tuple: raise TypeError
        raise TypeError(i) #must be int/__index__, or slice


    def __len__(sf, /):
        return len(sf.__s)
    def __contains__(sf, x, /):
        return x in sf.__s
    def __iter__(sf, /):
        return iter(sf.__s)
    def __reversed__(sf, /):
        return reversed(sf.__s)
    def index(sf, /, *args):
        return sf.__s.index(*args)
    def count(sf, /, *args):
        return sf.__s.count(*args)





def cfg2may_cfg4RecurView(cfg4RecurView, /):
    if cfg4RecurView is default_cfg4RecurView:
        may_cfg4RecurView = None
    else:
        may_cfg4RecurView = cfg4RecurView
    return may_cfg4RecurView
def cfg5may_cfg4RecurView(may_cfg4RecurView, /):
    if may_cfg4RecurView is None:
        cfg4RecurView = default_cfg4RecurView
    else:
        cfg4RecurView = may_cfg4RecurView

    if not isinstance(cfg4RecurView, IConfig4RecurView): raise TypeError
    return cfg4RecurView

class RecurView4Mapping(IRecurView, Mapping):
    'immutable; .__d/.__cfg should not be assigned again!'
    #__slots__ = ('__d', '__cfg', '__weakref__')

    @classmethod
    @override
    def try_view_(cls, cfg4RecurView, obj, /):
        '{{cls/IRecurView}} -> cfg4RecurView/IConfig4RecurView -> obj -> tmay IRecurView<cfg4RecurView, obj>'
        if not isinstance(obj, Mapping):
            return ()
        return (cls(cfg4RecurView, obj),)
    @override
    def get_type_of_wrapped_obj(sf, /):
        '{{sf/IRecurView<cfg4RecurView, obj>}} -> type<obj>'
        return type(sf.__d)



    def __init__(sf, may_cfg4RecurView, mapping, /):
        cfg4RecurView = cfg5may_cfg4RecurView(may_cfg4RecurView)
        sf.__cfg = cfg4RecurView

        if not isinstance(mapping, Mapping): raise TypeError
        if isinstance(mapping, __class__):
            # since immutable, we can use the underly object directly
            mapping = mapping.__d
            assert not isinstance(mapping, __class__)
        sf.__d = mapping
    def __repr__(sf, /):
        cfg4RecurView = sf.__cfg
        may_cfg4RecurView = cfg2may_cfg4RecurView(cfg4RecurView)
        return repr_helper(sf, may_cfg4RecurView, sf.__d)
            # ?why not list(sf.__d)?
            #   view is not to hide info!!

    @classmethod
    def _from_iterable(cls, it, /):
        return cls(None, dict(it))
    def __contains__(sf, x, /):
        return x in sf.__d
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not isinstance(ot, Mapping):
            return NotImplemented
        if not len(sf) == len(ot):
            return False
        Nothing = object()
        return all(ot.get(k, Nothing) in [v] for k, v in sf.__d.items())

    def __iter__(sf, /):
        return iter(sf.__d)
    def __len__(sf, /):
        return len(sf.__d)
    def keys(sf, /):
        return sf.__d.keys()

    def __getitem__(sf, key, /):
        v = sf.__d[key]
        return sf.__cfg.to_view(v)
    if 0:
        #bug:
        def values(sf, /):
            return sf.__d.values()
        def items(sf, /):
            return sf.__d.items()
        def get(sf, key, default=None, /):
            return sf.__d.get(key, default)


___begin_mark_of_excluded_global_names__2___ = ...
from fractions import Fraction
from decimal import Decimal
from numbers import Number
from array import array as WordArray
import datetime
import time
from pathlib import PurePath
from types import MappingProxyType
___end_mark_of_excluded_global_names__2___ = ...
def _():
    'is time.struct_time immutable? YES!!!'
    t = time.localtime()
    if not type(t) is time.struct_time: raise logic-err
    hash(t)
_()
del _
def _():
    import pathlib
    s = set()
    for nm in pathlib.__all__:
        x = getattr(pathlib, nm)
        if isinstance(x, type) and issubclass(x, PurePath):
            s.add(x)
    assert PurePath in s
    #print(s)
    #{<class 'pathlib.Path'>, <class 'pathlib.WindowsPath'>, <class 'pathlib.PurePath'>, <class 'pathlib.PosixPath'>, <class 'pathlib.PureWindowsPath'>, <class 'pathlib.PurePosixPath'>}
    assert pathlib.PosixPath in s
    assert pathlib.WindowsPath in s
    return s
_PathTypes = _()
del _
r'''
types.FunctionType
types.LambdaType
types.MethodType
types.BuiltinFunctionType
types.BuiltinMethodType
MappingProxyType


class datetime.date
class datetime.time
class datetime.datetime
class datetime.timedelta
class datetime.tzinfo #ABC
    class datetime.timezone
time.struct_time?immutable?


basecls
class enum.Enum
class enum.IntEnum
class enum.IntFlag
class enum.Flag

Path/PurePath/...
#'''

def _asif_RecurView4bytearray(cfg4RecurView, bs, /):
    return memoryview(bs)
def _asif_RecurView4Set(cfg4RecurView, s, /):
    'mimic dict, where key are considered immutable solid data like str/datetime'
    return SetView(s)

class _asif_RecurView4XXX(IRecurView):
    @abstractmethod
    class ___ABC4XXX___:pass
    @classmethod
    @override
    def try_view_(cls, cfg4RecurView, obj, /):
        '{{cls/IRecurView}} -> cfg4RecurView/IConfig4RecurView -> obj -> tmay IRecurView<cfg4RecurView, obj>'
        if not isinstance(obj, cls.___ABC4XXX___):
            return ()
        return (cls(cfg4RecurView, obj),)
    @override
    def get_type_of_wrapped_obj(obj, /):
        '{{sf/IRecurView<cfg4RecurView, obj>}} -> type<obj>'
        return type(obj)
class asif_RecurView4bytearray(_asif_RecurView4XXX, ByteString):
    ___ABC4XXX___ = ByteString
    def __new__(sf, may_cfg4RecurView, bs, /):
        return _asif_RecurView4bytearray(may_cfg4RecurView, bs)
class asif_RecurView4Set(_asif_RecurView4XXX, Set):
    ___ABC4XXX___ = Set
    def __new__(sf, may_cfg4RecurView, set_, /):
        return _asif_RecurView4Set(may_cfg4RecurView, set_)









default_cfg4RecurView = Config4RecurView(
    {bool, int, float, complex
    ,Fraction, Decimal
    ,str, bytes
    ,range
    ,type(None)
    ,type(...) #Ellipsis
    ,type(NotImplemented)
    ,memoryview
    ,frozenset#,frozenset??
        #key-slot is immutable
        #the key obj itself is considered immutable

    ,datetime.date
    ,datetime.time
    ,datetime.datetime
    ,datetime.timedelta
    ,datetime.timezone
    ,time.struct_time
    ,*_PathTypes
    }

    ,{list:RecurView4Seq
    ,tuple:RecurView4Seq
    ,bytearray:asif_RecurView4bytearray#RecurView4Seq#??memoryview
    ,WordArray:RecurView4Seq
    ,set:asif_RecurView4Set
        #key-slot is mutable
    #,frozenset:asif_RecurView4Set
        #key-slot is immutable
        #the key obj itself is considered immutable
    ,dict:RecurView4Mapping
    ,MappingProxyType:RecurView4Mapping
        #key-value-slot is immutable
        #but the value obj itself is mutable!!!
    }

    ,[Number]

    ,[(Sequence, RecurView4Seq)
    ,(Mapping, RecurView4Mapping)
    ,(Set, asif_RecurView4Set)
    ]

    ,[]
    )



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


