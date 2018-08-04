
'''
the ring of coefficients is field # really??
    1) div not left_div/right_div ==>> commutative
        # so, why not def left_div/right_div?? division ring
    2) deg (f*h) == deg f + deg h ==>> ([c0!=0!=c1] -->> [c0*c1!=0]) ==>> domain
        ==>> integral domain
    3) div_scale ==>> 1/c ==>> field
        # why not div monic polynomial only??
        # or psuedo-division
'''

'''
[f!=0]: deg f >= 0
len f = 0 if f==0 else deg f + 1
add f g = f+g
concat [f,g] = f++g = f+g where
    exist h. x^(deg g+1)*h == f
mul f g = f*g
[f*g!=0]:deg (f*g) = deg f + deg g
    len (f*g) - 1 = (len f - 1) + (len g - 1)
    len (f*g) = len f + len g - 1

low m f = g where
    len g <= m # deg g <= m-1
    exist h. f = g + x^m * h
low_opp m f = f - low m f
lead m f = low_opp (len f - m) f

f >> m = rshift m f = div f (x^m)
f << m = lshift m f = f * (x^m)

# DIV
divmod f g = (q, r) where
    f = q*g + r
    r = 0 or deg r < deg g

# DIV_SHORT
# floor_div
div f g = q where
    (q, r) = divmod f g
div_lead m f g = lead m (div f g)
    = (div (f>>dL) g) << dL where
    dL = len f +1 - m - len g

# MUL_SHORT
mul_low m f g = low m (mul f g)
# MUL_SHORT_OPP
mul_low_opp m f g = low_opp m (mul f g)

inv k g = div (1 << k) g
inv2 g = inv (2 * deg g) g

####### new
    1) def inv2
        # recur; half the size
        inv2 g = ...inv2 (g>>m)...      # by (T3-2) decrease (deg g)
    2) def inv
        invg ::= inv (2*deg g - 2) g
        invg = inv2 g >> 2              # by (T0-2) rshift
        inv k g = ...                   # by (T2) square each time
                                        #  and finally by (T0-2) rshift
    3) def div_core
        k = len f - 1
        div_core f g = mul f (inv k g) >> k  # by (T1) "div via mul inv"
    4) def div
        # rshift f and g when possible
        div f g = div (f>>m) (g>>m)  # by (T3-2) when dL = 0, m>0
        div f g = div (f>>m) (g>>m)  # m == ndeg g > 0
        div f g = div_core f g




####### old
    div_std f g | deg f == 2 * deg g = ??????????
        # deg q = m = 2m - m = deg f - deg g
    div_reduce f g | deg f == 2 * deg g = div_std f g
    div_reduce f g | deg f < 2 * deg g =
        let k = len g * 2 - len f - 1 = deg g * 2 - deg f in
        div_std (f >> k) (g >> k)
    div_reduce f g | deg f > 2 * deg g = q where
        k = len g
        (q_, r_) = divmod (f >> k) g  # O(n) ==>> total O(n^2)??
        q_low = div_reduce ((r_ << k) + low k f) g
        q = (q_ << k) + q_low

'''


