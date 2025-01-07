#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/uint25bijective_numeration.py
view ../../python3_src/seed/math/log__bijective_numeration.py


seed.int_tools.digits.uint25bijective_numeration
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.uint25bijective_numeration -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.uint25bijective_numeration:__doc__ -ht # -ff -df


[[
regex{radix_repr} ::= ([1..<radix] [0..<radix]*)?
regex{bijective_numeration} ::= [1..=radix]+

 digit{radix_repr} ::= [0..<radix]
 digit{bijective_numeration} ::= [1..=radix]
    i.e. u += 111...1 == total_lesser_uints
]]













DONE:25T/partial & uint25radix_reprT
    e ../../python3_src/seed/int_tools/digits/uint25radix_repr.py










>>> [*_iter_uints_lt_(10, 0, 1)]
[()]
>>> [*_iter_uints_lt_(10, 0, 2)]
[(), (0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)]
>>> [*_iter_uints_lt_(10, 1, 2)]
[(0,), (1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)]
>>> [*_iter_decimal_strs_(0, 1)]
['']
>>> [*_iter_decimal_strs_(0, 2)]
['', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> [*_iter_decimal_strs_(1, 2)]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



>>> [*uints5nonempty_uints__inc_or_dec_solo_uint_([])]
Traceback (most recent call last):
    ...
ValueError: uints are empty


>>> [*uints5nonempty_uints__inc_or_dec_solo_uint_([0])]
[]
>>> [*uints5nonempty_uints__inc_or_dec_solo_uint_([1])]
[0]
>>> [*uints5nonempty_uints__inc_or_dec_solo_uint_([2])]
[1]
>>> [*uints5nonempty_uints__inc_or_dec_solo_uint_([0, 0])]
[0, 0]
>>> [*uints5nonempty_uints__inc_or_dec_solo_uint_([0, 0, 0])]
[0, 0, 0]
>>> [*uints5nonempty_uints__inc_or_dec_solo_uint_([1, 0, 2])]
[1, 0, 2]










>>> uints2may_bijective_numeration__sep_by_zero__decimal_str_([9,0,12], is_big_endian=True)
'90013'
>>> nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_([9,0,12], is_big_endian=True)
'90013'

>>> [*uints5may_bijective_numeration__sep_by_zero__decimal_str_('90013', is_big_endian=True)]
[9, 0, 12]
>>> [*nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_('90013', is_big_endian=True)]
[9, 0, 12]
>>> iter(__:=uints5may_bijective_numeration__sep_by_zero__decimal_str_('90013', is_big_endian=True)) is __
True
>>> iter(__:=nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_('90013', is_big_endian=True)) is __
True















>>> all(iter(it) is it for is_big_endian in [False, True] for offset4digit in range(-2, 3) for it in [uint2bijective_numeration_(3, 5, is_big_endian=is_big_endian, offset4digit=offset4digit)])
True

>>> [[*uint2bijective_numeration_(2, u, is_big_endian=True, offset4digit=0)] for u in range(20)]
[[], [0], [1], [0, 0], [0, 1], [1, 0], [1, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0]]
>>> [[*uint2bijective_numeration_(2, u, is_big_endian=True, offset4digit=1)] for u in range(20)]
[[], [1], [2], [1, 1], [1, 2], [2, 1], [2, 2], [1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 2, 2], [2, 1, 1], [2, 1, 2], [2, 2, 1], [2, 2, 2], [1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 1, 2, 2], [1, 2, 1, 1]]

>>> [[*uint2bijective_numeration_(3, u, is_big_endian=True, offset4digit=0)] for u in range(20)]
[[], [0], [1], [2], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0]]
>>> [[*uint2bijective_numeration_(3, u, is_big_endian=True, offset4digit=1)] for u in range(20)]
[[], [1], [2], [3], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3], [1, 3, 1]]

>>> all(u == uint5bijective_numeration_(2, uint2bijective_numeration_(2, u, is_big_endian=True, offset4digit=0), is_big_endian=True, offset4digit=0) for u in range(200))
True
>>> all(u == uint5bijective_numeration_(3, uint2bijective_numeration_(3, u, is_big_endian=False, offset4digit=1), is_big_endian=False, offset4digit=1) for u in range(200))
True


>>> all([*uint2bijective_numeration_(2, u, is_big_endian=True, offset4digit=0)] == [*reversed([*uint2bijective_numeration_(2, u, is_big_endian=False, offset4digit=0)])] for u in range(200))
True
>>> all([*uint2bijective_numeration_(3, u, is_big_endian=True, offset4digit=1)] == [*reversed([*uint2bijective_numeration_(3, u, is_big_endian=False, offset4digit=1)])] for u in range(200))
True




>>> uint5bijective_numeration__decimal_str_('', is_big_endian=True)
0
>>> uint5bijective_numeration__decimal_str_('0', is_big_endian=True)
1
>>> uint5bijective_numeration__decimal_str_('8', is_big_endian=True)
9
>>> uint5bijective_numeration__decimal_str_('9', is_big_endian=True)
10
>>> uint5bijective_numeration__decimal_str_('00', is_big_endian=True)
11
>>> uint5bijective_numeration__decimal_str_('01', is_big_endian=True)
12


>>> uint2bijective_numeration__decimal_str_(0, is_big_endian=True)
''
>>> uint2bijective_numeration__decimal_str_(1, is_big_endian=True)
'0'
>>> uint2bijective_numeration__decimal_str_(9, is_big_endian=True)
'8'
>>> uint2bijective_numeration__decimal_str_(10, is_big_endian=True)
'9'
>>> uint2bijective_numeration__decimal_str_(11, is_big_endian=True)
'00'
>>> uint2bijective_numeration__decimal_str_(12, is_big_endian=True)
'01'








>>> [*nonempty_uints2bijective_numeration__sep_by_zero_(10, [], is_big_endian=True, zero_digit=0)]
Traceback (most recent call last):
    ...
