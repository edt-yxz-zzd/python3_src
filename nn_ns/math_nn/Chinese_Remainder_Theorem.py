r'''[[[
e ../../python3_src/nn_ns/math_nn/Chinese_Remainder_Theorem.py
nn_ns.math_nn.Chinese_Remainder_Theorem
py -m nn_ns.math_nn.Chinese_Remainder_Theorem
from nn_ns.math_nn.Chinese_Remainder_Theorem import IChinese_Remainder_Theorem, Chinese_Remainder_Theorem, CRT, Extended_Chinese_Remainder_Theorem, ECRT
from nn_ns.math_nn.Chinese_Remainder_Theorem import CRT, ECRT, mk_CRT, apply_CRT, apply_CRT__pairs, check_CRT_ans, CRT_Answer_Error

are_pairwise_coprime(us)
M := II(us)
rs %. us
r := sum rs[i]*(M///us[i])*invmod<%us[i]>(M///us[i]) {i} %M

#]]]'''
__all__ = '''
    check_CRT_ans
        CRT_Answer_Error
    IChinese_Remainder_Theorem
        Chinese_Remainder_Theorem
            CRT

        Extended_Chinese_Remainder_Theorem
            ECRT

    apply_CRT
        mk_CRT
        apply_CRT__pairs

    '''.split()

from seed.math.II import II
from seed.math.gcd import gcd
from seed.math.lcm import lcm_many
from seed.math.are_pairwise_coprime import are_pairwise_coprime
from seed.math.lcm_parts_of import lcm_parts_of
from seed.iters.unzip import unzip
from seed.tiny import mk_tuple
from seed.abc.abc__ver0 import ABC, abstractmethod, override

#from nn_ns.math_nn.integer.mod import invmod
from seed.math.inv_mod_ import inv_mod_

#from itertools import islice
import operator as opss

class CRT_Answer_Error(Exception):pass

def check_CRT_ans(us, M, rs, ans, /):
    if not len(rs) == len(us): raise TypeError
    if not 0 <= ans < M: raise CRT_Answer_Error
    if not all((ans-r)%u==0 for r, u in zip(rs, us)): raise CRT_Answer_Error
    return
class IChinese_Remainder_Theorem(ABC):
    __slots__ = ()

    @abstractmethod
    def get_whole_modulus(sf, /):
        '-> pint'
    @abstractmethod
    def get_all_moduli(sf, /):
        '-> [pint]'
    @abstractmethod
    def __call__(sf, rs, /):
        '[int] -> uint%sf.get_whole_modulus()'
    def get_num_moduli(sf, /):
        return len(sf.get_all_moduli())
    def check_CRT_ans(sf, rs, ans, /):
        us = sf.get_all_moduli()
        M = sf.get_whole_modulus()
        check_CRT_ans(us, M, rs, ans)
