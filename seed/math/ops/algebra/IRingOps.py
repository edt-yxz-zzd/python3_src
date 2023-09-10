#__all__:goto
r'''[[[
e ../../python3_src/seed/math/ops/algebra/IRingOps.py
seed.math.ops.algebra.IRingOps
view ../../python3_src/seed/math/IRingOps.py
view ../../python3_src/seed/math/Field2xPolynomial.py

view ../../python3_src/seed/math/ops/algebra/algebra.txt


[[
/\<ops\>[.]_\(\w*\)
xxx %s/\<ops\>[.]_\(\w*\)/object.__getattribute__(ops, '_\1')/g
    ops._xxx = ...

]]


[[

/ops<z> -> z -> \(z \)\@!
/\<is_Fraction\>
%s//\0_/g
append "_" to func name
    # except: mul.*
    why rename?
        is_field()
        get_zero()
        get_characteristic()
        get_ring_ops4coeff()
        mk5int(...)
        #classmethod
        ====vs:
        #instancemethod
        is_int_(z)
        eq_zero_(z)
        get_imay_degree_(z)
        get_num_nonzero_coeffs_(z)
        to_may_int_(z)
        neg_(z)
        inv_(z)
    why not rename:add/mul/sub/truediv/try_left_div/eq/...???
        binary op vivi __xxx__ is called from cls
]]


[[
mv seed.math.ops.algebra.IFiniteFieldOps --> seed.math.ops.algebra.IRingOps
!mv ../../python3_src/seed/math/ops/algebra/IFiniteFieldOps.py   ../../python3_src/seed/math/ops/algebra/IRingOps.py
e ../../python3_src/seed/math/ops/algebra/IFiniteFieldOps.py
e ../../python3_src/seed/math/ops/algebra/IRingOps.py
.+1,$s/seed[.]math[.]ops[.]algebra[.]IFiniteFieldOps/seed.math.ops.algebra.IRingOps/g
]]

[[cancel:
rename: truediv --> div
    except: __truediv__
.+1,$s/truediv/div/g
]]



seed.math.ops.algebra.IRingOps
py -m nn_ns.app.debug_cmd   seed.math.ops.algebra.IRingOps -x


py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IFiniteFieldOps@T    =T

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IBaseSemiringOps,IBaseRingOps,IRingOps,IFieldOps,IFieldOps___characteristic_is_0,IFieldOps___characteristic_is_prime,IFiniteFieldOps     =IBaseSemiringOps =IBaseRingOps =IRingOps =IFieldOps =IFieldOps___characteristic_is_0 =IFieldOps___characteristic_is_prime =IFiniteFieldOps      --exclude='lambda nm:nm.startswith("_")'    > ~/my_tmp/out4py/print_methods..seed.math.ops.algebra.IRingOps.out.txt
view /sdcard/0my_files/tmp/out4py/print_methods..seed.math.ops.algebra.IRingOps.out.txt


py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IPolynomialRingOps@T    =T
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IFieldOps@T    =T      ++exclude_prefixes:_
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IFieldOps___characteristic_is_0@T    =T      ++exclude_prefixes:_
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IFieldOps___characteristic_is_prime@T    =T      ++exclude_prefixes:_

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IFiniteFieldOps@T    =T      ++exclude_prefixes:_



py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IRingOps@T    =T      ++exclude_prefixes:_
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IEuclideanRingOps@T    =T      ++exclude_prefixes:_

py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IPolynomialRingOps@T    =T      ++exclude_prefixes:_
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IBasePolynomialRingOps@T    =T      ++exclude_prefixes:_
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.ops.algebra.IRingOps:IPolynomialRingOps@T,IPolynomialRingQuotientRingOps@C    =T =C     ++exclude_prefixes:_    > ~/my_tmp/out4py/print_methods..seed.math.ops.algebra.IRingOps.out.txt
view /sdcard/0my_files/tmp/out4py/print_methods..seed.math.ops.algebra.IRingOps.out.txt





NOTE:
    [gcd(x,y) :: z -> z -> z|^NotExistError]
    [GCD(x,y) :: z -> z -> {z}]
    [[GCD(x,y) =!= {}] -> [gcd(x,y) <- GCD(x,y)]]
    #####
    even for Euclidean rings, the notion of GCD of two elements of a ring is not the same as the GCD of two ideals of a ring. This is sometimes a source of confusion when studying rings other than Z, such as polynomial rings in several variables.
    see:gcd4ideal()
        [gcd4ideal(ring;<m>,<n>) == Ideal<m> + Ideal<n> |<=| Ideal<gcd(ring;m,n)>]
        [ring := QQ[X,Y]]:
            [gcd4ideal(ring;<X>,<Y>) == Ideal<X> + Ideal<Y> |<| Ideal<gcd(ring;X,Y)> == Ideal<1> == ring]
    ####



NOTE:
    K(x) vs K[x]
        ExtensionField vs PolynomialRing
        K(x) the field of fractions of polynomial ring K[x]

    [K(x) =[def]= extension_field(K; {x}) = {Fraction(n,d) | [n,d <- K[x]]}]
    [K[x] =[def]= polynomial_ring(K; x) = {sum~ k*x**e ~{(e,k) <- ps} | [ps :: [(uint,K)]{len finite}]}]


NOTE:
    Quotient Ring =[def]= Ring/Ideal
    but:
    Quotient Field =[def]= field of fractions = field of quotients of an integral domain (D/D{=!=0})
    ===

===
[ring/ideal =[def]= quotient_ring(ring; ideal)]
===
[CR <- CommutativeRing][f(x) <- CR[x]]:
    [quotient_ring_of_polynomial_ring(CR; f(x)) =[def]= quotient_ring(CR[x]; Ideal<f(x)>) = {g(x) + <f(x)> | [g(x) <- CR[x]]}]
===
[K <- Field][f(x) <- K[x]][is_irreducible_polynomial_(K; f(x))][deg(f) >= 1]:
    [quotient_ring_of_polynomial_ring(K; f(x)) <- Field]
    [quotient_ring_of_polynomial_ring(K; f(x)) =[def]= extension_field(K; one_arbitrary_root_of_(f))]
    ===
    #QuotientRingOfPolynomialRing
    IPolynomialRingQuotientRingOps
    ICommutativePolynomialRingQuotientRingOps
    ICommutativePolynomialRingQuotientRingOps___modulus_is_monic_irreducible_polynomial
===
[K <- Field][f(x) <- K[x]][deg(f) >= 1]:
    [splitting_field(K; f(x)) =[def]= /-\~ F ~{F <- Field | [K <= F][all_roots_of_(f) |<=| F]}]
    [splitting_field(K; f(x)) =[def]= extension_field(K; all_roots_of_(f))]
===
[K <- Field][f(x) <- K[x]][is_irreducible_polynomial_(K; f(x))][deg(f) >= 1]:
    ???[extension_field(K; all_roots_of_(f)) =[def]= splitting_field(K; f(x)) =?= quotient_ring_of_polynomial_ring(K; f(x)) =[def]= extension_field(K; one_arbitrary_root_of_(f))]???
        counterexample:
        [quotient_ring_of_polynomial_ring(QQ; (x^3-2))
        == QQ[x]/<x^3-2>
        ~=~ QQ(2**(1/3))
        == extension_field(QQ; 2**(1/3))
        #  [extension_field(QQ; all_roots_of_(x^3-2)) has one Real root and two conjugation non-Real roots]
        #  [extension_field(QQ; 2**(1/3)) has one Real root]
        !! [(extension_field(QQ; all_roots_of_(x^3-2)):QQ) == deg(x^3-2) * deg(x^2+2**(1/3)*x+2**(2/3)) = 3*2 = 6 = 3!]
        !! [(extension_field(QQ; 2**(1/3)):QQ) == deg(x^3-2) = 3]
        =!= extension_field(QQ; all_roots_of_(x^3-2))
        == splitting_field(QQ; (x^3-2))
        ]
        but true if [K <- FiniteField]
===
[K <- FiniteField][f(x) <- K[x]][is_irreducible_polynomial_(K; f(x))][deg(f) >= 1]:
    [extension_field(K; all_roots_of_(f)) === splitting_field(K; f(x)) == quotient_ring_of_polynomial_ring(K; f(x)) === extension_field(K; one_arbitrary_root_of_(f))]
    ===
    #SplittingFieldOfIrreduciblePolynomialOverFiniteField
    IFiniteFieldIrreduciblePolynomialSplittingFieldOps
===

[ring.is_mul_commutative()][n,d :<- ring]:
    [is_divisor_of_(ring; n; d) =[def]= [?[q :<- ring] -> [q*d == n]]]
[ring.is_mul_commutative()][d :<- ring][d =!= 0]:
    [is_primal_(ring; d) =[def]= [@[m,n :<- ring] -> [is_divisor_of_(ring; m*n; d)] -> ?[a,b :<- ring] -> [[a*b==d][is_divisor_of_(ring; m; a)][is_divisor_of_(ring; n; b)]]]]




[ring :<- Ring]:
    !! [ring.is_mul_associative()]
    !! [[is_mul_associative] -> [left_inv_ === right_inv_]]
    [ring.left_inv_ === ring.right_inv_ === ring.inv_]
    ===
    [is_ring_unit_ =[def]= is_invertable_]
    [UnitGroup(ring) = U(ring) =[def]= multiplicative_group_of_units_of(ring)]

[ring :<- Ring][I,J,K :<- ring.Ideal]:
    [I+J =[def]= {m+n | [[m :<- I][n :<- J]]}]
    [is_divisor_of_ideal_(ring; I;J) =[def]= [I |<=| J]]
    [is_common_divisor_of_ideal_(ring; I,J;K) =[def]= [[I |<=| K][I |<=| K]]]
    [is_common_divisor_of_ideal_(ring; I,J;I+J)]
    [[is_common_divisor_of_ideal_(ring; I,J;K)] -> [I+J |<=| K]]
    # ==>>:
    [
    [gcd4ideal(ring; I,J) =[def]= I+J]
        # vs:GCD

[ring.is_mul_commutative()][d :<- ring][ns :<- {ring}]:
    [is_common_divisor_of_(ring; ns; d) =[def]= [@[n :<- ns] -> [is_divisor_of_(ring; n; d)]]]

[ring.is_mul_commutative()][not ring.is_trivial_ring()][m,n :<- ring]:
    #lcm(least common multiple)
    #gcd (greatest common divisor)
    [GCD(ring; m,n) =[def]= {d | [[d :<- ring][is_common_divisor_of_(ring; {m,n}; d)][@[c :<- ring] -> [is_common_divisor_of_(ring; {m,n}; c)] -> [is_divisor_of_(ring; d; c)]]]}]
        # vs:gcd4ideal
        #
    #『gcd --> GCD』==>> ?update?:
        #inv_ --> all_inv_of_ --> INV_
        #try_left_div --> LEFT_DIV
        #try_right_div --> RIGHT_DIV
        #try_truediv --> TRUE_DIV

[ring.is_mul_commutative()][not ring.is_trivial_ring()][m,n,u :<- ring]:
    [GCD(ring;0,0) == {0}]
    [GCD(ring;n,1) == UnitGroup(ring)]
    [GCD(ring;m,n) == GCD(ring;n,m)]
        # commutative
    [GCD(ring;m,GCD(ring;n,u)) == GCD(ring;GCD(ring;m,n),u)]
        # associative
    [n <- GCD(ring;n,n)]
        # idempotent
    [GCD(ring;m,n)*u == GCD(ring;m*u,n*u)]
        # distributive
    [m <- LCM(m,*GCD(m,n))]
        #satisfies the absorption law



[ring.is_mul_commutative()][not ring.is_trivial_ring()][m,n :<- ring][GCD(ring; m,n) =!= {}]:
    [gcd(ring; m,n) =[def]= arbitrary element of GCD(ring; m,n)]
    [gcd(ring; m,n) <- GCD(ring; m,n)]
    [gcd(ring;0,0) == 0]
    ???[GCD(ring; m,n) == gcd(ring; m,n)*UnitGroup(ring)]???

[ring.is_mul_commutative()][not ring.is_trivial_ring()][m,n :<- ring]:
    [are_relatively_prime_(ring;m,n) =[def]= [GCD(ring; m,n)/-\UnitGroup(ring) =!= {}]]
[ring.is_mul_commutative()][not ring.is_trivial_ring()][d :<- ring]:
    [[is_irreducible_(ring;d)] -> [@[n :<- ring] -> [[are_relatively_prime_(ring;n,d)]or[is_divisor_of_(ring; n; d)]]]]




[ring :<- Ring][n,d :<- ring]:
    ===
    [[is_left_divisor_of_(ring;n;d)] = [is_right_multiple_of_(d;n)] =[def]= [?[q :<- ring] -> [d*q == n]]]
    ===
    [[is_right_divisor_of_(ring;n;d)] = [is_left_multiple_of_(d;n)] =[def]= [?[q :<- ring] -> [q*d == n]]]
    ===

    ===
    #mine-def:
    ===
    [[is_weak_divisor_of_(ring;n;d)] = [is_weak_multiple_of_(d;n)] =[def]= [[is_left_divisor_of_(ring;n;d)]or[is_right_divisor_of_(ring;n;d)]]]
    ===
    [[is_strong_divisor_of_(ring;n;d)] = [is_strong_multiple_of_(d;n)] =[def]= [[is_left_divisor_of_(ring;n;d)][is_right_divisor_of_(ring;n;d)]]]
    ===

[ring :<- Ring][d :<- ring]:
    [is_irreducible_(ring;d) =[def]= [[d=!=0][not [is_ring_unit_(ring;d)]][[x,y :<- ring] -> [x*y==d] -> [[is_ring_unit_(ring;x)]or[is_ring_unit_(ring;y)]]]]]

[ring :<- Ring][p :<- ring]:
    # ???[ring.is_mul_commutative()]
    ===
    #mine-def:def____1_is_prime_
    ===
    [is_prime_(ring;p) =[def]= [[p=!=0][not [is_ring_unit_(ring;p)]][@[x,y :<- ring] -> [is_weak_divisor_of_(ring;x*y;p)] -> [[is_weak_divisor_of_(ring;x;p)]or[is_weak_divisor_of_(ring;y;p)]]]]]
    ===
    #mine-def:def____2_is_prime_
    ===
    [is_prime_(ring;p) =[def]= [[p=!=0][not [is_ring_unit_(ring;p)]][@[x,y :<- ring] -> [is_weak_divisor_of_(ring;x*y;p)] -> [[is_left_divisor_of_(ring;x;p)]or[is_right_divisor_of_(ring;y;p)]]]]]
    ===

[NOT_ALWAYS [is_prime_ <: is_irreducible_]]
    !! see:PrincipalRing:Z_6 #ZZ%6
[[ring.is_integral_domain()] -> [ring.is_prime_ <: ring.is_irreducible_]]
    ZZ[i*sqrt(5)], where i is the imaginary unit, is not a unique factorization domain:
        [6 == 2*3 == (1-i*sqrt(5))(1+i*sqrt(5))]
    [is_irreducible_(ZZ[i*sqrt(5)]; 2)]
    [not is_prime_(ZZ[i*sqrt(5)]; 2)]
    ===not_gcd_domain:
    [ring := ZZ[x]%(x**2+5)]:
        [6 == 2*3 == (1-x)*(1+x)]
        [all_common_divisors_of(6,2*(x+1)) == {+1,-1} .* {2,x+1}]
    [GCD(ZZ[x]%(x**2+5); 6,2*(x+1)) == {}]
    [not is_gcd_domain(ZZ[x]%(x**2+5))]

[[ring.is_pre_Schreier_domain()] -> [ring.is_prime_ == ring.is_irreducible_]]
[[using:def____2_is_prime_] -> [ring.is_domain()] -> [ring.is_prime_ <: ring.is_irreducible_]]

???[[ring.is_domain()] -> [ring.is_prime_ <: ring.is_irreducible_]]???
    # fail:using:def____1_is_prime_
    # ok:using:def____2_is_prime_
    ???fail:using:def____1_is_prime_:[[proof:
    [p :<- ring][is_prime_(ring;p)]:
        [p=!=0]
        [not [is_ring_unit_(ring;p)]]
        #[not [is_irreducible_(ring;p)]]:
        [[x,y :<- ring][x*y==p][not [is_ring_unit_(ring;x)]][not [is_ring_unit_(ring;y)]]]:
            !! [is_strong_divisor_of_(ring;p;p)]
            [is_weak_divisor_of_(ring;x*y;p)]
            [is_weak_divisor_of_(ring;x;p)]:
                * [p*q == x]:
                    [p*q*y == x*y == p]
                    [p*(q*y-1) == 0]
                    !! [ring.is_domain()]
                    !! [p=!=0]
                    [(q*y-1) == 0]
                    [q*y == 1]
                    [ring.left_inv_ === ring.right_inv_ === ring.inv_]
                    [inv_(ring;y) == q]
                    [is_ring_unit_(ring;y)]
                    _L
                * [q*p == x]:
                    [q*p*y == x*y == p]
                    # 『Fraction Field of Integral Domains』
                    # but here domain only ???
                    # a*(1/b) + c*(1/d) == ???
                    # if denominator==b*d:
                    #   1/(b*d) == (1/d)*(1/b)
                    #   a*(1/b) == a*(d*(1/d))*(1/b) == (a*d)*(1/(b*d))
                    #   c*(1/d) == c*(1/d)*((1/b)*b) == c*(1/(b*d))*b
                    #       useless
                    #more: since add is commutative, no matter denominator is (b*d)or(d*b), it is not eqv
                    ???[is_ring_unit_(ring;y)]???
                    ???fail
    ]]
    ok:using:def____2_is_prime_:[[proof:
    [p :<- ring][is_prime_(ring;p)]:
        [p=!=0]
        [not [is_ring_unit_(ring;p)]]
        #[not [is_irreducible_(ring;p)]]:
        [[x,y :<- ring][x*y==p][not [is_ring_unit_(ring;x)]][not [is_ring_unit_(ring;y)]]]:
            !! [is_strong_divisor_of_(ring;p;p)]
            [is_weak_divisor_of_(ring;x*y;p)]
            [[is_left_divisor_of_(ring;x;p)]or[is_right_divisor_of_(ring;y;p)]]
            * [is_left_divisor_of_(ring;x;p)]:
                ?:[q :<- ring] -> [p*q == x]
                [p*q*y == x*y == p]
                [p*(q*y-1) == 0]
                !! [ring.is_domain()]
                !! [p=!=0]
                [(q*y-1) == 0]
                [q*y == 1]
                !! [ring.left_inv_ === ring.right_inv_ === ring.inv_]
                [inv_(ring;y) == q]
                [is_ring_unit_(ring;y)]
                _L
            * [is_right_divisor_of_(ring;y;p)]:
                ?:[q :<- ring] -> [q*p == y]
                [x*q*p == x*y == p]
                [(x*q-1)*p == 0]
                !! [ring.is_domain()]
                !! [p=!=0]
                [(x*q-1) == 0]
                [x*q == 1]
                !! [ring.left_inv_ === ring.right_inv_ === ring.inv_]
                [inv_(ring;x) == q]
                [is_ring_unit_(ring;x)]
                _L
            _L
        [not [[x,y :<- ring][x*y==p][not [is_ring_unit_(ring;x)]][not [is_ring_unit_(ring;y)]]]]
        [@[x,y :<- ring] -> [x*y==p] -> [not [[not [is_ring_unit_(ring;x)]][not [is_ring_unit_(ring;y)]]]]]
        [@[x,y :<- ring] -> [x*y==p] -> [[is_ring_unit_(ring;x)]or[is_ring_unit_(ring;y)]]]
        [is_irreducible_(ring;p)]
    [@[p :<- ring] -> [is_prime_(ring;p)] -> [is_irreducible_(ring;p)]]
    DONE
    ]]

PrincipalRing:Z_6 #ZZ%6
[ring := ZZ%6]:
    0, +-1: 0,1,5
    +-2: 2, 4
    3: 3
    [2 * 2 == -2]
    [2 * 3 == 0]
    [3 * 3 == 3]
    [2,3 reducible]

    [all multiples of 2 are 0,2,-2]
    [all divisors of +-2 are +-1,+-2]
    [2 divs one divisor of any multiple of 2]
    [2 prime]

    [all multiples of 3 are 0,3]
    [all divisors of 3 are +-1,3]
    [3 divs one divisor of any multiple of 3]
    [3 prime]

    # non-unique factorization into primes
    [2 == -2*2 == 2*2*2 == ...]
    [3 == 3*3 == 3*3*3 == ...]


[unit_ring > commutative_unit_ring > principal_ring > Euclidean_ring]
[commutative rings > integral domains > integrally closed domains > GCD domains > unique factorization domains > principal ideal domains > Euclidean domains > fields > finite fields]
[integral_domain > pre_Schreier_domain > Schreier_domain > gcd_domain > unique_factorization_domain]

[gcd_domain > unique_factorization_domain > principal_ideal_domain > Euclidean_domain]
[gcd_domain > Bezout_domain > principal_ideal_domain > Euclidean_domain]
Euclidean domain
.   |
.   v
.  PID           -> UFD
.   |                |
.   v                v
.  Bezout domain -> gcd domain


[[ring.is_gcd_domain()] =[def]= [[ring.is_integral_domain()][@[m,n :<- ring] -> [GCD(ring; m,n) =!= {}]]]]

[ring.is_mul_commutative()][not ring.is_trivial_ring()][u,v,k4u,k4v :<- ring]:
    [is_Bezout_coefficient_pair_of_(ring; u,v; k4u,k4v) =[def]= [k4u*u+k4v*v <- GCD(ring; u,v)]]

[ring.is_mul_commutative()][not ring.is_trivial_ring()]:
    # [Bezout_lemma =[def]= Bezout_identity]
    [ring.does_Bezout_identity_hold() =[def]= [@[u,v :<- ring] -> ?[k4u,k4v :<- ring] -> [is_Bezout_coefficient_pair_of_(ring; u,v; k4u,k4v)]]]
        # the above gcd condition is stronger than the mere existence of a gcd.
        # <==> [Ideal<u,v> == Ideal<gcd(u,v)>]
        # generally:[Ideal<u,v> <= Ideal<gcd(u,v)>]
        # when? -> [Ideal<u,v> < Ideal<gcd(u,v)>]
        # e.g. [Ideal<X,Y> < Ideal<gcd(X,Y)> == Ideal<1> == ring[X,Y]]
    #####
    [ring := int[x]]:
        [GCD(ring; 2*x, x**2) == {x,-x}]
        [GCD(ring; 2*x, x**2) /-\ Ideal<ring;{2*x, x**2}> == {}]
        [not ring.does_Bezout_identity_hold()]
    [not does_Bezout_identity_hold(int[x])]

# [[ring <- BezoutDomain] =[def]= [[ring <- IntegralDomain][ring.does_Bezout_identity_hold()]]]
[ring.is_Bezout_domain() =[def]= [[ring.is_integral_domain()][ring.does_Bezout_identity_hold()]]]
    see:is_every_finitely_generated_ideal_principal


[[K :<- Field] -> [is_principal_ideal_domain(K[x])]] #univariate polynomial_ring
# [[K :<- Field] -> [is_unique_factorization_domain(K[*xs])]]
[[K :<- UFD] -> [is_unique_factorization_domain(K[*xs])]]

[[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]]
[principal_ideal_ring === principal_ring]
[ring.is_principal_ring() =[def]= [[ring.is_commutative_unit_ring()][ring.is_every_ideal_principal()]]]
    #principal ring (sometimes also called a principal ideal ring) simply as a commutative unit ring (different from the zero ring) in which every ideal is principal, i.e., can be generated by a single element.
    #Principal rings are very useful because in a principal ring, any two nonzero elements have a well-defined greatest common divisor. Furthermore each nonzero, nonunit element in a principal ring has a unique factorization into prime elements (up to unit elements).
    #
    #『well-defined greatest common divisor』
    #   left_GCD,right_GCD? left-ideal/right-ideal/two-side-ideal?
    #   A<g> = ring*g
    #   B<g> = g*ring
    #   C<g> = ring*g*ring
    #
    #
    #bug:『nonzero, nonunit element』『has a unique factorization into prime elements (up to unit elements)』
    #   !! see:PrincipalRing:Z_6 #ZZ%6
    #   ZZ%6 : [3 is prime][3==3*3==3*3*3=...]
    #   prime include nonzero zero_divisor?
    #       if exclude, then counterexample for [NOT_ALWAYS [is_prime_ <: is_irreducible_]] is invalid


[[ring.is_domain()] -> @[p,q,d :<- ring] -> [d =!= 0] -> [[q*d == p*d]or[d*q == d*p]] -> [q==p]] # cancellation

Euclidean ring
    A ring without zero divisors in which an integer norm and an associated division algorithm (i.e., a Euclidean algorithm) can be defined.

#]]]'''
__all__ = r'''
IsTrivialRingError
ValidateError____divmod
    ValidateError____divmod____not__remainder_degree__lt__divisor_degree
NotMonicPolynomialError


MonoidOps4mul5IRingOps
CommutativeGroupOps4add5IRingOps

IBaseSemiringOps
    IBaseRingOps
        IRingOps
            pow__int_
            ICommutativeRingOps
                IPrincipalRingOps
                    IEuclideanRingOps
                        IEuclideanDomainOps
                            IFieldOps
            IBasePolynomialRingOps

IFieldOps
    IFieldOps___characteristic_is_0
        RationalFieldOps
            the_rational_field_ops
    IFieldOps___characteristic_is_prime
        IFiniteFieldOps
            PrimeFieldOps

IBasePolynomialRingOps
    IPolynomialRingOps
        validate__try_right_divmod_ex6IPolynomialRingOps_
        IPolynomialRingOps___coeff_ring_is_field
            is_divisor_of__6IPolynomialRingOps___coeff_ring_is_field_
    IIntegralDomainFractionFieldOps
        IPolynomialRingFractionFieldOps
    IPolynomialRingQuotientRingOps
        ICommutativePolynomialRingQuotientRingOps
            ICommutativePolynomialRingQuotientRingOps___modulus_is_monic_irreducible_polynomial
                IFiniteFieldIrreduciblePolynomialSplittingFieldOps

'''.split()#'''
__all__

