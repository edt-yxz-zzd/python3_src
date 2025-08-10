#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/RadixInfo.py

seed.int_tools.RadixInfo
py -m nn_ns.app.debug_cmd   seed.int_tools.RadixInfo -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.RadixInfo:__doc__ -ht # -ff -df

[[
源起:
    view ../../python3_src/seed/int_tools/concat_digits2bytes.py
    view ../../python3_src/seed/int_tools/digits/codecs4int.py
]]

######################
test ZpowRadixInfo
>>> r16 = ZpowRadixInfo(4)
>>> r16
ZpowRadixInfo(4)
>>> r16.num_bits4digit
4
>>> r16.radix
16
>>> r16.max_digit
15



######################
test 『mk_ZpowRadixInfo_』
0x00041/65 128
#>>> dir(_mk_ZpowRadixInfo_)
>>> def f(i,sz):
...     for k in range(i,i+sz):
...         ZpowRadixInfo(k)
>>> _mk_ZpowRadixInfo_.cache_info()
CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
>>> f(0, 0x00041)
>>> _mk_ZpowRadixInfo_.cache_info()
CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
>>> f(0, 0x00041)
>>> _mk_ZpowRadixInfo_.cache_info()
CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
>>> f(0x00041, 128)
>>> _mk_ZpowRadixInfo_.cache_info()
CacheInfo(hits=0, misses=128, maxsize=128, currsize=128)
>>> f(0x00041, 128)
>>> _mk_ZpowRadixInfo_.cache_info()
CacheInfo(hits=128, misses=128, maxsize=128, currsize=128)
>>> f(0x00041+128, 1)
>>> _mk_ZpowRadixInfo_.cache_info()
CacheInfo(hits=128, misses=129, maxsize=128, currsize=128)

######################




######################
test RadixInfo
>>> r7 = RadixInfo(7)
>>> r7
RadixInfo(7)
>>> r7.radix
7
>>> r7.max_digit
6
>>> r7.num_bits4digit
Traceback (most recent call last):
    ...
AttributeError: num_bits4digit

>>> r16 = RadixInfo(16)
>>> r16
RadixInfo(16)
>>> r16.radix
16
>>> r16.max_digit
15
>>> r16.num_bits4digit
4

>>> r7.is_zpow_radix
False
>>> r16.is_zpow_radix
True


######################
test 『mk_RadixInfo_』
0x00101/257 128
#>>> dir(_mk_RadixInfo_)
>>> def f(i,sz):
...     for k in range(i,i+sz):
...         RadixInfo(k)
>>> _mk_RadixInfo_.cache_info()
CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
>>> f(1, 0x00101-1)
>>> _mk_RadixInfo_.cache_info()
CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
>>> f(1, 0x00101-1)
>>> _mk_RadixInfo_.cache_info()
CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
>>> f(0x00101, 128)
>>> _mk_RadixInfo_.cache_info()
CacheInfo(hits=0, misses=128, maxsize=128, currsize=128)
>>> f(0x00101, 128)
>>> _mk_RadixInfo_.cache_info()
CacheInfo(hits=128, misses=128, maxsize=128, currsize=128)
>>> f(0x00101+128, 1)
>>> _mk_RadixInfo_.cache_info()
CacheInfo(hits=128, misses=129, maxsize=128, currsize=128)

######################




######################
test:RadixedDigit
>>> rdgt = RadixedDigit(r16, 7)
>>> rdgt
RadixedDigit(RadixInfo(16), 7)
>>> rdgt.radix_info
RadixInfo(16)
>>> rdgt.digit
7


######################





py_adhoc_call   seed.int_tools.RadixInfo   @f
from seed.int_tools.RadixInfo import *
]]]'''#'''
__all__ = r'''
IRadixInfo
    RadixInfo
        mk_RadixInfo_
    IZpowRadixInfo
        ZpowRadixInfo
            mk_ZpowRadixInfo_
IRadixedDigit
    RadixedDigit
        rxdigit8no_bits
'''.split()#'''
    #flip_digits_
    #flip_rxdigit_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property
#.from collections import namedtuple
from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_
from functools import lru_cache
from seed.tiny_.check import check_type_is, check_int_ge
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
[count_num_leading1s_,count_num_leading1s_ex_,count_num_leading0s_,count_num_leading0s_ex_] = lazy_import4funcs_('seed.int_tools.count_num_leading1s', 'count_num_leading1s_,count_num_leading1s_ex_,count_num_leading0s_,count_num_leading0s_ex_', __name__)
if 0:from seed.int_tools.count_num_leading1s import count_num_leading1s_, count_num_leading1s_ex_
    #(num_leading1s, imay_num_bits4payload) = count_num_leading1s_ex_(num_bits4digit, max_digit, digit)