'''
theroem and proof
------------------------------------
(T0-1) [g != 0] ==>> [(f+h)//g == f//g + h//g][(f+h)%g == f%g + h%g]
(T0-2) [g != 0 != h] ==>> [f//h//g == f//(g*h) == f//g//h]
# Q: div f g = ??
(T1) [g != 0][len f <= k+1][invg == (1<<k)//g][k>=-1] ==>> [f//g == (f*invg)>>k]
# A: div f g = (f*inv k g) >> k where k = len f - 1
#    inv k g = q where (q, r) = kdivmod k g
# Q: kdivmod k g = divmod (1<<k) g = ??
(T2-0) [g != 0][L = 2*deg g - 2][invg = (1<<L)//g][
    len r1 < len g][r2 == (r1^2 % g)]
    ] ==>> [r2 = r1^2 - ((r1^2*invg)>>L)*g]
(T2) [g != 0][L = 2*deg g - 2][invg = (1<<L)//g][
    (invk, r1) == divmod (1<<k) g][(inv2k, r2) == divmod (1<<(2*k)) g
    ] ==>> [inv2k = (invk*g+2*r1)*invk + (r1^2*invg)>>L][
            r2 = r1^2 - ((r1^2*invg)>>L)*g]
# A: kdivmod 1 g = ...
#    kdivmod (2^k) g = (inv2k, r2) where (invk, r1) = kdivmod (2^(k-1)) g; ...
#    but requires: inv (2*deg g - 2) g
#    should decrease (deg g)
(T3-1)[g != 0][L >= 0][div f g >> L == div (f>>L) g] # by (T0-2)
(T3-2)[g !=0][deg g >= m][dL = max 0 (deg f+m - 2*deg g)]
    ==>> [div (f>>dL) g = div (f>>dL>>m) (g>>m)]
    =[(T3-1)]=>> [div f g >>dL = div (f>>dL>>m) (g>>m)]
    # [dL = def f+m -2*deg g > 0]
    #   N = deg (f>>dL>>m) = def f -dL-m = 2*deg g -2*m = 2*deg (g>>m)
    #   deg q = deg f - deg g - dL = deg g - m
    #   m = (deg g+1)//2 ==>> [N ~=~ deg g -[0/1]][deg q = (deg g)//2]
# _div f g | deg g == 0 = ...
# _div f g = let x = deg f -2*deg g in q where
#       if x < 0 then let m = -x, dL = 0 in div (f>>m) (g>>m)
#       else let m = (deg g+1)//2 > 0, dL=...>0 in q where
#           # eval (1<<N/(g>>m)) and then mul
#           invg = inv2 (g>>m)
#           invN = inv N (g>>m) invg
#           q = (f>>dL>>m)*invN>>N
#           ### old version:
#           #q_ = div (f>>dL>>m) (g>>m)
#           #r_ = f - q_<<dL*g = f - q_*g<<dL = (f>>dL-q_*g)<<dL ++ low dL f
#           #_q = div r_ g
#           #q = q_<<dL ++ _q

# inv2 g ::= inv (2*deg g) g
# inv2 g | deg g == 0 = ...
# inv2 g = q where
#   deg g >= 1
#   f = 1<<(2*deg g)
#   m = (deg g + 1)//2 >= 1
#       low m f == 0
#       2m <= deg g + 1 <= 2*deg g
#       f >> 2m != 0
#   gh = g >> m
#   inv_gh = inv2 gh # deg inv_gh = deg gh = deg g - m
#   rem_gh = 1<<(2*(deg g - m)) - inv_gh*gh = f>>(2m) - inv_gh*gh
#          = - mul_low (deg g - m) inv_gh gh
#   dL = deg f + m - 2*deg g = m
#   f//g >>dL = f>>dL>>m //(g>>m)
#   q_ = f//g >>m = f>>(2m) //(g>>m) = 1<<(2*(deg g - m)) //gh = inv_gh
#   r_ = f - q_<<dL*g = f - q_*g<<dL = (f>>dL-q_*g)<<dL ++ low dL f
#       = (f>>m - inv_gh*g)<<m  +  0
#       = (f>>(2m)<<m + (low m (f>>m)) - inv_gh*(g>>m)<<m - inv_gh*(low m g))<<m
#       = (f>>(2m)<<m + 0 - inv_gh*gh<<m - inv_gh*(low m g))<<m
#       = ((f>>(2m)-inv_gh*gh)<<m - inv_gh*(low m g))<<m
#       = (rem_gh<<m - inv_gh*(low m g))<<m
#   deg r_ <= m + max [deg (rem_gh<<m), deg inv_gh + m-1]
#           = m + max [deg g - 1, deg g - m +m -1]
#           = m + deg g - 1
#   deg (r_>>m) = deg g - 1 = (2*deg gh) + deg g - 1 - 2(deg g - m)
#           = 2*deg gh -(1+deg g) +2m <= 2*deg gh
#   # dL{f:=r_} = 0 for deg r_ + m -2*deg g <= 2m -(deg g +1) <= 0
#   _q = div r_ g = r_>>m // (g>>m) = r_>>m//gh
#       = (r_>>m)*inv_gh >> (2*deg gh)
#       = (rem_gh<<m - inv_gh*(low m g))*inv_gh >> (2*deg gh)
#       = (-mul_low(deg g-m, inv_gh, gh)<<m - inv_gh*(low m g))*inv_gh>>(2*deg g-2m)
#       = -(mul_low(deg g-m, inv_gh, gh)<<m + inv_gh*(low m g))*inv_gh>>(2*deg g-2m)
#   q = q_<<dL ++ _q = inv_gh<<m ++ _q
#       = inv_gh<<m ++ (rem_gh<<m - inv_gh*(low m g))*inv_gh >> (2*deg g-2m)
#       = inv_gh<<m ++ mul_rshift(2*deg g-2m, rem_gh<<m - inv_gh*(low m g), inv_gh)



(T4) [len g > L >= 0] ==>> [inv2 (g>>L) == inv2 g >> L]
    # for may_invGE2_g/extract_may_invGE2_g



----------
proof:
------------------------------------
(T0-1) [g != 0] ==>> [(f+h)//g == f//g + h//g][(f+h)%g == f%g + h%g]
    f = (f//g)*g + f%g
    h = (h//g)*g + h%g
    f+h = (f//g+h//g)*g + (f%g+h%g)
    f+h = (f+h)//g*g + (f+h)%g
    # len (f%g + h%g) =?= len ((f+h)%g)
    [deg g == 0]
        f%g = 0 = h%g
        f%g+h%g = 0
        f//g+h//g = (f+h)//g
    [deg g > 0]
        deg (f%g) < deg g
        deg (h%g) < deg g
        deg (f%g + h%g) <= max [deg (f%g), deg (h%g)] < deg g
        f//g+h//g = (f+h)//g
    (f+h)//g == f//g + h//g
(T0-2) [g != 0 != h] ==>> [f//h//g == f//(g*h) == f//g//h]
    obviously

# div = mul inv
(T1) [g != 0][len f <= k+1][invg == (1<<k)//g][k>=-1] ==>> [f//g == (f*invg)>>k]
    [k < deg g]
        invg = 0
        len f <= k+1 < deg g + 1 = len g
        f//g = 0 = (f*invg)>>k
    [f = 0]
        f//g = 0 = (f*invg)>>k
    [deg g == 0]
        invg = (1/g) << k
        f*invg = f*(1/g) << k
        (f*invg)>>k = f*(1/g) = f//g
    [k >= deg g > 0][f != 0]
        deg (1<<k) = k
        deg invg = k - deg g            # k >= deg g
        (1<<k) = invg*g + ri
            0 <= deg ri < deg g         # deg g > 0
        # using (deg f)                 # f != 0
            deg ((f*ri)//g) = deg f + deg ri - deg g
                            < deg f = len f - 1 <= (k+1) - 1 = k
            deg ((f*ri)//g) < k
            (f*ri//g) >> k = 0
            f//g = (f<<k)//g >> k
                = (f*(1<<k))//g >> k
                = (f*(invg*g + ri))//g >> k
                = (f*invg*g + f*ri)//g >> k
                = (f*invg + f*ri//g) >> k
                = (f*invg) >> k + (f*ri//g) >> k
                = (f*invg) >> k
    ---------------------- done ----------------------------
    invg = div (1 << (len f - 1)) g
    div f g = mul_rshift (len f - 1) f invg

(T2-0) [g != 0][L = 2*deg g - 2][invg = (1<<L)//g][
    len r1 < len g][r2 == (r1^2 % g)]
    ] ==>> [r2 = r1^2 - ((r1^2*invg)>>L)*g]
    # ==>> [r2 = mul_low (deg g) r1 r1 - mul_low (deg g) ((r1^2*invg)>>L) g]
    r = f%g = f - (f//g)*g = f - (f * (inv (len f-1) g) >> (len f-1))*g # (T1)
    let f = r1^2
    [r1 == 0]
        left = r2 = 0 = right
    [r1 != 0]
        len f = len r1 * 2 - 1          # r1 != 0
        Dr12 = len f - 1 = len r1 * 2 - 2 <= deg g * 2 - 2 = L
        r2 = (r1^2)%g = (r1^2) - (f * inv L g >>L) * g = right
    -------------- done -----------------
    # used in pow_mod/inv2
    [r1 != 0][deg r1 < deg g]
        Dg = deg g
        Dr12 = deg (r1^2) = 2*deg r1 <= 2*(deg g - 1) = L
        # r2 may be 0; e.g. r1^2 == g
        len r2 <= min [Dg, Dr12+1] = maxLr2
        f = r1^2
        r2 = low maxLr2 (f - (f*inv Dr12 g >>Dr12)*g)
           = low maxLr2 f - low maxLr2 ((f*inv Dr12 g >>Dr12)*g)
           = low maxLr2 f - mul_low maxLr2 (f*inv Dr12 g >>Dr12) g
           = low maxLr2 f - mul_low maxLr2 (f*(invg>>(L-Dr12)) >>Dr12) g
           = low maxLr2 f - mul_low maxLr2 (mul_rshift Dr12 f (invg>>(L-Dr12))) g

(T2) [g != 0][L = 2*deg g - 2][invg = (1<<L)//g][
    (invk, r1) == divmod (1<<k) g][(inv2k, r2) == divmod (1<<(2*k)) g
    ] ==>> [inv2k = (invk*g+2*r1)*invk + (r1^2*invg)>>L][
            r2 = r1^2 - ((r1^2*invg)>>L)*g]
    [k < 0]
        invk = 0 = inv2k
        r1 = 0 = r2
    [deg g == 0]
        L < 0
        invg = 0
        r1 = 0 = r2
        invk = (1/g) << k
        inv2k = (1/g) << 2k
        right = (invk*g+2*r1)*invk + (r1^2*invg)>>L
                = invk*g*invk
                = (1/g)<<k * g * (1/g)<<k
                = (1/g)<<2k
                = inv2k = left
    [k >= 0][deg g > 0]
        1<<k = invk*g + r1
            0 <= deg r1 < deg g # deg g > 0
        1<<(2k) = inv2k*g + r2
        1<<(2k) = (1<<k)^2 = (invk*g + r1)^2 = (invk*g+2*r1)*invk*g + r1^2
            0 <= deg (r1^2) = 2*deg r1 <= 2*deg g - 2 = L
        inv2k = (invk*g+2*r1)*invk + (r1^2)//g
        r2 = (r1^2)%g = r1^2 - (r1^2)//g
        (r1^2)//g = (r1^2*invg)>>L

(T3-1)[g != 0][L >= 0][div f g >> L == div (f>>L) g]
    # (T0-2) ==>> f//g>>L = f//g//(1<<L) = f//(1<<L)//g = f>>L>>g
    # f//g>>L =?= f>>L//g
    [len f+1 - len g <= L] or [f = 0]
        left = 0 = right
    [deg g = 0]
        left = f*(1/g)>>L = f>>L *(1/g) = right
    [L = 0]
        left = div f g = right
    [deg f >= deg g + L][deg g > 0][L > 0] # using (deg f) # f!=0
        deg f >= deg g + L > deg g > 0 # deg g > 0 ; L > 0
            deg f > L
        f = (f//g)*g + (f%g) = inv1*g + r1
        deg r1 < deg g # deg g > 0
        f>>L//g = (inv1*g+r1)>>L//g
                # 0) (f+h)//g = f//g + h//g
                = inv1*g>>L//g + r1>>L//g
                = (inv1>>L<<L + low L inv1)*g>>L//g + r1>>L//g
                = inv1>>L<<L*g>>L//g + (low L inv1)*g>>L//g + r1>>L//g
                = inv1>>L + (low L inv1)*g>>L//g + r1>>L//g
                = inv1>>L + r1>>L//g
                = inv1>>L
                = f//g>>L
    ----------------- done -----------------

(T3-2)[g !=0][deg g >= m][dL = max 0 (deg f+m - 2*deg g)]
    ==>> [div (f>>dL) g = div (f>>dL>>m) (g>>m)]
    # (T3-1)
    ==>> [div f g >>dL = div (f>>dL>>m) (g>>m)]
    [m <= 0]
        right = div (f>>dL <<(-m)) (g <<(-m)) = div (f>>dL) g = left
    [len f < len g]
        left = 0 = right
    [deg f >= deg g >= m > 0][deg f+m - 2*deg g > 0] # using (deg f) # f!=0
        dL > 0
        dL - deg f = m - 2*deg g <= -deg g < 0 # deg g>=m>0
        f_ = f>>dL != 0
        deg f_ = deg f - dL > 0
        dL_ = deg f_ + m - 2*deg g = dL - dL = 0
        f_>>dL_ = f>>dL
        (see below) by (T3-2):
            [g !=0][deg g >= m][dL_ = max 0 (deg f_+m - 2*deg g) = 0]
            ==>> [div (f_>>dL_) g = div (f_>>dL_>>m) (g>>m)]
            ==>> [div (f>>dL) g = div (f>>dL>>m) (g>>m)]
    [deg f >= deg g >= m > 0][deg f+m - 2*deg g <= 0] # using (deg f) # f!=0
        dL = 0
        left = div f g = inv1
        right = div (f>>m) (g>>m) = inv2
        # to prove: deg (f - (f>>m)//(g>>m)*g) < deg g
        f = (f//g)*g + f%g = inv1 * g + r1
        f>>m = (f>>m)//(g>>m) + (f>>m)%(g>>m) = inv2 * (g>>m) + r2
        f = f>>m<<m + low m f
            = (inv2*(g>>m)+r2) << m + low m f
            = inv2*(g>>m)<<m + r2<<m + low m f
            = inv2*(g - low m g) + r2<<m + low m f
            = inv2*g - (inv2 * low m g) + r2<<m + low m f
        f - inv2*g = -(inv2 * low m g) + r2<<m + low m f
        deg inv2 = deg (f>>m) - deg (g>>m) = deg f - deg g = deg inv1 # deg f >= deg g >= m
        deg (low m f) = m-1 = deg (low m g) # deg f >= m; deg g >= m; m > 0
        deg (f-inv2*g)
            <= max [deg (inv2 * low m g), deg (r2<<m), deg (low m f)]
            = max [deg inv2 + deg (low m g), deg (r2<<m), deg (low m f)]
            <= max [deg f - deg g + m-1, deg (r2<<m), m-1]
            <= max [deg f - deg g + m-1, deg (r2<<m)]
        [deg g > m]
            deg (g>>m) = deg g - m > 0 # deg g > m
            deg r2 <= deg (g>>m) - 1 = deg g - m - 1
            deg (f-inv2*g)
                <= max [deg f - deg g + m-1, deg (r2<<m)]
                <= max [deg f - deg g + m-1, deg r2 + m]
                <= max [deg f - deg g + m-1, deg g - m - 1 + m]
                = max [deg f - deg g + m-1, deg g - 1]
                = deg g - 1 + max [deg f - 2*deg g + m, 0]
                # deg f+m - 2*deg g <= 0
                = deg g - 1
            inv2 = inv1
        [deg g == m]
            deg (g>>m) = 0
            r2 = 0
            deg (r2>>m) = 0
            deg (f-inv2*g)
                <= max [deg f - deg g + m-1, deg (r2<<m)]
                <= max [deg f - deg g + m-1, 0]
                # deg f >= deg g ; m > 0
                = deg f - deg g + m-1
                = (deg f + m - 2*deg g) + deg g - 1
                # deg f+m - 2*deg g <= 0
                <= deg g - 1
        deg (f-inv2*g) <= deg g - 1 < deg g
        inv2 = f//g = inv1
    --------------------------- done ----------------------

(T4) [len g > L >= 0] ==>> [inv2 (g>>L) == inv2 g >> L]
    # proof1:
    inv2 (g>>L) =[def]= (1<<(2*deg g -2*L)) //(g>>L)
        == (1<<(2*deg g -L)) //g
        =[(T1)]= (1<<(2*deg g -L))*(1<<(2*deg g) //g)  >>(2*deg g)
        =[def]= (1<<(2*deg g -L))*inv2 g  >>2*(deg g)
        == inv2 g  >>L
    # proof 2:
    let f = 1<<(2*deg g); m = L <= deg g
    by (T3-2) # dL = deg f +m -2*deg g = m = L >= 0
        (T3-2)[g !=0][deg g >= m][dL = max 0 (deg f+m - 2*deg g)]
            ==>> [div f g >>dL = div (f>>dL>>m) (g>>m)]
            ==>> [inv2 g >>L = div (f>>(2*L)) (g>>L)]
            ==>> [inv2 g >>L = inv2 (g>>L)]
(T4-ERROR-1) [len g >= len h > 0] ==>>? [f//(g//h) == (f*h)//g]
    f//(g//h) = (f*h) // (g//h *h) = (f*h) // (g - g%h) != (f*h)//g
    # g = x+1; h=x; f=x
    # g//h = 1; f//(g//h)=x; f*h//g=x^2//(x+1) = x-1
(T4-ERROR-2) [len g >= len h > 0] ==>>? [(f//h)//(g//h) == f//g]
    left = (f//h*h)//(g//h*h) = (f-f%h)//(g-g%h) != f//g

    --------------------------- done ----------------------

'''




















