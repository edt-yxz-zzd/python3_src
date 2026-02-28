#__all__:goto
r'''[[[
e ../../python3_src/seed/types/LazyDict8Array.py
view ../../python3_src/seed/types/LazyValueDict.py
view ../../python3_src/seed/types/DefaultDict.py

seed.types.LazyDict8Array
py -m nn_ns.app.debug_cmd   seed.types.LazyDict8Array -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.LazyDict8Array:__doc__ -ht # -ff -df
#######

[[
LazyDict8Array(len, key2val_):
  LazyDict(key2val_)
  Dict8Array(len, d)
]]


'#'; __doc__ = r'#'

########
>>> ls = mk_LazyDict8Array_(10, str)
>>> len(ls)
10
>>> ls
Dict8Array(10, DefaultDict2({}, 1, <class 'str'>))
>>> ls[:-1:-1]
()
>>> ls
Dict8Array(10, DefaultDict2({}, 1, <class 'str'>))

>>> ls[:-2:-1]
('9',)
>>> ls
Dict8Array(10, DefaultDict2({9: '9'}, 1, <class 'str'>))

>>> ls[1:2]
('1',)
>>> ls
Dict8Array(10, DefaultDict2({9: '9', 1: '1'}, 1, <class 'str'>))

>>> ls[-3]
'7'
>>> ls
Dict8Array(10, DefaultDict2({9: '9', 1: '1', 7: '7'}, 1, <class 'str'>))

>>> ls[3]
'3'
>>> ls
Dict8Array(10, DefaultDict2({9: '9', 1: '1', 7: '7', 3: '3'}, 1, <class 'str'>))

>>> ls[::-3]
('9', '6', '3', '0')
>>> ls
Dict8Array(10, DefaultDict2({9: '9', 1: '1', 7: '7', 3: '3', 6: '6', 0: '0'}, 1, <class 'str'>))

>>> [*ls]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']




########
>>> ls = mk_LazyDict8Array_ex_(10, lambda d, j:j if j < 2 else d[j-2]+d[j-1])
>>> len(ls)
10
>>> ls #doctest: +ELLIPSIS
Dict8Array(10, DefaultDict2({}, 2, <function <lambda> at 0x...>))

>>> ls[5]
5
>>> ls #doctest: +ELLIPSIS
Dict8Array(10, DefaultDict2({1: 1, 0: 0, 2: 1, 3: 2, 4: 3, 5: 5}, 2, <function <lambda> at 0x...>))

>>> ls[6:9]
(8, 13, 21)
>>> [*ls]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]





########
>>> ls = mk_LazyDict8Array_(10, str, smay_repr='j2digit')
>>> ls
j2digit
>>> ls._repr_()
"Dict8Array(10, DefaultDict2({}, 1, <class 'str'>))"
>>> repr(ls)
'j2digit'
>>> str(ls)
'j2digit'
>>> ascii(ls)
'j2digit'

########
>>> from seed.types.Symbol import P
>>> 靶值讠最小显链长 = P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()
>>> 靶值讠最小显链长
P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()
>>> 靶值讠最小显链长 is eval(repr(靶值讠最小显链长))
True
>>> 靶值讠最小显链长[12509]
17


py_adhoc_call   '' @str   %%:P  ='P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()[12509]'
    =>『'17'』
py_adhoc_call   '' @str   %%:P  ='P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()'
    =>『'P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()'』







########
py_adhoc_call   seed.types.LazyDict8Array   @f
]]]'''#'''
__all__ = r'''
mk_LazyDict8Array_ex_ex_
    mk_LazyDict_ex_ex_
mk_LazyDict8Array_ex_
    mk_LazyDict_ex_
mk_LazyDict8Array_
    mk_LazyDict_
    Dict8Array
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
from seed.types.DefaultDict import DefaultDict2
    #DefaultDict2(mapping, ncall, value_mkr, /, *ex_args):
    #   [-1 <= ncall <= 2]: (d,k)
from collections.abc import Sequence #MutableMapping
___end_mark_of_excluded_global_names__0___ = ...


def mk_LazyDict8Array_ex_ex_(sz, may_mapping, ncall, value_mkr, /, *ex_args, smay_repr=''):
    'sz/uint -> may d/{k:v} -> ncall/(imay uint%3) -> (case ncall of {-1=>v; 0=>((*ex_args)->v); 1=>(k -> (*ex_args) -> v); 2=>(LazyDict{k:v} -> k -> (*ex_args) -> v);}) -> (*ex_args) -> LazyDict8Array{j:v}'
    d = mk_LazyDict_ex_ex_(may_mapping, ncall, value_mkr, *ex_args)
    seq = Dict8Array(sz, d, smay_repr=smay_repr)
    return seq
def mk_LazyDict8Array_ex_(sz, d_j2val_, may_mapping=None, /, *, smay_repr=''):
    'sz/uint -> (LazyDict{j:v} -> j/uint%sz -> v) -> may d/{j:v} -> LazyDict8Array{j:v}'
    return mk_LazyDict8Array_ex_ex_(sz, may_mapping, 2, d_j2val_, smay_repr=smay_repr)
    #.d = mk_LazyDict_ex_(d_j2val_, may_mapping)
    #.seq = Dict8Array(sz, d)
    #.return seq
def mk_LazyDict8Array_(sz, j2val_, may_mapping=None, /, *, smay_repr=''):
    'sz/uint -> (j/uint%sz -> v) -> may d/{j:v} -> LazyDict8Array{j:v}'
    return mk_LazyDict8Array_ex_ex_(sz, may_mapping, 1, j2val_, smay_repr=smay_repr)
    #.d = mk_LazyDict_(j2val_, may_mapping)
    #.seq = Dict8Array(sz, d)
    #.return seq

def mk_LazyDict_ex_ex_(may_mapping, ncall, value_mkr, /, *ex_args):
    'may d/{k:v} -> ncall/(imay uint%3) -> (case ncall of {-1=>v; 0=>((*ex_args)->v); 1=>(k -> (*ex_args) -> v); 2=>(LazyDict{k:v} -> k -> (*ex_args) -> v);}) -> (*ex_args) -> LazyDict{k:v}'
    mapping = {} if None is may_mapping else may_mapping
    return DefaultDict2(mapping, ncall, value_mkr, *ex_args)
def mk_LazyDict_ex_(d_key2val_, may_mapping=None, /):
    '(LazyDict{k:v} -> k -> v) -> may d/{k:v} -> LazyDict{k:v}'
    return mk_LazyDict_ex_ex_(may_mapping, 2, d_key2val_)
def mk_LazyDict_(key2val_, may_mapping=None, /):
    '(k -> v) -> may d/{k:v} -> LazyDict{k:v}'
    return mk_LazyDict_ex_ex_(may_mapping, 1, key2val_)

class Dict8Array(Sequence):
    def __init__(sf, sz, d, /, *, smay_repr=''):
        check_int_ge(0, sz)
        check_type_is(str, smay_repr)
        sf._sz = sz
        sf._d = d
        sf._sm = smay_repr
    def _repr_(sf, /):
        args = (sf._sz, sf._d)
        return f'Dict8Array{args}'
    def __repr__(sf, /):
        smay_repr = sf._sm
        if smay_repr:
            return smay_repr
        return sf._repr_()
    def __len__(sf, /):
        return sf._sz
    def _at(sf, j, /):
        #no:check
        #check_int_ge_lt(0, len(sf), j)
        #assert j >= 0
        return sf._d[j]
    def __getitem__(sf, j_or_sl, /):
        #.if type(j_or_sl) is slice:
        #.    sl = j_or_sl
        #.else:
        #.    j = j_or_sl
        j_or_js = range(len(sf))[j_or_sl]
        if type(j_or_js) is range:
            js = j_or_js
            return tuple(map(sf._at, js))
        else:
            j = j_or_js
            #check_int_ge_lt(0, len(sf), j)
            return sf._at(j)
__all__
from seed.types.LazyDict8Array import mk_LazyDict8Array_ex_ex_, mk_LazyDict_ex_ex_, Dict8Array
#def mk_LazyDict8Array_ex_ex_(sz, may_mapping, ncall, value_mkr, /, *ex_args, smay_repr=''):
from seed.types.LazyDict8Array import mk_LazyDict8Array_ex_, mk_LazyDict_ex_, Dict8Array
#def mk_LazyDict8Array_ex_(sz, d_j2val_, may_mapping=None, /, *, smay_repr=''):
from seed.types.LazyDict8Array import mk_LazyDict8Array_, mk_LazyDict_, Dict8Array
#def mk_LazyDict8Array_(sz, j2val_, may_mapping=None, /, *, smay_repr=''):
from seed.types.LazyDict8Array import *
