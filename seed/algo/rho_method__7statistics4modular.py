#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/rho_method__7statistics4modular.py

seed.algo.rho_method__7statistics4modular
py -m nn_ns.app.debug_cmd   seed.algo.rho_method__7statistics4modular -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.rho_method__7statistics4modular:__doc__ -ht # -ff -df
#######

[[
rho%2**20: n->min4num_steps
    [p:<-[3..<2**20]][p::prime]
        [x0:=1]
        [x:=(1+x**2)%p]

!! iter_prefix_max4min4num_steps6modulus_le_
=> [[using default_setting: [x0:=1][x:=(1+x**2)%p][max4num_steps:=2**12]] -> [recognize prime < 2**18]]

#using_default_setting:goto
#using_alter_x0s:goto

]]


'#'; __doc__ = r'#'
>>> modulus2min4num_steps_(1)
1
>>> modulus2min4num_steps_(17)
13
>>> modulus2min4num_steps_(257)
36
>>> [*moduli2iter4min4num_steps_([1,2,3,5,7,31,127,17,257,65537,49,121,361,19,11])]
[1, 3, 2, 6, 4, 4, 17, 13, 36, 427, 4, 5, 8, 8, 5]
>>> [*moduli2iter4min4num_steps_([1,2,3,5,7,31,127,17,257,65537,49,121,361,19,11], with_modulus=True)]
[(1, 1), (2, 3), (3, 2), (5, 6), (7, 4), (31, 4), (127, 17), (17, 13), (257, 36), (65537, 427), (49, 4), (121, 5), (361, 8), (19, 8), (11, 5)]


>>> [*iter_prefix_max4min4num_steps6modulus_le_(257)]
[1, 3, 6, 7, 13, 17, 19, 25, 26, 29, 33, 48, 56, 59]
>>> [*iter_prefix_max4min4num_steps6modulus_le_(257, with_modulus=True)]
[(1, 1), (2, 3), (5, 6), (13, 7), (17, 13), (29, 17), (47, 19), (61, 25), (71, 26), (89, 29), (109, 33), (137, 48), (139, 56), (229, 59)]
>>> [*iter_prefix_max4min4num_steps6modulus_le_(400, with_modulus=True)]
[(1, 1), (2, 3), (5, 6), (13, 7), (17, 13), (29, 17), (47, 19), (61, 25), (71, 26), (89, 29), (109, 33), (137, 48), (139, 56), (229, 59), (331, 63), (359, 68)]
>>> [*iter_prefix_max4min4num_steps6modulus_le_(range(257,1+400), with_modulus=True, min4max4min4num_steps=1+59)]
[(331, 63), (359, 68)]
>>> [*iter_prefix_max4min4num_steps6modulus_le_(range(257,1+400), with_modulus=True)]
[(257, 36), (263, 57), (331, 63), (359, 68)]
>>> [*iter_prefix_max4min4num_steps6modulus_le_(range(257,1+400), with_modulus=True, min4max4min4num_steps=36)]
[(257, 36), (263, 57), (331, 63), (359, 68)]
>>> [*iter_prefix_max4min4num_steps6modulus_le_(range(257,1+400), with_modulus=True, min4max4min4num_steps=1+36)]
[(263, 57), (331, 63), (359, 68)]



>>> imay_max4min4num_steps6modulus_le_(0, with_modulus=True)
(-1, -1)
>>> imay_max4min4num_steps6modulus_le_(0)
-1
>>> imay_max4min4num_steps6modulus_le_(1)
1
>>> imay_max4min4num_steps6modulus_le_(257)
59
>>> imay_max4min4num_steps6modulus_le_(257, with_modulus=True)
(229, 59)
>>> imay_max4min4num_steps6modulus_le_(257, with_modulus=True, zmay_max4max4min4num_steps=13)
Traceback (most recent call last):
    ...
Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (29, 17))
>>> imay_max4min4num_steps6modulus_le_(257, with_modulus=True, min4max4min4num_steps=13)
(229, 59)
>>> imay_max4min4num_steps6modulus_le_(257, with_modulus=True, min4max4min4num_steps=59)
(229, 59)
>>> imay_max4min4num_steps6modulus_le_(257, with_modulus=True, min4max4min4num_steps=60)
(-1, -1)





















