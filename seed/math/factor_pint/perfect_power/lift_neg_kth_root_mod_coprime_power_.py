#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/perfect_power/lift_neg_kth_root_mod_coprime_power_.py

seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_:__doc__ -ht # -ff -df
#######

[[
NOTE:[M%2==0] => MAY_NOT[xij =[%Mj]= xj]
NOTE:[M==2**ez] => [xij =[%(max(2,Mj)///2)]= xj]
]]


'#'; __doc__ = r'#'
>>> k = 2
>>> y = 465871**k
>>> M = 2
>>> may_max_mulorder_mod_M = None
>>> j = 3
>>> xj = 1
>>> i = j
>>> lift_neg_kth_root_mod_coprime_power__human__ij_(k, M, may_max_mulorder_mod_M, i:=j, j, y, xj)
(2, 17)
>>> j = i+j-1
>>> xj = 17
>>> lift_neg_kth_root_mod_coprime_power__human__ij_(k, M, may_max_mulorder_mod_M, i:=j, j, y, xj)
(2, 209)
>>> j = i+j-1
>>> xj = 209
>>> lift_neg_kth_root_mod_coprime_power__human__ij_(k, M, may_max_mulorder_mod_M, i:=j, j, y, xj)
(2, 128209)
>>> j = i+j-1
>>> xj = 128209
>>> lift_neg_kth_root_mod_coprime_power__human__ij_(k, M, may_max_mulorder_mod_M, i:=j, j, y, xj)
(2, 4706006225)
>>> j
17
>>> xj
128209
>>> y*xj**2 %2**j
1
>>> j = i+j-1
>>> xj = 4706006225
>>> j
33
>>> xj
4706006225
>>> y*xj**2 %2**j
1
>>> sqrt_of_odd_mod_zpow_(y.bit_length()//2, y)
320561
>>> sqrt_of_odd_mod_zpow_(1+y.bit_length()//2, y)
58417
>>> sqrts_of_odd_mod_zpow_(y.bit_length()//2, y, validate=True)
(58417, 203727, 320561, 465871)
>>> sqrts_of_odd_mod_zpow_(1+y.bit_length()//2, y, validate=True)
(58417, 465871, 582705, 990159)
>>> sqrts_of_odd_mod_zpow_(2+y.bit_length()//2, y, validate=True)
(465871, 582705, 1514447, 1631281)
>>> sqrts_of_odd_mod_zpow_(3+y.bit_length()//2, y, validate=True)
(465871, 1631281, 2563023, 3728433)
>>> (1+y.bit_length()//2) -(5+y.bit_length())//2
-1
>>> (2+y.bit_length()//2) -(5+y.bit_length())//2
0
>>> (3+y.bit_length()//2) -(5+y.bit_length())//2
1



>>> kth_root_of_odd_mod_zpow__k_is_odd_(3, 3, 27)
3
>>> kth_root_of_odd_mod_zpow__k_is_odd_(3, 10, 999**3)
999
>>> kth_root_of_odd_mod_zpow__k_is_odd_(101, 10, 6847801**101)
313
>>> 6847801%2**10
313
>>> 6847801 .bit_length()
23
>>> kth_root_of_odd_mod_zpow__k_is_odd_(101, 23, 6847801**101)
6847801
>>> 6847801 -2**22
2653497
>>> kth_root_of_odd_mod_zpow__k_is_odd_(101, 22, 6847801**101)
2653497






py_adhoc_call   seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_   @f
from seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ import *
]]]'''#'''
__all__ = r'''
lift_neg_kth_root_mod_coprime_power__human__ij_
    lift_neg_kth_root_mod_coprime_power__human__MN_
        lift_neg_kth_root_mod_coprime_power__strict__ver1_



inv_mod_coprime_power_
sqrt_mod_coprime_power_
    sqrt_of_odd_mod_zpow_
        sqrts_of_odd_mod_zpow_


kth_root_of_odd_mod_zpow__k_is_odd_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge, check_may_
    from seed.math.floor_ceil_tools.fc_perfect import perfect_div
    from math import gcd
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...



def kth_root_of_odd_mod_zpow__k_is_odd_(k, j, y, i=None, xi=None, /):
    'k -> j -> y -> i -> xi -> xj/uint%2**j # [y%2 == 1][xi**k =[%2**i]= y][xj**k =[%2**j]= y][xj =[%2**i]= xi][j>=i>=3]'
    check_int_ge(1, k)
    check_int_ge(3, j)
    check_type_is(int, y)
    if i is None:
        i = 3
        xi = y&7
    check_int_ge(3, i)
    check_int_ge(i, j)
    check_type_is(int, xi)

    if not k&1 == 1:raise ValueError(k)
    if not y&1 == 1:raise ValueError(y)
    if i == j:
        xj = xi
        return xj
    M = 2
    777; may_max_mulorder_mod_M = None
    vy = inv_mod_coprime_power_(M, j, y)
    xj = _lifts__gkm_eq1_(k, M, may_max_mulorder_mod_M, j, vy, i, xi)
    return xj


def sqrts_of_odd_mod_zpow_(j, y, /, *, i_xi_pair=None, validate=False):
    'j -> y -> roots/[xj] # [y%2 == 1][xj**2 =[%2**j]= y][roots == {xj, 2**j-xj, (2**(j-1)+xj)%2**j, (2**(j-1)-xj)%2**j}]'
    xj = sqrt_of_odd_mod_zpow_(j, y, i_xi_pair=i_xi_pair)
    if j >= 3:
        half = 1 << (j-1)
        if xj > half:
            xj ^= half
        # [0 < xj < half]
        z = half -xj
        # [0 < z < half]
        if z < xj:
            a, b = z, xj
        else:
            a, b = xj, z
        # [0 < a < b < a+b==half]
        c = a^half
        d = b^half
        # [0 < a < b < a+b==half==c-a==d-b < c < d < 2**j]
        ls = [a, b, c, d]
    elif j == 2:
        ls = [1, 3]
        assert xj in ls
    elif j == 1:
        assert xj == 1
        ls = [1]
    elif j == 0:
        assert xj == 0
        ls = [0]
    else:
        raise 000
    assert xj in ls
    rs = (*ls,)
    if validate:
        Mj = 1<<j
        Mjmm = Mj-1
        yj = y&Mjmm
        for r in rs:
            assert yj == r**2&Mjmm
    return rs
def sqrt_of_odd_mod_zpow_(j, y, /, *, i_xi_pair=None):
    'j -> y -> xj/uint%2**max(1,j-2) # [y%2 == 1][xj**2 =[%2**j]= y][roots == {xj, 2**j-xj, (2**(j-1)+xj)%2**j, (2**(j-1)-xj)%2**j}] # xi => [j>=i>=3] => [xj =[%M**(i-2)]= xi]'
    check_int_ge(0, j)
    check_type_is(int, y)
    k = 2
    M = 2
    if y&1 == 0 and j > 0:raise ValueError(y)
    if i_xi_pair:
        (i, xi) = i_xi_pair
        check_int_ge(1, i)
        # [1 <= i]
        if i >= j:
            xj = xi&(-1+(1<<j))
            return xj
        # [1 <= i < j]
    else:
        (i, xi) = (3, 1)
        # [i == 3]
    # [i == 3]or[1 <= i < j]
    if j < 3:
        match j:
            case 2:
                if not y&3 == 1:raise ValueError
                xj = 1
            case 1:
                if not y&1 == 1:raise ValueError
                xj = 1
            case 0:
                xj = 0
            case _:
                raise 000
            #case _:
        xj
    else:
        # [j >= 3]
        # !! [i == 3]or[1 <= i < j]
        # [1 <= i <= j]
        if not y&7 == 1:raise ValueError
        if i == 1:
            i, xi = 2, 1
        # [2 <= i <= j]
        # [j >= 3]
        vy = inv_mod_coprime_power_(M, j, y)
        xj = _lifts__gkm_eq2__M_eq2_(k, M, j, vy, i, xi)
    return xj

def sqrt_mod_coprime_power_(M, j, y, x1, /):
    '[[M%2==1]or[log2(M)%1 == 0]] => M -> j -> y -> x1 -> xj # [gcd(M,y) == 1][x1**2 =[%M**1]= y][xj**2 =[%M**j]= y][[M%2==1] -> [xj =[%M]= x1]][[log2(M)%1 == 0] -> [xj =[%(max(2,Mj)///2)]= x1]]!!!!!!NOTE!!!!!!'
    check_int_ge(1, M)
    check_int_ge(0, j)
    check_type_is(int, y)
    check_type_is(int, x1)
    k = 2
    777; may_max_mulorder_mod_M = None
    if M == 1 or j == 0:
        xj = 0
    elif j == 1:
        xj = x1
    elif M&1 == 0:
        # [M :: even]
        if not 1 == M.bit_count():raise NotImplementedError
        ez = -1+M.bit_length()
        assert M == (1<<ez)
        xj = sqrt_of_odd_mod_zpow_(ez*j, y, i_xi_pair=(ez, x1))
    else:
        # [M :: odd]
        # [gcd(M,k) == 1]
        # [gkm == 1]
        vy = inv_mod_coprime_power_(M, j, y)
        xj = _lifts__gkm_eq1_(k, M, may_max_mulorder_mod_M, j, vy, 1, x1)
    return xj

def _lifts__gkm_eq1_(k, M, may_max_mulorder_mod_M, j, y, i, xi, /):
    # [gkm == 1]
    # [gcd(M,k) == 1]
    # [1 <= i <= j]
    ij_ls = _3_decompose_j_as_ij_pairs_(i, j)
    saved_j = j
    xj = xi
    Mj = Mi = M**i
    vk6Mj = vk6gkm_eq1 = pow(k, -1, Mi)
        # !! [gkm == 1]
    while ij_ls:
        (i, j) = ij_ls.pop()
        Mj
        if i == j:
            Mi = Mj
        elif i == j-1:
            Mi = Mj//M
        else:
            #raise 000
            #raise Exception(ij_ls, (i, j))
                # Exception: ([(15, 15), (7, 8), (4, 4)], (1, 3))
            Mi = M**i
        Mi
        if i == j:
            vk6Mi = vk6Mj
        else:
            vk6Mi = vk6Mj%Mi
        vk6Mi
        (_1, vk6Mij) = lift_neg_kth_root_mod_coprime_power__human__MN_(1, Mi, Mj, may_max_mulorder_mod_MN:=None, k, vk6Mj)
        may_max_mulorder_mod_Mij = _mk_may_max_mulorder_mod_MN(k, M, may_max_mulorder_mod_M, i, j, Mi, Mj)
        r = lift_neg_kth_root_mod_coprime_power__human__MN_(k, Mi, Mj, may_max_mulorder_mod_Mij, y, xj, vk6gkm_eq1=vk6Mi)
        #old:r = lift_neg_kth_root_mod_coprime_power__human__ij_(k, M, may_max_mulorder_mod_M, i, j, y, xj)
        match r:
            case (1, int(xij)):
                j += i
                xj = xij
                Mj *= Mi
                vk6Mj = vk6Mij
            case (_, None):
                raise 000
            case _:
                raise 000
            #case _:
        pass
    j, xj
    assert j == saved_j
    return xj

def _lifts__gkm_eq2__M_eq2_(k, M, j, y, i, xi, /):
    # [gkm == 2]
    # [gcd(M,k) == 2]
    # [M == 2]
    # [2 <= i <= j]
    assert k&3 == 2
    assert M == 2
    777; may_max_mulorder_mod_M = None
    saved_args = (k, M, j, y, i, xi)
    ij_ls = _2_decompose_j_as_ij_pairs_(i, j)
    saved_j = j
    xj = xi
    while ij_ls:
        (i, j) = ij_ls.pop()
        #for t in range(4):
        for t in range(2):
            r = lift_neg_kth_root_mod_coprime_power__human__ij_(k, M, may_max_mulorder_mod_M, i, j, y, xj)
            match r:
                case (2, int(xj)):
                    j += i
                    j -= 1
                    break
                case (_, None):
                    match t:
                        case 0:
                            half = 1<<(j-1)
                            # to keep lowbits, change only one bit
                            xj ^= half
                            continue
                            #old version:change too many bits
 
                    raise Exception(saved_args, (i, j, xj), r)
                        # ^Exception: ((2, 2, 18, 186153, 3, 1), (2, 3, 1), (2, None))
                        #   from:may_perfect_kth_root_of_(12, 35**12)
                    raise 000
                case _:
                    raise 000
                #case _:
            pass
        pass
    j, xj
    assert j == saved_j
    return xj



def _3_decompose_j_as_ij_pairs_(i0, j, /):
    # [j == _i+_j] # [gkm == 1]
    #
    # [1 <= i0 <= j]
    assert 1 <= i0 <= j
    zi = i0<<1
    ij_ls = []
    # [j >= i0]
    while j > zi:
        # [j > 2*i0]
        i = j//2
        j -= i
        # [j >= i >= i0]
        ij_ls.append((i,j))
        # [j >= i0]
    # [i0 <= j <= 2*i0]
    if j > i0:
        # [i0 < j <= 2*i0]
        # [0 < j-i0 <= i0]
        i = j-i0
        j = i0
        ij_ls.append((i,j))
    return ij_ls

def _2_decompose_j_as_ij_pairs_(i0, j, /):
    # [j == _i+_j-1] #2**j
    #
    # [k == 2]
    # [j >= 1]
    # [2 <= i0 <= j]
    assert 2 <= i0 <= j
    zimm = -1+(i0<<1)
    # [zimm >= 3]
    ij_ls = []
    # [j >= i0]
    while j > zimm:
        # [j > -1+2*i0 >= 3]
        j += 1
        # [j > 2*i0 >= 4]
        i = j//2
        j -= i
        # [j >= i >= i0 >= 2]
        ij_ls.append((i,j))
        # [j >= i0]
    # [i0 <= j <= -1+2*i0]
    if j > i0:
        # [i0 < j <= -1+2*i0]
        # [1 < j+1-i0 <= i0]
        i = j+1-i0
        j = i0
        ij_ls.append((i,j))
    return ij_ls

def _1_decompose_j_as_ij_pairs_(j, /):
    # [i0 == 1]
    # [j >= 1]
    assert j >= 1
    ij_ls = []
    while j > 1:
        i = j//2
        j -= i
        ij_ls.append((i,j))
    return ij_ls

def inv_mod_coprime_power_(M, j, y, /):
    'M -> j -> y -> xj # [gcd(M,y) == 1][y*xj =[%M**j]= 1]'
    check_int_ge(1, M)
    check_int_ge(0, j)
    check_type_is(int, y)
    k = 1
    777; may_max_mulorder_mod_M = None
    if M == 1 or j == 0:
        xj = 0
    else:
        # [j >= 1]
        saved_j = j
        x1 = pow(y, -1, M)
        xj = _lifts__gkm_eq1_(k, M, may_max_mulorder_mod_M, j, y, 1, x1)
    return xj


def lift_neg_kth_root_mod_coprime_power__human__ij_(k, M, may_max_mulorder_mod_M, i, j, y, xj, /, *, vk6gkm_eq1=None):
    'k -> M -> may max_mulorder_mod_M -> i -> j -> y -> xj -> (gkmi, may xij_g) # [[y*xj**k%M**j == 1][y*xij_g**k%M**(i+j) == 1][xij_g =[%M**j]= xj][0 <= xij_g < M**(i+j)///gcd(k,M**i)][gkmi == gcd(k,M**i)]] #see:lift_neg_kth_root_mod_coprime_power__strict__ver1_'
    check_int_ge(1, k)
    check_int_ge(2, M)
    check_may_([check_int_ge, 1], may_max_mulorder_mod_M)
    check_int_ge(1, i)
    check_int_ge(i, j)
    check_type_is(int, y)
    check_type_is(int, xj)
    Mi = M**i
    Mj = Mi if i == j else M**j
    _M, _N = Mi, Mj
    _xn = xj
    _may_max_mulorder_mod_MN = _mk_may_max_mulorder_mod_MN(k, M, may_max_mulorder_mod_M, i, j, Mi, Mj)

    (_gkm, _may_xmn_g) = lift_neg_kth_root_mod_coprime_power__human__MN_(k, _M, _N, _may_max_mulorder_mod_MN, y, _xn, vk6gkm_eq1=vk6gkm_eq1)
    may_xij_g = _may_xmn_g
    gkmi = _gkm
    return (gkmi, may_xij_g)

def _mk_may_max_mulorder_mod_MN(k, M, may_max_mulorder_mod_M, i, j, Mi, Mj, /):
    if k < 3:
        return None
    if not may_max_mulorder_mod_M is None:
        max_mulorder_mod_M = may_max_mulorder_mod_M
        if k < max_mulorder_mod_M:
            return None
    #
    if M&1 == 1:
        if not may_max_mulorder_mod_M is None:
            max_mulorder_mod_Mij = max_mulorder_mod_M*Mi*(Mj//M)
            _may_max_mulorder_mod_MN = max_mulorder_mod_Mij
        else:
            _may_max_mulorder_mod_MN = None
        _may_max_mulorder_mod_MN
    elif M.bit_count() == 1:
        ez4Mij = (-1+M.bit_length())*(i+j)
        assert ez4Mij >= 2
        max_mulorder_mod_Mij = 1<<max(1, ez4Mij-2)
        _may_max_mulorder_mod_MN = max_mulorder_mod_Mij
    elif not may_max_mulorder_mod_M is None:
        (ez4M, odd4M) = factor_pint_out_power_of_base_(2, M)
        (ez4xM, odd4xM) = factor_pint_out_power_of_base_(2, max_mulorder_mod_M)
        ez4Mij = ez4M*(i+j)
        assert ez4Mij >= 2
        ez4xMij6zpow = 1<<max(1, ez4Mij-2)
        ez4xMij6M = ez4xM
        ez4xMij = max(ez4xM, ez4xMij6zpow)
        d = (ez4xM +ez4Mij -ez4M) -ez4xMij
        if not d >= 0:raise 000
        max_mulorder_mod_Mij = (max_mulorder_mod_M*Mi*(Mj//M)) >>d
        _may_max_mulorder_mod_MN = max_mulorder_mod_Mij
    else:
        _may_max_mulorder_mod_MN = None
    return _may_max_mulorder_mod_MN
def lift_neg_kth_root_mod_coprime_power__human__MN_(k, M, N, may_max_mulorder_mod_MN, y, xn, /, *, vk6gkm_eq1=None):
    'k -> M -> N -> may max_mulorder_mod_MN -> y -> xn -> (gkm, may xmn_g) # [[y*xn**k%N == 1][y*xmn_g**k%(M*N) == 1][xmn_g =[%N]= xn][0 <= xmn_g < (M*N)///gcd(k,M)][gkm == gcd(k,M)]] #see:lift_neg_kth_root_mod_coprime_power__strict__ver1_'
    check_int_ge(1, k)
    check_int_ge(2, M)
    check_int_ge(M, N)
    check_may_([check_int_ge, 1], may_max_mulorder_mod_MN)
    if not N%M == 0:raise ValueError(M, N)
    check_type_is(int, y)
    check_type_is(int, xn)
    if not None is vk6gkm_eq1:
        # [gkm == 1]
        gkm = 1
        k_g = k
        M_g = M
        vk_g = vk6gkm_eq1%M_g
    else:
        gkm = gcd(k, M)
        k_g = k //gkm
        M_g = M //gkm
        vk_g = pow(k_g, -1, M_g)
    MN = M*N
    ymn = y%MN
    xn %= N

    may_xmn_g = lift_neg_kth_root_mod_coprime_power__strict__ver1_(k, gkm, M_g, vk_g, N, MN, may_max_mulorder_mod_MN, ymn, xn)
    return (gkm, may_xmn_g)
def lift_neg_kth_root_mod_coprime_power__strict__ver1_(k, gkm, M_g, vk_g, N, MN, may_max_mulorder_mod_MN, ymn, xn, /):
    r'''[[[
... -> xn -> may xmn_g
[[y*xn**k%N == 1][y*xmn_g**k%(M*N) == 1][xmn_g =[%N]= xn][0 <= xmn_g < (M*N)///gcd(k,M)]]

##############################
ver1:
##############################
[[k,M,N,y,xn,xmn_g :: int]
    [k >= 1]        # x**-k
    [M >= 2]        #%M
    [N >= 2]        #%N
    [N%M == 0]
    [gcd(N,y) == 1] #coprime
    [MN := M*N]
    [ymn := y%MN]
    [yn := y%N]
    [0 <= xn < N]
    [yn == xn**-k%N] #neg_kth_root%N


    [gkm := gcd(k,M)]
    [M_g := M///gkm]
    [MN_g := (M_g*N)]
    [k_g := k///gkm]
    [vk_g := (k_g**-1 %M_g)]
    [ymn_g := y%MN_g]
    [zmn := xn**k %MN]
    [0 <= qm_g < M_g]
    [xmn_g := (qm_g*N +xn)]
    #xxx:[ymn_g == xmn_g**-k%MN_g]
    [ymn*xmn_g**k%MN == 1]
    ]:
    #########neg_kth_root:xn --> xmn_g
    [yn*xn**k%N == 1]
    [ymn*xmn_g**k%MN == 1]
    [0 <= xmn_g < M_g*N]
    #########
    [ymn*xmn_g**k %MN == 1]
    [ymn*(qm_g*N +xn)**k %MN == 1]
    !! [N%M == 0]
    [(N)**2 %MN == 0]
    !! [k >= 1]
    !! binomial_theorem
    [ymn*(k*qm_g*N*xn**(k-1) +xn**k) %MN == 1]
    [(ymn*k*qm_g*N*xn**(k-1)) %MN == (1 -ymn*xn**k) %MN]
    !! [zmn := xn**k %MN]
    [(ymn*k*qm_g*N*xn**(k-1)) %MN == (1 -ymn*zmn) %MN]
    [(ymn*k*qm_g*xn**(k-1)) %M == (1 -ymn*zmn) ///N %M]
    [(ymn*k*qm_g*xn**k) %M == (1 -ymn*zmn) ///N *xn %M]
    !! [N%M == 0]
    [(ymn*k*qm_g*xn**k %N) %M == (1 -ymn*zmn) ///N *xn %M]
    [(k*qm_g*(ymn*xn**k %N)) %M == (1 -ymn*zmn) ///N *xn %M]
    [(k*qm_g*(yn*xn**k %N)) %M == (1 -ymn*zmn) ///N *xn %M]
    !! [yn == xn**-k%N]
    [(k*qm_g) %M == (1 -ymn*zmn) ///N *xn %M]
    !! [gkm := gcd(k,M)]
    !! [M_g := M///gkm]
    !! [k_g := k///gkm]
    [(gkm*k_g*qm_g) %(gkm*M_g) == (1 -ymn*zmn) ///N *xn %(gkm*M_g)]
    [(1 -ymn*zmn) ///N %gkm == 0]:
        [(k_g*qm_g) %M_g == (1 -ymn*zmn) ///N ///gkm *xn %M_g]
        !! [vk_g := (k_g**-1 %M_g)]
        [qm_g == (1 -ymn*zmn) ///N ///gkm *xn *vk_g %M_g]
        !! [xmn_g := (qm_g*N +xn)]
        #bug:[xmn_g == xn *(1 +vk_g*(1 -ymn*zmn) ///gkm) %M_g]
        [xmn_g == xn +N*(xn*vk_g*(1 -ymn*zmn) ///N ///gkm %M_g)]
        [xmn_g == xn +N*(xn*vk_g*(1 -ymn*zmn) %MN ///N ///gkm %M_g)]
        [xmn_g == xn +N*((1 -ymn*zmn) %MN ///(gkm*N) *xn*vk_g %M_g)]
            # FORMULA_1
        #cannot factor out "xn":
        [xmn_g == xn +(xn*vk_g*(1 -ymn*zmn) ///gkm %MN_g)]
        [xmn_g == xn +(xn*vk_g*(1 -ymn*zmn) %MN ///gkm)]
        [xmn_g == (xn*gkm +(xn*vk_g*(1 -ymn*zmn)) %MN) ///gkm]
##############################





##############################
ver2:
##############################
[[k,M,N,N_g,y,xn_g,xmn_g :: int]
    [k >= 1]        # x**-k
    [M >= 2]        #%M
    [N >= 2]        #%N
    [N_g >= 2]      #%N_g
    [N%M == 0]
    [N%N_g == 0]
    [gcd(N,y) == 1] #coprime
    [MN := M*N]
    [ymn := y%MN]
    [yn := y%N]
    [0 <= xn_g < N_g]
    #xxx:[yn == xn_g**-k%N] #neg_kth_root%N
    #xxx:[yn*xn_g**k%N == 1]
    [gkw := N///N_g]
    [@[u:<-[0..<gkw]] -> [yn*(u*N_g+xn_g)**k%N == 1]]


    [gkm := gcd(k,M)]
    [M_g := M///gkm]
    [MN_g := (M_g*N)]
    [k_g := k///gkm]
    [vk_g := (k_g**-1 %M_g)]
    [ymn_g := y%MN_g]
    [u:<-[0..<gkw]]
    [zmn := (u*N_g +xn)**k %MN]
    [qm_g:<-[0..<M_g]]
    [xmn_g := (qm_g*N +u*N_g +xn)]
    #xxx:[ymn_g == xmn_g**-k%MN_g]
    #xxx:[ymn*xmn_g**k%MN == 1]
    [@[h:<-[0..<gkm]] -> [ymn*(h*MN_g+xmn_g)**k%MN == 1]]
    ]:
    #########neg_kth_root:xn --> xmn_g
    #xxx:[yn*xn**k%N == 1]
    #xxx:[ymn*xmn_g**k%MN == 1]
    [@[u:<-[0..<gkw]] -> [yn*(u*N_g+xn_g)**k%N == 1]]
    [@[h:<-[0..<gkm]] -> [ymn*(h*MN_g+xmn_g)**k%MN == 1]]
    [0 <= xmn_g < M_g*N]
    #########
    [h:<-[0..<gkm]]:
        [ymn*(h*MN_g+xmn_g)**k %MN == 1]
        !! [xmn_g := (qm_g*N +u*N_g +xn)]
        [ymn*(h*MN_g +(qm_g*N +u*N_g +xn))**k %MN == 1]
        [ymn*((h*M_g +qm_g)*N +(u*N_g +xn))**k %MN == 1]
        !! [N%M == 0]
        [(N)**2 %MN == 0]
        !! [k >= 1]
        !! binomial_theorem
        [ymn*(k*(h*M_g +qm_g)*N*(u*N_g +xn)**(k-1) +(u*N_g +xn)**k) %MN == 1]
        !! [zmn := (u*N_g +xn)**k %MN]
        [ymn*(k*(h*M_g +qm_g)*N*(u*N_g +xn)**(k-1) +zmn) %MN == 1]
        [(k*(h*M_g +qm_g)*N*ymn*(u*N_g +xn)**(k-1) +ymn*zmn) %MN == 1]
        [(k*(h*M_g +qm_g)*N*ymn*(u*N_g +xn)**(k-1)) %MN == (1 -ymn*zmn) %MN]
        [(k*(h*M_g +qm_g)*ymn*(u*N_g +xn)**(k-1)) %M == (1 -ymn*zmn)///N %M]
        [(k*(h*M_g +qm_g)*ymn*(u*N_g +xn)**k) %M == (1 -ymn*zmn)///N *(u*N_g +xn) %M]
        !! [N%M == 0]
        [(k*(h*M_g +qm_g)*(ymn*(u*N_g +xn)**k %N)) %M == (1 -ymn*zmn)///N *(u*N_g +xn) %M]
        !! [@[u:<-[0..<gkw]] -> [yn*(u*N_g+xn_g)**k%N == 1]]
        !! [yn == ymn%N]
        [(k*(h*M_g +qm_g)) %M == (1 -ymn*zmn)///N *(u*N_g +xn) %M]
        !! [gkm := gcd(k,M)]
        !! [M_g := M///gkm]
        !! [k_g := k///gkm]
        [((gkm*k_g)*(h*M_g +qm_g)) %(gkm*M_g) == (1 -ymn*zmn)///N *(u*N_g +xn) %(gkm*M_g)]
        [(1 -ymn*zmn) ///N %gkm == 0]:
            [(k_g*(h*M_g +qm_g)) %M_g == (1 -ymn*zmn)///N ///gkm *(u*N_g +xn) %M_g]
            [(k_g*qm_g) %M_g == (1 -ymn*zmn)///N ///gkm *(u*N_g +xn) %M_g]
            #########howto_set_u_to_mk_zmn_pass_the_test?:goto
            [(k_g*qm_g) %M_g == (1 -ymn*zmn)///N ///gkm *(u*N_g +xn) %M_g]
            !! [vk_g := (k_g**-1 %M_g)]
            [qm_g == (1 -ymn*zmn)///N ///gkm *(u*N_g +xn) *vk_g %M_g]

            !! [xmn_g := (qm_g*N +u*N_g +xn)]
            [xmn_g == (u*N_g +xn) +N*((1 -ymn*zmn)///N ///gkm *(u*N_g +xn) *vk_g %M_g)]
            [xmn_g == (u*N_g +xn) +N*((1 -ymn*zmn%MN)///N ///gkm *(u*N_g +xn) *vk_g %M_g)]
                #cannot factor out "(u*N_g +xn)":
##############################
##############################



#########howto_set_u_to_mk_zmn_pass_the_test?:here
    # [:sufficient_condition]:goto
    [[N_g%(gkm*gkw) == 0][gkw%gkm == 0][1 == gcd(k_g, gkw)]]
        + <<==: [gkm == gkw == 1]
        + <<==: [gkm == gkw == k][is_prime_(k)][N%k**3 == 0]
#########:begin:
...recur???
!! [zmn := (u*N_g +xn)**k %MN]
!! [(1 -ymn*zmn) ///N %gkm == 0]
[(1 -ymn*(u*N_g +xn)**k %MN) ///N %gkm == 0]
[ymn*(u*N_g +xn)**k %(gkm*N) == 1]
[N_g**2%(gkm*N) == 0]:
    <==> [N_g%(gkm*gkw) == 0]
    [ymn*(k*u*N_g*xn**(k-1) +xn**k) %(gkm*N) == 1]
    [(k*u*N_g*ymn*xn**(k-1) +ymn*xn**k) %(gkm*N) == 1]
    [(k*u*N_g*ymn*xn**(k-1)) %(gkm*N) == (1 -ymn*xn**k) %(gkm*N)]
    !! [gkm := gcd(k,M)]
    !! [k_g := k///gkm]
    !! [gkw := N///N_g]
    [((gkm*k_g)*u*N_g*ymn*xn**(k-1)) %(gkm*(gkw*N_g)) == (1 -ymn*xn**k) %(gkm*(gkw*N_g))]
    [((gkm*k_g)*u*ymn*xn**(k-1)) %(gkm*gkw) == (1 -ymn*xn**k %(gkm*N)) ///N_g %(gkm*gkw)]
    [(1 -ymn*xn**k %(gkm*N)) ///N_g %gkm == 0]:
        # <<==: eg. [gkw%gkm == 0]
        [(k_g*u*ymn*xn**(k-1)) %gkw == (1 -ymn*xn**k %(gkm*N)) ///(gkm*N_g) %gkw]
        !! [(1 -yn*xn**k) %N == 0]
        !! [N%gkw == 0]
        [(1 -yn*xn**k) %gkw == 0]
        [(1 -ymn*xn**k) %gkw == 0]
        [(k_g*u) %gkw == (1 -ymn*xn**k %(gkm*N)) ///(gkm*N_g) *xn %gkw]
        [ggkw := gcd(k_g, gkw)]
        ...recur???
        [ggkw == 1]:
            [u == (1 -ymn*xn**k %(gkm*N)) ///(gkm*N_g) *xn *(k_g**-1 %gkw) %gkw]
            [vk_gg := (k_g**-1 %gkw)]
            [u == (1 -ymn*xn**k %(gkm*N)) ///(gkm*N_g) *xn * vk_gg %gkw]
                # <<==: [[N_g%(gkm*gkw) == 0][gkw%gkm == 0][1 == gcd(k_g, gkw)]]
                #   [:sufficient_condition]:here
    [gkw%gkm == 0]:
        !! [(1 -yn*xn**k) %N == 0]
        [(1 -ymn*xn**k) %N == 0]
        [(1 -ymn*xn**k) %(N_g*gkw) == 0]
        !! [gkw%gkm == 0]
        [(1 -ymn*xn**k) %(gkm*N_g) == 0]
        [(1 -ymn*xn**k) ///N_g %gkm == 0]
        [(1 -ymn*xn**k %(gkm*N)) ///N_g %gkm == 0]
#########:end


    #]]]'''#'''
    #zmn = pow(xn, k, MN)
    _k = k%may_max_mulorder_mod_MN if not may_max_mulorder_mod_MN is None else k
    zmn = pow(xn, _k, MN)

    # [xmn_g == xn +N*((1 -ymn*zmn) %MN ///(gkm*N) *xn*vk_g %M_g)]
    tmp = perfect_div((1 -ymn*zmn %MN), N)
    if not tmp%gkm == 0:
        may_xmn_g = None
    else:
        tmp = perfect_div(tmp, gkm)
        xmn_g = xn +N*(xn%M_g *vk_g %M_g *tmp %M_g)
        may_xmn_g = xmn_g
    may_xmn_g
    return may_xmn_g


__all__

from seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ import lift_neg_kth_root_mod_coprime_power__human__ij_, lift_neg_kth_root_mod_coprime_power__human__MN_, lift_neg_kth_root_mod_coprime_power__strict__ver1_

from seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ import inv_mod_coprime_power_, sqrt_mod_coprime_power_, sqrt_of_odd_mod_zpow_, sqrts_of_odd_mod_zpow_, kth_root_of_odd_mod_zpow__k_is_odd_

from seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ import *
