#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/codecs4int__alnum__abc.py

seed.int_tools.digits.codecs4int__alnum__abc
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.codecs4int__alnum__abc -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.codecs4int__alnum__abc:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   seed.int_tools.digits.codecs4int__alnum__abc   @f
]]]'''#'''
__all__ = r'''
ICodes4int
ICodes4uint
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
from seed.tiny_.check import check_type_is, check_int_ge

from seed.abc.abc__ver1 import abstractmethod, override, ABC
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

class ICodes4int(ABC):
    __slots__ = ()
    @abstractmethod
    def encode__int_(sf, i, /):
        'int -> str'
    @abstractmethod
    def _decode__int_ex_(sf, s, begin, end, /):
        'str -> begin/uint -> end/uint -> (int, next_begin)|^ValueError'
    def decode__int_(sf, s, begin=None, end=None, /, *, strict=True):
        'str -> int|^ValueError'
        (j, next_begin) = sf.decode__int_ex_(s, begin, end, strict=strict)
        return j
    def decode__int_ex_(sf, s, begin=None, end=None, /, *, strict=False):
        'str -> (int, next_begin)|^ValueError'
        (begin, end) = mk_seq_rng(s, begin, end)
        if not begin < end:raise ValueError
        r = sf._decode__int_ex_(s, begin, end)
        if strict:
            (j, next_begin) = r
            if not next_begin == end:raise ValueError
        return r

    def encode__ints_(sf, js, /):
        'Iter int -> str'
        return ''.join(map(sf.encode__int_, js))
    def decode__ints_(sf, s, begin=None, end=None, /, *, max_num_ints=None, strict=True):
        '-> [int]|^ValueError'
        (js, next_begin) = sf.decode__ints_ex_(s, begin, end, max_num_ints=max_num_ints, strict=strict)
        return js
    def decode__ints_ex_(sf, s, begin=None, end=None, /, *, max_num_ints=None, strict=False):
        '-> ([int], next_begin)|^ValueError'
        (begin, end) = mk_seq_rng(s, begin, end)
            #=> init:next_begin&&strict-check
        it = sf.iter_decode__ints_ex_(s, begin, end, strict=strict)
        if not max_num_ints is None:
            it = islice(it, 0, max_num_ints)
        js = []
        next_begin = begin
        for (j, next_begin) in it:
            js.append(j)
        if strict:
            if not next_begin == end:raise ValueError
        js = tuple(js)
        return (js, next_begin)
    def iter_decode__ints_ex_(sf, s, begin=None, end=None, /, *, strict=False):
        '-> Iter (int, next_begin)|^ValueError'
        (begin, end) = mk_seq_rng(s, begin, end)
        if not begin <= end:raise ValueError
        try:
            while not begin == end:
                r = sf._decode__int_ex_(s, begin, end)
                    #^ValueError
                yield r
                (j, next_begin) = r
                begin = next_begin
        except ValueError:
            if strict:
                raise
            else:
                pass
        #yield (True, begin)
#class ICodes4int(ABC):

class ICodes4uint(ICodes4int):
    __slots__ = ()
    @abstractmethod
    def encode__uint_(sf, i, /):
        'uint -> str'
    @abstractmethod
    def _decode__uint_ex_(sf, s, begin, end, /):
        'str -> begin/uint -> end/uint -> (uint, next_begin)|^ValueError'
    @override
    def encode__int_(sf, i, /):
        'int -> str'
        check_int_ge(0, i)
        u = i
        return sf.encode__uint_(u)
    @override
    def _decode__int_ex_(sf, s, begin, end, /):
        'str -> begin/uint -> end/uint -> (int, next_begin)|^ValueError'
        return sf._decode__uint_ex_(s, begin, end)
    def decode__uint_(sf, s, begin=None, end=None, /, *, strict=True):
        'str -> uint|^ValueError'
        return sf.decode__int_(s, begin, end, strict=strict)
    def decode__uint_ex_(sf, s, begin=None, end=None, /, *, strict=False):
        'str -> (uint, next_begin)|^ValueError'
        return sf.decode__int_ex_(s, begin, end, strict=strict)
    def encode__uints_(sf, us, /):
        'Iter uint -> str'
        return sf.encode__ints_(us)
    def decode__uints_(sf, s, begin=None, end=None, /, *, max_num_uints=None, strict=True):
        '-> [uint]|^ValueError'
        return sf.decode__ints_(s, begin, end, max_num_ints=max_num_uints, strict=strict)
    def decode__uints_ex_(sf, s, begin=None, end=None, /, *, max_num_uints=None, strict=False):
        '-> ([uint], next_begin)|^ValueError'
        return sf.decode__ints_ex_(s, begin, end, max_num_ints=max_num_uints, strict=strict)
    def iter_decode__uints_ex_(sf, s, begin=None, end=None, /, *, strict=False):
        '-> Iter (uint, next_begin)|^ValueError'
        return sf.iter_decode__ints_ex_(s, begin, end, strict=strict)
#class ICodes4uint(ICodes4int):


__all__
from seed.int_tools.digits.codecs4int__alnum__abc import ICodes4int, ICodes4uint
from seed.int_tools.digits.codecs4int__alnum__abc import *
