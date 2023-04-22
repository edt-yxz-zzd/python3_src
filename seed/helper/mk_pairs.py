#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/mk_pairs.py
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


seed.helper.mk_pairs
py -m nn_ns.app.debug_cmd   seed.helper.mk_pairs
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.helper.mk_pairs   @f
py -m nn_ns.app.doctest_cmd seed.helper.mk_pairs:__doc__ -v


from seed.helper.mk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples#, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk

from seed.helper.mk_pairs import ListOrderedItems, ListOrderedItems__replace_then_move_to_end, ListSortedItems
    #__module__, __qualname__ need special treat... ==> see: seed.types.MakeDict

from seed.helper.mk_pairs import pairs5api_, pairs5api__zdefault_
from seed.helper.mk_pairs import pairs5api__raise, pairs5api__Nothing_, pairs5api__None

from seed.helper.mk_pairs import triples5api_, triples5api__zdefault_
from seed.helper.mk_pairs import triples5api__raise, triples5api__Nothing_, triples5api__None









>>> from seed.tiny import echo
>>> class ok(Exception):pass
>>> class bad(Exception):pass
>>> ok.__module__ = '__main__'
>>> bad.__module__ = '__main__'



[[pairs5api_
>>> from seed.helper.mk_pairs import pairs5api_, pairs5api__zdefault_
>>> from seed.helper.mk_pairs import pairs5api__raise, pairs5api__Nothing_, pairs5api__None


>>> @pairs5api__raise
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @pairs5api__raise
... def ps(a='aaa', b='bbb'):pass
>>> ps
[('a', 'aaa'), ('b', 'bbb')]
>>> @pairs5api__Nothing_(999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api__None
... def ps(a, b='bbb'):pass
>>> ps
[('a', None), ('b', 'bbb')]




>>> @pairs5api_
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @pairs5api_(None, 1, echo)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 'a'), ('b', 'bbb')]
>>> @pairs5api_(None, 999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api_
... def ps(a='aaa', b='bbb'):pass
>>> ps
[('a', 'aaa'), ('b', 'bbb')]
>>> @pairs5api_
... def ps(_0=999, /, a='aaa', b='bbb'):pass
>>> ps
[('_0', 999), ('a', 'aaa'), ('b', 'bbb')]
>>> @pairs5api__zdefault_(999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api__zdefault_(-1, 999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api__zdefault_(0, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok()), ('b', 'bbb')]
>>> @pairs5api__zdefault_(1, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok(111)), ('b', 'bbb')]
>>> @pairs5api__zdefault_(2, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok(222, 111)), ('b', 'bbb')]
>>> @pairs5api__zdefault_(4, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok('a', 333, 222, 111)), ('b', 'bbb')]

>>> @pairs5api__zdefault_()
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @pairs5api__zdefault_(-3- -1, bad(999))
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
bad: 999

]]
[[triples5api_
>>> from seed.helper.mk_pairs import triples5api_, triples5api__zdefault_
>>> from seed.helper.mk_pairs import triples5api__raise, triples5api__Nothing_, triples5api__None


>>> @triples5api__raise
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__raise
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__raise
... def ts(a:'aa'='aaa', b:'bb'='bbb'):pass
>>> ts
[('a', 'aa', 'aaa'), ('b', 'bb', 'bbb')]
>>> @triples5api__Nothing_(999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api__None
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', None, None), ('b', 'bb', 'bbb')]




>>> @triples5api_
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api_
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api_(None, 1, echo)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 'a', 'a'), ('b', 'bb', 'bbb')]
>>> @triples5api_(None, 999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api_
... def ts(a:'aa'='aaa', b:'bb'='bbb'):pass
>>> ts
[('a', 'aa', 'aaa'), ('b', 'bb', 'bbb')]

>>> @triples5api__zdefault_(999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(-1, 999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(0, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok(), ok()), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(1, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok(111), ok(111)), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(2, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok(222, 111), ok(222, 111)), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(4, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok('a', 333, 222, 111), ok('a', 333, 222, 111)), ('b', 'bb', 'bbb')]

>>> @triples5api__zdefault_()
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__zdefault_()
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__zdefault_(-3- -1, bad(999))
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
bad: 999
>>> @triples5api__zdefault_(-3- -1, bad(999))
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
bad: 999

]]
[[
__module__, __qualname__ need special treat... ==> see: seed.types.MakeDict

>>> from seed.helper.mk_pairs import ListOrderedItems, ListOrderedItems__replace_then_move_to_end, ListSortedItems

>>> class ps(ListSortedItems):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('a', 4), ('b', 5), ('c', 3)]
>>> class ps(ListOrderedItems):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('a', 4), ('c', 3), ('b', 5)]
>>> class ps(ListOrderedItems__replace_then_move_to_end):
...     a = 1
...     b = 2
...     c = 3
...     a = 4
...     del b; b = 5
>>> ps
[('c', 3), ('a', 4), ('b', 5)]

]]
[[
>>> from seed.helper.mk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples#, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk

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


]]







#]]]'''
__all__ = r'''
bmk_pairs
bmk_triples
    show_ordered_pairs_as_bmk_pairs
    show_ordered_triples_as_bmk_triples

    bmk_OrderedDict
        show_ordered_pairs_as_bmk_OrderedDict
        show_ordered_dict_as_bmk_OrderedDict

    cased_bmk


ListOrderedItems
    ListOrderedItems__replace_then_move_to_end
    ListSortedItems


pairs5api_
    pairs5api__zdefault_
    pairs5api__raise
    pairs5api__Nothing_
    pairs5api__None

triples5api_
    triples5api__zdefault_
    triples5api__raise
    triples5api__Nothing_
    triples5api__None

'''.split()#'''
__all__

######################
######################
######################
######################
######################
from seed.tiny_.bmk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk

from seed.types.MakeDict import ListOrderedItems, ListOrderedItems__replace_then_move_to_end, ListSortedItems

from seed.for_libs.for_inspect import pairs5api_, pairs5api__zdefault_
from seed.for_libs.for_inspect import pairs5api__raise, pairs5api__Nothing_, pairs5api__None

from seed.for_libs.for_inspect import triples5api_, triples5api__zdefault_
from seed.for_libs.for_inspect import triples5api__raise, triples5api__Nothing_, triples5api__None


######################
######################
######################
######################
######################
from seed.helper.mk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk

from seed.helper.mk_pairs import ListOrderedItems, ListOrderedItems__replace_then_move_to_end, ListSortedItems
    #__module__, __qualname__ need special treat... ==> see: seed.types.MakeDict

from seed.helper.mk_pairs import pairs5api_, pairs5api__zdefault_
from seed.helper.mk_pairs import pairs5api__raise, pairs5api__Nothing_, pairs5api__None

from seed.helper.mk_pairs import triples5api_, triples5api__zdefault_
from seed.helper.mk_pairs import triples5api__raise, triples5api__Nothing_, triples5api__None


