#__all__:goto
r'''[[[
e ../../python3_src/seed/types/NamedTuple__split_table.py
used in:
    nn_ns.codec.DecodeUtils


seed.types.NamedTuple__split_table
py -m nn_ns.app.debug_cmd   seed.types.NamedTuple__split_table -x
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.types.NamedTuple__split_table   @f
py -m nn_ns.app.doctest_cmd seed.types.NamedTuple__split_table:__doc__ -v
from seed.types.NamedTuple__split_table import NamedTuple, Descriptor4NamedTuple, gmk_Descriptor4NamedTuple


[[
class Descriptor4NamedTuple
    .name2idx[]
    .idx2name[]
    .names
    .idc
    #no:__iter__
    __len__
    __hash__
    __ne__
    __eq__
    .mk_tuple__fold()
    .mk_tuple__star()
    .mk_dict__fold()
    .mk_dict__star()
    .mk_partial_dict__fold()
    .mk_partial_dict__star()
gmk_Descriptor4NamedTuple = get_or_mk_Descriptor4NamedTuple = echo_or_lookup_or_mk_Descriptor4NamedTuple
]]



>>> from seed.types.NamedTuple__split_table import NamedTuple, Descriptor4NamedTuple, gmk_Descriptor4NamedTuple

>>> from seed.helper.mk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples#, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk

>>> from seed.helper.mk_pairs import ListOrderedItems, ListOrderedItems__replace_then_move_to_end, ListSortedItems #__module__, __qualname__ need special treat... ==> see: seed.types.MakeDict

>>> from seed.helper.mk_pairs import pairs5api_, pairs5api__zdefault_
>>> from seed.helper.mk_pairs import pairs5api__raise, pairs5api__Nothing_, pairs5api__None

>>> Descriptor4NamedTuple()
Traceback (most recent call last):
    ...
TypeError: Descriptor4NamedTuple.__new__() missing 1 required positional argument: 'sf_or_names'
>>> Descriptor4NamedTuple([])
Descriptor4NamedTuple([])
>>> gmk_Descriptor4NamedTuple([]) is gmk_Descriptor4NamedTuple([])
True
>>> gmk_Descriptor4NamedTuple([]) is Descriptor4NamedTuple([])
True
>>> null = Descriptor4NamedTuple([])
>>> len(null)
0
>>> bool(null)
False


>>> gmk_Descriptor4NamedTuple('bccbdaae')
Traceback (most recent call last):
    ...
KeyError: "duplicate_names: ['a', 'b', 'c']"
>>> gmk_Descriptor4NamedTuple([*'abc']) is gmk_Descriptor4NamedTuple([*'abc'])
True
>>> gmk_Descriptor4NamedTuple([*'abc']) is Descriptor4NamedTuple([*'abc'])
True
>>> abc = gmk_Descriptor4NamedTuple([*'abc'])
>>> abc
Descriptor4NamedTuple(['a', 'b', 'c'])
>>> len(abc)
3
>>> bool(abc)
True
>>> abc.names is abc.idx2name
True
>>> abc.idx2name
('a', 'b', 'c')

#mappingproxy({'a': 0, 'b': 1, 'c': 2})
>>> type(abc.name2idx) is MapView
True
>>> abc.name2idx == {'a': 0, 'b': 1, 'c': 2}
True




>>> iter(abc)
Traceback (most recent call last):
    ...
TypeError: 'Descriptor4NamedTuple' object is not iterable
>>> 'a' in abc
Traceback (most recent call last):
    ...
TypeError: argument of type 'Descriptor4NamedTuple' is not iterable
>>> abc['a']
Traceback (most recent call last):
    ...
TypeError: 'Descriptor4NamedTuple' object is not subscriptable
>>> abc[0]
Traceback (most recent call last):
    ...
TypeError: 'Descriptor4NamedTuple' object is not subscriptable





>>> abc = gmk_Descriptor4NamedTuple([*'abc'])
>>> xyz = gmk_Descriptor4NamedTuple([*'xyz'])
>>> abc._h is None
True
>>> abc == xyz
False
>>> abc._h is None
True
>>> xyz._h is None
True
>>> __ = hash(xyz);
>>> xyz._h is None
False
>>> abc == xyz
False
>>> abc._h is None
True
>>> __ = hash(abc);
>>> abc._h is None
False
>>> abc == xyz
False





>>> NamedTuple()
Traceback (most recent call last):
    ...
TypeError: NamedTuple.__new__() missing 1 required positional argument: 'items_or_descriptor4named_tuple_or_names'
>>> NamedTuple([])
NamedTuple([])
>>> NamedTuple([]) is NamedTuple([])
True
>>> len(NamedTuple([]))
0
>>> bool(NamedTuple([]))
False

>>> abc = gmk_Descriptor4NamedTuple([*'abc'])
>>> NamedTuple(abc, [111, 222])
Traceback (most recent call last):
    ...
TypeError
>>> NamedTuple(abc, [111, 222, 333, 444])
Traceback (most recent call last):
    ...
TypeError
>>> NamedTuple(abc, [111, 222, 333])
NamedTuple([('a', 111), ('b', 222), ('c', 333)])
>>> abc123 = _
>>> abc123.get_descriptor4named_tuple() is abc
True
>>> abc123.as_tuple()
(111, 222, 333)
>>> len(abc123)
3
>>> bool(abc123)
True
>>> [*iter(abc123)]
[111, 222, 333]
>>> [*reversed(abc123)]
[333, 222, 111]
>>> [*abc123.iter_items()]
[('a', 111), ('b', 222), ('c', 333)]
>>> abc123.idx2name is abc123.names is abc.idx2name
True
>>> abc123.name2idx == abc.name2idx
True

>>> abc123.get_(1)
222
>>> abc123.get_('b')
222
>>> abc123.getattr_('a')
111
>>> abc123.getitem_(2)
333


>>> abc123.as_getter4named_tuple()
_Getter4NamedTuple(NamedTuple([('a', 111), ('b', 222), ('c', 333)]))
>>> ns = _
>>> len(ns)
3
>>> bool(ns)
True
>>> [*iter(ns)]
[111, 222, 333]
>>> [*reversed(ns)]
[333, 222, 111]
>>> ns[...] is abc123
True
>>> ns[0]
111
>>> ns['a']
Traceback (most recent call last):
    ...
TypeError: tuple indices must be integers or slices, not str
>>> ns.a
111
>>> abc123._h is None
True
>>> ns == abc123.as_getter4named_tuple()
True
>>> ns is abc123.as_getter4named_tuple()
False
>>> abc123._h is None
True
>>> __ = hash(ns)
>>> abc123._h is None
False




>>> abc123 = NamedTuple(abc, [111, 222, 333])
>>> _abc123 = NamedTuple(abc, abc123)
>>> abc123._h is None
True
>>> abc123 is _abc123
False
>>> abc123 == _abc123
True
>>> abc123._h is None
True
>>> _abc123._h is None
True
>>> __ = hash(_abc123);
>>> _abc123._h is None
False
>>> abc123 == _abc123
True
>>> abc123._h is None
True
>>> __ = hash(abc123);
>>> abc123._h is None
False
>>> abc123 == _abc123
True




#]]]'''
__all__ = r'''
    NamedTuple
    Descriptor4NamedTuple
        echo_or_lookup_or_mk_Descriptor4NamedTuple
            get_or_mk_Descriptor4NamedTuple
            gmk_Descriptor4NamedTuple

'''.split()#'''
__all__