__all__ = '''
    IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops
        IUnivariatePolynomialOverField_Ops
            IUnivariatePolynomialOverField_DegCoefPairsLE_Ops
                UnivariatePolynomialOverRationalField_DegCoefPairsLE_Ops
    UnivariatePolynomialOverFieldOps2ModRingOps
    '''.split()

from itertools import chain
from abc import ABCMeta, abstractmethod
from collections import defaultdict
from seed.algo.sort_ints import sort_seqs_by_key_at
from seed.types.Heap import HeapWithKey
from nn_ns.math_nn.ops.IPowers import IPowers
from nn_ns.math_nn.ops.IRingOps import \
    ( IFieldOps
    , TheRationalFieldOps
    , IEuclideanDomainOps
    , EuclideanDomainOps2ModularGcdDomainOps
    , ICommutativeRingWithIdentityOps
    )


def global_replace_x_powers(self, m, f, deg2poly):
    # m = max len of {output polynomial} + {deg2poly[deg] | deg}
    # return f.replace(x^deg = deg2poly[deg] for all deg)
    # for linear-transform, e.g. f^characteristic
    # assert isinstance(self, IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops)
    ls = []
    for deg, coef in self.iter_degree_nonzero_coefficient_pairsXE(f):
        g = deg2poly[deg]
        assert self.len(g) <= m
        g = self.mul_scale(g, coef)
        ls.append(g)
    r = self.sum(ls)
    assert self.len(r) <= m
    return r

def global_eval__X_is_coef(self, f, x, x_powers):
    # assert isinstance(self, IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops)
    assert isinstance(x_powers, IPowers)
    ops = self.get_coefficient_ring_ops()
    assert ops.is_element(x)
    cz = ops.zero # coef zero, not polynomial zero
    if self.is_the_zero_polynomial(f):
        return cz
    if ops.is_zero(x):
        f = self.low(1, f)
        return self.get_leading_coefficient__maybe0(f)
    if ops.is_one(x):
        it = self.iter_degree_nonzero_coefficient_pairs__arbitrary(f)
        snd = lambda pair: pair[1]
        coefs = map(snd, it)
        return ops.sum(coefs)
    if ops.is_neg_one(x):
        it = self.iter_degree_nonzero_coefficient_pairs__arbitrary(f)
        even = []
        odd = []
        for deg, coef in it:
            ls = odd if deg & 1 else even
            ls.append(coef)
        return ops.sub(ops.sum(even), ops.sum(odd))
    it = self.iter_degree_nonzero_coefficient_pairsBE(f)
    for deg0, LC in it:break
    else: raise logic-error
    add = ops.add
    mul = ops.mul
    for deg1, coef1 in it:
        # f(x) = LC*x^deg0 + coef1*x^deg1 + poly(it)
        # f(x) = (LC*x^(deg0-deg1) + coef1)*x^deg1 + poly(it)
        # LC := LC*x^(deg0-deg1) + coef1; deg0:=deg1
        LC = add(coef1, mul(LC, x_powers[deg0-deg1]))
        deg0 = deg1

    # f(x) == LC*x^deg0
    fx = mul(LC, x_powers[deg0]) if deg0 else LC
    return fx
def global_eval(polynomial_nonzero_termsBE, x, coef2X, add_coef_X, mul_coef_X, X_ring_ops, x_powers):
    # assert isinstance(x_powers, IPowers)
    # polynomial_nonzero_termsBE :: Iterable (Deg, NonZeroCoef)
    # coef_ring_ops != X_ring_ops
    #   polynomial add/mul use coef_ring_ops
    #   but polynomial eval use X_ring_ops/mul_coef_X
    # f = LC * x^deg + a * x^da + b * x^db ... = (LC*x^(deg-da) + a)*x^da + ...
    # return global_eval__X_is_coef(map(lambda d_c: (d_c[0], coef2X(d_c[1])), polynomial_nonzero_termsBE), x, X_ring_ops, x_powers)
    it = iter(polynomial_nonzero_termsBE)
    for deg0, LC in it: break
    else:
        # f == 0
        return X_ring_ops.zero
    for deg1, coef1 in it: break
    else:
        # f = LC*x^deg0
        if deg0 == 0: return coef2X(LC)
        return mul_coef_X(LC, x_powers[deg0])

    # leading X := LC*x^(deg0-deg1) + coef1
    LX = add_coef_X(coef1, mul_coef_X(LC, x_powers[deg0-deg1]))
    deg0 = deg1
    mulX = X_ring_ops.mul
    for deg1, coef1 in it:
        # leading X := LX*x^(deg0-deg1) + coef1
        LX = add_coef_X(coef1, mulX(LX, x_powers[deg0-deg1]))
        deg0 = deg1

    # f(x) == LX*x^deg0
    fx = LX if deg0 == 0 else mulX(LX, x_powers[deg0])
    return fx

def global_product_low(self, m, fs):
    # return self.low(m, self.product(fs))
    assert m >= 0
    z = self.get_the_zero_polynomial()
    # m is the max len of output
    if m < 1: return z
    fs = tuple(fs)
    L = len(fs)
    if L < 2:
        if not L: return self.get_the_one_polynomial()
        f, = fs
        return self.low(m, f)
    del L
    if any(map(self.is_the_zero_polynomial, fs)): return z
    total_ndeg = sum(map(self.ndeg, fs))
    if total_ndeg >= m: return z
    pad = total_ndeg

    # product_low m fs = product_low (m-pad) (fs>>pad) <<pad
    # (m-1) is the max degree of output
    if sum(map(self.deg, fs)) <= m-1: return global_product(self, fs)
    fs = map(lambda f: self.low(m,f), fs)
    fs = map(lambda f: self.rshift_ndeg(f)[0], fs)
    m -= total_ndeg
    fs = map(lambda f: self.low(m,f), fs)
    fs = tuple(fs)
    assert not any(map(self.is_the_zero_polynomial, fs))
    # (m-1) is the max degree of output
    if sum(map(self.deg, fs)) <= m-1: return global_product(self, fs)

    it = map(self.to_degree2nonzero_coefficient, fs)
    deg2coef_heap = HeapWithKey(len, it); del it

    # choose polynomials with only one term
    coef_ops = self.get_coefficient_ring_ops()
    lhs_deg2coef = _product_one_term_polynomials(coef_ops.product, deg2coef_heap)

    # product lhs_deg2coef deg2coef_heap
    is_zero = coef_ops.is_zero
    coef_mul = coef_ops.mul
    coef_sum = coef_ops.sum
    while deg2coef_heap:
        rhs_deg2coef = deg2coef_heap.pop()
        # lhs *= rhs
        lhs_deg2coef = _global_mul_low(coef_sum, coef_mul, m, lhs_deg2coef, rhs_deg2coef)
        _remove_zero_coefficients(is_zero, lhs_deg2coef) # inplace

        # let lhs_deg2coef be the shortest polynomial
        lhs_deg2coef = deg2coef_heap.push_then_pop(lhs_deg2coef)
    r = self.make_polynomial_from_degree2coefficient(lhs_deg2coef)
    return self.lshift(pad, r)