ValueError: uints are empty


>>> [*nonempty_uints2bijective_numeration__sep_by_zero_(10, [0], is_big_endian=True, zero_digit=0)]
[]
>>> [*nonempty_uints5bijective_numeration__sep_by_zero_(10, [], is_big_endian=True, zero_digit=0)]
[0]










>>> nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_([0], is_big_endian=True)
''
>>> [*nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_('', is_big_endian=True)]
[0]


>>> [*nonempty_uints2bijective_numeration__sep_by_zero_(9, [0, 999, 666, 1, 2, 3], is_big_endian=True, zero_digit=0)]
[0, 1, 3, 2, 9, 0, 8, 1, 9, 0, 1, 0, 2, 0, 3]
>>> nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_([0, 999, 666, 1, 2, 3], is_big_endian=True)
'013290819010203'
>>> nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_([0, 999, 666, 1, 2, 3], is_big_endian=False)
'092310918010203'



>>> [*map(list, _iter_split_by_(0, [0, 1, 3, 2, 9, 0, 8, 1, 9, 0, 1, 0, 2, 0, 3]))]
[[], [1, 3, 2, 9], [8, 1, 9], [1], [2], [3]]

>>> [*nonempty_uints5bijective_numeration__sep_by_zero_(9, [0, 1, 3, 2, 9, 0, 8, 1, 9, 0, 1, 0, 2, 0, 3], is_big_endian=True, zero_digit=0)]
[0, 999, 666, 1, 2, 3]
>>> [*nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_('013290819010203', is_big_endian=True)]
[0, 999, 666, 1, 2, 3]
>>> [*nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_('092310918010203', is_big_endian=False)]
[0, 999, 666, 1, 2, 3]



>>> all(us == tuple(nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_(nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_(us, is_big_endian=True), is_big_endian=True)) for us in _iter_uints_lt_(12, 1,4))
True
>>> all(s8ds == nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_(nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_(s8ds, is_big_endian=True), is_big_endian=True) for s8ds in _iter_decimal_strs_(0,5))
True













>>> None is uints2may_bijective_numeration__sep_by_zero_(10, [], is_big_endian=True, zero_digit=0)
True
>>> [*uints5may_bijective_numeration__sep_by_zero_(10, None, is_big_endian=True, zero_digit=0)]
[]

>>> None is uints2may_bijective_numeration__sep_by_zero__decimal_str_([], is_big_endian=True)
True
>>> [*uints5may_bijective_numeration__sep_by_zero__decimal_str_(None, is_big_endian=True)]
[]

>>> all(us == tuple(uints5may_bijective_numeration__sep_by_zero__decimal_str_(uints2may_bijective_numeration__sep_by_zero__decimal_str_(us, is_big_endian=False), is_big_endian=False)) for us in _iter_uints_lt_(12, 1,4))
True
>>> all(s8ds == uints2may_bijective_numeration__sep_by_zero__decimal_str_(uints5may_bijective_numeration__sep_by_zero__decimal_str_(s8ds, is_big_endian=False), is_big_endian=False) for s8ds in _iter_decimal_strs_(0,5))
True







>>> [*uints2nonempty_uints__inc_or_dec_solo_uint_([])]
[0]
>>> [*uints2nonempty_uints__inc_or_dec_solo_uint_([0])]
[1]
>>> [*uints2nonempty_uints__inc_or_dec_solo_uint_([1])]
[2]
>>> [*uints2nonempty_uints__inc_or_dec_solo_uint_([0, 0])]
[0, 0]
>>> [*uints2nonempty_uints__inc_or_dec_solo_uint_([0, 0, 0])]
[0, 0, 0]
>>> [*uints2nonempty_uints__inc_or_dec_solo_uint_([1, 0, 2])]
[1, 0, 2]















>>> [*uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [], is_big_endian=True, zero_digit=0)]
[]
>>> [*uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [0], is_big_endian=True, zero_digit=0)]
[0, 0]
>>> [*uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [1], is_big_endian=True, zero_digit=0)]
[0]
>>> [*uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [9], is_big_endian=True, zero_digit=0)]
[8]
>>> [*uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [1, 1], is_big_endian=True, zero_digit=0)]
[9]
>>> [*uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [0, 0], is_big_endian=True, zero_digit=0)]
[0, 0, 0]



>>> [*uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [], is_big_endian=True, zero_digit=0)]
[]
>>> [*uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [0, 0], is_big_endian=True, zero_digit=0)]
[0]
>>> [*uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [0], is_big_endian=True, zero_digit=0)]
[1]
>>> [*uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [8], is_big_endian=True, zero_digit=0)]
[9]
>>> [*uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [9], is_big_endian=True, zero_digit=0)]
[1, 1]
>>> [*uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(9, [0, 0, 0], is_big_endian=True, zero_digit=0)]
[0, 0]




>>> all(us == tuple(uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(10, uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(10, us, is_big_endian=False, zero_digit=0), is_big_endian=False, zero_digit=0)) for us in _iter_uints_lt_(12, 0,4))
True
>>> all(ds == tuple(uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(10, uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(10, ds, is_big_endian=False, zero_digit=0), is_big_endian=False, zero_digit=0)) for ds in _iter_uints_lt_(10, 0,5))
True



>>> all(us == tuple(uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_(uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_(us, is_big_endian=False), is_big_endian=False)) for us in _iter_uints_lt_(12, 0,4))
True
>>> all(s8ds == uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_(uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_(s8ds, is_big_endian=False), is_big_endian=False) for s8ds in _iter_decimal_strs_(0,5))
True





















def uints25bijective_numeration__sep_by_zeroT_(radix, *, is_big_endian, zero_digit, to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint):
def uints25bijective_numeration__sep_by_zero__decimal_strT_(*, is_big_endian, to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint):

