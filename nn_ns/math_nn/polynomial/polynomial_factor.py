


'''
a univariate polynomial over the integers, assumed to be content-free and square-free
coefficients = integer^(degree+1) = [integer]{degree}
gcd(coefficients) == 1, coefficients[degree] > 0
polynomial(x) = sum coefficients[i] * x^i {i=0..degree}
assume square free
if coefficients[degree] != 1, then
    polynomial(x/coefficients[degree])*coefficients[degree]^(degree-1)
        = x^degree + x^(degree-1)*coefficients[degree-1] + ...
assume coefficients[degree] == 1
then find a subset of roots of which sum is a integer
O(2^degree)
'''

from abc import ABCMeta, abstractmethod

class IFactorPolynomialOverUFD(metaclass=ABCMeta):
    '''factor polynomial over unique factorization domain

f is primitive_polynomial <==> gcd(coefficients_of(f)) is unit
primitive_polynomial may not be monic_polynomial
factors of primitive_polynomial are primitive_polynomial
product of primitive_polynomials is primitive_polynomial
[f = h*g != 0]
    exists h2,g2, s.t.
        LC(f)*f == h2 * g2
        LC(h2) == LC(g2) == LC(f)
        h2 == LC(f)/LC(h) * h
        g2 == LC(f)/LC(g) * g

to integer UFD:
    # see The Art of Computer Programming, Volume 2 :: Chapter4
    #   [page 684-685] 4.6.2 exercise 22 answer.
    #   about "Hensel's Lemma" # Hensel lift
    #
    #
    f,s,t,S,T are polynomial
    m,n,g are integer
    ??how to lift [f = s*t mod m] to [f = S*T mod (m*g)][S=s, T=t (mod m)]??
    # g: [g\m][gcd(s,t)=1 mod g]
    S=s+m*s'; T=t+m*t' <<== find s',t' instead of S,T
    (mod m*g):
        f = (s+m*s')(t+m*t') = s*t + m*m*s't'+ m*(s'*t+s*t')
        [g\\m] ==>> [mg\\mm] ==[mm=0 mod mg]=>> m*(s'*t+s*t') = (f-s*t)
    [g\\m] (mod g):
        (F1) (s'*t+s*t') = (f-s*t)/m  =[named]= L
        [gcd(s,t)=1 mod g]
            A*s+B*t = 1 <<== find A,B since gcd = 1
            L*A*s+L*B*t = L     # compare with (F1)
            s'=L*B; t'=L*A      # mod g
'''
class IFactorPolynomialOverField(IFactorPolynomialOverUFD):
    '''
monic_polynomial <= primitive_polynomial
when coefficient ring is a field, primitive_polynomial can standardize to monic_polynomial
'''
    @abstractmethod
    # get_polymonial_ops() -> IPolynomialDivision
    # get_polymonial_ops().get_coefficient_ring_ops() -> IFieldOps
    def get_polymonial_ops(self):pass
    @abstractmethod
    # input: non-linear--monic-polynomial
    # return [monic_irreducible_factor]
    def factor_monic_square_free_polynomial_degreeGE2(self, f):pass
    def get_coefficient_field_ops(self):
        return self.get_polymonial_ops().get_coefficient_ring_ops()
    def factor(self, f):
        # return (LC, [(monic_irreducible_factor, power)])
        #       where LC is 0 or the leadiing coefficient
        # factors may be equal; deg factor >= 1
        content, monic_primitive_part = self.content_monic_primitive_part_factor(f)
        return content, self.factor_monic_polynomial(monic_primitive_part)
    def factor_monic_polynomial(self, f):
        # return [(monic_irreducible_factor, power)] where power >= 1
        # factors may be equal; deg factor >= 1
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        assert fops.is_monic_polynomial(f)
        # f = x**ndeg * ??
        ndeg = fops.ndeg(f)
        f = fops.rshift(ndeg, f)
        fs = self.square_free_factors_of_monic_polynomial(f)
        ls = [(fops.lshift_one(1), ndeg)] if ndeg else []
        factor = self.factor_monic_square_free_polynomial
        for f, exp in fs:
            ls.extend((f, exp) for f in factor(f))
        return tuple(ls)
    def factor_monic_square_free_polynomial(self, f):
        # return [monic_irreducible_factor]
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        assert fops.is_monic_polynomial(f)
        if fops.deg(f) == 1: return (f,)
        return self.factor_monic_square_free_polynomial_degreeGE2(f)
    def derived_function_of(self, f):
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        def it():
            for d,c in fops.iter_degree_nonzero_coefficient_pairsXE(f):
                if d == 0: continue
                c = cops.mul_int(c, d)
                d -= 1
                yield (d, c)
        return fops.make_polynomial_from_degree_coefficient_pairsXE(it())
    def square_free_factors_of_monic_polynomial(self, f):
        # return [(monic_square_free_factor, power)] # tuple
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        assert fops.is_monic_polynomial(f)
        def this_func(f):
            # f != 0 ; f may be not monic
            # return [(square_free_factor, power)] # list
            Df = fops.deg(f)
            if Df == 0:
                return ()
            if Df == 1:
                return ((f, 1),)
            df = self.derived_function_of(f)
            if fops.is_the_zero_polynomial(df):
                # f is polynomial over finite field
                assert isinstance(cops, IFiniteFieldOps)
                p = cops.characteristic
                assert p >= 2
                def g():
                    for d,c in fops.iter_degree_nonzero_coefficient_pairsXE():
                        q,r = divmod(d,p)
                        assert r == 0
                        yield q,c
                # f(x) = g(x^p) = (g(x))^p
                g = fops.make_polynomial_from_degree_coefficient_pairsXE(g())
                gs = this_func(g)
                return tuple((g, exp*p) for g,exp in gs)
            g, fg, dfg = fops.gcd_ex3(f, df)
            fgg = fops.true_div(fg, g)
            gs = this_func(g)
            fs = [(fgg, 1)]
            fs.extend((g, exp*2) for g,exp in gs)
            return fs
        fs = this_func(f)
        mpp = self.monic_primitive_part_of
        return tuple((mpp(f), exp) for f, exp in fs)

    def monic_primitive_part_of(self, f):
        LC, mpp = self.content_monic_primitive_part_factor(f)
        return mpp
    def content_monic_primitive_part_factor(self, f):
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        LC = fops.get_leading_coefficient__maybe0(f)
        if cops.is_zero(LC):
            monic_primitive_part = fops.get_the_one_polynomial()
        else:
            monic_primitive_part = fops.div_scale(f, LC)
        return LC, monic_primitive_part


