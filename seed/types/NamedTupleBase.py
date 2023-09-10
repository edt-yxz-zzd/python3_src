#__all__:goto
r'''[[[
e ../../python3_src/seed/types/NamedTupleBase.py
    view ../../python3_src/seed/types/namedtuple.txt
    view ../../python3_src/seed/types/NamedTupleBase.py
        allow '._xxx' # __getattribute__ # only field_names, no other methods
        allow '.def' # py_kw # getattr
        support stable_repr
    view ../../python3_src/seed/types/namedtuple.py
        forbid '._xxx' # to avoid '.py.namedtuple._fields...'
        forbid '.def' # py_kw
        not yet support stable_repr
    view ../../python3_src/seed/types/ImmutableNamespaceBase.py
        similar:basecls
        not yet support stable_repr
    view ../../python3_src/seed/types/NamedTuple__split_table.py
        reuse:Descriptor4NamedTuple
        not yet support stable_repr

    view ../../python3_src/seed/types/mk_ordered_field_name_seq_.py


    view ../../python3_src/seed/helper/repr_input.py
    view ../../python3_src/seed/helper/stable_repr.py

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



seed.types.NamedTupleBase
py -m nn_ns.app.debug_cmd   seed.types.NamedTupleBase -x
py -m nn_ns.app.doctest_cmd seed.types.NamedTupleBase:__doc__ -ff -v
py_adhoc_call   seed.types.NamedTupleBase   @f
from seed.types.NamedTupleBase import NamedTupleBase, mk_NamedTuple, as_dict, replace, extract_as, format_as, as_mapping_view, MappingView4NamedTuple


为了保证下面py_help的doctest例子:
    >>> from collections import namedtuple

[[[
py_help collections:namedtuple
===
namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
    Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

]]]



>>> from seed.types.NamedTupleBase import NamedTupleBase, mk_NamedTuple, as_dict, replace, extract_as, format_as, as_mapping_view, MappingView4NamedTuple


>>> class Pt(NamedTupleBase, ordered_field_name_seq='xy', field_defaults=[999], __module__='aaa.bbb'):pass
>>> Pt.__qualname__
'Pt'
>>> Pt.__name__
'Pt'
>>> Pt.__module__
'aaa.bbb'
>>> Pt.__doc__
'Pt(x, y)'
>>> str(Pt(11))
'Pt(x = 11, y = 999)'
>>> repr(Pt(11))
'Pt(11, 999)'
>>> p = Pt(11, y=22)
>>> p[:1]
(11,)
>>> p[:]
(11, 22)
>>> p[0] + p[1]
33
>>> x, y = p
>>> x, y
(11, 22)
>>> p.x + p.y
33
>>> d = Pt.___as_dict___(p)
>>> d['x']
11
>>> Pt(**d) #Pt(x = 11, y = 22)
Pt(11, 22)
>>> Pt.___replace___(p, x=100) #Pt(x = 100, y = 22)
Pt(100, 22)


>>> p.___replace___
Traceback (most recent call last):
    ...
AttributeError: ___replace___


>>> as_dict(p) == d == dict(x = 11, y = 22)
True
>>> replace(p, x=100) == Pt(x = 100, y = 22)
True
>>> extract_as(p, 'x, y, (y, [x])')
(11, 22, (22, [11]))
>>> format_as(p, '{x} * {y}')
'11 * 22'


>>> vw = as_mapping_view(p)
>>> vw
MappingView4NamedTuple(Pt(11, 22))
>>> len(vw)
2
>>> [*vw]
['x', 'y']
>>> {**vw} == d == dict(x = 11, y = 22)
True
>>> 'x' in vw
True
>>> vw['x']
11
>>> 0 in vw
False
>>> vw[0]
Traceback (most recent call last):
    ...
KeyError: 0




# ok: startswith "_"
# ok: py.keywords
>>> class C(NamedTupleBase, ordered_field_name_seq='_x def'.split(), field_name2default={'_x':666}):pass
>>> C(def=111)
Traceback (most recent call last):
    ...
SyntaxError: invalid syntax
>>> C(**{'def':111})
C(666, 111)
>>> str(C(**{'def':111})) #invalid syntax
'C(_x = 666, def = 111)'



#mk_NamedTuple
>>> T = mk_NamedTuple('C.B.XX', 'ab', defaults=[1])
>>> T.__qualname__
'C.B.XX'
>>> T.__name__
'XX'
>>> T.__module__
''
>>> T.__doc__
'C.B.XX(ab)'
>>> T()
XX(1)
>>> T(1)
XX(1)
>>> T(ab=1)
XX(1)

#space sep:
>>> T = mk_NamedTuple('YY', 'a b')
>>> T.__doc__
'YY(a, b)'
>>> T(1, 2)
YY(1, 2)
>>> T(1, 2).b
2

>>> T = mk_NamedTuple('ZZ', 'a b'.split())
>>> T.__doc__
'ZZ(a, b)'
>>> T(1, 2)
ZZ(1, 2)
>>> T(1, 2).b
2


>>> from seed.helper.stable_repr import stable_repr
>>> stable_repr(p)
'Pt(11, 22)'



Python 3.10.5 (main, Jun  7 2022, 03:52:12) [Clang 12.0.8 (https://android.googlesource.com/toolchain/llvm-project c935d99d7 on linux
#>>> from keyword import iskeyword, issoftkeyword
#>>> from keyword import kwlist, softkwlist
#>>> softkwlist
['_', 'case', 'match']
#>>> kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#>>> sorted(kwlist, key=len)
['as', 'if', 'in', 'is', 'or', 'and', 'def', 'del', 'for', 'not', 'try', 'None', 'True', 'elif', 'else', 'from', 'pass', 'with', 'False', 'async', 'await', 'break', 'class', 'raise', 'while', 'yield', 'assert', 'except', 'global', 'import', 'lambda', 'return', 'finally', 'continue', 'nonlocal']



#>>> T = mk_NamedTuple('XXX', 'as is or if in not try for def pass with from else elif class import lambda assert'.split())
>>> mk = lambda nm, a,b,c,d:mk_NamedTuple(nm, 'if in for def True from'.split(), len4impl_via_kwds4__repr__=a, len4impl_via_kwds4__str__=b, special4py_kw4__repr__=c, special4py_kw4__str__=d)
>>> T = mk('X0', 0, -1, True, True)
>>> L = len(T.descriptor4named_tuple)
>>> x0 = T(*range(L))
>>> x0.def
Traceback (most recent call last):
        x0.def
           ^^^
SyntaxError: invalid syntax
>>> x0.True
Traceback (most recent call last):
        x0.True
           ^^^^
SyntaxError: invalid syntax
>>> getattr(x0, 'def')
3
>>> getattr(x0, 'True')
4
>>> repr(T(*range(L)))
'X0(0, 1, 2, 3, 4, 5)'
>>> str(T(*range(L)))
"X0(**{'if': 0}, **{'in': 1}, **{'for': 2}, **{'def': 3}, **{'True': 4}, **{'from': 5})"
>>> X0 = T
>>> x0 == X0(0, 1, 2, 3, 4, 5)
True
>>> x0 == X0(**{'if': 0}, **{'in': 1}, **{'for': 2}, **{'def': 3}, **{'True': 4}, **{'from': 5})
True


>>> T = mk('X1', 0, -1, True, False)
>>> repr(T(*range(L)))
'X1(0, 1, 2, 3, 4, 5)'
>>> str(T(*range(L)))
'X1(if = 0, in = 1, for = 2, def = 3, True = 4, from = 5)'

>>> T = mk('X2', 3, -3, True, False)
>>> repr(T(*range(L)))
"X2(0, 1, 2, **{'def': 3}, **{'True': 4}, **{'from': 5})"
>>> str(T(*range(L)))
'X2(0, 1, for = 2, def = 3, True = 4, from = 5)'

>>> T = mk('X3', 3, -3, False, True)
>>> repr(T(*range(L)))
'X3(0, 1, 2, def = 3, True = 4, from = 5)'
>>> str(T(*range(L)))
"X3(0, 1, **{'for': 2}, **{'def': 3}, **{'True': 4}, **{'from': 5})"

>>> T = mk('X4', 2, -2, False, False)
>>> repr(T(*range(L)))
'X4(0, 1, 2, 3, True = 4, from = 5)'
>>> str(T(*range(L)))
'X4(0, in = 1, for = 2, def = 3, True = 4, from = 5)'



>>> pass

#]]]'''
__all__ = r'''
NamedTupleBase
        default4len4impl_via_kwds4__repr__
        default4len4impl_via_kwds4__str__
        default4special4py_kw4__repr__
        default4special4py_kw4__str__
    mk_NamedTuple
    as_dict
    replace
    extract_as
    format_as
    as_mapping_view
MappingView4NamedTuple

IndexedReadOnlyProperty
'''.split()#'''
__all__