from seed.tiny import MapView, check_pseudo_identifier, check_type_is, mk_tuple
from seed.tiny import echo, fst as fst_, snd as snd_
from seed.tiny import ifNone
from seed.helper.repr_input import repr_helper
from seed.iters.duplicate_elements import iter_duplicate_representative_elements



_names2descriptor4named_tuple = {}
#def mk_Descriptor4NamedTuple(sf_or_names, /):
def echo_or_lookup_or_mk_Descriptor4NamedTuple(sf_or_names, /):
    '(Descriptor4NamedTuple|[name]) -> Descriptor4NamedTuple'
    return _descriptor4named_tuple5or_names(sf_or_names)
gmk_Descriptor4NamedTuple = get_or_mk_Descriptor4NamedTuple = echo_or_lookup_or_mk_Descriptor4NamedTuple

def _descriptor4named_tuple5or_names(descriptor4named_tuple_or_names, /):
    '(Descriptor4NamedTuple|[name]) -> Descriptor4NamedTuple'
    if type(descriptor4named_tuple_or_names) is Descriptor4NamedTuple:
        descriptor4named_tuple = descriptor4named_tuple_or_names
    else:
        names = descriptor4named_tuple_or_names
        descriptor4named_tuple = _lookup_or_mk_Descriptor4NamedTuple(names)
    return descriptor4named_tuple