if 0:from seed.int_tools.count_num_leading1s import count_num_leading0s_, count_num_leading0s_ex_
    #(num_leading0s, imay_num_bits4payload) = count_num_leading0s_ex_(num_bits4digit, digit)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError


class IRadixInfo(ABC):
    'radix_info'
    __slots__ = ()
    @property
    @abstractmethod
    def radix(sf, /):
        '-> uint{>=1}'
    @property
    @abstractmethod
    def max_digit(sf, /):
        '-> (uint%radix){==radix-1}'
    @property
    @abstractmethod
    def is_zpow_radix(sf, /):
        '-> bool{radix==2**???} # [hasattr .num_bits4digit]'
    @property
    @abstractmethod
    def num_bits4digit(sf, /):
        '-> uint{>=0} if is_zpow_radix else ^AttributeError'
    ######################
    def flip_digits_(sf, digits, /):
        'Iter digit/uint%radix -> Iter digit'
        #xxx:'[.is_zpow_radix] => Iter digit/uint%2**num_bits4digit -> Iter digit'
        #.assert sf.is_zpow_radix
        mask = sf.max_digit
        #.f = mask.__xor__
        f = mask.__xor__ if sf.is_zpow_radix else mask.__sub__
        return map(f, digits)
    def count_num_leading1s_(sf, digit, /):
        '[.is_zpow_radix] => digit/uint%2**num_bits4digit -> num_leading1s/uint%(1+num_bits4digit)'
        return sf.count_num_leading1s_ex_(digit)[0]
    def count_num_leading1s_ex_(sf, digit, /):
        '[.is_zpow_radix] => digit/uint%2**num_bits4digit -> (num_leading1s, imay_num_bits4payload)/(uint%(1+num_bits4digit), imay uint%num_bits4digit) # [num_bits4digit==num_leading1s+1[#(maybe nonexist) the "0" bit#]+imay_num_bits4payload]'
        return count_num_leading1s_ex_(sf.num_bits4digit, sf.max_digit, digit)
    def count_num_leading0s_(sf, digit, /):
        '[.is_zpow_radix] => digit/uint%2**num_bits4digit -> num_leading0s/uint%(1+num_bits4digit)'
        return sf.count_num_leading0s_ex_(digit)[0]
    def count_num_leading0s_ex_(sf, digit, /):
        '[.is_zpow_radix] => digit/uint%2**num_bits4digit -> (num_leading0s, imay_num_bits4payload)/(uint%(1+num_bits4digit), imay uint%num_bits4digit) # [num_bits4digit==num_leading0s+1[#(maybe nonexist) the "1" bit#]+imay_num_bits4payload]'
        return count_num_leading0s_ex_(sf.num_bits4digit, digit)
    ######################
    ######################
    @property
    def is_null(sf, /):
        '-> bool{[radix == 1]}'
        return sf.radix == 1
    ######################
#end-class IRadixInfo(ABC):
class IZpowRadixInfo(IRadixInfo):
    'zpow_radix_info #zpow radix only'
    __slots__ = ()
    #@override
    is_zpow_radix = True
    @property
    @abstractmethod
    @override
    def num_bits4digit(sf, /):
        '-> uint{>=0}'
    @property
    @abstractmethod
    @override
    def radix(sf, /):
        '-> uint{>=1}{==2**num_bits4digit}'
#end-class IZpowRadixInfo(ABC):








######################
class ZpowRadixInfo(IZpowRadixInfo):
    ___no_slots_ok___ = True
    def __new__(cls, /, num_bits4digit, radix=None, max_digit=None, *, _new=False):
        if not _new:
            return mk_ZpowRadixInfo_(num_bits4digit, radix, max_digit)
        check_int_ge(0, num_bits4digit)
        #check_int_ge(1, radix)
        #check_int_ge(0, max_digit)

        sf = super(__class__, cls).__new__(cls)
        sf._nb = num_bits4digit
        if not radix is None:
            sf._R = radix
        if not max_digit is None:
            sf._9 = max_digit
        return sf
    def __eq__(sf, ot, /):
        if ot is sf:return True
        if not isinstance(__class__, ot):return NotImplemented
        return sf.num_bits4digit == ot.num_bits4digit
    def __hash__(sf, /):
        return hash((__class__, sf.radix))
    def __repr__(sf, /):
        return repr_helper(sf, sf.num_bits4digit)
        #bug:return f'ZpowRadixInfo({sf.radix})'
        return f'ZpowRadixInfo({sf.num_bits4digit})'
    @property
    @override
    def num_bits4digit(sf, /):
        '-> uint{>=0}'
        return sf._nb
    @property
    @override
    def radix(sf, /):
        '-> uint{>=1}{==2**num_bits4digit}'
        try:
            return sf._R
        except AttributeError:
            pass
        sf._R = 1<<sf.num_bits4digit
        sf._R
        return sf.radix
    @property
    @override
    def max_digit(sf, /):
        '-> (uint%radix){==radix-1}'
        try:
            return sf._9
        except AttributeError:
            pass
        sf._9 = sf.radix-1
        sf._9
        return sf.max_digit
    def _assign(sf, /, radix=None, max_digit=None):
        if radix and not hasattr(sf, '_R'):
            sf._R = radix
        if not None is max_digit and not hasattr(sf, '_9'):
            sf._9 = max_digit
