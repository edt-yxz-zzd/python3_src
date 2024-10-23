#__all__:goto
r'''
e ../../python3_src/seed/tiny_/bmk_pairs.py
[[
see:
    seed.tiny_.bmk_pairs
        bracket-make-pairs
        using __getitem__, not __call__

    seed.types.MakeDict
        baseclass
        using "class"

    seed.for_libs.for_inspect
        @decorator
        using api-signature #inspect.getfullargspec

    seed.helper.mk_pairs
        asm above
]]

py -m seed.tiny_.bmk_pairs
seed.tiny_.bmk_pairs
py -m nn_ns.app.debug_cmd   seed.tiny_.bmk_pairs -x
py -m nn_ns.app.doctest_cmd seed.tiny_.bmk_pairs:__doc__ -ht

++argpack@20241007


>>> from seed.tiny_.bmk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk


>>> bmk_pairs[1:2, 3:, :4, :, ::, ::None, []:{}]
((1, 2), (3, None), (None, 4), (None, None), (None, None), (None, None), ([], {}))
>>> ps = _
>>> show_ordered_pairs_as_bmk_pairs(ps)
'bmk_pairs[1: 2, 3: None, None: 4, None: None, None: None, None: None, []: {}]'
>>> show_ordered_pairs_as_bmk_pairs(ps, to_omit_None=True)
'bmk_pairs[1: 2, 3:, : 4, :, :, :, []: {}]'
>>> show_ordered_pairs_as_bmk_pairs(ps, to_omit_None=True, colon=':')
'bmk_pairs[1:2, 3:, :4, :, :, :, []:{}]'
>>> show_ordered_pairs_as_bmk_pairs(ps, to_shrink=True)
'bmk_pairs[1:2,3:,:4,:,:,:,[]:{}]'
>>> bmk_pairs[1:2,]
((1, 2),)
>>> show_ordered_pairs_as_bmk_pairs(_)
'bmk_pairs[1: 2]'
>>> bmk_pairs[()]
()
>>> show_ordered_pairs_as_bmk_pairs(_)
'bmk_pairs[()]'
>>> bmk_pairs[1:2]
((1, 2),)
>>> bmk_pairs[1:2, 3]
Traceback (most recent call last):
    ...
TypeError
>>> bmk_pairs[1:2:3,]
Traceback (most recent call last):
    ...
TypeError
>>> bmk_pairs[1]
Traceback (most recent call last):
    ...
TypeError


>>> bmk_triples[1:2:3, 4:, :5, ::6, :, ::, []:{}:()]
((1, 2, 3), (4, None, None), (None, 5, None), (None, None, 6), (None, None, None), (None, None, None), ([], {}, ()))
>>> ts = _
>>> show_ordered_triples_as_bmk_triples(ts)
'bmk_triples[1: 2: 3, 4: None: None, None: 5: None, None: None: 6, None: None: None, None: None: None, []: {}: ()]'
>>> show_ordered_triples_as_bmk_triples(ts, to_omit_None=True)
'bmk_triples[1: 2: 3, 4: :, : 5:, : : 6, : :, : :, []: {}: ()]'
>>> show_ordered_triples_as_bmk_triples(ts, to_omit_None=True, colon=':')
'bmk_triples[1:2:3, 4::, :5:, ::6, ::, ::, []:{}:()]'
>>> show_ordered_triples_as_bmk_triples(ts, to_shrink=True)
'bmk_triples[1:2:3,4::,:5:,::6,::,::,[]:{}:()]'
>>> bmk_triples[1:2:3,]
((1, 2, 3),)
>>> show_ordered_triples_as_bmk_triples(_)
'bmk_triples[1: 2: 3]'
>>> bmk_triples[()]
()
>>> show_ordered_triples_as_bmk_triples(_)
'bmk_triples[()]'
>>> bmk_triples[1:2:3]
((1, 2, 3),)
>>> bmk_triples[1:2:3, 4]
Traceback (most recent call last):
    ...
TypeError
>>> bmk_triples[1]
Traceback (most recent call last):
    ...
TypeError


>>> bmk_OrderedDict[3:4, 1:2]
OrderedDict([(3, 4), (1, 2)])
>>> show_ordered_dict_as_bmk_OrderedDict(_)
'bmk_OrderedDict[3: 4, 1: 2]'


>>> cased_bmk['{:}', 1:2]
{1: 2}
>>> cased_bmk['{:}',]
{}
>>> cased_bmk['{:}']
Traceback (most recent call last):
    ...
TypeError

>>> cased_bmk['[:]', 3:4, 1:2]
OrderedDict([(3, 4), (1, 2)])

>>> cased_bmk['{/}', 1]
{1}
>>> cased_bmk['[/]', 1]
[1]

>>> cased_bmk['{</>}', 1]
frozenset({1})
>>> cased_bmk['[</>]', 1]
(1,)


>>> bmk_argpack__grouped[::]
Traceback (most recent call last):
    ...
TypeError
>>> bmk_argpack__not_grouped[::]
Traceback (most recent call last):
    ...
TypeError
>>> bmk_argpack__grouped[1:2:]
Traceback (most recent call last):
    ...
TypeError
>>> bmk_argpack__not_grouped[:2:3]
Traceback (most recent call last):
    ...
TypeError




>>> bmk_argpack__grouped[()]
((),)
>>> bmk_argpack__not_grouped[()]
((),)
>>> bmk_argpack__grouped[:111:]
((111,),)
>>> bmk_argpack__not_grouped[:111:]
((111,),)

>>> bmk_argpack__grouped[999::666,:111:,888::777,22::44,:33:,:55:,66::77]
((111, 33, 55), ((999, 666), (888, 777), (22, 44), (66, 77)))
>>> bmk_argpack__not_grouped[999::666,:111:,888::777,22::44,:33:,:55:,66::77]
((), ((999, 666),), (111,), ((888, 777), (22, 44)), (33, 55), ((66, 77),))


#>>> mk_argpack_()
#>>> mk_argpack_(b=1,a=2)
#>>> mk_argpack_(3,b=1,a=2)
#>>> mk_argpack_(3,4,b=1,a=2)
#>>> mk_argpack_(3,4,a=2)
#>>> mk_argpack_(3,4)
#>>> mk_argpack_(3)

>>> mk_argpack_()
((),)
>>> mk_argpack_(b=1,a=2)
((), (('a', 2), ('b', 1)))
>>> mk_argpack_(3,b=1,a=2)
((3,), (('a', 2), ('b', 1)))
>>> mk_argpack_(3,4,b=1,a=2)
((3, 4), (('a', 2), ('b', 1)))
>>> mk_argpack_(3,4,a=2)
((3, 4), (('a', 2),))
>>> mk_argpack_(3,4)
((3, 4),)
>>> mk_argpack_(3)
((3,),)


>>> show_argpack_(None, ())
Traceback (most recent call last):
    ...
TypeError
>>> show_argpack_(None, ((),))
'bmk_argpack__grouped[()]'
>>> show_argpack_(None, bmk_argpack__grouped[()])
'bmk_argpack__grouped[()]'
>>> show_argpack_(None, bmk_argpack__grouped[:111:])
'bmk_argpack__grouped[:111]'
>>> show_argpack_(None, bmk_argpack__grouped[999::666,:111:,888::777,22::44,:33:,:55:,66::77])
'bmk_argpack__grouped[:111, :33, :55, 999::666, 888::777, 22::44, 66::77]'
>>> show_argpack_(None, bmk_argpack__not_grouped[()])
'bmk_argpack__grouped[()]'
>>> show_argpack_(None, bmk_argpack__not_grouped[:111:])
'bmk_argpack__grouped[:111]'
>>> show_argpack_(None, bmk_argpack__not_grouped[999::666,:111:,888::777,22::44,:33:,:55:,66::77])
'bmk_argpack__not_grouped[999::666, :111, 888::777, 22::44, :33, :55, 66::77]'




#'''

