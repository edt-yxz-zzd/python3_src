#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_pint/easy_primes.py
view ../../python3_src/seed/math/primes__inductive_generated__almost_smooth.py
    欤扩展幺链素数扌
    欤再扩展幺链素数扌
view script/枚举冫加一偶幂型素数.py
    #view script/枚举冫双幂方和型素数.py

seed.math.prime_pint.easy_primes
py -m nn_ns.app.debug_cmd   seed.math.prime_pint.easy_primes -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_pint.easy_primes:__doc__ -ht # -ff -df

[[
类似于:欤再扩展幺链素数扌
但是，自定义分解方案
]]

############
py_adhoc_call   seed.math.prime_pint.easy_primes   @list.10:iter_easy_primes__trial_division__fixed_known_primes_ ='[2,3]'  ='0'
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ ='[2,3]'  ='2**16'
65537
65557
65713
65719
65809
65867
66107
66169
66449
66629
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ ='[2,3]'  ='2**20'
1048627
1048897
1049773
1049809
1049977
1050013
1050769
1050773
1051069
1051409
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ ='[2,3]'  ='2**32'
KeyboardInterrupt

############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ ='[2,3,5,7,11,13,17,19,23,29]'  ='2**32'
4294967377
4294967387
4294967561
4294967653
4294967681
4294967821
4294967857
4294967861
4294967977
4294968317
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ ='[2,3,5,7,11,13,17,19,23,29]'  ='2**64'   ='2**64+10**5'
    <NONE>

############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ :'<0x1_00_00'  ='2**64'   ='2**64+10**4'
18446744073709551629
18446744073709551653
18446744073709551667
18446744073709552109
18446744073709552157
18446744073709552333
18446744073709552357
18446744073709552421
18446744073709552501
18446744073709552597

############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ :'<0x1_00_00'  ='2**128'   ='2**128+10**4'
    <NONE>

############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,1:iter_easy_primes__trial_division__fixed_known_primes_ :'<0x1_00_00'  ='2**128+10**4' +verbose
... ...
(12623, 340282366920938463463374607431768234079)
340282366920938463463374607431768234079
    ==2**128+10**4+12623
    ==2**128+22623

velidate:
py_adhoc_call   seed.math.prime_pint.easy_primes   ,1:iter_easy_primes__trial_division__fixed_known_primes_ :'<0x1_00_00'  ='2**128' +verbose
... ...
(22623, 340282366920938463463374607431768234079)
340282366920938463463374607431768234079

############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,1:iter_easy_primes__trial_division__fixed_known_primes_ :'<0x1_00_00'  ='2**128+22623+1' +verbose
... ...
(953, 340282366920938463463374607431768235033)
340282366920938463463374607431768235033
    ==2**128+22623+1+953
    ==2**128+22623+954
    ==2**128+23577
############
>>> 340282366920938463463374607431768234079 ==2**128+10**4+12623 ==2**128+22623
True
>>> 340282366920938463463374607431768235033 ==2**128+22623+1+953 ==2**128+22623+954 ==2**128+23577
True

############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,10:iter_easy_primes__trial_division__fixed_known_primes_ :'<0x1_00_00'  ='2**128+23577+1' +to_show6catch
340282366920938463463374607431768237277
340282366920938463463374607431768242071
340282366920938463463374607431768257329
340282366920938463463374607431768258787
340282366920938463463374607431768262661
340282366920938463463374607431768271817
340282366920938463463374607431768276509
340282366920938463463374607431768276721
340282366920938463463374607431768277241
340282366920938463463374607431768286669
############


############
############
+reverse
############
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,1:iter_easy_primes__trial_division__fixed_known_primes_ :'<0x1_00_00'  ='2**128' +verbose +reverse
... ...
(3837, 340282366920938463463374607431768207619)
340282366920938463463374607431768207619
############

>>> (340282366920938463463374607431768286669-340282366920938463463374607431768207619)
79050
>>> (340282366920938463463374607431768286669-340282366920938463463374607431768207619)/(12-0)
6587.5
>>> (340282366920938463463374607431768286669-340282366920938463463374607431768234079)/(12-1)
4780.909090909091
>>> (340282366920938463463374607431768234079-340282366920938463463374607431768207619)/(1-0)
26460.0


############
tmp_test='<xxx'
echo "$tmp_test"
echo "${tmp_test}"
echo ${tmp_test}
<xxx

