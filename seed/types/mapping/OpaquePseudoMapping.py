#__all__
r'''

NOTE!!!! [not Mapping <: IOpaquePseudoMapping]
    since IOpaquePseudoMapping forbid __bool__/__len__/__iter__/...
    DO NOT: IOpaquePseudoMapping.register(Mapping)


seed.types.mapping.OpaquePseudoMapping
py -m seed.types.mapping.OpaquePseudoMapping
py -m nn_ns.app.debug_cmd   seed.types.mapping.OpaquePseudoMapping




from seed.types.mapping.PseudoMapping import IPseudoMapping___get, IPseudoMapping___get__setdefault

from seed.types.mapping.OpaquePseudoMapping import IOpaquePseudoMapping, IMutableOpaquePseudoMapping, IMutableOpaquePseudoMapping__init_new_key_only,      OpaquePseudoMappingView, MutableOpaquePseudoMappingWrapper, MutableOpaquePseudoMappingWrapper__init_new_key_only

IOpaquePseudoMapping is not Mapping
    used as namespace<symbol, value>
    no: __iter__, __len__, __bool__, keys, items...
    has: __contains__, __getitem__, __setitem__, __delitem__, popitem...

Mapping:
    __getitem__, __iter__, __len__
    ---
    __contains__, keys, items, values, get, __eq__, __ne__
    ===
        MutableMapping
            __setitem__, __delitem__
            ---
            pop, popitem, clear, update, setdefault

IOpaquePseudoMapping:
    __getitem__, #xxx:__iter__, __len__
    ---
    __contains__, get, #xxx:keys, items, values, __eq__, __ne__
    ===
        IMutableOpaquePseudoMapping
            __setitem__, __delitem__
            ---
            pop, update, setdefault, #xxx: popitem, clear
        IMutableOpaquePseudoMapping__init_new_key_only
            __setitem__, #xxx: __delitem__
            ---
            update, setdefault, #xxx: pop, popitem, clear





>>> d = OpaquePseudoMappingView({1:2})
>>> bool(d)
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object is not callable
>>> len(d)
Traceback (most recent call last):
    ...
TypeError: object of type 'OpaquePseudoMappingView' has no len()
>>> iter(d)
Traceback (most recent call last):
    ...
TypeError: 'OpaquePseudoMappingView' object is not iterable
>>> d[1]
2
>>> 1 in d
True
>>> 2 in d
False
>>> d.get(2)
>>> d[2]
Traceback (most recent call last):
    ...
KeyError: 2
>>> d.get(2, 3)
3
>>> d[2] = 3
Traceback (most recent call last):
    ...
TypeError: 'OpaquePseudoMappingView' object does not support item assignment
>>> del d[1]
Traceback (most recent call last):
    ...
TypeError: 'OpaquePseudoMappingView' object doesn't support item deletion

#'


>>> d = MutableOpaquePseudoMappingWrapper({1:2})
>>> bool(d)
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object is not callable
>>> len(d)
Traceback (most recent call last):
    ...
TypeError: object of type 'MutableOpaquePseudoMappingWrapper' has no len()
>>> iter(d)
Traceback (most recent call last):
    ...
TypeError: 'MutableOpaquePseudoMappingWrapper' object is not iterable
>>> d[1]
2
>>> 1 in d
True
>>> 2 in d
False
>>> d.get(2)
>>> d[2]
Traceback (most recent call last):
    ...
KeyError: 2
>>> d.get(2, 3)
3
>>> d[2] = 3
>>> d[2]
3
>>> d[2] = 4
>>> d[2]
4
>>> del d[1]
>>> d[1]
Traceback (most recent call last):
    ...
KeyError: 1

>>> d.setdefault(2, 5)
4
>>> d[2]
4
>>> d.setdefault(1, 5)
5
>>> d[1]
5
>>> d.pop(1)
5
>>> d[1]
Traceback (most recent call last):
    ...
KeyError: 1
>>> d.pop(1)
Traceback (most recent call last):
    ...
KeyError: 1
>>> d.pop(1, None)
>>> d.pop(1, 9)
9
>>> d.pop(1, default=9)
9
>>> d.pop(1, xxx=9)
Traceback (most recent call last):
    ...
TypeError
>>> d.pop(1, default=9, xxx=7)
Traceback (most recent call last):
    ...
TypeError
>>> d.pop(1, 9, 7)
Traceback (most recent call last):
    ...
TypeError
>>> d.pop(1, 9, default=9)
Traceback (most recent call last):
    ...
TypeError

>>> d.update({6:7}, a=8)
>>> d[6]
7
>>> d['a']
8



>>> d = MutableOpaquePseudoMappingWrapper__init_new_key_only({1:2})
>>> bool(d)
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object is not callable
>>> len(d)
Traceback (most recent call last):
    ...
TypeError: object of type 'MutableOpaquePseudoMappingWrapper__init_new_key_only' has no len()
>>> iter(d)
Traceback (most recent call last):
    ...
TypeError: 'MutableOpaquePseudoMappingWrapper__init_new_key_only' object is not iterable
>>> d[1]
2
>>> 1 in d
True
>>> 2 in d
False
>>> d.get(2)
>>> d[2]
Traceback (most recent call last):
    ...
KeyError: 2
>>> d.get(2, 3)
3
>>> d[2] = 3
>>> d[2]
3
>>> del d[1]
Traceback (most recent call last):
    ...
AttributeError: __delitem__

TypeError: 'MutableOpaquePseudoMappingWrapper__init_new_key_only' object doesn't support item deletion

#'

>>> d[1]
2
>>> d[1] = -1
Traceback (most recent call last):
    ...
KeyError: 1
>>> d[1]
2







>>> d = MutableOpaquePseudoMappingWrapper({1:2}, forbid_delete_key=True)
>>> del d[1]
Traceback (most recent call last):
    ...
KeyError: 1
>>> d[1]
2
>>> d[1] = 5
>>> d[1]
5
>>> d[2] = 6
>>> d[2]
6


>>> d = MutableOpaquePseudoMappingWrapper({1:2}, forbid_override_key=True)
>>> d[1] = 5
Traceback (most recent call last):
    ...
KeyError: 1
>>> d[1]
2
>>> del d[1]
>>> d[1]
Traceback (most recent call last):
    ...
KeyError: 1
>>> d[1] = 5
>>> d[1]
5
>>> d[2] = 6
>>> d[2]
6




>>> d = MutableOpaquePseudoMappingWrapper({1:2}, forbid_new_key=True)
>>> d[1]
2
>>> d[1] = 5
>>> d[1]
5
>>> del d[1]
>>> d[1]
Traceback (most recent call last):
    ...
KeyError: 1
>>> d[1] = 5
Traceback (most recent call last):
    ...
KeyError: 1
>>> d[2] = 6
Traceback (most recent call last):
    ...
KeyError: 2





#'''