def _lookup_or_mk_Descriptor4NamedTuple(names, /):
    '[name] -> Descriptor4NamedTuple'
    names = mk_tuple(names)
    d = _names2descriptor4named_tuple
    if not names in d:
        #d[names] = Descriptor4NamedTuple(names)
        sf = object.__new__(Descriptor4NamedTuple)
        sf._init(names)
        d[names] = sf
    pass
    descriptor4named_tuple = d[names]
    return descriptor4named_tuple

class _MIXINS:
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        return sf is ot or (type(sf) is type(ot) and (sf._h is None or ot._h is None or sf._h==ot._h) and sf._get_args_used_in_hash() == ot._get_args_used_in_hash())
    def __hash__(sf, /):
        if sf._h is None:
            sf._h = hash(sf._get_args_used_in_hash())
        return sf._h
class Descriptor4NamedTuple(_MIXINS):
    'see:echo_or_lookup_or_mk_Descriptor4NamedTuple'
    #__iter__ = None
    def __repr__(sf, /):
        return repr_helper(sf, [*sf.names])
    def __new__(cls, sf_or_names, /):
        if not cls is __class__:raise TypeError(cls)
        return echo_or_lookup_or_mk_Descriptor4NamedTuple(sf_or_names)
    def __init__(sf, sf_or_names, /):
        #empty __init__() body to avoid double-init
        #   sf may be old <<== echo_or_lookup_or_mk_Descriptor4NamedTuple lookuo cache
        pass
    def _init(sf, names, /):
        names = mk_tuple(names)
        for nm in names:
            check_pseudo_identifier(nm)
        name2idx = {nm:idx for idx,nm in enumerate(names)}
        if not len(name2idx) == len(names):
            duplicate_names = iter_duplicate_representative_elements(names)
            duplicate_names = sorted(duplicate_names)
            raise KeyError(f'duplicate_names: {duplicate_names}')

        name2idx = MapView(name2idx)
        sf._i2nm = names
        sf._nm2i = name2idx
        sf._h = None
    @property
    def name2idx(sf, /):
        return sf._nm2i
    @property
    def idx2name(sf, /):
        return sf._i2nm
    names = idx2name
    @property
    def idc(sf, /):
        return range(len(sf))
    #def __iter__(sf, /): #use idx2name/names instead
    def __len__(sf, /):
        return len(sf.names)
    def _get_args_used_in_hash(sf, /):
        return (id(type(sf)), len(sf), sf.names)
    def mk_tuple__star(sf, /, *args, **kwargs):
        return sf.mk_tuple__fold(args, kwargs)
    def mk_tuple__fold(sf, args, kwargs, /, *, name2default=None):
        if 0:
            nm2obj = sf.mk_dict__fold(args, kwargs)
            return tuple(nm2obj[nm] for nm in sf.idx2name)
        (objs, nm2obj) = _prepare4mk_dict__fold(sf, args, kwargs, partial=False, may_name2default=name2default)
        for nm in sf.idx2name[len(objs):]:
            objs.append(nm2obj[nm])
        if not len(objs) == len(sf):raise logic-err
        return tuple(objs)
    def mk_dict__star(sf, /, *args, **kwargs):
        return sf.mk_dict__fold(args, kwargs)
    def mk_dict__fold(sf, args, kwargs, /, *, partial=False, name2default=None):
        partial = bool(partial)
        (objs, nm2obj) = _prepare4mk_dict__fold(sf, args, kwargs, partial=partial, may_name2default=name2default)
        for nm, obj in zip(sf.idx2name, objs):
            #if nm in nm2obj: raise logic-err
            nm2obj[nm] = obj
        if not partial:
            if not len(nm2obj) == len(sf):raise logic-err
            if not nm2obj.keys() == sf.name2idx.keys():raise logic-err
        else:
            if not len(nm2obj) <= len(sf):raise logic-err
            if not nm2obj.keys() <= sf.name2idx.keys():raise logic-err
        return nm2obj
    def mk_partial_dict__star(sf, /, *args, **kwargs):
        return sf.mk_partial_dict__fold(args, kwargs)
    def mk_partial_dict__fold(sf, args, kwargs, /):
        return sf.mk_dict__fold(args, kwargs, partial=True)

