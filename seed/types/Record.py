#__all__:goto
r'''[[[
e ../../python3_src/seed/types/Record.py
view ../../python3_src/seed/types/DictWithNewProtocol__ver2.py
view ../../python3_src/seed/for_libs/for_collections/namedtuple__nontuple4cached_property.py

seed.types.Record
py -m nn_ns.app.debug_cmd   seed.types.Record -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.Record:__doc__ -ht # -ff -df
#######

[[
used by:
seed.data_funcs.finger_tree.ft23_7types.Ops4Auto6FingerTree
    view ../../python3_src/seed/data_funcs/finger_tree/ft23_7types.py
]]


'#'; __doc__ = r'#'
>>> Rc = mk_RecordType_('u.v.w', 'xxx.yy.Rc', 'a b c'.split())
>>> Rc
<class 'u.v.w.xxx.yy.Rc'>
>>> t = Rc(11,22,33)
>>> t
Rc(11, 22, 33)
>>> t['a']
11
>>> t[0]
11
>>> t[0:2]
(11, 22)
>>> 1 in t
False
>>> 11 in t
False
>>> 'a' in t
True
>>> t.get(4, 999)
999
>>> t.get(1, 999)
999
>>> t.items()
ItemsView(Rc(11, 22, 33))
>>> t.keys()
KeysView(FrozenDict({'a': 0, 'b': 1, 'c': 2}))
>>> t.values()
ValuesView(Rc(11, 22, 33))
>>> [*t.items()]
[('a', 11), ('b', 22), ('c', 33)]
>>> [*t.values()]
[11, 22, 33]
>>> [*t.keys()]
['a', 'b', 'c']
>>> [*t]
['a', 'b', 'c']


>>> Rc(a=11, b=22, c=33)
Rc(11, 22, 33)
>>> Rc.from_mapping(dict(a=11, b=22, c=33))
Rc(11, 22, 33)
>>> Rc.from_iterable([11, 22, 33])
Rc(11, 22, 33)




py_adhoc_call   seed.types.Record   @f
]]]'''#'''
__all__ = r'''
mk_RecordType_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge

from seed.types.FrozenDict import mk_FrozenDict
from seed.lang.class_property import class_property# static_property
from collections.abc import Mapping as IMapping
from seed.abc.abc__ver1 import abstractmethod, override, ABC
___end_mark_of_excluded_global_names__0___ = ...

def _std_(cls, args, kwds, /):
    j2k = cls._field_key_seq_
    k2j = cls._field_key2seq_idx_
    if not len(args)+len(kwds) == len(j2k):raise TypeError
    if kwds:
        args = (*args, *map(kwds.pop, j2k[len(args):]))
    return args

def _check_field_key_infos6RecordType_(cls, /):
    j2k = cls._field_key_seq_
    k2j = cls._field_key2seq_idx_
    if not len(k2j) == len(j2k):raise TypeError
    if not len(k2j.keys()) == len(j2k[:]):raise TypeError
    for j, k in enumerate(j2k):
        if not k2j[k] == j:raise TypeError
    for k in j2k:
        if type(k) in _types4tpl:raise TypeError


_types4tpl = (int, slice)
_nms7ok = ('get', 'items', 'keys', 'values')
class _IBaseRecord(IMapping, tuple):
    __slots__ = ()

    @class_property
    @abstractmethod
    def _field_key_seq_(cls, /):
        '-> [field_key]'
    @class_property
    @abstractmethod
    def _field_key2seq_idx_(cls, /):
        '-> {field_key:uint%len(_field_key_seq_)}'
    #_field_key_seq_ = None
    #_field_key2seq_idx_ = None

    @classmethod
    def from_mapping(cls, d, /):
        j2k = cls._field_key_seq_
        if not len(d) == len(j2k):raise TypeError
        args = [d[k] for k in j2k]
        return cls.from_iterable(args)
    @classmethod
    def from_iterable(cls, args, /):
        return cls(*args)
    def __new__(cls, /, *args, **kwds):
        args = _std_(cls, args, kwds)
        777;del kwds
        sf = super(__class__, cls).__new__(cls, args)
        #sf._check6make_()
        cls._check6make_(sf)
        return sf
    def _check6make_(sf, /):
        pass
    def __getattribute__(sf, nm, /):
        if nm in _nms7ok:
            return object.__getattribute__(sf, nm)
        raise AttributeError(nm)
    def __getitem__(sf, k, /):
        if not type(k) in _types4tpl:
            cls = type(sf)
            k2j = cls._field_key2seq_idx_
            j = k2j[k]
            #return sf[j]
            k = j
        return tuple.__getitem__(sf, k)
    def __repr__(sf, /):
        #bug:args = (*sf,)
        args = (*sf[::],)
        nm = type(sf).__name__
        if len(args) == 1:
            [x] = args
            return f'{nm!s}({x!r})'
        return f'{nm!s}{args!r}'
    def __iter__(sf, /):
        cls = type(sf)
        j2k = cls._field_key_seq_
        return iter(j2k)
    def __reversed__(sf, /):
        cls = type(sf)
        j2k = cls._field_key_seq_
        return reversed(j2k)
    __len__ = tuple.__len__
    def __contains__(sf, k, /):
        cls = type(sf)
        k2j = cls._field_key2seq_idx_
        return k in k2j
    def keys(sf, /):
        cls = type(sf)
        k2j = cls._field_key2seq_idx_
        return k2j.keys()
    def get(sf, k, default=None, /):
        if type(k) in _types4tpl:
            #raise TypeError
            return default
        return super(sf).get(k, default)

#IMapping()
    #__getitem__, __iter__, __len__
#print(_IBaseRecord.__abstractmethods__)
#_IBaseRecord()#ok???#tuple subclass bypass ABC check


def mk_RecordType_(__module__, __qualname__, _field_key_seq_, /):
    j2k = _field_key_seq_ = tuple(_field_key_seq_)
    k2j = _field_key2seq_idx_ = mk_FrozenDict({k:j for j, k in enumerate(j2k)})
    class Record(_IBaseRecord):
        #___no_slots_ok___ = True
        #@override
        _field_key_seq_ = j2k
        #@override
        _field_key2seq_idx_ = k2j
    _check_field_key_infos6RecordType_(Record)
    assert not Record.__abstractmethods__
    Record.__module__ = __module__
    Record.__qualname__ = __qualname__
    _, _, __name__ = __qualname__.rpartition('.')
    Record.__name__ = __name__
    return Record



__all__
from seed.types.Record import mk_RecordType_
from seed.types.Record import *