py_adhoc_call   seed.algo.rho_method__7statistics4modular   @f
]]]'''#'''
__all__ = r'''
modulus2min4num_steps_
    moduli2iter4min4num_steps_
        iter_prefix_max4min4num_steps6modulus_le_
            imay_max4min4num_steps6modulus_le_
                iter_imay_max4min4num_steps6modulus_le__5x0s_



max4modulus5or_moduli_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from math import gcd

#.#################################
___end_mark_of_excluded_global_names__0___ = ...
__all__
r'''[[[

[[
using_default_setting:here
===
py_adhoc_call   seed.algo.rho_method__7statistics4modular   @modulus2min4num_steps_  =17
    13
py_adhoc_call   seed.algo.rho_method__7statistics4modular   @modulus2min4num_steps_  =257
    36
py_adhoc_call   seed.algo.rho_method__7statistics4modular   @modulus2min4num_steps_  =65537
    427

py_adhoc_call   seed.algo.rho_method__7statistics4modular   ,moduli2iter4min4num_steps_  +with_modulus ='[1,2,3,5,7,31,127,17,257,65537,49,121,361,19,11]'
    (1, 1)
    (2, 3)
    (3, 2)
    (5, 6)
    (7, 4)
    (31, 4)
    (127, 17)
    (17, 13)
    (257, 36)
    (65537, 427)
    (49, 4)
    (121, 5)
    (361, 8)
    (19, 8)
    (11, 5)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  =257
    (229, 59)
    total::duration: 0.04239853200000002 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**12'
    (3467, 401)
    total::duration: 0.24843468999999996 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**14'
    (13649, 821)
    total::duration: 0.467131152 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**15'
    (27691, 1549)
    total::duration: 0.539014309 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**16'
    (65053, 1884)
    total::duration: 1.17582701 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**17'
    (130399, 3462)
    total::duration: 2.823190313 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**18'
    (246203, 3783)
    total::duration: 7.07480101 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**10' --zmay_max4max4min4num_steps='100'
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (521, 118))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12'
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (290047, 6251))
    total::duration: 8.099590388000001 *(unit: 0:00:01)
    # [290047 == 0b1000110110011111111 == 2**18 +2**14 + ...]

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   ,100:iter_prefix_max4min4num_steps6modulus_le_  +with_modulus  ='range(1800,2000)' --min4max4min4num_steps='60'
    (1801, 83)
    (1823, 94)
    (1847, 122)
    (1867, 213)
    total::duration: 0.04840392399999999 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   ,100:iter_prefix_max4min4num_steps6modulus_le_  +with_modulus  ='range(2**18,2**20)' --min4max4min4num_steps='2**12'
    (290047, 6251)
    (419171, 6397)
    (501617, 6583)
    (514639, 6625)
    (594313, 6764)
    (636731, 6832)
    (686551, 6962)
    (744859, 7151)
    (776759, 7461)
    (874771, 7685)
    total::duration: 41.395291883 *(unit: 0:00:01)

]]
[[
using_alter_x0s:here
===
x0 avoid (x0+u**2)
    1,2,5,26,677,...
    3,10,101,10202,...
    4,17,290,...
    6,37,1370,...
    7,50,2501,...
    8,65,...
    9,82,...
    11,122,...
    12,145,...
    13
    14
    15
    16
    18
    19
    20

===
py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   ,iter_imay_max4min4num_steps6modulus_le__5x0s_  +with_modulus +with_x0 ='2**12' ='[1,34,6,7,8,9,11,12]'
    (1, (3467, 401))
    (34, (3467, 401))
    (6, (3919, 290))
    (7, (3467, 401))
    (8, (3467, 401))
    (9, (3467, 401))
    (11, (3467, 401))
    (12, (3467, 401))
    total::duration: 0.35548261600000003 *(unit: 0:00:01)


py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**16' =6
    (65053, 1884)
    total::duration: 1.191091928 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =6
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (280897, 4470))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =3
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (290047, 6251))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =4
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (290047, 6251))
    total::duration: 8.134360934 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =7
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (290047, 6251))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =8
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (290047, 6251))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =9
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (279823, 4242))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =11
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (312211, 4268))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =12
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (290047, 6251))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   ,iter_imay_max4min4num_steps6modulus_le__5x0s_  +with_modulus +with_x0 ='[290047]' ='range(1,101)' | grep -v -e '(290047, 6251)'
    (11, (290047, 527))
    (18, (290047, 143))
    (42, (290047, 56))
    (52, (290047, 271))
    (63, (290047, 527))                    (77, (290047, 271))
    (80, (290047, 143))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   ,iter_imay_max4min4num_steps6modulus_le__5x0s_  +with_modulus +with_x0 ='[335299]' ='[11,18,42,52,63,80]' | grep -v -e '(335299, 6284)'
    (80, (335299, 557))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =80
    ^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (366917, 4365))

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   ,iter_imay_max4min4num_steps6modulus_le__5x0s_  +with_modulus +with_x0 ='[290047,335299,366917]' ='range(101,500)' | grep -v -e '(290047, 6251)\|(335299, 6284)\|(366917, 4365)'
    (288, (366917, 953))
    (296, (366917, 781))
    (390, (366917, 2317))
    (456, (366917, 953))
    total::duration: 2.3564128569999996 *(unit: 0:00:01)