>>> (d20, d50) = uints25bijective_numeration__sep_by_zeroT__both_(3, is_big_endian=True, zero_digit=0, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=0)
>>> (d21, d51) = uints25bijective_numeration__sep_by_zeroT__both_(3, is_big_endian=True, zero_digit=0, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=1)
>>> (d22, d52) = uints25bijective_numeration__sep_by_zeroT__both_(3, is_big_endian=True, zero_digit=0, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=2)

>>> (s20, s50) = uints25bijective_numeration__sep_by_zero__decimal_strT__both_(is_big_endian=True, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=0)
>>> (s21, s51) = uints25bijective_numeration__sep_by_zero__decimal_strT__both_(is_big_endian=True, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=1)
>>> (s22, s52) = uints25bijective_numeration__sep_by_zero__decimal_strT__both_(is_big_endian=True, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=2)





>>> [*d20([])]
Traceback (most recent call last):
    ...
ValueError: uints are empty
>>> [*d50([])]
[0]
>>> d21([]) is None
True
>>> [*d51(None)]
[]
>>> [*d51([])]
[0]
>>> [*d22([])]
[]
>>> [*d52([])]
[]

>>> s20([])
Traceback (most recent call last):
    ...
ValueError: uints are empty
>>> [*s50('')]
[0]
>>> s21([]) is None
True
>>> [*s51(None)]
[]
>>> [*s51('')]
[0]
>>> s22([])
''
>>> [*s52('')]
[]



>>> for i, ds in enumerate(_iter_uints_lt_(4, 1,3), 1):print((i, [*d50(ds)], ds, [*d20(ds)]))
(1, [0, 0], (0,), [])
(2, [1], (1,), [1])
(3, [2], (2,), [2])
(4, [3], (3,), [3])
(5, [0, 0, 0], (0, 0), [0])
(6, [0, 1], (0, 1), [0, 1])
(7, [0, 2], (0, 2), [0, 2])
(8, [0, 3], (0, 3), [0, 3])
(9, [1, 0], (1, 0), [1, 0])
(10, [4], (1, 1), [1, 0, 1])
(11, [5], (1, 2), [1, 0, 2])
(12, [6], (1, 3), [1, 0, 3])
(13, [2, 0], (2, 0), [2, 0])
(14, [7], (2, 1), [2, 0, 1])
(15, [8], (2, 2), [2, 0, 2])
(16, [9], (2, 3), [2, 0, 3])
(17, [3, 0], (3, 0), [3, 0])
(18, [10], (3, 1), [3, 0, 1])
(19, [11], (3, 2), [3, 0, 2])
(20, [12], (3, 3), [3, 0, 3])
>>> all(([*d50(ds)], [*d20(ds)]) == ([*d51(ds)], [*d21(ds)]) for i, ds in enumerate(_iter_uints_lt_(4, 1,3), 1))
True
>>> for i, ds in enumerate(_iter_uints_lt_(4, 1,3), 1):print((i, [*d52(ds)], ds, [*d22(ds)]))
(1, [0, 0], (0,), [1])
(2, [0], (1,), [2])
(3, [1], (2,), [3])
(4, [2], (3,), [1, 1])
(5, [0, 0, 0], (0, 0), [0])
(6, [0, 1], (0, 1), [0, 1])
(7, [0, 2], (0, 2), [0, 2])
(8, [0, 3], (0, 3), [0, 3])
(9, [1, 0], (1, 0), [1, 0])
(10, [3], (1, 1), [1, 0, 1])
(11, [4], (1, 2), [1, 0, 2])
(12, [5], (1, 3), [1, 0, 3])
(13, [2, 0], (2, 0), [2, 0])
(14, [6], (2, 1), [2, 0, 1])
(15, [7], (2, 2), [2, 0, 2])
(16, [8], (2, 3), [2, 0, 3])
(17, [3, 0], (3, 0), [3, 0])
(18, [9], (3, 1), [3, 0, 1])
(19, [10], (3, 2), [3, 0, 2])
(20, [11], (3, 3), [3, 0, 3])

>>> all(ds == tuple(d20(d50(ds))) for ds in _iter_uints_lt_(4, 1,5))
True
>>> all(us == tuple(d50(d20(us))) for us in _iter_uints_lt_(6, 1,4))
True






