#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/uint25radix_repr.py

seed.int_tools.digits.uint25radix_repr
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.uint25radix_repr -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.uint25radix_repr:__doc__ -ht # -ff -df

>>> [*_iter_uints_lt__avoid_tailing_zero_(10, 0, 1)]
[()]
>>> [*_iter_uints_lt__avoid_tailing_zero_(10, 0, 2)]
[(), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)]
>>> [*_iter_uints_lt__avoid_tailing_zero_(10, 1, 2)]
[(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)]
>>> [*_iter_decimal_strs__avoid_tailing_zero_(0, 1)]
['']
>>> [*_iter_decimal_strs__avoid_tailing_zero_(0, 2)]
['', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> [*_iter_decimal_strs__avoid_tailing_zero_(1, 2)]
['1', '2', '3', '4', '5', '6', '7', '8', '9']








>>> [*uint2radix_repr_(10, 0, is_big_endian=False)]
[]
>>> [*uint2radix_repr_(10, 963, is_big_endian=False)]
[3, 6, 9]

>>> uint5radix_repr_(10, [], is_big_endian=False)
0
>>> uint5radix_repr_(10, [3, 6, 9], is_big_endian=False)
963



>>> uint2radix_repr__decimal_str_(0, is_big_endian=False)
''
>>> uint2radix_repr__decimal_str_(963, is_big_endian=False)
'369'

>>> uint5radix_repr__decimal_str_('', is_big_endian=False)
0
>>> uint5radix_repr__decimal_str_('369', is_big_endian=False)
963

>>> (d2, d5) = uint25radix_reprT__both_(3, is_big_endian=False)
>>> (s2, s5) = uint25radix_repr__decimal_strT__both_(is_big_endian=False)


>>> [*d2(0)]
[]
>>> d5([])
0
>>> s2(0)
''
>>> s5('')
0

>>> [*d2(3)]
[0, 1]
>>> d5([0, 1])
3
>>> s2(10)
'01'
>>> s5('01')
10


>>> for u, ds in enumerate(_iter_uints_lt__avoid_tailing_zero_(3, 0,3), 0):print((d5(ds), ds, u, [*d2(u)]))
(0, (), 0, [])
(1, (1,), 1, [1])
(2, (2,), 2, [2])
(3, (0, 1), 3, [0, 1])
(4, (1, 1), 4, [1, 1])
(5, (2, 1), 5, [2, 1])
(6, (0, 2), 6, [0, 2])
(7, (1, 2), 7, [1, 2])
(8, (2, 2), 8, [2, 2])
>>> all(ds == tuple(d2(d5(ds))) for ds in _iter_uints_lt__avoid_tailing_zero_(3, 0,5))
True
>>> all(u == d5(d2(u)) for u in range(3**6))
True



>>> for u, s8ds in enumerate(_iter_decimal_strs__avoid_tailing_zero_(0,3), 0):print((s5(s8ds), s8ds, u, s2(u)))
(0, '', 0, '')
(1, '1', 1, '1')
(2, '2', 2, '2')
(3, '3', 3, '3')
(4, '4', 4, '4')
(5, '5', 5, '5')
(6, '6', 6, '6')
(7, '7', 7, '7')
(8, '8', 8, '8')
(9, '9', 9, '9')
(10, '01', 10, '01')
(11, '11', 11, '11')
(12, '21', 12, '21')
(13, '31', 13, '31')
(14, '41', 14, '41')
(15, '51', 15, '51')
(16, '61', 16, '61')
(17, '71', 17, '71')
(18, '81', 18, '81')
(19, '91', 19, '91')
(20, '02', 20, '02')
(21, '12', 21, '12')
(22, '22', 22, '22')
(23, '32', 23, '32')
(24, '42', 24, '42')
(25, '52', 25, '52')
(26, '62', 26, '62')
(27, '72', 27, '72')
(28, '82', 28, '82')
(29, '92', 29, '92')
(30, '03', 30, '03')
(31, '13', 31, '13')
(32, '23', 32, '23')
(33, '33', 33, '33')
(34, '43', 34, '43')
(35, '53', 35, '53')
(36, '63', 36, '63')
(37, '73', 37, '73')
(38, '83', 38, '83')
(39, '93', 39, '93')
(40, '04', 40, '04')
(41, '14', 41, '14')
(42, '24', 42, '24')
(43, '34', 43, '34')
(44, '44', 44, '44')
(45, '54', 45, '54')
(46, '64', 46, '64')
(47, '74', 47, '74')
(48, '84', 48, '84')
(49, '94', 49, '94')
(50, '05', 50, '05')
(51, '15', 51, '15')
(52, '25', 52, '25')
(53, '35', 53, '35')
(54, '45', 54, '45')
(55, '55', 55, '55')
(56, '65', 56, '65')
(57, '75', 57, '75')
(58, '85', 58, '85')
(59, '95', 59, '95')
(60, '06', 60, '06')
(61, '16', 61, '16')
(62, '26', 62, '26')
(63, '36', 63, '36')
(64, '46', 64, '46')
(65, '56', 65, '56')
(66, '66', 66, '66')
(67, '76', 67, '76')
(68, '86', 68, '86')
(69, '96', 69, '96')
(70, '07', 70, '07')
(71, '17', 71, '17')
(72, '27', 72, '27')
(73, '37', 73, '37')
(74, '47', 74, '47')
(75, '57', 75, '57')
(76, '67', 76, '67')
(77, '77', 77, '77')
(78, '87', 78, '87')
(79, '97', 79, '97')
(80, '08', 80, '08')
(81, '18', 81, '18')
(82, '28', 82, '28')
(83, '38', 83, '38')
(84, '48', 84, '48')
(85, '58', 85, '58')
(86, '68', 86, '68')
(87, '78', 87, '78')
(88, '88', 88, '88')
(89, '98', 89, '98')
(90, '09', 90, '09')
(91, '19', 91, '19')
(92, '29', 92, '29')
(93, '39', 93, '39')
(94, '49', 94, '49')
(95, '59', 95, '59')
(96, '69', 96, '69')
(97, '79', 97, '79')
(98, '89', 98, '89')
(99, '99', 99, '99')
>>> all(s8ds == s2(s5(s8ds)) for s8ds in _iter_decimal_strs__avoid_tailing_zero_(0,5))
True
>>> all(u == s5(s2(u)) for u in range(10**3))
True


py_adhoc_call   seed.int_tools.digits.uint25radix_repr   @f

]]]'''#'''
__all__ = r'''
uint2radix_repr_
uint5radix_repr_
    uint2radix_repr__decimal_str_
    uint5radix_repr__decimal_str_

uint25radix_reprTT__both_
    uint25radix_reprT__both_
    uint25radix_repr__decimal_strT__both_
uint25radix_reprTT_
    uint25radix_reprT_
    uint25radix_repr__decimal_strT_
    selector4uint25radix_repr_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import partial
from itertools import product



from seed.tiny_.check import check_type_is, check_int_ge

from seed.int_tools.digits.uint25bijective_numeration import decimal_str2iter_digits_, decimal_str5iter_digits_



from seed.int_tools.digits.uint2radix_repr import uint2radix_repr# IUint2RadixRepr__little_endian__plain, IUint2RadixRepr, Uint2RadixRepr
#def uint2radix_repr(radix_or_an_IUint2RadixRepr, uint, /,*, is_big_endian:bool, _split_ver:'0|1'=1, min_len=0, imay_max_len=-1, input_is_an_IUint2RadixRepr_not_radix=False):

from seed.int_tools.digits.radix_repr2uint import radix_repr2uint# IRadixRepr2Uint, RadixRepr2Uint
#def radix_repr2uint(radix_or_an_IRadixRepr2Uint, digits, /,*, is_big_endian:bool, _merge_ver:'0|1|2'=0, input_is_an_IRadixRepr2Uint_not_radix=False):

___end_mark_of_excluded_global_names__0___ = ...


def _iter_decimal_strs__avoid_leading_zero_(min_sz, max1_sz, /):
    return map(decimal_str5iter_digits_, _iter_uints_lt__avoid_leading_zero_(10, min_sz, max1_sz))
def _iter_uints_lt__avoid_leading_zero_(radix, min_sz, max1_sz, /):
    us = range(radix)
    hs = range(1, radix)
    uss = [hs, *[us]*max1_sz]
    for sz in range(min_sz, max1_sz):
        yield from product(*uss[:sz])


def _iter_decimal_strs__avoid_tailing_zero_(min_sz, max1_sz, /):
    return map(decimal_str5iter_digits_, _iter_uints_lt__avoid_tailing_zero_(10, min_sz, max1_sz))
def _iter_uints_lt__avoid_tailing_zero_(radix, min_sz, max1_sz, /):
    #new ver:sorted@is_big_endian=False
    for us in _iter_uints_lt__avoid_leading_zero_(radix, min_sz, max1_sz):
        yield us[::-1]
    return
    #old ver:sorted@is_big_endian=True
    us = range(radix)
    ts = range(1, radix)
    uss = [*[us]*max1_sz, ts]
    L = len(uss)
    for sz in range(min_sz, max1_sz):
        yield from product(*uss[L-sz:])
    return





uint2radix_repr_ = uint2radix_repr
uint5radix_repr_ = radix_repr2uint

def uint2radix_repr__decimal_str_(u, /, *, is_big_endian:bool, **kwds):
    radix = 10
    decimal_digits = uint2radix_repr_(radix, u, is_big_endian=is_big_endian, **kwds)
    decimal_str8digits = decimal_str5iter_digits_(decimal_digits)
    return decimal_str8digits

def uint5radix_repr__decimal_str_(decimal_str8digits, /, *, is_big_endian:bool, **kwds):
    decimal_digits = decimal_str2iter_digits_(decimal_str8digits)
    radix = 10
    u = uint5radix_repr_(radix, decimal_digits, is_big_endian=is_big_endian, **kwds)
    return u




def _both_(f, kwds, /):
    _2 = f(to_vs_from=False, **kwds)
    _5 = f(to_vs_from=True, **kwds)
    return (_2, _5)
def uint25radix_reprTT__both_(*, using_decimal_str):
    kwds = {**locals()}
    return _both_(uint25radix_reprTT_, kwds)
#comon:radix, /, *, is_big_endian
#    ++using_decimal_str
def uint25radix_reprTT_(*, to_vs_from, using_decimal_str):
    f = selector4uint25radix_repr_(to_vs_from=to_vs_from, using_decimal_str=using_decimal_str)
    def _uint25radix_reprT_(radix, /, *, is_big_endian, **kwds):
        return partial(f, radix, is_big_endian=is_big_endian, **kwds)
    def _uint25radix_repr__decimal_strT_(*, is_big_endian, **kwds):
        return partial(f, is_big_endian=is_big_endian, **kwds)
    return _uint25radix_reprT_ if not using_decimal_str else _uint25radix_repr__decimal_strT_

def uint25radix_reprT__both_(radix, *, is_big_endian, **kwds):
    kwds.update(radix=radix, is_big_endian=is_big_endian)
        # NOTE:radix become kw
    return _both_(uint25radix_reprT_, kwds)
def uint25radix_reprT_(radix, *, to_vs_from, is_big_endian, **kwds):
    # NOTE:radix become kw to support _both_@uint25radix_reprT__both_
    return uint25radix_reprTT_(to_vs_from=to_vs_from, using_decimal_str=False)(radix, is_big_endian=is_big_endian, **kwds)
def uint25radix_repr__decimal_strT__both_(*, is_big_endian, **kwds):
    kwds.update(is_big_endian=is_big_endian)
    return _both_(uint25radix_repr__decimal_strT_, kwds)
def uint25radix_repr__decimal_strT_(*, to_vs_from, is_big_endian, **kwds):
    return uint25radix_reprTT_(to_vs_from=to_vs_from, using_decimal_str=True)(is_big_endian=is_big_endian, **kwds)

def selector4uint25radix_repr_(*, to_vs_from, using_decimal_str):
    check_type_is(bool, to_vs_from)
    check_type_is(bool, using_decimal_str)
    j = to_vs_from
    i = using_decimal_str
    f = _fs4TT[i*2+j]
    return f
_fs4TT = (*[]
,uint2radix_repr_
,uint5radix_repr_

,uint2radix_repr__decimal_str_
,uint5radix_repr__decimal_str_
)




__all__
from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_
from seed.int_tools.digits.uint25radix_repr import uint2radix_repr__decimal_str_, uint5radix_repr__decimal_str_

from seed.int_tools.digits.uint25radix_repr import uint25radix_reprTT__both_, uint25radix_reprT__both_, uint25radix_repr__decimal_strT__both_
from seed.int_tools.digits.uint25radix_repr import uint25radix_reprTT_, uint25radix_reprT_, uint25radix_repr__decimal_strT_, selector4uint25radix_repr_

from seed.int_tools.digits.uint25radix_repr import *