__all__ = r'''
    bmk_pairs
    bmk_triples
    bmk_OrderedDict
    cased_bmk

    show_ordered_pairs_as_bmk_pairs
    show_ordered_triples_as_bmk_triples

    show_ordered_pairs_as_bmk_OrderedDict
    show_ordered_dict_as_bmk_OrderedDict



check_argpack
mk_argpack_
show_argpack_
bmk_argpack__grouped
    bmk_argpack__not_grouped














check_argpack
mk_argpack_
    mk_argpackZ
        mk_argpackEM
            mk_argpackEO
show_argpack_
    show_argpack8bracket_only
        show_argpack_item_
            show_kwarg6argpack
            show_arg6argpack
cased_argpack_item2bracket_item
    cased_argpack_item5bracket_item
bmk_argpack__grouped
    bmk_argpack__not_grouped







'''.split()#'''
#BracketMaker
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from collections import OrderedDict
from itertools import chain, cycle
from seed.tiny_.containers import mk_pair, mk_pair_tuple, mk_tuple
#from seed.tiny_.containers import is_pair
from seed.tiny_.check import check_type_is, check_pair# check_int_ge

___end_mark_of_excluded_global_names__0___ = ...



class _Common4BMk:
    def __getattribute__(sf, attr, /):
        raise AttributeError
