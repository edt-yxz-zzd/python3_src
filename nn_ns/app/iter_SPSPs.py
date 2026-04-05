#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/iter_SPSPs.py

nn_ns.app.iter_SPSPs
py -m nn_ns.app.debug_cmd   nn_ns.app.iter_SPSPs -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.iter_SPSPs:__doc__ -ht # -ff -df
#######

[[
view ../../python3_src/seed/math/prime_gens.py.note.txt


(2,3,5,7)首败点:3215031751
assert A014233[3] == 3215031751
assert 2**31 < A014233[3] < 2**32

(2,3)首败点:1373653
assert A014233[1] == 1373653
assert 2**20 < A014233[1] < 2**21


]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =1  =2000 =3000
    #######total:1:
    2047

]]
[[
test:
    +_stderr_too_if_found
    +_stdout_too_if_raise
py_adhoc_call   nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =1  =2000 ='2**22' +verbose +_stderr_too_if_found +_stdout_too_if_raise

]]
[[
test:
    +also_stderr
    +flush4print
py_adhoc_call  { +also_stderr +flush4print }  nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =1  =2000 ='2**22' +verbose +_stdout_too_if_raise
    +_stderr_too_if_found --> +also_stderr

py_adhoc_call  { +also_stderr +flush4print }  nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =1  =2000 ='2**22' +verbose +_stdout_too_if_raise > /dev/null

]]
[[
py_adhoc_call   nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =2  =1373653 ='2**23'
    #######total:7:
    1373653
    1530787
    1987021
    2284453
    3116107
    5173601
    6787327

>>> 2**21
2097152
>>> 2**22
4194304

==>>:
    [{1373653,1530787,1987021,2284453,3116107,5173601,6787327} == SPSP{2,3}/-\[1..=2**23]]
        #total:7
    [{1373653,1530787,1987021,2284453,3116107} == SPSP{2,3}/-\[1..=2**22]]
        #total:5
    [{1373653,1530787,1987021} == SPSP{2,3}/-\[1..=2**21]]
        #total:3

===
py_adhoc_call  { +also_stderr +flush4print }  nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =2  ='2**23' ='2**25' +verbose +_stdout_too_if_raise > /sdcard/0my_files/tmp/-1tmp
    #######total:9:
    11541307
    13694761
    15978007
    16070429
    16879501
    25326001
    27509653
    27664033
    28527049

===
py_adhoc_call  { +also_stderr +flush4print }  nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =2  ='2**25' ='2**28' +verbose +_stdout_too_if_raise > /sdcard/0my_files/tmp/-1tmp
    #######total:19:
    54029741
    61832377
    66096253
    74927161
    80375707
    101649241
    102690677
    104852881
    105919633
    143168581
    154287451
    161304001
    193949641
    206304961
    218642029
    223625851
    247318957
    252853921
    259765747

==>>:
[SPSP{2,3}/-\[1..=2**28] == {1373653,1530787,1987021,2284453,3116107,5173601,6787327,11541307,13694761,15978007,16070429,16879501,25326001,27509653,27664033,28527049,54029741,61832377,66096253,74927161,80375707,101649241,102690677,104852881,105919633,143168581,154287451,161304001,193949641,206304961,218642029,223625851,247318957,252853921,259765747}]
    #total:35==7+9+19
    [21, 22, 23, 24, 25, 26, 27, 28]
    [3, 2, 2, 4, 5, 3, 6, 10]
    [3, 5, 7, 11, 16, 19, 25, 35]
]]
[[
echo $[2**32-3215031751]
    1079935545
10_7993_5545 #十亿
7秒 处理 百万/2**20
预计耗时:7千秒/2小时
==>>:
py_adhoc_call   nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =4  =3215031751 ='2**32' +verbose > /sdcard/0my_files/tmp/-1tmp

------at: 3450863617
^C KeyboardInterrupt
    testing: 3451195917 in range(3215031751, 4294967296, 2)
        =>total:1: 3215031751


py_adhoc_call   nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =4  =3451195917 ='2**32' +verbose +_stderr_too_if_found +_stdout_too_if_raise >> /sdcard/0my_files/tmp/-1tmp

------at: 3836739585
^C
    testing: 3836842735 in range(3451195917, 4294967296, 2)

py_adhoc_call   nn_ns.app.iter_SPSPs   ,iter_SPSPs_ =4  =3836842735 ='2**32' +verbose +_stderr_too_if_found +_stdout_too_if_raise >> /sdcard/0my_files/tmp/-1tmp
view /sdcard/0my_files/tmp/-1tmp
=>total:1: 3215031751
==>>:
    [{3215031751} == SPSP{2,3,5,7}/-\[1..=2**32]]
]]

]]]'''#'''
__all__ = r'''
iter_SPSPs_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
    from seed._lazy_ import mk_tuple, ifNone, check_int_ge, print_err
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.prime_gens import is_prime__le_pow2_81_, is_strong_probable_prime__basis_, prime_gen, hold_all_weakrefs4caches_
    #from itertools import count#islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def iter_SPSPs_(basis_or_num_primes, begin=None, end=None, /, *, verbose=False, _stderr_too_if_found=False, _stdout_too_if_raise=False):
    '(basis|num_primes)-> Iter SPSP{composite_number;strong pseudoprime{basis}}'
    ws = hold_all_weakrefs4caches_()
    if isinstance(basis_or_num_primes, int):
        num_primes = basis_or_num_primes
        basis = prime_gen[:num_primes]
    else:
        basis = basis_or_num_primes
    basis = mk_tuple(basis)
    if not basis:raise TypeError

    end = ifNone(end, 1<<81)
    check_int_ge(0, end)

    begin = ifNone(begin, 9)
    check_int_ge(0, begin)
    begin = max(begin, 1+max(basis))
    begin |= 1 #odd

    if verbose:print_err('start:', range(begin, end, 2))
    #for u in count(begin, 2)
    u = -1
    try:
        for u in range(begin, end, 2):
            if verbose and not (u&0x0F_FF_FE):print_err('------at:', u)
            #if is_prime__le_pow2_81_(u): continue
            if is_strong_probable_prime__basis_(basis, u) and not is_prime__le_pow2_81_(u):
                if _stderr_too_if_found:print_err(u)
                yield u
    except:
        print_err('testing:', u, 'in', range(begin, end, 2))
        if _stdout_too_if_raise:print('testing:', u, 'in', range(begin, end, 2))
        raise
    #except (KeyboardInterrupt, Exception)
    #except BaseException:

__all__
from nn_ns.app.iter_SPSPs import iter_SPSPs_
from nn_ns.app.iter_SPSPs import *
