#py -m seed.tiny_.containers
__all__ = '''
    mk_immutable_seq
        mk_immutable_seq5iterT_
        mk_immutable_seq5iter__
        mk_bytes5iter_

    mk_Just
    mk_Left
    mk_Right

    mk_frozenset
    mk_tuple
        mk_pair
        mk_pair_tuple
            is_pair

    null_str
    null_bytes
    null_int
    null_tuple
    null_frozenset
    null_mapping_view
    null_iter
    '''.split()
from types import MappingProxyType as MapView



def mk_Just(x, /):
    #null_tuple
    return (x,)
def mk_Left(x, /):
    return (False, x)
def mk_Right(x, /):
    return (True, x)

def mk_frozenset(iterable, /):
    return _mk_immutable(frozenset, null_frozenset, iterable)
def mk_tuple(iterable, /):
    return _mk_immutable(tuple, null_tuple, iterable)
def mk_pair(iterable, /):
    if type(iterable) is tuple:
        if len(iterable) == 2:
            return iterable
        raise TypeError(len(iterable))
    (x, y) = iterable
    return (x, y)
def is_pair(x, /):
    return type(x) is tuple and len(x) == 2
def mk_pair_tuple(iterable, /):
    'see also:view ../../python3_src/seed/helper/mk_pairs.py'
    if type(iterable) is tuple:
        if all(map(is_pair, iterable)):
            return iterable
    return mk_tuple(map(mk_pair, iterable))

def _mk_immutable(ImmutableType, null, iterable, /):
    if type(iterable) is ImmutableType:
        x = iterable
    else:
        x = ImmutableType(iterable)
    if not x:
        x = null
    return x



null_str = ''
null_bytes = b''
null_int = 0
null_tuple = ()
null_frozenset = frozenset()
null_mapping_view = MapView({})
null_iter = iter(null_str)#iter(())

assert mk_Just(1) == (1,)
assert mk_Left(1) == (False, 1)
assert mk_Right(1) == (True, 1)
assert mk_tuple([]) is null_tuple
assert mk_frozenset([]) is null_frozenset
assert null_str == ''
assert null_bytes == b''
assert null_int == 0
assert null_tuple == ()
assert null_frozenset == frozenset()
assert type(null_mapping_view) is MapView and not null_mapping_view
assert iter(null_iter) is null_iter
assert next(null_iter, [..., {}]) == [..., {}]
assert next(null_iter, None) is None

#null_range = range(0)
#assert not null_range
#[] = null_range

_types4immutable_seq = (tuple, str, bytes, range)
#_nulls4immutable_seq = (null_tuple, null_str, null_bytes, null_range)
_nulls4immutable_seq = (null_tuple, null_str, null_bytes, null_tuple)
def mk_immutable_seq(iterable, /):
    'Iter a -> (tuple a | str | bytes | range) #vs:mk_tuple'
    if not type(iterable) in _types4immutable_seq:
        seq = mk_tuple(iterable)
    else:
        seq = iterable
    if not seq:
        seq = null_tuple
    return seq
    ######################
    try:
        j = _types4immutable_seq.index(type(iterable))
    except IndexError:
        seq = mk_tuple(iterable)
    else:
        seq = iterable
        if not seq:
            seq = _nulls4immutable_seq[j]
    return seq
assert mk_immutable_seq('') is null_tuple
assert mk_immutable_seq(b'') is null_tuple
assert mk_immutable_seq(range(9,9)) is null_tuple
assert mk_immutable_seq(()) is null_tuple

assert mk_immutable_seq(__:='a') is __
assert mk_immutable_seq(__:=b'a') is __
assert mk_immutable_seq(__:=range(999)) is __
assert mk_immutable_seq(__:=(999,)) is __
assert mk_immutable_seq([999]) == (999,)

import builtins as _B
def mk_immutable_seq5iterT_(T, /):
    'type{==(tuple|str|bytes|bytearray|?range?)} -> (Iter x -> [x])'
    match T:
        case _B.tuple | _B.range:
            return mk_immutable_seq
        case _B.str:
            return ''.join
        case _B.bytes | _B.bytearray:
            return mk_bytes5iter_
            return bytes
            return b''.join
        case _:
            raise TypeError(T)
    raise 000
def _iter_bss(xs, /):
    'Iter (uint%256 | bytes) -> Iter bytes'
    for x in xs:
        try:
            bs = bytes([x])
        except TypeError:
            bs = x
        bs
        yield bs
def mk_bytes5iter_(xs, /):
    'Iter (uint%256 | bytes) -> bytes'
    bss = _iter_bss(xs)
    return b''.join(bss)
def mk_immutable_seq5iter__(T, xs, /):
    'type{==(tuple|str|bytes|bytearray|?range?)} -> Iter x -> [x]'
    return mk_immutable_seq5iterT_(T)(xs)
assert mk_immutable_seq5iter__(str, iter('abc')) == 'abc'
assert mk_immutable_seq5iter__(bytes, iter(b'abc')) == b'abc'
assert mk_immutable_seq5iter__(bytearray, iter(b'abc')) == bytearray(b'abc')
assert mk_immutable_seq5iter__(tuple, iter('abc')) == tuple('abc')
assert mk_immutable_seq5iter__(range, iter('abc')) == tuple('abc')


def mk_tuple__split_first_if_str(xs, /, chars8blank=''):
    '(str|Iter x) -> (chars8blank="") -> tuple{str|x}'
    if type(xs) is str:
        s = xs
        if not chars8blank:
            pass
        elif len(chars8blank) == 1:
            ch = chars8blank
            s = s.replace(ch, ' ')
        else:
            tbl = dict.fromkeys(map(ord, chars8blank), ' ')
            s = s.translate(tbl)
        s
        xs = s.split()
    xs = mk_tuple(xs)
    return xs
assert mk_tuple__split_first_if_str(b'0 1') == (48, 32, 49)
assert mk_tuple__split_first_if_str('0 1') == ('0', '1')
assert mk_tuple__split_first_if_str('0 1,2') == ('0', '1,2')
assert mk_tuple__split_first_if_str('0 1,2', ',') == ('0', '1', '2')
assert mk_tuple__split_first_if_str('0 1,2;3', ',') == ('0', '1', '2;3')
assert mk_tuple__split_first_if_str('0 1,2;3', ',;') == ('0', '1', '2', '3')



from seed.tiny_.containers import mk_tuple__split_first_if_str

from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right
from seed.tiny_.containers import mk_immutable_seq, mk_immutable_seq5iterT_, mk_immutable_seq5iter__, mk_bytes5iter_

from seed.tiny_.containers import mk_pair, mk_pair_tuple
from seed.tiny_.containers import is_pair
from seed.tiny_.containers import *