_get = object.__getattribute__
class BracketMaker(_Common4BMk):
    def __init__(sf, may_mk, may_b_maker, /):
        if not (may_mk is None or callable(may_mk)): raise TypeError
        if not (may_b_maker is None or hasattr(type(may_b_maker), '__getitem__')): raise TypeError
        sf._may_mk = may_mk
        sf._may_b_maker = may_b_maker
    def __getitem__(sf, k, /):
        may_b_maker = _get(sf, '_may_b_maker')
        may_mk = _get(sf, '_may_mk')

        r = k
        if may_b_maker is not None:
            b_maker = may_b_maker
            r = b_maker[r]
        if may_mk is not None:
            mk = may_mk
            r = mk(r)
        return r
class _BMk4CasedKey(_Common4BMk):
    def __init__(sf, case2mk_bmk_pair, /):
        if not (callable(case2mk_bmk_pair)): raise TypeError
        sf._case2mk_bmk_pair = case2mk_bmk_pair
    def __getitem__(sf, k, /):
        case2mk_bmk_pair = _get(sf, '_case2mk_bmk_pair')
        if not type(k) is tuple: raise TypeError
        if not len(k) > 0: raise TypeError

        case = k[0]
        r = k[1:]
        mk, may_b_maker = case2mk_bmk_pair(case)
        if not callable(mk): raise TypeError
        if may_b_maker is not None:
            b_maker = may_b_maker
            r = b_maker[r]
        r = mk(r)
        return r

class _BMkPairs(_Common4BMk):
    def __getitem__(sf, slices4pairs, /):
        if type(slices4pairs) is slice:
            slices4pairs = (slices4pairs,)
        if not type(slices4pairs) is tuple: raise TypeError
        if not all(type(slice_) is slice for slice_ in slices4pairs): raise TypeError
        if not all(slice_.step is None for slice_ in slices4pairs): raise TypeError
        return tuple((slice_.start, slice_.stop) for slice_ in slices4pairs)

def _repr_then_strip__but_omit_None(may_x, /):
    if may_x is None:
        return ''
    x = may_x
    return _repr_then_strip(x)
def _repr_then_strip(x, /):
    return repr(x).strip()
def _join_(to_omit_None, colon, /, *args):
    _repr = _repr_then_strip__but_omit_None if to_omit_None else _repr_then_strip
    s = colon.join(map(_repr, args))
    return s.strip()

def _prepare(iterable, colon, comma, name, to_omit_None, /, *, to_shrink):
    iterable = iter(iterable)
    to_omit_None = bool(to_omit_None)
    if to_shrink:
        to_omit_None = True
        colon = colon.strip()
        comma = comma.strip()
    name = name.strip()
    return (iterable, colon, comma, name, to_omit_None)
def show_ordered_pairs_as_bmk_pairs(pairs, /, *, colon=': ', comma=', ', name='bmk_pairs', to_omit_None=False, to_shrink=False):
    (pairs, colon, comma, name, to_omit_None) = _prepare(pairs, colon, comma, name, to_omit_None, to_shrink=to_shrink); del to_shrink
    s = comma.join(_join_(to_omit_None, colon, x, y) for x, y in pairs)
    s = s.strip()
    if not s:
        s = '()'
    return f'{name}[{s}]'


bmk_pairs = _BMkPairs()



class _BMkTriples(_Common4BMk):
    def __getitem__(sf, slices4triples, /):
        if type(slices4triples) is slice:
            slices4triples = (slices4triples,)
        if not type(slices4triples) is tuple: raise TypeError
        if not all(type(slice_) is slice for slice_ in slices4triples): raise TypeError
        return tuple((slice_.start, slice_.stop, slice_.step) for slice_ in slices4triples)

