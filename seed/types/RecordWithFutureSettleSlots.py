#__all__:goto
r'''[[[
e ../../python3_src/seed/types/RecordWithFutureSettleSlots.py

seed.types.RecordWithFutureSettleSlots
py -m nn_ns.app.debug_cmd   seed.types.RecordWithFutureSettleSlots -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.RecordWithFutureSettleSlots:__doc__ -ht # -ff -df
#######

[[
@20260402
come_from:
    ++ft23:lazy-auto-property #hash
    e ../../python3_src/seed/data_funcs/finger_tree/ft23.py
    e ../../python3_src/seed/data_funcs/finger_tree/ft23_7types.py
view ../../python3_src/seed/types/Record.py
]]


'#'; __doc__ = r'#'
>>> R = mk_RecordTypeWithFutureSettleSlots_('aa.bb', 'C.R', 'a b c'.split(), ...)
>>> R()
R(Ellipsis, Ellipsis, Ellipsis)
>>> R(1)
R(1, Ellipsis, Ellipsis)
>>> R(1, 2)
R(1, 2, Ellipsis)
>>> R(1, 2, 3)
R(1, 2, 3)
>>> R(1, 2, 3, 4)
Traceback (most recent call last):
    ...
TypeError
>>> R(1, 2)['a']
1
>>> R(1, 2)['b']
2
>>> R(1, 2)['c']
Ellipsis
>>> R(1, 2)['d']
Traceback (most recent call last):
    ...
KeyError: 'd'
>>> R(1, 2)[0]
1
>>> R(1, 2)[1]
2
>>> R(1, 2)[2]
Ellipsis
>>> R(1, 2)[3]
Traceback (most recent call last):
    ...
IndexError: list index out of range
>>> R(1, 2)[-1]
Ellipsis
>>> R(1, 2)[-2]
2
>>> R(1, 2)[-3]
1
>>> R(1, 2)[-4]
Traceback (most recent call last):
    ...
IndexError: list index out of range
>>> R(1, 2)[2:]
(Ellipsis,)
>>> R(1, 2)[1:]
(2, Ellipsis)


>>> x = R(1, 2); x[...:-1] = 999; x
R(1, 2, 999)
>>> x = R(1, 2); x[...:1] = 999
Traceback (most recent call last):
    ...
KeyError: ('settled:', 1)

>>> x = R(1, 2); x[...:'c'] = 999; x
R(1, 2, 999)
>>> x = R(1, 2); x[...:'a'] = 999
Traceback (most recent call last):
    ...
KeyError: ('settled:', 'a')


py_adhoc_call   seed.types.RecordWithFutureSettleSlots   @f
]]]'''#'''
__all__ = r'''
mk_RecordTypeWithFutureSettleSlots_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from collections.abc import Mapping as IMapping
from seed.lang.class_property import class_property
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.repr_input import repr_helper
    from seed.types.FrozenDict import mk_FrozenDict
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

_nms7ok = ('keys', 'values', 'items', 'get')
_Ts = (int, slice)
_get = object.__getattribute__
_set = object.__setattr__
class _IRecordWithFutureSettleSlots(IMapping, ABC):
    r'''[[[
    '[record is mapping_view && seq][key is not int/slice]'
    usage:
        sf[k]
        sf[j]
        sf[i:j]
    usage:
        sf[type(sf).Nothing:k] = v

    ]]]'''#'''
    #__slots__ = ()
    ___no_slots_ok___ = True
    @class_property
    @abstractmethod
    def Nothing(cls, /):
        '-> object # repr empty slot:resettable'
    @class_property
    @abstractmethod
    def key2idx(cls, /):
        '-> {k:j}'
    @class_property
    @abstractmethod
    def idx2key(cls, /):
        '-> [k]'
    #.@property
    #.@abstractmethod
    #.def _j2v(sf, /):
    #.    '-> [v]'
    def __init__(sf, /, *args):
        cls = type(sf)
        if not len(args) <= len(cls.idx2key):raise TypeError
        j2v = list(args)
        j2v.extend([cls.Nothing]*(len(cls.idx2key) -len(args)))
        assert len(j2v) == len(cls.idx2key)
        _set(sf, '_j2v', j2v)
    def __getattribute__(sf, nm, /):
        if not nm in _nms7ok:
            raise AttributeError(nm)
        return _get(sf, nm)
    def __setattr__(sf, nm, v, /):
        raise AttributeError(nm)
    def __delattr__(sf, nm, /):
        raise AttributeError(nm)
    def __repr__(sf, /):
        j2v = _get(sf, '_j2v')
        return repr_helper(sf, *j2v)
    def __len__(sf, /):
        cls = type(sf)
        return len(cls.idx2key)
    def __iter__(sf, /):
        cls = type(sf)
        return iter(cls.idx2key)
    def __reversed__(sf, /):
        cls = type(sf)
        return reversed(cls.idx2key)
    def __contains__(sf, k, /):
        cls = type(sf)
        return k in cls.key2idx
    def keys(sf, /):
        cls = type(sf)
        return cls.key2idx.keys()
    def get(sf, k, default=None, /):
        if type(k) in _Ts:
            #raise TypeError
            return default
        return super(sf).get(k, default)


    def __getitem__(sf, k, /):
        j2v = _get(sf, '_j2v')
        T = type(k)
        if T in _Ts:
            x = j2v[k]
            if T is slice:
                x = tuple(x)
            return x
        cls = type(sf)
        j = cls.key2idx[k]
        return j2v[j]
    def __setitem__(sf, n_k, v, /):
        cls = type(sf)
        match n_k:
            case slice(start=cls.Nothing, stop=k, step=None):
                pass
            case _:
                raise TypeError(n_k)
        T = type(k)
        if T is slice:raise TypeError
        if T is int:
            j = k
            j = range(len(cls.idx2key))[j]
        else:
            j = cls.key2idx[k]
        j
        j2v = _get(sf, '_j2v')
        if not cls.Nothing is j2v[j]:raise KeyError('settled:', k)
        if cls.Nothing is v:raise ValueError('value is Nothing:', v)
        j2v[j] = v
        return
_IRecordWithFutureSettleSlots
def mk_RecordTypeWithFutureSettleSlots_(__module__, __qualname__, _field_key_seq_, Nothing, /):
    j2k = _field_key_seq_ = tuple(_field_key_seq_)
    if any(type(k) is int for k in j2k):raise TypeError(j2k)
    k2j = _field_key2seq_idx_ = mk_FrozenDict({k:j for j, k in enumerate(j2k)})
    if not len(k2j) == len(j2k):raise Exception('duplicated:', j2k)
    _Nothing = Nothing
    class Record(_IRecordWithFutureSettleSlots):
        #___no_slots_ok___ = True
        #@override
        Nothing = _Nothing
        #@override
        idx2key = j2k
        #@override
        key2idx = k2j
        #...compatible:
        _field_key_seq_ = j2k
        _field_key2seq_idx_ = k2j
    assert not Record.__abstractmethods__
    Record.__module__ = __module__
    Record.__qualname__ = __qualname__
    _, _, __name__ = __qualname__.rpartition('.')
    Record.__name__ = __name__
    return Record




__all__
from seed.types.RecordWithFutureSettleSlots import mk_RecordTypeWithFutureSettleSlots_
#def mk_RecordTypeWithFutureSettleSlots_(__module__, __qualname__, _field_key_seq_, Nothing, /):

from seed.types.RecordWithFutureSettleSlots import *
