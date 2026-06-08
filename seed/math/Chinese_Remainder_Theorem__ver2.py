#__all__:goto
r'''[[[
e ../../python3_src/seed/math/Chinese_Remainder_Theorem__ver2.py

seed.math.Chinese_Remainder_Theorem__ver2
py -m nn_ns.app.debug_cmd   seed.math.Chinese_Remainder_Theorem__ver2 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.Chinese_Remainder_Theorem__ver2:__doc__ -ht # -ff -df
#######

[[
used by:
view ../../python3_src/seed/math/factor_pint/perfect_power/detect_perfect_power.py
]]
[[
[M:=II(moduli)][L:=len(moduli)]:
    ########
    #both precomputation&&reconstruction:
    #both stepwise&&blockwise
    slow.__mul__ => O(lnM**2)

    ########
    #stepwise{both precomputation&&reconstruction}:
    #precomputation{both stepwise&&blockwise}:
    fast.__mul__ => O(L*lnM*lnlnM*lnlnlnM)

    ########
    #reconstruction{blockwise}:
    fast.__mul__ => O(lnL*lnM*lnlnM*lnlnlnM)

]]
[[
page88[102/604] Algorithm__2_1_7
    stepwise M_0j*Mj
    -->:
        ver0:using list
        ver1:using finger_tree-Seq
page508[517/604] Algorithm__9_5_26
    blockwise M_ij
    [using fast multiplication][precomputation done]:
        [L:=len(moduli)]
        [M:=II(moduli)] # M_0L
        [TIME == O(lnL*lnM*lnlnM*lnlnlnM)]

    old ver:the book ver:
        deleted:
            !! precomputation has some useless steps
            !! hard to fit non-zpow
    -->:
        new ver1:rvheap-style
        new ver2:padded_infix_heap-style
]]



'#'; __doc__ = r'#'
>>> crt_data7precomputation = crt_precomputation7coprime7blockwise_([])

old:
Traceback (most recent call last):
    ...
seed.math.Chinese_Remainder_Theorem__ver2.CRT_Error__moduli_empty
>>> crt_data7precomputation
((), (), (), ())

>>> crt_data7precomputation = crt_precomputation7coprime7blockwise_([0])
Traceback (most recent call last):
    ...
seed.math.Chinese_Remainder_Theorem__ver2.CRT_Error__modulus_le_0: 0
>>> crt_data7precomputation = crt_precomputation7coprime7blockwise_([4,6])
Traceback (most recent call last):
    ...
seed.math.Chinese_Remainder_Theorem__ver2.CRT_Error__moduli_not_coprime: (4, 6)
>>> crt_data7precomputation = crt_precomputation7coprime7blockwise_([1])
>>> crt_reconstruction7coprime7blockwise_(crt_data7precomputation, [])
Traceback (most recent call last):
    ...
seed.math.Chinese_Remainder_Theorem__ver2.CRT_Error__len4remainders: (0, 1)
>>> crt_reconstruction7coprime7blockwise_(crt_data7precomputation, [1,2])
Traceback (most recent call last):
    ...
seed.math.Chinese_Remainder_Theorem__ver2.CRT_Error__len4remainders: (2, 1)
>>> crt_reconstruction7coprime7blockwise_(crt_data7precomputation, [999], validate=True)
0
>>> crt_data7precomputation
((1,), (1,), (0,), (1,))

old:
((1,), (1,), (0,), ((1,),))

>>> apply_CRT([1], [999], extended=False, validate=True)
0
>>> apply_CRT__pairs([(1, 999)], extended=False, validate=True)
0




>>> from seed.debug.show_name_value_pairs_ import show_name_value_pairs_, parse_xnms_
>>> xnms = parse_xnms_('(j2Mj, j2Wj, j2Vj, e2i2M_i_ize)')
>>> xnms = parse_xnms_('(j2Mj, j2Wj, j2Vj, rvheap8vj2M6vj)')
>>> crt_data7precomputation = crt_precomputation7coprime7blockwise_(moduli:=(3,5,7,11,13,17,19,23))
>>> show_name_value_pairs_(xnms, crt_data7precomputation)
j2Mj=(3, 5, 7, 11, 13, 17, 19, 23)
j2Wj=(37182145, 22309287, 15935205, 10140585, 8580495, 6561555, 5870865, 4849845)
j2Vj=(1, -2, -1, 3, 1, -6, 9, -6)
rvheap8vj2M6vj=(3, 5, 7, 11, 13, 17, 19, 23, 15, 77, 221, 437, 1155, 96577, 111546435)

#old:
j2Mj=(3, 5, 7, 11, 13, 17, 19, 23)
j2Wj=(37182145, 22309287, 15935205, 10140585, 8580495, 6561555, 5870865, 4849845)
j2Vj=(1, -2, -1, 3, 1, -6, 9, -6)
e2i2M_i_ize=((3, 5, 7, 11, 13, 17, 19, 23), (15, 35, 77, 143, 221, 323, 437), (1155, 5005, 17017, 46189, 96577), (111546435,))

>>> crt_reconstruction7coprime7blockwise_(crt_data7precomputation, residues:=(1,1,1,1,3,3,3,3), validate=True)
97446196

# test@[len(moduli) is not zpow]
>>> apply_CRT(moduli[:-1], residues[:-1], extended=False, validate=True)
449296
>>> apply_CRT(moduli[:-2], residues[:-2], extended=False, validate=True)
194041
>>> apply_CRT(moduli[:-3], residues[:-3], extended=False, validate=True)
13861
>>> apply_CRT(moduli[:-4], residues[:-4], extended=False, validate=True)
1
>>> apply_CRT(moduli[:-5], residues[:-5], extended=False, validate=True)
1
>>> apply_CRT(moduli[:-6], residues[:-6], extended=False, validate=True)
1
>>> apply_CRT(moduli[:-7], residues[:-7], extended=False, validate=True)
1



>>> crt = CRT7coprime7blockwise(moduli)
>>> crt
CRT7coprime7blockwise((3, 5, 7, 11, 13, 17, 19, 23))
>>> crt(residues)
97446196
>>> crt(residues, validate=True)
97446196
>>> crt == CRT7coprime7blockwise(moduli)
True
>>> crt == CRT7coprime7blockwise(moduli[:-1])
False
>>> crt in {crt}
True
>>> j=-1;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
449296
>>> j=-2;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
194041
>>> j=-3;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
13861
>>> j=-4;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
1
>>> j=-6;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
1
>>> j=-6;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
1
>>> j=-7;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
1
>>> j=-8;CRT7coprime7blockwise(moduli[:j])(residues[:j], validate=True)
0




>>> crt = CRT7coprime7stepwise(moduli)
>>> crt
CRT7coprime7stepwise((3, 5, 7, 11, 13, 17, 19, 23))
>>> crt(residues)
97446196
>>> crt(residues, validate=True)
97446196
>>> crt == CRT7coprime7stepwise(moduli)
True
>>> crt == CRT7coprime7stepwise(moduli[:-1])
False
>>> crt in {crt}
True
>>> crt(residues[:-1], validate=True)
Traceback (most recent call last):
    ...
seed.math.Chinese_Remainder_Theorem__ver2.CRT_Error__len4remainders: (7, 8)
>>> crt(residues[:-1], validate=True, partial_ok=True)
449296
>>> crt(residues[:-2], validate=True, partial_ok=True)
194041
>>> crt(residues[:-3], validate=True, partial_ok=True)
13861
>>> crt(residues[:-4], validate=True, partial_ok=True)
1
>>> crt(residues[:-5], validate=True, partial_ok=True)
1
>>> crt(residues[:-6], validate=True, partial_ok=True)
1
>>> crt(residues[:-7], validate=True, partial_ok=True)
1
>>> crt(residues[:-8], validate=True, partial_ok=True)
0



>>> get_CRT_type_(ver='incremental') is CRT7coprime7stepwise
True
>>> get_CRT_type_(ver='stepwise') is CRT7coprime7stepwise
True
>>> get_CRT_type_(ver='blockwise') is CRT7coprime7blockwise
True
>>> get_CRT_type_(ver='long_term') is CRT7coprime7blockwise
True





iextend_
>>> CRT7coprime7stepwise(moduli[:0], incremental=True)
CRT7coprime7stepwise(Seq())
>>> crt0 = CRT7coprime7stepwise(moduli[:0])
>>> crt5 = crt0.iextend_(moduli[0:5])
>>> crt6 = crt5.iextend_(moduli[5:6])
>>> crt7 = crt6.iextend_(moduli[6:7])
>>> crt0
CRT7coprime7stepwise(())
>>> crt5
CRT7coprime7stepwise(Seq([3, 5, 7, 11, 13]))
>>> crt6
CRT7coprime7stepwise(Seq([3, 5, 7, 11, 13, 17]))
>>> crt7
CRT7coprime7stepwise(Seq([3, 5, 7, 11, 13, 17, 19]))
>>> crt0(residues[:0])
0
>>> crt5(residues[:5])
13861
>>> crt6(residues[:6])
194041
>>> crt7(residues[:7])
449296


py_adhoc_call   seed.math.Chinese_Remainder_Theorem__ver2   @f
]]]'''#'''
__all__ = r'''
get_CRT_type_
apply_CRT
apply_CRT__pairs

CRT7coprime7blockwise
    crt_precomputation7coprime7blockwise_
    crt_reconstruction7coprime7blockwise_

CRT7coprime7stepwise
    crt_precomputation7coprime7stepwise_
    crt_reconstruction7coprime7stepwise_



check_CRT_ans
CRT_Error
    CRT_Error__moduli_empty
    CRT_Error__modulus_le_0
    CRT_Error__moduli_not_coprime
    CRT_Error__len4remainders
    CRT_Answer_Error


hrem_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.tiny_.containers import mk_tuple
    from seed.math.II import II
    from seed.math.inv_mod__py_ import inv_mod__py_
    from seed.seq_tools.split_tuples import unzip_pairs
    #from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.data_funcs.heap.heap_shape import mk_rvheap__fill_# mk_rvheap__Nothing_

    from seed.helper.repr_input import repr_helper
    from seed.data_funcs.finger_tree.ft23_7sized_seq import Seq
#.    from itertools import islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def hrem_(M, x, /):
    H = M//2
    if not abs(x) <= H:
        x %= M
        if x > H:
            x -= M
    assert abs(x) <= H
    if M&1 == 0 and x == -H:
        x = H
    return x



def _std_Ms(moduli7pairwise_coprime, /, *, moduli_empty_ok=False):
    j2Mj = moduli = mk_tuple(moduli7pairwise_coprime)
    if not (moduli_empty_ok or moduli):raise CRT_Error__moduli_empty#TypeError
    for Mj in moduli:
        #check_int_ge(1, Mj)
        check_type_is(int, Mj)
        if Mj <= 0:raise CRT_Error__modulus_le_0(Mj)
    return moduli

def _std_Rs(j2Mj, residues, /, *, partial_ok=False):
    L = len(j2Mj)
    residues = mk_tuple(residues)
    if not partial_ok:
        if not len(residues) == L:raise CRT_Error__len4remainders(len(residues), L)
    else:
        if not len(residues) <= L:raise CRT_Error__len4remainders(len(residues), L)
    for Rj in residues:
        check_type_is(int, Rj)
    j2Rj = [*map(hrem_, j2Mj, residues)]
        # residues keep unchanged for validate
    return (residues, j2Rj)

if 0:
    _prev_data7stepwise = ...
def _gmk_prev_data7stepwise_():
    global _prev_data7stepwise
    try:
        return _prev_data7stepwise
    except NameError:
        pass
    _prev_data7stepwise = (Seq(),)*3
    return _gmk_prev_data7stepwise_()
def crt_precomputation7coprime7stepwise_(moduli7pairwise_coprime, /, *, incremental=None):
    r'''[[[
    [M:=II(moduli)][L:=len(moduli)]:
        fast.__mul__ => O(L*lnM*lnlnM*lnlnlnM)
        slow.__mul__ => O(lnM**2)
    #]]]'''#'''
    j2Mj = moduli = _std_Ms(moduli7pairwise_coprime, moduli_empty_ok=True)
    L = len(moduli)
    ########
    if incremental:
        prev_data = _gmk_prev_data7stepwise_() if incremental is True else incremental
        incremental = True
        (j2Mj_, j2M_0jpp, j2V_0j) = prev_data
        j = len(j2Mj_)
        M_0j = j2M_0jpp[j-1] if j else 1
        j2Mj_ = Seq(j2Mj_)
        j2M_0jpp = Seq(j2M_0jpp)
        j2V_0j = Seq(j2V_0j)
    else:
        j = 0
        M_0j = 1 # partial_modulus
        j2M_0jpp = []
        j2V_0j = []
    ########
    for Mj in moduli:
        # [M_0j == II(moduli[0:j])]
        # [Mj == moduli[j]]
        M_0jpp = M_0j*Mj
        # [M_0jpp == II(moduli[0:1+j])]
            # O(TIME{__mul__(M_0j,Mj)})
        V_0j = inv_mod__py_(Mj, M_0j)
        # [V_0j == (II(moduli[0:j])%moduli[j])]
            # O(TIME{__mul__(M_0j,Mj)})
        if incremental:
            j2Mj_ = j2Mj_.ipushR(Mj)
            j2M_0jpp = j2M_0jpp.ipushR(M_0jpp)
            j2V_0j = j2V_0j.ipushR(V_0j)
        else:
            j2M_0jpp.append(M_0jpp)
            j2V_0j.append(V_0j)
        ####
        j += 1
        M_0j = M_0jpp
        ####
    # O(sum[TIME{__mul__(M_0j,Mj)} | [j:<-[0..<L]]])
    # O(L*TIME{__mul__(M_0L,max(moduli))})
    # * O(L*TIME{fast.__mul__(M_0L,M_0L)})
    #   O(L*lnM*lnlnM*lnlnlnM)
    # * O(L*TIME{slow.__mul__(M_0L,max(moduli))})
    #   O(L*lnM*ln(max(moduli)))
    #   O(lnM**2)
    j2M_0jpp
    j2V_0j
    ####
    if incremental:
        j2Mj = j2Mj_
    else:
        j2Mj = mk_tuple(j2Mj)
        j2M_0jpp = mk_tuple(j2M_0jpp)
        j2V_0j = mk_tuple(j2V_0j)
    ####
    crt_data7precomputation = (j2Mj, j2M_0jpp, j2V_0j)
    return crt_data7precomputation

def crt_reconstruction7coprime7stepwise_(crt_data7precomputation, residues, /, *, validate=False, partial_ok=False):
    r'''[[[
    [M:=II(moduli)][L:=len(moduli)]:
        fast.__mul__ => O(L*lnM*lnlnM*lnlnlnM)
        slow.__mul__ => O(lnM**2)
    #]]]'''#'''
    (j2Mj, j2M_0jpp, j2V_0j) = crt_data7precomputation
    (residues, j2Rj) = _std_Rs(j2Mj, residues, partial_ok=partial_ok)
    #partial_ok! #L = len(j2Mj)
    L = len(j2Rj)
    j = 0
    M_0j = 1 # partial_modulus
    R_0j = 0 # partial_residue
    it = zip(j2Mj, j2Rj, j2V_0j, j2M_0jpp)
    while not j == L:
        M_0j
        R_0j
        ####
        #Mj = j2Mj[j]
        #Rj = j2Rj[j]
        #V_0j = j2V_0j[j]
        #M_0jpp = j2M_0jpp[j]
        (Mj, Rj, V_0j, M_0jpp) = next(it, None)
        ####
        R_0jpp = _crt_step_(M_0j, Mj, M_0jpp, V_0j, R_0j, Rj)
            # O(TIME{__mul__(M_0j,Mj)})
        ####
        j += 1
        M_0j = M_0jpp
        R_0j = R_0jpp
        ####
    # O(sum[TIME{__mul__(M_0j,Mj)} | [j:<-[0..<L]]])
    # O(L*TIME{__mul__(M_0L,max(moduli))})
    # * O(L*TIME{fast.__mul__(M_0L,M_0L)})
    #   O(L*lnM*lnlnM*lnlnlnM)
    # * O(L*TIME{slow.__mul__(M_0L,max(moduli))})
    #   O(L*lnM*ln(max(moduli)))
    #   O(lnM**2)
    M_0j
    R_0j
    # [j == L]
    M_0L = M_0j
    R_0L = R_0j
    #######
    N_0L = R_0L%M_0L
    #######
    if validate:
        check_CRT_ans(j2Mj, M_0L, residues, N_0L, partial_ok=partial_ok)
    return N_0L

def _crt_step_(M_0j, Mj, M_0jpp, V_0j, R_0j, Rj, /):
    # O(TIME{__mul__(M_0j,Mj)})
    r'''[[[
    [M_0jpp == M_0j*Mj]
    [M_0j*V_0j =[%Mj]= 1]
    [R_0jpp =[%M_0j]= R_0j]
    [R_0jpp =[%Mj]= Rj]

    [x*M_0j*V_0j =[%M_0j]= 0]
    [x*M_0j*V_0j =[%Mj]= x]

    [y +x*M_0j*V_0j =[%M_0j]= y +0 == R_0j]
    [y +x*M_0j*V_0j =[%Mj]= y +x == Rj]
    [y == R_0j]
    [x == (Rj -R_0j)]

    [R_0jpp =[%(M_0j*Mj)]= y +x*M_0j*V_0j == R_0j +(Rj -R_0j)*M_0j*V_0j]
    [R_0jpp =[%(M_0j*Mj)]= (Rj -R_0j)*V_0j*M_0j%(M_0j*Mj) +R_0j]
    [R_0jpp =[%M_0jpp]= (Rj -R_0j%Mj)*V_0j%Mj *M_0j +R_0j]
    #]]]'''#'''

    R_0jpp = hrem_(M_0jpp, R_0j +M_0j*hrem_(Mj, V_0j*hrem_(Mj, Rj -hrem_(Mj, R_0j))))
        # O(TIME{__mul__(M_0j,Mj)})
    return R_0jpp


















def crt_precomputation7coprime7blockwise_(moduli7pairwise_coprime, /):
    r'''[[[
    [M:=II(moduli)][L:=len(moduli)]:
        slow.__mul__ => O(lnM**2)
        fast.__mul__ => O(L*lnM*lnlnM*lnlnlnM)
    #]]]'''#'''

    moduli = _std_Ms(moduli7pairwise_coprime, moduli_empty_ok=True)
    crt_data7precomputation = _crt_precomputation7coprime7blockwise__Lge1_(moduli) if moduli else _4Leq0
    return crt_data7precomputation
if 1:
    _4Leq0 = ((),)*4

def _crt_precomputation7coprime7blockwise__Lge1_(moduli, /):
    assert moduli


    r'''[[[
    rvheap8vj2M6vj = mk_rvheap__Nothing_(None, moduli)
    sz = len(rvheap8vj2M6vj)

    assert sz&1 #odd
    for vj in range(sz, 2, -2):
        # [vj%2 == 1]
        # [sz >= vj > 2]
        vi = vj -1
        # [sz > vi >= 2]
        vparent = vi >> 1
        # [sz > vi > vparent >= 1]
        M6vj = rvheap8vj2M6vj[-vj]
        M6vi = rvheap8vj2M6vj[-vi]
        M6vparent = M6vj * M6vi
        rvheap8vj2M6vj[-vparent] = M6vparent
    rvheap8vj2M6vj
    #]]]'''#'''
    r'''[[[
    def parent5children_(M6vj, M6vi, /):
        M6vparent = M6vj * M6vi
        return M6vparent
    rvheap8vj2M6vj = mk_rvheap__fill_(parent5children_, moduli)
    #]]]'''#'''
    rvheap8vj2M6vj = mk_rvheap__fill_(int.__mul__, moduli)
        # O(sum[TIME{__mul__(M_i_izemm,M_izemm_ize)} | [j:<-[0..<log2(L)]][zemm:=2**j][ze:=2*zemm][i:<-[0,ze..<L]]])
        # O(sum[L/ze*TIME{__mul__(M_i_izemm,M_izemm_ize)} | [j:<-[0..<log2(L)]][zemm:=2**j][ze:=2*zemm][i:=0]])
        # O(sum[(L/2/zemm)*TIME{__mul__(M**/(L/zemm),M**/(L/zemm))} | [j:<-[0..<log2(L)]][zemm:=2**j]])
        #######
        # slow.__mul__ => O(TIME{__mul__(M**/2,M**/2)})
        # slow.__mul__ => O(TIME{__mul__(M,M)})
        # slow.__mul__ => O(lnM**2)
        #######
        # fast.__mul__ => O(sum[(L/2/zemm)*(lnM/(L/zemm))*ln(lnM/(L/zemm))*lnln(lnM/(L/zemm)) | [j:<-[0..<log2(L)]][zemm:=2**j]])
        # fast.__mul__ => O(sum[(Lz/2)*(lnM/Lz)*ln(lnM/Lz)*lnln(lnM/Lz) | [j:<-[0..<log2(L)]][Lz:=2**j]])
        # fast.__mul__ => O(sum[lnM*lnlnM*lnlnlnM | [j:<-[0..<log2(L)]][Lz:=2**j]])
        # fast.__mul__ => O(lnL*lnM*lnlnM*lnlnlnM) #but be overvomed below
        #######
    #######
    #######
    #######
    M = M_0L = rvheap8vj2M6vj[-1] # II(moduli)
    j2Mj = moduli
    j2Wj = [M//Mj for Mj in moduli]
        # O(L*TIME{__mul__(M_0L,Mj)})
    try:
        j2Vj = [*map(hrem_, j2Mj, map(inv_mod__py_, j2Mj, j2Wj))]
        # O(L*TIME{__mul__(M_0L/Mj,Mj)})
    except ValueError:
        raise CRT_Error__moduli_not_coprime(moduli)
    j2Vj
    j2Wj
        # O(L*TIME{__mul__(M_0L,Mj)})
        #######
        # slow.__mul__ => O(lnM**2)
        #######
        # fast.__mul__ => O(L*lnM*lnlnM*lnlnlnM)
        #######
    #######
    #######
    #######
    j2Mj = mk_tuple(j2Mj)
    j2Wj = mk_tuple(j2Wj)
    j2Vj = mk_tuple(j2Vj)
    rvheap8vj2M6vj = mk_tuple(rvheap8vj2M6vj)
    #######
    crt_data7precomputation = (j2Mj, j2Wj, j2Vj, rvheap8vj2M6vj)
    return crt_data7precomputation

def crt_reconstruction7coprime7blockwise_(crt_data7precomputation, residues, /, *, validate=False):
    r'''[[[
    [M:=II(moduli)][L:=len(moduli)]:
        slow.__mul__ => O(lnM**2)
        fast.__mul__ => O(lnL*lnM*lnlnM*lnlnlnM)
    #]]]'''#'''
    #(j2Mj, j2Wj, j2Vj, e2i2M_i_ize) = crt_data7precomputation
    (j2Mj, j2Wj, j2Vj, rvheap8vj2M6vj) = crt_data7precomputation
    (residues, j2Rj) = _std_Rs(j2Mj, residues)

    r'''[[[
    sz = len(rvheap8vj2M6vj)
    rvheap8vj2R6vj = [Vj*Rj for Vj, Rj in zip(j2Vj, j2Rj)]
    rvheap8vj2R6vj += [None]*(sz -len(rvheap8vj2R6vj))
    assert sz == len(rvheap8vj2R6vj)

    assert not sz or sz&1 #0 or odd
    for vj in range(sz, 2, -2):
        # [vj%2 == 1]
        # [sz >= vj > 2]
        vi = vj -1
        # [sz > vi >= 2]
        vparent = vi >> 1
        # [sz > vi > vparent >= 1]
        M6vj = rvheap8vj2M6vj[-vj]
        M6vi = rvheap8vj2M6vj[-vi]
        M6vparent = rvheap8vj2M6vj[-vparent]

        R6vj = rvheap8vj2R6vj[-vj]
        R6vi = rvheap8vj2R6vj[-vi]
        R6vparent = M6vj * R6vi + R6vj * M6vi
        777;R6vparent = hrem_(M6vparent, R6vparent)
        rvheap8vj2R6vj[-vparent] = R6vparent
    rvheap8vj2R6vj
    #]]]'''#'''

    sz = len(rvheap8vj2M6vj)
    rvheap8vj2R6vj = [Vj*Rj for Vj, Rj in zip(j2Vj, j2Rj)]
    def parent5children_(vidc, R6vj, R6vi, /):
        (vj, vi, vparent) = vidc
        M6vj = rvheap8vj2M6vj[-vj]
        M6vi = rvheap8vj2M6vj[-vi]
        M6vparent = rvheap8vj2M6vj[-vparent]
        #R6vj = rvheap8vj2R6vj[-vj]
        #R6vi = rvheap8vj2R6vj[-vi]
        R6vparent = M6vj * R6vi + R6vj * M6vi
        777;R6vparent = hrem_(M6vparent, R6vparent)
            # O(TIME{__mul__(M_i_izemm,M_izemm_ize)})
        return R6vparent
    #bug:rvheap8vj2R6vj = mk_rvheap__fill_(parent5children_, j2Rj, with_bwd_idc=True)
    mk_rvheap__fill_(parent5children_, rvheap8vj2R6vj, inplace=True, with_bwd_idc=True)
        # O(sum[TIME{__mul__(M_i_izemm,M_izemm_ize)} | [j:<-[0..<log2(L)]][zemm:=2**j][ze:=2*zemm][i:<-[0,ze..<L]]])
        # same as crt_precomputation7coprime7blockwise_::mk_rvheap__fill_
        #######
        # slow.__mul__ => O(lnM**2)
        # fast.__mul__ => O(lnL*lnM*lnlnM*lnlnlnM)
        #######

    #######
    sz = len(rvheap8vj2M6vj)
    assert sz == len(rvheap8vj2R6vj)
    #######
    if sz:
        M_0L = rvheap8vj2M6vj[-1]
        R_0L = rvheap8vj2R6vj[-1]
        N_0L = R_0L %M_0L
    else:
        M_0L = 1
        R_0L = 0
        N_0L = 0
    #######
    if validate:
        check_CRT_ans(j2Mj, M_0L, residues, N_0L)
    return N_0L




class _IBaseCRT7coprime7XXX:
    @classmethod
    def _crt_precomputation7coprime7XXX_(cls, moduli7pairwise_coprime, /, **kwds4precomputation):
        raise NotImplementedError
    @classmethod
    def _crt_reconstruction7coprime7XXX_(cls, crt_data7precomputation, residues, /, **kwds4reconstruction):
        raise NotImplementedError
    def __init__(sf, moduli7pairwise_coprime, /, precomputed=False, **kwds4precomputation):
        if precomputed:
            crt_data7precomputation = moduli7pairwise_coprime
        else:
            cls = type(sf)
            crt_data7precomputation = cls._crt_precomputation7coprime7XXX_(moduli7pairwise_coprime, **kwds4precomputation)
        sf._dat = crt_data7precomputation
    @property
    def crt_data7precomputation(sf, /):
        return sf._dat
    @property
    def moduli(sf, /):
        return sf._dat[0]
    def __repr__(sf, /):
        return repr_helper(sf, sf.moduli)
    def __hash__(sf, /):
        return hash((__class__, sf.moduli))
    def __eq__(sf, ot, /):
        if not isinstance(ot, __class__):return NotImplemented
        return sf.moduli == ot.moduli
    def __call__(sf, residues, /, **kwds4reconstruction):
        cls = type(sf)
        return cls._crt_reconstruction7coprime7XXX_(sf.crt_data7precomputation, residues, **kwds4reconstruction)
class _IBaseCRT7coprime7XXX7incremental(_IBaseCRT7coprime7XXX):
    def mk5crt_data7precomputation_(sf, crt_data7precomputation, /):
        cls = type(sf)
        return cls(crt_data7precomputation, precomputed=True)
    def iextend_(sf, more_moduli7pairwise_coprime, /, **kwds4precomputation):
        cls = type(sf)
        crt_data7precomputation = cls._crt_precomputation7coprime7XXX_(more_moduli7pairwise_coprime, incremental=sf.crt_data7precomputation, **kwds4precomputation)
        return sf.mk5crt_data7precomputation_(crt_data7precomputation)

class CRT7coprime7stepwise(_IBaseCRT7coprime7XXX7incremental):
    r'''[[[
    [M:=II(moduli)][L:=len(moduli)]:
        #both precomputation&&reconstruction:
        fast.__mul__ => O(L*lnM*lnlnM*lnlnlnM)
        slow.__mul__ => O(lnM**2)
    #]]]'''#'''
    @classmethod
    def _crt_precomputation7coprime7XXX_(cls, moduli7pairwise_coprime, /, **kwds4precomputation):
        return crt_precomputation7coprime7stepwise_(moduli7pairwise_coprime, **kwds4precomputation)
    @classmethod
    def _crt_reconstruction7coprime7XXX_(cls, crt_data7precomputation, residues, /, **kwds4reconstruction):
        return crt_reconstruction7coprime7stepwise_(crt_data7precomputation, residues, **kwds4reconstruction)
class CRT7coprime7blockwise(_IBaseCRT7coprime7XXX):
    r'''[[[
    [M:=II(moduli)][L:=len(moduli)]:
        #both precomputation&&reconstruction:
        slow.__mul__ => O(lnM**2)

        #precomputation:
        fast.__mul__ => O(L*lnM*lnlnM*lnlnlnM)
        #reconstruction:
        fast.__mul__ => O(lnL*lnM*lnlnM*lnlnlnM)
    #]]]'''#'''
    @classmethod
    def _crt_precomputation7coprime7XXX_(cls, moduli7pairwise_coprime, /, **kwds4precomputation):
        return crt_precomputation7coprime7blockwise_(moduli7pairwise_coprime, **kwds4precomputation)
    @classmethod
    def _crt_reconstruction7coprime7XXX_(cls, crt_data7precomputation, residues, /, **kwds4reconstruction):
        return crt_reconstruction7coprime7blockwise_(crt_data7precomputation, residues, **kwds4reconstruction)





def _API():
    def check_CRT_ans(us, M, rs, ans, /):
        'moduli/[pint] -> whole_modulus/pint -> remainders/[uint%modulus]{len==len(moduli)} -> whole_remainder/uint%whole_modulus -> None'
    def apply_CRT(us, rs, /, *, extended:bool):
        'moduli/[pint] -> remainders/[uint%modulus]{len==len(moduli)} -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'
    def apply_CRT__pairs(u_r_pairs, /, *, extended:bool):
        'Iter (modulus/pint, remainder/uint%modulus) -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'



def get_CRT_type_(*, extended:bool=False, ver=None):
    if extended: raise NotImplementedError
    match ver:
        #case None | 'long_term' | 'blockwise':
        #case 'short_term' | 'stepwise':
        case None | 'short_term' | 'long_term' | 'blockwise':
            CRT = CRT7coprime7blockwise
        case 'incremental' | 'growable' | 'stepwise':
            CRT = CRT7coprime7stepwise
        case _:
            raise Exception(ver)
    return CRT
def apply_CRT(us, rs, /, *, extended:bool, ver=None, **kwds4reconstruction):
    'moduli/[pint] -> remainders/[uint%modulus]{len==len(moduli)} -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'
    if extended: raise NotImplementedError
    if ver is None:
        ver = 'short_term'
    CRT = get_CRT_type_(extended=extended, ver=ver)
    return CRT(us)(rs, **kwds4reconstruction)
def apply_CRT__pairs(u_r_pairs, /, *, extended:bool, ver=None, **kwds4reconstruction):
    'Iter (modulus/pint, remainder/uint%modulus) -> (extended/bool{?allow modulus not coprime?}) -> whole_remainder/uint%whole_modulus'
    if extended: raise NotImplementedError
    us, rs = unzip_pairs(u_r_pairs)
    return apply_CRT(us, rs, extended=extended, ver=ver, **kwds4reconstruction)

# copy from:
#   view ../../python3_src/nn_ns/math_nn/Chinese_Remainder_Theorem.py
class CRT_Error(Exception):pass
class CRT_Answer_Error(CRT_Error):pass
#class CRT_Error__ECRT__remainders_inconsistent(CRT_Error):pass
class CRT_Error__moduli_empty(CRT_Error):pass
class CRT_Error__modulus_le_0(CRT_Error):pass
class CRT_Error__moduli_not_coprime(CRT_Error):pass
class CRT_Error__len4remainders(CRT_Error):pass

def check_CRT_ans(us, M, rs, ans, /, *, partial_ok=False):
    'moduli/[pint] -> whole_modulus/pint -> remainders/[uint%modulus]{len==len(moduli)} -> whole_remainder/uint%whole_modulus -> None'
    if partial_ok:
        if not len(rs) <= len(us): raise TypeError
    else:
        if not len(rs) == len(us): raise TypeError

    if not 0 <= ans < M: raise CRT_Answer_Error
    if not all((ans-r)%u==0 for r, u in zip(rs, us)): raise CRT_Answer_Error(us, M, rs, ans)
    return


__all__
from seed.math.Chinese_Remainder_Theorem__ver2 import crt_precomputation7coprime7blockwise_, crt_reconstruction7coprime7blockwise_

from seed.math.Chinese_Remainder_Theorem__ver2 import CRT7coprime7blockwise
from seed.math.Chinese_Remainder_Theorem__ver2 import apply_CRT, apply_CRT__pairs

from seed.math.Chinese_Remainder_Theorem__ver2 import check_CRT_ans
from seed.math.Chinese_Remainder_Theorem__ver2 import *
