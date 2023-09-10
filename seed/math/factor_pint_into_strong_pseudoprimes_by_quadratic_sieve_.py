#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_.py
now:
    from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_

view others/数学/整数分解/Quadratic-Sieve-Method.txt
[[
Quadratic Sieve Method
wget 'https://www.cs.virginia.edu/crab/QFS_Simple.pdf' -O 'The Quadratic Sieve Factoring Algorithm.pdf'
  good
  /sdcard/0my_files/book/math/factorint/202308/The Quadratic Sieve Factoring Algorithm.pdf
  [Q(x) =[def]= x**2-N]
  [x <- [floor_sqrtN-M..=floor_sqrtN+M]]
  [MM := [floor_sqrtN-M..=floor_sqrtN+M]]
  [Q(x)%p == 0]:
    [N =[%p]= x**2]
    [Legendre_symbol(N/p) == +1 == N**((p-1)///2) %p]
    [sqrts<%p>(N) =[def]= {x%p, p-x%p}]
  [Q(x) =[%p]= Q(y)]:
    [(x**2-y**2)%p == 0]
    [[x =[%p]= y]or[x =[%p]= -y]]
  [Q(x)%p == 0]:
    [x%p <- sqrts<%p>(N)]
  [prime include -1]
  generate primes, eval sqrts<%p>(N) (if not exist, discard the prime)
    [x__p_1 == {x | [x :<- MM][Q(x)%p == 0]} == MM /-\ [(rNp+i*p) | [rNp :<- sqrts<%p>(N)][i :: int]]]
    [x__p_k == {x | [x :<- MM][Q(x)%p**k == 0]} == MM /-\ [(rNp_k+i*p**k) | [rNp_k :<- sqrts<%p**k>(N)][i :: int]]]
        sqrts<%p**k>(N) <<== Shanks-Tonelli Algorithm
        e ../../python3_src/seed/math/sqrts_mod_.py
    这是筛%p
    还可提升，是筛%p**k
    这样就知道，所有数的 p幂因子
    再对比 比特数，就知道 有没有 额外因子，有则排除x
  不断 扩张 MM 直到 找到足够数量的x
  optimum value for:
    number of primes/the size of the factor base: [B := (e**sqrt(lnN*lnlnN))**(sqrt(2)/4)]
    sieving interval [M := B**3]
  an asymptotic running time for the QS of e √ 1.125ln(n)ln(ln(n)) #==(e**sqrt(1.125*lnN*lnlnN))

]]

[[
try:
    factor: n*II(prime_gen[:k]) instead n
    why?
        @[i :<- [0..<n]]:
            [num_good_js_(n;i) =[def]= len{j :<- [0..<n] | [gcd(i+j,n) > 1]}]
            [num_good_ratio_(n) =[def]= num_good_js_(n;0)/n]
            [num_good_js_(n;i) == n-phi(n)]
            [num_good_ratio_(n) == (n-phi(n))/n]
        if [n==p*q]:
            [num_good_js_(n;i) == n-phi(n) == p*q-(p-1)*(q-1) == p+q-1]
            [num_good_ratio_(n) == (p+q-1)/p/q == 1/p+1/q-1/n]
        if [n==p*q*2*3]:
            [num_good_js_(n;i) == n-phi(n) == p*q*2*3-(p-1)*(q-1)*1*2 == 4*p*q +2*p+2*q-2]
            [num_good_ratio_(n) == (4*p*q +2*p+2*q-2)/p/q/6 == 2/3 +1/3*(1/p+1/q-1/n)]
            this may ease find matchs or small square

]]



seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_
py -m nn_ns.app.debug_cmd   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ -x
py -m nn_ns.app.doctest_cmd seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_:__doc__ -ff -v




from seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ import factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_, factor_pint_as_pefect_power_, detect_pefect_kth_root_






######################
######################
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='199 * 257' +verbose -grow_size_from_null_instead_optimum_size
semi-factor by trial_division<max1=1024>(51143): ... ...
semi-factor by trial_division<max1=1024>(51143):duration: 0.005687769999999981 *(unit: 0:00:01)
{199: 1, 257: 1}
######################

py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='199 * 257' +verbose --upperbound4prime_factor4trial_division=199 -grow_size_from_null_instead_optimum_size
... ...
sprp-factors-of(51143) = [199, 257]
sprp-factorization-of(51143) = {199: 1, 257: 1}
{199: 1, 257: 1}
######################
######################





######################
######################
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**17'
131101
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**16'
65537
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**13'
8209

py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='8209 * 65537' +verbose --upperbound4prime_factor4trial_division=199 -grow_size_from_null_instead_optimum_size
... ...
QS-init j2neg1p2e4Qx: ... ...
QS-init j2neg1p2e4Qx:duration: 0.009505615999999995 *(unit: 0:00:01)
QS-init i2neg1prime_base: ... ...
QS-init i2neg1prime_base:duration: 0.00012984599999998903 *(unit: 0:00:01)
QS-init-prepare<n=537993233, B=16, M=4096>: floor_log2(n)=29, floor_log2(B)=4, floor_log2(M)=12:duration: 0.08901846200000008 *(unit: 0:00:01)
_quadratic_sieve_: B=16, M=4096
mk mx<17,85>: ... ...
mk mx<17,85>:duration: 0.0058362310000000805 *(unit: 0:00:01)
solve_matrix: ... ...
solve_matrix:duration: 0.459997232 *(unit: 0:00:01)
find factors from solutions: ... ...
find factors from solutions:duration: 0.00574253899999988 *(unit: 0:00:01)
_quadratic_sieve_(537993233):duration: 0.562242848 *(unit: 0:00:01)
_quadratic_sieve_(537993233) = (65537, 8209)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 8209
detect strong_pseudoprime(8209): ... ...
detect strong_pseudoprime(8209):duration: 0.0001125390000000781 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 65537
detect strong_pseudoprime(65537): ... ...
detect strong_pseudoprime(65537):duration: 9.076999999990676e-05 *(unit: 0:00:01)
sprp-factors-of(537993233) = [8209, 65537]
sprp-factorization-of(537993233) = {8209: 1, 65537: 1}
{8209: 1, 65537: 1}
######################
0.6 second <<==:
_quadratic_sieve_(537993233):duration: 0.562242848 *(unit: 0:00:01)

######################
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='8209 * 65537' +verbose --upperbound4prime_factor4trial_division=199 +grow_size_from_null_instead_optimum_size
... ...
... ...
QS-init on prime p=47, kk=5: ... ...
QS-init on prime p=47, kk=5:duration: 0.000396923000000049 *(unit: 0:00:01)
QS-init on primes:duration: 0.013012308000000083 *(unit: 0:00:01)
QS-init j2neg1p2e4Qx: ... ...
QS-init j2neg1p2e4Qx:duration: 0.00187046099999999 *(unit: 0:00:01)
QS-init i2neg1prime_base: ... ...
QS-init i2neg1prime_base:duration: 0.00011938499999997187 *(unit: 0:00:01)
QS-init-prepare<n=537993233, B=8, M=512>: floor_log2(n)=29, floor_log2(B)=3, floor_log2(M)=9:duration: 0.022120923000000015 *(unit: 0:00:01)
_quadratic_sieve_: B=8, M=512
mk mx<9,10>: ... ...
mk mx<9,10>:duration: 0.0007626920000000093 *(unit: 0:00:01)
solve_matrix: ... ...
solve_matrix:duration: 0.019949076000000066 *(unit: 0:00:01)
find factors from solutions: ... ...
find factors from solutions:duration: 0.00046315399999996565 *(unit: 0:00:01)
_quadratic_sieve_(537993233):duration: 0.06600784599999998 *(unit: 0:00:01)
_quadratic_sieve_(537993233) = (8209, 65537)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 65537
detect strong_pseudoprime(65537): ... ...
detect strong_pseudoprime(65537):duration: 0.00025746100000001437 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 8209
detect strong_pseudoprime(8209): ... ...
detect strong_pseudoprime(8209):duration: 0.0001477690000000198 *(unit: 0:00:01)
sprp-factors-of(537993233) = [65537, 8209]
sprp-factorization-of(537993233) = {65537: 1, 8209: 1}
{65537: 1, 8209: 1}
######################
0.07 second <<==:
_quadratic_sieve_(537993233):duration: 0.06600784599999998 *(unit: 0:00:01)
######################
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='65537**3' +verbose --upperbound4prime_factor4trial_division=199 +grow_size_from_null_instead_optimum_size
... ...
... ...
semi-factor by trial_division<max1=199>(281487861809153): ... ...
semi-factor by trial_division<max1=199>(281487861809153):duration: 0.005862153000000037 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 281487861809153
detect strong_pseudoprime(281487861809153): ... ...
detect strong_pseudoprime(281487861809153):duration: 0.0003166150000000201 *(unit: 0:00:01)
detect pefect_power(281487861809153): ... ...
floor_sqrt(281487861809153): ... ...
floor_sqrt(281487861809153):duration: 0.00018300000000004424 *(unit: 0:00:01)
floor_kth_root_(3, 281487861809153): ... ...
floor_kth_root_(3, 281487861809153):duration: 0.0002243080000000619 *(unit: 0:00:01)
floor_kth_root_(3, 65537): ... ...
floor_kth_root_(3, 65537):duration: 0.000164922999999928 *(unit: 0:00:01)
floor_kth_root_(5, 65537): ... ...
floor_kth_root_(5, 65537):duration: 0.0001497689999999663 *(unit: 0:00:01)
floor_kth_root_(7, 65537): ... ...
floor_kth_root_(7, 65537):duration: 9.6922999999971e-05 *(unit: 0:00:01)
floor_kth_root_(11, 65537): ... ...
floor_kth_root_(11, 65537):duration: 9.599999999998499e-05 *(unit: 0:00:01)
floor_kth_root_(13, 65537): ... ...
floor_kth_root_(13, 65537):duration: 9.507699999999897e-05 *(unit: 0:00:01)
detect pefect_power(281487861809153):duration: 0.0025474620000000003 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 65537
detect strong_pseudoprime(65537): ... ...
detect strong_pseudoprime(65537):duration: 0.00023723100000005992 *(unit: 0:00:01)
sprp-factors-of(281487861809153) = [65537]
sprp-factorization-of(281487861809153) = {65537: 3}
{65537: 3}
######################
ok:factor_pint_as_pefect_power_ <<==:
floor_kth_root_(3, 281487861809153): ... ...
floor_kth_root_(3, 281487861809153):duration: 0.0002243080000000619 *(unit: 0:00:01)
floor_kth_root_(3, 65537): ... ...
floor_kth_root_(3, 65537):duration: 0.000164922999999928 *(unit: 0:00:01)
floor_kth_root_(5, 65537): ... ...

######################
######################
######################




















######################
######################
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**72'
4722366482869645213711
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**50'
1125899906842679
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='1125899906842679 * 4722366482869645213711' +verbose -grow_size_from_null_instead_optimum_size
... ...
... ...
QS-init-prepare<n=5316911983139923221788674570210771769, B=943, M=838561807>: floor_log2(n)=122, floor_log2(B)=9, floor_log2(M)=29: ... ...
QS-init-prepare log2_Qx__ls: ... ...
    # mk log2_Qx__ls of len > 2**29
    #   memory consume to much, quiet useless
... ...
... ...  KeyboardInterrupt
######################
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='1125899906842679 * 4722366482869645213711' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size
... ...
... ...
QS-init-prepare<n=5316911983139923221788674570210771769, B=256, M=16777216>: floor_log2(n)=122, floor_log2(B)=8, floor_log2(M)=24: ... ...
QS-init-prepare log2_Qx__ls: ... ...
^CQS-init-prepare log2_Qx__ls:duration: 22.239237118 *(unit: 0:00:01)
QS-init-prepare<n=5316911983139923221788674570210771769, B=256, M=16777216>: floor_log2(n)=122, floor_log2(B)=8, floor_log2(M)=24:duration: 22.239407578999998 *(unit: 0:00:01)
_quadratic_sieve_(5316911983139923221788674570210771769):duration: 40.544477939000004 *(unit: 0:00:01)
Traceback (most recent call last):
... ...
... ...
KeyboardInterrupt
######################


py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='8209 * 65537' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size
_quadratic_sieve_: B=18, M=256
    final state
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='8209 * 65537' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
_quadratic_sieve_: B=23, M=512
    final state
        worse when turnon +time_6
            but an example below better!



py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='131101 * 65537' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
_quadratic_sieve_: B=37, M=2048
mk mx<38,68>: ... ...
    final state

py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='131101 * 65537' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
_quadratic_sieve_: B=37, M=2048
mk mx<38,55>: ... ...
    final state


py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**25'
33554467
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**25+2**14+2**11'
33572881
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**35+2**24+2**19'
34377039877


py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33554467 * 65537' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size
_quadratic_sieve_: B=47, M=4096
mk mx<48,63>: ... ...

py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33554467 * 65537' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
_quadratic_sieve_: B=37, M=2048
mk mx<38,75>: ... ...
        better when turnon +time_6
            but an example above worse!




py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33554467 * 33572881' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size
_quadratic_sieve_: B=6, M=16
mk mx<7,1>: ... ...
    ??????
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33554467 * 33572881' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
_quadratic_sieve_: B=96, M=32768
mk mx<97,145>: ... ...
    !!!!!!





py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33554467 * 33572881 * 34377039877' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
_quadratic_sieve_: B=308, M=1048576
mk mx<309,212>: ... ...
KeyboardInterrupt
    to slow at 『solve_matrix: ... ...』

py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33554467 * 33572881 * 34377039877' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size
_quadratic_sieve_: B=244, M=524288
mk mx<245,247>: ... ...
    一次发现3个因子？
    看来+time_6 是真的不行
QS-init-prepare<n=38726427349072400660120479, B=244, M=524288>: floor_log2(n)=85, floor_log2(B)=7, floor_log2(M)=19:duration: 12.844326860999999 *(unit: 0:00:01)
_quadratic_sieve_: B=244, M=524288
mk mx<245,247>: ... ...
mk mx<245,247>:duration: 0.12084561599999688 *(unit: 0:00:01)
solve_matrix: ... ...
solve_matrix:duration: 68.207220495 *(unit: 0:00:01)
find factors from solutions: ... ...
find factors from solutions:duration: 0.011779922999991754 *(unit: 0:00:01)
_quadratic_sieve_(38726427349072400660120479):duration: 117.11754713 *(unit: 0:00:01)
_quadratic_sieve_(38726427349072400660120479) = (33572881, 34377039877, 33554467)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 33554467
detect strong_pseudoprime(33554467): ... ...
detect strong_pseudoprime(33554467):duration: 0.00012346200000479257 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 34377039877
detect strong_pseudoprime(34377039877): ... ...   detect strong_pseudoprime(34377039877):duration: 0.00013146100000938077 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 33572881
detect strong_pseudoprime(33572881): ... ...
detect strong_pseudoprime(33572881):duration: 7.26920000033715e-05 *(unit: 0:00:01)
sprp-factors-of(38726427349072400660120479) = [33554467, 34377039877, 33572881]
sprp-factorization-of(38726427349072400660120479) = {33554467: 1, 34377039877: 1, 33572881: 1}
{33554467: 1, 34377039877: 1, 33572881: 1}












py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33572881 * 5**15' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
... ...
QS-init-prepare<n=6147378112792968750, B=2, M=2>: floor_log2(n)=62, floor_log2(B)=1, floor_log2(M)=1: ... ...
QS-init-prepare log2_Qx__ls: ... ...
QS-init-prepare log2_Qx__ls:duration: 0.0003017690000000073 *(unit: 0:00:01)
QS-init on primes: ... ...
QS-init found_prime_factor: [6147378112792968750%5 == 0]
QS-init drop prime 5
QS-init drop prime 7
QS-init drop prime 11
... ...



py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33572881 * 8209**3' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size +time_6
_quadratic_sieve_: B=153, M=131072
mk mx<154,109>: ... ...
_quadratic_sieve_: B=193, M=262144
mk mx<194,270>: ... ...
KeyboardInterrupt


py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_  ='33572881 * 8209**3' +verbose --upperbound4prime_factor4trial_division=3 +grow_size_from_null_instead_optimum_size
_quadratic_sieve_: B=96, M=32768
mk mx<97,183>: ... ...
mk mx<97,183>:duration: 0.03569646300000073 *(unit: 0:00:01)
solve_matrix: ... ...
solve_matrix:duration: 13.157571641999999 *(unit: 0:00:01)
File "/sdcard/0my_files/git_repos/python3_src/seed/math/factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_.py", line 1002, in _quadratic_sieve_
    assert all(e&1==0 for e in acc__neg1p2e.values())
AssertionError
######after fix bug: put 3 into prime_bases when init:
QS-init-prepare<n=18572030067003190849, B=96, M=32768>: floor_log2(n)=64, floor_log2(B)=6, floor_log2(M)=15:duration: 0.8384727710000002 *(unit: 0:00:01)
_quadratic_sieve_: B=96, M=32768
mk mx<97,179>: ... ...
mk mx<97,179>:duration: 0.03508984599999998 *(unit: 0:00:01)
solve_matrix: ... ...
solve_matrix:duration: 12.698674572 *(unit: 0:00:01)
find factors from solutions: ... ...
find factors from solutions:duration: 0.02250346199999953 *(unit: 0:00:01)
_quadratic_sieve_(18572030067003190849):duration: 17.156134272 *(unit: 0:00:01)
_quadratic_sieve_(18572030067003190849) = (33572881, 553185473329)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 553185473329
detect strong_pseudoprime(553185473329): ... ...  detect strong_pseudoprime(553185473329):duration: 0.00015846199999813848 *(unit: 0:00:01)
detect pefect_power(553185473329): ... ...
floor_sqrt(553185473329): ... ...
floor_sqrt(553185473329):duration: 7.423099999925853e-05 *(unit: 0:00:01)
floor_kth_root_(3, 553185473329): ... ...
floor_kth_root_(3, 553185473329):duration: 7.36160000016639e-05 *(unit: 0:00:01)
floor_kth_root_(3, 8209): ... ...
floor_kth_root_(3, 8209):duration: 4.738499999845658e-05 *(unit: 0:00:01)
floor_kth_root_(5, 8209): ... ...
floor_kth_root_(5, 8209):duration: 7.730700000152524e-05 *(unit: 0:00:01)
floor_kth_root_(7, 8209): ... ...
floor_kth_root_(7, 8209):duration: 5.053900000007161e-05 *(unit: 0:00:01)
floor_kth_root_(11, 8209): ... ...
floor_kth_root_(11, 8209):duration: 6.461599999951773e-05 *(unit: 0:00:01)
floor_kth_root_(13, 8209): ... ...
floor_kth_root_(13, 8209):duration: 8.707699999987994e-05 *(unit: 0:00:01)
detect pefect_power(553185473329):duration: 0.0011434620000017048 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 8209
detect strong_pseudoprime(8209): ... ...
detect strong_pseudoprime(8209):duration: 7.238400000275647e-05 *(unit: 0:00:01)
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: 33572881
detect strong_pseudoprime(33572881): ... ...
detect strong_pseudoprime(33572881):duration: 9.446199999985083e-05 *(unit: 0:00:01)
sprp-factors-of(18572030067003190849) = [8209, 33572881]
sprp-factorization-of(18572030067003190849) = {8209: 3, 33572881: 1}
{8209: 3, 33572881: 1}









######################
######################
quadratic_sieve vs trial_division #_calc_asymptotic_running_time4QS_
    2**40?
    2**16?
    to set "default_upperbound4prime_factor4trial_division"
        see:factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_()::kw:upperbound4prime_factor4trial_division
py_adhoc_call   seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_   @_find_e_that_quadratic_sieve_faster_than_trial_division_if_n_eq_pow2_e_
>>> _find_e_that_quadratic_sieve_faster_than_trial_division_if_n_eq_pow2_e_()
16

######################
######################

>>> _3th_root_of_2
1.2599210498948732
>>> _3th_root_of_2**3
2.0

>>> from seed.helper.stable_repr import stable_repr
>>> stable_repr(factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_(8209 * 65537, verbose=False, upperbound4prime_factor4trial_division=3, grow_size_from_null_instead_optimum_size=True))
'{8209: 1, 65537: 1}'


#]]]'''
__all__ = r'''
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_
    factor_pint_as_pefect_power_
    detect_pefect_kth_root_
'''.split()#'''
    #_coprimes5factors_
__all__

#import math
from math import log as ln_, log2 as log2_, exp as exp_
from math import sqrt as sqrt_, isqrt as isqrt_
from math import ceil as ceil_, floor as floor_
from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_, iter_sqrts_mod_prime_power__coprime__5one_sqrt_
#from seed.math.sqrts_mod_ import is_square_residual_mod_prime_
from seed.math.Jacobi_symbol import Jacobi_symbol
    #def Jacobi_symbol(M, x, /):
    #    'M/int{%2==1} -> x/int -> Jacobi_symbol(x::/M)/(-1|0|+1)'



from seed.math.prime_gens import prime_gen
from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_, calc_len_prime_basis4II_prime_basis_gtN_
from seed.math.prime_gens import prime_basis4A014233



from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers #factor_pint_out_power_of_base_
from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_ex_, default4upperbound4probably_prime, check_result5factor_pint_
from seed.math.factor_pint_by_trial_division_ import _is_prime__tribool4factor_pint_



from seed.tiny import print_err
from seed.tiny import check_type_is
from seed.math.II import II, II_mod
from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division


from seed.math.gcd import gcd#, gcd_many, are_coprime
from seed.math.floor_ceil import floor_sqrt, ceil_sqrt
from seed.math.floor_ceil import floor_kth_root_, ceil_kth_root_
from seed.math.floor_ceil import floor_log_, floor_log2
from seed.math.merge_coprimess_into_smaller_coprimes import merge_coprimess_into_smaller_coprimes# semi_factor_coprimess_via_gcd
from seed.math.matrix.solve_matrix import NoRowMatrix, linear_solver, ring_ex_ops__Fraction, ring_ex_ops__BinaryField
    #def solve_equations__matrix__to_representative_solutions(sf, ring_ex_ops, lhs_mx, rhs_mx, /, *, validate):
    #    '-> representative_solutions/Array<(0|(1+(N-L)*K)), matrix<N,K> >'
    #def mk_matrix__default(sf, num_rows, num_cols, default, /):
    #def mk_matrix__ij2v(sf, num_rows, num_cols, ij2v, /):



from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)


__all__
if 1:
    _timer = timer__print_err__thread_wide
    #with _timer(prefix=, _fmt_=, _show_hint_on_enter_=True, _to_show_=verbose):

def _find_e_that_quadratic_sieve_faster_than_trial_division_if_n_eq_pow2_e_():
    #quadratic_sieve vs trial_division
    for e in range(1000):
        n = 1<<e
        time4quadratic_sieve = _calc_asymptotic_running_time4QS_(n)
        time4trial_division = floor_sqrt(n)
        if time4quadratic_sieve < time4trial_division:
            return e
    else:
        raise 000
def _calc_asymptotic_running_time4QS_(n, /):
    'asymptotic running time for the QS of e √ 1.125ln(n)ln(ln(n)) #==(e**sqrt(1.125*lnN*lnlnN))'
    # [lnlnN exists] <==> [lnN > 0] <==> [N >= 3]
    if not n >= 3:
        return 1.0
    lnN = ln_(n)
    lnlnN = ln_(lnN)
    T = (exp_(sqrt_(lnN*lnlnN*9.0/8.0))) # == B**3 == M
    return T

def _calc_optimum_values4QS_(n, /):
    'n -> (B, M)  #size4prime_factor_base:[B := (e**sqrt(lnN*lnlnN))**(sqrt(2)/4)]; half_size4sieving_interval:[M := B**3]'
    # [lnlnN exists] <==> [lnN > 0] <==> [N >= 3]
    if not n >= 3:
        return 1.0
    lnN = ln_(n)
    lnlnN = ln_(lnN)
    B = ceil_(exp_(sqrt_(lnN*lnlnN/8.0)))
    M = B**3
    return (B, M)


def _Q_(n, x, /):
    return x**2 -n #keep small # DONOT (%n)
def _sieving_loop_(x0, x_end, p, kk, rs__p_kk, p_kk, x0__p_kk, /):
    p_k = p_kk
    x0__p_k = x0__p_kk
    rs__p_k = rs__p_kk
    for k in reversed(range(1, kk+1)):
        for r in rs__p_k:
            if r < x0__p_k:
                r += p_k
            for offseted_x in range(r-x0__p_k, x_end-x0, p_k):
                yield k, offseted_x
        ######################
        #next round:
        p_k //= p
        x0__p_k %= p_k
        #rs__p_k =:
        if k == 1:
            # [next k == 0]
            rs__p_k = [0]
        else:
            # [next k > 0]
            r0 = rs__p_k[0]
            r0 %= p_k
            [*rs__p_k] = iter_sqrts_mod_prime_power__coprime__5one_sqrt_(p, k-1, p_k, r0)
        rs__p_k
        ######################
    #end-for k in reversed(range(1, kk+1)):
    ######################
    assert p_k == 1
    assert not any(rs__p_k)
    ######################
    return
class _D23_(dict):pass
def _body4prepare4QS_(n, B, M, ceil_sqrtN, /, *, verbose, time_6):
    def save__offseted_x_(p, offseted_x, /):
        j2offseted_x.append(offseted_x)
    j2offseted_x = []

    sieving_interval = range(ceil_sqrtN-M, ceil_sqrtN+M)
    x0 = sieving_interval[0]
    x_end = sieving_interval[-1]+1
    Qx0 = _Q_(n, x0)
    with _timer(prefix='QS-init-prepare log2_Qx__ls', _show_hint_on_enter_=True, _to_show_=verbose):
        #Qx__ls = [x**2 -n for x in sieving_interval]
        #Qx__ls = [Qx0]
        log2_Qx__ls = [] #offseted at x0
            # orinal:omit sign:[log2_Qx__ls[x-x0] == p2e/dict or log2(abs(Q(x)))]
            # now:omit {sign,2}:[log2_Qx__ls[x-x0] == p2e/dict or log2(abs(Q(x)) >> gde_(2; abs(Q(x))))]
            #
        Qx = Qx0
        max_x4neg_Qx = x0
        #offseted_xs__Qx_is_2power = []
        spectial_treated_primes = (2,3)
        for x in sieving_interval:
            # treat_2_specially
            # treat_3_specially
            uuu = abs(Qx)
            #bug:assert not uuu == 1
            #(e, uuu) = factor_pint_out_power_of_base_(p, uuu)
            (p2e__23, uuu) = semi_factor_pint_via_trial_division(spectial_treated_primes, uuu)
            if 0b0:
                if verbose:
                    if e:
                        print_err(f'n={n}, x={x}, Qx={Qx}={uuu}*{p}**{e}')
            if uuu == 1:
                #store e for 2,3
                #   since no other p can found it
                p2e__23 = _D23_(p2e__23)
                offseted_x = x -x0
                #log2_Qx__ls.append({p:e} if e else {})
                log2_Qx__ls.append(p2e__23)
                p = min(p2e__23, default=2)
                save__offseted_x_(p, offseted_x)
            else:
                #discard e for 2,3
                #   since x may be discard, neednot save info for it
                #
                #   will find back later by recompute... if needed
                #
                log2_Qx__ls.append(log2_(uuu))
            ######################
            if Qx < 0:
                max_x4neg_Qx = x
            Qx += 2*x+1
        Qx_end = Qx
        assert Qx_end == _Q_(n, x_end)
        assert max_x4neg_Qx == ceil_sqrtN -1
        max_offseted_x4neg_Qx = max_x4neg_Qx -x0

    log2_Qx__ls
    max_offseted_x4neg_Qx
    assert max_offseted_x4neg_Qx == M-1

    _many = []
    def save__many_(p, kk, rs__p_kk, p_kk, x0__p_kk, /):
        'for reuse-_sieving_loop_'
        _many.append((p, kk, rs__p_kk, p_kk, x0__p_kk))
    def iter__many_():
        '-> Iter (p, kk, rs__p_kk, p_kk, x0__p_kk) #match save__many_'
        return iter(_many)

    #prime_bases = prime_gen[B]
    #    dynamic determine...


    # treat_2_specially
    # treat_3_specially
    # treat_neg1_specially
    #prime_bases = [-1]
    prime_bases = [*spectial_treated_primes]
    found_prime_factors = []
        #e.g. debugging: [upperbound4prime_factor4trial_division := 3]
    def on_new_p4loop_body_(p, log2_p, kk, rs__p_kk, /):
        prime_bases.append(p)
        p_kk = p**kk
        x0__p_kk = x0%p_kk
        save__many_(p, kk, rs__p_kk, p_kk, x0__p_kk)
        if p > 2:
            assert len(rs__p_kk) == 2
        for k, offseted_x in _sieving_loop_(x0, x_end, p, kk, rs__p_kk, p_kk, x0__p_kk):
            log2_Qx__ls[offseted_x] -= log2_p
            if k == 1:
                #if log2_Qx__ls[offseted_x] < log2_p:
                if log2_Qx__ls[offseted_x] < log2_p/2.0:
                    # since p grows, [remain bit < log2_p] means has no further factor, all possible factor are processed (dropped primes cannot be factor)
                    #   except [n%p==0]
                    log2_Qx__ls[offseted_x] = {} # to save p2e
                    save__offseted_x_(p, offseted_x)
            ######################
        #end-for k, offseted_x in _sieving_loop_(x0, x_end, p, kk, rs__p_kk, p_kk, x0__p_kk):
        return
    #end-def on_new_p4loop_body_(p, log2_p, kk, rs__p_kk, /):
    ######################
    with _timer(prefix='QS-init on primes', _show_hint_on_enter_=True, _to_show_=verbose):
        #for p in prime_bases:
        for p in prime_gen:
            # [p :: prime]
            if not len(prime_bases) < B:
                break
            # treat_2_specially
            if p==2:continue
            # [p :: prime][p =!= 2]
            # [p :: prime][p%2 == 1] #required by Jacobi_symbol

            ######################
            # see:time_6
            # treat_3_specially
            if p==3:continue
            ######################
            if n%p == 0:
                to_drop_p = True
                #if not (time_6 and p==3):
                if 1:
                    found_prime_factors.append(p)
                        #e.g. debugging: [upperbound4prime_factor4trial_division := 3]
                    if verbose:
                        print_err(f'QS-init found_prime_factor: [{n}%{p} == 0]')
            else:
                #to_drop_p = not is_square_residual_mod_prime_(p, n)
                assert p&1
                to_drop_p = not Jacobi_symbol(p, n) == +1
                        #Jacobi_symbol(odd M;n)
            if to_drop_p:
                #drop p
                if verbose:
                    print_err(f'QS-init drop prime {p}')
                continue
            ######################
            #bug?:kk = floor_log_(p, 2*M)
            #kk = floor_log_(p, Qx_end)
            #kk = floor_log_(p, (ceil_sqrtN+M-1)**2-n)
            #kk = floor_log_(p, 2*M*(ceil_sqrtN-1) +M**2)
            log2_p = log2_(p)
            kk = floor_(log2_Qx__ls[-1]//log2_p) +1+2
            rs__p_kk = [*iter_sqrts_mod_prime_power_(p, kk, n)]
            ######################
            with _timer(prefix=f'QS-init on prime p={p}, kk={kk}', _show_hint_on_enter_=True, _to_show_=verbose):
                on_new_p4loop_body_(p, log2_p, kk, rs__p_kk)
            ######################
        #end-for p in prime_gen:
    #end-with _timer(prefix='QS-init on primes', _show_hint_on_enter_=True, _to_show_=verbose):
    ######################
    prime_bases
    found_prime_factors
    j2offseted_x
    log2_Qx__ls
    assert len(prime_bases) == max(B, len(spectial_treated_primes))









    with _timer(prefix=f'QS-init j2neg1p2e4Qx', _show_hint_on_enter_=True, _to_show_=verbose):
        p2e5offseted_x = log2_Qx__ls
        log2_Qx__ls = None
        #save__many_ 2nd sieve...
        for (p, kk, rs__p_kk, p_kk, x0__p_kk) in iter__many_():
            for k, offseted_x in _sieving_loop_(x0, x_end, p, kk, rs__p_kk, p_kk, x0__p_kk):
                p2e4Qx = p2e5offseted_x[offseted_x]
                if not type(p2e4Qx) is dict:
                    continue
                p2e4Qx.setdefault(p, 0)
                p2e4Qx[p] += 1
        p2e4Qx = None

        j2p2e4Qx = []
        for offseted_x in j2offseted_x:
            p2e4Qx = p2e5offseted_x[offseted_x]
            j2p2e4Qx.append(p2e4Qx)
        p2e5offseted_x = None
        #if 0b0:print_err(j2p2e4Qx[:5])
        assert len(j2p2e4Qx) == len(j2offseted_x)

        for offseted_x, p2e4Qx in zip(j2offseted_x, j2p2e4Qx):
            if offseted_x <= max_offseted_x4neg_Qx:
                # treat_neg1_specially
                p2e4Qx[-1] = 1
            if not type(p2e4Qx) is _D23_:
                assert not 2 in p2e4Qx
                assert not 3 in p2e4Qx
                # treat_2_specially
                # treat_3_specially
                x = x0 +offseted_x
                Qx = _Q_(n, x)
                uuu = abs(Qx)
                (p2e__23, uuu) = semi_factor_pint_via_trial_division(spectial_treated_primes, uuu)
                p2e4Qx.update(p2e__23)
            if verbose:
                assert II(p**e for p,e in p2e4Qx.items()) == Qx, (n, offseted_x, x, p2e4Qx, Qx)
        j2neg1p2e4Qx = j2p2e4Qx
        j2p2e4Qx = None


    with _timer(prefix=f'QS-init i2neg1prime_base', _show_hint_on_enter_=True, _to_show_=verbose):
        # treat_neg1_specially
        i2neg1prime_base = (-1, *prime_bases)
        prime_bases = None

    assert -1 in i2neg1prime_base
    assert 2 in i2neg1prime_base
    assert 3 in i2neg1prime_base

    found_prime_factors
    i2neg1prime_base
    j2offseted_x
    j2neg1p2e4Qx
    assert len(i2neg1prime_base) == 1+max(B, len(spectial_treated_primes))
    assert len(j2neg1p2e4Qx) == len(j2offseted_x)
    return (B, M, x0, x_end, max_offseted_x4neg_Qx, i2neg1prime_base, j2offseted_x, j2neg1p2e4Qx, found_prime_factors)
        # [x<j> == x0+j2offseted_x[j]]
        # [Q(x<j>) == II__p2e_(j2neg1p2e4Qx[j])]
        # [len(i2neg1prime_base) == 1+B]
        #
#end-def _body4prepare4QS_(n, B, M, ceil_sqrtN, /, *, verbose):
def _prepare4QS_(n, /, *, verbose, grow_size_from_null_instead_optimum_size, time_6):
    '-> Iter (B, M, x0, x_end, max_offseted_x4neg_Qx, i2neg1prime_base, j2offseted_x, j2neg1p2e4Qx, found_prime_factors)'
    if time_6:
        assert n%6 in [1,5]
        n *= 6
    if grow_size_from_null_instead_optimum_size:
        B = 1
        M = B**3
    else:
        (B, M) = _calc_optimum_values4QS_(n)
    assert M
    ceil_sqrtN = isqrt_(n)+1
    while 1:
        with _timer(prefix=f'QS-init-prepare<n={n}, B={B}, M={M}>: floor_log2(n)={floor_log2(n)}, floor_log2(B)={floor_log2(B)}, floor_log2(M)={floor_log2(M)}', _show_hint_on_enter_=True, _to_show_=verbose):
            (B, M, x0, x_end, max_offseted_x4neg_Qx, i2neg1prime_base, j2offseted_x, j2neg1p2e4Qx, found_prime_factors) = _body4prepare4QS_(n, B, M, ceil_sqrtN, verbose=verbose, time_6=time_6)
        yield (B, M, x0, x_end, max_offseted_x4neg_Qx, i2neg1prime_base, j2offseted_x, j2neg1p2e4Qx, found_prime_factors)
        ######################
        #next round:
        if 0:
            B <<= 1
            M <<= 3
        else:
            #bug:when[B==1]:B = floor_(_3th_root_of_2 * B)
            B = ceil_(_3th_root_of_2 * B)
            M <<= 1
_3th_root_of_2 = 2.0**(1.0/3.0)


default_upperbound4prime_factor4trial_division = 1024
default_upperbound4prime_factor4trial_division = 2**16
    # !! [_find_e_that_quadratic_sieve_faster_than_trial_division_if_n_eq_pow2_e_() == 16]
    # to use quadratic_sieve, [n >= 2**16]
    #
def factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_(n, /, *, verbose=False, upperbound4prime_factor4trial_division=default_upperbound4prime_factor4trial_division, grow_size_from_null_instead_optimum_size=True, time_6=False):
    'n/int{>=1} -> sprp2e/{strong_pseudoprime/int:exp/int{>=1}}'
    check_type_is(int, n)
    check_type_is(int, upperbound4prime_factor4trial_division)

    if not n > 0:raise ValueError(n)

    #if not upperbound4prime_factor4trial_division > 2: raise ValueError
    upperbound4prime_factor4trial_division = max(3, upperbound4prime_factor4trial_division)
    assert upperbound4prime_factor4trial_division > 2
        # below requires: [upperbound4prime_factor4trial_division > 2]
        #
    with _timer(prefix=f'semi-factor by trial_division<max1={upperbound4prime_factor4trial_division}>({n})', _show_hint_on_enter_=True, _to_show_=verbose):
        (p2e, unfactored_part, may_next_prime_factor) = factor_pint_by_trial_division_ex_(n, may_upperbound4prime_factor=upperbound4prime_factor4trial_division)
    # [[unfactored_part==1] or [next_prime_factor >=upperbound4prime_factor4trial_division] or [unfactored_part is pseudoprime >=upperbound4probably_prime]]
    # !! [upperbound4prime_factor4trial_division > 2]
    # [unfactored_part is odd]
    sprp2e = p2e
    if unfactored_part == 1:
        return p2e
    else:
        assert not may_next_prime_factor is None
        next_prime_factor = may_next_prime_factor
        if next_prime_factor >= upperbound4prime_factor4trial_division:
            if unfactored_part < next_prime_factor**2:
                #prime
                p, unfactored_part = unfactored_part, 1
                p2e[p] = 1
                return p2e
            # [unfactored_part >= next_prime_factor**2]
        else:
            # [unfactored_part is pseudoprime >=upperbound4probably_prime]
            #strong_pseudoprime
            sprp, unfactored_part = unfactored_part, 1
            sprp2e[sprp] = 1
            return sprp2e
        # [unfactored_part >= next_prime_factor**2]
    # [unfactored_part >= next_prime_factor**2]

    if not detect_strong_pseudoprime__not_waste_too_much_time_(unfactored_part) == 0:
        #strong_pseudoprime
        sprp, unfactored_part = unfactored_part, 1
        sprp2e[sprp] = 1
        return sprp2e
    #bug:skip_check = True
    skip_check = upperbound4prime_factor4trial_division > prime_basis4A014233[-1]


    # [unfactored_part =!= 1]
    # [unfactored_part is odd]
    # [unfactored_part >= 3]
    main_unfactored_part = unfactored_part
    us = [main_unfactored_part]
        # :: [int{>=3, odd}]
    sprps = []
        # :: [strong_pseudoprime]
    while us:
        u = us.pop()
        if verbose:
            print_err(f'factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ main loop body: {u}')

        with _timer(prefix=f'detect strong_pseudoprime({u})', _show_hint_on_enter_=True, _to_show_=verbose):
            #if not detect_strong_pseudoprime__not_waste_too_much_time_(u) == 0:
            if not False is _is_prime__tribool4factor_pint_(skip_check, u):
                #strong_pseudoprime
                sprp = u
                sprps.append(sprp)
                continue

        #odd_composite
        odd_composite = u
        000;    u = None

        with _timer(prefix=f'detect pefect_power({odd_composite})', _show_hint_on_enter_=True, _to_show_=verbose):
            (odd_base, exp) = factor_pint_as_pefect_power_(odd_composite, verbose=verbose)
            #bug:odd_composite = odd_base
            #   odd_base may be sprp
            if exp > 1:
                us.append(odd_base)
                continue
            assert odd_base is odd_composite

        with _timer(prefix=f'_quadratic_sieve_({odd_composite})', _show_hint_on_enter_=True, _to_show_=verbose):
            coprimes = _quadratic_sieve_(odd_composite, verbose=verbose, grow_size_from_null_instead_optimum_size=grow_size_from_null_instead_optimum_size, time_6=time_6)
            assert len(coprimes) >= 2
        if verbose:
            print_err(f'_quadratic_sieve_({odd_composite}) = {coprimes}')

        us.extend(coprimes)

    if verbose:
        print_err(f'sprp-factors-of({main_unfactored_part}) = {sprps}')

    (_sprp2e, unfactored_part) = semi_factor_pint_via_trial_division(sprps, unfactored_part)
    assert unfactored_part == 1
    sprp2e.update(_sprp2e)
    may_next_prime_factor = None
    may_upperbound4prime_factor4trial_division = None
    upperbound4probably_prime = default4upperbound4probably_prime
    check_result5factor_pint_(n, sprp2e, unfactored_part, may_next_prime_factor, may_upperbound4prime_factor4trial_division, upperbound4probably_prime)
    if verbose:
        print_err(f'sprp-factorization-of({n}) = {sprp2e}')
    return sprp2e

def factor_pint_as_pefect_power_(n, /, *, verbose):
    'n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}'
    check_type_is(int, n)
    if not n > 1:raise ValueError(n)
    n0 = n
    L = n.bit_length()
    e = 1
    assert 1 < n < (1<<L)
    # [1 < n < (1<<L)]
    for p in prime_gen:
        # [1 < n < (1<<L)]
        if p >= L:
            # [2**p >= 2**L > n]
            break
        # [2**p < 2**L]
        while 1:
            # [1 < n < (1<<L)]
            may_kth_root = detect_pefect_kth_root_(p, n, verbose=verbose)
            if may_kth_root is None:
                break
            kth_root = may_kth_root
            assert 1 < kth_root < n
            e *= p
            n = kth_root
            L = n.bit_length()
            assert 1 < n < (1<<L)
            # [1 < n < (1<<L)]
    base = n
    exp = e
    n = n0
    assert n == base**exp
    return (base, exp)

def detect_pefect_kth_root_(k, n, /, *, verbose):
    'k/int{>=1} -> n/int{>=2} -> may base/int{>=2}{n==base**k}'
    check_type_is(int, n)
    if not n > 1:raise ValueError(n)
    check_type_is(int, k)
    if not k > 0:raise ValueError(n)
    if k == 1:
        _kth_root = n
    elif k == 2:
        # now: math.isqrt
        with _timer(prefix=f'floor_sqrt({n})', _show_hint_on_enter_=True, _to_show_=verbose):
            sqrt_ = floor_sqrt(n)
        _kth_root = sqrt_
    else:
        #if 1:
        with _timer(prefix=f'floor_kth_root_({k}, {n})', _show_hint_on_enter_=True, _to_show_=verbose):
            _kth_root = floor_kth_root_(k, n)
    if _kth_root**k == n:
        return _kth_root
    return None
def _quadratic_sieve_(odd_composite, /, *, verbose, grow_size_from_null_instead_optimum_size, time_6):
    'odd_composite -> coprimes/[int{>=2}]{len>=2, pairwise coprime}'
    if not odd_composite > 0:raise ValueError(odd_composite)
    # [lnlnN exists] <==> [lnN > 0] <==> [N >= 3]
    if not odd_composite >= 3:raise ValueError(odd_composite)
    if not odd_composite&1 == 1:raise ValueError(odd_composite)
    if not odd_composite >= 9:raise ValueError(odd_composite)




    check_type_is(int, odd_composite)
    if not odd_composite >= 3:raise ValueError(odd_composite)
    if not False is _is_prime__tribool4factor_pint_(False, odd_composite):raise ValueError(odd_composite)
    lazy_prime_seq = prime_gen() #turnon weakref
    _5i_ = ring_ex_ops__BinaryField.mk_ring_element5int
    for (B, M, x0, x_end, max_offseted_x4neg_Qx, i2neg1prime_base, j2offseted_x, j2neg1p2e4Qx, found_prime_factors) in _prepare4QS_(odd_composite, verbose=verbose, grow_size_from_null_instead_optimum_size=grow_size_from_null_instead_optimum_size, time_6=time_6):
        if verbose:
            print_err(f'_quadratic_sieve_: B={B}, M={M}')

        if 0:
            # remove if p occur only once and its exp is odd
            #   recursive remove???
            r'''[[[
            from collections import Counter
            neg1p2count = Counter()
            for neg1p2e4Qx in j2neg1p2e4Qx:
                neg1p2count.update(iter(neg1p2e4Qx))
            i2count = []
            for neg1p in i2neg1prime_base:
                ...
            #]]]'''#'''
        def ij2v(i, j, /):
            neg1p = i2neg1prime_base[i]
            neg1p2e4Qx = j2neg1p2e4Qx[j]
            return _5i_(neg1p2e4Qx.get(neg1p, 0))

        num_rows = len(i2neg1prime_base)
        num_cols = len(j2neg1p2e4Qx)
            # neg1p per row
            # Qx per column
        with _timer(prefix=f'mk mx<{num_rows},{num_cols}>', _show_hint_on_enter_=True, _to_show_=verbose):
            mx = linear_solver.mk_matrix__ij2v(num_rows, num_cols, ij2v)
            zero_column = linear_solver.mk_matrix__default(num_rows, 1, _5i_(0))


        with _timer(prefix='solve_matrix', _show_hint_on_enter_=True, _to_show_=verbose):
            representative_solutions = linear_solver.solve_equations__matrix__to_representative_solutions(ring_ex_ops__BinaryField, mx, zero_column, validate=True)

        with _timer(prefix='find factors from solutions', _show_hint_on_enter_=True, _to_show_=verbose):
            factors = [*found_prime_factors]
            for column in representative_solutions:
                assert len(column) == len(j2neg1p2e4Qx)
                [row] = linear_solver.transpose__matrix(column)
                assert len(row) == len(j2neg1p2e4Qx)
                acc__x = []
                acc__neg1p2e = {}
                for bit, offseted_x, neg1p2e4Qx in zip(row, j2offseted_x, j2neg1p2e4Qx):
                    if bit:
                        x = x0 + offseted_x
                        acc__x.append(x)
                        for neg1p,e in neg1p2e4Qx.items():
                            acc__neg1p2e.setdefault(neg1p, 0)
                            acc__neg1p2e[neg1p] += e
                #end-for bit, offseted_x, neg1p2e4Qx in zip(row, j2offseted_x, j2neg1p2e4Qx):
                assert all(e&1==0 for e in acc__neg1p2e.values()), (acc__neg1p2e)
                    # {11: 10, 41: 4, 59: 4, 71: 4, 127: 8, -1: 10, 2: 62, 3: 55, 5: 26, 7: 20, 131: 4, 43: 8, 47: 8, 179: 4, 23: 4, 37: 8, 107: 2, 151: 4, 211: 4, 89: 4, 227: 2, 229: 4, 257: 2, 293: 2, 349: 4, 223: 2, 241: 2, 359: 2, 379: 2, 401: 2, 31: 6, 409: 2, 139: 2, 421: 2, 449: 2, 461: 2, 479: 2, 487: 2, 509: 2}
                    # since forgot to put 2,3 in prime_bases
                _sqrt_II__acc__neg1p2e = II_mod(odd_composite, (pow(neg1p, (e//2), odd_composite) for neg1p,e in acc__neg1p2e.items()))
                _II__acc__x = II_mod(odd_composite, acc__x)
                assert (_II__acc__x**2 -_sqrt_II__acc__neg1p2e**2)%odd_composite == 0
                ft = gcd(odd_composite, _II__acc__x +_sqrt_II__acc__neg1p2e)
                if 1 < ft < odd_composite:
                    factors.append(ft)
                ft = gcd(odd_composite, _II__acc__x -_sqrt_II__acc__neg1p2e)
                if 1 < ft < odd_composite:
                    factors.append(ft)
            #end-for column in representative_solutions:
        #end-with _timer(prefix='find factors from solutions', _show_hint_on_enter_=True, _to_show_=verbose):
        if factors:
            r'''[[[
            if time_6:
                for ft in factors:
                    _p2e_, ft = semi_factor_pint_via_trial_division((2,3), ft)
            #]]]'''#'''
            break
    #end-for (B, M, x0, x_end, max_offseted_x4neg_Qx, i2neg1prime_base, j2offseted_x, j2neg1p2e4Qx) in _prepare4QS_(odd_composite, verbose=verbose):
    factors = {*factors}
    assert len(factors) >= 1
    coprimes = _coprimes5factors_(odd_composite, factors)
    assert len(coprimes) >= 2
    return coprimes
def _coprimes5factors_(n, factors, /):
    coprimes = merge_coprimess_into_smaller_coprimes([[ft] for ft in factors] + [[n]])
    assert all(1 < ft < n for ft in coprimes)
    assert all(n%ft == 0 for ft in coprimes)
    return coprimes
###def __():
###  def _quadratic_sieve_(odd_composite, /, *, verbose):
###    'odd_composite -> coprimes/[int{>=2}]{len>=2, pairwise coprime}'
###    check_type_is(int, odd_composite)
###    if not odd_composite >= 3:raise ValueError(odd_composite)
###    if not False is _is_prime__tribool4factor_pint_(False, odd_composite):raise ValueError(odd_composite)
###    lazy_prime_seq = prime_gen() #turnon weakref
###    floor_sqrt__odd_composite = floor_sqrt(odd_composite)
###    L = calc_len_prime_basis4II_prime_basis_gtN_(odd_composite)
###    while 1:
###        prime_basis = prime_gen[:L]
###        L <<= 1
###
###        M = len(prime_basis)
###        for _ in range(3):
###            factors = _try_quadratic_sieve_(M, prime_basis, floor_sqrt__odd_composite, odd_composite, verbose=verbose)
###            if factors:
###                break
###            M <<= 1
###        else:
###            continue
###        break
###    return _coprimes5factors_(odd_composite, factors)
###
###  def _try_quadratic_sieve_(M, prime_basis, floor_sqrt__odd_composite, odd_composite, /, *, verbose):
###    factors = []
###    offset = floor_sqrt__odd_composite+1
###    yy = (offset-M)**2 -odd_composite
###    i_yy_p2e__ls = []
###    for i in range(offset-M, offset+M):
###        #yy = i**2 -odd_composite
###        yy
###        (p2e, unfactored_part) = semi_factor_pint_via_trial_division(prime_basis, yy)
###        if unfactored_part == 1:
###            i_yy_p2e__ls.append((i, yy, p2e))
###        ######################
###        #next round:
###        # (i+1)**2 - i**2 = 2*i+1
###        yy += (i<<1)|1
###    _5i_ = ring_ex_ops__BinaryField.mk_ring_element5int
###    mx = [[_5i_(p2e.get(p,0)) for p in prime_basis] for (i, yy, p2e) in i_yy_p2e__ls]
###        # :: [[bit]]
###    mxT = linear_solver.transpose__matrix(mx)
###    zero_column = linear_solver.mk_matrix__default(len(mxT), 1, _5i_(0))
###
###    representative_solutions = linear_solver.solve_equations__matrix__to_representative_solutions(ring_ex_ops__BinaryField, mxT, zero_column, validate=True)
###    for column in representative_solutions:
###        [row] = linear_solver.transpose__matrix(column)
###        assert len(row) == len(i_yy_p2e__ls)
###        acc__i = 1
###        acc__p2e = {p:0 for p in prime_basis}
###        for bit, (i, yy, p2e) in zip(row, i_yy_p2e__ls):
###            if bit:
###                acc__i *= i
###                acc__i %= odd_composite
###                for p,e in p2e.items():
###                    acc__p2e[p] += e
###        assert all(e&1==0 for e in acc__p2e.values())
###        acc_j = II_mod(odd_composite, (pow(p, (e//2), odd_composite) for p,e in acc__p2e.items()))
###        assert (acc__i**2 -acc_j**2)%odd_composite == 0
###        ft = gcd(odd_composite, acc__i +acc_j)
###        if 1 < ft < odd_composite:
###            factors.append(ft)
###    factors = {*factors}
###    return factors
factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_
factor_pint_as_pefect_power_
detect_pefect_kth_root_
_quadratic_sieve_





__all__


from seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ import factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_, factor_pint_as_pefect_power_, detect_pefect_kth_root_

from seed.math.factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_ import *