__all__ = '''
    IPseudoMapping___get
        IPseudoMapping___get__setdefault
    IOpaquePseudoMapping
        IMutableOpaquePseudoMapping
        IMutableOpaquePseudoMapping__init_new_key_only
            OpaquePseudoMappingView
            MutableOpaquePseudoMappingWrapper
            MutableOpaquePseudoMappingWrapper__init_new_key_only
    '''.split()




from seed.lang.hasattr__as_cls import hasattr__as_cls
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
#from seed.types.AddrAsHash import BaseAddrAsHash #AddrAsHash as EqById
#from seed.abc.eq_by_id.AddrAsHash import BaseAddrAsHash #AddrAsHash as EqById
from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash
from seed.mapping_tools.fdefault import mapping_set__new_or_pass__cased_, mapping_get__tmay__get_Nothing

class IPseudoMapping___get(ABC):
    __slots__ = ()
    def __bool__(sf, /): raise NotImplementedError
    #def __len__(sf, /): raise NotImplementedError
    __iter__ = None
    def __bool__(sf, /):
        raise NotImplementedError
    def __contains__(sf, key, /):
        Nothing = object()
        return not Nothing is sf.get(key, Nothing)
    @abstractmethod
    def get(sf, key, /, default=None):
        'key -> value|default'
    @classmethod
    @override
    def __subclasshook__(cls, C, /):
        # ABCMeta::__subclasshook__
        if cls is __class__:
            #assert isinstance(C, type)
            #if any("get" in B.__dict__ for B in C.__mro__) and any("__contains__" in B.__dict__ for B in C.__mro__):
            if hasattr__as_cls(C, 'get') and hasattr__as_cls(C, '__contains__'):
                return True
        return NotImplemented