___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.math.ops.algebra.IAlgebraOps import IAlgebraOps, NonInvertibleError, NonInvertibleError__not_injective, NonInvertibleError__out_of_domain, NonInvertibleError__not_implemented, NonInvertibleError__not_commutative
from seed.tiny import check_type_is
from seed.math.power_of import calc_power
#view ../../python3_src/seed/math/power_of.py
#def calc_power(I, T_2pow_ls, power:int, *, mul):


#from seed.math.ops.algebra.IGroupOps import IMagmaOps, IGroupoidOps, ISemigroupOps, IAssociativeMagmaOps, ICommutativeMagmaOps, IIdempotentMagmaOps, ISemilatticeOps, IQuasigroupOps, ICommutativeQuasigroupOps, IMagmaOps__has_identity4mul, ILoopOps, ILoopOps__has_inv, ICommutativeLoopOps, IMonoidOps, ICommutativeMonoidOps, IGroupOps, IAbelianGroupOps, ICommutativeGroupOps
from seed.math.ops.algebra.IGroupOps import IMonoidOps, ICommutativeMonoidOps, ICommutativeGroupOps



___end_mark_of_excluded_global_names__0___ = ...



class IsTrivialRingError(Exception):
    'try_right_divmod_ex cannot satisfy [get_imay_degree_(r) < get_imay_degree_(d)]'


class ValidateError____divmod(Exception):pass
class ValidateError____divmod____not__remainder_degree__lt__divisor_degree(ValidateError____divmod):pass
class NotMonicPolynomialError(Exception):pass



#xxx class ISemiringOps(IMonoidOps):
class IBaseSemiringOps(IAlgebraOps):
    r'''[[[
    Monoid<mul>
        identity4mul/one
    absorbing4mul/zero
        [0*x == 0 == x*0]

    Monoid<add>
        identity4add/zero
            [0+x == x == x+0]
    commutative add
    [absorbing4mul is identity4add]

    distributive mul add, left/right
    [[(a+b)*c == a*c + b*c][c*(a+b) == c*a + c*b]]

    #]]]'''#'''
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `get_commutative_monoid_ops4add
    `get_monoid_ops4mul
#concrete_methods:
    get_zero4mul
    is_mul_add_distributive
    is_zero4mul_zero4add
    '''#'''
    #___all___ = ...
    @abstractmethod
    def get_monoid_ops4mul(ops, /):
        'ops<z> -> monoid_ops4mul<z>/IMonoidOps'
    @abstractmethod
    def get_commutative_monoid_ops4add(ops, /):
        'ops<z> -> commutative_monoid_ops4add<z>/ICommutativeMonoidOps'

    def is_mul_add_distributive(ops, /):
        '[[(a+b)*c == a*c + b*c][c*(a+b) == c*a + c*b]]'
        return True
    def is_zero4mul_zero4add(ops, /):
        '[absorbing4mul is identity4add]'
        return True
    def get_zero4mul(ops, /):
        'ops<z> -> absorbing4mul/z'
        commutative_monoid_ops4add = ops.get_commutative_monoid_ops4add()
        zero4add = commutative_monoid_ops4add.get_identity4mul()
        zero4mul = zero4add
        return zero4mul

class IBaseRingOps(IBaseSemiringOps):
    r'''[[[
    Monoid<mul>
        identity4mul/one
    CommutativeGroup<add>
        identity4add/zero
        inv4add = neg_
        commutative add
    distributive mul add, left/right
    ==>>:
    [absorbing4mul is identity4add]
    [0*x == 0 == x*0]
        [[proof:
        [0*x+y*x
        #distributive
        == (0+y)*x
        #identity4add
        == y*x
        ]
        [0*x+y*x == y*x]
        #neg_
        [0*x == y*x - y*x]
        #identity4add
        [0 + y*x == y*x]
        #neg_
        [0 == y*x - y*x]
        !! [0*x == y*x - y*x]
        [0 == 0*x]
        同理:[0 == x*0]
        [0*x == 0 == x*0]
        DONE
        ]]
    #]]]'''#'''
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `get_commutative_group_ops4add
    `get_monoid_ops4mul
#concrete_methods:
    get_commutative_monoid_ops4add
    get_zero4mul
    is_mul_add_distributive
    is_zero4mul_zero4add
    '''#'''
    #___all___ = ...
    @abstractmethod
    def get_commutative_group_ops4add(ops, /):
        'ops<z> -> commutative_group_ops4add<z>/ICommutativeGroupOps'
    @override
    def get_commutative_monoid_ops4add(ops, /):
        'ops<z> -> commutative_monoid_ops4add<z>/ICommutativeMonoidOps'
        return ops.get_commutative_group_ops4add()

