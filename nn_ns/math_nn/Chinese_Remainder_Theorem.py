r'''[[[
e ../../python3_src/nn_ns/math_nn/Chinese_Remainder_Theorem.py
nn_ns.math_nn.Chinese_Remainder_Theorem
py -m nn_ns.math_nn.Chinese_Remainder_Theorem
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.Chinese_Remainder_Theorem -x


are_pairwise_coprime(us)
M := II(us)
rs %. us
r := sum rs[i]*(M///us[i])*invmod<%us[i]>(M///us[i]) {i} %M

#]]]'''
__all__ = '''
    CRT_Error
        CRT_Answer_Error
        CRT_Error__ECRT__remainders_inconsistent
        CRT_Error__modulus_le_0
        CRT_Error__moduli_not_coprime


    apply_raw_CRT__inc
        prepare4apply_raw_CRT__inc
            mk_coeff_pair4apply_raw_CRT__inc
            mk_coeff_pairs4apply_raw_CRT__inc
            mk_accumulated_partial_moduli4apply_raw_CRT__inc

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
from seed.math.inv_mod_ import inv_mod_, ginv_mod_respectively_

#from itertools import islice
import operator as opss

class CRT_Error(Exception):pass
class CRT_Answer_Error(CRT_Error):pass
class CRT_Error__ECRT__remainders_inconsistent(CRT_Error):pass
class CRT_Error__modulus_le_0(CRT_Error):pass
class CRT_Error__moduli_not_coprime(CRT_Error):pass

def check_CRT_ans(us, M, rs, ans, /, *, partial_ok=False):
    'moduli/[pint] -> whole_modulus/pint -> remainders/[uint%modulus]{len==len(moduli)} -> whole_remainder/uint%whole_modulus -> None'
    if partial_ok:
        if not len(rs) <= len(us): raise TypeError
    else:
        if not len(rs) == len(us): raise TypeError

    if not 0 <= ans < M: raise CRT_Answer_Error
    if not all((ans-r)%u==0 for r, u in zip(rs, us)): raise CRT_Answer_Error
    return

def apply_raw_CRT__inc(us, vs, coeff_pairs, rs, /, *, partial_ok=False):
    r'''[[[
    'moduli/[pint] -> accumulated_partial_moduli/[pint] -> coeff_pairs/[(uint%moduli[i], uint%accumulated_partial_moduli[i])] -> remainders/[uint%moduli[i]] -> whole_remainder/uint%whole_modulus'

    'us/[pint] -> vs/[pint]{.len==1+len(us);.[i]==II(us[:i])} -> coeff_pairs/[(uint%us[i], uint%vs[i])]{.[i]==(vs[i]*inv_mod_(us[i];vs[i]), us[i]*inv_mod_(vs[i];us[i])))} -> remainders/[uint%us[i]]{len==len(us)} -> whole_remainder/uint%vs[-1]'
    #]]]'''#'''
    rs = mk_tuple(rs)
    if not all(type(r) is int for r in rs): raise TypeError
    if partial_ok:
        if not len(rs) <= len(us): raise TypeError
    else:
        if not len(rs) == len(us): raise TypeError
    if 1:
        if not len(vs) == 1+len(us): raise TypeError
        #if not len(inv_pairs) == len(us): raise TypeError
        if not len(coeff_pairs) == len(us): raise TypeError

    v = 1
    r4v = 0
    for i, rrr in enumerate(rs):
        u = us[i]
        #v = vs[i]
        r4u = rrr %u
        #(inv_u, inv_v) = inv_pairs[i]
        (coeff4u, coeff4v) = coeff_pairs[i]
        uv = vs[i+1]

        r4uv = (r4u*coeff4u + r4v*coeff4v) %uv
        ##########next round:
        v = uv
        r4v = r4uv
    M = v
    ans = r4v
    if 1:
        #M = vs[len(rs)]
        check_CRT_ans(us, M, rs, ans, partial_ok=partial_ok)
    return ans

def mk_coeff_pair4apply_raw_CRT__inc(u, v, /, *, extended):
    'u -> v -> (coeff4u, coeff4v){coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if not [[extended]or[gcd(u,v) == 1]]'
def mk_coeff_pair4apply_raw_CRT__inc(u, v, /):
    'u -> v -> (coeff4u, coeff4v){coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if not [gcd(u,v) == 1]'
    extended = False
    #inv_v = inv_mod_(u, v)
    #inv_u = inv_mod_(v, u)
    (inv_u_g, inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g) = ginv_mod_respectively_(u, v)
    # [inv_u_g*u_g %v_g == 1%v_g]
    # [inv_v_g*v_g %u_g == 1%u_g]
    if not extended:
        if not gcd_of_uv == 1:raise CRT_Error__moduli_not_coprime(u,v)
        # [gcd_of_uv == 1]
        # [inv_u*u %v == 1%v]
        # [inv_v*v %u == 1%u]
    else:
        save = (u, gcd_of_uv, u_g)
        if not gcd_of_uv == 1:
            # [gcd_of_uv =!= 1]
            # [inv_u_g*u_g %v == (1+?*v_g)%v]
            # [inv_v_g*v %u_g == gcd_of_uv%u_g]
            u = u_g
            (inv_u_g, inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g) = ginv_mod_respectively_(u, v)
            if not gcd_of_uv == 1:raise 000

    (inv_u, inv_v) = (inv_u_g, inv_v_g)
    #inv_pairs.append((inv_u, inv_v))
    # [r =[%(u*v)]= r4u*(inv_v*v) + r4v*(inv_u*u)]
    # [r =[%(u*v)]= r4u*coeff4u + r4v*coeff4v]
    # [coeff4u =[%(u*v)]= (inv_v*v)]
    # [coeff4v =[%(u*v)]= (inv_u*u)]
    coeff4u = (inv_v*v)
    coeff4v = (inv_u*u)
    # [0 <= coeff4u < u*v]
    # [0 <= coeff4v < u*v]
    if not extended:
        return (coeff4u, coeff4v)
    else:
        coeff4u_g = coeff4u
        (u, gcd_of_uv, u_g) = save
        return (gcd_of_uv, u_g), (coeff4u_g, coeff4v)

def mk_coeff_pairs4apply_raw_CRT__inc(us, vs, /):
    'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])} -> coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'
    #inv_pairs = []
    coeff_pairs = []
    try:
        for i, u in enumerate(us):
            # II(us[:i]) vs us[i]
            v = II_us_i = vs[i]
            uv = vs[i+1] # == v*u
            (coeff4u, coeff4v) = mk_coeff_pair4apply_raw_CRT__inc(u, v)
                # ^CRT_Error__moduli_not_coprime
            # [0 <= coeff4u < u*v]
            # [0 <= coeff4v < u*v]
            assert 0 <= coeff4u < uv
            assert 0 <= coeff4v < uv
            coeff_pairs.append((coeff4u, coeff4v))
    except CRT_Error__moduli_not_coprime:
        raise CRT_Error__moduli_not_coprime((us, i, u))
    return coeff_pairs
def mk_accumulated_partial_moduli4apply_raw_CRT__inc(us, /):
    'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])}'
    acc = 1
    vs = [1]
    for u in us:
        acc *= u
        vs.append(acc)
    # [vs[i] == II(us[:i])]
    # [vs[-1] == M]
    # [vs[0] == 1]
    #
    return vs
def prepare4apply_raw_CRT__inc(us, /):
    'us/[pint] -> (vs/{.len=1+len(us)}{vs[i]==II(us[:i])}, coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)}) |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'
    vs = mk_accumulated_partial_moduli4apply_raw_CRT__inc(us)
    # [vs[i] == II(us[:i])]
    # [vs[-1] == M]
    # [vs[0] == 1]
    #
    coeff_pairs = mk_coeff_pairs4apply_raw_CRT__inc(us, vs)
    return vs, coeff_pairs



class IChinese_Remainder_Theorem(ABC):
    __slots__ = ()

    @abstractmethod
    def get_whole_modulus(sf, /):
        '-> whole_modulus/pint'
    @abstractmethod
    def get_all_moduli(sf, /):
        '-> moduli/[pint]'
    @abstractmethod
    def __call__(sf, rs, /):
        'remainders/[int] -> whole_remainder/uint%whole_modulus'
    def get_num_moduli(sf, /):
        '-> len(moduli)/uint'
        return len(sf.get_all_moduli())
    def check_CRT_ans(sf, rs, ans, /):
        'remainders/[uint] -> whole_remainder -> None'
        us = sf.get_all_moduli()
        M = sf.get_whole_modulus()
        check_CRT_ans(us, M, rs, ans)



class Chinese_Remainder_Theorem(IChinese_Remainder_Theorem):
    @override
    def get_whole_modulus(sf, /):
        '-> whole_modulus/pint'
        ######################new:
        return sf._vs[-1]
        ######################old:
        return sf._M
    @override
    def get_all_moduli(sf, /):
        '-> moduli/[pint]'
        return sf._us
    def __init__(sf, us, /):
        # if not len(us) > 0: raise TypeError
        #if not len(rs) == len(us): raise TypeError
        #us[:0]#, rs[:0] # be seq
        us = mk_tuple(us)
        if not all(type(u) is int for u in us): raise TypeError
        if not all(u >= 1 for u in us): raise CRT_Error__modulus_le_0(us)

        ######################new:
        vs, coeff_pairs = prepare4apply_raw_CRT__inc(us)
        # [vs[i] == II(us[:i])]
        # [vs[-1] == M]
        # [vs[0] == 1]
        #


        #M = vs.pop()
        vs = tuple(vs)
        #inv_pairs = tuple(inv_pairs)
        coeff_pairs = tuple(coeff_pairs)
        sf._us = us
        sf._vs = vs
        #sf._inv_pairs = inv_pairs
        sf._coeff_pairs = coeff_pairs
        return


        return
        ######################old:
        M = II(us)
        if not are_pairwise_coprime(us, M): raise CRT_Error__moduli_not_coprime(us)

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
        return

    @override
    def __call__(sf, rs, /):
        'remainders/[int] -> whole_remainder/uint%whole_modulus'
        ######################new:
        us = sf._us
        vs = sf._vs
        #inv_pairs = sf._inv_pairs
        coeff_pairs = sf._coeff_pairs
        return apply_raw_CRT__inc(us, vs, coeff_pairs, rs)


        return
        ######################old:
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
        '-> whole_modulus/pint'
        return sf._crt.get_whole_modulus()
    @override
    def get_all_moduli(sf, /):
        '-> moduli/[pint]'
        return sf._us
    def __init__(sf, us, /):
        us = mk_tuple(us)
        if not all(type(u) is int for u in us): raise TypeError
        if not all(u >= 1 for u in us): raise CRT_Error__modulus_le_0(us)

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
        'remainders/[int] -> whole_remainder/uint%whole_modulus'
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
                    raise CRT_Error__ECRT__remainders_inconsistent(f'incompatible: (rs[{i}]%us[{i}])=({ri}%{ui}), (rs[{j}]%us[{j}])=({rj}%{uj}): ({ui}%{g}=={ui%g})==0==({uj}%{g}=={ui%g}), ({ri}%{g}=={ri%g})=!=({rj}%{g}=={rj%g})')
        ans = sf._crt(rs)
            # check_CRT_ans with vs
        sf.check_CRT_ans(rs, ans)
            # check_CRT_ans with us
        return ans
ECRT = Extended_Chinese_Remainder_Theorem





def mk_CRT(us, /, *, extended:bool):
    'moduli/[pint] -> (extended/bool{?allow modulus not coprime?}) -> IChinese_Remainder_Theorem'
    T = ECRT if extended else CRT
    return T(us)

def apply_CRT(us, rs, /, *, extended:bool):
    'moduli/[pint] -> remainders/[uint%modulus]{len==len(moduli)} -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'
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
    'Iter (modulus/pint, remainder/uint%modulus) -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'
    (us, rs) = unzip(2, u_r_pairs)
    return apply_CRT(us, rs, extended=extended)
assert apply_CRT__pairs(zip([5,7,11], [2,4,8]), extended=False) == 382
assert apply_CRT__pairs(zip([4*5,2*3*49,9*7*11], [12,42,105]), extended=True) == 13272


from nn_ns.math_nn.Chinese_Remainder_Theorem import IChinese_Remainder_Theorem, Chinese_Remainder_Theorem, CRT, Extended_Chinese_Remainder_Theorem, ECRT
from nn_ns.math_nn.Chinese_Remainder_Theorem import CRT, ECRT, mk_CRT, apply_CRT, apply_CRT__pairs, check_CRT_ans, CRT_Answer_Error
from nn_ns.math_nn.Chinese_Remainder_Theorem import apply_raw_CRT__inc, prepare4apply_raw_CRT__inc, mk_coeff_pair4apply_raw_CRT__inc, mk_coeff_pairs4apply_raw_CRT__inc, mk_accumulated_partial_moduli4apply_raw_CRT__inc
from nn_ns.math_nn.Chinese_Remainder_Theorem import CRT_Error, CRT_Answer_Error, CRT_Error__ECRT__remainders_inconsistent, CRT_Error__modulus_le_0, CRT_Error__moduli_not_coprime
from nn_ns.math_nn.Chinese_Remainder_Theorem import *