def global_product_mod(self, fs, g, *, may_invGE2_g=()):
    # reorder <<== commutative
    # product_mod([], M) <<== identity
    # product_mod([], M) <<== divmod
    # assert isinstance(self, IUnivariatePolynomialOverField_Ops)
    assert not self.is_the_zero_polynomial(g)
    Dg = self.deg(g)
    if Dg == 0: return self.get_the_zero_polynomial()
    fs = tuple(fs)
    L = len(fs)
    if L == 0:
        # since deg g > 0
        return self.get_the_one_polynomial()
    if L == 1:
        f, = fs
        return self.mod(f, g, may_invGE2_g=may_invGE2_g)
    del L
    if any(map(self.is_the_zero_polynomial, fs)):
        return self.get_the_zero_polynomial()
    if self.has_only_one_nonzero_term(g):
        # g = (1<<Dg)*LC ; Dg > 0
        r = self.product_low(Dg, fs)
        # LC = self.get_leading_coefficient__maybe0(g)
        #bug: r = self.div_scale(r, LC)
        return r



    # product fs % g == ((product fs >> pad) % (g >> pad)) << pad
    total_ndeg = 0
    rshift_ndeg = self.rshift_ndeg
    fs_ = fs
    fs = []
    for f in fs_:
        f, ndeg = rshift_ndeg(f)
        total_ndeg += ndeg
        fs.append(f)
    del fs_
    pad = min(total_ndeg, self.ndeg(g))
    if pad:
        g = self.rshift(pad, g)
        Dg = self.deg(g)
        assert Dg > 0
        total_ndeg -= pad
    # should put (1<<total_ndeg) into fs
    for idx, f in enumerate(fs):
        if self.len(f) > 1:
            fs[idx] = self.lshift(total_ndeg, f)
            break
    else:
        fs.append(self.lshift_one(total_ndeg))



    # result = (fs % g) << pad
    inv2_g = self.extract_may_invGE2_g(g, may_invGE2_g)
    may_invGE2_g = (inv2_g,)
        # since may_invGE2_g may be () or g rshift
        # cache may_invGE2_g here
    fs = self.mods(fs, g, may_invGE2_g=may_invGE2_g)
    if any(map(self.is_the_zero_polynomial, fs)):
        return self.get_the_zero_polynomial()

    it = map(self.to_degree2nonzero_coefficient, fs)
    deg2coef_heap = HeapWithKey(len, it); del it

    # choose polynomials with only one term
    coef_ops = self.get_coefficient_ring_ops()
    lhs_deg2coef = _product_one_term_polynomials(coef_ops.product, deg2coef_heap)

    # product lhs_deg2coef deg2coef_heap
    def mod_(deg2coef):
        f = self.make_polynomial_from_degree2coefficient(deg2coef)
        f = self.mod(f, g, may_invGE2_g=may_invGE2_g)
        return f
    def mod(deg2coef):
        f = mod_(deg2coef)
        return self.to_degree2nonzero_coefficient(f)
    is_zero = coef_ops.is_zero
    coef_mul = coef_ops.mul
    coef_sum = coef_ops.sum
    Lg2 = self.len(g)*3 //2
        # compare Lg with (len(deg2coef)) though not the same concept
        # len(deg2coef) tell how hard to mul
    while deg2coef_heap:
        rhs_deg2coef = deg2coef_heap.pop()
        # lhs *= rhs
        lhs_deg2coef = _global_mul(coef_sum, coef_mul, lhs_deg2coef, rhs_deg2coef)
        _remove_zero_coefficients(is_zero, lhs_deg2coef) # inplace
        if len(lhs_deg2coef) > Lg2:
            lhs_deg2coef = mod(lhs_deg2coef)

        # let lhs_deg2coef be the shortest polynomial
        lhs_deg2coef = deg2coef_heap.push_then_pop(lhs_deg2coef)
    r = mod_(lhs_deg2coef)
    return self.lshift(pad, r)
# end of global_product_mod



def _product_one_term_polynomials(coef_product, deg2coef_heap):
    one_term__degs = []
    one_term__coefs = []
    while deg2coef_heap:
        deg2coef = deg2coef_heap.peek()
        if len(deg2coef) > 1: break
        (deg, coef), = deg2coef.items()
        one_term__degs.append(deg)
        one_term__coefs.append(coef)
        deg2coef_heap.pop()
    # product one_term_ls
    one_term__deg = sum(one_term__degs)
    one_term__coef = coef_product(one_term__coefs)
    deg2coef = {one_term__deg:one_term__coef}
    return deg2coef
def global_product(self, fs):
    # reorder <<== commutative
    # product([]) <<== identity
    # assert isinstance(self, IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops)
    fs = tuple(fs)
    L = len(fs)
    if L < 2:
        if not L:
            return self.get_the_one_polynomial()
        f, = fs
        return f
    if any(map(self.is_the_zero_polynomial, fs)):
        return self.get_the_zero_polynomial()

    it = map(self.to_degree2nonzero_coefficient, fs)
    deg2coef_heap = HeapWithKey(len, it); del it

    # choose polynomials with only one term
    coef_ops = self.get_coefficient_ring_ops()
    lhs_deg2coef = _product_one_term_polynomials(coef_ops.product, deg2coef_heap)

    # product lhs_deg2coef deg2coef_heap
    is_zero = coef_ops.is_zero
    coef_mul = coef_ops.mul
    coef_sum = coef_ops.sum
    while deg2coef_heap:
        rhs_deg2coef = deg2coef_heap.pop()
        # lhs *= rhs
        lhs_deg2coef = _global_mul(coef_sum, coef_mul, lhs_deg2coef, rhs_deg2coef)
        _remove_zero_coefficients(is_zero, lhs_deg2coef) # inplace

        # let lhs_deg2coef be the shortest polynomial
        lhs_deg2coef = deg2coef_heap.push_then_pop(lhs_deg2coef)
    return self.make_polynomial_from_degree2coefficient(lhs_deg2coef)


    ############# old version
    f = fs[0]
    iter_XE = self.iter_degree_nonzero_coefficient_pairsXE
    for g in fs[1:]:
        ls = []
        for d,c in iter_XE(g):
            s = self.lshift(d, self.mul_scale(f,c))
            ls.append(s)
        f = self.sum(ls)
    return self.sum(ls)
# end of global_product

def global_sum(self, fs):
    # sum([]) <<== ring??
    # assert isinstance(self, IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops)
    fs = tuple(fs)
    L = len(fs)
    if L < 2:
        if not L:
            return self.get_the_zero_polynomial()
        f, = fs
        return f
    ops = self.get_coefficient_ring_ops()
    add = ops.add
    deg2coef = {}
    iter_pairs =self.iter_degree_nonzero_coefficient_pairs__arbitrary
    for f in fs:
        for d,c in iter_pairs(f):
            _global_iadd(add, deg2coef, d, c)
    return self.make_polynomial_from_degree2coefficient(deg2coef)


def _remove_zero_coefficients(is_zero, deg2coef):
    # since zero coefficients are rare, we modify inplace
    degs = [deg for deg, coef in deg2coef.items() if is_zero(coef)]
    for deg in degs: del deg2coef[deg]

class _Deg2Coefs:
    def __init__(self):
        self.deg2coefs = defaultdict(list)
    def put(self, deg, coef):
        self.deg2coefs[deg].append(coef)
    def to_deg2coef(self, coef_sum):
        deg2coef = {deg:coef_sum(coefs)
                    for deg, coefs in self.deg2coefs.items()}
        return deg2coef
def _global_mul_low(coef_sum, coef_mul, m, lhs_deg2coef, rhs_deg2coef):
    # donot remove zero
    assert 0 < len(lhs_deg2coef) <= len(rhs_deg2coef) <= m
    deg2coefs = _Deg2Coefs()
    # LE
    lhs_pairs = sort_seqs_by_key_at(0, lhs_deg2coef.items())
    rhs_pairs = sort_seqs_by_key_at(0, rhs_deg2coef.items())
    assert 0 == lhs_pairs[0][0] and lhs_pairs[-1][0] < m
    assert 0 == rhs_pairs[0][0] and rhs_pairs[-1][0] < m
    for lhs_deg, lhs_coef in lhs_pairs:
        for rhs_deg, rhs_coef in rhs_pairs:
            deg = lhs_deg + rhs_deg
            if deg >= m: break
            deg2coefs.put(deg, coef_mul(lhs_coef, rhs_coef))
    deg2coef = deg2coefs.to_deg2coef(coef_sum)
    return deg2coef

def _global_mul(coef_sum, coef_mul, lhs_deg2coef, rhs_deg2coef):
    # donot remove zero
    assert len(lhs_deg2coef) <= len(rhs_deg2coef)
    deg2coefs = _Deg2Coefs()
    for lhs_deg, lhs_coef in lhs_deg2coef.items():
        for rhs_deg, rhs_coef in rhs_deg2coef.items():
            deg2coefs.put(lhs_deg+rhs_deg, coef_mul(lhs_coef, rhs_coef))
    deg2coef = deg2coefs.to_deg2coef(coef_sum)
    return deg2coef

def _global_iadd(add, deg2coef, deg, coef):
    # donot remove zero
    # assert isinstance(ops, IUnivariatePolynomialOverField_Ops)
    nothing = []
    may_coef = deg2coef.get(deg, nothing)
    if may_coef is nothing:
        deg2coef[deg] = coef
    else:
        deg2coef[deg] = add(coef, may_coef)