class IPseudoMapping___get__setdefault(IPseudoMapping___get):
    __slots__ = ()
    @abstractmethod
    def setdefault(sf, key, input_value, /):
        '-> old_value|input_value'
    @classmethod
    @override
    def __subclasshook__(cls, C, /):
        # ABCMeta::__subclasshook__
        if cls is __class__:
            #assert isinstance(C, type)
            #if any("get" in B.__dict__ for B in C.__mro__) and any("__contains__" in B.__dict__ for B in C.__mro__) and any("setdefault" in B.__dict__ for B in C.__mro__):
            if hasattr__as_cls(C, 'get') and hasattr__as_cls(C, '__contains__') and hasattr__as_cls(C, 'setdefault'):
                return True
        return NotImplemented


class IOpaquePseudoMapping(BaseAddrAsHash, ABC):#(EqById, ABC):
    __slots__ = ()
    #__getitem__, __contains__, get
    #__len__ = None
    __bool__ = None
        #require the assigment!!!!
        #   otherwise object.__bool__ -> True
        #TypeError: 'NoneType' object is not callable
    __iter__ = None
        #require the assigment!!!!
        #   otherwise do mk an iterator!!!
        #       ???__getitem__???
    #__bool__ = NotImplemented
    #del __bool__
        #NameError: name '__bool__' is not defined
    r'''
    def __bool__(sf, /):
        raise NotImplementedError
        return None
        return NotImplemented
    #'''

    @abstractmethod
    def __getitem__(sf, key, /):
        '-> value|raise KeyError'
    def __contains__(sf, key, /):
        try:
            sf[key]
        except KeyError:
            return False
        return True
    def get(sf, key, /, default=None):
        'key -> value|default'
        try:
            return sf[key]
        except KeyError:
            return default
    def __init_subclass__(cls, /,*args, **kwargs):
        if cls.__bool__ is not None:raise logic-err
        if cls.__iter__ is not None:raise logic-err
        if hasattr(cls, '__len__'):raise logic-err
        #keys, items, values
        if hasattr(cls, 'keys'):raise logic-err
        if hasattr(cls, 'items'):raise logic-err
        if hasattr(cls, 'values'):raise logic-err
        super().__init_subclass__(*args, **kwargs)

class _IMutableOpaquePseudoMapping(IOpaquePseudoMapping):
    __slots__ = ()
    #__setitem__, update, setdefault
    @abstractmethod
    def __setitem__(sf, key, value, /):
        '-> None'
    def update(sf, /,*args, **kwargs):
        d = dict(*args, **kwargs)
        for k, v in d.items():
            sf[k] = v
    def setdefault(sf, key, input_value, /):
        '-> old_value|input_value'
        #bug:(is_old_value, value) = mapping_set__new_or_pass__cased_(sf, key, -1, input_value, try_vs_Nothing_vs_in=None)
        #   using mapping.setdefault inside!!!
        tmay_old_value = mapping_get__tmay__get_Nothing(sf, key)
        if tmay_old_value:
            [old_value] = tmay_old_value
            value = old_value
        else:
            sf[key] = input_value
            value = input_value
        return value

class IMutableOpaquePseudoMapping(_IMutableOpaquePseudoMapping):
    __slots__ = ()
    #__setitem__, __delitem__, pop, update, setdefault
    @abstractmethod
    def __delitem__(sf, key, /):
        '-> None|raise KeyError'
    def pop(sf, key, /, *tmay_default, **kwargs):
        m = len(tmay_default)+len(kwargs)
        if m == 0:
            v = sf[key]
                # raise KeyError here
            del sf[key]
        elif m == 1:
            if kwargs:
                (key, default) = kwargs.popitem()
                if key != 'default':raise TypeError
            else:
                [default] = tmay_default
            default
            try:
                v = sf[key]
            except KeyError:
                v = default
            else:
                del sf[key]
        else:
            if m >= 2: raise TypeError
            raise logic-err
        v
        return v