class Chinese_Remainder_Theorem(IChinese_Remainder_Theorem):
    @override
    def get_whole_modulus(sf, /):
        return sf._M
    @override
    def get_all_moduli(sf, /):
        return sf._us
    def __init__(sf, us, /):
        # if not len(us) > 0: raise TypeError
        #if not len(rs) == len(us): raise TypeError
        #us[:0]#, rs[:0] # be seq
        us = mk_tuple(us)
        if not all(type(u) is int for u in us): raise TypeError
        if not all(u >= 1 for u in us): raise ValueError

        M = II(us)
        if not are_pairwise_coprime(us, M): raise ValueError

        #if M == 1: return 0
        #if not M >= 2: raise logic-err
        Mus = tuple(M//u for u in us)
        #bug:[when u==1]:invs = tuple(invmod(M_u, u) for u, M_u in zip(us, Mus))
        invs = tuple(inv_mod_(u, M_u) for u, M_u in zip(us, Mus))
        coeffs = tuple((M_u*inv_M_u) for inv_M_u, M_u in zip(invs, Mus))
        if not max(coeffs, default=0) < M: raise logic-err
        sf._us = us
        sf._M = M
        sf._Mus = Mus
        sf._invs = invs
        sf._coeffs = coeffs

    @override
    def __call__(sf, rs, /):
        rs = mk_tuple(rs)
        if not all(type(r) is int for r in rs): raise TypeError
        if not len(rs) == sf.get_num_moduli(): raise TypeError

        coeffs = sf._coeffs
        M = sf.get_whole_modulus()
        ans = sum(map(opss.__mul__, coeffs, rs))%M
        sf.check_CRT_ans(rs, ans)
        return ans
CRT = Chinese_Remainder_Theorem


class Extended_Chinese_Remainder_Theorem(IChinese_Remainder_Theorem):
    @override
    def get_whole_modulus(sf, /):
        return sf._crt.get_whole_modulus()
    @override
    def get_all_moduli(sf, /):
        return sf._us
    def __init__(sf, us, /):
        us = mk_tuple(us)
        if not all(type(u) is int for u in us): raise TypeError
        if not all(u >= 1 for u in us): raise ValueError

        vs = []
        for u in us:
            for i in range(len(vs)):
                v = vs[i]
                (v_, g, u_) = lcm_parts_of(v, u)
                v = vs[i] = v_*g
                u = u_
            vs.append(u)
        vs = tuple(vs)
        assert len(vs) == len(us)
        crt = Chinese_Remainder_Theorem(vs)
        assert vs is crt.get_all_moduli()
        M = lcm_many(us)
        if not M == crt.get_whole_modulus(): raise logic-err

        L = len(us)
        i__j_g_pairs__pairs = []
        for i, v in enumerate(vs):
            u_v = us[i]
            miss = u_v//v
            assert miss*v == u_v
            j_g_pairs = []
            m = miss
            for j, w in enumerate(vs):
                if i==j: continue
                g = gcd(m, w)
                if g==1: continue
                m //= g
                j_g_pairs.append((j, g))
            if j_g_pairs:
                i__j_g_pairs__pairs.append((i, tuple(j_g_pairs)))
        i__j_g_pairs__pairs = tuple(i__j_g_pairs__pairs)
        sf._us = us
        #sf._vs = vs
        sf._crt = crt
        sf._i_j_g_ps_ps = i__j_g_pairs__pairs

    @override
    def __call__(sf, rs, /):
        rs = mk_tuple(rs)
        if not all(type(r) is int for r in rs): raise TypeError
        if not len(rs) == sf.get_num_moduli(): raise TypeError

        #compatible??
        i__j_g_pairs__pairs = sf._i_j_g_ps_ps
        for i, j_g_pairs in i__j_g_pairs__pairs:
            ri = rs[i]
            for j, g in j_g_pairs:
                rj = rs[j]
                if not ri%g == rj%g:
                    us = sf.get_all_moduli()
                    ui = us[i]
                    uj = us[j]
                    assert ui%g == 0
                    assert uj%g == 0
                    raise ValueError(f'incompatible: (rs[{i}]%us[{i}])=({ri}%{ui}), (rs[{j}]%us[{j}])=({rj}%{uj}): ({ui}%{g}=={ui%g})==0==({uj}%{g}=={ui%g}), ({ri}%{g}=={ri%g})=!=({rj}%{g}=={rj%g})')
        ans = sf._crt(rs)
            # check_CRT_ans with vs
        sf.check_CRT_ans(rs, ans)
            # check_CRT_ans with us
        return ans
ECRT = Extended_Chinese_Remainder_Theorem





def mk_CRT(us, /, *, extended:bool):
    T = ECRT if extended else CRT
    return T(us)

def apply_CRT(us, rs, /, *, extended:bool):
    return mk_CRT(us, extended=extended)(rs)


assert apply_CRT([], [], extended=False) == 0
assert apply_CRT([1], [3], extended=False) == 0
assert apply_CRT([5], [7], extended=False) == 2
assert apply_CRT([1, 5,7], [3,7,7], extended=False) == 7
#print(apply_CRT([5,7,11], [2,4,8], extended=False))
assert apply_CRT([5,7,11], [2,4,8], extended=False) == 382

assert apply_CRT([], [], extended=True) == 0
assert apply_CRT([1], [3], extended=True) == 0
assert apply_CRT([5], [7], extended=True) == 2
assert apply_CRT([1, 4*5,2*7], [3,7,7], extended=True) == 7
#print(apply_CRT([4*5,2*3*49,9*7*11], [12,42,105], extended=True))
assert apply_CRT([4*5,2*3*49,9*7*11], [12,42,105], extended=True) == 13272

def apply_CRT__pairs(u_r_pairs, /, *, extended:bool):
    (us, rs) = unzip(2, u_r_pairs)
    return apply_CRT(us, rs, extended=extended)
assert apply_CRT__pairs(zip([5,7,11], [2,4,8]), extended=False) == 382
assert apply_CRT__pairs(zip([4*5,2*3*49,9*7*11], [12,42,105]), extended=True) == 13272