py_adhoc_call { +to_show_total_timedelta }  seed.algo.rho_method__7statistics4modular   @imay_max4min4num_steps6modulus_le_  +with_modulus  ='2**20' --zmay_max4max4min4num_steps='2**12' =288
    ^^Exception: ('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (344293, 4100))


vs:
    (290047, 6251){x0:=1,3,4,7,8,12,13,14,15,16,19,21,22}
    (280897, 4470){x0:=6,20}
    (279823, 4242){x0:=9}
    (312211, 4268){x0:=11}
    (335299, 6284){x0:=18,42}
    (366917, 4365){x0:=80}
    (344293, 4100){x0:=288}

[312211 == 0b1001100001110010011 == 2**18+2**15+...]
[366917 == 0b1011001100101000101 == 2**18+2**16+...]


]]



#]]]'''#'''



__all__

def max4modulus5or_moduli_(max4modulus_or_moduli, /):
    match max4modulus_or_moduli:
        case int() as max4modulus:
            moduli = range(1, 1+max4modulus)
        case moduli:
            iter(moduli)
    moduli
    return moduli
def iter_imay_max4min4num_steps6modulus_le__5x0s_(max4modulus_or_moduli, x0s, addend=1, exp=2, /, *, known_modulus_be_prime=False, with_modulus=False, zmay_max4max4min4num_steps=0, min4max4min4num_steps=0, with_x0=False):
    for x0 in x0s:
        r = imay_max4min4num_steps6modulus_le_(max4modulus_or_moduli, x0, addend, exp, known_modulus_be_prime=known_modulus_be_prime, with_modulus=with_modulus, zmay_max4max4min4num_steps=zmay_max4max4min4num_steps, min4max4min4num_steps=min4max4min4num_steps)
        yield r if not with_x0 else (x0, r)

