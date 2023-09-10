#__all__:goto
#API:goto
r'''[[[
e ../../python3_src/seed/math/Chinese_Remainder_Theorem.py
view ../../python3_src/nn_ns/math_nn/Chinese_Remainder_Theorem.py


seed.math.Chinese_Remainder_Theorem
py -m nn_ns.app.debug_cmd   seed.math.Chinese_Remainder_Theorem -x
py -m nn_ns.app.doctest_cmd seed.math.Chinese_Remainder_Theorem:__doc__ -ff -v
py_adhoc_call   seed.math.Chinese_Remainder_Theorem   @f

>>> from seed.math.Chinese_Remainder_Theorem import CRT, ECRT, mk_CRT, apply_CRT, apply_CRT__pairs, check_CRT_ans, CRT_Answer_Error
>>> apply_CRT__pairs([(5,1),(3,2)], extended=False)
11
>>> apply_CRT([5,3], [1,2], extended=False)
11
>>> apply_CRT([2*5,3*5], [5,10], extended=False)
Traceback (most recent call last):
    ...
nn_ns.math_nn.Chinese_Remainder_Theorem.CRT_Error__moduli_not_coprime: (10, 15)
>>> apply_CRT([2*5,3*5], [5,10], extended=True)
25
>>> crt = mk_CRT([2*5,3*5], extended=True)
>>> crt([5,10])
25
>>> crt([1,1])
1
>>> crt([1,6])
21
>>> crt([1,11])
11
>>> crt([1,16])
1
>>> crt([1,2]) # %5 inconsistent
Traceback (most recent call last):
    ...
nn_ns.math_nn.Chinese_Remainder_Theorem.CRT_Error__ECRT__remainders_inconsistent: incompatible: (rs[1]%us[1])=(2%15), (rs[0]%us[0])=(1%10): (15%5==0)==0==(10%5==0), (2%5==2)=!=(1%5==1)


#]]]'''
__all__ = r'''
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


'''.split()#'''
__all__
from nn_ns.math_nn.Chinese_Remainder_Theorem import IChinese_Remainder_Theorem, Chinese_Remainder_Theorem, CRT, Extended_Chinese_Remainder_Theorem, ECRT
from nn_ns.math_nn.Chinese_Remainder_Theorem import CRT, ECRT, mk_CRT, apply_CRT, apply_CRT__pairs, check_CRT_ans, CRT_Answer_Error
from nn_ns.math_nn.Chinese_Remainder_Theorem import apply_raw_CRT__inc, prepare4apply_raw_CRT__inc, mk_coeff_pair4apply_raw_CRT__inc, mk_coeff_pairs4apply_raw_CRT__inc, mk_accumulated_partial_moduli4apply_raw_CRT__inc
from nn_ns.math_nn.Chinese_Remainder_Theorem import CRT_Error, CRT_Answer_Error, CRT_Error__ECRT__remainders_inconsistent, CRT_Error__modulus_le_0, CRT_Error__moduli_not_coprime

def __():
    # API:here
    def check_CRT_ans(us, M, rs, ans, /):
        'moduli/[pint] -> whole_modulus/pint -> remainders/[uint%modulus]{len==len(moduli)} -> whole_remainder/uint%whole_modulus -> None'
    class IChinese_Remainder_Theorem:
        def get_whole_modulus(sf, /):
            '-> whole_modulus/pint'
        def get_all_moduli(sf, /):
            '-> moduli/[pint]'
        def __call__(sf, rs, /):
            'remainders/[int] -> whole_remainder/uint%whole_modulus'
        def get_num_moduli(sf, /):
            '-> len(moduli)/uint'
            return len(sf.get_all_moduli())
        def check_CRT_ans(sf, rs, ans, /):
            'remainders/[uint] -> whole_remainder -> None'

    def mk_CRT(us, /, *, extended:bool):
        'moduli/[pint] -> (extended/bool{?allow modulus not coprime?}) -> IChinese_Remainder_Theorem'
    def apply_CRT(us, rs, /, *, extended:bool):
        'moduli/[pint] -> remainders/[uint%modulus]{len==len(moduli)} -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'
    def apply_CRT__pairs(u_r_pairs, /, *, extended:bool):
        'Iter (modulus/pint, remainder/uint%modulus) -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'
    def apply_raw_CRT__inc(us, vs, coeff_pairs, rs, /, *, partial_ok=False):
        r'''[[[
        'moduli/[pint] -> accumulated_partial_moduli/[pint] -> coeff_pairs/[(uint%moduli[i], uint%accumulated_partial_moduli[i])] -> remainders/[uint%moduli[i]] -> whole_remainder/uint%whole_modulus'

        'us/[pint] -> vs/[pint]{.len==1+len(us);.[i]==II(us[:i])} -> coeff_pairs/[(uint%us[i], uint%vs[i])]{.[i]==(vs[i]*inv_mod_(us[i];vs[i]), us[i]*inv_mod_(vs[i];us[i])))} -> remainders/[uint%us[i]]{len==len(us)} -> whole_remainder/uint%vs[-1]'
        #]]]'''#'''
    def mk_coeff_pair4apply_raw_CRT__inc(u, v, /):
        'u -> v -> (coeff4u, coeff4v){coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if [gcd(u,v) =!= 1]'
    def mk_coeff_pairs4apply_raw_CRT__inc(us, vs, /):
        'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])} -> coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'
    def mk_accumulated_partial_moduli4apply_raw_CRT__inc(us, /):
        'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])}'
    def prepare4apply_raw_CRT__inc(us, /):
        'us/[pint] -> (vs/{.len=1+len(us)}{vs[i]==II(us[:i])}, coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)}) |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'

__all__


from seed.math.Chinese_Remainder_Theorem import IChinese_Remainder_Theorem, Chinese_Remainder_Theorem, CRT, Extended_Chinese_Remainder_Theorem, ECRT
from seed.math.Chinese_Remainder_Theorem import CRT, ECRT, mk_CRT, apply_CRT, apply_CRT__pairs, check_CRT_ans, CRT_Answer_Error
from seed.math.Chinese_Remainder_Theorem import apply_raw_CRT__inc, prepare4apply_raw_CRT__inc, mk_coeff_pair4apply_raw_CRT__inc, mk_coeff_pairs4apply_raw_CRT__inc, mk_accumulated_partial_moduli4apply_raw_CRT__inc
from seed.math.Chinese_Remainder_Theorem import CRT_Error, CRT_Answer_Error, CRT_Error__ECRT__remainders_inconsistent, CRT_Error__modulus_le_0, CRT_Error__moduli_not_coprime
from seed.math.Chinese_Remainder_Theorem import *