# polynomial
class IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops(ICommutativeRingWithIdentityOps):
    '''
get_coefficient_ring_ops() -> ICommutativeRingWithIdentityOps
'''
    '''
get_coefficient_ring_ops() -> IFieldOps

XE is LE or BE depended by self. should not random
    LE - little-endian; BE - big-endian; term degree inc/dec

iter_degree_nonzero_coefficient_pairsXE <<== is_XE_LE
    len/deg/may_deg
        <<== get_may_leading_nonzero_term
        <<== iter_degree_nonzero_coefficient_pairsBE
    ndeg/may_ndeg
        <<== get_may_lowest_nonzero_term
        <<== iter_degree_nonzero_coefficient_pairsLE
    they should be as fast as possible

to override:
    get_coefficient_ring_ops
    __untypecheck_make_polynomial_from_degree_coefficient_pairsLE__
    __untypecheck_make_polynomial_from_degree_coefficient_pairsBE__
    is_XE_LE
    iter_degree_nonzero_coefficient_pairsLE
    iter_degree_nonzero_coefficient_pairsBE
    iter_degree_nonzero_coefficient_pairs__arbitrary
    get_may_leading_nonzero_term
    get_may_lowest_nonzero_term
    len/may_ndeg
    product # to reorder the mul order and use divide and conquer method
    rshift/rshift_low/low/low_opposite
    mul_low/mul_low_opposite/mul_rshift
    pow_uint

may_deg = None | degree
may_term = None | (degree, coefficient)

############# types
Deg = UInt
Coef < IFieldOps
NonZeroCoef = Coef\\{0}
Term = (Deg, Coef)
NonZeroTerm = (Deg, NonZeroCoef)
TermsLE = [Term] where deg increase strictly
TermsBE = [Term] where deg decrease strictly
'''
    @abstractmethod
    # should be nn_ns.math_nn.ops.IRingOps.IFieldOps
    def get_coefficient_ring_ops(self):pass
    @abstractmethod
    def iter_degree_nonzero_coefficient_pairsLE(self, f):pass
    @abstractmethod
    def iter_degree_nonzero_coefficient_pairsBE(self, f):pass
    @abstractmethod
    def __untypecheck_make_polynomial_from_degree_coefficient_pairsLE__(
        self, pairs:'NonZeroTerm LE tuple'):pass
    @abstractmethod
    def __untypecheck_make_polynomial_from_degree_coefficient_pairsBE__(
        self, pairs:'NonZeroTerm BE tuple'):pass
    def is_XE_LE(self):
        # XE is LE or BE depended by self. should not random
        return True




    def make_polynomial_from_degree_coefficient_pairsLE(self, pairs:'iterable'):
        # degree should be nonnegative integer
        # allow zero coefficients
        # should be little-endian, no duplicated degree
        pairs = self.typecheck_std_degree_coefficient_pairsXE(True, pairs)
        return self.__untypecheck_make_polynomial_from_degree_coefficient_pairsLE__(pairs)
    def make_polynomial_from_degree_coefficient_pairsBE(self, pairs:'iterable'):
        pairs = self.typecheck_std_degree_coefficient_pairsXE(False, pairs)
        return self.__untypecheck_make_polynomial_from_degree_coefficient_pairsBE__(pairs)
    def typecheck_std_degree_coefficient_pairsXE(self, is_XE_LE, pairs:'iterable'):
        # is_XE_LE -> Iter (Deg,Coef) -> Tuple (Deg, NonZeroCoef)
        ops = self.get_coefficient_ring_ops()
        is_zero = ops.is_zero
        is_element = ops.is_element
        pairs = tuple(pairs)
        if not all(type(deg) is int for deg,coef in pairs):raise TypeError
        if not all(deg >= 0 for deg,coef in pairs):raise TypeError
        if not all(is_element(coef) for deg,coef in pairs):raise TypeError
        pairs = tuple((d,c) for d,c in pairs if not is_zero(c))
        if is_XE_LE:
            # LE
            if not all(d < d_ for (d,_), (d_,_) in zip(pairs, pairs[1:])): raise TypeError('not little-endian')
        else:
            # BE
            if not all(d > d_ for (d,_), (d_,_) in zip(pairs, pairs[1:])): raise TypeError('not big-endian')
        return pairs

    def make_polynomial_from_degree2coefficient(self, deg2coef):
        ops = self.get_coefficient_ring_ops()
        is_zero = ops.is_zero
        pairs = ((d,c) for d,c in deg2coef.items() if not is_zero(c))
        if self.is_XE_LE():
            # LE
            pairsXE = sort_seqs_by_key_at(0, pairs)
        else:
            # BE
            pairsXE = sort_seqs_by_key_at(0, pairs, key=lambda i: -i)
        return self.make_polynomial_from_degree_coefficient_pairsXE(pairsXE)
    def iter_degree_nonzero_coefficient_pairs__arbitrary(self, f):
        # to be overrided
        # e.g. when f :: {sorted_degs::[Deg], deg2nonzero_coef::Map Deg NonZeroCoef}
        #   this_func f = (deg2nonzero_coef f).items()
        return self.iter_degree_nonzero_coefficient_pairsXE(f)
        return self.to_degree2nonzero_coefficient().items()
    def to_degree2nonzero_coefficient(self, f):
        return dict(self.iter_degree_nonzero_coefficient_pairs__arbitrary(f))
    @property
    def iter_degree_nonzero_coefficient_pairsXE(self):
        if self.is_XE_LE():
            return self.iter_degree_nonzero_coefficient_pairsLE
        return self.iter_degree_nonzero_coefficient_pairsBE
    @property
    def make_polynomial_from_degree_coefficient_pairsXE(self):
        if self.is_XE_LE():
            return self.make_polynomial_from_degree_coefficient_pairsLE
        return self.make_polynomial_from_degree_coefficient_pairsBE
    def is_monic_polynomial(self, f):
        LC = self.get_leading_coefficient__maybe0(f)
        ops = self.get_coefficient_ring_ops()
        return ops.is_one(LC)
    def get_leading_coefficient__maybe0(self, f):
        # may be zero
        may_term = self.get_may_leading_nonzero_term(f)
        if may_term is None:
            ops = self.get_coefficient_ring_ops()
            return ops.zero
        deg, LC = may_term
        return LC
    def get_may_leading_nonzero_term(self, f):
        # SHOULD BE
        for term in self.iter_degree_nonzero_coefficient_pairsBE(f):
            return term
        return None
    def get_may_lowest_nonzero_term(self, f):
        # SHOULD LE
        for term in self.iter_degree_nonzero_coefficient_pairsLE(f):
            return term
        return None
    def has_only_one_nonzero_term(self, f):
        # deg f == ndeg f
        L = self.len(f)
        if not L: return False
        return L-1 == self.ndeg(f)
    def get_the_only_nonzero_term(self, f):
        # deg f == ndeg f
        [deg_coef] = self.iter_degree_nonzero_coefficient_pairs__arbitrary(f)
        return deg_coef
    def make_polynomial_from_degree_coefficient(self, deg, coef):
        return self.make_polynomial_from_degree_coefficient_pairsXE([(deg, coef)])

    def extract_degrees_nonzero_coefficients_XE(self, x):
        degsX, coefsX = [], []
        iter_XE = self.iter_degree_nonzero_coefficient_pairsXE
        for d,c in iter_XE(x):
            degsX.append(d)
            coefsX.append(c)
        return degsX, coefsX
    def element_equal(self, x, y):
        if self.len(x) != self.len(y): return False
        if self.is_the_zero_polynomial(x): return True
        if self.ndeg(x) != self.ndeg(y): return False
        get = self.extract_degrees_nonzero_coefficients_XE
        degsX, coefsX = get(x)
        degsY, coefsY = get(y)
        if degsX != degsY: return False
        ops = self.get_coefficient_ring_ops()
        return all(map(ops.element_equal, coefsX, coefsY))


    def mul(self, f, g):
        return self.product([f,g])
    def product(self, fs):
        return global_product(self, fs)

    def get_the_one_polynomial(self):
        return self.lshift_one(0)
        ops = self.get_coefficient_ring_ops()
        one = ops.one
        return self.make_polynomial_from_degree_coefficient(0,one)
    def get_the_zero_polynomial(self):
        ops = self.get_coefficient_ring_ops()
        zero = ops.zero
        return self.make_polynomial_from_degree_coefficient(0,zero)
    def sum(self, fs):
        return global_sum(self, fs)

    def neg(self, f):
        ops = self.get_coefficient_ring_ops()
        neg = ops.neg
        def op(deg_coef):
            deg, coef = deg_coef
            return deg, neg(coef)
        return self.make_polynomial_from_degree_coefficient_pairsXE(
            map(op, self.iter_degree_nonzero_coefficient_pairsXE(f)))
    def div_scale(self, f, c):
        ops = self.get_coefficient_ring_ops()
        return self.mul(f, ops.inv(c))
    def mul_scale(self, f, c):
        ops = self.get_coefficient_ring_ops()
        if ops.is_zero(c):
            return self.get_the_zero_polynomial()
        def op(deg_coef):
            deg, coef = deg_coef
            coef = ops.mul(coef, c)
            return deg, coef
        return self.make_polynomial_from_degree_coefficient_pairsXE(
            map(op, self.iter_degree_nonzero_coefficient_pairsXE(f)))

    def rshift(self, m, f):
        if m == 0: return f
        def ipair():
            # SHOULD BE
            for d,c in self.iter_degree_nonzero_coefficient_pairsBE(f):
                if d < m: break
                yield (d-m, c)
        # SHOULD BE
        return self.make_polynomial_from_degree_coefficient_pairsBE(ipair())
    def lshift(self, m, f):
        return self.rshift(-m, f)

    def sub(self, f, g):
        return self.add(f, self.neg(g))
    def add(self, f, g):
        return self.sum([f,g])
    def is_the_zero_polynomial(self, f):
        return self.len(f) == 0
    def len(self, f):
        # SHOULD BE
        may_term = self.get_may_leading_nonzero_term(f)
        if may_term is None: return 0
        d, _ = may_term
        return d+1
    def ndeg(self, f):
        may_deg = self.may_ndeg(f)
        if may_deg is None: raise NoDegree
        return may_deg
    def deg(self, f):
        may_deg = self.may_deg(f)
        if may_deg is None: raise NoDegree
        return may_deg
    def may_ndeg(self, f):
        # SHOULD LE
        may_term = self.get_may_lowest_nonzero_term(f)
        if may_term is None: return None
        d, _ = may_term
        return d
    def may_deg(self, f):
        L = self.len(f)
        if not L: return None
        return L-1

    def concatBE(self, fs):
        fs = [f for f in fs if not self.is_the_zero_polynomial(f)]
        if not all(self.ndeg(f) > self.deg(g) for f, g in zip(fs, fs[1:])):
            raise ValueError('f++g requires ndeg f > deg g')
        if self.is_XE_LE():
            fs = reversed(fs) # concatBE that is the BE
        return self.make_polynomial_from_degree_coefficient_pairsXE(
                chain.from_iterable(map(
                    self.iter_degree_nonzero_coefficient_pairsXE, fs)))



    def low(self, m, f):
        # [m >= 0] ==>> [len(low m f) <= m]
        assert m >= 0
        # return self.sub(f, self.low_opposite(m, f))
        if self.len(f) <= m: return f
        def ilow():
            # SHOULD LE
            for d, c in self.iter_degree_nonzero_coefficient_pairsLE(f):
                if d < m: yield (d,c)
                else:     break
        return self.make_polynomial_from_degree_coefficient_pairsLE(ilow())
    def rshift_ndeg(self, f):
        may_ndeg = self.may_ndeg(f)
        if may_ndeg is None or may_ndeg == 0: return f, 0
        return self.rshift(ndeg, f), may_ndeg

    def rshift_low(self, m, f):
        assert m >= 0
        # return self.rshift(m, f), self.low(m, f)
        # SHOULD BE
        make = self.make_polynomial_from_degree_coefficient_pairsBE
        it = self.iter_degree_nonzero_coefficient_pairsBE(f)
        #it = iter(it)
        low = []
        rshift = []
        for d, c in it:
            if d < m:
                low.append((d,c))
                break
            else:
                rshift.append((d-m, c))
        low.extend(it)
        return make(rshift), make(low)

    def low_opposite(self, m, f):
        assert m >= 0
        return self.lshift(m, self.rshift(m, f))
        return self.sub(f, self.low(m, f))
    def lead(self, m, f):
        # [0 <= m <= len(f)]
        assert m >= 0
        assert m <= self.len(f)
        L = self.len(f)
        L_low = L - m
        return self.low_opposite(L_low, f)
    def product_low(self, m, fs):
        return global_product_low(self, m, fs)
    def mul_low(self, m, f, g):
        # return self.low(m, self.mul(f, g))
        return self.product_low(m, [f,g])
        ######### old version
        assert m >= 0
        if m == 0 or self.is_the_zero_polynomial(f) or self.is_the_zero_polynomial(g):
            return self.get_the_zero_polynomial()
        # (m-1) is the max degree of output
        M = m-1
        if M >= self.deg(f) + self.deg(g):
            return self.mul(f, g)
        Nf = self.ndeg(f)
        Ng = self.ndeg(g)
        if M < Nf+Ng: return self.get_the_zero_polynomial()
        Mg = M - Nf
        Mf = M - Ng
        f = self.low(Mf+1, f)
        ls = []
        # SHOULD LE
        for d, c in self.iter_degree_nonzero_coefficient_pairsLE(f):
            Mg = M-d # inc d ==>> dec Mg ==>> dec (len g)
            g = self.low(Mg+1, g)
            s = self.lshift(d, self.mul_scale(g, c))
            ls.append(s)
        return self.sum(ls)

    def mul_low_opposite(self, m, f, g):
        # return self.low_opposite(m, self.mul(f, g))
        assert m >= 0
        if self.is_the_zero_polynomial(f) or self.is_the_zero_polynomial(g):
            return self.get_the_zero_polynomial()
        # m is the min degree of output
        Df = self.deg(f)
        Dg = self.deg(g)
        if m > Df+Dg:
            return self.get_the_zero_polynomial()
        Nf = self.ndeg(f)
        Ng = self.ndeg(g)
        if m <= Nf+Nf:
            return self.mul(f,g)
        mg = m - Df
        mf = m - Dg # min ndeg of valid f term
        f = self.low_opposite(mf, f)
        ls = []
        # SHOULD BE
        for d, c in self.iter_degree_nonzero_coefficient_pairsBE(f):
            mg = m-d # dec d ==>> inc mg ==>> inc (ndeg g)
            g = self.low_opposite(mg, g)
            s = self.lshift(d, self.mul_scale(g, c))
            ls.append(s)
        return self.sum(ls)


    def div_via_mul_inv(self, f, g, invg):
        # invg = inv K g where K = len invg + deg g - 1
        # f//g = (f*inv k g)>>k where k>=len f-1
        # len(inv k g) = max [0, k - deg g + 1]
        assert not self.is_the_zero_polynomial(g)
        Dg = self.deg(g)
        Li = self.len(invg)
        K = Li + Dg - 1
        k = self.len(f) - 1
        if k > K: raise ValueError('invg too short')
        if k < 0: return self.get_the_zero_polynomial()
        minL = max(0, k - Dg+1)
        invg = self.rshift(Li-minL, invg)
        assert self.len(invg) == minL
        return self.mul_rshift(k, f, invg)
    def mul_rshift(self, m, f, g):
        return self.rshift(m, self.mul_low_opposite(m, f, g))

    ##### ICommutativeRingWithIdentityOps abstractmethod
    @property
    def one(self):
        return self.get_the_one_polynomial()
    @property
    def zero(self):
        return self.get_the_zero_polynomial()
    def is_zero(self, x):
        return self.is_the_zero_polynomial(x)
    def int2coefficient(self, i):
        ops = self.get_coefficient_ring_ops()
        return ops.int2element(i)
    def int2element(self, i):
        return self.make_polynomial_from_degree_coefficient(
                    0, self.int2coefficient(i))
    def mul_int(self, f, i):
        c = self.int2coefficient(i)
        return self.mul_scale(f,c)

    def true_div_int(self, x, i):
        tdiv = self.get_coefficient_ring_ops().true_div_int
        return self.make_polynomial_from_degree_coefficient_pairsXE(
            (deg, tdiv(coef,i)) for deg, coef in
                self.iter_degree_nonzero_coefficient_pairsXE(x))