'''
IPolynomialDivision
PolynomialDivision2ModRingOps
IPolynomialDivision_DegCoefPairsLE
PolynomialDivision_DegCoefPairsLE_RationalField


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



class IFactorPolynomialOverFiniteField(IFactorPolynomialOverField):
    @abstractmethod
    # get_polymonial_ops() -> IPolynomialDivision
    # get_polymonial_ops().get_coefficient_ring_ops() -> IFiniteFieldOps
    def get_polymonial_ops(self):pass
    @abstractmethod
    # deg(result) < deg
    def generate_random_polynomial_degree_ge_lt(self, deg_begin, deg_end):pass
    @abstractmethod
    def iter_all_finite_field_elements(self):pass

    def factor_monic_square_free_polynomial_degreeGE2(self, f):
        # return [monic_irreducible_factor]
        deg_factor_pairs = self.distinct_degree_factor_monic_square_free_polynomial_degreeGE2(f)
        eq_factor__odd = self.equal_degree_factor_monic_square_free_polynomial__odd_field_order__random
        eq_factor__any = self.equal_degree_factor_monic_square_free_polynomial__random
        p = self.get_coefficient_field_ops().characteristic
        eq_factor = eq_factor__odd if p%2 else eq_factor__any
        output = []
        for deg, factor in deg_factor_pairs:
            output.extend(eq_factor(deg, factor))
        return tuple(output)
    # see The Art of Computer Programming, Volume 2 :: Chapter4
    #   [page 687] 4.6.2 exercise 30 answer.
    #       when p == 2 # i.e. not odd field order
    #   [p is prime][f and f[i] are irreducible polynomial over Field[p] of degree d]
    #       x^p^d - x === 0 (mod f) # i.e. contains all irreducible polynomials of degree d
    #       f must divide one factor of "x^p^d - x"
    #       let fs = f1*f2... = II f[i] {i}
    #           fs = II gcd(fs, h) {h <- factors of (x^p^d - x)}
    #       ???how to factor "x^p^d - x"???
    #       [p is odd]
    #           x^p^d - x === x(x^[(p^d-1)/2]-1)(x^[(p^d-1)/2]+1) (always)
    #       x^p^d - x === II T(x,d)-i {i=0..p-1} (mod f)
    #           T(x,d) = SUM x^p^i {i=0..d-1}
    #           [g mod f]  #  to factor, deg g < 2d
    #               (mod f): g^p^d === g === g^p^0
    #               (mod f): T(g,d)^p = SUM g^p^i {i=1..d} = sum~{i=1..d-1} + g^p^d = sum~{1..d-1} + g = sum~{0..d-1} = T(g,d)
    #               T(g,d) is a root of "y^p = y mod f", whose roots are [0..p-1]
    #           compute T(g,d) = g + (g+(...)^p)^p
    #           to factor, should try (p-1) factors
    #           which g?
    #               since:  (E1) (mod p): [T(g+h,d)=T(g,d)+T(h,d)]
    #                       (E2) (mod f1*f2...): [T(g^p,d)=T(g,d)^p=T(g,d)]
    #                       (E3) (mod p): [c <- {0..p-1}] ==>> [c^p=c][T(c*g,d)=c*T(g,d)]
    #               choose g <- [x^i | i<-[0..2d-1], i%p!=0]
    #               why? if fs=f1*f2: g_ = SUM c[i]*x^i {i}
    #                   (mod fs): T(g_,d) =[(E1)]= SUM T(c[i]*x^i,d) {i} =[(E3)]= SUM c[i]*T((x^no_p[i])^p^k[i],d) {i} =[(E2)]= SUM c[i]*T(x^no_p[i], d) {i}
    #                   let S = {no_p[i] | i} where no_p%p != 0
    #                   if T(x^s,d) == 0 (mod fs) for s in S, then also T(g_,d) == 0 (mod fs). # i.e. try g_, but has no effect.
    #           [p == 2] # only two factors
    #               which g? g <- [x, x^3, x^5 .. x^(2d-1)]
    #       why "i<2d"??
    #           [page 686-687] 4.6.2 exercise 29 answer.
    # mine: # factor over subfield first
    #   over finite field F[q] or F[2^s]; q=2^s  # 2 can be replaced by any prime p
    #   define T(x,r,s,d) = SUM x^(2^r)^i {i=0..(s/r)*d-1} where [r\s]
    #   (M1) (mod f): g^q^d = g^2^(s*d) = g = g^q^0 # g is an element of F[q^d]
    #   (M2) (mod 2): (g+h)^2 = g^2 + h^2 ==>> (g+h)^(2^r) == g^2^r + h^2^r # characteristic is p
    #       ==>> (M2-1) T(x+y,r,s,d) = T(x,r,s,d)+T(y,r,s,d)
    #   (M3) (mod f): T(g,r,s,d)^(2^r) =[(M2)]= sum~{i=1..s/r*d} = sum~{i=1..s/r*d-1} + g^2^(s*d) =[(M1)]= sum~{i=0..s/r*d-1} = T(g,r,s,d)
    #   (M3) ==>> T(g,r,s,d) is root of "y^(2^r)=y (mod f)" i.e. element of subfield F[2^r]
    #   [c in F[2^r]] # i.e. [c^(2^r) == c]
    #       (M4)(mod f): T(c*x,r,s,d) = SUM (c*x)^(2^r)^i {i} = SUM c*(..^..) {i} = c*T(x,r,s,d)
    #   [coefficients_of(g) are in F[2^r]] # i.e. [g(x)^(2^r)=g(x^2^r) (mod 2)]
    #       (mod f): T(g^2^r,r,s,d) = T(g(x^2^r),r,s,d) = SUM ci*(x^2^r)^(2^r)^i {i} = T(g,r,s,d)^2^r =[(M3)]= T(g,r,s,d)
    #   which g?
    #       what if g <- [x^i | i<-[1..2d-1], i%2^r != 0] # i%p^r!=0 and i < 2d
    #           but only 2^(2d)(1-1/2^r) possible, not enough!! there are 2^(r*d) polynomials of degree d with coefficients in F[2^r]
    #       ERROR

    def equal_degree_factor_monic_square_free_polynomial__random(self, deg, f):
        # return [factor] # all factors of f have same degree deg >= 1
        # for all field order, but mainly for field order 2
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        assert deg >= 1
        assert fops.deg(f)%deg == 0
        Df = fops.deg(f)
        p,s,q = cops.get_characteristic_power_order()
        assert p >= 2
        assert s >= 1
        assert p**s == q
        def iter_i():
            return (i for i in range(2*deg) if i%p)
        def iter_g():
            # g = x^i  #  will beyond mops
            return map(fops.lshift_one, iter_i())
        x = fops.lshift_one(1)
        def T(g,d,mops):
            # g = x^i  #  will beyond mops
            # T g d = g + g^q + ... + g^q^d = g + (T g (d-1))^q
            D = d
            g = mops.euclidean_domain_element2modular_ring_element(g)
            d = 0; Tgd = g
            for d in range(1, D+1):
                # can compute [(x^i)^q mod f] first
                # and then replace (x^i) in (T g (d-1))
                Tgd1_q = mops.pow_uint(Tgd, q) # (T g (d-1))^q
                Tgd = fops.add(g, Tgd1_q) # fops; need not mops
            return Tgd

        it_g = iter_g()
        # nonlocal
        Tgd = None
        it_elem = iter([])
        mops_old = None
        def elem2gcd(elem, mops):
            Tgd_elem = fops.add(Tgd, elem)
            product_of_fs = mops.modulus
            gcd = fops.gcd(Tgd_elem, product_of_fs)
            return gcd
        def _next_gcd(mops):
            nonlocal Tgd, it_elem, mops_old
            if mops is not mops_old:
                mops_old = mops
                if Tgd is not None:
                    Tgd = mops.euclidean_domain_element2modular_ring_element(Tgd)
            for elem in it_elem:
                return elem2gcd(elem, mops)

            new_Tgd_it_elem()
            for elem in it_elem:
                return elem2gcd(elem, mops)
            else: raise logic-error-FiniteField1
        def new_Tgd_it_elem(mops):
            nonlocal Tgd, it_elem
            for g in it_g:
                Tgd = T(g,deg, mops)
                break
            else:
                raise logic-error # i.e. concept error: g = [x^i|i<2d, i%p!=0]
            it_elem = self.iter_all_finite_field_elements()
            # skip one elem
            for elem in it_elem:break
            else: raise logic-error-FiniteFieldNoElement


        # nonlocal
        remain_deg = Df # no less than deg
        def next_gcd(mops):
            nonlocal remain_deg
            if remain_deg <= deg:
                new_Tgd_it_elem()
                remain_deg = fops.deg(mops.modulus)
            gcd = _next_gcd(mops)
            remain_deg -= fops.deg(gcd)
            return gcd
        return self.__equal_degree_factor_monic_square_free_polynomial(deg, f, next_gcd)
    def equal_degree_factor_monic_square_free_polynomial__odd_field_order__random(self, deg, f):
        # return [factor] # all factors of f have same degree deg >= 1
        # field order q is odd
        # random polynomial g
        #   ==>> f = gcd(f, g^q^deg - g)
        #   ==>> f = gcd(f, g) * gcd(f, g^[(q^deg-1)/2] +1) * gcd(f, g^[(q^deg-1)/2] -1)
        #   [deg(g) <= 2*deg - 1] ==>> gcd(f, g^[(q^deg-1)/2] -1) is nontrivial factor of f
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        assert cops.order%2 == 1
        beyond_maxDg = 2*deg
        exp = (cops.order**deg - 1)//2
        one = fops.get_the_one_polynomial()
        def next_gcd(mops):
            g = self.generate_random_polynomial_degree_ge_lt(1, beyond_maxDg)
            # len g <= beyond_maxDg == 2*deg <= deg(product_of_fs) < len product_of_fs
            # so, g is an element of mops
            g_exp = mops.pow_uint(g, exp)
            g_exp_1 = fops.sub(g_exp, one) # g^exp - 1 mod product_of_fs
            product_of_fs = mops.modulus
            gcd = fops.gcd(g_exp_1, product_of_fs)
            return gcd
        return self.__equal_degree_factor_monic_square_free_polynomial(deg, f, next_gcd)
    def __equal_degree_factor_monic_square_free_polynomial(self, deg, f, next_gcd):
        # return [factor] # all factors of f have same degree deg >= 1
        # next_gcd(mops) -> gcd | raise Error
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        assert deg >= 1
        assert fops.deg(f)%deg == 0
        assert cops.order%2 == 1
        Df = fops.deg(f)
        if Df == 0:
            return ()
        if Df == deg:
            return (f,)
        output = [] # deg(x) == deg for x in output
        fs = [f] # deg(x)/deg >= 2 for x in fs
        product_of_fs = f # deg(product_of_fs) >= 2*deg
        mops = fops.make_modular_ring_ops(product_of_fs)
        Dfs = fops.deg(product_of_fs)
        while fs:
            gcd = next_gcd(mops)

            assert fops.len(gcd)
            if not (0 < fops.deg(gcd) < Dfs):
                # unit; trivial
                continue
            # may split some f in fs
            output_more = []
            fs_new = []
            for f in fs:
                h = fops.gcd(gcd, f)
                Dh = fops.deg(h)
                if 0 < Dh < fops.deg(f):
                    # nontrivial
                    fh = fops.true_div(f, h)
                    for h in [h,fh]:
                        if fops.deg(h) == deg:
                            output_more.append(h)
                        else:
                            fs_new.append(h)
                else:
                    # recycle f
                    fs_new.append(f)

            # next iter
            # update fs/output/product_of_fs/mops/Dfs
            fs = fs_new
            if output_more:
                output += output_more
                product_of_output_more = fops.product(output_more)
                product_of_fs = fops.true_div(product_of_fs, product_of_output_more)
                mops = fops.make_modular_ring_ops(product_of_fs)
                Dfs = fops.deg(product_of_fs)
            # end of while
        return tuple(output)

    '''
    def distinct_degree_factor_monic_square_free_polynomial__subfield(self, basic_deg, f, p, r, p_r, s, p_rs, factors_of_s):
        # target: to factor f over F[p_rs]
        # coefficients_of f are in F[p_rs]
        # factors of f over F[p_rs] are all have degree multple of "basic_deg"
        # p_r = p^r; p_rs = p^(r*s); p^(r*s*t) == q
        # factors_of_s = [(prime, exp)] whose product is s
        # gcd(r,s) == 1
        assert basic_deg >= 1
        assert deg f % basic_deg == 0
        if deg f <= basic_deg:
            return [] | [f]
        if s == 1:
            # f has no factor over subfield
            return do_real_work(...) # distinct_degree_factor_monic_square_free_polynomial_degreeGE2
        S = s
        R = r
        p_R = p_r
        output = []
        for idx, (prime, exp) in enumerate(factors_of_s):
            # S = product factors_of_s[idx:]
            # S*R = s*r
            # p_R = p**R
            p_RSp = p_R^(S/prime) # max subfield
            d = deg f Error should for d in [basic_deg,2 basic_deg...]
            g = gcd(x^p_RSp^d-x, f)
            # if g == 1: continue # S = ...
            if deg g > 0:
                factors_of_Sp = factors_of_s[idx+1:]
                if exp>0: factors_of_Sp = ((prime,exp-1),)+factors_of_Sp
                output <- recur(g, p, R, p_R, S/prime, p_RSp, factors_of_Sp)
                f = f/g
                if deg f <= basic_deg: break
            De = prime^exp
            S /= De
            R *= De
            p_R **= De
        output <- recur(f,p,r*s, p_rs, 1, p_rs, [])
        return output
    '''


    def distinct_degree_factor_monic_square_free_polynomial_degreeGE2(self, f):
        # return [(degree, factor)] # LE
        # product of factor of degree d == gcd(f, x^q^d - x) where q is field order
        cops = self.get_coefficient_field_ops()
        fops = self.get_polymonial_ops()
        assert fops.is_monic_polynomial(f)
        assert fops.deg(f) >= 2
        Df = fops.deg(f)
        q = cops.order
        d = 0
        mops = make_modular_ring_ops(f)
        x_q_d_mod_f = x = fops.lshift_one(1)
        deg_factor_pairs = []
        #for d in range(1, Df//2+1):
        # f and Df are changing, dec
        while d < Df//2:
            d += 1
            # d <= Df//2 < Df//2+1
            x_q_d_mod_f = mops.pow_uint(x_q_d_mod_f, q)
            g, fg, _ = fops.gcd_ex3(f, fops.sub(x_q_d_mod_f, x))
            if fops.is_one(g): continue
            deg_factor_pairs.append((d, g))
            f = fg
            Df = fops.deg(f)
            if not Df: break
            mops = make_modular_ring_ops(f)
            x_q_d_mod_f = mops.euclidean_domain_element2modular_ring_element(x_q_d_mod_f)
        else:
            assert Df
            deg_factor_pairs.append((Df, f))
        return tuple(deg_factor_pairs)