#end-class ZpowRadixInfo(IZpowRadixInfo):
assert 0x00041 == 65
_j2zri = tuple(ZpowRadixInfo(j, _new=True) for j in range(0x00041))
def mk_ZpowRadixInfo_(num_bits4digit, radix=None, max_digit=None):
    if num_bits4digit < 0x00041:
        assert num_bits4digit >= 0
        zri = _j2zri[num_bits4digit]
    else:
        zri = _mk_ZpowRadixInfo_(num_bits4digit)
        zri._assign(radix, max_digit)
    return zri
@lru_cache(maxsize=128)
def _mk_ZpowRadixInfo_(num_bits4digit):
    return ZpowRadixInfo(num_bits4digit, _new=True)












######################
class RadixInfo(IRadixInfo):
    ___no_slots_ok___ = True
    def __new__(cls, /, radix, max_digit=None, *, _new=False):
        if not _new:
            return mk_RadixInfo_(radix, max_digit)
        check_int_ge(1, radix)
        #check_int_ge(0, max_digit)
        sf = super(__class__, cls).__new__(cls)
        sf._R = radix
        if not max_digit is None:
            sf._9 = max_digit
        return sf
        #.if max_digit is None:
        #.    max_digit = radix-1
        #.b_zpow = (radix&max_digit) == 0
        #.b_zpow = radix.bit_count()==1
        #.if b_zpow:
        #.    bsz = max_digit.bit_length()
        #.    sf = ZpowRadixInfo(bsz, radix, max_digit)
        #.else:
        #.    sf = super(__class__, cls).__new__(cls)
        #.    sf._R = radix
        #.    sf._9 = max_digit
        #.return sf

    def __eq__(sf, ot, /):
        if ot is sf:return True
        if not isinstance(__class__, ot):return NotImplemented
        return sf.radix == ot.radix
    def __hash__(sf, /):
        return hash((__class__, sf.radix))
    def __repr__(sf, /):
        return repr_helper(sf, sf.radix)
        return f'RadixInfo({sf.radix})'
    @property
    @override
    def radix(sf, /):
        '-> uint{>=1}{==2**num_bits4digit}'
        return sf._R
    @property
    @override
    def max_digit(sf, /):
        '-> (uint%radix){==radix-1}'
        try:
            return sf._9
        except AttributeError:
            pass
        sf._9 = sf.radix-1
        sf._9
        return sf.max_digit
    def _assign(sf, /, max_digit=None):
        if not None is max_digit and not hasattr(sf, '_9'):
            sf._9 = max_digit

    @property
    @override
    def is_zpow_radix(sf, /):
        '-> bool{radix==2**???} # [hasattr .num_bits4digit]'
        try:
            return sf._b_zpow
        except AttributeError:
            pass
        sf._b_zpow = not (sf.radix & sf.max_digit)
        return sf.is_zpow_radix
    @property
    @override
    def num_bits4digit(sf, /):
        '-> uint{>=0} if is_zpow_radix else ^AttributeError'
        try:
            return sf._nb
        except AttributeError:
            pass
        if not sf.is_zpow_radix:
            #not zpow
            raise AttributeError('num_bits4digit')
        num_bits4digit = sf.max_digit.bit_length()
        sf._nb = num_bits4digit
        sf._nb
        return sf.num_bits4digit
    #.def __getattr__(sf, nm, /):
    #.    if nm == 'num_bits4digit':
    #.        d = vars(sf)
    #.        assert not nm in d
    #.        if not sf.is_zpow_radix:
    #.            #not zpow
    #.            raise AttributeError(nm)
    #.        num_bits4digit = sf.max_digit.bit_length()
    #.        sf.num_bits4digit = num_bits4digit
    #.        return sf.num_bits4digit
    #.    return super().__getattr__(nm)