def imay_max4min4num_steps6modulus_le_(max4modulus_or_moduli, x0=1, addend=1, exp=2, /, *, known_modulus_be_prime=False, with_modulus=False, zmay_max4max4min4num_steps=0, min4max4min4num_steps=0):
    check_int_ge(0, zmay_max4max4min4num_steps)
    it = iter_prefix_max4min4num_steps6modulus_le_(max4modulus_or_moduli, x0, addend, exp, known_modulus_be_prime=known_modulus_be_prime, with_modulus=True, min4max4min4num_steps=min4max4min4num_steps)
    imay_modulus = -1
    imay_max4min4num_steps = -1
    for (imay_modulus, imay_max4min4num_steps) in it:
        if 0 < zmay_max4max4min4num_steps < imay_max4min4num_steps:
            raise Exception('imay_max4min4num_steps6modulus_le_()!!zmay_max4max4min4num_steps', (imay_modulus, imay_max4min4num_steps))
    return imay_max4min4num_steps if not with_modulus else (imay_modulus, imay_max4min4num_steps)

def iter_prefix_max4min4num_steps6modulus_le_(max4modulus_or_moduli, x0=1, addend=1, exp=2, /, *, known_modulus_be_prime=False, with_modulus=False, min4max4min4num_steps=0):
    check_int_ge(0, min4max4min4num_steps)
    moduli = max4modulus5or_moduli_(max4modulus_or_moduli)

    it = moduli2iter4min4num_steps_(moduli, x0, addend, exp, known_modulus_be_prime=known_modulus_be_prime, with_modulus=True)
    imay_modulus = -1
    imay_max4min4num_steps = -1 if 0 == min4max4min4num_steps else -1+min4max4min4num_steps
    for modulus, min4num_steps in it:
        if min4num_steps > imay_max4min4num_steps:
            imay_modulus = modulus
            imay_max4min4num_steps = min4num_steps
            yield imay_max4min4num_steps if not with_modulus else (imay_modulus, imay_max4min4num_steps)

    if imay_modulus == -1:
        imay_max4min4num_steps = -1
    return imay_max4min4num_steps if not with_modulus else (imay_modulus, imay_max4min4num_steps)

def moduli2iter4min4num_steps_(moduli, x0=1, addend=1, exp=2, /, *, known_modulus_be_prime=False, with_modulus=False):
    for modulus in moduli:
        min4num_steps = modulus2min4num_steps_(modulus, x0, addend, exp, known_modulus_be_prime=known_modulus_be_prime)
        yield min4num_steps if not with_modulus else (modulus, min4num_steps)
def modulus2min4num_steps_(modulus, x0=1, addend=1, exp=2, /, *, known_modulus_be_prime=False):
    'modulus/int{>=1} -> x[0] -> addend -> exp/int{>=1} -> min4num_steps/int{>=1} # [[x[1+j] := (addend+x[j]**exp)%modulus][x[min4num_steps] == x[-1+2**floor_log2(min4num_steps)]]]'
    check_int_ge(1, modulus)
    check_type_is(int, x0)
    check_type_is(int, addend)
    check_type_is(int, exp)
    if known_modulus_be_prime:
        exp %= (-1+modulus)
    check_int_ge(1, exp)

    x0 %= modulus
    addend %= modulus

    ez4ipp = 0
    i = 0
    # [1+i == 2**ez4ipp]
    xi = x0
    j = i
    xj = xi
    while 1:
        # [i <= j < 2*(1+i)]
        for j in range(1+i, 2*(1+i)):
            xj = (addend +pow(xj, exp, modulus)) %modulus
            if 1 < gcd(modulus, xj-xi) or 1==modulus:
                # [1 < gcd(modulus, xj-xi) <= modulus]
                min4num_steps = j
                return j
        ###########
        if i > modulus:
            raise Exception('modulus2min4num_steps_()', modulus, x0, addend, exp, [(i,xi), (j,xj)])
        ###########
        ez4ipp += 1
        i = 1+2*i
        assert j == i
        xi = xj
        ###########

__all__
from seed.algo.rho_method__7statistics4modular import modulus2min4num_steps_, imay_max4min4num_steps6modulus_le_
from seed.algo.rho_method__7statistics4modular import *