us_13='[340282366920938463463374607431768207619,340282366920938463463374607431768234079,340282366920938463463374607431768235033,340282366920938463463374607431768237277,340282366920938463463374607431768242071,340282366920938463463374607431768257329,340282366920938463463374607431768258787,340282366920938463463374607431768262661,340282366920938463463374607431768271817,340282366920938463463374607431768276509,340282366920938463463374607431768276721,340282366920938463463374607431768277241,340282366920938463463374607431768286669]'
echo "$us_13"
echo "${us_13}"
echo "'${us_13}'"
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_ :'<0x1_00_00'  ="${us_13}"
(340282366920938463463374607431768207619, 4755326233275085093214878173517, 169185114351068033, 188822672266817, 199501, 26003, 16339, 1303, 443, 251, 149, 113, 37, 19, 7, 5, 3, 2)
(340282366920938463463374607431768234079, 1552748849297529604457525479619, 776374424648764802228762739809, 105946291573248471919863911, 22913895579323020873, 222188887395499, 295777, 13267, 9437, 4297, 229, 103, 79, 67, 41, 31, 13, 5, 3, 2)
(340282366920938463463374607431768235033, 14278380619374725724377920754941601, 4562284561, 61681, 1321, 331, 257, 241, 229, 151, 61, 41, 31, 19, 17, 13, 11, 7, 5, 3, 2)
(340282366920938463463374607431768237277, 691630827075078177771086600471073653, 13300592828366888034059357701366801, 4562284561, 61681, 1321, 331, 257, 241, 229, 151, 61, 41, 31, 19, 17, 13, 11, 7, 5, 3, 2)
(340282366920938463463374607431768242071, 42453096057875246985945289362443, 728707710405919246157249, 16426742647451, 497027009, 56773, 28657, 4241, 971, 661, 421, 271, 229, 131, 29, 7, 5, 3, 2)
(340282366920938463463374607431768257329, 6361791502976084283020725229, 3653422052975830048297, 5142941277542921, 214465439, 573437, 33487, 29599, 1811, 863, 271, 227, 139, 31, 23, 19, 17, 13, 11, 5, 3, 2)
(340282366920938463463374607431768258787, 10292504572913892294092044483823, 173140405963629046430239957, 418711139720704427557, 1318187966603, 162473, 29723, 10223, 9629, 3217, 2749, 2027, 883, 97, 23, 17, 13, 11, 7, 3, 2)
(340282366920938463463374607431768262661, 5198454592037244186851318579, 2704606894446958955197, 46896331082311, 14082982307, 360197, 26309, 14177, 5297, 4013, 1783, 173, 113, 37, 31, 17, 11, 7, 5, 3, 2)
(340282366920938463463374607431768271817, 23487187114918447229664177763098307, 6361791502976084283020725229, 3653422052975830048297, 5142941277542921, 214465439, 573437, 33487, 29599, 1811, 863, 271, 227, 139, 31, 23, 19, 17, 13, 11, 5, 3, 2)
(340282366920938463463374607431768276509, 378130419177988127809057991659, 2571279183884304599659, 19867483729, 137968637, 20773, 17807, 5801, 2293, 2069, 509, 179, 149, 97, 59, 19, 13, 7, 3, 2)
(340282366920938463463374607431768276721, 17191598842418021887698235339, 97972870219723621, 49481247585719, 17459381, 44053, 5737, 2473, 419, 353, 229, 223, 103, 19, 13, 11, 7, 5, 3, 2)
(340282366920938463463374607431768277241, 654389167155650891275720398907246687, 17191598842418021887698235339, 97972870219723621, 49481247585719, 17459381, 44053, 5737, 2473, 419, 353, 229, 223, 103, 19, 13, 11, 7, 5, 3, 2)
(340282366920938463463374607431768286669, 34916600185888628400194593, 121238195089891070834009, 115685300658293006521, 519113526193, 70685393, 53791, 45613, 9931, 859, 331, 139, 131, 37, 17, 11, 5, 3, 2)
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_ :'<0x20_00'  ="${us_13}"
=[out]=
py_adhoc_call   seed.math.prime_pint.easy_primes   ,iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_ :'<13267'  ="${us_13}"
-340282366920938463463374607431768207619
-340282366920938463463374607431768234079
-340282366920938463463374607431768235033
-340282366920938463463374607431768237277
-340282366920938463463374607431768242071
-340282366920938463463374607431768257329
-340282366920938463463374607431768258787
-340282366920938463463374607431768262661
-340282366920938463463374607431768271817
-340282366920938463463374607431768276509
-340282366920938463463374607431768276721
-340282366920938463463374607431768277241
-340282366920938463463374607431768286669
############
上下两例说明easy_prime十分稀少#(2**128附近79050多个数里,才有一个easy_prime{PRIMES_le13267},没有一个easy_prime{PRIMES_lt13267})
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_ :'<0x40_00'  ="${us_13}"
=[out]=
py_adhoc_call   seed.math.prime_pint.easy_primes   ,iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_ :'<13267+1'  ="${us_13}"
-340282366920938463463374607431768207619
(340282366920938463463374607431768234079, 1552748849297529604457525479619, 776374424648764802228762739809, 105946291573248471919863911, 22913895579323020873, 222188887395499, 295777, 13267, 9437, 4297, 229, 103, 79, 67, 41, 31, 13, 5, 3, 2)
-340282366920938463463374607431768235033
-340282366920938463463374607431768237277
-340282366920938463463374607431768242071
-340282366920938463463374607431768257329
-340282366920938463463374607431768258787
-340282366920938463463374607431768262661
-340282366920938463463374607431768271817
-340282366920938463463374607431768276509
-340282366920938463463374607431768276721
-340282366920938463463374607431768277241
-340282366920938463463374607431768286669
############
py_adhoc_call   seed.math.prime_pint.easy_primes   ,iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_ :'<0x80_00'  ="${us_13}"
(340282366920938463463374607431768207619, 4755326233275085093214878173517, 169185114351068033, 188822672266817, 199501, 26003, 16339, 1303, 443, 251, 149, 113, 37, 19, 7, 5, 3, 2)
(340282366920938463463374607431768234079, 1552748849297529604457525479619, 776374424648764802228762739809, 105946291573248471919863911, 22913895579323020873, 222188887395499, 295777, 13267, 9437, 4297, 229, 103, 79, 67, 41, 31, 13, 5, 3, 2)
-340282366920938463463374607431768235033
-340282366920938463463374607431768237277
-340282366920938463463374607431768242071
-340282366920938463463374607431768257329
(340282366920938463463374607431768258787, 10292504572913892294092044483823, 173140405963629046430239957, 418711139720704427557, 1318187966603, 162473, 29723, 10223, 9629, 3217, 2749, 2027, 883, 97, 23, 17, 13, 11, 7, 3, 2)
(340282366920938463463374607431768262661, 5198454592037244186851318579, 2704606894446958955197, 46896331082311, 14082982307, 360197, 26309, 14177, 5297, 4013, 1783, 173, 113, 37, 31, 17, 11, 7, 5, 3, 2)
-340282366920938463463374607431768271817
(340282366920938463463374607431768276509, 378130419177988127809057991659, 2571279183884304599659, 19867483729, 137968637, 20773, 17807, 5801, 2293, 2069, 509, 179, 149, 97, 59, 19, 13, 7, 3, 2)
-340282366920938463463374607431768276721
-340282366920938463463374607431768277241
-340282366920938463463374607431768286669
############