def show_ordered_triples_as_bmk_triples(triples, /, *, colon=': ', comma=', ', name='bmk_triples', to_omit_None=False, to_shrink=False):
    (triples, colon, comma, name, to_omit_None) = _prepare(triples, colon, comma, name, to_omit_None, to_shrink=to_shrink); del to_shrink
    to_omit_None = bool(to_omit_None)
    triples = iter(triples)
    s = comma.join(_join_(to_omit_None, colon, x, y, z) for x, y, z in triples)
    s = s.strip()
    if not s:
        s = '()'
    return f'{name}[{s}]'


bmk_triples = _BMkTriples()


bmk_OrderedDict = BracketMaker(OrderedDict, bmk_pairs)
def show_ordered_pairs_as_bmk_OrderedDict(pairs, /, *, colon=': ', comma=', ', name='bmk_OrderedDict', to_omit_None=False, to_shrink=False):
    return show_ordered_pairs_as_bmk_pairs(pairs, colon=colon, comma=comma, name=name, to_omit_None=to_omit_None, to_shrink=to_shrink)
def show_ordered_dict_as_bmk_OrderedDict(mapping, /, *, colon=': ', comma=', ', name='bmk_OrderedDict', to_omit_None=False, to_shrink=False):
    pairs = mapping.items()
    return show_ordered_pairs_as_bmk_OrderedDict(pairs, colon=colon, comma=comma, name=name, to_omit_None=to_omit_None, to_shrink=to_shrink)

_case2mk = {
    #ordered? frozen/immutable?
    #[]vs{}; <>vs~~
    '{:}': (dict, bmk_pairs)
    ,'[:]': (OrderedDict, bmk_pairs)
    ,'{/}': (set, None)
    ,'[/]': (list, None)
    ,'{</>}': (frozenset, None)
    ,'[</>]': (tuple, None)
    }
cased_bmk = _BMk4CasedKey(_case2mk.__getitem__)

__all__
from seed.tiny_.bmk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk



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
######################

def check_argpack(x, /, *, grouped):
    'SHOULDBE [args{maybe-empty}, (kwarg_pairs{nonempty}, args{nonempty}, ...)?]'
    check_type_is(tuple, x)
    if not x:raise TypeError
    if grouped and not len(x) <= 2:raise TypeError
    for y in x:
        check_type_is(tuple, y)
    for i, y in enumerate(x):
        if not (y or i==0):raise TypeError
        if i&1:
            for z in y:
                check_pair(z)

def mk_argpack_(*args, **kwargs):
    return mk_argpackZ(args, sorted(kwargs.items()))
def mk_argpackZ(args, kwarg_pairs, /):
    'Z:2:pair:(args, kwarg_pairs)'
    return mk_argpackEM([(False, args), (True, kwarg_pairs)], to_group=False)
def mk_argpackEM(eithers, /, *, to_group):
    'Iter (Either args kwarg_pairs) -> [args{maybe-empty}, (kwarg_pairs{nonempty}, args{nonempty}, ...)?] #E:Either,M:many'
    def f():
        for is_kvs, xs in eithers:
            check_type_is(bool, is_kvs)
            if is_kvs:
                yield from ((is_kvs, kv) for kv in map(mk_pair, xs))
            else:
                yield from ((is_kvs, v) for v in xs)
    return mk_argpackEO(f(), to_group=to_group)

def mk_argpackEO(eithers, /, *, to_group):
    'Iter (Either arg kwarg_pair) -> [args{maybe-empty}, (kwarg_pairs{nonempty}, args{nonempty}, ...)?] #E:Either,O:one-by-one'
    check_type_is(bool, to_group)
    if to_group:
        kvs = []
        vs = []
        put_kv = kvs.append
        put_v = vs.append
        def mk_result():
            if kvs:
                return (mk_tuple(vs), mk_tuple(kvs))
            return (mk_tuple(vs),)
    else:
        #ess = []
        #prev = ...
        #prev = True # is_kv@(-1), (not is_kv)@0, ...
        ess = [[]]
        prev = False # is_kv@(-1), (not is_kv)@0, ...
        def put(same, y, /):
            if not same:
                ess.append([y])
            else:
                ess[-1].append(y)
        def mk_result():
            return mk_tuple(map(mk_tuple, ess))
        def put_kv(kv, /):
            put(prev is is_kv, kv)
        def put_v(v, /):
            put(prev is is_kv, v)
                #bug:put(prev is not is_kv, v)
    for is_kv, y in eithers:
        if is_kv:
            put_kv(y)
        else:
            put_v(y)
        prev = is_kv
    argpack = mk_result()
    assert argpack
    #assert all(rs or i==0 for i, rs in enumerate(argpack))
    #from seed.tiny import print_err
    #if 0b001:print_err(argpack)
    check_argpack(argpack, grouped=to_group)
    return argpack