class IMutableOpaquePseudoMapping__init_new_key_only(_IMutableOpaquePseudoMapping):
    __slots__ = ()
    #__setitem__, update, setdefault
    @abstractmethod
    def ___set_new_item___(sf, key, value, /):
        '-> None #__setitem__'
    @override
    def __setitem__(sf, key, value, /):
        '-> None'
        if key in sf: raise KeyError(key) #existed
        type(sf).___set_new_item___(sf, key, value)

r'''
class OpaquePseudoMapping(IOpaquePseudoMapping):
class MutableOpaquePseudoMapping(IMutableOpaquePseudoMapping):
class MutableOpaquePseudoMapping__init_new_key_only(IMutableOpaquePseudoMapping__init_new_key_only):
#'''


class _OpaquePseudoMappingWrapper(IOpaquePseudoMapping, ABC__no_slots):
    #__slots__ = ()
    def __init__(sf, pseudo_mapping, /):
        if not hasattr(type(pseudo_mapping), '__getitem__'): raise TypeError
        sf.__dict__[_OpaquePseudoMappingWrapper] = pseudo_mapping
        super().__init__()
    @override
    def __getitem__(sf, key, /):
        '-> value|raise KeyError'
        return sf.__dict__[_OpaquePseudoMappingWrapper][key]
class OpaquePseudoMappingView(_OpaquePseudoMappingWrapper):
    #__slots__ = ()
    pass

class MutableOpaquePseudoMappingWrapper(_OpaquePseudoMappingWrapper, IMutableOpaquePseudoMapping):
    #__slots__ = ()
    def __init__(sf, pseudo_mapping, /,*, forbid_new_key=False, forbid_override_key=False, forbid_delete_key=False):
        if not hasattr(type(pseudo_mapping), '__setitem__'): raise TypeError
        if not hasattr(type(pseudo_mapping), '__delitem__'): raise TypeError
        if not set(map(type, [forbid_new_key, forbid_override_key, forbid_delete_key])) == {bool}: raise TypeError
        sf.__dict__[__class__] = sum(bit << i for i, bit in enumerate([forbid_new_key, forbid_override_key, forbid_delete_key]))
        super().__init__(pseudo_mapping)
    @override
    def __setitem__(sf, key, value, /):
        d = sf.__dict__[_OpaquePseudoMappingWrapper]
        _ff = sf.__dict__[__class__]&0b11
        ok = False
        if _ff == 0:
            ok = True
        elif _ff == 0b11:
            ok = False
        else:
            ok = _ff != (0b10 if key in d else 0b01)
        if not ok: raise KeyError(key)
        d[key] = value

    @override
    def __delitem__(sf, key, /):
        f__ = sf.__dict__[__class__]&0b100
        ok = not f__
        if not ok: raise KeyError(key)
        del sf.__dict__[_OpaquePseudoMappingWrapper][key]

class MutableOpaquePseudoMappingWrapper__init_new_key_only(_OpaquePseudoMappingWrapper, IMutableOpaquePseudoMapping__init_new_key_only):
    #__slots__ = ()
    def __init__(sf, pseudo_mapping, /):
        if not hasattr(type(pseudo_mapping), '__setitem__'): raise TypeError
        super().__init__(pseudo_mapping)
    @override
    def ___set_new_item___(sf, key, value, /):
        #not bug:
        sf.__dict__[_OpaquePseudoMappingWrapper][key] = value
        return
        d = sf.__dict__[_OpaquePseudoMappingWrapper]
        n = len(d)
        v = d.setdefault(key, value)
        if v is not value or len(d) != n+1: raise KeyError#existed

OpaquePseudoMappingView({})
MutableOpaquePseudoMappingWrapper({})
MutableOpaquePseudoMappingWrapper__init_new_key_only({})

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