#grep special -i -r ../../python3_src/seed/ -l -a
from seed.tiny_.call2getattr import get5cls, call5cls, get5cls_, call5cls_
from seed.types.NamedTuple__split_table import Descriptor4NamedTuple, gmk_Descriptor4NamedTuple #NamedTuple
from seed.types.mk_ordered_field_name_seq_ import mk_ordered_field_name_seq_, mk_field_name2default_
from seed.tiny_.check import check_pseudo_qual_name, check_pseudo_identifier, check_smay_pseudo_qual_name
from seed.tiny_.check import check_bool, check_uint, check_int_ge_lt, check_type_is
from seed.tiny import ifNone
from seed.helper.safe_eval import safe_eval# safe_exec, data_eval

from seed.helper.repr_input import repr_helper, repr_helper_ex
from seed.helper.stable_repr import IGetFuncNameArgsOrderedKwds4stable_repr, register4get__funcname__args__ordered_kwdxxxs
from seed.abc.abc__ver0 import abstractmethod, override, ABC, final

from collections.abc import Mapping
__all__


class IndexedReadOnlyProperty:
    def __init__(sf, name, idx, /):
        sf.name = name
        sf.idx = idx
    def __get__(sf, instance, owner, /):
        if instance is None:
            return sf
        return instance[sf.idx]

    # MUST define "__set__" to make sf a data_descriptor
    #   otherwise, instance override sf
    def __set__(sf, instance, value, /):
        raise AttributeError(sf.name)
    def __delete__(sf, instance, /):
        raise AttributeError(sf.name)
    def __repr__(sf, /):
        return repr_helper(sf, sf.name, sf.idx)