#class IRingOps(IAlgebraOps):
class IRingOps(IBaseRingOps):
    r'''[[[

    [ring :<- Ring][not [is_trivial_ring ring]]:
        [[is_domain ring] =[def]= [[a,b :<- ring] -> [a*b==0] -> [[a==0]or[b==0]]]]
    [ring :<- Ring]:
        [[is_integral_domain ring] =[def]= [][is_domain ring][is_mul_commutative]]

    !! [IRingOps.is_mul_associative()]
    !! [[is_mul_associative] -> [left_inv_ === right_inv_]]
    [IRingOps.left_inv_ === IRingOps.right_inv_ === IRingOps.inv_]



    ???try_truediv() requires is_mul_commutative()
        No. try_truediv is not truediv!
        * not is_mul_commutative():
            eg: [not is_mul_commutative()][try_truediv(n,-1)==-n]
        * not result commutative:
            eg: [try_inv_(x) but try_left_inv_(x) =!= try_right_inv_(x)]
            eg: [try_truediv(n,d) but try_left_div(n,d) =!= try_right_div(n,d)]
            NonInvertibleError__not_commutative
        * [int ring] => has no truediv (e.g. 1/2), but has [6/2==3]
            NonInvertibleError__out_of_domain
        * [square matrix ring] => has no truediv/inv_ (e.g. [1,0;0,0]**-1), but has [[1,1;0,1]**-1 == [1,-1;0,1]]
            NonInvertibleError__not_injective
        * try_truediv neednot find out all possible answer:
            NonInvertibleError__not_implemented

    try_truediv --> try_left_div/try_right_div
    try_inv_ --> try_left_inv_/try_right_inv_

    [[
    left_div,right_div
    left_inv_,right_inv_
    ===
    #eg:square matrix
    left_div:  [d*q == n][q := d\n]
        [d*left_div(n,d) == n]
        [left_div(n,d) == d\n]
        [d*(d\n) == n]
    right_div: [q*d == n][q := n/d]
        [right_div(n,d)*d == n]
        [right_div(n,d) == n/d]
        [(n/d)*d == n]

    left_inv_: [left_inv_(d)*d == 1]
        [left_inv_(d) == 1/d == right_div(1,d)]
        [(1/d)*d == 1]
    right_inv_: [d*right_inv_(d) == 1]
        [right_inv_(d) == d\1 == left_div(1,d)]
        [d*(d\1) == 1]
    ]]

    NOTE:
    [[
    left_inv_,right_inv_ =?= inv_
    ===
    [[left_inv_ =!= right_inv_] -> [[not is_mul_associative][not is_mul_commutative]]]
    <==>:
    [[is_mul_associative] -> [left_inv_ === right_inv_]]
    [[is_mul_commutative] -> [left_inv_ === right_inv_]]
    proof:
    [[is_mul_associative] -> [left_inv_ === right_inv_]]
        [[proof:
        [left_inv_(d)
        == left_inv_(d)*1
        !! [d*right_inv_(d) == 1]
        == left_inv_(d)*(d*right_inv_(d))
        !! [is_mul_associative]
        == (left_inv_(d)*d)*right_inv_(d)
        !! [left_inv_(d)*d == 1]
        == 1*right_inv_(d)
        == right_inv_(d)
        ]
        DONE
        ]]

    [[is_mul_commutative] -> [left_inv_ === right_inv_]]
        [[proof:
        [d*left_inv_(d)
        !! [is_mul_commutative]
        == left_inv_(d)*d
        !! [left_inv_(d)*d == 1]
        == 1
        !! [d*right_inv_(d) == 1]
        == d*right_inv_(d)
        ]
        DONE
        ]]
    ]]

    #]]]'''#'''
    __slots__ = ()
    #see above: py_adhoc_call
    ___all___ = r'''
#abstract_methods:
    `add
    `eq
    `get_characteristic
    `is_order_finite
    `get_xorder4add
    `get_xorder4mul
    `mk5int
    `mul
    `neg_
    `to_may_int_
#concrete_methods:
    eq_neg_one_
    eq_one_
    eq_zero_
    get_neg_one
    get_one
    get_zero
    is_int_
    ne
    pow__int_
    sub
    '''#'''
    #___all___
    ___all___ = r'''
#abstract_methods:
    `add
    `are_all_GCD_nonempty
    `contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring
    `does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements
    `eq
    `get_characteristic
    `get_xorder4add
    `get_xorder4mul
    `has_a_uint_norm4nonzero_elements_and_an_associated_divmod
    `has_nontrivial_zero_divisors
    `is_every_finitely_generated_ideal_principal
    `is_every_ideal_principal
    `is_every_nonzero_element_primal
    `is_every_nonzero_element_ring_uint
    `is_left_divisor_of_
    `is_mul_commutative
    `is_mul_idempotent
    `is_order_finite
    `is_multiplicative_group_order_finite
    `is_right_divisor_of_
    `mk5int
    `mul
    `neg_
    `to_may_int_
    `try_left_div
    `try_right_div
#concrete_methods:
    does_Bezout_identity_hold
    eq_neg_one_
    eq_one_
    eq_zero_
    get_commutative_group_ops4add
    get_commutative_monoid_ops4add
    get_monoid_ops4mul
    get_neg_one
    get_one
    get_zero
    get_zero4mul
    is_Bezout_domain
    is_Euclidean_domain
    is_Euclidean_ring
    is_Schreier_domain
    is_add_associative
    is_add_commutative
    is_add_idempotent
    is_commutative_ring
    is_commutative_unit_ring
    is_domain
    is_field
    is_finite_field
    is_gcd_domain
    is_int_
    is_integral_domain
    is_integrally_closed_domain
    is_invertable_
    is_lcm_domain
    is_mul_add_distributive
    is_mul_associative
    is_pre_Schreier_domain
    is_principal_ideal_domain
    is_principal_ideal_ring
    is_principal_ring
    is_trivial_ring
    is_unique_factorization_domain
    is_unit_ring
    is_zero4mul_zero4add
    is_zero_ring
    mul__flipped
    mul_ex
    ne
    pow__int_
    sub
    try_inv_
    try_left_div_ex
    try_left_inv_
    try_left_inv_ex_
    try_right_div_ex
    try_right_inv_
    try_right_inv_ex_
    try_truediv

    is_weak_divisor_of_
    is_strong_divisor_of_
    '''#'''
    #___all___ = ...

    # from:IBaseRingOps:
    @override
    def get_monoid_ops4mul(ops, /):
        'ops<z> -> monoid_ops4mul<z>/IMonoidOps'
        return MonoidOps4mul5IRingOps(ops)
    @override
    def get_commutative_group_ops4add(ops, /):
        'ops<z> -> commutative_group_ops4add<z>/ICommutativeGroupOps'
        return CommutativeGroupOps4add5IRingOps(ops)
    # required by CommutativeGroupOps4add5IRingOps/MonoidOps4mul5IRingOps
    ##@abstractmethod
    def is_mul_associative(ops, /):
        'ops<z> -> bool'
        return True
    @abstractmethod
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        return False
    @abstractmethod
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        return False
    ##@abstractmethod
    def is_add_associative(ops, /):
        'ops<z> -> bool'
        return True
    ##@abstractmethod
    def is_add_commutative(ops, /):
        'ops<z> -> bool'
        return True
    ##@abstractmethod
    def is_add_idempotent(ops, /):
        'ops<z> -> bool'
        # [(add x) is bijective]
        # [0 =!= 1] ==>> [len(Ring) >= 2]
        return False




    # ring type detect
    @abstractmethod
    def has_nontrivial_zero_divisors(ops, /):
        'ops<z> -> bool'
        return True
    @abstractmethod
    def contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring(ops, /):
        'ops<z> -> bool'
        return False
    @abstractmethod
    def is_every_nonzero_element_ring_uint(ops, /):
        'ops<z> -> bool #is_invertable_ === is_ring_unit_'
        return False
    @abstractmethod
    def is_every_nonzero_element_primal(ops, /):
        'ops<z> -> bool # ???[[ring.is_mul_commutative()][@[d :<- ring] -> [d =!= 0] -> [is_primal_(ring; d)]]]??? # see:is_primal_'
        return False
    @abstractmethod
    def are_all_GCD_nonempty(ops, /):
        'ops<z> -> bool # [[ring.is_mul_commutative()][not ring.is_trivial_ring()][@[m,n :<- ring] -> [GCD(ring; m,n) =!= {}]]]'
        return False
    @abstractmethod
    def is_every_finitely_generated_ideal_principal(ops, /):
        'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_finitely_generated_ideal_principal === does_Bezout_identity_hold === does_every_finite_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
        return False
    @abstractmethod
    def is_every_ideal_principal(ops, /):
        'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_ideal_principal < is_every_finitely_generated_ideal_principal] # [is_every_ideal_principal === does_every_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
        return False
    ##@abstractmethod
    def does_Bezout_identity_hold(ops, /):
        'ops<z> -> bool # Bezout_identity # [@[u,v :<- ring] -> ?[k4u,k4v :<- ring] -> [k4u*u+k4v*v == gcd(u,v)]]'
        # [[ring.does_Bezout_identity_hold()] -> @[m,n :<- ring] -> [Ideal<m> + Ideal<n> == Ideal<gcd(m,n)>]]
        return ops.is_every_finitely_generated_ideal_principal()

    @abstractmethod
    def does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements(ops, /):
        'ops<z> -> bool # <<== UFD'
        'ops<z> -> bool # <<== UFD or bug:PrincipalRing # but in PrincipalRing, prime may be reducible, eg ZZ%6 !! bug !! [3 is prime][3==3*3==3*3*3=...]'
        return False
    @abstractmethod
    def has_a_uint_norm4nonzero_elements_and_an_associated_divmod(ops, /):
        'ops<z> -> bool # (uint_norm4Euclidean_, divmod4Euclidean) since py.Fraction.__divmod__ not an Euclidean_divmod'
        return False

    # [unit_ring > commutative_unit_ring > principal_ring > Euclidean_ring]
    # [commutative rings > integral domains > integrally closed domains > GCD domains > unique factorization domains > principal ideal domains > Euclidean domains > fields > finite fields]
    # [integral_domain > pre_Schreier_domain > Schreier_domain > gcd_domain > unique_factorization_domain]
    # [gcd_domain > unique_factorization_domain > principal_ideal_domain > Euclidean_domain]
    # [gcd_domain > Bezout_domain > principal_ideal_domain > Euclidean_domain]

    def is_zero_ring(ops, /):
        'ops<z> -> bool'
        return ops.is_trivial_ring()
    def is_unit_ring(ops, /):
        'ops<z> -> bool'
        return not ops.is_zero_ring()

    def is_commutative_ring(ops, /):
        'ops<z> -> bool'
        return ops.is_mul_commutative()
    def is_commutative_unit_ring(ops, /):
        'ops<z> -> bool'
        return ops.is_unit_ring() and ops.is_mul_commutative()

    def is_principal_ring(ops, /):
        'ops<z> -> bool #vs:is_principal_ideal_domain'
        return ops.is_commutative_unit_ring() and ops.is_every_ideal_principal()
    def is_principal_ideal_ring(ops, /):
        'ops<z> -> bool'
        return ops.is_principal_ring()



    def is_domain(ops, /):
        'ops<z> -> bool'
        # [[using:def____2_is_prime_] -> [ring.is_domain()] -> [ring.is_prime_ <: ring.is_irreducible_]]
        # [[ring.is_domain()] -> @[p,q,d :<- ring] -> [d =!= 0] -> [[q*d == p*d]or[d*q == d*p]] -> [q==p]] # cancellation
        return not (ops.has_nontrivial_zero_divisors() or ops.is_trivial_ring())
    def is_integral_domain(ops, /):
        'ops<z> -> bool'
        # [NOT_ALWAYS [is_prime_ <: is_irreducible_]]
        #     !! see:PrincipalRing:Z_6 #ZZ%6
        # [[ring.is_integral_domain()] -> [ring.is_prime_ <: ring.is_irreducible_]]
        # field of fractions/quotients of an integral domain
        return ops.is_domain() and ops.is_mul_commutative()
    def is_integrally_closed_domain(ops, /):
        'ops<z> -> bool'
        return ops.is_integral_domain() and ops.contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring()
    def is_pre_Schreier_domain(ops, /):
        'ops<z> -> bool #pre-Schreier_domain'
        # [[ring.is_pre_Schreier_domain()] -> [ring.is_prime_ == ring.is_irreducible_]]
        return ops.is_integral_domain() and ops.is_every_nonzero_element_primal()
    def is_Schreier_domain(ops, /):
        'ops<z> -> bool #Schreier_domain'
        return ops.is_integrally_closed_domain() and ops.is_every_nonzero_element_primal()
        return ops.is_pre_Schreier_domain() and ops.is_integrally_closed_domain()
    def is_gcd_domain(ops, /):
        'ops<z> -> bool #gcd(greatest common divisor)'
        # [[ring.is_gcd_domain()] =[def]= [[ring.is_integral_domain()][@[m,n :<- ring] -> [GCD(ring; m,n) =!= {}]]]]
        return ops.is_integral_domain() and ops.are_all_GCD_nonempty()
    def is_lcm_domain(ops, /):
        'ops<z> -> bool #lcm(least common multiple)'
        return ops.is_gcd_domain()
    def is_Bezout_domain(ops, /):
        'ops<z> -> bool # Bezout_domain'
        # [[ring <- BezoutDomain] =[def]= [[ring <- IntegralDomain][ring.does_Bezout_identity_hold()]]]
        # [[ring.does_Bezout_identity_hold()] -> @[m,n :<- ring] -> [Ideal<m> + Ideal<n> == Ideal<gcd(m,n)>]]
        return ops.is_integral_domain() and ops.is_every_finitely_generated_ideal_principal()
        return ops.is_integral_domain() and ops.does_Bezout_identity_hold()
        return ops.is_gcd_domain() and ops.is_every_finitely_generated_ideal_principal()
    def is_unique_factorization_domain(ops, /):
        'ops<z> -> bool #UFD(unique factorization domain)'
        # [[K :<- Field] -> [is_principal_ideal_domain(K[x])]] #univariate polynomial_ring
        # # [[K :<- Field] -> [is_unique_factorization_domain(K[*xs])]]
        # [[K :<- UFD] -> [is_unique_factorization_domain(K[*xs])]]
        return ops.is_integral_domain() and ops.does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements()
        return ops.is_gcd_domain() and ops.does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements()
    def is_principal_ideal_domain(ops, /):
        'ops<z> -> bool #PID(principal ideal domain) #vs:is_principal_ring'
        return ops.is_integral_domain() and ops.is_every_ideal_principal()
        return ops.is_integral_domain() and ops.is_principal_ring()
        return ops.is_unique_factorization_domain() and ops.is_Bezout_domain() and ops.is_every_ideal_principal()
    def is_Euclidean_ring(ops, /):
        'ops<z> -> bool # [can use Euclidean_algorithm to find gcd(m,n)]'
        return ops.is_principal_ring() and ops.has_a_uint_norm4nonzero_elements_and_an_associated_divmod()

    def is_Euclidean_domain(ops, /):
        'ops<z> -> bool # [can use Euclidean_algorithm to find gcd(m,n)]'
        return ops.is_principal_ideal_domain() and ops.has_a_uint_norm4nonzero_elements_and_an_associated_divmod()
        return ops.is_principal_ideal_domain() and ops.is_Euclidean_ring()
    def is_field(ops, /):
        'ops<z> -> bool'
        return ops.is_mul_commutative() and ops.is_every_nonzero_element_ring_uint() and not ops.is_trivial_ring()
        return ops.is_Euclidean_domain() and ops.is_every_nonzero_element_ring_uint()
    def is_finite_field(ops, /):
        'ops<z> -> bool'
        return ops.is_order_finite() and ops.is_field()
    @abstractmethod
    def is_left_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool #[[is_left_divisor_of_(ring;n;d)] <-> [is_right_multiple_of_(d;n)] <-> [?[q :<- ring] -> [d*q == n]]] # not use try_left_div_ex, since not require output unique'
    @abstractmethod
    def is_right_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool #[[is_right_divisor_of_(ring;n;d)] <-> [is_left_multiple_of_(d;n)] <-> [?[q :<- ring] -> [q*d == n]]] # not use try_right_inv_ex_, since not require output unique'

    def is_weak_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool # [[is_weak_divisor_of_(ring;n;d)] = [is_weak_multiple_of_(d;n)] =[def]= [[is_left_divisor_of_(ring;n;d)]or[is_right_divisor_of_(ring;n;d)]]]'
        return ops.is_right_divisor_of_(n, d) or (not ops.is_mul_commutative() and ops.is_left_divisor_of_(n, d))
    def is_strong_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool # [[is_strong_divisor_of_(ring;n;d)] = [is_strong_multiple_of_(d;n)] =[def]= [[is_left_divisor_of_(ring;n;d)][is_right_divisor_of_(ring;n;d)]]]'
        return ops.is_right_divisor_of_(n, d) and (ops.is_mul_commutative() or ops.is_left_divisor_of_(n, d))





    # normal API for IRingOps:
    @abstractmethod
    def get_characteristic(ops, /):
        'ops<z> -> (0|1|prime)/uint{==0|>=2} # 1=>is_zero_ring'
        return 0
    @abstractmethod
    def is_order_finite(ops, /):
        'ops<z> -> bool # order4add # order of additive_group/whole ring'
        return False
    @abstractmethod
    def is_multiplicative_group_order_finite(ops, /):
        'ops<z> -> bool # order4mul # order of multiplicative_group # [ZZ.multiplicative_group == {-1,+1}]'
    @abstractmethod
    def get_xorder4add(ops, /):
        'ops<z> -> xorder4add/(-1|uint|...) #(-1 if not is_order_finite() else (order4add/uint if known else ...)) # '
        return (-1 if not ops.is_order_finite() else ...)
    @abstractmethod
    def get_xorder4mul(ops, /):
        'ops<z> -> xorder4mul/(-1|uint|...) #(-1 if not is_order_finite<multiplicative_group>() else (order4mul/uint if known else ...)) # '
        # order of multiplicative_group
        # number of ring units
        raise 000
        #bug:
        return (-1 if not ops.is_order_finite() else ...)
        #only field:
        xorder4add = ops.get_xorder4add()
        if xorder4add is ...:
            return ...
        elif xorder4add < 1:
            # -1, 0
            # inf, [0==1]
            xorder4mul = xorder4add
        else:
            xorder4mul = xorder4add -1
        return xorder4mul

    if 0:
        @abstractmethod
        def is_field(ops, /):
            'ops<z> -> bool'
            return False

    @abstractmethod
    def eq(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> bool'


    @abstractmethod
    def add(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
    @abstractmethod
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
    @abstractmethod
    def neg_(ops, rhs, /):
        'ops<z> -> z -> z'
    @abstractmethod
    def mk5int(ops, i, /):
        'ops<z> -> int -> z'
    @abstractmethod
    def to_may_int_(ops, rhs, /):
        'ops<z> -> z -> (None|int)'
    def is_int_(ops, rhs, /):
        'ops<z> -> z -> bool'
        return not ops.to_may_int_(rhs) is None

    def get_zero(ops, /):
        'ops<z> -> z'
        return ops.mk5int(0)
    def get_one(ops, /):
        'ops<z> -> z'
        return ops.mk5int(1)
    def get_neg_one(ops, /):
        'ops<z> -> z'
        return ops.mk5int(-1)

    def sub(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return ops.add(lhs, ops.neg_(rhs))
    def pow__int_(ops, lhs, idx, /, *, double_pows):
        'ops<z> -> z -> int -> z|^NonInvertibleError'
        return pow__int_(ops, lhs, idx, double_pows=double_pows)

    def ne(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> bool'
        return not ops.eq(lhs, rhs)

    def eq_zero_(ops, lhs, /):
        'ops<z> -> z -> bool'
        return ops.eq(lhs, ops.get_zero())
    def eq_one_(ops, lhs, /):
        'ops<z> -> z -> bool'
        return ops.eq(lhs, ops.get_one())
    def eq_neg_one_(ops, lhs, /):
        'ops<z> -> z -> bool'
        return ops.eq(lhs, ops.get_neg_one())
    def is_trivial_ring(ops, /):
        'ops<z> -> bool'
        return ops.eq_zero_(ops.get_one())

    #@newmethod
    #@abstractmethod
    def try_inv_(ops, rhs, /):
        'ops<z> -> z -> z|^NonInvertibleError'
        return ops.try_truediv(ops.get_one(), rhs)
    #@newmethod
    def try_left_inv_(ops, z, /):
        'ops<z> -> z -> z|^NonInvertibleError # [left_inv_(d)*d == 1]'
        # !! [IRingOps.left_inv_ === IRingOps.right_inv_ === IRingOps.inv_]
        return ops.try_inv_(z)
        return ops.try_right_div(ops.get_one(), z)
    #@newmethod
    def try_right_inv_(ops, z, /):
        'ops<z> -> z -> z|^NonInvertibleError # [d*right_inv_(d) == 1]'
        # !! [IRingOps.left_inv_ === IRingOps.right_inv_ === IRingOps.inv_]
        return ops.try_inv_(z)
        return ops.try_left_div(ops.get_one(), z)
    #@newmethod
    def try_left_inv_ex_(ops, z, /, *, reverse:bool):
        'ops<z> -> z -> z|^NonInvertibleError # [left_inv_(d)*d == 1]'
        return ops.try_right_inv_ex_(z, reverse=not reverse)
    #@newmethod
    def try_right_inv_ex_(ops, z, /, *, reverse:bool):
        'ops<z> -> z -> z|^NonInvertibleError # [d*right_inv_(d) == 1]'
        if reverse:
            _inv_ = ops.try_left_inv_
        else:
            _inv_ = ops.try_right_inv_
        return _inv_(z)
    #@newmethod
    def is_invertable_(ops, rhs, /):
        'ops<z> -> z -> bool #is_ring_unit_ #[0=>False][+1/-1=>True] #square matrix'
        try:
            ops.try_inv_(rhs)
        except NonInvertibleError:
            return False
        return True
    #@newmethod
    #@abstractmethod
    def try_truediv(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError'
        qL = ops.try_left_div(lhs, rhs)
        #assert ops.eq(lhs, ops.mul(rhs, qL))
        if 0:
            qR = ops.try_right_div(lhs, rhs)
            #assert ops.eq(lhs, ops.mul(qR, rhs))
            if ops.eq(qL, qR):
                q = qR = qL
        if ops.is_mul_commutative() or ops.eq(lhs, ops.mul(qL, rhs)):
            qR = qL
            q = qR = qL
            return q
        raise NonInvertibleError__not_commutative(r'[(n/d) =!= (d\n)]')
        raise 000
        # now try_inv_() using try_truediv()
        #   [int ring] ==>> [1/2 --> NonInvertibleError__out_of_domain][6/2 == 3]
        # NonInvertibleError__not_injective
        # NonInvertibleError__out_of_domain
        inv_rhs = ops.try_inv_(rhs)
                    # ^NonInvertibleError
        return ops.mul(lhs, inv_rhs)
    #@newmethod
    @abstractmethod
    def try_left_div(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [d*left_div(n,d) == n]'
    #@newmethod
    @abstractmethod
    def try_right_div(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [right_div(n,d)*d == n]'
    #@newmethod
    def try_left_div_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [d*left_div(n,d) == n]'
        return ops.try_right_div_ex(lhs, rhs, reverse=not reverse)
    #@newmethod
    def try_right_div_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [right_div(n,d)*d == n]'
        if reverse:
            _div_ = ops.try_left_div
        else:
            _div_ = ops.try_right_div
        return _div_(lhs, rhs)
    #@newmethod
    def mul__flipped(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return ops.mul(rhs, lhs)
    #@newmethod
    def mul_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> z'
        _mul_ = ops.mul__flipped if reverse else ops.mul
        return _mul_(lhs, rhs)
#ICommutativeRingOps
def _init__double_pows(double_pows, lhs, /):
    if double_pows is None:
        double_pows = []
    if not double_pows:
        double_pows.append(lhs)
    if not double_pows[0] is lhs: raise logic-err
    return double_pows
def pow__int_(ops, lhs, idx, /, *, double_pows):
    'ops<z> -> z -> int -> z|^NonInvertibleError'
    check_type_is(int, idx)
    if idx == 1:
        return lhs
    # [idx =!= 1]
    if ops.eq_zero_(lhs):
        if idx <= 0:
            raise NonInvertibleError #NaNError
        return lhs
    if ops.eq_one_(lhs):
        return lhs
    if ops.eq_neg_one_(lhs):
        return lhs if idx&1 else ops.get_one()

    # [lhs <-/- {0,1,-1}]
    # [idx =!= 1]
    if idx <= 0:
        # [idx <= 0]
        if idx == 0:
            return ops.get_one()
        # [idx <= -1]
        if ops.is_field() and ops.is_order_finite():
            q_1 = ops.get_order4mul()
            idx %= q_1
            # [idx <- {0..=q-2}]
            if idx == 0:
                return ops.get_one()
            # [idx <- {1..=q-2}]
            # [idx >= 1]
        else:
            # [lhs <-/- {0,1,-1}]
            #lhs = ops.inv_(lhs)
            lhs = ops.try_inv_(lhs)
            # [lhs <-/- {0,1,-1}]
            idx = -idx
            # [idx >= 1]
            double_pows = [lhs]
        # [idx >= 1]
        if idx == 1:
            return lhs
        # [idx >= 2]
    else:
        # [idx =!= 1][idx > 0]
        pass
        # [idx >= 2]
    # [idx >= 2]
    assert idx > 1

    double_pows = _init__double_pows(double_pows, lhs)
    assert double_pows
    assert double_pows[0] is lhs


    if len(double_pows) < 2:
        square = ops.mul(lhs, lhs)
        double_pows.append(square)
    else:
        square = double_pows[1]
    assert square is double_pows[1]

    # [idx >= 2]
    if idx == 2:
        return square
    # [idx >= 3]
    if 0:
        if ops.eq_one_(square):
            if idx&1:
                # [idx%2 == 1]
                return lhs
            # [idx%2 == 0]
            return square #ops.get_one()

    r = calc_power(None, double_pows, idx, mul=ops.mul)
    return r



class MonoidOps4mul5IRingOps(IMonoidOps):
    ___no_slots_ok___ = True
    #___all___ = {'mul', 'get_identity4mul', 'is_mul_commutative', 'is_mul_idempotent'}
    def __init__(sf, ops:IRingOps, /):
        sf._ops = ops
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        ops = object.__getattribute__(ops, '_ops')
        return ops.mul(lhs, rhs)
    @override
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        ops = object.__getattribute__(ops, '_ops')
        return ops.is_mul_commutative()
    @override
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        ops = object.__getattribute__(ops, '_ops')
        return ops.is_mul_idempotent()
    @override
    def get_identity4mul(ops, /):
        'ops<z> -> identity4mul/z'
        ops = object.__getattribute__(ops, '_ops')
        return ops.get_one()

    @override
    def is_order_finite(ops, /):
        'ops<z> -> bool'
        ops = object.__getattribute__(ops, '_ops')
        return ops.is_multiplicative_group_order_finite()
        return ops.is_order_finite()
    @override
    def get_xorder4mul(ops, /):
        'ops<z> -> xorder4mul/(-1|uint|...) #(-1 if not is_order_finite<multiplicative_group>() else (order4mul/uint if known else ...)) # '
        ops = object.__getattribute__(ops, '_ops')
        return ops.get_xorder4mul()

    pass
class CommutativeGroupOps4add5IRingOps(ICommutativeGroupOps):
    ___no_slots_ok___ = True
    #___all___ = {'inv_', 'get_identity4mul', 'is_mul_idempotent', 'mul'}
    def __init__(sf, ops:IRingOps, /):
        sf._ops = ops
    @override
    def inv_(ops, d, /):
        r'ops<z> -> d/z -> q/z # [q := (1/d)][(1/d)*d == 1 == d*(1/d)]'
        ops = object.__getattribute__(ops, '_ops')
        # [mul := add]
        return ops.neg_(d)
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        ops = object.__getattribute__(ops, '_ops')
        # [mul := add]
        return ops.add(lhs, rhs)
    @override
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        ops = object.__getattribute__(ops, '_ops')
        # [mul := add]
        return False
        #return ops.is_add_idempotent()
    @override
    def get_identity4mul(ops, /):
        'ops<z> -> identity4mul/z'
        ops = object.__getattribute__(ops, '_ops')
        # [mul := add]
        return ops.get_zero()

    @override
    def is_order_finite(ops, /):
        'ops<z> -> bool'
        ops = object.__getattribute__(ops, '_ops')
        # [mul := add]
        return ops.is_order_finite()
    @override
    def get_xorder4mul(ops, /):
        'ops<z> -> xorder4mul/(-1|uint|...) #(-1 if not is_order_finite<multiplicative_group>() else (order4mul/uint if known else ...)) # '
        ops = object.__getattribute__(ops, '_ops')
        # [mul := add]
        return ops.get_xorder4add()


    pass
assert not (MonoidOps4mul5IRingOps.__abstractmethods__ or CommutativeGroupOps4add5IRingOps.__abstractmethods__), (MonoidOps4mul5IRingOps.__abstractmethods__, CommutativeGroupOps4add5IRingOps.__abstractmethods__)
    # AssertionError: (frozenset({'mul', 'get_identity4mul', 'is_mul_commutative', 'is_mul_idempotent'}), frozenset({'inv_', 'get_identity4mul', 'is_mul_idempotent', 'mul'}))




class ICommutativeRingOps(IRingOps):
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
    `is_divisor_of_
    '''#'''
    #___all___

    @override
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        return True
    @classmethod
    @override
    def __instancehook__(cls, ops, /):
        # ABCMeta::__instancehook__
        if cls is __class__:
            return isinstance(ops, IRingOps) and ops.is_mul_commutative()
        return NotImplemented


    #@newmethod
    @abstractmethod
    def is_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool # is_mul_commutative => [is_divisor_of_ === is_strong_divisor_of_]'
    #@not-newmethod
    @abstractmethod
    def try_truediv(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError'
    @override
    def try_left_div(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [d*left_div(n,d) == n]'
        return ops.try_truediv(lhs, rhs)
    @override
    def try_right_div(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [right_div(n,d)*d == n]'
        return ops.try_truediv(lhs, rhs)
    @override
    def is_left_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool #[[is_left_divisor_of_(ring;n;d)] <-> [is_right_multiple_of_(d;n)] <-> [?[q :<- ring] -> [d*q == n]]] # not use try_left_div_ex, since not require output unique'
        return ops.is_divisor_of_(n, d)
        return ops.is_right_divisor_of_(n, d)
    @override
    def is_right_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool #[[is_right_divisor_of_(ring;n;d)] <-> [is_left_multiple_of_(d;n)] <-> [?[q :<- ring] -> [q*d == n]]] # not use try_right_inv_ex_, since not require output unique'
        return ops.is_divisor_of_(n, d)

class IPrincipalRingOps(ICommutativeRingOps):
    __slots__ = ()

    # ring type detect
    @override
    def are_all_GCD_nonempty(ops, /):
        'ops<z> -> bool # [[ring.is_mul_commutative()][not ring.is_trivial_ring()][@[m,n :<- ring] -> [GCD(ring; m,n) =!= {}]]]'
        return True
    @override
    def is_every_finitely_generated_ideal_principal(ops, /):
        'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_finitely_generated_ideal_principal === does_Bezout_identity_hold === does_every_finite_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
        return True
    @override
    def is_every_ideal_principal(ops, /):
        'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_ideal_principal < is_every_finitely_generated_ideal_principal] # [is_every_ideal_principal === does_every_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
        return True


class IEuclideanRingOps(IPrincipalRingOps):
    r'''[[[
    TODO:
    @override
    `is_right_divisor_of_
    @override
    `try_truediv
    #]]]'''#'''
    __slots__ = ()

    ___bases4all___ = True
    ___all___ = r'''
#abstract_methods:
    `add
    `contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring
    `divmod4Euclidean
    `does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements
    `eq
    `get_characteristic
    `get_xorder4add
    `has_nontrivial_zero_divisors
    `is_every_nonzero_element_primal
    `is_every_nonzero_element_ring_uint
    `is_mul_idempotent
    `is_order_finite
    `is_right_divisor_of_
    `mk5int
    `mul
    `neg_
    `to_may_int_
    `try_truediv
    `uint_norm4Euclidean_
    '''#'''
    #___all___
    @abstractmethod
    def uint_norm4Euclidean_(ops, z, /):
        'ops<z> -> z -> uint'
    @abstractmethod
    def divmod4Euclidean(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError'


    # ring type detect
    @override
    def has_a_uint_norm4nonzero_elements_and_an_associated_divmod(ops, /):
        'ops<z> -> bool # (uint_norm4Euclidean_, divmod4Euclidean) since py.Fraction.__divmod__ not an Euclidean_divmod'
        return True



class IEuclideanDomainOps(IEuclideanRingOps):
    __slots__ = ()
    # ring type detect
    @override
    def has_nontrivial_zero_divisors(ops, /):
        'ops<z> -> bool'
        return False
    @override
    def contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring(ops, /):
        'ops<z> -> bool'
        return True
    @override
    def is_every_nonzero_element_primal(ops, /):
        'ops<z> -> bool # ???[[ring.is_mul_commutative()][@[d :<- ring] -> [d =!= 0] -> [is_primal_(ring; d)]]]??? # see:is_primal_'
        return True

    @override
    def does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements(ops, /):
        'ops<z> -> bool # <<== UFD'
        'ops<z> -> bool # <<== UFD or bug:PrincipalRing # but in PrincipalRing, prime may be reducible, eg ZZ%6 !! bug !! [3 is prime][3==3*3==3*3*3=...]'
        return True



class IFieldOps(IEuclideanDomainOps):
    __slots__ = ()
    #see above: py_adhoc_call
    ___all___ = r'''
#abstract_methods:
    `add
    `eq
    `get_characteristic
    `inv_
    `is_order_finite
    `get_xorder4add
    `mk5int
    `mul
    `neg_
    `to_may_int_
#concrete_methods:
    eq_neg_one_
    eq_one_
    eq_zero_
    get_neg_one
    get_one
    get_zero
    is_int_
    ne
    pow__int_
    sub
    truediv
    '''#'''
    #___all___
    ___all___ = r'''
#abstract_methods:
    `add
    `eq
    `get_characteristic
    `get_xorder4add
    `inv_
    `is_order_finite
    `mk5int
    `mul
    `neg_
    `to_may_int_
#concrete_methods:
    are_all_GCD_nonempty
    contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring
    divmod4Euclidean
    does_Bezout_identity_hold
    does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements
    eq_neg_one_
    eq_one_
    eq_zero_
    get_commutative_group_ops4add
    get_commutative_monoid_ops4add
    get_monoid_ops4mul
    get_neg_one
    get_one
    get_xorder4mul
    get_zero
    get_zero4mul
    has_a_uint_norm4nonzero_elements_and_an_associated_divmod
    has_nontrivial_zero_divisors
    is_Bezout_domain
    is_Euclidean_domain
    is_Euclidean_ring
    is_Schreier_domain
    is_add_associative
    is_add_commutative
    is_add_idempotent
    is_commutative_ring
    is_commutative_unit_ring
    is_domain
    is_every_finitely_generated_ideal_principal
    is_every_ideal_principal
    is_every_nonzero_element_primal
    is_every_nonzero_element_ring_uint
    is_field
    is_finite_field
    is_gcd_domain
    is_int_
    is_integral_domain
    is_integrally_closed_domain
    is_invertable_
    is_lcm_domain
    is_left_divisor_of_
    is_mul_add_distributive
    is_mul_associative
    is_mul_commutative
    is_mul_idempotent
    is_multiplicative_group_order_finite
    is_pre_Schreier_domain
    is_principal_ideal_domain
    is_principal_ideal_ring
    is_principal_ring
    is_right_divisor_of_
    is_trivial_ring
    is_unique_factorization_domain
    is_unit_ring
    is_zero4mul_zero4add
    is_zero_ring
    mul__flipped
    mul_ex
    ne
    pow__int_
    sub
    truediv
    try_inv_
    try_left_div
    try_left_div_ex
    try_left_inv_
    try_left_inv_ex_
    try_right_div
    try_right_div_ex
    try_right_inv_
    try_right_inv_ex_
    try_truediv
    uint_norm4Euclidean_

    is_divisor_of_
    is_weak_divisor_of_
    is_strong_divisor_of_
    '''#'''
    #___all___ = ...
    @abstractmethod
    def inv_(ops, rhs, /):
        'ops<z> -> z -> z|^NonInvertibleError'
    #@newmethod
    def truediv(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError'
        return ops.mul(lhs, ops.inv_(rhs))
    if 1:
        @override
        def is_field(ops, /):
            'ops<z> -> bool'
            return True
    @override
    def is_multiplicative_group_order_finite(ops, /):
        'ops<z> -> bool # order4mul # order of multiplicative_group # [ZZ.multiplicative_group == {-1,+1}]'
        return ops.is_order_finite()
    @override
    def try_inv_(ops, rhs, /):
        'ops<z> -> z -> z|^NonInvertibleError'
        return ops.inv_(rhs)
    @override
    def try_truediv(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError'
        return ops.truediv(lhs, rhs)
    @override
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        # [(mul x) is bijective except [x==0]]
        # [0 =!= 1] ==>> [len(Field\-\{0}) >= 1]
        # [Field is GF(2)] <==> [len(Field\-\{0}) == 1] <==> [mul is idempotent]
        #
        # [x*x == x] <-> [(x-0)*(x-1) == 0] <-> [x <- {0,1}]
        # [mul is idempotent]
        #   <-> [@[x <- Field] -> [x*x == x]]
        #   <-> [@[x <- Field] -> [x <- {0,1}]]
        #   <-> [all_elements_of(Field) |<=| {0,1}]
        #   <-> [Field is GF(2)]
        return (ops.is_order_finite() and ops.get_characteristic() == 2 and ops.get_order4add() == 2)
        #return False

    # ring type detect
    @override
    def is_every_nonzero_element_ring_uint(ops, /):
        'ops<z> -> bool #is_invertable_ === is_ring_unit_'
        return True

    @override
    def is_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool # is_mul_commutative => [is_divisor_of_ === is_strong_divisor_of_]'
        return (not ops.eq_zero_(d)) or ops.eq_zero_(n)
        if ops.eq_zero_(n):
            return True
        if ops.eq_zero_(d):
            return False
        return True

    @override
    def uint_norm4Euclidean_(ops, z, /):
        'ops<z> -> z -> uint'
        return 1-ops.eq_zero_(z)
    @override
    def divmod4Euclidean(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError'
        q = ops.truediv(lhs, rhs)
        r = ops.get_zero()
        return (q, r)

    @override
    def get_xorder4mul(ops, /):
        'ops<z> -> xorder4mul/(-1|uint|...) #(-1 if not is_order_finite<multiplicative_group>() else (order4mul/uint if known else ...)) # '
        #only field:
        xorder4add = ops.get_xorder4add()
        if xorder4add is ...:
            return ...
        elif xorder4add < 1:
            # -1, 0
            # inf, [0==1]
            xorder4mul = xorder4add
        else:
            xorder4mul = xorder4add -1
        return xorder4mul
class IFieldOps___characteristic_is_0(IFieldOps):
    __slots__ = ()
    #see above: py_adhoc_call
    ___bases4all___ = True
    ___all___ = r'''
#abstract_methods:
    `add
    `eq
    `inv_
    `mk5Fraction
    `mul
    `neg_
    `to_may_Fraction_
#concrete_methods:
    eq_neg_one_
    eq_one_
    eq_zero_
    get_characteristic
    get_neg_one
    get_one
    get_rational_field_ops
    get_zero
    is_Fraction_
    is_int_
    is_order_finite
    get_xorder4add
    mk5int
    ne
    pow__int_
    sub
    to_may_int_
    truediv
    '''#'''
    #___all___
    @override
    def get_characteristic(ops, /):
        'ops<z> -> (0|1|prime)/uint{==0|>=2} # 1=>is_zero_ring'
        'ops<z> -> (0|prime)/uint{==0|>=2}'
        return 0
    def get_rational_field_ops(ops, /):
        'ops<z> -> RationalFieldOps'
        return the_rational_field_ops #RationalFieldOps()

    @override
    def is_order_finite(ops, /):
        'ops<z> -> bool'
        return False
    @override
    def get_xorder4add(ops, /):
        'ops<z> -> xorder4add/(-1|uint|...) #(-1 if not is_order_finite() else (order4add/uint if known else ...)) # '
        return -1


    @abstractmethod
    def mk5Fraction(ops, fr, /):
        'ops<z> -> Fraction -> z'
    @abstractmethod
    def to_may_Fraction_(ops, rhs, /):
        'ops<z> -> z -> (None|Fraction)'
    def is_Fraction_(ops, rhs, /):
        'ops<z> -> z -> bool'
        return not ops.to_may_Fraction_(rhs) is None
    @override
    def mk5int(ops, i, /):
        'ops<z> -> int -> z'
        return ops.mk5Fraction(Fraction(int.__index__(i)))
    @override
    def to_may_int_(ops, rhs, /):
        'ops<z> -> z -> (None|int)'
        m = ops.to_may_Fraction_(rhs)
        if not m is None:
            fr = m
            if fr.denominator == 1:
                i = fr.numerator
                m = i
            else:
                m = None
        return m

class IFieldOps___characteristic_is_prime(IFieldOps):
    __slots__ = ()
    #see above: py_adhoc_call
    ___bases4all___ = True
    ___all___ = r'''
#abstract_methods:
    `add
    `eq
    `get_prime_characteristic
    `inv_
    `is_order_finite
    `get_xorder4add
    `mk5int
    `mul
    `neg_
    `to_may_int_
#concrete_methods:
    eq_neg_one_
    eq_one_
    eq_zero_
    get_characteristic
    get_neg_one
    get_one
    get_prime_field_ops
    get_zero
    is_int_
    ne
    pow__int_
    sub
    truediv
    '''#'''
    #___all___

    @abstractmethod
    def get_prime_characteristic(ops, /):
        'ops<z> -> prime/uint{>=2}'
        #return ops.get_prime_field_ops.get_prime_characteristic()
    def get_prime_field_ops(ops, /):
        'ops<z> -> PrimeFieldOps'
        p = ops.get_prime_characteristic()
        return PrimeFieldOps(p)
    @override
    def get_characteristic(ops, /):
        'ops<z> -> (0|1|prime)/uint{==0|>=2} # 1=>is_zero_ring'
        'ops<z> -> (0|prime)/uint{==0|>=2}'
        return ops.get_prime_characteristic()






class IFiniteFieldOps(IFieldOps___characteristic_is_prime):
    r'''[[[
finite field === Galois field/GF
    In a finite field of order q, the polynomial (X**q − X) has all q elements of the finite field as roots. The non-zero elements of a finite field form a multiplicative group. This group is cyclic, so all non-zero elements can be expressed as powers of a single element called a primitive element of the field.

When n>1, GF(p^n) can be represented as the field of equivalence classes of polynomials whose coefficients belong to GF(p).
For any prime or prime power q and any positive integer n, there exists a primitive irreducible polynomial of degree n over GF(q).


splitting field for the polynomial
    if f(x) irreducible over K and K is finite field:
        splitting field of f(x) in K[x] <==> K[x]%f(x)
quotient ring of polynomial ring
    K[x]/<f(x)>
    # K[x]%f(x)
fraction field of polynomial ring
    {f/g}


    #]]]'''#'''
    __slots__ = ()
    #see above: py_adhoc_call
    ___bases4all___ = True
    ___all___ = r'''
#abstract_methods:
    `add
    `eq
    `get_logarithm_of_order__base_prime_characteristic
    `get_prime_characteristic
    `inv_
    `mk5int
    `mul
    `neg_
    `to_may_int_
#concrete_methods:
    eq_neg_one_
    eq_one_
    eq_zero_
    get_characteristic
    get_neg_one
    get_one
    get_order4add
    get_order4mul
    get_prime_field_ops
    get_zero
    is_int_
    is_order_finite
    get_xorder4add
    ne
    pow__int_
    sub
    truediv
    '''#'''
    #___all___

    @override
    def is_order_finite(ops, /):
        'ops<z> -> bool'
        return True
    @override
    def get_xorder4add(ops, /):
        'ops<z> -> xorder4add/(-1|uint|...) #(-1 if not is_order_finite() else (order4add/uint if known else ...)) # '
        return ops.get_order4add()

    @abstractmethod
    def get_logarithm_of_order__base_prime_characteristic(ops, /):
        'ops<z> -> logarithm/uint{>=1}'

    def get_order4add(ops, /):
        'ops<z> -> uint{>=2}'
        p = ops.get_prime_characteristic()
        m = ops.get_logarithm_of_order__base_prime_characteristic()
        q = p**m
        return q
    def get_order4mul(ops, /):
        'ops<z> -> uint{>=1}'
        q = ops.get_order4add()
        return q-1

___begin_mark_of_excluded_global_names__1___ = ...
from seed.abc.ISingleton import ISingleton
from numbers import Rational
from fractions import Fraction
___end_mark_of_excluded_global_names__1___ = ...

_Fraction0 = Fraction(0)
_Fraction1 = Fraction(1)
_Fraction_neg1 = Fraction(-1)
class RationalFieldOps(IFieldOps___characteristic_is_0, ISingleton):
    '[z =[def]= Fraction]'
    #__slots__ = ()
    ___no_slots_ok___ = True
    #___all___ = ...

    @override
    def get_rational_field_ops(ops, /):
        'ops<z> -> RationalFieldOps'
        return ops


    @override
    def eq(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> bool'
        return Fraction.__eq__(lhs, rhs)


    @override
    def add(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return Fraction.__add__(lhs, rhs)
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return Fraction.__mul__(lhs, rhs)
    @override
    def neg_(ops, rhs, /):
        'ops<z> -> z -> z'
        return Fraction.__neg__(rhs)
    @override
    def inv_(ops, rhs, /):
        'ops<z> -> z -> z|^NonInvertibleError'
        #Fraction.as_integer_ratio(rhs)
        return Fraction.__truediv__(_Fraction1, rhs)
    @override
    def mk5Fraction(ops, fr, /):
        'ops<z> -> Fraction -> z'
        check_type_is(Fraction, fr)
        return fr
    @override
    def to_may_Fraction_(ops, rhs, /):
        'ops<z> -> z -> (None|Fraction)'
        #check_type_is(Fraction, rhs)
        return rhs
    def is_Fraction_(ops, rhs, /):
        'ops<z> -> z -> bool'
        #check_type_is(Fraction, rhs)
        return True

    def get_zero(ops, /):
        'ops<z> -> z'
        return _Fraction0
    def get_one(ops, /):
        'ops<z> -> z'
        return _Fraction1
    def get_neg_one(ops, /):
        'ops<z> -> z'
        return _Fraction_neg1
    #def pow__int_(ops, lhs, idx, /, *, double_pows):


the_rational_field_ops = RationalFieldOps()
assert the_rational_field_ops is RationalFieldOps()


___begin_mark_of_excluded_global_names__2___ = ...
from seed.helper.repr_input import repr_helper
from seed.math.is_prime__le_pow2_64 import is_prime__le_pow2_64
from seed.math.inv_mod_ import inv_mod_
from seed.tiny_.check import check_int_ge
___end_mark_of_excluded_global_names__2___ = ...

_pow2_64 = 2**64
class PrimeFieldOps(IFiniteFieldOps, int):
    '[z =[def]= int%p]'
    #__slots__ = ()
    ___no_slots_ok___ = True
    #___all___ = ...
    def __new__(cls, p, /):
        check_int_ge(2, p)
        if p <= _pow2_64:
            if not is_prime__le_pow2_64(p): raise ValueError
        sf = super(__class__, cls).__new__(cls, p)
        return sf
    def __init__(ops, p, /):
        ops._p_1 = p-1
    def __repr__(ops, /):
        p = ops.get_prime_characteristic()
        return repr_helper(ops, p)
    @override
    def get_prime_characteristic(ops, /):
        'ops<z> -> prime/uint{>=2}'
        return int.__index__(ops)
    @override
    def get_logarithm_of_order__base_prime_characteristic(ops, /):
        'ops<z> -> logarithm/uint{>=1}'
        return 1
    #@override
    get_order4add = get_prime_characteristic
    @override
    def get_prime_field_ops(ops, /):
        'ops<z> -> PrimeFieldOps'
        return ops


    @override
    def eq(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> bool'
        return int.__eq__(lhs, rhs)


    @override
    def add(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return int.__mod__(int.__add__(lhs, rhs), ops)
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return int.__mod__(int.__mul__(lhs, rhs), ops)
    @override
    def neg_(ops, rhs, /):
        'ops<z> -> z -> z'
        return int.__mod__(int.__neg__(rhs), ops)
    @override
    def inv_(ops, rhs, /):
        'ops<z> -> z -> z|^NonInvertibleError'
        p = ops.get_prime_characteristic()
        return inv_mod_(p, rhs)
    @override
    def mk5int(ops, i, /):
        'ops<z> -> int -> z'
        #check_type_is(int, rhs)
        return int.__mod__(i, ops)
    @override
    def to_may_int_(ops, rhs, /):
        'ops<z> -> z -> (None|int)'
        #check_type_is(int, rhs)
        return rhs
    @override
    def is_int_(ops, rhs, /):
        'ops<z> -> z -> bool'
        #check_type_is(int, rhs)
        return True

    def get_zero(ops, /):
        'ops<z> -> z'
        return 0
    def get_one(ops, /):
        'ops<z> -> z'
        return 1
    def get_neg_one(ops, /):
        'ops<z> -> z'
        return ops.get_order4mul()
        #return p-1
    def get_order4mul(ops, /):
        return object.__getattribute__(ops, '_p_1')
        return ops._p_1 #AttributeError from IAlgebraOps.__getattribute__
    #def pow__int_(ops, lhs, idx, /, *, double_pows):
assert not PrimeFieldOps.__abstractmethods__,  PrimeFieldOps.__abstractmethods__
    # ??int.__new__ donot check ABC??
PrimeFieldOps(2)
PrimeFieldOps(3)
assert PrimeFieldOps(2**7-1).get_order4mul() == 126
assert object.__getattribute__(PrimeFieldOps(2**7-1), '_p_1') == 126

__all__


























___begin_mark_of_excluded_global_names__3___ = ...
from seed.tiny import fst, snd, null_tuple
from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
from seed.tiny import print_err
___end_mark_of_excluded_global_names__3___ = ...


# monomial 单项式 k*x**e
# polynomial 多项式 sum~ k[i]*x**e[i] ~{i}
class IBasePolynomialRingOps(IRingOps):
    '--> IPolynomialRingOps,IPolynomialRingQuotientRingOps'
    __slots__ = ()
    ___all___ = r'''
#abstract_methods:
    `are_all_GCD_nonempty
    `contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring
    `does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements
    `get_num_nonzero_coeffs_
    `get_ring_ops4coeff
    `get_xorder4add
    `get_xorder4mul
    `has_a_uint_norm4nonzero_elements_and_an_associated_divmod
    `has_nontrivial_zero_divisors
    `is_every_finitely_generated_ideal_principal
    `is_every_ideal_principal
    `is_every_nonzero_element_primal
    `is_every_nonzero_element_ring_uint
    `is_left_divisor_of_
    `is_mul_commutative
    `is_mul_idempotent
    `is_multiplicative_group_order_finite
    `is_order_finite
    `is_right_divisor_of_
    `iter_strict_sorted_degree_nonzero_coeff_pairs_ex_
    `mk5strict_sorted_degree_nonzero_coeff_pairs_ex
    `try_left_div
    `try_right_div
#concrete_methods:
    add
    are_all_coeffs_int_
    does_Bezout_identity_hold
    eq
    eq_neg_one_
    eq_one_
    eq_zero_
    get_characteristic
    get_commutative_group_ops4add
    get_commutative_monoid_ops4add
    get_imay_degree_
    get_leading_coefficient_or_zero_
    get_leading_monomial_as_may_pair_
    get_monoid_ops4mul
    get_neg_one
    get_one
    get_tmay_leading_coefficient_
    get_zero
    get_zero4mul
    is_Bezout_domain
    is_Euclidean_domain
    is_Euclidean_ring
    is_Schreier_domain
    is_add_associative
    is_add_commutative
    is_add_idempotent
    is_commutative_ring
    is_commutative_unit_ring
    is_domain
    is_field
    is_finite_field
    is_gcd_domain
    is_int_
    is_integral_domain
    is_integrally_closed_domain
    is_invertable_
    is_lcm_domain
    is_mul_add_distributive
    is_mul_associative
    is_polynomial_monic_
    is_pre_Schreier_domain
    is_principal_ideal_domain
    is_principal_ideal_ring
    is_principal_ring
    is_trivial_ring
    is_unique_factorization_domain
    is_unit_ring
    is_zero4mul_zero4add
    is_zero_ring
    iter_merge_degree_coeff_pairs_if_neighbor_degrees_are_same_
    iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_
    iter_strict_sorted_degree_nonzero_coeff_pairs_
    mk5int
    mk5nonstrict_sorted_degree_coeff_pairs
    mk5strict_sorted_degree_coeff_pairs
    mul
    mul__flipped
    mul__lhs_coeff
    mul__lhs_coeff_ex
    mul__lhs_monomial
    mul__lhs_monomial_ex
    mul__monic_monomial
    mul__rhs_coeff
    mul__rhs_coeff_ex
    mul__rhs_monomial
    mul__rhs_monomial_ex
    mul_ex
    ne
    neg_
    pow__int_
    sub
    to_may_int_
    try_inv_
    try_left_div_ex
    try_left_inv_
    try_left_inv_ex_
    try_right_div_ex
    try_right_inv_
    try_right_inv_ex_
    try_truediv

    is_weak_divisor_of_
    is_strong_divisor_of_
    '''#'''
    #___all___

    @abstractmethod
    def get_ring_ops4coeff(ops, /):
        'ops<z> -> ring_ops4coeff/IRingOps<coeff>'
    @abstractmethod
    def mk5strict_sorted_degree_nonzero_coeff_pairs_ex(ops, iter_strict_sorted_degree_nonzero_coeff_pairs, /, *, reverse:bool):
        'ops<z> -> Iter (degree/uint, coeff/{=!=0}) -> z # [degree strictly decreased] if reverse else [degree strictly increased]'
    @abstractmethod
    def get_num_nonzero_coeffs_(ops, poly, /):
        'ops<z> -> z -> num_nonzero_coeffs/uint'
    @abstractmethod
    def iter_strict_sorted_degree_nonzero_coeff_pairs_ex_(ops, poly, /, *, reverse:bool):
        'ops<z> -> z -> Iter (degree/uint, coeff/{=!=0}) # [degree strictly decreased] if reverse else [degree strictly increased]'
    def iter_strict_sorted_degree_nonzero_coeff_pairs_(ops, poly, /, *, reverse=False):
        'ops<z> -> z -> Iter (degree/uint, coeff/{=!=0}) # [degree strictly increased]'
        return ops.iter_strict_sorted_degree_nonzero_coeff_pairs_ex_(poly, reverse=reverse)
    def iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(ops, poly, /, *, reverse=False):
        'ops<z> -> z -> Iter (degree/uint, coeff/{=!=0}) # [degree strictly decreased]'
        return ops.iter_strict_sorted_degree_nonzero_coeff_pairs_ex_(poly, reverse=not reverse)
    def get_leading_monomial_as_may_pair_(ops, poly, /):
        'ops<z> -> z -> may (degree/uint, coeff)'
        for (degree, coeff) in ops.iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(poly):
            break
        else:
            return None
        return (degree, coeff)
    def get_tmay_leading_coefficient_(ops, poly, /):
        'ops<z> -> z -> tmay leading_coefficient/coeff'
        m = ops.get_leading_monomial_as_may_pair_(poly)
        if m is None:
            return null_tuple
        (degree, leading_coefficient) = m
        return (leading_coefficient,)
    def get_leading_coefficient_or_zero_(ops, poly, /):
        'ops<z> -> z -> (leading_coefficient|coeff.zero)/coeff'
        m = ops.get_leading_monomial_as_may_pair_(poly)
        if m is None:
            ring_ops4coeff = ops.get_ring_ops4coeff()
            return ring_ops4coeff.get_zero()
        (degree, leading_coefficient) = m
        return leading_coefficient
    def get_imay_degree_(ops, poly, /):
        'ops<z> -> z -> (imay degree)/int{>=-1}'
        m = ops.get_leading_monomial_as_may_pair_(poly)
        if m is None:
            imay_degree = -1
        else:
            (degree, leading_coefficient) = m
            imay_degree = degree
        return imay_degree
        ###old:
        imay_degree = -1
        for imay_degree, _ in ops.iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(poly):
            break
        return imay_degree
    def iter_merge_degree_coeff_pairs_if_neighbor_degrees_are_same_(ops, iter_degree_coeff_pairs, /):
        'ops<z> -> Iter (degree/uint, coeff) -> Iter (degree/uint, coeff)/{[neighbor degrees will be diff]}'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        it = iter(iter_degree_coeff_pairs)
        for (prev_deg, prev_coeff) in it:
            break
        else:
            return
        for deg, coeff in it:
            if prev_deg == deg:
                prev_coeff = ring_ops4coeff.add(prev_coeff, coeff)
            else:
                yield (prev_deg, prev_coeff)
                (prev_deg, prev_coeff) = (deg, coeff)
        else:
                yield (prev_deg, prev_coeff)
        return
    def mk5strict_sorted_degree_coeff_pairs(ops, iter_strict_sorted_degree_coeff_pairs, /, *, reverse=False):
        'ops<z> -> Iter (degree/uint, coeff) -> z # [degree strictly increased]'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        eq_zero_ = ring_ops4coeff.eq_zero_
        iter_strict_sorted_degree_nonzero_coeff_pairs = filter(lambda p:not eq_zero_(snd(p)), iter_strict_sorted_degree_coeff_pairs)
        return ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(iter_strict_sorted_degree_nonzero_coeff_pairs, reverse=reverse)
    def mk5nonstrict_sorted_degree_coeff_pairs(ops, iter_nonstrict_sorted_degree_coeff_pairs, /, *, reverse=False):
        'ops<z> -> Iter (degree/uint, coeff) -> z # [degree nonstrictly increased]'
        return ops.mk5strict_sorted_degree_coeff_pairs(ops.iter_merge_degree_coeff_pairs_if_neighbor_degrees_are_same_(iter_nonstrict_sorted_degree_coeff_pairs), reverse=reverse)

    def is_polynomial_monic_(ops, poly, /):
        #monic polynomial
        leading_coefficient = ops.get_leading_coefficient_or_zero_(poly)
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.eq_one_(leading_coefficient)
    def are_all_coeffs_int_(ops, poly, /):
        ring_ops4coeff = ops.get_ring_ops4coeff()
        is_int_ = ring_ops4coeff.is_int_
        ps = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(poly)
        return all(is_int_(coeff) for deg, coeff in ps)



    def mul__lhs_coeff(ops, coeff4lhs, rhs, /):
        'ops<z> -> coeff -> z -> z'
        return ops.mul__rhs_coeff_ex(rhs, coeff4lhs, reverse=True)
    def mul__rhs_coeff(ops, lhs, coeff4rhs, /):
        'ops<z> -> z -> coeff -> z'
        return ops.mul__rhs_coeff_ex(lhs, coeff4rhs, reverse=False)
    def mul__lhs_coeff_ex(ops, coeff4lhs, rhs, /, *, reverse:bool):
        'ops<z> -> coeff -> z -> z'
        return ops.mul__rhs_coeff_ex(rhs, coeff4lhs, reverse=not reverse)
    if 0:
        @abstractmethod
        def mul__rhs_coeff_ex(ops, lhs, coeff4rhs, /, *, reverse:bool):
            'ops<z> -> z -> coeff -> z'
    @override
    def mul__rhs_coeff_ex(ops, lhs, coeff4rhs, /, *, reverse:bool):
        'ops<z> -> z -> coeff -> z'
        _mul__coeff_if_commutative = object.__getattribute__(ops, '_mul__coeff_if_commutative')
        tm = _mul__coeff_if_commutative(lhs, coeff4rhs)
        if tm:
            [result] = tm
        else:
            [] = tm
            ring_ops4coeff = ops.get_ring_ops4coeff()
            _mul_ = ring_ops4coeff.mul__flipped if reverse else ring_ops4coeff.mul
            itL = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(lhs)
            result = ops.mk5strict_sorted_degree_coeff_pairs((deg, _mul_(coeffL, coeff4rhs)) for deg, coeffL in itL)
                # donot use ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex
                # [a=!=0][b=!=0] but [(a*b) may be 0]
        return result
    def _mul__coeff_if_commutative(ops, poly, coeff, /):
        'ops<z> -> z -> coeff -> tmay z'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        if ops.eq_zero_(poly):
            result = poly
        elif ring_ops4coeff.eq_zero_(coeff):
            result = ops.get_zero()
        elif ring_ops4coeff.eq_one_(coeff):
            result = poly
        elif ring_ops4coeff.eq_neg_one_(coeff):
            result = ops.neg_(poly)
        else:
            return null_tuple
        return (result,)
    def mul__monic_monomial(ops, degree, poly, /):
        'ops<z> -> degree/uint -> z -> z'
        if degree == 0:
            result = poly
        else:
            ps = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(poly)
            result = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(((degree+deg, coeff) for deg, coeff in ps), reverse=False)
        return result
    #lshift_ = mul__monic_monomial
    def mul__lhs_monomial(ops, degree4lhs, coeff4lhs, rhs, /):
        'ops<z> -> degree/uint -> coeff -> z -> z'
        return ops.mul__rhs_monomial_ex(rhs, degree4lhs, coeff4lhs, reverse=True)
    def mul__rhs_monomial(ops, lhs, degree4rhs, coeff4rhs, /):
        'ops<z> -> z -> degree/uint -> coeff -> z'
        return ops.mul__rhs_monomial_ex(lhs, degree4rhs, coeff4rhs, reverse=False)
    def mul__lhs_monomial_ex(ops, degree4lhs, coeff4lhs, rhs, /, *, reverse:bool):
        'ops<z> -> degree/uint -> coeff -> z -> z'
        return ops.mul__rhs_monomial_ex(rhs, degree4lhs, coeff4lhs, reverse=not reverse)
    def mul__rhs_monomial_ex(ops, lhs, degree4rhs, coeff4rhs, /, *, reverse:bool):
        'ops<z> -> z -> degree/uint -> coeff -> z'
        result = ops.mul__rhs_coeff_ex(lhs, coeff4rhs, reverse=reverse)
        result = ops.mul__monic_monomial(degree4rhs, result)
        return result
    # normal API for IRingOps:
    @override
    def get_characteristic(ops, /):
        'ops<z> -> (0|1|prime)/uint{==0|>=2} # 1=>is_zero_ring'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.get_characteristic()
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        if ops.eq_zero_(lhs):
            return lhs
        elif ops.eq_zero_(rhs):
            return rhs

        elif ops.eq_one_(lhs):
            return rhs
        elif ops.eq_one_(rhs):
            return lhs

        elif ops.eq_neg_one_(lhs):
            return ops.neg_(rhs)
        elif ops.eq_neg_one_(rhs):
            return ops.neg_(lhs)
        ######################
        ######################
        ######################
        ######################

        # new ver:O(N_N_logN) <<== O(N**2 + N**2 * log(N**2)) where [N:=num_nonzero_coeffs]
        #    should be O(N**2)
        #
        ring_ops4coeff = ops.get_ring_ops4coeff()
        mul = ring_ops4coeff.mul
        add = ring_ops4coeff.add
        ps = []
        itL = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(lhs)
        for (degree4lhs, coeff4lhs) in itL:
            itR = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(rhs)
            for (degree4rhs, coeff4rhs) in itR:
                deg = degree4lhs + degree4rhs
                coeff = mul(coeff4lhs, coeff4rhs)
                ps.append((deg, coeff))
        # [len(ps) == O(N**2)]
        ps.sort(key=fst)
        # [TIME(ps.sort) == O(N**2 * log(N**2)) == O(N_N_logN)]
        return ops.mk5nonstrict_sorted_degree_coeff_pairs(ps)

        # deprecaded:
        #below:bad: O(N**3) where [N:=num_nonzero_coeffs]
        #    should be O(N**2)
        #
        #itL = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(lhs)
        itR = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(rhs)
        acc = ops.get_zero()
        for (degree4rhs, coeff4rhs) in itR:
            acc = ops.add(acc, ops.mul__rhs_monomial(lhs, degree4rhs, coeff4rhs))
        result = acc
        return result
    @override
    def eq(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> bool'
        a = ops.get_num_nonzero_coeffs_(lhs)
        b = ops.get_num_nonzero_coeffs_(rhs)
        if not a == b:
            return False
        itL = ops.iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(lhs)
        itR = ops.iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(rhs)
        itL = map(fst, itL)
        itR = map(fst, itR)
        if not all(map(int.__eq__, itL, itR)):
            # deg cmp
            return False
        itL = ops.iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(lhs)
        itR = ops.iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(rhs)
        itL = map(snd, itL)
        itR = map(snd, itR)
        ring_ops4coeff = ops.get_ring_ops4coeff()
        if not all(map(ring_ops4coeff.eq, itL, itR)):
            # coeff cmp
            return False
        return True


    @override
    def add(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        itL = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(lhs)
        itR = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(rhs)
        ps = merge_two_sorted_iterables(itL, itR, left_key=fst, right_key=fst, before=int.__le__)
            #sorted but nonstrictly
        return ops.mk5nonstrict_sorted_degree_coeff_pairs(ps)



    @override
    def neg_(ops, rhs, /):
        'ops<z> -> z -> z'
        if ops.eq_zero_(rhs):
            return rhs
        elif ops.eq_one_(rhs):
            return ops.get_neg_one()
        elif ops.eq_neg_one_(rhs):
            return ops.get_one()

        ring_ops4coeff = ops.get_ring_ops4coeff()
        neg_ = ring_ops4coeff.neg_
        itR = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(rhs)
        result = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(((deg, neg_(coeffR)) for deg, coeffR in itR), reverse=False)
        return result
    @override
    def mk5int(ops, i, /):
        'ops<z> -> int -> z'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        coeff = ring_ops4coeff.mk5int(i)
            #may be 0
            # is_trivial_ring()??
        deg = 0
        return ops.mk5strict_sorted_degree_coeff_pairs([(deg, coeff)])
    @override
    def to_may_int_(ops, poly, /):
        'ops<z> -> z -> (None|int)'
        m = ops.get_leading_monomial_as_may_pair_(poly)
        if m is None:
            return 0
        (degree, leading_coefficient) = m
        if not degree == 0:
            return None
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.to_may_int_(leading_coefficient)
        ###old:
        im = ops.get_imay_degree_(poly)
        if im == -1:
            return 0
        degree = im
        if not degree == 0:
            assert degree > 0
            return None
        [(_, coeff)] = ops.iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_(poly)
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.to_may_int_(coeff)




    r'''[[[

    IPolynomialRingQuotientRingOps should override: #no div/divmod...
    @override
    def mul__monic_monomial(ops, degree, poly, /):
        'ops<z> -> degree/uint -> z -> z'
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
    #]]]'''#'''

class IPolynomialRingOps(IBasePolynomialRingOps, IRingOps):
    'univariate[1var X]; [z =[def]= coeff[X]]; [X * coeff == coeff * X]; [coeff ring is not zero ring],i.e.[not ring_ops4coeff.eq_zero_(ring_ops4coeff.get_one())]'
    #newmethod: '*divmod*'
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
are_all_coeffs_int_
get_imay_degree_
get_leading_coefficient_or_zero_
get_leading_monomial_as_may_pair_
get_num_nonzero_coeffs_
get_ring_ops4coeff
get_tmay_leading_coefficient_
is_polynomial_monic_
iter_merge_degree_coeff_pairs_if_neighbor_degrees_are_same_
iter_reversed_strict_sorted_degree_nonzero_coeff_pairs_
iter_strict_sorted_degree_nonzero_coeff_pairs_
iter_strict_sorted_degree_nonzero_coeff_pairs_ex_
mk5nonstrict_sorted_degree_coeff_pairs
mk5strict_sorted_degree_coeff_pairs
mk5strict_sorted_degree_nonzero_coeff_pairs_ex
mul__lhs_coeff
mul__lhs_coeff_ex
mul__lhs_monomial
mul__lhs_monomial_ex
mul__monic_monomial
mul__rhs_coeff
mul__rhs_coeff_ex
mul__rhs_monomial
mul__rhs_monomial_ex
try_divmod
try_left_divmod
try_left_divmod__rhs_monic
try_left_divmod__rhs_monic_ex
try_left_divmod_ex
try_right_divmod
try_right_divmod__rhs_monic
try_right_divmod__rhs_monic_ex
try_right_divmod_ex

add
eq
get_characteristic
is_field
is_mul_commutative
is_mul_idempotent
is_order_finite
    get_xorder4add
is_trivial_ring
mk5int
mul
neg_
to_may_int_
try_truediv
    '''#'''
    ___all___ = r'''
    try_divmod

    try_left_divmod
    try_left_divmod__rhs_monic
    try_left_divmod__rhs_monic_ex
    try_left_divmod_ex

    try_right_divmod
    try_right_divmod__rhs_monic
    try_right_divmod__rhs_monic_ex
    try_right_divmod_ex

    '''#'''
    #___all___


    # `is_left_divisor_of_
    # `is_right_divisor_of_
    #   ...until ring_ops4coeff is field?


    @override
    def is_trivial_ring(ops, /):
        'ops<z> -> bool'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_trivial_ring()
        return ops.eq_zero_(ops.get_one())

    @override
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_mul_commutative()
    @override
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        # deg increase
        return False

    # normal API for IRingOps:
    @override
    def is_order_finite(ops, /):
        'ops<z> -> bool'
        return False
    @override
    def is_multiplicative_group_order_finite(ops, /):
        'ops<z> -> bool # order4mul # order of multiplicative_group # [ZZ.multiplicative_group == {-1,+1}]'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_multiplicative_group_order_finite()
    @override
    def get_xorder4add(ops, /):
        'ops<z> -> xorder4add/(-1|uint|...) #(-1 if not is_order_finite() else (order4add/uint if known else ...)) # '
        # !! [not ring_ops4coeff.is_trivial_ring()]
        return -1
    @override
    def get_xorder4mul(ops, /):
        'ops<z> -> xorder4mul/(-1|uint|...) #(-1 if not is_order_finite<multiplicative_group>() else (order4mul/uint if known else ...)) # '
        # order of multiplicative_group
        # number of ring units
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.get_xorder4mul()
    if 0:
        @override
        def is_field(ops, /):
            'ops<z> -> bool'
            return False


    def try_left_divmod(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [(qL,r) := d \% n][d*qL + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        return ops.try_right_divmod_ex(lhs, rhs, reverse=True)
    def try_right_divmod(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [(qR,r) := n /% d][qR*d + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        return ops.try_right_divmod_ex(lhs, rhs, reverse=False)
    def try_left_divmod_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [(qL,r) := d \% n][d*qL + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        return ops.try_right_divmod_ex(lhs, rhs, reverse=not reverse)
    def try_right_divmod_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [(qR,r) := n /% d][qR*d + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        _try_right_divmod_ex = object.__getattribute__(ops, '_try_right_divmod_ex')
        N, D = lhs, rhs
        qR, r = _try_right_divmod_ex(N, D, reverse=reverse)
        validate__try_right_divmod_ex6IPolynomialRingOps_(ops, lhs, rhs, reverse, qR, r)
        return (qR, r)
    def _try_right_divmod_ex(ops, N, D, /, *, reverse:bool):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError|^IsTrivialRingError # [(qR,r) := n /% d][qR*d + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        if ops.is_trivial_ring(): raise IsTrivialRingError('try_right_divmod_ex cannot satisfy [get_imay_degree_(r) < get_imay_degree_(d)]')

        degD = ops.get_imay_degree_(D)
        if degD < 0:
            # [D == 0]
            raise NonInvertibleError__not_injective
        # [D.leading_coefficient =!= 0]
        degN = ops.get_imay_degree_(N)
        if degN < degD:
            r = N
            qR = ops.get_zero()
            return (qR, r)
        lcD = ops.get_leading_coefficient_or_zero_(D)
        # [D.leading_coefficient =!= 0]
        ring_ops4coeff = ops.get_ring_ops4coeff()
        if ring_ops4coeff.eq_one_(lcD):
            # [monic D]
            qR, r = ops.try_right_divmod__rhs_monic_ex(N, D, reverse=reverse)
            return (qR, r)

        if ring_ops4coeff.eq_neg_one_(lcD):
            neg_D = ops.neg_(D)
            neg_qR, r = ops.try_right_divmod__rhs_monic_ex(N, neg_D, reverse=reverse)
            qR = ops.neg_(neg_qR)
            return (qR, r)

        try:
            # !! [IRingOps.left_inv_ === IRingOps.right_inv_ === IRingOps.inv_]
            inv_lcD = ring_ops4coeff.try_inv_(lcD)
        except NonInvertibleError:
            pass
        else:
            # !! [qR*d + r == n]
            # [(qR*lcD)*(inv_lcD*d) + r == n]
            # [(qR_mul_lcD)*(monic_d) + r == n]
            monicD = ops.mul__lhs_coeff_ex(inv_lcD, D, reverse=reverse)
            qR_mul_lcD, r = ops.try_right_divmod__rhs_monic_ex(N, monicD, reverse=reverse)
            qR = ops.mul__rhs_coeff_ex(qR_mul_lcD, inv_lcD, reverse=reverse)
            return (qR, r)

        _try_right_divmod_ex_ex = object.__getattribute__(ops, '_try_right_divmod_ex_ex')
        # not monic D
        return _try_right_divmod_ex_ex(N, D, reverse=reverse, monic=False)
    def _try_right_divmod_ex_ex(ops, N, D, /, *, reverse:bool, monic:bool):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [not monic rhs][(qR,r) := n /% d][qR*d + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        if not monic is ops.is_polynomial_monic_(D): raise logic-err
        if ops.is_trivial_ring(): raise IsTrivialRingError('try_right_divmod_ex cannot satisfy [get_imay_degree_(r) < get_imay_degree_(d)]')


        degD = ops.get_imay_degree_(D)
        degN = ops.get_imay_degree_(N)
        if not 0 <= degD <= degN:
            # [not 0 <= degD <= degN]
            if degN < degD:
                r = N
                qR = ops.get_zero()
                return (qR, r)
            # [degD <= degN]
            # !! [not 0 <= degD <= degN]
            # [not 0 <= degD]
            # [degD < 0]
            assert degD == -1
            # [D == 0]
            raise NonInvertibleError__not_injective
        ring_ops4coeff = ops.get_ring_ops4coeff()
        if not monic:
            _try_right_div = ring_ops4coeff.try_left_div if reverse else ring_ops4coeff.try_right_div
            lcD = ops.get_leading_coefficient_or_zero_(D)
            #lcN = ops.get_leading_coefficient_or_zero_(N)
            #lc_of_qR = ring_ops4coeff.try_right_div(lcN, lcD)
        #####
        if degD == 0:
            # !! [get_imay_degree_(r) < get_imay_degree_(d)]
            # [r == 0]
            # !! [qR*d + r == n]
            # [qR*d == n]
            # !! [deg(d) == 0]
            # [qR*lcD == n]
            # [qR == n/lcD]
            if monic:
                # [D == 1]
                # [qR == n/lcD == n/1 == n]
                qR = N
            else:
                itN = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(N)
                qR = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(((deg, _try_right_div(coeffN, lcD)) for deg, coeffN in itN), reverse=False)
                    # !! [deg(d) == 0]
                    # [lcD =!= 0]
                    # !! [coeffN =!= 0]
                    # [0*lcD == 0 =!= coeffN]
                    # !! [right_div(n,d)*d == n]
                    # [try_right_div(coeffN, lcD)*lcD == coeffN]
                    # !! [0*lcD == 0 =!= coeffN]
                    # [try_right_div(coeffN, lcD) =!= 0]
            r = ops.get_zero()
            return (qR, r)
        # [0 < degD <= degN]
        # !! [deg(d) =!= -1]
        # [lcD =!= 0]
        [*psN] = ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(N)
        psD = (*ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(D),)
        if not monic:
            neg_lcD = ring_ops4coeff.neg_(lcD)
        (degD, lcD) = psD[-1]
        (low_degD, _low_coeffD) = psD[0]
        W_1 = degD -low_degD
        ps_of_neg_qR__reverse = []
        while psN:
            #print_err(N, D, psN, ps_of_neg_qR__reverse)
            (degN, lcN) = psN[-1]
            if degN < degD:
                break
            # [0 < degD <= degD]
            low_degN = degN -W_1
            L = len(psN)
            # [L > 0]
            #seed.seq_tools.seq_index_if
            for i in reversed(range(L)):
                if psN[i][0] < low_degN:
                    break
            else:
                i = -1
            i += 1
            assert 0 <= i < L
            assert i==0 or psN[i-1][0] < low_degN
            assert psN[i][0] >= low_degN
            #lc_of_qR = ring_ops4coeff.try_right_div(lcN, lcD)
            if not monic:
                neg_lc_of_qR = _try_right_div(lcN, neg_lcD)
            else:
                # !! [lcD == 1]
                # [neg_lcD == -1]
                neg_lc_of_qR = ring_ops4coeff.neg_(lcN) # = _try_right_div(lcN, neg_lcD)
            #deg_qR = low_degN -low_degD
            deg_qR = degN -degD
            ps_of_neg_qR__reverse.append((deg_qR, neg_lc_of_qR))
            # !! [qR*d + r == n]
            _pad_neg_qD = ops.mul__lhs_monomial_ex(deg_qR, neg_lc_of_qR, D, reverse=reverse)
            _N = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(psN[i:], reverse=False)
            _N_ = ops.add(_N, _pad_neg_qD)
            del psN[i:]
            psN.extend(ops.iter_strict_sorted_degree_nonzero_coeff_pairs_(_N_))
            assert not psN or psN[-1][0] < degN
        assert not psN or psN[-1][0] < degD
        r = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(psN, reverse=False)
        neg_qR = ops.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(ps_of_neg_qR__reverse, reverse=True)
        qR = ops.neg_(neg_qR)
        return (qR, r)
    def try_left_divmod__rhs_monic(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [monic rhs][(qL,r) := d \% n][d*qL + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        return ops.try_right_divmod__rhs_monic_ex(lhs, rhs, reverse=True)
    def try_right_divmod__rhs_monic(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [monic rhs][(qR,r) := n /% d][qR*d + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        return ops.try_right_divmod__rhs_monic_ex(lhs, rhs, reverse=False)
    def try_left_divmod__rhs_monic_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [monic rhs][(qL,r) := d \% n][d*qL + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        return ops.try_right_divmod__rhs_monic_ex(lhs, rhs, reverse=not reverse)
    def try_right_divmod__rhs_monic_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError # [monic rhs][(qR,r) := n /% d][qR*d + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
        if not ops.is_polynomial_monic_(rhs): raise NotMonicPolynomialError
        _try_right_divmod_ex_ex = object.__getattribute__(ops, '_try_right_divmod_ex_ex')
        (qR, r) = _try_right_divmod_ex_ex(lhs, rhs, reverse=reverse, monic=True)
        validate__try_right_divmod_ex6IPolynomialRingOps_(ops, lhs, rhs, reverse, qR, r)
        return (qR, r)

#class ICommutativePolynomialRingOps(IPolynomialRingOps, ICommutativeRingOps):
    #@newmethod
    def try_divmod(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> (z,z)|^NonInvertibleError'
        (qR, r) = ops.try_right_divmod(lhs, rhs)
        # !! [qR*d + r == n]
        # !! [d*qL + r == n]
        #validate__try_right_divmod_ex6IPolynomialRingOps_
        if not (ops.is_mul_commutative() or ops.eq(lhs, ops.add(r, ops.mul_ex(qR,rhs, reverse=True)))): raise NonInvertibleError__not_commutative
        q = qL = qR
        return (q, r)

    @override
    def try_left_div(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [d*left_div(n,d) == n]'
        return ops.try_right_div_ex(lhs, rhs, reverse=True)
    @override
    def try_right_div(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [right_div(n,d)*d == n]'
        return ops.try_right_div_ex(lhs, rhs, reverse=False)
    @override
    def try_right_div_ex(ops, lhs, rhs, /, *, reverse:bool):
        'ops<z> -> z -> z -> z|^NonInvertibleError # [right_div(n,d)*d == n]'
        (qR, r) = ops.try_right_divmod_ex(lhs, rhs, reverse=reverse)
        if not ops.eq_zero_(r): raise NonInvertibleError__out_of_domain(r)
        return qR

    # ring type detect
    @override
    def has_nontrivial_zero_divisors(ops, /):
        'ops<z> -> bool'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.has_nontrivial_zero_divisors()
    @override
    def contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring(ops, /):
        'ops<z> -> bool'
        #??? to_prove
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_integrally_closed_domain()
    @override
    def is_every_nonzero_element_ring_uint(ops, /):
        'ops<z> -> bool #is_invertable_ === is_ring_unit_'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_zero_ring()
    @override
    def is_every_nonzero_element_primal(ops, /):
        'ops<z> -> bool # ???[[ring.is_mul_commutative()][@[d :<- ring] -> [d =!= 0] -> [is_primal_(ring; d)]]]??? # see:is_primal_'
        #??? to_prove
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_pre_Schreier_domain()
    @override
    def are_all_GCD_nonempty(ops, /):
        'ops<z> -> bool # [[ring.is_mul_commutative()][not ring.is_trivial_ring()][@[m,n :<- ring] -> [GCD(ring; m,n) =!= {}]]]'
        #??? to_prove
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_gcd_domain()
    @override
    def is_every_finitely_generated_ideal_principal(ops, /):
        'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_finitely_generated_ideal_principal === does_Bezout_identity_hold === does_every_finite_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
        #??? to_prove
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_Bezout_domain()
    @override
    def is_every_ideal_principal(ops, /):
        'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_ideal_principal < is_every_finitely_generated_ideal_principal] # [is_every_ideal_principal === does_every_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
        #??? to_prove
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_principal_ideal_ring()
        return ring_ops4coeff.is_field()

    @override
    def does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements(ops, /):
        'ops<z> -> bool # <<== UFD'
        'ops<z> -> bool # <<== UFD or bug:PrincipalRing # but in PrincipalRing, prime may be reducible, eg ZZ%6 !! bug !! [3 is prime][3==3*3==3*3*3=...]'
        #??? to_prove
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_unique_factorization_domain()
    @override
    def has_a_uint_norm4nonzero_elements_and_an_associated_divmod(ops, /):
        'ops<z> -> bool # (uint_norm4Euclidean_, divmod4Euclidean) since py.Fraction.__divmod__ not an Euclidean_divmod'
        #??? to_prove
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_field()
        return ring_ops4coeff.is_Euclidean_ring()

def validate__try_right_divmod_ex6IPolynomialRingOps_(ops, lhs, rhs, reverse, qR, r, /):
    '[(qR,r) := n /% d][qR*d + r == n][get_imay_degree_(r) < get_imay_degree_(d)]'
    if not (ops.get_imay_degree_(r) < ops.get_imay_degree_(rhs)): raise ValidateError____divmod____not__remainder_degree__lt__divisor_degree
    if not ops.eq(lhs, ops.add(r, ops.mul_ex(qR,rhs, reverse=reverse))): raise ValidateError____divmod
#end-class IPolynomialRingOps(IRingOps):
class IPolynomialRingOps___coeff_ring_is_field(IPolynomialRingOps, ICommutativeRingOps):
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
    `get_field_ops4coeff
    '''#'''
    #___all___
    @abstractmethod
    def get_field_ops4coeff(ops, /):
        'ops<z> -> field_ops4coeff/IFieldOps<coeff>'
    @override
    def get_ring_ops4coeff(ops, /):
        'ops<z> -> ring_ops4coeff/IRingOps<coeff>'
        return ops.get_field_ops4coeff()
    @override
    def is_divisor_of_(ops, n, d, /):
        'ops<z> -> z -> z -> bool # is_mul_commutative => [is_divisor_of_ === is_strong_divisor_of_]'
        if ops.eq_zero_(n):
            return True
        if ops.eq_zero_(d):
            return False
        q, r = ops.try_divmod(n, d)
        return ops.eq_zero_(r)
is_divisor_of__6IPolynomialRingOps___coeff_ring_is_field_ = IPolynomialRingOps___coeff_ring_is_field.is_divisor_of_

#class FinitePermutationGroupOps:
#class PolynomialRingOps(IPolynomialRingOps): DONE
class IIntegralDomainFractionFieldOps(IFieldOps):
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
    `get_integral_domain_ops4ND
    '''#'''
    #___all___
    @abstractmethod
    def get_integral_domain_ops4ND(ops, /):
        'ops<z> -> integral_domain_ops4ND/IIntegralDomainOps<numerator&denominator> #IIntegralDomainOps===IRingOps+is_integral_domain'
class IPolynomialRingFractionFieldOps(IIntegralDomainFractionFieldOps):
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
    `get_polynomial_integral_domain_ops4ND
    '''#'''
    #___all___
    @abstractmethod
    def get_polynomial_integral_domain_ops4ND(ops, /):
        'ops<z> -> polynomial_integral_domain_ops4ND/IPolynomialIntegralDomainOps<numerator&denominator> #IPolynomialIntegralDomainOps===IPolynomialRingOps+is_integral_domain'
    @override
    def get_integral_domain_ops4ND(ops, /):
        'ops<z> -> integral_domain_ops4ND/IIntegralDomainOps<numerator&denominator> #IIntegralDomainOps===IRingOps+is_integral_domain'
        return ops.get_polynomial_integral_domain_ops4ND()






#xxx class IQuotientRingOfPolynomialRingOps(IRingOps):
class IPolynomialRingQuotientRingOps(IBasePolynomialRingOps, IRingOps):
    '[z =[def]= coeff[X]%modulus][modulus is monic polynomial][deg modulus > 0]'
    'modulo/vt; modulus/n, moduli/n.pl'
    'using_ left_div right_div ?? since not commutative'
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
#new_abstract_methods:
    `get_polynomial_ring_ops4modulus
    `get_the_monic_polynomial_modulus
    `is_the_monic_polynomial_modulus_irreducible
    `use_the_monic_polynomial_modulus_irreducible_in_right_divmod
    `mk5polynomial_of_degree_lt_modulus_degree
    `to_polynomial_of_degree_lt_modulus_degree_
#new_concrete_methods:
    mk5polynomial
    get_degree_of_the_monic_polynomial_modulus
    has_nontrivial_zero_divisors
    contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring
    is_every_nonzero_element_ring_uint
    is_every_nonzero_element_primal
    is_every_ideal_principal
    has_a_uint_norm4nonzero_elements_and_an_associated_divmod
    get_ring_ops4coeff
    mk5strict_sorted_degree_nonzero_coeff_pairs_ex
    get_num_nonzero_coeffs_
    iter_strict_sorted_degree_nonzero_coeff_pairs_ex_
    is_trivial_ring
    is_mul_commutative
    is_mul_idempotent
    is_order_finite
    is_multiplicative_group_order_finite
    get_xorder4add
    get_xorder4mul
    eq
    add
    mul__rhs_coeff_ex
    mul__monic_monomial
    mul
    '''#'''
    #___all___

    @abstractmethod
    def get_polynomial_ring_ops4modulus(ops, /):
        'ops<z> -> polynomial_ring_ops4modulus/IPolynomialRingOps<modulus>'
    @abstractmethod
    def get_the_monic_polynomial_modulus(ops, /):
        'ops<z> -> the_monic_polynomial_modulus/z'
    @abstractmethod
    def is_the_monic_polynomial_modulus_irreducible(ops, /):
        'ops<z> -> bool'
    @abstractmethod
    def use_the_monic_polynomial_modulus_irreducible_in_right_divmod(ops, /):
        'ops<z> -> bool # since may be not commutative'




    @abstractmethod
    def mk5polynomial_of_degree_lt_modulus_degree(ops, poly, /):
        'ops<z> -> coeff[X]{.deg < deg(modulus)} -> z'
    @abstractmethod
    def to_polynomial_of_degree_lt_modulus_degree_(ops, poly_mod, /):
        'ops<z> -> z -> coeff[X]{.deg < deg(modulus)}'

    #@newmethod
    def mk5polynomial(ops, poly, /, *, degree_lt_modulus_degree=False):
        'ops<z> -> coeff[X] -> z'
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        if degree_lt_modulus_degree:
            pass
        elif ops4modulus.get_imay_degree_(poly) < ops.get_degree_of_the_monic_polynomial_modulus():
            pass
        else:
            the_monic_polynomial_modulus = ops.get_the_monic_polynomial_modulus()
            right = ops.use_the_monic_polynomial_modulus_irreducible_in_right_divmod()
            (qR, r) = ops4modulus.try_right_divmod_ex(poly, the_monic_polynomial_modulus, reverse=not right)
            poly = r
        poly_mod = ops.mk5polynomial_of_degree_lt_modulus_degree(poly)
        return poly_mod

    def get_degree_of_the_monic_polynomial_modulus(ops, /):
        'ops<z> -> degree_of_the_monic_polynomial_modulus/uint'
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        the_monic_polynomial_modulus = ops.get_the_monic_polynomial_modulus()
        deg = ops4modulus.get_imay_degree_(the_monic_polynomial_modulus)
        assert deg > 0
        return deg

    # ring type detect
    @override
    def has_nontrivial_zero_divisors(ops, /):
        'ops<z> -> bool'
        #??? to_prove
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.has_nontrivial_zero_divisors() and ops.is_the_monic_polynomial_modulus_irreducible()
    @override
    def contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring(ops, /):
        'ops<z> -> bool'
        #??? to_prove
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.contains_all_fraction_roots_of_all_monic_polynomials_over_this_ring()
    @override
    def is_every_nonzero_element_ring_uint(ops, /):
        'ops<z> -> bool #is_invertable_ === is_ring_unit_'
        #??? to_prove
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.is_field() and ops.is_the_monic_polynomial_modulus_irreducible()
    @override
    def is_every_nonzero_element_primal(ops, /):
        'ops<z> -> bool # ???[[ring.is_mul_commutative()][@[d :<- ring] -> [d =!= 0] -> [is_primal_(ring; d)]]]??? # see:is_primal_'
        #??? to_prove
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.is_every_nonzero_element_primal() and ops.is_the_monic_polynomial_modulus_irreducible()
        return ops4modulus.is_pre_Schreier_domain() and ops.is_the_monic_polynomial_modulus_irreducible()
    if 0:
        r'''[[[
        ===not_gcd_domain:
        [ring := ZZ[x]%(x**2+5)]:
            [6 == 2*3 == (1-x)*(1+x)]
            [all_common_divisors_of(6,2*(x+1)) == {+1,-1} .* {2,x+1}]
        [GCD(ZZ[x]%(x**2+5); 6,2*(x+1)) == {}]
        [not is_gcd_domain(ZZ[x]%(x**2+5))]
        @override
        def are_all_GCD_nonempty(ops, /):
            'ops<z> -> bool # [[ring.is_mul_commutative()][not ring.is_trivial_ring()][@[m,n :<- ring] -> [GCD(ring; m,n) =!= {}]]]'
            #??? to_prove
            ops4modulus = ops.get_polynomial_ring_ops4modulus()
            return ops4modulus.are_all_GCD_nonempty()

        @override
        def is_every_finitely_generated_ideal_principal(ops, /):
            'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_finitely_generated_ideal_principal === does_Bezout_identity_hold === does_every_finite_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
            #??? to_prove
            ops4modulus = ops.get_polynomial_ring_ops4modulus()
            # [(g+<f>) + (h+<f>) =?= (gcd(g,h)+<f>)]
            return ops4modulus.does_Bezout_identity_hold()

        @override
        def does_every_nonzero_noninvertible_element_have_an_essentially_unique_decomposition_as_the_product_of_prime_elements_up_to_order_and_unit_elements(ops, /):
            'ops<z> -> bool # <<== UFD'
            'ops<z> -> bool # <<== UFD or bug:PrincipalRing # but in PrincipalRing, prime may be reducible, eg ZZ%6 !! bug !! [3 is prime][3==3*3==3*3*3=...]'
            #??? to_prove
            ops4modulus = ops.get_polynomial_ring_ops4modulus()
            return ops4modulus.is_unique_factorization_domain()
        #]]]'''#'''
    @override
    def is_every_ideal_principal(ops, /):
        'ops<z> -> bool # [[ideal is principal] =[def]= [ideal is ideal of rank 1] = [ideal is generated by a single element]] # [is_every_ideal_principal < is_every_finitely_generated_ideal_principal] # [is_every_ideal_principal === does_every_nonempty_set_of_nonzero_elements_have_a_well_defined_gcd]'
        #??? to_prove
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.is_field() and ops.is_the_monic_polynomial_modulus_irreducible()

    @override
    def has_a_uint_norm4nonzero_elements_and_an_associated_divmod(ops, /):
        'ops<z> -> bool # (uint_norm4Euclidean_, divmod4Euclidean) since py.Fraction.__divmod__ not an Euclidean_divmod'
        #??? to_prove
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.is_field() and ops.is_the_monic_polynomial_modulus_irreducible()




    #vivi:IPolynomialRingOps
    #@abstractmethod
    @override
    def get_ring_ops4coeff(ops, /):
        'ops<z> -> ring_ops4coeff/IRingOps<coeff>'
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.get_ring_ops4coeff()
    #@abstractmethod
    @override
    def mk5strict_sorted_degree_nonzero_coeff_pairs_ex(ops, iter_strict_sorted_degree_nonzero_coeff_pairs, /, *, reverse:bool, degree_lt_modulus_degree:bool=False):
        'ops<z> -> Iter (degree/uint, coeff/{=!=0}) -> z # [degree strictly decreased] if reverse else [degree strictly increased]'
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        poly = ops4modulus.mk5strict_sorted_degree_nonzero_coeff_pairs_ex(iter_strict_sorted_degree_nonzero_coeff_pairs, reverse=reverse)
        if degree_lt_modulus_degree:
            poly_mod = ops.mk5polynomial_of_degree_lt_modulus_degree(poly)
        else:
            poly_mod = ops.mk5polynomial(poly)
        return poly_mod

    #@abstractmethod
    @override
    def get_num_nonzero_coeffs_(ops, poly_mod, /):
        'ops<z> -> z -> num_nonzero_coeffs/uint'
        poly = ops.to_polynomial_of_degree_lt_modulus_degree_(poly_mod)
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.get_num_nonzero_coeffs_(poly)

    #@abstractmethod
    @override
    def iter_strict_sorted_degree_nonzero_coeff_pairs_ex_(ops, poly_mod, /, *, reverse:bool):
        'ops<z> -> z -> Iter (degree/uint, coeff/{=!=0}) # [degree strictly decreased] if reverse else [degree strictly increased]'
        poly = ops.to_polynomial_of_degree_lt_modulus_degree_(poly_mod)
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        return ops4modulus.iter_strict_sorted_degree_nonzero_coeff_pairs_ex_(poly, reverse=reverse)


    if 0b0:
        #???meaning less... since %modulus
        r'''[[[
        def is_polynomial_monic_(ops, poly_mod, /):
            #monic polynomial
        def are_all_coeffs_int_(ops, poly_mod, /):
        #]]]'''#'''










    @override
    def is_trivial_ring(ops, /):
        'ops<z> -> bool'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        # !! [ops.get_degree_of_the_monic_polynomial_modulus() > 0]
        return ring_ops4coeff.is_trivial_ring()
        return ring_ops4coeff.is_trivial_ring() and ops.get_degree_of_the_monic_polynomial_modulus() > 0

    @override
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        # !! [ops.get_degree_of_the_monic_polynomial_modulus() > 0]
        return ring_ops4coeff.is_mul_commutative()
        return ring_ops4coeff.is_mul_commutative() and ops.get_degree_of_the_monic_polynomial_modulus() > 0
    @override
    def is_mul_idempotent(ops, /):
        'ops<z> -> bool'
        # deg increase
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_mul_idempotent() and ops.get_degree_of_the_monic_polynomial_modulus() < 2
        return False

    # normal API for IRingOps:
    @override
    def is_order_finite(ops, /):
        'ops<z> -> bool'
        ring_ops4coeff = ops.get_ring_ops4coeff()
        return ring_ops4coeff.is_order_finite() or ops.is_trivial_ring()
    #r'''[[[
    @override
    def is_multiplicative_group_order_finite(ops, /):
        'ops<z> -> bool # order4mul # order of multiplicative_group # [ZZ.multiplicative_group == {-1,+1}]'
        if ops.is_order_finite():
            return True
        #[ring_ops4coeff order inf]
        ring_ops4coeff = ops.get_ring_ops4coeff()
        if not ring_ops4coeff.is_multiplicative_group_order_finite():
            return False
        #[ring_ops4coeff order inf, but order4mul finite]
        #   eg: ZZ
        #return ???
        #??? to_prove
        return True
    #]]]'''#'''
    @override
    def get_xorder4add(ops, /):
        'ops<z> -> xorder4add/(-1|uint|...) #(-1 if not is_order_finite() else (order4add/uint if known else ...)) # '
        ring_ops4coeff = ops.get_ring_ops4coeff()
        xorder4add4coeff = ring_ops4coeff.get_xorder4add()
        # !! [ops.get_degree_of_the_monic_polynomial_modulus() > 0]
        if xorder4add4coeff is ...:
            return ...
        if xorder4add4coeff == -1:
            return -1
        sz = xorder4add4coeff
        deg = ops.get_degree_of_the_monic_polynomial_modulus()
        return sz**deg
    @override
    def get_xorder4mul(ops, /):
        'ops<z> -> xorder4mul/(-1|uint|...) #(-1 if not is_order_finite<multiplicative_group>() else (order4mul/uint if known else ...)) # '
        # order of multiplicative_group
        # number of ring units


        #if ops.is_the_monic_polynomial_modulus_irreducible() and ring_ops4coeff.is_field():
        if ops.is_field():
            return ops.get_xorder4add() -1
        if ops.get_degree_of_the_monic_polynomial_modulus() == 1:
            ring_ops4coeff = ops.get_ring_ops4coeff()
            return ring_ops4coeff.get_xorder4mul()
        if ops.is_trivial_ring():
            return 1
        return ... if ops.is_multiplicative_group_order_finite() else -1

    if 0:
        @override
        def is_field(ops, /):
            'ops<z> -> bool'
            return False

    #@staticmethod
    def _binop(nm, ops, lhs, rhs, /, *, result_is_poly, result_degree_lt_modulus_degree):
        return __class__._fwd_op(nm, ops, result_is_poly, result_degree_lt_modulus_degree, [(True, lhs), (True, rhs)])
    def _fwd_op(nm, ops, result_is_poly, result_degree_lt_modulus_degree, ispoly_arg_pairs, /, **kwds):
        ops4modulus = ops.get_polynomial_ring_ops4modulus()
        op = getattr(ops4modulus, nm)
        args = []
        poly_pairs = []
        for arg_is_poly, arg in ispoly_arg_pairs:
            if arg_is_poly:
                arg_mod = ops.to_polynomial_of_degree_lt_modulus_degree_(arg)
                poly_pairs.append((arg, arg_mod))
            args.append(arg)
        result = op(*args, **kwds)
        if result_is_poly:
            poly = result
            poly_mod = ops.mk5polynomial(poly, degree_lt_modulus_degree=result_degree_lt_modulus_degree)
            #seed.seq_tools.seq_index_if
            for (poly_, poly_mod_) in poly_pairs:
                if ops.eq(poly_mod, poly_mod_):
                    poly_mod = poly_mod_
                    break
            result = poly_mod
        return result

    @override
    def eq(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> bool'
        return __class__._binop('eq', ops, lhs, rhs, result_is_poly=False, result_degree_lt_modulus_degree=False)

    @override
    def add(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return __class__._binop('add', ops, lhs, rhs, result_is_poly=True, result_degree_lt_modulus_degree=True)

    @override
    def mul__rhs_coeff_ex(ops, lhs, coeff4rhs, /, *, reverse:bool):
        'ops<z> -> z -> coeff -> z'
        return __class__._fwd_op('mul__rhs_coeff_ex', ops, True, True, [(True, lhs), (False, coeff4rhs)], reverse=reverse)

    @override
    def mul__monic_monomial(ops, degree, poly_mod, /):
        'ops<z> -> degree/uint -> z -> z'
        return __class__._fwd_op('mul__monic_monomial', ops, True, False, [(False, degree), (True, poly_mod)])
    #lshift_ = mul__monic_monomial
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
        return __class__._binop('mul', ops, lhs, rhs, result_is_poly=True, result_degree_lt_modulus_degree=False)

    r'''[[[
    IPolynomialRingQuotientRingOps should override: #no div/divmod...
    @override
    def mul__monic_monomial(ops, degree, poly, /):
        'ops<z> -> degree/uint -> z -> z'
    @override
    def mul(ops, lhs, rhs, /):
        'ops<z> -> z -> z -> z'
    #]]]'''#'''

class ICommutativePolynomialRingQuotientRingOps(IPolynomialRingQuotientRingOps):
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
    `get_commutative_polynomial_ring_ops4modulus
    '''#'''
    #___all___
    @abstractmethod
    def get_commutative_polynomial_ring_ops4modulus(ops, /):
        'ops<z> -> commutative_polynomial_ring_ops4modulus/ICommutativePolynomialRingOps<modulus> #ICommutativePolynomialRingOps===IPolynomialRingOps+is_mul_commutative'
    @override
    def get_polynomial_ring_ops4modulus(ops, /):
        'ops<z> -> polynomial_ring_ops4modulus/IPolynomialRingOps<modulus>'
        return ops.get_commutative_polynomial_ring_ops4modulus()
    @override
    def use_the_monic_polynomial_modulus_irreducible_in_right_divmod(ops, /):
        'ops<z> -> bool # since may be not commutative'
        return True
    @override
    def is_mul_commutative(ops, /):
        'ops<z> -> bool'
        if not super().is_mul_commutative(): raise TypeError
        return True

class ICommutativePolynomialRingQuotientRingOps___modulus_is_monic_irreducible_polynomial(ICommutativePolynomialRingQuotientRingOps):
    #xxx class ModIrreduciblePolynomialFieldOps:
#class ICommutativePolynomialRingQuotientRingOps___modulus_is_monic_irreducible_polynomial(IRingOps):
    '[z =[def]= coeff[X]%modulus][modulus is monic irreducible polynomial][deg modulus > 0]'
    'modulo/vt; modulus/n, moduli/n.pl'
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
    `get_the_monic_irreducible_polynomial_modulus
    '''#'''
    #___all___
    @abstractmethod
    def get_the_monic_irreducible_polynomial_modulus(ops, /):
        'ops<z> -> the_monic_irreducible_polynomial_modulus/z'

    @override
    def is_the_monic_polynomial_modulus_irreducible(ops, /):
        'ops<z> -> bool'
        return True
    @override
    def get_the_monic_polynomial_modulus(ops, /):
        'ops<z> -> the_monic_polynomial_modulus/z'
        return ops.get_the_monic_irreducible_polynomial_modulus()





#class ISplittingFieldOfIrreduciblePolynomialOverFiniteFieldOps(IFiniteFieldOps):
#swap bases:class IFiniteFieldIrreduciblePolynomialSplittingFieldOps(ICommutativePolynomialRingQuotientRingOps___modulus_is_monic_irreducible_polynomial, IFiniteFieldOps):
class IFiniteFieldIrreduciblePolynomialSplittingFieldOps(IFiniteFieldOps, ICommutativePolynomialRingQuotientRingOps___modulus_is_monic_irreducible_polynomial):
    '[z =[def]= coeff[X]%modulus][modulus is monic irreducible polynomial][deg modulus > 0][coeff ring is finite field]'
    __slots__ = ()
    ___bases4all___ = True
    ___all___ = r'''
    `get_finite_field_coeff_polynomial_domain_ops4modulus
    '''#'''
    #___all___
    @abstractmethod
    def get_finite_field_coeff_polynomial_domain_ops4modulus(ops, /):
        'ops<z> -> finite_field_coeff_polynomial_domain_ops4modulus/IFiniteFieldCoeffPolynomialDomainOps<modulus> #IFiniteFieldCoeffPolynomialDomainOps===IPolynomialRingOps+get_ring_ops4coeff().is_finite_field'
    @override
    def get_commutative_polynomial_ring_ops4modulus(ops, /):
        'ops<z> -> commutative_polynomial_ring_ops4modulus/ICommutativePolynomialRingOps<modulus> #ICommutativePolynomialRingOps===IPolynomialRingOps+is_mul_commutative'
        return ops.get_finite_field_coeff_polynomial_domain_ops4modulus()





from seed.math.ops.algebra.IRingOps import IRingOps, IFieldOps, IFiniteFieldOps, IPolynomialRingOps
from seed.math.ops.algebra.IRingOps import PrimeFieldOps, the_rational_field_ops
from seed.math.ops.algebra.IRingOps import *