>>> for i, (s8ds, us) in enumerate(_iter_decimal_str_and_digits_pairs_(1,3), 1):print((i, [*s50(s8ds)], s8ds, s20(us)))
(1, [0, 0], '0', '')
(2, [1], '1', '1')
(3, [2], '2', '2')
(4, [3], '3', '3')
(5, [4], '4', '4')
(6, [5], '5', '5')
(7, [6], '6', '6')
(8, [7], '7', '7')
(9, [8], '8', '8')
(10, [9], '9', '9')
(11, [0, 0, 0], '00', '0')
(12, [0, 1], '01', '01')
(13, [0, 2], '02', '02')
(14, [0, 3], '03', '03')
(15, [0, 4], '04', '04')
(16, [0, 5], '05', '05')
(17, [0, 6], '06', '06')
(18, [0, 7], '07', '07')
(19, [0, 8], '08', '08')
(20, [0, 9], '09', '09')
(21, [1, 0], '10', '10')
(22, [10], '11', '101')
(23, [11], '12', '102')
(24, [12], '13', '103')
(25, [13], '14', '104')
(26, [14], '15', '105')
(27, [15], '16', '106')
(28, [16], '17', '107')
(29, [17], '18', '108')
(30, [18], '19', '109')
(31, [2, 0], '20', '20')
(32, [19], '21', '201')
(33, [20], '22', '202')
(34, [21], '23', '203')
(35, [22], '24', '204')
(36, [23], '25', '205')
(37, [24], '26', '206')
(38, [25], '27', '207')
(39, [26], '28', '208')
(40, [27], '29', '209')
(41, [3, 0], '30', '30')
(42, [28], '31', '301')
(43, [29], '32', '302')
(44, [30], '33', '303')
(45, [31], '34', '304')
(46, [32], '35', '305')
(47, [33], '36', '306')
(48, [34], '37', '307')
(49, [35], '38', '308')
(50, [36], '39', '309')
(51, [4, 0], '40', '40')
(52, [37], '41', '401')
(53, [38], '42', '402')
(54, [39], '43', '403')
(55, [40], '44', '404')
(56, [41], '45', '405')
(57, [42], '46', '406')
(58, [43], '47', '407')
(59, [44], '48', '408')
(60, [45], '49', '409')
(61, [5, 0], '50', '50')
(62, [46], '51', '501')
(63, [47], '52', '502')
(64, [48], '53', '503')
(65, [49], '54', '504')
(66, [50], '55', '505')
(67, [51], '56', '506')
(68, [52], '57', '507')
(69, [53], '58', '508')
(70, [54], '59', '509')
(71, [6, 0], '60', '60')
(72, [55], '61', '601')
(73, [56], '62', '602')
(74, [57], '63', '603')
(75, [58], '64', '604')
(76, [59], '65', '605')
(77, [60], '66', '606')
(78, [61], '67', '607')
(79, [62], '68', '608')
(80, [63], '69', '609')
(81, [7, 0], '70', '70')
(82, [64], '71', '701')
(83, [65], '72', '702')
(84, [66], '73', '703')
(85, [67], '74', '704')
(86, [68], '75', '705')
(87, [69], '76', '706')
(88, [70], '77', '707')
(89, [71], '78', '708')
(90, [72], '79', '709')
(91, [8, 0], '80', '80')
(92, [73], '81', '801')
(93, [74], '82', '802')
(94, [75], '83', '803')
(95, [76], '84', '804')
(96, [77], '85', '805')
(97, [78], '86', '806')
(98, [79], '87', '807')
(99, [80], '88', '808')
(100, [81], '89', '809')
(101, [9, 0], '90', '90')
(102, [82], '91', '901')
(103, [83], '92', '902')
(104, [84], '93', '903')
(105, [85], '94', '904')
(106, [86], '95', '905')
(107, [87], '96', '906')
(108, [88], '97', '907')
(109, [89], '98', '908')
(110, [90], '99', '909')
>>> all(([*s50(s8ds)], [*s20(us)]) == ([*s51(s8ds)], [*s21(us)]) for i, (s8ds, us) in enumerate(_iter_decimal_str_and_digits_pairs_(1,3), 1))
True
>>> for i, (s8ds, us) in enumerate(_iter_decimal_str_and_digits_pairs_(1,3), 1):print((i, [*s52(s8ds)], s8ds, s22(us)))
(1, [0, 0], '0', '1')
(2, [0], '1', '2')
(3, [1], '2', '3')
(4, [2], '3', '4')
(5, [3], '4', '5')
(6, [4], '5', '6')
(7, [5], '6', '7')
(8, [6], '7', '8')
(9, [7], '8', '9')
(10, [8], '9', '11')
(11, [0, 0, 0], '00', '0')
(12, [0, 1], '01', '01')
(13, [0, 2], '02', '02')
(14, [0, 3], '03', '03')
(15, [0, 4], '04', '04')
(16, [0, 5], '05', '05')
(17, [0, 6], '06', '06')
(18, [0, 7], '07', '07')
(19, [0, 8], '08', '08')
(20, [0, 9], '09', '09')
(21, [1, 0], '10', '10')
(22, [9], '11', '101')
(23, [10], '12', '102')
(24, [11], '13', '103')
(25, [12], '14', '104')
(26, [13], '15', '105')
(27, [14], '16', '106')
(28, [15], '17', '107')
(29, [16], '18', '108')
(30, [17], '19', '109')
(31, [2, 0], '20', '20')
(32, [18], '21', '201')
(33, [19], '22', '202')
(34, [20], '23', '203')
(35, [21], '24', '204')
(36, [22], '25', '205')
(37, [23], '26', '206')
(38, [24], '27', '207')
(39, [25], '28', '208')
(40, [26], '29', '209')
(41, [3, 0], '30', '30')
(42, [27], '31', '301')
(43, [28], '32', '302')
(44, [29], '33', '303')
(45, [30], '34', '304')
(46, [31], '35', '305')
(47, [32], '36', '306')
(48, [33], '37', '307')
(49, [34], '38', '308')
(50, [35], '39', '309')
(51, [4, 0], '40', '40')
(52, [36], '41', '401')
(53, [37], '42', '402')
(54, [38], '43', '403')
(55, [39], '44', '404')
(56, [40], '45', '405')
(57, [41], '46', '406')
(58, [42], '47', '407')
(59, [43], '48', '408')
(60, [44], '49', '409')
(61, [5, 0], '50', '50')
(62, [45], '51', '501')
(63, [46], '52', '502')
(64, [47], '53', '503')
(65, [48], '54', '504')
(66, [49], '55', '505')
(67, [50], '56', '506')
(68, [51], '57', '507')
(69, [52], '58', '508')
(70, [53], '59', '509')
(71, [6, 0], '60', '60')
(72, [54], '61', '601')
(73, [55], '62', '602')
(74, [56], '63', '603')
(75, [57], '64', '604')
(76, [58], '65', '605')
(77, [59], '66', '606')
(78, [60], '67', '607')
(79, [61], '68', '608')
(80, [62], '69', '609')
(81, [7, 0], '70', '70')
(82, [63], '71', '701')
(83, [64], '72', '702')
(84, [65], '73', '703')
(85, [66], '74', '704')
(86, [67], '75', '705')
(87, [68], '76', '706')
(88, [69], '77', '707')
(89, [70], '78', '708')
(90, [71], '79', '709')
(91, [8, 0], '80', '80')
(92, [72], '81', '801')
(93, [73], '82', '802')
(94, [74], '83', '803')
(95, [75], '84', '804')
(96, [76], '85', '805')
(97, [77], '86', '806')
(98, [78], '87', '807')
(99, [79], '88', '808')
(100, [80], '89', '809')
(101, [9, 0], '90', '90')
(102, [81], '91', '901')
(103, [82], '92', '902')
(104, [83], '93', '903')
(105, [84], '94', '904')
(106, [85], '95', '905')
(107, [86], '96', '906')
(108, [87], '97', '907')
(109, [88], '98', '908')
(110, [89], '99', '909')
>>> all(s8ds == s20(s50(s8ds)) for ds in _iter_decimal_strs_(1,5))
True
>>> all(us == tuple(s50(s20(us))) for us in _iter_uints_lt_(10, 1,4))
True