if 1:
    default4len4impl_via_kwds4__repr__=0#False#no-kwds
    default4len4impl_via_kwds4__str__=-1#True#no-args
    default4special4py_kw4__repr__=True
    default4special4py_kw4__str__=False
class NamedTupleBase(IGetFuncNameArgsOrderedKwds4stable_repr, tuple):
    'see:mk_NamedTuple'
    __slots__ = ()
    @classmethod
    def __init_subclass__(cls, /, *
        , ordered_field_name_seq=None
            # mimic: py.namedtuple._fields
        , type2ordered_field_name_seq=None
        , type_field_name4ordered_field_name_seq=None
        , field_name2default=None
        , field_defaults=()
        #, field_defaults=None
            # mimic: py.namedtuple._field_defaults
            #   right align
        , __module__=None
            # mimic: py.namedtuple:kw`module`
        , __qualname__=None
            #to generate __doc__
        , len4impl_via_kwds4__repr__=default4len4impl_via_kwds4__repr__
        , len4impl_via_kwds4__str__=default4len4impl_via_kwds4__str__
        , special4py_kw4__repr__=default4special4py_kw4__repr__
        , special4py_kw4__str__=default4special4py_kw4__str__
        , **kwargs
        ):
        ######################
        len4impl_via_kwds4__repr__ = ifNone(len4impl_via_kwds4__repr__, default4len4impl_via_kwds4__repr__)
        len4impl_via_kwds4__str__ = ifNone(len4impl_via_kwds4__str__, default4len4impl_via_kwds4__str__)
        special4py_kw4__repr__ = ifNone(special4py_kw4__repr__, default4special4py_kw4__repr__)
        special4py_kw4__str__ = ifNone(special4py_kw4__str__, default4special4py_kw4__str__)

        ######################
        check_type_is(int, len4impl_via_kwds4__repr__)
        check_type_is(int, len4impl_via_kwds4__str__)
        check_bool(special4py_kw4__repr__)
        check_bool(special4py_kw4__str__)
        ######################
        cls.len4impl_via_kwds4__repr__ = len4impl_via_kwds4__repr__
        cls.len4impl_via_kwds4__str__ = len4impl_via_kwds4__str__
        cls.special4py_kw4__repr__ = special4py_kw4__repr__
        cls.special4py_kw4__str__ = special4py_kw4__str__
        ######################

        ordered_field_name_seq = mk_ordered_field_name_seq_(cls
            , ordered_field_name_seq
            = ordered_field_name_seq
            , type2ordered_field_name_seq
            = type2ordered_field_name_seq
            , type_field_name4ordered_field_name_seq
            = type_field_name4ordered_field_name_seq
            )
        descriptor4named_tuple = gmk_Descriptor4NamedTuple(ordered_field_name_seq)
            #using:check_pseudo_identifier

        cls.ordered_field_name_seq = ordered_field_name_seq
        #cls.field_name_set = frozenset(ordered_field_name_seq)
        #cls.field_name2idx = ...
        cls.descriptor4named_tuple = descriptor4named_tuple
        assert cls.ordered_field_name_seq == cls.descriptor4named_tuple.idx2name is cls.descriptor4named_tuple.names

        if 0:
            #bug: may override cls.__xxx__
            #comment out this ==>> help() will show no item in section 『Data descriptors defined here:』
            for idx, name in enumerate(ordered_field_name_seq):
                setattr(cls, name, IndexedReadOnlyProperty(name, idx))

        ######################
        L = len(ordered_field_name_seq) #len(sf)
        L1 = L+1
        check_int_ge_lt(-L1, +L1, len4impl_via_kwds4__repr__)
        check_int_ge_lt(-L1, +L1, len4impl_via_kwds4__str__)

        ######################
        cls.field_name2default = mk_field_name2default_(ordered_field_name_seq, field_name2default=field_name2default, field_defaults=field_defaults)

        ######################
        __module__ = ifNone(__module__, cls.__module__)
        __module__ = ifNone(__module__, '')
        #check_pseudo_qual_name(__module__)
        check_smay_pseudo_qual_name(__module__)
        cls.__module__ = __module__
        ######################
        __qualname__ = ifNone(__qualname__, cls.__qualname__)
        #if not __qualname__ is None:
        if 1:
            qname4type = __qualname__
            check_pseudo_qual_name(qname4type)
            _, _, typename = qname4type.rpartition('.')
            cls.__name__ = typename
            cls.__qualname__ = qname4type
                #to generate __doc__
        s = ', '.join(ordered_field_name_seq)
        cls.__doc__ = f'{cls.__qualname__!s}({s!s})'


        super().__init_subclass__(**kwargs)
    #end-def __init_subclass__(cls, /, *, ...):

    def __new__(cls, /, *field_objs, **field_name2obj):
        cls.descriptor4named_tuple
        cls.field_name2default

        if field_name2obj or not len(field_objs) == len(cls.descriptor4named_tuple):
            xs = cls.descriptor4named_tuple.mk_tuple__fold(field_objs, field_name2obj, name2default=cls.field_name2default)
        else:
            xs = field_objs
        assert len(xs) == len(cls.descriptor4named_tuple)

        sf = super(__class__, cls).__new__(cls, xs)
        assert len(sf) == len(cls.descriptor4named_tuple)
        return sf
    def _repr_(sf, /, *, len4impl_via_kwds, special4py_kw):
        '[-1-len(sf) <= len4impl_via_kwds <= len(sf)]'
        L = len(sf)
        L1 = L+1
        check_int_ge_lt(-L1, +L1, len4impl_via_kwds)
        cls = type(sf)
        if len4impl_via_kwds < 0:
            len4impl_via_kwds += 1+L
        check_uint(len4impl_via_kwds)

        len4args = L-len4impl_via_kwds
        return repr_helper_ex(sf, sf[:len4args], cls.ordered_field_name_seq[len4args:], {}, ordered_attrs_only=True, special4py_kw=special4py_kw)
        cls = type(sf)

        if len4impl_via_kwds:
        #if impl_via_kwds:
            return repr_helper_ex(sf, [], cls.ordered_field_name_seq, {}, ordered_attrs_only=True, special4py_kw=special4py_kw)
        else:
            return repr_helper(sf, *sf)
    def __str__(sf, /):
        '[default:len4impl_via_kwds4__str__=-1][default:special4py_kw4__str__=False]:show as: "T(x = u, y = v)" #may be invalid syntax/keywords: T(def=...)'
        cls = type(sf)
        return cls._repr_(sf, len4impl_via_kwds=cls.len4impl_via_kwds4__str__, special4py_kw=cls.special4py_kw4__str__)
        cls = type(sf)
        return repr_helper_ex(sf, [], cls.ordered_field_name_seq, {}, ordered_attrs_only=True)
        #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
    def __repr__(sf, /):
        '[default:len4impl_via_kwds4__repr__=0]show as: "T(u, v)" #to avoid invalid syntax/keywords <<==T(def=...) cause SyntaxError'
        cls = type(sf)
        return cls._repr_(sf, len4impl_via_kwds=cls.len4impl_via_kwds4__repr__, special4py_kw=cls.special4py_kw4__repr__)
        return repr_helper(sf, *sf)
    @override
    def ___get__funcname__args__ordered_kwdxxxs___(sf):
        '-> (may func_name, args, (ordered_kwd_pairs/[(nm,v)]|ordered_field_names__str/str|ordered_either_Ellipsis_field_name_pair_or_kwd_pair__seq)/[((nm,v)|(Ellipsis,nm))])'
        if 1:
            return (None, [*sf], []) # <<== __repr__
        else:
            return (None, [], ' '.join(type(sf).descriptor4named_tuple.idx2name)) # <<== __str__

    r'''[[[
    def __len__(sf, /):
        #using tuple.__len__
    def __iter__(sf, /):
        #using tuple.__iter__
    def __reversed__(sf, /):
        #using tuple.__reversed__
    def __contains__(sf, /):
        #using tuple.__contains__
        #   [field_obj in sf] instead of [field_name in sf]
        #   see:__getitem__
    def __getitem__(sf, idx_or_slice, /):
        #using tuple.__getitem__
        #not accept "field_name" as input
        #   since [v in sf][sf[idx]] donot meet mapping interface --> bug:[nm in sf][sf[nm]]
        #see:__contains__
        #see:as_mapping_view/___as_mapping_view___/MappingView4NamedTuple
        #
    #]]]'''#'''
    def __getattribute__(sf, nm, /):
        'vs __getitem__'
        cls = type(sf)
        m = cls.descriptor4named_tuple.name2idx.get(nm)
        if m is None:
            raise AttributeError(nm)
        idx = m
        return sf[idx]

    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and tuple.__eq__(sf, ot) # <<== __hash__()
        ######################<==>:
        if not type(sf) is type(ot):
            return False # <<== __hash__()
            return NotImplemented
        return tuple.__eq__(sf, ot) # <<== __hash__()
        return super().__eq__(ot)
    def __hash__(sf, /):
        cls = type(sf)
        return hash(id(cls), tuple.__hash__(sf))
    if 0:
        def __dir__(sf, /):
            cls = type(sf)
            return sorted(cls.descriptor4named_tuple.idx2name)
                #py.dir() will sorted() result from __dir__
        #xxx:no ".__vars__":???vars() get .__dict__ bypass __getattribute__???: def __vars__(sf, /):


    def ___extract_as___(sf, pattern8target, /):
        return safe_eval(pattern8target, locals=as_dict(sf))
    def ___format_as___(sf, fmt, /, *args, **kwds):
        d = as_dict(sf)
        d.update(kwds) #overwrite
        return fmt.format(*args, **d)

    def ___as_mapping_view___(sf, /):
        return MappingView4NamedTuple(sf)
    def __getnewargs__(sf, /):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return (*sf,)
    def ___as_dict___(sf, /):
        'mimic: py.namedtuple._asdict'
        cls = type(sf)
        return cls.descriptor4named_tuple.mk_dict__star(*sf)
    def ___replace___(sf, /, **field_name2obj):
        'mimic: py.namedtuple._replace'
        if not field_name2obj:
            return sf
        cls = type(sf)
        d = cls.___as_dict___(sf)
        d.update(field_name2obj)
        return cls.make5dict(d)

    @classmethod
    def make5vars(cls, locals, /):
        field_name2obj = {nm:locals[nm] for nm in cls.descriptor4named_tuple.idx2name if nm in locals}
        return cls.make5dict(field_name2obj)
    @classmethod
    def make5dict(cls, field_name2obj, /):
        return cls(**field_name2obj)
    @classmethod
    def _make(cls, iterable, /):
        'mimic: py.namedtuple._make'
        return cls(*iterable)