#end-class Descriptor4NamedTuple:
def _prepare4mk_dict__fold(sf, args, kwargs, /, *, partial, may_name2default):
    #args = mk_tuple(args)
    objs = [*args]
    if not len(objs) <= len(sf):raise TypeError
    nm2obj = {**kwargs}
    _nms = {*sf.idx2name[len(objs):]}

    name2default = ifNone(may_name2default, {})
    while 1:
        if 1:
            #partial____pass
            if not len(objs)+len(nm2obj) <= len(sf):raise TypeError
            if not nm2obj.keys() <= _nms:raise TypeError

        unfill_nms = _nms - nm2obj.keys()
        #filling_nms = (unfill_nms & name2default.keys())
        filling_nms = {nm for nm in unfill_nms if nm in name2default}
        if not filling_nms:
            break
        for nm in filling_nms:
            nm2obj[nm] = name2default[nm]
    nm2obj, unfill_nms

    if partial:
        #see:above:partial____pass
        pass
    else:
        if not len(objs)+len(nm2obj) == len(sf):raise TypeError
        if not nm2obj.keys() == _nms:raise TypeError
    return (objs, nm2obj)

_og = object.__getattribute__
class _Getter4NamedTuple:
    def __repr__(sf, /):
        return repr_helper(sf, sf[...])
    def __init__(sf, named_tuple, /):
        check_type_is(NamedTuple, named_tuple)
        sf._ntpl = named_tuple
    def __getattribute__(sf, nm, /):
        return sf[...].getattr_(nm)
    def __getitem__(sf, x, /):
        if ... is x:
            return _og(sf, '_ntpl')
        return sf[...].getitem_(x)
    def __len__(sf, /):
        return len(sf[...])
    def __iter__(sf, /):
        return iter(sf[...])
    def __reversed__(sf, /):
        return reversed(sf[...])
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        return sf is ot or (type(sf) is type(ot) and sf[...] == ot[...])
    def __hash__(sf, /):
        #bug:return hash((id(type(sf)), sf[...]))
        return hash((id(type(sf)), hash(sf[...])))
    if 0:
        def __dir__(sf, /):
            return sorted(sf[...].idx2name)
                #py.dir() will sorted() result from __dir__
        #xxx:no ".__vars__":???vars() get .__dict__ bypass __getattribute__???: def __vars__(sf, /):