# end of IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops

class IUnivariatePolynomialOverField_Ops(IUnivariatePolynomialOverCommutativeRingWithIdentity_Ops, IEuclideanDomainOps):
    '''
# but may_invGE2_g is not like above
may_invGE2_g = () | (inv2(g)<<L ++ arbitrary_tail,) where
    len arbitrary_tail == L >=0
    extract_may_invGE2_g; inv2 g == inv (2*deg g) g
'''

    def div_lead(self, m, f, g, *, may_invGE2_g=()):
        # [g != 0][0 <= m <= len f +1 - len g] ==>> [div_lead m f g == lead m (div f g)]
        assert not self.is_the_zero_polynomial(g)
        assert m >= 0
        assert 0 <= m <= self.len(f)+1 - self.len(g)
        if m == 0 or self.len(f) < self.len(g):
            return self.get_the_zero_polynomial()
        assert m > 0
        Lf = self.len(f)
        Lg = self.len(g)
        Lq = m = max(0, min(m, Lf+1-Lg))
        leadLf = Lq + Lg - 1
        assert leadLf >= 0
        dL = Lf - leadLf
        q = self.floor_div(self.rshift(dL, f), g, may_invGE2_g=may_invGE2_g)
        assert self.len(q) == Lq
        return self.lshift(dL, q)

    def make_modular_ring_ops(self, g, *, may_invGE2_g=()):
        # return a ring ops, whose modulus is g
        # len ring_element < len g
        assert not self.is_the_zero_polynomial(g)
        return UnivariatePolynomialOverFieldOps2ModRingOps(self, g, may_invGE2_g=may_invGE2_g)
    def pow_mod(self, f, exp, g, *, may_invGE2_g=()):
        # pow_mod f exp g = mod (pow f exp) g
        assert type(exp) is int and exp >= 0
        assert not self.is_the_zero_polynomial(g)
        if exp == 0 or self.len(g)==1:
            return self.get_the_one_polynomial()
        r = self.mod(f, g, may_invGE2_g=may_invGE2_g)
        if self.is_the_zero_polynomial(r): return r
        if exp == 1: return r
        mod_ops = self.make_modular_ring_ops(g, may_invGE2_g=may_invGE2_g)
        return mod_ops.pow_uint(r, exp)

        '''
        Dr12 = deg (r1^2) = 2*deg r1 <= 2*(deg g - 1) = L
        # r2 may be 0; e.g. r1^2 == g
        len r2 <= min [Dg, Dr12+1] = maxLr2
        f = r1^2
        r2 = low maxLr2 f - mul_low maxLr2 (mul_rshift Dr12 f (invg>>(L-Dr12))) g
        '''


    def product_mod(self, fs, g, *, may_invGE2_g=()):
        # product_mod fs g = mod (product fs) g
        return global_product_mod(fs, g, may_invGE2_g=may_invGE2_g)
        ###### old version
        assert not self.is_the_zero_polynomial(g)
        z = self.get_the_zero_polynomial()
        if self.len(g) == 1: return z
        fs = tuple(fs)
        if any(self.is_the_zero_polynomial, fs): return z

        rs = self.mods(fs, g, may_invGE2_g=may_invGE2_g)
        L = len(rs)
        if L == 1: return rs[0]
        if L == 0: return self.get_the_one_polynomial()
        if any(self.is_the_zero_polynomial, rs): return z
        mod_ops = self.make_modular_ring_ops(g, may_invGE2_g=may_invGE2_g)
        return mod_ops.product(rs)
    def mods(self, fs, g, *, may_invGE2_g=()):
        assert not self.is_the_zero_polynomial(g)
        fs = tuple(fs)
        Lg = self.len(g)
        if Lg < 2:
            if Lg < 1: raise ZeroDivisionError
            # g is constant scale
            z = self.get_the_zero_polynomial()
            return (z,)*len(fs)
        if self.has_only_one_nonzero_term(g):
            max_len = Dg = self.deg(g)
            return tuple(map(lambda f: self.low(max_len, f), fs))

        ss = [] # short
        ls = [] # long
        for idx, f in enumerate(fs):
            s = ss if self.len(f) < Lg else ls
            s.append((idx,f))
        if not ls: return fs
        qs, rs = self.divmods(ls, g, may_invGE2_g=may_invGE2_g)

        ls = rs
        nothing = []
        rs = [nothing]*len(fs)
        for s in [ss, ls]:
            for idx, f in s: rs[idx] = f
        assert all(r is not nothing for r in rs)
        assert len(rs) == len(ls)+len(ss)
        rs = tuple(rs)
        return rs
    def mod(self, f, g, *, may_invGE2_g=()):
        r, = self.mods([f], g, may_invGE2_g=may_invGE2_g)
        return r
    def divmods(self, fs, g, *, may_invGE2_g=()):
        # divmods fs g = (floor_divs fs g, mods fs g)
        fs = tuple(fs)
        qs = self.floor_divs(fs,g, may_invGE2_g=may_invGE2_g)
        Dg = self.deg(g)
        rs = tuple(self.sub(self.low(Dg, f), self.mul_low(Dg, q,g))
                    for q,f in zip(qs,fs))
        return qs, rs
        r = self.sub(f, self.mul(q,g))
    def divmod(self, f, g, *, may_invGE2_g=()):
        [q], [r] = self.divmods([f], g, may_invGE2_g=may_invGE2_g)
        return q, r
        try:
            assert 0 <= self.len(r) < self.len(g)
            assert self.is_the_zero_polynomial(r) or self.deg(r) < self.deg(g)
        except:
            print(f'{f!s}, {g}')
            print(f'{q!s}, {r}')
            raise
        return q, r

    def floor_divs(self, fs, g, *, may_invGE2_g=()):
        # may_invGE2_g = () | (inv2(g)<<L ++ arbitrary_tail,) where L >=0
        org_fs = fs
        fs = sorted(fs, key=self.len, reverse=True)
        qs = self.__floor_divs__sorted_fs_by_dec_len(fs, g, may_invGE2_g=may_invGE2_g)
        id2q = dict(zip(map(id, fs), qs))
        return tuple(id2q[id(f)] for f in org_fs)
    def __floor_divs__sorted_fs_by_dec_len(self, fs, g, may_invGE2_g):
        # fs are sorted by (-len(f))
        assert not self.is_the_zero_polynomial(g)
        fs = tuple(fs)
        if not fs: return ()

        NDg = self.ndeg(g)
        if NDg > 0:
            rs = lambda f: self.rshift(NDg, f)
            g = rs(g)
            fs = tuple(map(rs, fs))
            NDg = self.ndeg(g)
            del rs
            # return floor_divs(fs, g)
        assert NDg == 0

        Lg = self.len(g)
        assert Lg > 0
        Lfs = tuple(map(self.len, fs))
        assert all(L0 >= L1 for L0,L1 in zip(Lfs, Lfs[1:]))
        MLf = Lfs[0] # max(Lfs)
        z = self.get_the_zero_polynomial()
        if MLf < Lg:
            return (z,)*len(fs)
        MDf = MLf - 1
        invg = self.inv(MDf, g, may_invGE2_g=may_invGE2_g)
        assert self.len(invg) + Lg - 1 == MLf
        # q = self.mul_rshift(Df, f, invg) = div_via_mul_inv(f,g,invg)
        qs = []
        for f,Lf in zip(fs, Lfs):
            assert MLf >= Lf
            if Lf < Lg:
                q = z
                qs += [z] * (len(fs) - len(qs))
                break
            else:
                assert Lf >= Lg > 0
                invg = self.rshift(MLf - Lf, invg)
                MLf = Lf
                assert self.len(invg) + Lg - 1 == MLf
                # f != 0 ==>> deg f
                # f//g = f * inv (deg f) g >> deg f
                q = self.mul_rshift(Lf-1, f, invg)
            qs.append(q)
        assert len(qs) == len(fs)
        return tuple(qs)

    def floor_div(self, f, g, *, may_invGE2_g=()):
        q, = self.floor_divs([f], g, may_invGE2_g=may_invGE2_g)
        return q

    def lshift_one(self, deg):
        # lshift_one(deg) = 1<<deg
        assert deg >= 0
        ops = self.get_coefficient_ring_ops()
        one = ops.one
        return self.make_polynomial_from_degree_coefficient(deg, coef)
    def inv(self, k, g, *, may_invGE2_g=()):
        # inv k g = 1<<k//g
        # may_invGE2_g = () | (inv2(g)<<L ++ arbitrary_tail,) where L >=0
        assert not self.is_the_zero_polynomial(g)
        assert k >= 0
        Lf = k+1
        Lg = self.len(g)
        if Lf < Lg:
            return self.get_the_zero_polynomial()
        ndeg = min(k, self.ndeg(g))
        if ndeg > 0:
            return self.inv(k-ndeg, self.rshift(ndeg, g), may_invGE2_g=may_invGE2_g)
        if Lg == 1:
            return self.lshift(k, self.__inv1(g))

        Lq = Lf - Lg + 1
        assert Lq > 0
        Dg = Lg - 1
        Df = Lf - 1
        dL = 2*Dg - Df
        if dL > 0:
            assert Df < 2*Dg
            # f_ = self.rshift(dL, f)
            k_ = k - dL # = deg f_
            g_ = self.rshift(dL, g)
            # len(g_) = Lg - dL = Lg - 2Dg+Df = Df+1-Dg=Lq
            # len(f_) = Lf - dL = Lf - 2Dg+Df = 2Df+1-2Dg=2*Lq-1
            assert self.len(g_) == Lq > 0
            #assert self.len(f_) == 2*Lq-1 > 0
            #assert self.deg(g_)*2 == self.deg(f_)
            assert k_+1 == 2*Lq-1 > 0
            assert k_ == self.deg(g_)*2
            return self.inv(k_, g_, may_invGE2_g=may_invGE2_g)
        assert k >= self.deg(g)*2
        return self.__inv_long(k, g, may_invGE2_g=may_invGE2_g)
    def __inv_long(self, k, g, may_invGE2_g):
        # may_invGE2_g = () | (inv2(g)<<L ++ arbitrary_tail,) where L >=0
        assert not self.is_the_zero_polynomial(g)
        assert k >= 0
        assert k >= 2*self.deg(g)
        assert self.deg(g) >= 1
        assert self.ndeg(g) == 0
        ##########
        '''
        (T2) [g != 0][L = 2*deg g - 2][invg = (1<<L)//g][
            (invk, r1) == divmod (1<<k) g][(inv2k, r2) == divmod (1<<(2*k)) g
            ] ==>> [inv2k = (invk*g+2*r1)*invk + (r1^2*invg)>>L][
                r2 = r1^2 - ((r1^2*invg)>>L)*g]
        '''
        Dg = self.deg(g) # == deg invk
        kk = 2*Dg
        # invk = self.__inv2(g)
        invk = self.extract_may_invGE2_g(g, may_invGE2_g)
        assert self.deg(invk) == Dg

        r1 = self.neg(self.mul_low(Dg, invk, g))
        #rint('g, invk, r1')
        #rint(g, invk, r1)

        invg = self.rshift(2, invk)
        L = 2*Dg - 2
        # self.len(invg) may be 0
        assert self.len(invg) == L -Dg +1 # bug:self.deg(invg) == L - Dg
        while k > kk:
            r1_2 = self.mul(r1, r1)
            r1_2_invg_high = self.mul_rshift(L, r1_2, invg)
            r2 = self.sub(self.low(L, r1_2), self.mul_low(L, r1_2_invg_high, g))
            invk_g = self.mul(invk, g)
            invk_g_2r1 = self.sum([invk_g, r1, r1])
            invk_g_2r1_invk = self.mul(invk_g_2r1, invk)
            inv2k = self.add(invk_g_2r1_invk, r1_2_invg_high)

            kk += kk
            invk = inv2k
        # r = invk >> d
        # deg r = k - deg g
        # deg r = deg invk - d = kk - deg g - d
        # d = kk - k
        # r = invk >> (kk- k)
        d = kk - k
        return self.rshift(d, invk)
    def __inv1(self, g):
        # inv1 g = 1/g where g = c*x^0
        assert self.len(g) == 1
        (_, c) = self.get_the_only_nonzero_term(g)
        ops = self.get_coefficient_ring_ops()
        inv = ops.inv(c)
        return self.make_polynomial_from_degree_coefficient(0, inv)
    def __inv2(self, g):
        # inv2 g = 1<<(2*deg g) //g
        assert not self.is_the_zero_polynomial(g)
        Dg = self.deg(g)
        if Dg == 0:
            return self.__inv1(g)
        #   m = (deg g + 1)//2 >= 1
        #   gh = g >> m
        #   inv_gh = inv2 gh # deg inv_gh = deg gh = deg g - m
        #   rem_gh = 1<<(2*(deg g - m)) - inv_gh*gh = f>>(2m) - inv_gh*gh
        #          = - mul_low (deg g - m) inv_gh gh
        m = (Dg+1)//2
        assert m >= 1
        gh, _g = self.rshift_low(m, g)
        inv_gh = self.__inv2(gh)
        rem_gh = self.neg(self.mul_low(Dg-m, inv_gh, gh))
        ## g = 3x+3, Dg = 1, m = 1
        ## gh = 3, _g = 3
        ## inv_gh = 1/3, rem_gh = 0
        ##print(f'gh={gh}, _g={_g}, inv_gh={inv_gh}, rem_gh={rem_gh}')

        #   q = q_<<dL ++ _q = inv_gh<<m ++ _q
        #       = inv_gh<<m ++ mul_rshift(2*deg g-2m, rem_gh<<m - inv_gh*(low m g), inv_gh)
        ## _q_1 = 0, _q_2 = 1, _q_12 = -1, _q = -1/3
        ## q = 1/3 x - 1/3
        _q_1 = self.lshift(m, rem_gh)
        _q_2 = self.mul(inv_gh, _g)
        _q_12 = self.sub(_q_1, _q_2)
        _q = self.mul_rshift(2*(Dg-m), _q_12, inv_gh)
        q = self.concatBE([self.lshift(m, inv_gh), _q])
        return q

    def __div1(self, f, g):
        assert self.len(g) == 1
        (_, c) = self.get_the_only_nonzero_term(g)
        return self.div_scale(f, c)


    def extract_may_invGE2_g(self, g, may_invGE2_g):
        # return inv2(g)
        # g != 0
        k = 2*self.deg(g)
        if may_invGE2_g == ():
            # bug: return self.inv(k, g)
            # since this func will used in __inv_long/inv
            return self.__inv2(g)
        invGE2_g, = may_invGE2_g
        # SHOULD remove arbitrary_tail
        # L = len (inv k g) = 1 + deg (1<<k //g) = 1+ k - deg g = 1+deg g = len g
        L = self.len(g)
        L2 = self.len(invGE2_g)
        if L2 == L:
            inv2_g = invGE2_g
        elif L2 > L:
            dL = L2 - L
            inv2_g = self.rshift(dL, invGE2_g)
        else:
            raise ValueError('not may_invGE2_g')
        assert self.len(inv2_g) == L
        return inv2_g


    ##### IEuclideanDomainOps abstractmethod
    def __divmod_nonzero__(self, n, d):
        return self.divmod(n,d)
    def arbitrary_norm_EuclideanDomain(self, x):
        return self.len(x)