from seed.math.prime_pint.easy_primes import *
]]]'''#'''
__all__ = r'''
IDetectEasyPrime
    DetectEasyPrime__trial_division__fixed_known_primes
DetectEasyNumber

iter_easy_primes__trial_division__fixed_known_primes_
iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import pairwise
from seed.tiny_.check import check_type_le, check_type_is, check_int_ge

from seed.helper.lazy_import import BaseCachedPropertyGroup, ImportProperty
class _Imports(BaseCachedPropertyGroup):
    def print_err(sf, /):
        from seed.tiny import print_err
        return print_err
    def mk_tuple(sf, /):
        from seed.tiny import mk_tuple
        return mk_tuple
    def is_strict_sorted(sf, /):
        from seed.iters.is_sorted import is_strict_sorted
        return is_strict_sorted
    factor_pint_as_pefect_power_ = ImportProperty('seed.math.factor_pint_as_pefect_power_', 'factor_pint_as_pefect_power_')
    semi_factor_pint_via_trial_division = ImportProperty('seed.math.semi_factor_pint_via_trial_division', 'semi_factor_pint_via_trial_division')
    complete_factor_pint_via_trial_division = ImportProperty('seed.math.semi_factor_pint_via_trial_division', 'complete_factor_pint_via_trial_division')
    is_prime__via_complete_factorization_Nmm_ = ImportProperty('seed.math.is_prime__via_complete_factorization_Nmm_', 'is_prime__via_complete_factorization_Nmm_')
    repr_helper = ImportProperty('seed.helper.repr_input', 'repr_helper')
    #z = ImportProperty('x', 'z')
_imports = _Imports()
#.from seed.tiny import mk_tuple
#.from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
#.from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
#.from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
#.from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError


class IDetectEasyPrime(ABC):
    __slots__ = ()
    @abstractmethod
    def _may_factor_pint__relax_(sf, u, /):
        'u/pint -> may ft2e/{pint:pint}'
    @abstractmethod
    def _tribool_detect_prime__relax_(sf, u, /, *, from_factor:bool):
        'u/pint -> tribool/(-1/recur_detect|0/composite/+1/prime)'
    def is_easy_prime_(sf, u, /, *, from_factor:bool=False):
        return bool(sf.may_detect_easy_prime_ex_(u, from_factor=from_factor))
    def may_detect_easy_prime_ex_(sf, u, /, *, from_factor:bool):
        'u/pint -> may certification4easy_prime/primes/[pint]{reverse-sorted}{nonempty}{primes[0]==u}'
        return sf.may_detect_easy_primes_ex_([u], from_factor=from_factor)
    def may_detect_easy_primes_ex_(sf, us, /, *, from_factor:bool):
        'us/(Iter pint) -> may certification4easy_primes/primes/[pint]{reverse-sorted}{nonempty}'
        us = tuple(us)
        for u in us:
            check_type_is(int, u)
        if not all(u == 2 or (u > 2 and u&1)  for u in us):
            return None
        us = sorted(set(us))
        if not all(abs(sf._tribool_detect_prime__relax_(u, from_factor=from_factor)) == 1 for u in us):
            return None
        p2em = p2emay_ft2pmm = {}
        def put(u, /):
            if u in p2em:
                return
            us.append(u)
        #put(u)
        while us:
            u = us.pop()
            match sf._tribool_detect_prime__relax_(u, from_factor=True):
                case 1:
                    #prime
                    p = u
                    p2em[p] = ...
                    #relax_known_prime
                    continue
                case 0:
                    #composite
                    return None
                case -1:
                    #maybe_prime
                    pass
                case r:
                    raise ValueError(r)
            #end-match sf._tribool_detect_prime__relax_(u):
            #maybe_prime
            #assume prime
            p = u
            pmm = p-1
            may_ft2e4pmm = sf._may_factor_pint__relax_(pmm)
            if may_ft2e4pmm is None:
                return None
            ft2e4pmm = may_ft2e4pmm
            p2em[p] = ft2e4pmm
            if 0 == len(ft2e4pmm):
                assert p==2
                #prime
            else:
                fts = sorted(ft2e4pmm)
                assert fts[-1] < pmm
                assert 2 <= fts[0]
                for ft in reversed(fts):
                    put(ft)
            pass
        #end-while us:
        p2emay_ft2pmm
        items = sorted(p2emay_ft2pmm.items())
        for p, emay_ft2e4pmm in items:
            if emay_ft2e4pmm is ...:
                #relax_known_prime
                continue
            ft2e4pmm = emay_ft2e4pmm
            if not _imports.is_prime__via_complete_factorization_Nmm_(ft2e4pmm, p):
                return None
        #p2emay_ft2pmm
        certification4easy_primes = primes = tuple(p for p, _ in reversed(items))
        return certification4easy_primes
    #end-def may_detect_easy_primes_ex_(sf, us, /):
    def certify_(sf, certification4easy_prime, /):
        'certification4easy_prime/primes/[pint]{reverse-sorted}{nonempty}{primes[0]==u} -> None|^Exception'
        return _certify_(sf, certification4easy_prime, prime_vs_pint=False)
#class IDetectEasyPrime(ABC):
def _certify_(sf, certification4easy_prime, /, prime_vs_pint=False):
    'certification4easy_prime/primes/[pint]{reverse-sorted}{nonempty}{primes[0]==u} -> None|^Exception'
    check_type_is(tuple, certification4easy_prime)
    if not certification4easy_prime:raise TypeError
    for x in certification4easy_prime:
        check_int_ge(2, x)
    if not all(a > b for a, b in pairwise(certification4easy_prime)):raise TypeError
    if not all(abs(sf._tribool_detect_prime__relax_(u, from_factor=False)) == 1 for u in certification4easy_prime):raise TypeError
    #######
    u = certification4easy_prime[0]
    #######
    if prime_vs_pint:
        #easy_number
        may_ft2e = sf._may_factor_pint__relax_(u)
        if may_ft2e is None: raise TypeError
        ft2e = may_ft2e
        vs = sorted(ft2e)
        ps = set(certification4easy_prime)
    else:
        #easy_prime
        vs = [u]
    vs
    #######
    _ps = set()
    for v in vs:
        may_certification4v = _DetectEasyPrime4certify(sf, certification4easy_prime).may_detect_easy_prime_ex_(v, from_factor=True)
        if may_certification4v is None: raise ValueError(u, v)
        certification4v = may_certification4v
        if prime_vs_pint:
            #easy_number
            if not all(p in ps for p in certification4v):raise ValueError(certification4easy_prime, certification4v)
            _ps.update(certification4v)
        else:
            #easy_prime
            if not certification4easy_prime == certification4v:raise ValueError(certification4easy_prime, certification4v)
        pass
    #######
    if prime_vs_pint:
        #easy_number
        if not _ps == ps:raise ValueError(ps-_ps)
    #######
#end-def _certify_(sf, certification4easy_prime, /):
class _DetectEasyPrime4certify(IDetectEasyPrime):
    ___no_slots_ok___ = True
    def __init__(sf, aDetectEasyPrime, certification4easy_prime, /):
        check_type_le(IDetectEasyPrime, aDetectEasyPrime)
        sf.aDetectEasyPrime = aDetectEasyPrime
        sf.certification4easy_prime = certification4easy_prime
        #sf._ps = set(certification4easy_prime)
    @override
    def _may_factor_pint__relax_(sf, u, /):
        'u/pint -> may ft2e/{pint:pint}'
        return _imports.complete_factor_pint_via_trial_division(sf.certification4easy_prime, u)
    @override
    def _tribool_detect_prime__relax_(sf, u, /, *, from_factor:bool):
        'u/pint -> tribool/(-1/recur_detect|0/composite/+1/prime)'
        return sf.aDetectEasyPrime._tribool_detect_prime__relax_(u, from_factor=from_factor)
#end-class _DetectEasyPrime4certify(IDetectEasyPrime):
def _prepare_arg__primes(primes_or_spec, /):
    if type(primes_or_spec) is str:
        s = primes_or_spec
        if s.startswith('<='):
            max0 = eval(s[2:])
            max1 = max0+1
        elif s.startswith('<'):
            max1 = eval(s[1:])
        else:
            raise Exception(s)
        max1
        check_type_is(int, max1)
        from seed.math.prime_gens import raw_list_all_strict_sorted_primes__lt_#prime_gen
        primes = raw_list_all_strict_sorted_primes__lt_(max1, to_cache_only_busy_primes_plus_next=False, may_primes=None)
    else:
        primes = primes_or_spec
    primes
    prime_seq = _imports.mk_tuple(primes)
    assert _imports.is_strict_sorted(prime_seq)
        #assert list(prime_seq) == sorted(prime_seq)
    assert prime_seq
    assert prime_seq[0] == 2
    prime_set = set(prime_seq)
    assert len(prime_set) == len(prime_seq)
    return (prime_seq, prime_set)
class DetectEasyPrime__trial_division__fixed_known_primes(IDetectEasyPrime):
    ___no_slots_ok___ = True
    def __init__(sf, primes_or_spec, /):
        (prime_seq, prime_set) = _prepare_arg__primes(primes_or_spec)
        sf._ps = prime_seq
        sf._p_set = prime_set
    def __repr__(sf, /):
        return _imports.repr_helper(sf, sf._ps)
    @override
    def _may_factor_pint__relax_(sf, u, /):
        'u/pint -> may ft2e/{pint:pint}'
        (p2e, unfactored_part) = _imports.semi_factor_pint_via_trial_division(sf._ps, u)
        if not unfactored_part == 1:
            (n, e) = _imports.factor_pint_as_pefect_power_(unfactored_part)
            assert not n in p2e
            p2e[n] = e
        return p2e
    @override
    def _tribool_detect_prime__relax_(sf, u, /, *, from_factor:bool):
        'u/pint -> tribool/(-1/recur_detect|0/composite/+1/prime)'
        return +1 if u in sf._p_set else (-1 if from_factor or all(u%p for p in sf._ps) else 0)
class DetectEasyNumber:
    def __init__(sf, aDetectEasyPrime, /):
        check_type_le(IDetectEasyPrime, aDetectEasyPrime)
        sf._aDetectEasyPrime = aDetectEasyPrime
    def __repr__(sf, /):
        return _imports.repr_helper(sf, sf._aDetectEasyPrime)
    def is_easy_number_(sf, u, /, *, from_factor:bool=False):
        return bool(sf.may_detect_easy_number_ex_(u, from_factor=from_factor))
    def may_detect_easy_number_ex_(sf, u, /, *, from_factor:bool):
        #vs:may_detect_easy_prime_ex_
        #vs:may_detect_easy_number_ex_
        'u/pint -> may certification4easy_number/[pint]{reverse-sorted}{nonempty}{certification4easy_number[0]==u}'
        check_type_is(int, u)
        if not u >= 1:
            return None
        may_ft2e = sf._aDetectEasyPrime._may_factor_pint__relax_(u) if not from_factor else None
        if may_ft2e is None:
            # u may be prime
            vs = [u]
        else:
            ft2e = may_ft2e
            vs = sorted(ft2e)
        vs
        may_certification4vs = sf._aDetectEasyPrime.may_detect_easy_primes_ex_(vs, from_factor=True)
        may_certification4easy_number = may_certification4vs
        if not may_certification4vs is None:
            certification4vs = may_certification4vs
            if not certification4vs[0] == u:
                certification4easy_number = (u, *certification4vs)
                may_certification4easy_number = certification4easy_number
        may_certification4easy_number
        return may_certification4easy_number
    def certify_(sf, certification4easy_number, /):
        'certification4easy_number/[pint]{reverse-sorted}{nonempty}{certification4easy_number[0]==u} -> None|^Exception'
        return _certify_(sf._aDetectEasyPrime, certification4easy_number, prime_vs_pint=True)
#end-class DetectEasyNumber:

def iter_easy_primes__trial_division__fixed_known_primes_(primes_or_spec, /, begin=0, end=None, *, reverse=False, verbose=False, to_show6catch=False):
    from seed.math.prime_gens import hold_all_weakrefs4caches_
    __ws = hold_all_weakrefs4caches_()
    from seed.iters.count_ import count_
    aDetectEasyPrime = DetectEasyPrime__trial_division__fixed_known_primes(primes_or_spec)
    if not type(begin) is int:
        iter(begin)
        if not end is None:raise TypeError
        if reverse:raise TypeError
        us = iter(begin)
    elif reverse:
        us = iter(range(begin, (0 if end is None else end), -1))
    else:
        us = count_(begin, end)
    us
    if verbose:
        def __(us=us, f=_imports.print_err):
            for j, u in enumerate(us):
                f((j, u))
                yield u
        us = __()
    us
    if to_show6catch:
        def __(us=us, f=aDetectEasyPrime.is_easy_prime_):
            try:
                for j, u in enumerate(us):
                    if f(u):
                        yield u
            except BaseException as e:
                _imports.print_err((j, u, e))
                raise
        us = __()
    else:
        us = filter(aDetectEasyPrime.is_easy_prime_, us)
    us
    return us
def iter_neg_or_certification4easy_prime__trial_division__fixed_known_primes_(primes_or_spec, us, /):
    'primes_or_spec -> Iter u/pint -> Iter (-u|certification4easy_prime<u>)'
    aDetectEasyPrime = DetectEasyPrime__trial_division__fixed_known_primes(primes_or_spec)
    for u in us:
        check_int_ge(1, u)
        m = aDetectEasyPrime.may_detect_easy_prime_ex_(u, from_factor=False)#not:may_detect_easy_primes_ex_
        if m is None:
            yield -u
        else:
            certification4easy_prime = m
            yield certification4easy_prime
            aDetectEasyPrime.certify_(certification4easy_prime)
__all__
from seed.math.prime_pint.easy_primes import *