class MappingView4NamedTuple(Mapping):
    def __init__(sf, named_tuple, /):
        sf._ntpl = named_tuple
    @property
    def the_named_tuple(sf, /):
        return sf._ntpl

    def __repr__(sf, /):
        return repr_helper(sf, sf._ntpl)
    def __len__(sf, /):
        return len(sf._ntpl)
    def __iter__(sf, /):
        T = type(sf._ntpl)
        return iter(T.descriptor4named_tuple.idx2name)
    def __getitem__(sf, field_name, /):
        'vs __getattribute__'
        T = type(sf._ntpl)
        idx = T.descriptor4named_tuple.name2idx[field_name]
            # ^KeyError(field_name)
        return sf._ntpl[idx]
        ###??bug:
        if not type(field_name) is str:
            #to avoid TypeError
            raise KeyError(field_name)
        try:
            return getattr(sf._ntpl, field_name) #??bug??
        except AttributeError:
            raise KeyError(field_name)
    def __hash__(sf, /):
        cls = type(sf)
        return hash(id(cls), hash(sf._ntpl))
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        return type(sf) is type(ot) and sf._ntpl == ot._ntpl # <<== __hash__()
MappingView4NamedTuple#(())



def as_mapping_view(sf, /):
    return call5cls.___as_mapping_view___(sf)