# end of IUnivariatePolynomialOverField_Ops



class UnivariatePolynomialOverFieldOps2ModRingOps(EuclideanDomainOps2ModularGcdDomainOps):
    def __init__(self, the_division, the_modulus_polynomial, *, may_invGE2_g=()):
        assert isinstance(the_division, IUnivariatePolynomialOverField_Ops)
        assert the_division.is_element(the_modulus_polynomial)
        assert the_division.len(the_modulus_polynomial) > 0
        ops = the_division
        M = the_modulus_polynomial
        self.inv2_modulus = ops.extract_may_invGE2_g(M, may_invGE2_g)
        super().__init__(ops, M)
    def product(self, fs):
        return self.ops.product_mod(fs, self.modulus
            , may_invGE2_g=(self.inv2_modulus,))
    def __modulo__(self, f):
        return self.ops.mod(f, self.modulus, may_invGE2_g=(self.inv2_modulus,))
    def neg(self, x):
        return (self.ops.neg(x))
        return self.__mod(self.ops.neg(x))
    def mul(self, x, y):
        return self.__mod(self.ops.mul(x,y))
    def add(self, x, y):
        return (self.ops.add(x,y))
        return self.__mod(self.ops.add(x,y))


    def int2element(self, i):
        # may be zero-ring
        return self.__mod(self.ops.int2element(i))
    def mul_int(self, x, i):
        return self.ops.mul(x, self.int2element(i))
        return self.mul(x, self.int2element(i))