#end-class RadixInfo(IRadixInfo):
assert 0x00101 == 257
_j2ri = tuple(RadixInfo(j, _new=True) if j else None for j in range(0x00101))
def mk_RadixInfo_(radix, max_digit=None):
    if radix < 0x00101:
        assert radix > 0
        ri = _j2ri[radix]
    else:
        ri = _mk_RadixInfo_(radix)
        ri._assign(max_digit)
    return ri
@lru_cache(maxsize=128)
def _mk_RadixInfo_(radix):
    return RadixInfo(radix, _new=True)


class IRadixedDigit(ABC):
    'rdgt/rxdigit # digit with radix_info'
    __slots__ = ()
    @property
    @abstractmethod
    def radix_info(sf, /):
        '-> IRadixInfo'
    @property
    @abstractmethod
    def digit(sf, /):
        '-> uint%radix'
    ######################
    def flip_rxdigit_(sf, /):
        '-> IRadixedDigit'
        #xxx:'[.is_zpow_radix] => IRadixedDigit -> IRadixedDigit'
        ri = sf.radix_info
        #.assert ri.is_zpow_radix
        #.digit = ri.max_digit ^ sf.digit
        digit = ri.max_digit ^ sf.digit if ri.is_zpow_radix else ri.max_digit - sf.digit
        return RadixedDigit(ri, digit)
    #.def __invert__(sf, /):
    #.    return flip_rxdigit_
    __invert__ = flip_rxdigit_
    @property
    def count_num_leading1s(sf, /):
        '[.is_zpow_radix] => -> num_leading1s/uint%(1+num_bits4digit)'
        return sf.count_num_leading1s_ex[0]
    @property
    def count_num_leading1s_ex(sf, /):
        '[.is_zpow_radix] => -> (num_leading1s, imay_num_bits4payload)/(uint%(1+num_bits4digit), imay uint%num_bits4digit) # [num_bits4digit==num_leading1s+1[#(maybe nonexist) the "0" bit#]+imay_num_bits4payload]'
        return sf.radix_info.count_num_leading1s_ex_(sf.digit)
    @property
    def count_num_leading0s(sf, /):
        '[.is_zpow_radix] => -> num_leading0s/uint%(1+num_bits4digit)'
        return sf.count_num_leading0s_ex[0]
    @property
    def count_num_leading0s_ex(sf, /):
        '[.is_zpow_radix] => -> (num_leading0s, imay_num_bits4payload)/(uint%(1+num_bits4digit), imay uint%num_bits4digit) # [num_bits4digit==num_leading0s+1[#(maybe nonexist) the "1" bit#]+imay_num_bits4payload]'
        return sf.radix_info.count_num_leading0s_ex_(sf.digit)
    ######################
    @cached_property
    def is_null(sf, /):
        '-> bool{[radix == 1]}'
        return sf.radix_info.is_null
        return sf.radix_info.radix == 1
    ######################

_BaseRadixedDigit = mk_namedtuple_(__name__, 'BaseRadixedDigit', 'radix_info digit')
class RadixedDigit(_BaseRadixedDigit, IRadixedDigit):
    ___no_slots_ok___ = True
    #.def __repr__(sf, /):
    #.    #RadixedDigit(radix_info=RadixInfo(16), digit=7)
    #.    #-->RadixedDigit(RadixInfo(16), 7)
    #.    return repr_helper(sf, sf.radix_info, sf.digit)
    ######################
    #.def __new__(cls, /, radix_info, digit):
    #.    #check_type_le(IRadixInfo, radix_info)
    #.    #check_int_ge_lt(0, radix_info.radix, digit)
    #.    sf = super(__class__, cls).__new__(cls, radix_info, digit)
    #.    return sf
    ######################
    #.def __init__(sf, /, radix_info, digit):
    #.    sf._ri = radix_info
    #.    sf._d = digit
    #.@property
    #.def radix_info(sf, /):
    #.@property
    #.def digit(sf, /):
    #.def __eq__(sf, /):
    #.def __hash__(sf, /):

rxdigit8no_bits = RadixedDigit(ZpowRadixInfo(0), 0)

__all__
from seed.int_tools.RadixInfo import IZpowRadixInfo, ZpowRadixInfo, mk_ZpowRadixInfo_
from seed.int_tools.RadixInfo import IRadixInfo, RadixInfo, mk_RadixInfo_
from seed.int_tools.RadixInfo import IRadixedDigit, RadixedDigit, rxdigit8no_bits
from seed.int_tools.RadixInfo import *
