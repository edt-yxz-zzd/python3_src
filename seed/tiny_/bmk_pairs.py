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


#'''

__all__ = '''
    bmk_pairs
    bmk_triples
    bmk_OrderedDict
    cased_bmk

    show_ordered_pairs_as_bmk_pairs
    show_ordered_triples_as_bmk_triples

    show_ordered_pairs_as_bmk_OrderedDict
    show_ordered_dict_as_bmk_OrderedDict
    '''.split()

from collections import OrderedDict

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

from seed.tiny_.bmk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk

if 0:
    #del _ #otherwise doctest not set result to "_"
    #   now remove 『def _():』
    pass
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):