#]]]'''#'''
#__all__
#__doc__ = \
r'''[[[

>>> def eq(a, b, /):
...     assert a == b, (a, b)
...     return True

>>> 0

py_adhoc_call   seed.int_tools.digits.uint25bijective_numeration   @f
]]]'''#'''
__all__ = r'''
uint5bijective_numeration_
uint2bijective_numeration_
    uint5bijective_numeration__decimal_str_
    uint2bijective_numeration__decimal_str_



uints5may_bijective_numeration__sep_by_zero_
uints2may_bijective_numeration__sep_by_zero_
    uints5may_bijective_numeration__sep_by_zero__decimal_str_
    uints2may_bijective_numeration__sep_by_zero__decimal_str_


    nonempty_uints5bijective_numeration__sep_by_zero_
    nonempty_uints2bijective_numeration__sep_by_zero_
        nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_
        nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_






uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_
uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_
    uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_
    uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_










uints25bijective_numeration__sep_by_zeroTT__both_
    uints25bijective_numeration__sep_by_zeroT__both_
    uints25bijective_numeration__sep_by_zero__decimal_strT__both_
uints25bijective_numeration__sep_by_zeroTT_
    selector4uints25bijective_numeration__sep_by_zero_
    uints25bijective_numeration__sep_by_zeroT_
    uints25bijective_numeration__sep_by_zero__decimal_strT_



















decimal_str2iter_digits_
decimal_str5iter_digits_



uints2nonempty_uints__inc_or_dec_solo_uint_
uints5nonempty_uints__inc_or_dec_solo_uint_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from string import digits as _j2digit
from functools import partial
from itertools import takewhile, islice, product# chain
from seed.tiny import null_iter

from seed.math.log__bijective_numeration import uint2len_bijective_numeration_, radix_pow__bijective_numeration_

from seed.int_tools.digits.uint2radix_repr import uint2radix_repr# IUint2RadixRepr__little_endian__plain, IUint2RadixRepr, Uint2RadixRepr
#def uint2radix_repr(radix_or_an_IUint2RadixRepr, uint, /,*, is_big_endian:bool, _split_ver:'0|1'=1, min_len=0, imay_max_len=-1, input_is_an_IUint2RadixRepr_not_radix=False):

from seed.int_tools.digits.radix_repr2uint import radix_repr2uint# IRadixRepr2Uint, RadixRepr2Uint
#def radix_repr2uint(radix_or_an_IRadixRepr2Uint, digits, /,*, is_big_endian:bool, _merge_ver:'0|1|2'=0, input_is_an_IRadixRepr2Uint_not_radix=False):

from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt
from seed.tiny_.fmap4may import fmap4may

___end_mark_of_excluded_global_names__0___ = ...












def _iter_decimal_str_and_digits_pairs_(min_sz, max1_sz, /):
    for ds in _iter_uints_lt_(10, min_sz, max1_sz):
        s8ds = decimal_str5iter_digits_(ds)
        yield (s8ds, ds)
def _iter_decimal_strs_(min_sz, max1_sz, /):
    return map(decimal_str5iter_digits_, _iter_uints_lt_(10, min_sz, max1_sz))
def _iter_uints_lt_(radix, min_sz, max1_sz, /):
    us = range(radix)
    for sz in range(min_sz, max1_sz):
        yield from product(us, repeat=sz)






















def uint5bijective_numeration_(radix, offsetted_digits, /, *, is_big_endian, offset4digit):
    'radix/uint{>=2} -> Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]} -> uint # [original-bijective_numeration => [offset4digit:=1]]'
    check_type_is(bool, is_big_endian)
    check_type_is(int, offset4digit)
    check_int_ge(2, radix)
    iter(offsetted_digits)

    dd = offset4digit -1
    # [offset4digit:=1] => [dd == 0]
    # [offset4digit:=0] => [dd == -1]
    if dd:
        # [offset4digit:=0] => [dd == -1]
        original_digits = map(dd.__rsub__, offsetted_digits)
        # [original-bijective_numeration-digit == offsetted-digit -dd]
        # [offset4digit:=0] => [dd == -1][original-bijective_numeration-digit == offsetted-digit +1]
    else:
        # [dd == 0]
        # [offset4digit == 1]
        original_digits = offsetted_digits
        # [original-bijective_numeration-digit == offsetted-digit -dd]
    original_digits
    # [original-bijective_numeration-digit == offsetted-digit -dd]
    # [original-bijective_numeration-digit == offsetted-digit -offset4digit +1]
    return radix_repr2uint(radix, original_digits, is_big_endian=is_big_endian)
def uint2bijective_numeration_(radix, u, /, *, is_big_endian, offset4digit):
    'radix/uint{>=2} -> uint -> Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]} # [original-bijective_numeration => [offset4digit:=1]]'
    check_type_is(bool, is_big_endian)
    check_type_is(int, offset4digit)
    check_int_ge(2, radix)
    check_int_ge(0, u)

    L = uint2len_bijective_numeration_(radix, u)
    zero_offset4u = radix_pow__bijective_numeration_(radix, L)
    #if 0b0001:assert zero_offset4u <= u < (__:=radix_pow__bijective_numeration_(radix, L+1)), (radix, u, L, zero_offset4u, __)

    #bug:original_digits = uint2radix_repr(radix, u-zero_offset4u, is_big_endian=is_big_endian, min_len=L)
    zero_offsetted_digits = uint2radix_repr(radix, u-zero_offset4u, is_big_endian=is_big_endian, min_len=L)

    zero_offsetted_digits
    zd = offset4digit -0
    # [offset4digit:=1] => [zd == 1]
    # [offset4digit:=0] => [zd == 0]
    if zd:
        # [offset4digit:=1] => [zd == 1]
        offsetted_digits = map(zd.__add__, zero_offsetted_digits)
        # [offsetted-digit == 0-offsetted-digit +zd]
    else:
        # [zd == 0]
        # [offset4digit == 0]
        offsetted_digits = zero_offsetted_digits
        # [offsetted-digit == 0-offsetted-digit +zd]
    offsetted_digits
    # [offsetted-digit == 0-offsetted-digit +zd]
    return offsetted_digits


def uint5bijective_numeration__decimal_str_(decimal_str8digits, /, *, is_big_endian):
    'decimal_str8digits/str/regex"[0-9]*" -> uint'
    radix = 10
    offset4digit = 0
    decimal_digits = decimal_str2iter_digits_(decimal_str8digits)
    u = uint5bijective_numeration_(radix, decimal_digits, is_big_endian=is_big_endian, offset4digit=offset4digit)
    return u
def uint2bijective_numeration__decimal_str_(u, /, *, is_big_endian):
    'uint -> decimal_str8digits/str/regex"[0-9]*"'
    radix = 10
    offset4digit = 0
    decimal_digits = uint2bijective_numeration_(radix, u, is_big_endian=is_big_endian, offset4digit=offset4digit)
    decimal_str8digits = decimal_str5iter_digits_(decimal_digits)
    return decimal_str8digits




def decimal_str2iter_digits_(decimal_str8digits, /):
    'decimal_str8digits/str/regex"[0-9]*" -> decimal_digits/(Iter uint{<- [0-9]})'
    check_type_is(str, decimal_str8digits)
    #decimal_digits = map(int, decimal_str8digits)
    #decimal_digits = map(_j2digit.index, decimal_str8digits)
    decimal_digits = map(ord('0').__rsub__, map(ord, decimal_str8digits))
    return decimal_digits
def decimal_str5iter_digits_(decimal_digits, /):
    'decimal_digits/(Iter uint{<- [0-9]}) -> decimal_str8digits/str/regex"[0-9]*"'

    #decimal_str8digits = ''.join(map(str, decimal_digits))
    #decimal_str8digits = ''.join(map(chr, map(ord('0').__add__, decimal_digits)))
    decimal_str8digits = ''.join(map(_j2digit.__getitem__, decimal_digits))
    return decimal_str8digits
















#above:uint25bijective_numeration
#below:uints25may_bijective_numeration
#below:nonempty_uints25bijective_numeration
#below:uints25bijective_numeration
def uints2nonempty_uints__inc_or_dec_solo_uint_(us, /):
    '(Iter uint) -> (Iter uint){nonempty}'
    us = iter(us)
    match [*islice(us, 2)]:
        case []:
            # empty
            u = 0 # empty->nonempty/solo/singleton
            yield u
        case [u]:
            # solo/singleton
            check_int_ge(0, u)
            u += 1 # inc the single uint
            yield u
        case [u0, u1]:
            yield u0
            yield u1
            yield from us
    return

def uints5nonempty_uints__inc_or_dec_solo_uint_(nonempty_us, /):
    '(Iter uint){nonempty} -> (Iter uint)'
    nonempty_us = iter(nonempty_us)
    match [*islice(nonempty_us, 2)]:
        case [u0, u1]:
            yield u0
            yield u1
            yield from nonempty_us
        case [u]:
            # solo/singleton
            check_int_ge(0, u)
            if u == 0:
                pass # nonempty/solo/singleton->empty
            else:
                u -= 1 # dec the single uint
                yield u
        case []:
            # empty
            raise ValueError('uints are empty')
    return



def uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(radix, offsetted_digits, /, *, is_big_endian, zero_digit):
    'radix/uint{>=2} -> (Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]}) -> (Iter uint) # [offset4digit := 1+zero_digit][original-bijective_numeration => [offset4digit:=1]]'
    nonempty_us = nonempty_uints5bijective_numeration__sep_by_zero_(radix, offsetted_digits, is_big_endian=is_big_endian, zero_digit=zero_digit)
    us = uints5nonempty_uints__inc_or_dec_solo_uint_(nonempty_us)
    return us
def uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_(radix, us, /, *, is_big_endian, zero_digit):
    'radix/uint{>=2} -> (Iter uint) -> (Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]}) # [offset4digit := 1+zero_digit][original-bijective_numeration => [offset4digit:=1]]'
    nonempty_us = uints2nonempty_uints__inc_or_dec_solo_uint_(us)
    offsetted_digits = nonempty_uints2bijective_numeration__sep_by_zero_(radix, nonempty_us, is_big_endian=is_big_endian, zero_digit=zero_digit)
    return offsetted_digits


def uints5may_bijective_numeration__sep_by_zero_(radix, may_offsetted_digits, /, *, is_big_endian, zero_digit, empty_uints_ok=True):
    'radix/uint{>=2} -> may (Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]}) -> (Iter uint) # [offset4digit := 1+zero_digit][original-bijective_numeration => [offset4digit:=1]]'
    check_type_is(bool, empty_uints_ok)
    check_type_is(bool, is_big_endian)
    check_type_is(int, zero_digit)
    check_int_ge(2, radix)
    if empty_uints_ok and may_offsetted_digits is None:
        # empty uints
        return;yield
        #return null_iter
    offsetted_digits = may_offsetted_digits
    iter(offsetted_digits) # not empty

    offset4digit = 1+zero_digit
    ds = None
    for ds in _iter_split_by_(zero_digit, offsetted_digits):
        u = uint5bijective_numeration_(radix, ds, is_big_endian=is_big_endian, offset4digit=offset4digit)
        yield u
    if ds is None:raise 000

def uints2may_bijective_numeration__sep_by_zero_(radix, us, /, *, is_big_endian, zero_digit, empty_uints_ok=True):
    'radix/uint{>=2} -> (Iter uint) -> may (Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]}) # [offset4digit := 1+zero_digit][original-bijective_numeration => [offset4digit:=1]]'
    check_type_is(bool, empty_uints_ok)
    it = _xempty_uints2bijective_numeration__sep_by_zero_(radix, us, is_big_endian=is_big_endian, zero_digit=zero_digit, nonempty_vs_cased=empty_uints_ok)
    if not empty_uints_ok:
        return it
    for b_empty in it:
        break
    else:
        raise 000
    return None if b_empty else it

def nonempty_uints5bijective_numeration__sep_by_zero_(radix, offsetted_digits, /, *, is_big_endian, zero_digit):
    'radix/uint{>=2} -> Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]} -> (Iter uint){nonempty} # [offset4digit := 1+zero_digit][original-bijective_numeration => [offset4digit:=1]]'
    return uints5may_bijective_numeration__sep_by_zero_(radix, offsetted_digits, is_big_endian=is_big_endian, zero_digit=zero_digit, empty_uints_ok=False)
def nonempty_uints2bijective_numeration__sep_by_zero_(radix, nonempty_us, /, *, is_big_endian, zero_digit):
    'radix/uint{>=2} -> (Iter uint){nonempty} -> Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]} # [offset4digit := 1+zero_digit][original-bijective_numeration => [offset4digit:=1]]'
    return uints2may_bijective_numeration__sep_by_zero_(radix, nonempty_us, is_big_endian=is_big_endian, zero_digit=zero_digit, empty_uints_ok=False)





def _xempty_uints2bijective_numeration__sep_by_zero_(radix, us, /, *, is_big_endian, zero_digit, nonempty_vs_cased):
    '-> ((Iter [digit, digit...] | ^ValueError) if not nonempty_vs_cased else Iter [b_empty; digit...])'
    check_type_is(bool, nonempty_vs_cased)
    check_type_is(bool, is_big_endian)
    check_type_is(int, zero_digit)
    check_int_ge(2, radix)
    us = iter(us)

    offset4digit = 1+zero_digit
    u2ds_ = partial(uint2bijective_numeration_, radix, is_big_endian=is_big_endian, offset4digit=offset4digit)
    for u in us:
        #check_int_ge(0, u)
        break
    else:
        # empty
        if nonempty_vs_cased:
            # cased
            # b_empty = True
            yield True
        else:
            raise ValueError('uints are empty')
        return
    if 1:
        # head
        # nonempty
        if nonempty_vs_cased:
            # cased
            # b_empty = False
            yield False
        ds = u2ds_(u)
        yield from ds
    sep = zero_digit
    for u in us:
        #check_int_ge(0, u)
        # not head
        yield sep
        ds = u2ds_(u)
        yield from ds


def _iter_split_by_(zero_digit, offsetted_digits, /):
    '-> (Iter (Iter offsetted-digit)){nonempty}'
    it = iter(offsetted_digits)
    777; del offsetted_digits

    b_zero = True
    def not_zero_(d, /, *, z=zero_digit):
        nonlocal b_zero
        #b_zero = z == d
        b = z == d
        if b:
            b_zero = True
        return not b
    while b_zero:
        b_zero = False
        yield takewhile(not_zero_, it)




def uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_(decimal_str8digits, /, *, is_big_endian):
    'decimal_str8digits/str/regex"[0-9]*" -> (Iter uint)'
    nonempty_us = nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_(decimal_str8digits, is_big_endian=is_big_endian)
    us = uints5nonempty_uints__inc_or_dec_solo_uint_(nonempty_us)
    return us
def uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_(us, /, *, is_big_endian):
    '(Iter uint) -> decimal_str8digits/str/regex"[0-9]*"'
    nonempty_us = uints2nonempty_uints__inc_or_dec_solo_uint_(us)
    decimal_str8digits = nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_(nonempty_us, is_big_endian=is_big_endian)
    return decimal_str8digits

def uints5may_bijective_numeration__sep_by_zero__decimal_str_(may_decimal_str8digits, /, *, is_big_endian, empty_uints_ok=True):
    'may decimal_str8digits/str/regex"[0-9]*" -> (Iter uint)'
    check_type_is(bool, empty_uints_ok)
    ######################
    may_decimal_digits = fmap4may(decimal_str2iter_digits_, may_decimal_str8digits)
    #bug:radix = 10
    radix = 9
    zero_digit = 0
    us = uints5may_bijective_numeration__sep_by_zero_(radix, may_decimal_digits, is_big_endian=is_big_endian, zero_digit=zero_digit, empty_uints_ok=empty_uints_ok)
    return us
def uints2may_bijective_numeration__sep_by_zero__decimal_str_(us, /, *, is_big_endian, empty_uints_ok=True):
    '(Iter uint) -> may decimal_str8digits/str/regex"[0-9]*"'
    check_type_is(bool, empty_uints_ok)
    ######################
    radix = 9
    zero_digit = 0
    may_decimal_digits = uints2may_bijective_numeration__sep_by_zero_(radix, us, is_big_endian=is_big_endian, zero_digit=zero_digit, empty_uints_ok=empty_uints_ok)
    may_decimal_str8digits = fmap4may(decimal_str5iter_digits_, may_decimal_digits)
    return may_decimal_str8digits
def nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_(decimal_str8digits, /, *, is_big_endian):
    'decimal_str8digits/str/regex"[0-9]*" -> (Iter uint){nonempty}'
    return uints5may_bijective_numeration__sep_by_zero__decimal_str_(decimal_str8digits, is_big_endian=is_big_endian, empty_uints_ok=False)
def nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_(nonempty_us, /, *, is_big_endian):
    '(Iter uint){nonempty} -> decimal_str8digits/str/regex"[0-9]*"'
    return uints2may_bijective_numeration__sep_by_zero__decimal_str_(nonempty_us, is_big_endian=is_big_endian, empty_uints_ok=False)


























def _both_(f, kwds, /):
    _2 = f(to_vs_from=False, **kwds)
    _5 = f(to_vs_from=True, **kwds)
    return (_2, _5)
def uints25bijective_numeration__sep_by_zeroTT__both_(*, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint, using_decimal_str):
    kwds = {**locals()}
    return _both_(uints25bijective_numeration__sep_by_zeroTT_, kwds)
def uints25bijective_numeration__sep_by_zeroTT_(*, to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint, using_decimal_str):
    f = selector4uints25bijective_numeration__sep_by_zero_(to_vs_from=to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint, using_decimal_str=using_decimal_str)
    def _uints25bijective_numeration__sep_by_zeroT_(radix, /, *, is_big_endian, zero_digit):
        return partial(f, radix, is_big_endian=is_big_endian, zero_digit=zero_digit)
    def _uints25bijective_numeration__sep_by_zero__decimal_strT_(*, is_big_endian):
        return partial(f, is_big_endian=is_big_endian)
    return _uints25bijective_numeration__sep_by_zeroT_ if not using_decimal_str else _uints25bijective_numeration__sep_by_zero__decimal_strT_


def uints25bijective_numeration__sep_by_zeroT__both_(radix, *, is_big_endian, zero_digit, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint):
    kwds = {**locals()}
        # NOTE:radix become kw
    return _both_(uints25bijective_numeration__sep_by_zeroT_, kwds)
def uints25bijective_numeration__sep_by_zeroT_(radix, *, is_big_endian, zero_digit, to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint):
    # NOTE:radix become kw to support _both_@uints25bijective_numeration__sep_by_zeroT__both_
    return uints25bijective_numeration__sep_by_zeroTT_(to_vs_from=to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint, using_decimal_str=False)(radix, is_big_endian=is_big_endian, zero_digit=zero_digit)

def uints25bijective_numeration__sep_by_zero__decimal_strT__both_(*, is_big_endian, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint):
    kwds = {**locals()}
    return _both_(uints25bijective_numeration__sep_by_zero__decimal_strT_, kwds)
def uints25bijective_numeration__sep_by_zero__decimal_strT_(*, is_big_endian, to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint):
    return uints25bijective_numeration__sep_by_zeroTT_(to_vs_from=to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint=nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint, using_decimal_str=True)(is_big_endian=is_big_endian)
def selector4uints25bijective_numeration__sep_by_zero_(*, to_vs_from, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint, using_decimal_str):
    check_type_is(bool, to_vs_from)
    check_uint_lt(3, nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint)
    check_type_is(bool, using_decimal_str)
    k = to_vs_from
    j = nonempty_uints__vs__may_bijective_numeration__vs__inc_or_dec_solo_uint
    i = using_decimal_str
    f = _fs4TT[i*6+j*2+k]
    return f
_fs4TT = (*[]
,nonempty_uints2bijective_numeration__sep_by_zero_
,nonempty_uints5bijective_numeration__sep_by_zero_
,uints2may_bijective_numeration__sep_by_zero_
,uints5may_bijective_numeration__sep_by_zero_
,uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_
,uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_

,nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_
,nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_
,uints2may_bijective_numeration__sep_by_zero__decimal_str_
,uints5may_bijective_numeration__sep_by_zero__decimal_str_
,uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_
,uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_
)

































__all__
from seed.int_tools.digits.uint25bijective_numeration import decimal_str2iter_digits_, decimal_str5iter_digits_

from seed.int_tools.digits.uint25bijective_numeration import uints2nonempty_uints__inc_or_dec_solo_uint_, uints5nonempty_uints__inc_or_dec_solo_uint_




from seed.int_tools.digits.uint25bijective_numeration import uint5bijective_numeration_, uint2bijective_numeration_
from seed.int_tools.digits.uint25bijective_numeration import uint5bijective_numeration__decimal_str_, uint2bijective_numeration__decimal_str_

from seed.int_tools.digits.uint25bijective_numeration import uints5may_bijective_numeration__sep_by_zero_, uints2may_bijective_numeration__sep_by_zero_
from seed.int_tools.digits.uint25bijective_numeration import uints5may_bijective_numeration__sep_by_zero__decimal_str_, uints2may_bijective_numeration__sep_by_zero__decimal_str_

from seed.int_tools.digits.uint25bijective_numeration import nonempty_uints5bijective_numeration__sep_by_zero_, nonempty_uints2bijective_numeration__sep_by_zero_
from seed.int_tools.digits.uint25bijective_numeration import nonempty_uints5bijective_numeration__sep_by_zero__decimal_str_, nonempty_uints2bijective_numeration__sep_by_zero__decimal_str_







from seed.int_tools.digits.uint25bijective_numeration import uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_, uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint_
from seed.int_tools.digits.uint25bijective_numeration import uints5bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_, uints2bijective_numeration__sep_by_zero__inc_or_dec_solo_uint__decimal_str_





from seed.int_tools.digits.uint25bijective_numeration import uints25bijective_numeration__sep_by_zeroTT__both_, uints25bijective_numeration__sep_by_zeroT__both_, uints25bijective_numeration__sep_by_zero__decimal_strT__both_
from seed.int_tools.digits.uint25bijective_numeration import uints25bijective_numeration__sep_by_zeroTT_, uints25bijective_numeration__sep_by_zeroT_, uints25bijective_numeration__sep_by_zero__decimal_strT_, selector4uints25bijective_numeration__sep_by_zero_



from seed.int_tools.digits.uint25bijective_numeration import *