class NamedTuple(_MIXINS):
    r'''[[[
    see:NamedTuple
    see:Descriptor4NamedTuple
    see: seed.helper.mk_pairs::bmk_pairs,pairs5api_,ListOrderedItems
    ]]]'''#'''
    def __repr__(sf, /):
        return repr_helper(sf, [*sf.iter_items()])
        return repr_helper(sf, [*sf.names], [*sf.as_tuple()])
    def __new__(cls, items_or_descriptor4named_tuple_or_names, may_iterable=None, /):
        global _null_NamedTuple
        if not cls is __class__:raise TypeError(cls)
        sf = object.__new__(__class__)
        sf._init(items_or_descriptor4named_tuple_or_names, may_iterable)
        if not sf:
            try:
                sf = _null_NamedTuple
            except NameError:
                _null_NamedTuple = sf
            assert sf is _null_NamedTuple
        return sf

    def __init__(sf, items_or_descriptor4named_tuple_or_names, may_iterable=None, /):
        pass
    def _init(sf, items_or_descriptor4named_tuple_or_names, may_iterable=None, /):
        if may_iterable is None:
            items = items_or_descriptor4named_tuple_or_names
            items = [(nm,v) for nm,v in items]
            names = map(fst_, items)
            iterable = map(snd_, items)
            descriptor4named_tuple_or_names = names
            del names, items
        else:
            iterable = may_iterable
            descriptor4named_tuple_or_names = items_or_descriptor4named_tuple_or_names
        ######################
        del may_iterable
        del items_or_descriptor4named_tuple_or_names
        descriptor4named_tuple_or_names
        iterable
        ######################

        #descriptor4named_tuple = _descriptor4named_tuple5or_names(descriptor4named_tuple_or_names)
        descriptor4named_tuple = echo_or_lookup_or_mk_Descriptor4NamedTuple(descriptor4named_tuple_or_names)
        ls = mk_tuple(iterable)
        del iterable
        ######################
        if not len(ls) == len(descriptor4named_tuple):raise TypeError
        sf._dsptr = descriptor4named_tuple
        sf._ls = ls
        sf._h = None
    def as_tuple(sf, /):
        return sf._ls
    def get_descriptor4named_tuple(sf, /):
        return sf._dsptr
    def as_getter4named_tuple(sf, /):
        return _Getter4NamedTuple(sf)
    def iter_items(sf, /):
        return zip(sf.names, sf.as_tuple())

    @property
    def name2idx(sf, /):
        return sf.get_descriptor4named_tuple().name2idx
    @property
    def idx2name(sf, /):
        return sf.get_descriptor4named_tuple().idx2name
    names = idx2name

    def __len__(sf, /):
        return len(sf.as_tuple())
    def __iter__(sf, /):
        return iter(sf.as_tuple())
    def __reversed__(sf, /):
        return reversed(sf.as_tuple())
    def get_(sf, nm_or_idx_or_slice, /):
        if type(nm_or_idx_or_slice) is str:
            nm = nm_or_idx_or_slice
            v = sf.getattr_(nm)
        else:
            x = idx_or_slice = nm_or_idx_or_slice
            v = sf.getitem_(x)
        return v
    def getattr_(sf, nm, /):
        check_pseudo_identifier(nm)
        try:
            i = sf.name2idx[nm]
        except KeyError:
            raise AttributeError(nm)
        return sf.getitem_(i)
    def getitem_(sf, x, /):
        '(int|slice) -> elem'
        return sf.as_tuple()[x]


    def _get_args_used_in_hash(sf, /):
        return (id(type(sf)), len(sf), sf.get_descriptor4named_tuple(), sf.as_tuple())
_null_NamedTuple = NamedTuple([])
#end-class NamedTuple:



from seed.types.NamedTuple__split_table import NamedTuple, Descriptor4NamedTuple, gmk_Descriptor4NamedTuple
from seed.types.NamedTuple__split_table import *