def as_dict(sf, /):
    return call5cls.___as_dict___(sf)
def replace(sf, /, **field_name2obj):
    return call5cls.___replace___(sf, **field_name2obj)
def extract_as(sf, pattern8target, /):
    return call5cls.___extract_as___(sf, pattern8target,)
def format_as(sf, fmt, /, *args, **kwds):
    return call5cls.___format_as___(sf, fmt, *args, **kwds)

def mk_NamedTuple(qname4type, field_names, /, *, defaults=None, module=None
    , len4impl_via_kwds4__repr__=default4len4impl_via_kwds4__repr__
    , len4impl_via_kwds4__str__=default4len4impl_via_kwds4__str__
    , special4py_kw4__repr__=default4special4py_kw4__repr__
    , special4py_kw4__str__=default4special4py_kw4__str__
    ):
    'see:NamedTupleBase'

    #check_pseudo_identifier(typename)
    check_pseudo_qual_name(qname4type)
    module = ifNone(module, '')
    if type(field_names) is str:
        field_names = field_names.split()
    class T(NamedTupleBase
        , ordered_field_name_seq=field_names
        , field_defaults=defaults
        , __module__=module
        , __qualname__=qname4type
        , len4impl_via_kwds4__repr__=len4impl_via_kwds4__repr__
        , len4impl_via_kwds4__str__=len4impl_via_kwds4__str__
        , special4py_kw4__repr__=special4py_kw4__repr__
        , special4py_kw4__str__=special4py_kw4__str__
        ):pass
    #assert T.__qualname__ == 'mk_NamedTuple.<locals>.T'
    #assert T.__name__ == 'T'
    #_, _, typename = qname4type.rpartition('.')
    #T.__qualname__ = qname4type
    #T.__name__ = typename
    return T

from seed.types.NamedTupleBase import NamedTupleBase, mk_NamedTuple, as_dict, replace, extract_as, format_as, as_mapping_view, MappingView4NamedTuple
from seed.types.NamedTupleBase import *