def show_kwarg6argpack(x, /):
    k,v = x
    if k is None is v:
        return 'True'#==is_kv
    return f'{k!r}::{v!r}'
def show_arg6argpack(x, /):
    if x is None:
        return 'False'#==is_kv
    return f':{x!r}'
def show_argpack_item_(is_kv, x, /):
    f = show_kwarg6argpack if is_kv else show_arg6argpack
    return f(x)
_fs4show_argpack = (show_arg6argpack, show_kwarg6argpack)
def show_argpack8bracket_only(argpack, /):
    check_argpack(argpack, grouped=False)
    fs = cycle(_fs4show_argpack)
    ss = ', '.join(s for f, xs in zip(fs, argpack) for s in map(f, xs))
    if not ss:
        ss = '()'
    return f'[{ss}]'
def cased_argpack_item2bracket_item(cased_argpack_item, /):
    '(Either arg kwarg_pair) -> (bool|slice)'
    (is_kv, x) = cased_argpack_item
    check_type_is(bool, is_kv)
    if is_kv:
        check_pair(x)
        k,v = x
        if k is None is v:
            return True#is_kv
        return slice(k,None,v)
    if x is None:
        return False#is_kv
    return slice(None, x, None)
def cased_argpack_item5bracket_item(bracket_item, /):
    '(bool|slice) -> (Either arg kwarg_pair)'
    z = bracket_item
    T = type(z)
    if T is slice:
        a = z.start
        b = z.stop
        c = z.step
        is_kv = b is None
        is_v = a is None is c
        if is_v is is_kv:raise TypeError
        if is_kv:
            return (is_kv, (a,c))
        return (is_kv, b)
    check_type_is(bool, z)
    is_kv = z
    if is_kv:
        return (is_kv, (None,None))
    return (is_kv, None)

class _BMkArgPack(_Common4BMk):
    to_group = True
    def __getitem__(sf, bracket_items, /):
        if not type(bracket_items) is tuple:
            bracket_item = bracket_items
            bracket_items = (bracket_item,)
        check_type_is(tuple, bracket_items)
        it = map(cased_argpack_item5bracket_item, bracket_items)
        argpack = mk_argpackEO(it, to_group=type(sf).to_group)
        return argpack
class _BMkArgPack__not_grouped(_BMkArgPack):
    to_group = False


bmk_argpack__grouped = _BMkArgPack()
bmk_argpack__not_grouped = _BMkArgPack__not_grouped()
def show_argpack_(may_header_or_grouped, argpack, /):
    'may (str|bool) -> argpack -> str'
    check_type_is(tuple, argpack)
    if may_header_or_grouped is None:
        header_or_grouped = len(argpack) <= 2
    else:
        header_or_grouped = may_header_or_grouped
    if type(header_or_grouped) is bool:
        grouped = header_or_grouped
        header = 'bmk_argpack__grouped' if grouped else 'bmk_argpack__not_grouped'
    else:
        header = header_or_grouped
    check_type_is(str, header)
    s = show_argpack8bracket_only(argpack)
    return header + s


if 0:
    #del _ #otherwise doctest not set result to "_"
    #   now remove 『def _():』
    pass
from seed.tiny_.bmk_pairs import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):



from seed.tiny_.bmk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk
from seed.tiny_.bmk_pairs import check_argpack, mk_argpack_, show_argpack_, bmk_argpack__grouped, bmk_argpack__not_grouped
from seed.tiny_.bmk_pairs import (check_argpack
,mk_argpack_
,    mk_argpackZ
,        mk_argpackEM
,            mk_argpackEO
,show_argpack_
,    show_argpack8bracket_only
,        show_argpack_item_
,            show_kwarg6argpack
,            show_arg6argpack
,cased_argpack_item2bracket_item
,    cased_argpack_item5bracket_item
,bmk_argpack__grouped
,    bmk_argpack__not_grouped
)


from seed.tiny_.bmk_pairs import *