class IUnivariatePolynomialOverField_DegCoefPairsLE_Ops(IUnivariatePolynomialOverField_Ops):
    # polynomial = [(deg, coef)] # little-endian, coef != 0
    # or?? polynomial = (ndeg, [(deg-ndeg, coef)]) # little-endian, coef != 0
    #       rshift/lshift would be fast
    @abstractmethod
    def get_coefficient_ring_ops(self):pass
    def is_XE_LE(self): return True
    def is_element(self, x):
        if not (type(x) is tuple
            and all(type(e) is tuple and len(e) == 2 for e in x)
            ):
            return False
        degs = map(lambda p:p[0], x)
        coefs = map(lambda p:p[1], x)
        is_coef = self.get_coefficient_ring_ops().is_element
        return (all(type(deg) is int and deg >= 0)
            and all(d0<d1 for d0,d1 in zip(degs, degs[1:]))
            and all(map(is_coef, coefs))
            )
    def __untypecheck_make_polynomial_from_degree_coefficient_pairsLE__(self, pairs:tuple):
        return pairs
    def __untypecheck_make_polynomial_from_degree_coefficient_pairsBE__(self, pairs:tuple):
        return pairs[::-1]
    def iter_degree_nonzero_coefficient_pairsLE(self, f):
        return iter(f)
    def iter_degree_nonzero_coefficient_pairsBE(self, f):
        return reversed(f)
    # rshift/rshift_low/low/low_opposite

class UnivariatePolynomialOverRationalField_DegCoefPairsLE_Ops(IUnivariatePolynomialOverField_DegCoefPairsLE_Ops):
    def get_coefficient_ring_ops(self):
        return TheRationalFieldOps


if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())
    print_global_names(dir(IUnivariatePolynomialOverField_Ops))
if __name__ == '__main__':
    from seed.test_utils.generate_test_data import str2values_by_line2expr
    def test1(the_division, n, d):
        q,r = the_division.divmod(n, d)
        assert the_division.len(r) < the_division.len(d)
        assert the_division.element_equal(the_division.mul(q,d), the_division.sub(n,r))
    def intsLE2polynomials(the_division, ints):
        F = the_division.get_coefficient_ring_ops()
        f = F.int2element
        return the_division.make_polynomial_from_degree_coefficient_pairsLE(
            (deg, f(i)) for deg,i in enumerate(ints))

    def intsLEss2polynomialss(the_division, intsss):
        return [[intsLE2polynomials(the_division, ints) for ints in intss] for intss in intsss]
    def test():
        from fractions import Fraction
        F = TheRationalFieldOps
        the_division = UnivariatePolynomialOverRationalField_DegCoefPairsLE_Ops()
        # [001]//[33] = [-1/3,1/3]
        # 100 - 33*(1/3,0) = 100-110 = (-1,0)
        # (-1,0) - 33*(-1/3,) = (-1,0) + 11 = 1
        f = ((0, Fraction(3, 1)), (1, Fraction(6, 1)), (2, Fraction(4, 1)))
        g = ((0, Fraction(3, 1)), (1, Fraction(3, 1)))
        Df = 2
        inv = the_division.inv(Df, g)
        assert inv == ((0, Fraction(-1, 3)), (1, Fraction(1, 3)))

        s = '''
        [], [1]
        [], [1,1,3]
        [3,6,4], [3, 3]
        [3,4,5,6,7,234,324,5345,453,464,4534,3423,53,232,5345], [2,3,4,6,7]
        '''
        n_d_pairs = str2values_by_line2expr(s)
        n_d_pairs = intsLEss2polynomialss(the_division, n_d_pairs)
        for n,d in n_d_pairs:
            test1(the_division, n, d)


    test()


'''
IUnivariatePolynomialOverField_Ops
UnivariatePolynomialOverFieldOps2ModRingOps
IUnivariatePolynomialOverField_DegCoefPairsLE_Ops
UnivariatePolynomialOverRationalField_DegCoefPairsLE_Ops


add
arbitrary_norm_EuclideanDomain
arbitrary_radix_reprBE2number
concatBE
deg
div_lead
div_scale
div_via_mul_inv
divmod
divmods
element_equal
element_equal_int
extract_degrees_nonzero_coefficients_XE
extract_may_invGE2_g
floor_div
floor_divs
gcd
gcd_ex3
gcd_ex5
get_coefficient_ring_ops
get_leading_coefficient__maybe0
get_may_leading_nonzero_term
get_may_lowest_nonzero_term
get_the_one_polynomial
get_the_only_nonzero_term
get_the_zero_polynomial
ginvmod
int2coefficient
int2element
inv
is_XE_LE
is_element
is_neg_one
is_one
is_the_zero_polynomial
is_unit
is_zero
iter_degree_nonzero_coefficient_pairsBE
iter_degree_nonzero_coefficient_pairsLE
iter_degree_nonzero_coefficient_pairsXE
iter_powers
iter_times
lead
len
low
low_opposite
lshift
lshift_one
make_modular_ring_ops
make_polynomial_from_degree2coefficient
make_polynomial_from_degree_coefficient
make_polynomial_from_degree_coefficient_pairsBE
make_polynomial_from_degree_coefficient_pairsLE
make_polynomial_from_degree_coefficient_pairsXE
may_deg
may_invmod
may_ndeg
mod
mods
mul
mul_int
mul_int_by_add
mul_low
mul_low_opposite
mul_rshift
mul_scale
ndeg
neg
neg_one
number2arbitrary_radix_reprLE
number2iter_arbitrary_radix_reprLE
one
pow_mod
pow_uint
powers
product
product_mod
rshift
rshift_low
sub
sum
times
try_div
try_div_int
typecheck_std_degree_coefficient_pairsXE
vector_add
vector_mul
zero
'''


