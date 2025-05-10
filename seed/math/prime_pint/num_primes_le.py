#__all__:goto
#py_adhoc_call:goto
#素数数量牜小于二幂:goto
#素数数量牜小于十幂:goto
r'''[[[
e ../../python3_src/seed/math/prime_pint/num_primes_le.py

seed.math.prime_pint.num_primes_le
py -m nn_ns.app.debug_cmd   seed.math.prime_pint.num_primes_le -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_pint.num_primes_le:__doc__ -ht # -ff -df

[[[[[
=====


# [PRIMES_S1[0] == N/A]
# [PRIMES_S1[1] == 2]
# [PRIMES_S1[2] == 3]
[[
view ../lots/NOTE/math-book/prime/The_new_book_of_prime_number_records-note.txt
===
D. The Exact Value of PI(x) and Comparison with x/(log x), Li(x), and Rm(x)
  page235[260/567]
  [m::int{>=0}]:
    [IIp_(m) =[def]= II[PRIMES_S1[k] | [k:<-[1..=m]]]]
    [phi_IIp_(m) =[def]= num_coprimes4IIp_le(IIp_(m);m)]
    [phi_IIp_(m) == phi(IIp_(m)) == II[(PRIMES_S1[k]-1) | [k:<-[1..=m]]]]
  [x::real][m::int{>=0}]:
    [num_coprimes4IIp_le(x;m) =[def]= len{n | [n:<-[1..]][n<=x][gcd(n,IIp_(m))==1]}]
    [num_coprimes4IIp_le(x;m) == len{n | [n:<-[1..]][n<=x][@[k:<-[1..=m]] -> [n%PRIMES_S1[k] =!= 0]]}]

  [@[x::real{>=0}] -> [m:=num_primes_le(x**/3)] -> [m2:=num_primes_le(x**/2)] -> [s:=m2-m] -> [num_primes_le(x) == num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -[x>=1] -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]]]
  <<==:
  [@[x::real{>=1}] -> [m:=num_primes_le(x**/3)] -> [m2:=num_primes_le(x**/2)] -> [s:=m2-m] -> [num_primes_le(x) == num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -1 -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]]]
    # the_Meissel_formula_1871
    #前提:数据预备:primes_le(x**/2) #用于 (x/PRIMES_S1[j])#简单
    #前提:数据预备:num_primes_le(y) where some y < x**(2/3) #用于 m,m2,num_primes_le(x/PRIMES_S1[j]) #麻烦，很多，还各自递归，不知多少... #有没有线性递归版？即递归之后使用的都是相同数据或高密度复用？
    #耗时递归计算:num_coprimes4IIp_le(x;m)
    #
    #Even though the calculation of num_coprimes4IIp_le(x;m) is long, when m is large, it offers no major difficulty.

  [num_primes_le(10**18) == 24739954287740860]
  [num_primes_le(4*10**16) == 1075292778793150 or 1075292778753150]
    #出现两处:结果不同:...93150 vs ...53150
  #如何递归计算:num_coprimes4IIp_le(x;m)
  [@[x::real] -> @[m::int{>=1}] -> [num_coprimes4IIp_le(x;m) == num_coprimes4IIp_le(x;m-1) -num_coprimes4IIp_le(floor(x/PRIMES_S1[m]);m-1)]]
    #recurrence_relation
  [@[n::int{>=0}] -> @[m::int{>=0}] -> [(q,r):=n/%IIp_(m)] -> [num_coprimes4IIp_le(n;m) == q*phi_IIp_(m) +num_coprimes4IIp_le(r;m)]]
    #division_property
  [@[m::int{>=1}] -> @[r::int{>=0}] -> [IIp_(m)///2 < r < IIp_(m)] -> [num_coprimes4IIp_le(r;m) == phi_IIp_(m) -num_coprimes4IIp_le(IIp_(m)-r-1;m)]]
    #symmetry_property
  我:
    [@[x::real] -> @[m::int{>=0}] -> [x < PRIMES_S1[m+1]**2] -> [num_coprimes4IIp_le(x;m) == [x>=1]+max(0,(num_primes_le(x) -m))]]

    [@[x::real] -> [num_coprimes4IIp_le(x;0) == max(0,floor(x))]]
    [@[x::real{>=1}] -> [m2:=num_primes_le(x**(1/2))] -> [num_primes_le(x) == -1+m2+num_coprimes4IIp_le(x;m2)]]
      # !! Eratosthenes sieve
      vs:
      这里是the_Meissel_formula_1871的起点<<==见下面证明
      the_Meissel_formula_1871相当于做了一点包装，但也允许使用更语义的缓存数据(即更小规模的num_primes_le)
  vs:
    [[N>=1] -> [num_primes_le(N) == num_primes_le(floor_sqrt(N)) -1+sum[mu(d)*(N//d) | [[d:<-all_divisors_of(II[p | [[p::prime][p**2<=N]]])][d<=N]]]]]
      # !! Eratosthenes sieve
      vs:
      * 这里mu版:筛选用素数基的各素数独立增删
        #小规模时2**e；越界后将近C(?n?;?k?)
      * 而the_Meissel_formula_1871改进了一下，素数逐个加入素数基，即 新增单素数 与 已过滤旧素数基 之间的 交合(一叉多<<==因为 多叉多 即 两个互斥素数基的糅合 很麻烦，没有显而易见的简单快速方法实现)。

  Meissel determined, in 1885, the number PI(10**9) (however he found a value which is low by 56).
    A simple proof of Meissel's formula was given by Brauer in 1946.
    In 1959, Lehmer simplified and extended Meissel's method.
    In 1985, Lagarias, Miller, and Odlyzko have further refined the method by incorporating new sieving techniques.

  [[
  证明:the_Meissel_formula_1871
  * [x < 1]:
    [m == 0]
    [m2 == 0]
    [s == 0]
    [num_primes_le(x) == 0]
    [num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -1 -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]
    == 0 +0 +0 -1 -0
    == -1
    ]
    [num_primes_le(x) =!= num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -1 -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]]
    只能成立于[x>=1]
  * [x >= 1][m+1>m2]:
    !! [m:=num_primes_le(x**/3)]
    !! [m2:=num_primes_le(x**/2)]
    [m2 >= m >= 0]
    !! [m+1>m2]
    [m >= m2]
    [m == m2]
    !! [s:=m2-m]
    [s == 0]

    [num_primes_le(x)
    !! [@[x::real{>=1}] -> [m2:=num_primes_le(x**(1/2))] -> [num_primes_le(x) == -1+m2+num_coprimes4IIp_le(x;m2)]]
    == -1+m2+num_coprimes4IIp_le(x;m2)
    !! [m == m2]
    == -1+m+num_coprimes4IIp_le(x;m2)
    ]
    [num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -1 -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]
    !! [m+1>m2]
    == num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -1
    !! [s==0]
    == num_coprimes4IIp_le(x;m) +m -1
    == -1+m+num_coprimes4IIp_le(x;m2)

    == num_primes_le(x)
    ]
  * [x >= 1][m+1<=m2]:
    [num_primes_le(x)
    !! [@[x::real{>=1}] -> [m2:=num_primes_le(x**(1/2))] -> [num_primes_le(x) == -1+m2+num_coprimes4IIp_le(x;m2)]]
    == -1+m2+num_coprimes4IIp_le(x;m2)
    !! [@[x::real] -> @[m::int{>=1}] -> [num_coprimes4IIp_le(x;m) == num_coprimes4IIp_le(x;m-1) -num_coprimes4IIp_le(floor(x/PRIMES_S1[m]);m-1)]]
    #应用s次:
    !! [0<=m<=m2]
    !! [s==m2-m]
    => [m2-s>=0][s>=0]
    == -1+m2+num_coprimes4IIp_le(x;m2-s) -sum[num_coprimes4IIp_le(floor(x/PRIMES_S1[j]);j-1) | [j:<-[m2-s+1..=m2]]]
    !! [s==m2-m]
    == -1+m2+num_coprimes4IIp_le(x;m) -sum[num_coprimes4IIp_le((x/PRIMES_S1[j]);j-1) | [j:<-[m+1..=m2]]]
    !! [m:=num_primes_le(x**/3)]
    => [x**/3 < PRIMES_S1[m+1]]
    !! [m2:=num_primes_le(x**/2)]
    !! [m+1 <= j <= m2]
    => [x**/3 < PRIMES_S1[m+1] <= PRIMES_S1[j] <= PRIMES_S1[m2] < x**/2]
    => [x**/3 < PRIMES_S1[j] < x**/2]
    => [PRIMES_S1[m2] < x**/2 < x/PRIMES_S1[j] < x**(2/3) < PRIMES_S1[m+1]**2]
    => [PRIMES_S1[j] <= PRIMES_S1[m2] < x/PRIMES_S1[j] < PRIMES_S1[m+1]**2 <= PRIMES_S1[(j-1)+1]**2]
    !! [@[x::real] -> @[m::int{>=0}] -> [x < PRIMES_S1[m+1]**2] -> [num_coprimes4IIp_le(x;m) == [x>=1]+max(0,(num_primes_le(x) -m))]]
    # [m' := (j-1)]
    # [x' := (x/PRIMES_S1[j])]
    == -1+m2+num_coprimes4IIp_le(x;m)
       -sum[[(x/PRIMES_S1[j])>=1]+max(0,(num_primes_le((x/PRIMES_S1[j])) -(j-1))) | [j:<-[m+1..=m2]]]
    !! [x>=1]
    !! [m>=1]
    !! [m+1<=m2]
    => [m2 >= 1]
    => [1 < 2 <= PRIMES_S1[m2] < x**/2 < x/PRIMES_S1[j]]
    => [x/PRIMES_S1[j] >= 1]
    !! [PRIMES_S1[j] <= PRIMES_S1[m2] < x/PRIMES_S1[j]]
    => [num_primes_le((x/PRIMES_S1[j])) >= m2 >= j > (j-1)]
    => [num_primes_le((x/PRIMES_S1[j])) -(j-1) > 0]
    == -1+m2+num_coprimes4IIp_le(x;m)
       -sum[1+(num_primes_le((x/PRIMES_S1[j])) -(j-1)) | [j:<-[m+1..=m2]]]
    == -1+m2+num_coprimes4IIp_le(x;m)
       -sum[num_primes_le((x/PRIMES_S1[j])) | [j:<-[m+1..=m2]]]
       -sum[1 -(j-1) | [j:<-[m+1..=m2]]]
    == -1+m2+num_coprimes4IIp_le(x;m)
       -sum[num_primes_le((x/PRIMES_S1[j])) | [j:<-[m+1..=m2]]]
       -2*s
       +sum[j | [j:<-[m+1..=m2]]]
    == -1+m2+num_coprimes4IIp_le(x;m)
       -sum[num_primes_le((x/PRIMES_S1[j])) | [j:<-[m+1..=m2]]]
       -2*s
       +s*(m2+m+1)///2
    !! [m2==m+s]
    == -1+(m+s)+num_coprimes4IIp_le(x;m)
       -sum[num_primes_le((x/PRIMES_S1[j])) | [j:<-[m+1..=m2]]]
       -2*s
       +s*((m+s)+m+1)///2
    == 
    == -1+num_coprimes4IIp_le(x;m)
       -sum[num_primes_le((x/PRIMES_S1[j])) | [j:<-[m+1..=m2]]]
       +m*(s+1) +s*(s-1)///2

    == num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -1 -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]
    ]
  !DONE
  ]]


]]
===
[[

  #Li(x) --> Li(z)
  [x::real]:
    [sgn_(x) =[def]= ([x>0]*(+1) +[x<0]*(-1) +[x==0]*(0))]
  [x::real]:
    # Li(x):the function logarithmic integral of x # ver1
    [Li(x) =[def]= SS{1/ln(t) | [t :<~ 2 ~> x]}]
  [z::complex][(u,v) :=> [e**(u+1j*v)==z]]:
    # Li(z):the function logarithmic integral of z # ver2
    [Li(z) =[def]= SS{e**t/t | [t :<~ -oo+ ~> u+1j*v]} +1j*pi*sgn_(v)]

  #Rm(x) --> Rm(z)
  [x::real{>0}]:
    #the_Riemann_function-ver1-单用(非精确估算num_primes_le)
    [Rm(x) =[def]= sum[mu(m)/m * Li(x**/m) | [m:<-[1..]]]]
  [z::complex]:
    #the_Riemann_function-ver2-复用(精确估算num_primes_le)
    # 需要拓展Li的定义
    [Rm(z) =[def]= sum[mu(m)/m * Li(z**/m) | [m:<-[1..]]]]


  [num_primes_le(x) == (Rm(x) - sum[Rm(x**z0) | [z0:<-[zeros of zeta(z) with its own multiplicity]]])]
    #复用(精确估算num_primes_le)
  [num_primes_le(x) ~= Rm(x)]
    #单用(非精确估算num_primes_le)
  [num_primes_le(x) == (Rm(x) - sum[Rm(x**z0) | [z0:<-[zeros of zeta(z) with its own multiplicity]]]) /~/ Rm(x) /~/ Li(x) /~/ (x/ln(x))]
    #Rm最佳估计, Li次佳估计, (x/ln(x))一般估计
    #但是:{Rm,Li}的误差有正有负，而(x/ln(x))尾部总是小于num_primes_le(x)
  [[x>=11] -> [num_primes_le(x) >= (x/ln(x))]]
  [lim{[Li(x) > num_primes_le(x)] | x-->+oo} == diverge]
    #the difference (Li(x) -PI(x)) changes sign infinitely often
  [?[n0:<-[6.62e370..=6.69e370-1e180]] -> @[n:<-[n0..<n0+1e180]] -> [num_primes_le(n) >= Li(n)]]
    # [between 6.62*10**370 and 6.69*10**370 there are more than 10**180 successive integers x for which PI(x) > Li(x)]



  [Rm(x) == 1+sum[(ln(x)**n /n! /n /zeta(n+1))| [n:<-[1..]]]]
    #求值冫黎曼函数
    # 快速收敛序列
    zeta(n+1) 独立计算缓存
    注意:偶数:[[k>=1] -> [zeta(2*k) == sum[1/n**(2*k) | [n:<-[1..]]] == ((-1)**(k+1)*(2*pi)**(2*k)*Bernoulli_numbers[2*k]/2/(2*k)!)]]
    奇数怎么办？难道用:
      [@[z::complex] -> [z.real>1] -> [k:<-[1..]] -> [zeta(z) == (1/(z-1) +1/2 +sum[Bernoulli_numbers[r]/r! * II[(z+i) | [i:<-[0..<(r-1)]]] | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)/k! *II[(z+i) | [i:<-[0..<k]]] *SS{Bernoulli_polynomials(k;t-floor(t))*(t**-(z+k)) | [t :<~ 1~>+oo]})]]


]]
===
[[
  @page214[239/567]
  [[x0 :: real][f,h :: real{>x0} -> real{>0}]]:
    [[f(x) /~/ h(x)] =[def]= is_asymptotically_equal_as_input_tends_to_infinity_(f,h) =[def]= [lim{f(x)/h(x) | x-->+oo} == 1]]
      # 对称性:
    [[f(x) /~/ h(x)] == [h(x) /~/ f(x)]]

    [have_the_same_order_of_magnitude_(f,h) =[def]= [?[C4inferior,C4superior :: real{>0}] -> ?[x1 :: real{>x0}] -> @[x :: real{>x1}] -> [C4inferior <= f(x)/h(x) <= C4superior]]]
      # 注意:C4inferior大于0
      # 对称性:
    [have_the_same_order_of_magnitude_(f,h) == have_the_same_order_of_magnitude_(h,f)]

    [[f(x) /~/ h(x)] -> [have_the_same_order_of_magnitude_(f,h)]]

  [[x0 :: real][f,g :: real -> real][h :: real{>x0} -> real{>0}]]:
    # big_O_notation:
    [[f(x) == g(x) +O(h(x))] =[def]= [?[C4superior :: real{>0}] -> ?[x1 :: real{>x0}] -> @[x :: real{>x1}] -> [abs(f(x)-g(x))/h(x) <= C4superior]]]
      # 注意:必须有abs()保证非负
      # 注意:不同于上面have_the_same_order_of_magnitude_，此处C4inferior可能为0，故没有出现
    [[f(x) == g(x) +O(h(x))] <-> [have_the_same_order_of_magnitude_((\x->h(x)+abs(f(x)-g(x))),h)]]
      # 注意:必须有abs()保证非负
      # 注意:必须加上h(x)保证C4inferior大于0

    # ???small_O_notation:
    [[f(x) == g(x) +o(h(x))] =[def]= the_error_is_negligible_in_comparison_to_(h; f,g) =[def]= [lim{(f(x)-g(x))/h(x) | x-->+oo} == 0]]
    [[f(x) == g(x) +o(h(x))] <-> [@[C4superior :: real{>0}] -> ?[x1 :: real{>x0}] -> @[x :: real{>x1}] -> [abs(f(x)-g(x))/h(x) <= C4superior]]]

  [?[x0 :: real] -> @[f,h :: real{>x0} -> real{>0}] -> [[f(x) /~/ h(x)] <-> [lim{f(x)/h(x) | x-->+oo} == 1]]]
  [?[x0 :: real] -> @[f,h :: real{>x0} -> real{>0}] -> [[have_the_same_order_of_magnitude_(f,h)] <-> [?[C4inferior,C4superior :: real{>0}] -> ?[x1 :: real{>x0}] -> @[x :: real{>x1}] -> [C4inferior <= f(x)/h(x) <= C4superior]]]]
  [?[x0 :: real] -> @[f,g :: real -> real] -> @[h :: real{>x0} -> real{>0}] -> [[f(x) == g(x) +O(h(x))] <-> [have_the_same_order_of_magnitude_((\x->h(x)+abs(f(x)-g(x))),h)]]]
    # big_O_notation
  [?[x0 :: real] -> @[f,g :: real -> real] -> @[h :: real{>x0} -> real{>0}] -> [[f(x) == g(x) +o(h(x))] <-> [lim{(f(x)-g(x))/h(x) | x-->+oo} == 0]]]
    # ???small_O_notation

  I. The Growth of PI(x)
  H. Some Properties of PI(x)
  @page247[272/567]
  [x::real]:
    [PI(x) =[def]= num_primes_le(x)]
  Bertrand_postulate_1845:
  [[n>=2] -> [num_primes_le(2*n) -num_primes_le(n) >= 1]]
  <==>:
  [[n>=1] -> [num_primes_le(2*n) -num_primes_le(n) >= 1]]
  <==>:
  [[n>=1] -> [PRIMES_S1(n+1) < 2*PRIMES_S1(n)]]
  <<==:
  [[n>=5] -> [1 < (1/3)*n/ln(n) < (num_primes_le(2*n) -num_primes_le(n)) < (7/5)*n/ln(n)]]

  [@[x,y :: real] -> [x>=6] -> [x>=y>=2] -> [num_primes_le(x*y) > num_primes_le(x)+num_primes_le(y)]]

  [@[x,y :: real] -> [???:[x>=???][y>=???][y>1]...] -> [num_primes_le(x+y) <= num_primes_le(x)+2*y/ln(y)]]
    # [2*y/ln(y) >= 2*e/ln(e) == 2*e == 5.43656365691809]
    #   where [e:=2.718281828459045]
    # [ln(y4)==4] <-> [y4==e**4==54.59815003314423]
    # [ln(y6)==6] <-> [y6==e**6==403.428793492735]
    # [ln(y8)==8] <-> [y8==e**8==2980.957987041727]
    =>:
    [@[x,y :: real] -> [???:[x>=???]...] -> [y>=54.59815003314423] -> [num_primes_le(x+y4) <= num_primes_le(x)+y/2]]
    [@[x,y :: real] -> [???:[x>=???]...] -> [y>=403.428793492735] -> [num_primes_le(x+y4) <= num_primes_le(x)+y/3]]
    [@[x,y :: real] -> [???:[x>=???]...] -> [y>=2980.957987041727] -> [num_primes_le(x+y4) <= num_primes_le(x)+y/4]]
  ==>>:
  [@[x,y :: real] -> [???:[x>=???][y>=2]...] -> [num_primes_le(x+y) <= num_primes_le(x)+2*num_primes_le(y)]]

  [@[x :: real] -> [x>=11] -> [num_primes_le(2*x) < 2*num_primes_le(x)]]

  [[x :: real][x>1]]:
    [main_ratio4num_primesLE =[def]= num_primes_le(x)/(x*ln(x))]
  [@[x :: real] -> [x>1] -> [main_ratio4num_primesLE(x) <= main_ratio4num_primesLE(113) ~=1.25...]]
  [@[x :: real] -> [x>1] -> [0.95695 < main_ratio4num_primesLE(x) < 1.04423]]

  the_prime_number_theorem
  the_fundamental_prime_number_theorem
  [num_primes_le(x) /~/ x/ln(x)]
    =>:
    [num_primes_le(p) /~/ p/ln(p)]
    [n == num_primes_le(PRIMES_S1[n]) /~/ PRIMES_S1[n]/ln(PRIMES_S1[n])]
    [n /~/ PRIMES_S1[n]/ln(PRIMES_S1[n])]
  [num_primes_le(x) /~/ Li(x) /~/ x/ln(x)]
    #Li更佳:
    #??? [(abs(Li(x) -num_primes_le(x))) = o(abs(x/ln(x) -num_primes_le(x)))]
  [[N>=1] -> [num_primes_le(N) == num_primes_le(floor_sqrt(N)) -1+sum[mu(d)*(N//d) | [[d:<-all_divisors_of(II[p | [[p::prime][p**2<=N]]])][d<=N]]]]]
    # !! Eratosthenes sieve
    #mu=the_Mobius_function
    #   含平方因子则为零
    #   不含平方因子且偶数个素因子则为一
    #   不含平方因子且奇数个素因子则为负一

  [k >= 0]:
    [def:Bernoulli_numbers[k] :=> [sum[C(k+1;k+1-j)*Bernoulli_numbers[j] | [j:<-[0..=k]]] == [k==0]]]
      # 1, -1/2, 1/6, 0, ...
    [Bernoulli_numbers[2*k+1] == [k==0]*(-1/2)]
  [k >= 0]:
    [Bernoulli_polynomials[k](x) =[def]= sum[C(k;i)*Bernoulli[k-i]*x**i | [i:<-[0..=k]]]]
  [[k>=1] -> [Bernoulli_numbers[2*k+1] == 0]]
  [x/(e**x-1) == sum[Bernoulli_numbers[k]*x**k/k! | [k:<-[0..]]]]
    #coefficients in the Taylor expansion
  [n! /~/ sqrt(2*pi)*n**(n+1/2)/e**n]
  [Bernoulli_numbers[2*n] /~/ 4*sqrt(pi*n)*(n/pi/e)**(2*n)]
    #Stirling_formula

  [[k>=1] -> [n>=0] -> [sum[j**k | [j:<-[1..=n]]] == (1/(k+1) * sum[(-1)**(k+1-i)*Bernoulli_numbers[k+1-i]*C(k+1;k+1-i)*n**i | [i:<-[1..=1+k]]]) == n**k/2 +(1/(k+1) * sum[Bernoulli_numbers[2*d]*C(k+1;2*d)*n**(k+1-2*d) | [d:<-[0..=k//2]]])]]
    # 公式纟求和纟离散幂方:here
    <==> [[k>=1] -> [n>=0] -> [sum[j**k | [j:<-[1..=n]]] == (1/(k+1) * (-1)**(k+1) * (Bernoulli_polynomials[k+1](-n) -Bernoulli_numbers[k+1]))]]

  [[k>=1] -> [zeta(2*k) == sum[1/n**(2*k) | [n:<-[1..]]] == ((-1)**(k+1)*(2*pi)**(2*k)*Bernoulli_numbers[2*k]/2/(2*k)!)]]
    [zeta(2) == sum[1/n**2 | [n:<-[1..]]] == pi**2/6]
    [zeta(4) == sum[1/n**4 | [n:<-[1..]]] == pi**4/90]

  [@[f :: continuous_function] -> @[k:<-[1..]] -> [is_continuously_differentiable_(k;f)] -> [a,b::int] -> [a<b] -> [sum[f(n) | [n:<-[a+1..=b]]] == (SS{f(t) | [t :<~ a~>b]} +sum[(-1)**r*Bernoulli_numbers[r]/r! * (D(r-1,f;b) -D(r-1,f;a)) | [r:<-[1..=k]]] +(-1)**(k-1)/k! * SS{Bernoulli_polynomials(k;t-floor(t))*D(k,f;t) | [t :<~ a~>b]})]]
    #Euler_MacLaurin_summation_formula:here
    # 公式纟求和转积分:here
    #     推导过程应该是依赖 f的泰勒展开式+公式纟求和纟离散幂方
    #######
    #######
    # a far-reaching generalization of Abel's summation formula, namely, the well-known Euler-MacLaurin summation formulas:
    # If f(x) is a continuous function, continuously differentiable as many times as required, if a < b are integers, then
    #######
    #######
  [+sum[(-1)**r*Bernoulli_numbers[r]/r! * (D(r-1,f;b) -D(r-1,f;a)) | [r:<-[1..=k]]]
  !! [[k>=1] -> [Bernoulli_numbers[2*k+1] == 0]]
  == +(-1)**1*Bernoulli_numbers[1]/1! * (D(1-1,f;b) -D(1-1,f;a))
     +sum[(-1)**(2*h)*Bernoulli_numbers[(2*h)]/(2*h)! * (D((2*h)-1,f;b) -D((2*h)-1,f;a)) | [h:<-[1..=k//2]]]
  == -(-1/2) * (f(b) -f(a))
     +sum[Bernoulli_numbers[(2*h)]/(2*h)! * (D((2*h)-1,f;b) -D((2*h)-1,f;a)) | [h:<-[1..=k//2]]]
  == +(f(b) -f(a))/2
     +sum[Bernoulli_numbers[r]/r! * (D(r-1,f;b) -D(r-1,f;a)) | [r:<-[2..=k]]]
  ]
  [@[f :: continuous_function] -> @[k:<-[1..]] -> [is_continuously_differentiable_(k;f)] -> [a,b::int] -> [a<b] -> [sum[f(n) | [n:<-[a+1..=b]]] == (SS{f(t) | [t :<~ a~>b]} +(f(b) -f(a))/2 +sum[Bernoulli_numbers[r]/r! * (D(r-1,f;b) -D(r-1,f;a)) | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)**(k-1)/k! * SS{Bernoulli_polynomials(k;t-floor(t))*D(k,f;t) | [t :<~ a~>b]})]]
    #Euler_MacLaurin_summation_formula__variant1:here
    # 公式纟求和转积分牜变体一:here


  [[z::complex][z.real>1]]:
    [zeta(z) =[def]= sum[1/n**z | [n:<-[1..]]]]
      #the_zeta_function
      #Euler-real-x
      #Riemann-complex-z
      #zeta==£
  [zeta(1) == sum[1/n | [n:<-[1..]]] == +oo]
  [sum[1/p | [p::prime]] == +oo]
  [@[z::complex] -> [z.real>1] -> [zeta(z) == sum[1/n**z | [n:<-[1..]]] == II[1/(1-1/p**z) | [p::prime]] =!= 0]]
    #Euler_product_formula:here
    #   联系zeta(z)与素数
    [zeta(z)
    == sum[1/n**z | [n:<-[1..]]]
    == II[sum[(1/p**z)**k | [k:<-[1..]]] | [p::prime]]
    == II[1/(1-1/p**z) | [p::prime]]
    # => [abs(zeta(z)) > 1]
    # => [abs(zeta(z)) =!= 0]
    =!= 0
    ]
  ==>>:
  [@[z::complex] -> [z.real>1] -> [zeta(z) =!= 0]]
      # [z.real>1] => [zeta(z) =!= 0]

  [@[z::complex] -> [z.real>1] -> [zeta(z) uniformly convergent]]
  [@[z::complex] -> [z.real>1] -> [zeta(z) continuous and differentiable]]
  [zeta(+oo) == 1]
  [lim{err*zeta(1+err) | err --> 0^+} == 1]

  [[z::complex][z.real>1]]:
    [x::real][x>=1][k:<-[1..]]:
      [SS{t**-z | t :<~ 1~>x} == x**(1-z)/(1-z) -1/(1-z)]
      [SS{t**-z | t :<~ 1~>+oo} == +oo**(1-z)/(1-z) -1/(1-z) == 0-1/(1-z) == -1/(1-z) == 1/(z-1)]
    [SS{t**-z | t :<~ 1~>+oo} == 1/(z-1)]
    [k:<-[1..]]:
      !! Euler_MacLaurin_summation_formula__variant1:公式纟求和转积分牜变体一:goto
      # [@[f :: continuous_function] -> @[k:<-[1..]] -> [is_continuously_differentiable_(k;f)] -> [a,b::int] -> [a<b] -> [sum[f(n) | [n:<-[a+1..=b]]] == (SS{f(t) | [t :<~ a~>b]} +(f(b) -f(a))/2 +sum[Bernoulli_numbers[k]/k! * (D(r-1,f;b) -D(r-1,f;a)) | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)**(k-1)/k! * SS{Bernoulli_polynomials(k;t-floor(t))*D(k,f;t) | [t :<~ a~>b]})]]
      # [f(t) := t**-z]
      # [a := 1]
      # [b := +oo]
      # [D(k,f;t) == (t**(-z-k)*II[(-z-i) | [i:<-[0..<k]]])]
      #
      #
      [zeta(z) - 1
      == sum[n**-z | [n:<-[2..]]]
      # [f(t) := t**-z]
      :> [a:=1]
      :> [b:=+oo]
      == (SS{t**-z | [t :<~ a~>b]} +(b**-z -a**-z)/2 +sum[Bernoulli_numbers[r]/r! * ((b**(-z-(r-1))*II[(-z-i) | [i:<-[0..<(r-1)]]]) -(a**(-z-(r-1))*II[(-z-i) | [i:<-[0..<(r-1)]]])) | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)**(k-1)/k! * SS{Bernoulli_polynomials(k;t-floor(t))*(t**(-z-k)*II[(-z-i) | [i:<-[0..<k]]]) | [t :<~ a~>b]})
      !! [a:=1]
      !! [b:=+oo]
      == (SS{t**-z | [t :<~ 1~>+oo]} +(+oo**-z -1**-z)/2 +sum[Bernoulli_numbers[r]/r! * (0 -(1*II[(-z-i) | [i:<-[0..<(r-1)]]])) | [r:<-[2..=k]]] +(-1)**(k-1)/k! * SS{Bernoulli_polynomials(k;t-floor(t))*(t**(-z-k)*II[(-z-i) | [i:<-[0..<k]]]) | [t :<~ 1~>+oo]})
    !! [SS{t**-z | t :<~ 1~>+oo} == 1/(z-1)]
      == (1/(z-1) +(0-1)/2 +sum[Bernoulli_numbers[r]/r! * (-1*II[(-z-i) | [i:<-[0..<(r-1)]]]) | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)**(k-1)/k! * SS{Bernoulli_polynomials(k;t-floor(t))*(t**(-z-k)*II[(-z-i) | [i:<-[0..<k]]]) | [t :<~ 1~>+oo]})
      # (-z-i) --> (-1)*(z+i)
      == (1/(z-1) -1/2 +sum[Bernoulli_numbers[r]/r! * (-1)*(-1)**(r-1)*II[(z+i) | [i:<-[0..<(r-1)]]] | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)**(k-1)/k! * SS{Bernoulli_polynomials(k;t-floor(t))*(t**(-z-k)*(-1)**k*II[(z+i) | [i:<-[0..<k]]]) | [t :<~ 1~>+oo]})
      !! [optional:[r%2==0]]
      == (1/(z-1) -1/2 +sum[Bernoulli_numbers[r]/r! * II[(z+i) | [i:<-[0..<(r-1)]]] | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)/k! *II[(z+i) | [i:<-[0..<k]]] *SS{Bernoulli_polynomials(k;t-floor(t))*(t**(-z-k)) | [t :<~ 1~>+oo]})
      ]
      [zeta(z) - 1 == (1/(z-1) -1/2 +sum[Bernoulli_numbers[r]/r! * II[(z+i) | [i:<-[0..<(r-1)]]] | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)/k! *II[(z+i) | [i:<-[0..<k]]] *SS{Bernoulli_polynomials(k;t-floor(t))*(t**(-z-k)) | [t :<~ 1~>+oo]})]
      ==>>:
      [zeta(z) == (1/(z-1) +1/2 +sum[Bernoulli_numbers[r]/r! * II[(z+i) | [i:<-[0..<(r-1)]]] | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)/k! *II[(z+i) | [i:<-[0..<k]]] *SS{Bernoulli_polynomials(k;t-floor(t))*(t**-(z+k)) | [t :<~ 1~>+oo]})]
    [[k:<-[1..]] -> [zeta(z) == (1/(z-1) +1/2 +sum[Bernoulli_numbers[r]/r! * II[(z+i) | [i:<-[0..<(r-1)]]] | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)/k! *II[(z+i) | [i:<-[0..<k]]] *SS{Bernoulli_polynomials(k;t-floor(t))*(t**-(z+k)) | [t :<~ 1~>+oo]})]]
      #最后的积分项:在[z.real+k>1]即[z.real>1-k]上收敛；由于[k>=1]，所以此积分项全复平面收敛。
      #zeta(z)只有一个简单极点:即首项(1/(z-1))
      #The integral converges for [Re(z) > 1-k], and since k is an arbitrary positive natural number, this formula provides the analytic continuation of zeta(z) to the whole plane. zeta(z) is everywhere holomorphic, except at z = 1, where it has a simple pole with residue 1, that is, [lim{zeta(z)*(z-1) | z-->1} == 1].
      # @page222[247/567]
  [@[z::complex] -> [z.real>1] -> [k:<-[1..]] -> [zeta(z) == (1/(z-1) +1/2 +sum[Bernoulli_numbers[r]/r! * II[(z+i) | [i:<-[0..<(r-1)]]] | [r:<-[2..=k]][optional:[r%2==0]]] +(-1)/k! *II[(z+i) | [i:<-[0..<k]]] *SS{Bernoulli_polynomials(k;t-floor(t))*(t**-(z+k)) | [t :<~ 1~>+oo]})]]
    #公式:证明zeta(z)全复平面唯一极点简单
    #公式:证明(zeta(z)*(z-1))全复平面连续性




  [[z::complex][z.real>0]]:
    #the_gamma_function-ver1-only_right_half_complex_plane
    [gamma(z) =[def]= SS{e**-t * t**(z-1) |t :<~ 0~>+oo}]
      #eulerian integral
  [[z::complex][z !<- {-n | [n:<-[0..]]}]]:
    #the_gamma_function-ver2-almost_whole_complex_plane
    [gamma(z) =[def]= (z**-1 * e**(-y4Euler*z) * II[e**(z/n)/(1+(z/n)) | [n:<-[1..]]])]
    [y4Euler == Euler_constant =[def]= lim{(sum[1/k| [k:<-[1..=n]]] -ln(n)) | n-->+oo} ~= 0.577215665...]
    [e**y4Euler == Mascheroni_constant =[def]= lim{((II[1/(1-1/PRIMES_S1[k])| [k:<-[1..=n]]]) /ln(n)) | n-->+oo} ~= 0.577215665...]
      #у
  [z::complex]:
    #reciprocal_of_the_gamma_function-whole_complex_plane
    [reciprocal_gamma(z) =[def]= (z * e**(y4Euler*z) * II[(1+(z/n))/e**(z/n) | [n:<-[1..]]])]
  [lim{reciprocal_gamma(z)/z | z-->0} == (e**(y4Euler*0) * II[(1+(0/n))/e**(0/n) | [n:<-[1..]]]) == 1]
  [lim{reciprocal_gamma(z)/z | z-->0} == 1]
  [lim{1/gamma(z)/z | z-->0} == 1]

  # @page223[248/567]
  #gamma(z) is never equal to 0; it is holomorphic everywhere except at the points 0, -1, -2, -3, ..., where it has simple poles.  For every positive integer n, gamma(n) = (n - 1)!, so the gamma function is an extension of the factorial function. The gamma function satisfies many interesting relations, among which are the functional equations:
  [gamma(z)*gamma(1-z) == pi/sin(pi*z)]
  [gamma(z)*gamma(z+1/2) == sqrt(pi)/2**(2*z-1) *gamma(2*z)]
  [gamma(z+1) == z*gamma(z)]

  [gamma(z) =!= 0]
  [[n::uint] -> [gamma(n+1) == n!]]
  [@[z::complex] -> [[1/gamma(z) == 0] <-> [z <- {-n | [n:<-[0..]]}]]]
    #极点
  [lim{1/gamma(z)/z | z-->0} == 1]

  !! [gamma(z)*gamma(z+1/2) == sqrt(pi)/2**(2*z-1) *gamma(2*z)]
  [gamma(z+1/2) == sqrt(pi)/2**(2*z-1) *gamma(2*z) /gamma(z)]
  [gamma(1/2)
  == sqrt(pi)/2**(2*0-1) *lim{gamma(2*z) /gamma(z) | z-->0}
  == sqrt(pi)/2**(2*0-1) *1/2 *lim{(gamma(2*z)*2*z) /(gamma(z)*z) | z-->0}
  !! [lim{1/gamma(z)/z | z-->0} == 1]
  == sqrt(pi)/2**(2*0-1) *1/2 *1/1
  == sqrt(pi)
  ]
  [gamma(1/2) == sqrt(pi)]










  [gamma_zeta(z) =[def]= pi**-(z/2) *gamma(z/2) *zeta(z)]

  [gamma_zeta(z) == gamma_zeta(1-z)]
    # the_functional_equation_for_the_Riemann_zeta_function
    #对称性:对称轴:[z.real==1/2]
  <==>:
  [pi**-(z/2) *gamma(z/2) *zeta(z) == pi**-((1-z)/2) *gamma((1-z)/2) *zeta((1-z))]
  <==>:
  [zeta(z) == pi**(z-1/2) *gamma((1-z)/2) /gamma(z/2) *zeta((1-z))]
  <==>:
  !! [gamma(z)*gamma(1-z) == pi/sin(pi*z)]
  => [gamma((1-z)/2)*gamma(1-(1-z)/2) == pi/sin(pi*(1-z)/2)]
  => [gamma((1-z)/2) == pi/sin(pi*(1-z)/2) /gamma((1+z)/2)]
  [zeta(z) == pi**(z-1/2) *pi/sin(pi*(1-z)/2) /gamma((1+z)/2) /gamma(z/2) *zeta((1-z))]
  <==>:
  !! [gamma(z)*gamma(z+1/2) == sqrt(pi)/2**(2*z-1) *gamma(2*z)]
  => [gamma((z/2))*gamma((z/2)+1/2) == sqrt(pi)/2**(2*(z/2)-1) *gamma(2*(z/2))]
  => [gamma(z/2)*gamma((1+z)/2) == sqrt(pi)/2**(z-1) *gamma(z)]
  [zeta(z) == pi**(z-1/2) *pi/sin(pi*(1-z)/2) /sqrt(pi) *2**(z-1) /gamma(z) *zeta((1-z))]
  <==>:
  [zeta(z) == (2**(z-1) *pi**z /sin(pi/2*(1-z)) /gamma(z) *zeta(1-z))]

  !! [zeta(z) == (2**(z-1) *pi**z /sin(pi/2*(1-z)) /gamma(z) *zeta(1-z))]
  !! [@[z::complex] -> [z.real>1] -> [zeta(z) =!= 0]]
  [@[z::complex] -> [z.real<0] -> [[zeta(z) == 0] -> [1/gamma(z) == 0]]]
  !! [@[z::complex] -> [[1/gamma(z) == 0] <-> [z <- {-n | [n:<-[0..]]}]]]
  [@[z::complex] -> [z.real<0] -> [[zeta(z) == 0] -> [z <- {-n | [n:<-[0..]]}]]]
    但是因为1/sin(pi/2*(1-z))抵消部分1/gamma(z)零点，所以只是『->』而非『<->』

  上面打开方式不对，从头再来:
  !! [zeta(z) == pi**(z-1/2) *gamma((1-z)/2) /gamma(z/2) *zeta((1-z))]
  !! [@[z::complex] -> [z.real>1] -> [zeta(z) =!= 0]]
  !! [gamma(z) =!= 0]
  [@[z::complex] -> [z.real<0] -> [[zeta(z) == 0] <-> [1/gamma(z/2) == 0]]]
  !! [@[z::complex] -> [[1/gamma(z) == 0] <-> [z <- {-n | [n:<-[0..]]}]]]
  [@[z::complex] -> [z.real<0] -> [[zeta(z) == 0] <-> [1/gamma(z/2) == 0] <-> [(z/2) <- {-n | [n:<-[0..]]}] <-> [z <- {-2*n | [n:<-[0..]]}] <-> [z <- {-2*n | [n:<-[1..]]}]]]
    # 注意:前提 => [z=!=0]
  [@[z::complex] -> [z.real<0] -> [[zeta(z) == 0] <-> [z <- {-2*n | [n:<-[1..]]}]]]
    #zeta(z)平凡零点

  !! [zeta(z) == pi**(z-1/2) *gamma((1-z)/2) /gamma(z/2) *zeta((1-z))]
  [zeta(0)
  == pi**(0-1/2) *gamma((1-0)/2) *lim{1/gamma(z/2) *zeta((1-z)) | z-->0}
  == pi**(-1/2) *gamma(1/2) *(-1/2)*lim{1/(gamma(z/2)*z/2) *zeta(1-z)*(-z) | z-->0}
  !! [lim{1/gamma(z)/z | z-->0} == 1]
  !! [lim{err*zeta(1+err) | err --> 0^+} == 1]
  == pi**(-1/2) *gamma(1/2) *(-1/2) *1
  !! [gamma(1/2) == sqrt(pi)]
  == pi**(-1/2) *sqrt(pi) * (-1/2)
  == (-1/2)
  ]
  [zeta(0) == (-1/2)]

  [Riemann_hypothesis:[@[z::complex] -> [0<=z.real<=1] -> [zeta(z) == 0] -> [z.real==1/2]]]
    #黎曼猜想:zeta(z)所有非平凡零点在对称轴[Re(z) = 1/2]上
    # vs:平凡零点:[@[z::complex] -> [z.real<0] -> [[zeta(z) == 0] <-> [z <- {-2*n | [n:<-[1..]]}]]]
  ==>>:
  [[
  Here is the functional equation for the Riemann zeta function:
      [pi**-(z/2) *gamma(z/2) *zeta(z) == pi**-((1-z)/2) *gamma((1-z)/2) *zeta((1-z))]
  For example, it follows from the functional equation that [zeta(0) == -1/2].
  The zeros of the zeta function are:
    (a) Simple zeros at the points -2, -4, -6, ..., which are called the trivial zeros.
    (b) Zeros in the critical strip, consisting of the nonreal complex numbers z with [0 < Re(z) < 1].
  Indeed, if Re(z) > 1, then by the Euler product, [zeta(z) =!= 0]. If Re(z) < 0, then Re(1-z) > 1, the right-hand side in the functional equation is not zero, so the zeros must be exactly at z = -2, -4, -6,..., which are the poles of gamma(z/2).
  The knowledge of the zeros in the critical strip has a profound influence on the understanding of the distribution of primes. A first thing to note is that the zeros in the critical strip are not real and they are symmetric about the real axis and the vertical line [Re(z) = 1/2].
  Riemann conjectured that all nontrivial zeros z0 of zeta(z) are on the critical line [Re(z) = 1/2], that is, [z0 == 1/2 + 1j*y0]. This is the famous Riemann's hypothesis, which has never been proved. It is undoubtedly a very difficult and important problem, and I shall return to it soon and narrate some modern developments.

  ]]


]]
===
[[
/sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu
  II. The nth Prime and Gaps
  page249[274/567]
  [n :<- [1..]]:
    [PRIMES_S1[n] =[def]= PRIMES[n-1]]
      @page3[28/567]
  [PRIMES_S1[1] == PRIMES[0] == 2]

  [[sufficiently large n] => [PRIMES_S1[n] == n*ln(n) + n*(lnln(n)-1) + o(n*lnln(n)/ln(n))]]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-10) < PRIMES_S1[n] < n*ln(n) + n*(lnln(n)+8)]]
    # [[n>=2] -> [-10 < (PRIMES_S1[n]/n -ln(n) -lnln(n)) < 8]]
    # [[n>=2] -> [abs(PRIMES_S1[n]/n -ln(n) -lnln(n) +1) < 9]]
  [[n>=1] -> [PRIMES_S1[n] > n*ln(n)]]
  [[n>=2] -> [n*ln(n) + n*(lnln(n)-1.0072629) <= PRIMES_S1[n]]]
  [[n>=2] -> [PRIMES_S1[n] <= 10**11] -> [n*ln(n) + n*(lnln(n)-1) <= PRIMES_S1[n]]]
  [[n>=7022] -> [PRIMES_S1[n] <= n*ln(n) + n*(lnln(n) -0.9385)]]
  [PRIMES_S1[7022] == PRIMES[7021] == 70919]
  view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
    0 2 1 1
    1 3 2 2
    2 5 2 2
    ... ...
    7021 70919 7 7
    7022 70921 13 13
    7023 70937 3 3
    ... ...
  The above inequalities required strenuous calculations to be established. If one is less ambitious, it is possible to obtain weaker estimates with elementary methods. Thus, for example, I quote an early result of Sierpinski 1964):
  [[n>=1] -> [1/4*n*ln(n) < PRIMES_S1[n] < 36*n*ln(n)]]
    # [[n>=1] -> [1/4 < PRIMES_S1[n]/(n*ln(n)) < 36]]
    # [[n>=1] -> [1/12 < 1/3*PRIMES_S1[n]/(n*ln(n)) < 12]]
    # [[n>=1] -> [abs(ln(1/3*PRIMES_S1[n]/(n*ln(n)))) < ln(12)]]
  More recently, Feigner 1990) obtained without much pain:
    [[n>=1] -> [0.91*n*ln(n) < PRIMES_S1[n] < 1.7*n*ln(n)]]

  [[n>=2] -> [PRIMES_S1[n]+PRIMES_S1[n+1] > PRIMES_S1[n+2]]]
  [[m,n>=1] -> [PRIMES_S1[m]*PRIMES_S1[n] > PRIMES_S1[m+n]]]
  [+oo == len{n | [[n:<-[1..]][@[i:<-[1..<n]] -> [PRIMES_S1[n]**2 > PRIMES_S1[n-i]*PRIMES_S1[n+i]]]]}]
    大于:几何平均
  [+oo == len{n | [[n:<-[1..]][@[i:<-[1..<n]] -> [PRIMES_S1[n]*2 < PRIMES_S1[n-i]+PRIMES_S1[n+i]]]]}]
    小于:算术平均

  [x::real]:
    [min_prime_ge_(x) =[def]= min{p | [[p :: prime][p >= x]]}]
    [min_prime_gt_(x) =[def]= min{p | [[p :: prime][p > x]]}]
    [max_prime_lt_(x) =[def]= min{p | [[p :: prime][p < x]]}]
    [max_prime_le_(x) =[def]= min{p | [[p :: prime][p <= x]]}]
  [x::real]:
    [num_primes_le(x) =[def]= len{p | [[p :: prime][p < x]]}]
  [x::real]:
    # Li(x):the function logarithmic integral of x # ver1
    [Li(x) =[def]= SS{1/ln(t) | [t :<~ 2 ~> x]}]
  [num_primes_le(x) /~/ Li(x) /~/ x/ln(x)]
    #Li更佳:
    #??? [(abs(Li(x) -num_primes_le(x))) = o(abs(x/ln(x) -num_primes_le(x)))]
    # The approximation of PI(x) by x/ln(x) is only reasonably good, while it is much better using the logarithmic integral,
    #
  [num_primes_le(PRIMES_S1[n]) == n]
  [PRIMES_S1[1+num_primes_le(x)] == min_prime_gt_(x)]
  [PRIMES_S1[num_primes_le(x)] == max_prime_le_(x)]

  [n>=1]:
    [gap4prime_(n) =[def]= min_prime_gt_(n) -n -1]
  [n>=1]:
    [gap_PRIMES_S1[n] =[def]= PRIMES_S1[n+1] -PRIMES_S1[n] -1]
    [diff_PRIMES_S1[n] =[def]= PRIMES_S1[n+1] -PRIMES_S1[n]]
  [diff_PRIMES_S1[n] == 1+gap_PRIMES_S1[n]]
  [diff_PRIMES_S1[n] == PRIMES_S1[n+1] -PRIMES_S1[n] == PRIMES[n] -PRIMES[n-1]]
  [low_gap>=1]:
    [min_prime4gap_ge_(low_gap) =[def]= min{PRIMES_S1[n] | [[n :<- [1..]][gap_PRIMES_S1[n] >= low_gap]]}]

  [素数间距猜想冫正偶数是无穷相邻素数对的间距:conjecture_Polignac_1849:[[k:<-[1..]] -> [len{n | [[n:<-[1..]][diff_PRIMES_S1[n]==2*k]]} == +oo]]]
    猜想特例:欤孪生素数对无穷多
    猜想泛化:[即使是未必相邻的素数间距同样不清楚]

  [猜想:ln(min_prime4gap_ge_(low_gap)) /~/ sqrt(low_gap)]
  [猜想:ln(min_prime4gap_ge_(low_gap)) /~/ sqrt(1.165746*low_gap)]
  [gap4prime_(6505941701960039) == 863]
    => [min_prime4gap_ge_(863) <= 6505941701960039]
  [gap4prime_(2500107922440823) == 783]
    => [min_prime4gap_ge_(783) <= 2500107922440823]
    [min_prime4gap_ge_(777) <= 42842283925351]
  [lim sup diff_PRIMES_S1[n] == +oo]
  [未知:lim inf diff_PRIMES_S1[n] < +oo]
  [[n>=1] -> [diff_PRIMES_S1[n] < PRIMES_S1[n]]]
    # [[n>=1] -> [PRIMES_S1[n+1] < 2*PRIMES_S1[n]]]
  [[(err,n0) :<- [(1/5,10),(1/13,118),(1/16597,2010760)]] -> [n>=n0] -> [diff_PRIMES_S1[n] < err*PRIMES_S1[n]]]
  [limit{diff_PRIMES_S1[n]/PRIMES_S1[n]| [n-->+oo]} == 0]



  [素数间距猜想冫素数间距估计约不超过对数平方:conjecture_Cramer_1937:diff_PRIMES_S1[n] == O(ln(PRIMES_S1[n])**2)]
  [[Riemann_hypothesis] => [diff_PRIMES_S1[n] == O(sqrt(PRIMES_S1[n])*ln(PRIMES_S1[n]))]]
  [[only the weaker density hypothesis on the nontrivial zeros of zeta(z)#Riemann_hypothesis] => @[err>0] -> [diff_PRIMES_S1[n] == O(PRIMES_S1[n]**(1/2+err))]]
  [@[e0 :<- [5/8,3/5,7/12,13/23,11/20,1/2+1/21~=0.5476...,11/20-1/384~=0.5473958...,6/11~=0.5454...,7/13~=0.53845...]] -> @[err>0] -> [diff_PRIMES_S1[n] == O(PRIMES_S1[n]**(e0+err))]]
  [lim inf (diff_PRIMES_S1[n]/ln(PRIMES_S1[n])) < 0.248]
  [lim sup (diff_PRIMES_S1[n]/ln(PRIMES_S1[n])) == +oo]

  #算术平均
  [[err>0] -> [+oo == len{n | [[n:<-[2..]][2*PRIMES_S1[n]**err > (PRIMES_S1[n-1]**err + PRIMES_S1[n+1]**err)]]}]]
    => [+oo == len{n | [[n:<-[2..]][diff_PRIMES_S1[n-1] > diff_PRIMES_S1[n]]]}]
  [[err>0] -> [+oo == len{n | [[n:<-[2..]][2*PRIMES_S1[n]**err < (PRIMES_S1[n-1]**err + PRIMES_S1[n+1]**err)]]}]]
    => [+oo == len{n | [[n:<-[2..]][diff_PRIMES_S1[n-1] < diff_PRIMES_S1[n]]]}]
  #几何平均
  [+oo == len{n | [[n:<-[2..]][PRIMES_S1[n]**2 > (PRIMES_S1[n-1] * PRIMES_S1[n+1])]]}]
  [+oo == len{n | [[n:<-[2..]][PRIMES_S1[n]**2 < (PRIMES_S1[n-1] * PRIMES_S1[n+1])]]}]

  [lim sup (min{diff_PRIMES_S1[n],diff_PRIMES_S1[n+1]}/ln(PRIMES_S1[n])) == +oo]
  [@[k:<-[1..]] -> [lim sup (min{diff_PRIMES_S1[n+i] | [i:<-[0..=k]]}/ln(PRIMES_S1[n]) * lnlnln(PRIMES_S1[n])**2/lnln(PRIMES_S1[n])/lnlnlnln(PRIMES_S1[n])) > 0]]

  [素数间距猜想冫素数平方根差分渐近于零:limit{(sqrt(PRIMES_S1[n+1]) -sqrt(PRIMES_S1[n])) | [n->+oo]} == 0]
  [素数间距猜想冫平方之间含素数:sqrt(PRIMES_S1[n+1]) -sqrt(PRIMES_S1[n]) < 1]
  [[PRIMES_S1[n] < 10**6] -> [sqrt(PRIMES_S1[n+1]) -sqrt(PRIMES_S1[n]) < 1]]

  #page248
  [conjecture_Opperman_1882:[n>1] -> [num_primes_le(n**2+n) > num_primes_le(n**2) > num_primes_le(n**2-n)]]
  #page248
  [conjecture_Brocard_1904:[n>=2] -> [num_primes_le(PRIMES_S1[n+1]**2) -num_primes_le(PRIMES_S1[n]**2) >= 4]]




]]
[[
素数数量牜小于十幂:here
    Table26
    Table27
    源自电子书，orc可能有误...
[num_primes_le(10**8) == 5761455]
[num_primes_le(10**9) == 50847534]
[num_primes_le(10**10) == 455052511]
[num_primes_le(10**11) == 4118054813]
[num_primes_le(10**12) == 37607912018]
[num_primes_le(10**13) == 346065536839]
[num_primes_le(1O**14) == 3204941750802]
[num_primes_le(1 * 10**15) == 29844570422669]
[num_primes_le(2 * 10**15) == 58478215681891]
[num_primes_le(3 * 10**15) == 86688602810119]
[num_primes_le(4 * 10**15) == 114630988904000]
[num_primes_le(5 * 10**15) == 142377417196364]
[num_primes_le(6 * 10**15) == 169969662554551]
[num_primes_le(7 * 10**15) == 197434994078331]
[num_primes_le(8 * 10**15) == 224792606318600]
[num_primes_le(9 * 10**15) == 252056733453928]
[num_primes_le(1 * 10**16) == 279238341033925]
[num_primes_le(2 * 10**16) == 547863431950008]
[num_primes_le(3 * 10**16) == 812760276789503]
[num_primes_le(4*10**16) <- {1075292778793150, 1075292778753150}]
[num_primes_le(5 * 10**16) == 1336094767763971]
[num_primes_le(6 * 10**16) == 1595534099589274]
[num_primes_le(7 * 10**16) == 1853851099626620]
[num_primes_le(8 * 10**16) == 2111215026220444]
[num_primes_le(9 * 10**16) == 2367751438410550]
[num_primes_le(1 * 10**17) == 2623557157654233]
[num_primes_le(2 * 10**17) == 5153329362645908]
[num_primes_le(3 * 10**17) == 7650011911275069]
[num_primes_le(4 * 10**17) == 10125681208311322]
[num_primes_le(5 * 10**17) == 12585956566571620]
[num_primes_le(6 * 10**17) == 15034102021263820]
[num_primes_le(7 * 10**17) == 17472251499627256]
[num_primes_le(8 * 10**17) == 19901908567967065]
[num_primes_le(9 * 10**17) == 22324189231374849]
[num_primes_le(1 * 10**18) == 24739954287740860]


<<==:

/sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu
I. The Growth of PI(x)
page237 [262/567] Table26
page238 [263/567] Table27

Table26:
x
10**8
10**9
10**10
10**11
10**12
10**13
1O**14
num_primes_le(x)
5761455
50847534
455052511
4118054813
37607912018
346065536839
3204941750802
floor(x/ln(x))-num_primes_le(x)
-332774
-2592592
-20758030
-169923160
-1416706193
-11992858452
-102838308636
floor(Li(x))-num_primes_le(x)
754
1701
3104
11588
38263
108971
314890
floor(Rm(x))-num_primes_le(x)
  #Rm(x):the_Riemann_function
97
-79
-1828
-2318
-1476
-5773
-19200
end-Table26
Table27:
x
1 * 10**15
2 * 10**15
3 * 10**15
4 * 10**15
5 * 10**15
6 * 10**15
7 * 10**15
8 * 10**15
9 * 10**15
1 * 10**16
2 * 10**16
3 * 10**16
4 * 10**16
5 * 10**16
6 * 10**16
7 * 10**16
8 * 10**16
9 * 10**16
1 * 10**17
2 * 10**17
3 * 10**17
4 * 10**17
5 * 10**17
6 * 10**17
7 * 10**17
8 * 10**17
9 * 10**17
1 * 10**18
num_primes_le(x)
29844570422669
58478215681891
86688602810119
114630988904000
142377417196364
169969662554551
197434994078331
224792606318600
252056733453928
279238341033925
547863431950008
812760276789503
1075292778753150#or:1075292778793150 # [num_primes_le(4*10**16) == 1075292778793150 or 1075292778753150]
1336094767763971
1595534099589274
1853851099626620
2111215026220444
2367751438410550
2623557157654233
5153329362645908
7650011911275069
10125681208311322
12585956566571620
15034102021263820
17472251499627256
19901908567967065
22324189231374849
24739954287740860
floor(Li(x))-num_primes_le(x)
1052619
1317791
1872580
1364039
2277608
1886041
2297328
2727671
1956031
3214632
3776488
4651601
5538861
6977890
5572837
8225687
6208817
9034988
7956589
10857072
14538005
19808695
19070319
20585416
18395468
16763001
26287786
21949555
floor(Rm(x))-num_primes_le(x)
73218
-37631
+233047
-512689
+193397
-384694
-144134
+127929
-791857
327052
-225875
-193899
-10980
811655
-1147719
997606
-1489898
895676
-598255
-1016134
152863
3323994
747495
609065
-3095204
-6132224
2077405
-3501366
end-Table27




]]


=====
]]]]]













py_adhoc_call   seed.math.prime_pint.num_primes_le   @num_primes_le__via_the_Meissel_formula_1871_ +with_stats  =2
py_adhoc_call   seed.math.prime_pint.num_primes_le   @num_primes_le__via_the_Meissel_formula_1871_ +with_stats  =20 +_verbose
    @num_primes_le(20): [g_r2 := 4][g_ps := (2, 3)]
    num_primes_le(2) -> 1
    num_primes_le(4) -> 2
    @num_primes_le(20): [r2 := 4][r3 := 2][m := 1][m2 := 2][s := 1]
    num_primes_le(0) -> 0
    num_coprimes4IIp_le(0, 1) -> 0
    num_coprimes4IIp_le(20, 1) -> 10
    num_primes_le(1) -> 0
    num_primes_le(2) -> 1
    @num_primes_le(6): [r2 := 2][r3 := 1][m := 0][m2 := 1][s := 1]
    num_coprimes4IIp_le(6, 0) -> 6
    num_primes_le(3) -> 2
    num_primes_le(6) -> 3
    num_primes_le(20) -> 8

    (8, (0.000414769000000037, 2, 1))

num_coprimes4IIp_le(28, 2)
    28//2==14
    28//3==9
    28//6==4
    28-14-9+4==9
    28==4*6+4
    4*2+1==9
>>> from math import gcd
>>> [i for i in range(28) if gcd(i,6)==1]
[1, 5, 7, 11, 13, 17, 19, 23, 25]
>>> len([i for i in range(28) if gcd(i,6)==1])
9
>>> num_primes_le__via_the_Meissel_formula_1871_(28)
9

[[[
===
py_adhoc_call   seed.math.prime_pint.num_primes_le   @num_primes_le__via_the_Meissel_formula_1871_ +with_stats  =200 +_verbose
@num_primes_le(200): [g_r2 := 14][g_ps := (2, 3, 5, 7, 11, 13)]
num_primes_le(5) -> 3
num_primes_le(14) -> 6
@num_primes_le(200): [r2 := 14][r3 := 5][m := 3][m2 := 6][s := 3]
num_primes_le(2) -> 1
num_primes_le(4) -> 2
@num_primes_le(20): [r2 := 4][r3 := 2][m := 1][m2 := 2][s := 1]
num_coprimes4IIp_le(0, 1) -> 0
num_coprimes4IIp_le(20, 1) -> 10
num_primes_le(6) -> 3
num_primes_le(20) -> 8
num_coprimes4IIp_le(20, 3) -> 6
num_coprimes4IIp_le(200, 3) -> 54
num_primes_le(3) -> 2
num_primes_le(5) -> 3
@num_primes_le(28): [r2 := 5][r3 := 3][m := 2][m2 := 3][s := 1]
num_primes_le(4) -> 2
num_coprimes4IIp_le(4, 2) -> 1
num_coprimes4IIp_le(28, 2) -> 9
num_primes_le(5) -> 3
num_primes_le(28) -> 9
num_primes_le(2) -> 1
num_primes_le(4) -> 2
@num_primes_le(18): [r2 := 4][r3 := 2][m := 1][m2 := 2][s := 1]
num_coprimes4IIp_le(0, 1) -> 0
num_coprimes4IIp_le(18, 1) -> 9
num_primes_le(6) -> 3
num_primes_le(18) -> 7
num_primes_le(2) -> 1
num_primes_le(3) -> 2
@num_primes_le(15): [r2 := 3][r3 := 2][m := 1][m2 := 2][s := 1]
num_coprimes4IIp_le(1, 1) -> 1
num_coprimes4IIp_le(15, 1) -> 8
num_primes_le(5) -> 3
num_primes_le(15) -> 6
num_primes_le(200) -> 46
(46, (0.0009720770000000156, 5, 5))
<<==:
===
py_adhoc_call   seed.math.prime_pint.num_primes_le   @num_primes_le__via_the_Meissel_formula_1871_ +with_stats  =28 +_verbose
@num_primes_le(28): [g_r2 := 5][g_ps := (2, 3, 5)]
num_primes_le(3) -> 2
num_primes_le(5) -> 3
@num_primes_le(28): [r2 := 5][r3 := 3][m := 2][m2 := 3][s := 1]
num_primes_le(4) -> 2
num_coprimes4IIp_le(4, 2) -> 1
num_coprimes4IIp_le(28, 2) -> 9
num_primes_le(5) -> 3
num_primes_le(28) -> 9
(9, (0.0002966920000000428, 1, 1))
===
<<==:
fixed:bug:bug_without_subtract_m:
py_adhoc_call   seed.math.prime_pint.num_primes_le   @num_primes_le__via_the_Meissel_formula_1871_ +with_stats  =28 +_verbose  >  /sdcard/0my_files/tmp/0tmp  2>&1
@num_primes_le(28): [g_r2 := 5][g_ps := (2, 3, 5)]
num_primes_le(3) -> 2
num_primes_le(5) -> 3
@num_primes_le(28): [r2 := 5][r3 := 3][m := 2][m2 := 3][s := 1]
num_primes_le(4) -> 2
num_coprimes4IIp_le(4, 2) -> 2
num_coprimes4IIp_le(28, 2) -> 10
num_primes_le(5) -> 3
num_primes_le(28) -> 10
(10, (0.00032769200000004606, 1, 1))
==>>:
py_adhoc_call   seed.math.prime_pint.num_primes_le   @num_primes_le__via_the_Meissel_formula_1871_ +with_stats  =200 +_verbose  >  /sdcard/0my_files/tmp/0tmp  2>&1
bug:(48, (0.0002325390000000871, 5, 5))
===
@num_primes_le(200): [g_r2 := 14][g_ps := (2, 3, 5, 7, 11, 13)]
num_primes_le(5) -> 3
num_primes_le(14) -> 6
@num_primes_le(200): [r2 := 14][r3 := 5][m := 3][m2 := 6][s := 3]
num_primes_le(2) -> 1
num_primes_le(4) -> 2
@num_primes_le(20): [r2 := 4][r3 := 2][m := 1][m2 := 2][s := 1]
num_primes_le(0) -> 0
num_coprimes4IIp_le(0, 1) -> 0
num_coprimes4IIp_le(20, 1) -> 10
num_primes_le(6) -> 3
num_primes_le(20) -> 8
num_coprimes4IIp_le(20, 3) -> 8
num_coprimes4IIp_le(200, 3) -> 56
num_primes_le(3) -> 2
num_primes_le(5) -> 3
@num_primes_le(28): [r2 := 5][r3 := 3][m := 2][m2 := 3][s := 1]
num_primes_le(4) -> 2
num_coprimes4IIp_le(4, 2) -> 2
num_coprimes4IIp_le(28, 2) -> 10
num_primes_le(5) -> 3
num_primes_le(28) -> 10 #bug
num_primes_le(2) -> 1
num_primes_le(4) -> 2
@num_primes_le(18): [r2 := 4][r3 := 2][m := 1][m2 := 2][s := 1]
num_primes_le(0) -> 0
num_coprimes4IIp_le(0, 1) -> 0
num_coprimes4IIp_le(18, 1) -> 9
num_primes_le(6) -> 3
num_primes_le(18) -> 7
num_primes_le(2) -> 1
num_primes_le(3) -> 2
@num_primes_le(15): [r2 := 3][r3 := 2][m := 1][m2 := 2][s := 1]
num_primes_le(1) -> 0
num_coprimes4IIp_le(1, 1) -> 0
num_coprimes4IIp_le(15, 1) -> 7
num_primes_le(5) -> 3
num_primes_le(15) -> 5
num_primes_le(200) -> 48
(48, (0.0009313080000000196, 5, 5))
===
]]]




py_adhoc_call   seed.math.prime_pint.num_primes_le   @num_primes_le__via_list_primes_le_ =200.5
46
[[[
===
py_adhoc_call { -lineno }  seed.math.prime_pint.num_primes_le   ,num_primes_le__via_list_primes_le__batch_ ='200'  >  /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp
0:0
1:0
2:1
3:2
4:2
5:3
6:3
7:4
8:4
9:4
10:4
11:5
12:5
13:6
14:6
15:6
16:6
17:7
18:7
19:8
20:8
21:8
22:8
23:9
24:9
25:9
26:9
27:9
28:9
29:10
30:10
31:11
32:11
33:11
34:11
35:11
36:11
37:12
38:12
39:12
40:12
41:13
42:13
43:14
44:14
45:14
46:14
47:15
48:15
49:15
50:15
51:15
52:15
53:16
54:16
55:16
56:16
57:16
58:16
59:17
60:17
61:18
62:18
63:18
64:18
65:18
66:18
67:19
68:19
69:19
70:19
71:20
72:20
73:21
74:21
75:21
76:21
77:21
78:21
79:22
80:22
81:22
82:22
83:23
84:23
85:23
86:23
87:23
88:23
89:24
90:24
91:24
92:24
93:24
94:24
95:24
96:24
97:25
98:25
99:25
100:25
101:26
102:26
103:27
104:27
105:27
106:27
107:28
108:28
109:29
110:29
111:29
112:29
113:30
114:30
115:30
116:30
117:30
118:30
119:30
120:30
121:30
122:30
123:30
124:30
125:30
126:30
127:31
128:31
129:31
130:31
131:32
132:32
133:32
134:32
135:32
136:32
137:33
138:33
139:34
140:34
141:34
142:34
143:34
144:34
145:34
146:34
147:34
148:34
149:35
150:35
151:36
152:36
153:36
154:36
155:36
156:36
157:37
158:37
159:37
160:37
161:37
162:37
163:38
164:38
165:38
166:38
167:39
168:39
169:39
170:39
171:39
172:39
173:40
174:40
175:40
176:40
177:40
178:40
179:41
180:41
181:42
182:42
183:42
184:42
185:42
186:42
187:42
188:42
189:42
190:42
191:43
192:43
193:44
194:44
195:44
196:44
197:45
198:45
199:46
200:46
===
]]]


[[[
素数数量牜小于二幂:here
2**[0..=40]
[num_primes_le(1) == num_primes_le(2**0) == 0]
[num_primes_le(2) == num_primes_le(2**1) == 1]
[num_primes_le(4) == num_primes_le(2**2) == 2]
[num_primes_le(8) == num_primes_le(2**3) == 4]
[num_primes_le(16) == num_primes_le(2**4) == 6]
[num_primes_le(32) == num_primes_le(2**5) == 11]
[num_primes_le(64) == num_primes_le(2**6) == 18]
[num_primes_le(128) == num_primes_le(2**7) == 31]
[num_primes_le(256) == num_primes_le(2**8) == 54]
[num_primes_le(512) == num_primes_le(2**9) == 97]
[num_primes_le(1024) == num_primes_le(2**10) == 172]
[num_primes_le(2048) == num_primes_le(2**11) == 309]
[num_primes_le(4096) == num_primes_le(2**12) == 564]
[num_primes_le(8192) == num_primes_le(2**13) == 1028]
[num_primes_le(16384) == num_primes_le(2**14) == 1900]
[num_primes_le(32768) == num_primes_le(2**15) == 3512]
[num_primes_le(65536) == num_primes_le(2**16) == 6542]
[num_primes_le(131072) == num_primes_le(2**17) == 12251]
[num_primes_le(262144) == num_primes_le(2**18) == 23000]
[num_primes_le(524288) == num_primes_le(2**19) == 43390]
[num_primes_le(1048576) == num_primes_le(2**20) == 82025]
[num_primes_le(2097152) == num_primes_le(2**21) == 155611]
[num_primes_le(4194304) == num_primes_le(2**22) == 295947]
[num_primes_le(8388608) == num_primes_le(2**23) == 564163]
[num_primes_le(16777216) == num_primes_le(2**24) == 1077871]
[num_primes_le(33554432) == num_primes_le(2**25) == 2063689]
[num_primes_le(67108864) == num_primes_le(2**26) == 3957809]
[num_primes_le(134217728) == num_primes_le(2**27) == 7603553]
[num_primes_le(268435456) == num_primes_le(2**28) == 14630843]
[num_primes_le(536870912) == num_primes_le(2**29) == 28192750]
[num_primes_le(1073741824) == num_primes_le(2**30) == 54400028]
[num_primes_le(2147483648) == num_primes_le(2**31) == 105097565]
[num_primes_le(4294967296) == num_primes_le(2**32) == 203280221]
[num_primes_le(8589934592) == num_primes_le(2**33) == 393615806]
[num_primes_le(17179869184) == num_primes_le(2**34) == 762939111]
[num_primes_le(34359738368) == num_primes_le(2**35) == 1480206279]
[num_primes_le(68719476736) == num_primes_le(2**36) == 2874398515]
[num_primes_le(137438953472) == num_primes_le(2**37) == 5586502348]
[num_primes_le(274877906944) == num_primes_le(2**38) == 10866266172]
[num_primes_le(549755813888) == num_primes_le(2**39) == 21151907950]
[num_primes_le(1099511627776) == num_primes_le(2**40) == 41203088796]
<<==:
(1, (0, (1.2845999999955282e-05, 0, 0)))
(2, (1, (6.069300000000055e-05, 1, 0)))
(4, (2, (5.1076999999954964e-05, 1, 0)))
(8, (4, (2.399999999991298e-05, 1, 0)))
(16, (6, (9.669199999995381e-05, 2, 1)))
(32, (11, (8.276899999992704e-05, 2, 1)))
(64, (18, (0.00013961500000003735, 3, 3)))
(128, (31, (8.676999999990276e-05, 2, 2)))
(256, (54, (0.00013230699999999818, 4, 4)))
(512, (97, (0.00016761499999995433, 6, 6)))
(1024, (172, (0.0002236930000000248, 8, 9)))
(2048, (309, (0.00031969200000003806, 11, 13)))
(4096, (564, (0.00044800000000000395, 15, 21)))
(8192, (1028, (0.0007126920000000148, 18, 35)))
(16384, (1900, (0.0008814609999999723, 23, 51)))
(32768, (3512, (0.0013126159999999887, 31, 78)))
(65536, (6542, (0.0019156150000000371, 43, 121)))
(131072, (12251, (0.0029338460000000177, 58, 218)))
(262144, (23000, (0.005807077000000049, 80, 400)))
(524288, (43390, (0.007611460999999986, 107, 720)))
(1048576, (82025, (0.010639385000000057, 147, 1268)))
(2097152, (155611, (0.01322246199999999, 199, 2226)))
(4194304, (295947, (0.022527768999999975, 273, 3722)))
(8388608, (564163, (0.022156999999999982, 373, 6346)))
(16777216, (1077871, (0.06516015399999997, 511, 10235)))
(33554432, (2063689, (0.054444924000000006, 695, 16798)))
(67108864, (3957809, (0.10313130800000003, 950, 27511)))
(134217728, (7603553, (0.16844461500000008, 1297, 45105)))
(268435456, (14630843, (0.27764715399999984, 1784, 74488)))
(536870912, (28192750, (0.4179942310000002, 2445, 120301)))
(1073741824, (54400028, (0.7102053880000003, 3341, 194828)))
(2147483648, (105097565, (1.1622141590000004, 4584, 313093)))
(4294967296, (203280221, (1.8447983140000002, 6286, 502217)))
(8589934592, (393615806, (3.1132509340000003, 8644, 807862)))
(17179869184, (762939111, (5.276228477000001, 11876, 1296831)))
(34359738368, (1480206279, (8.633271724, 16321, 2088659)))
(68719476736, (2874398515, (13.842304479000003, 22437, 3358733)))
(137438953472, (5586502348, (119.9659469, 30893, 43911572)))
(274877906944, (10866266172, (220.82194248899998, 42549, 81423720)))
(549755813888, (21151907950, (397.7775248660001, 58604, 151521755)))
(1099511627776, (41203088796, (755.9730056129999, 80760, 283701536)))

<<==:
===
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[2**e for e in range(16)]' +with_stats +to_pair
(1, (0, (1.2845999999955282e-05, 0, 0)))
(2, (1, (6.069300000000055e-05, 1, 0)))
(4, (2, (5.1076999999954964e-05, 1, 0)))
(8, (4, (2.399999999991298e-05, 1, 0)))
(16, (6, (9.669199999995381e-05, 2, 1)))
(32, (11, (8.276899999992704e-05, 2, 1)))
(64, (18, (0.00013961500000003735, 3, 3)))
(128, (31, (8.676999999990276e-05, 2, 2)))
(256, (54, (0.00013230699999999818, 4, 4)))
(512, (97, (0.00016761499999995433, 6, 6)))
(1024, (172, (0.0002236930000000248, 8, 9)))
(2048, (309, (0.00031969200000003806, 11, 13)))
(4096, (564, (0.00044800000000000395, 15, 21)))
(8192, (1028, (0.0007126920000000148, 18, 35)))
(16384, (1900, (0.0008814609999999723, 23, 51)))
(32768, (3512, (0.0013126159999999887, 31, 78)))

===
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[2**e for e in range(16,24)]' +with_stats +to_pair
(65536, (6542, (0.0019156150000000371, 43, 121)))
(131072, (12251, (0.0029338460000000177, 58, 218)))
(262144, (23000, (0.005807077000000049, 80, 400)))
(524288, (43390, (0.007611460999999986, 107, 720)))
(1048576, (82025, (0.010639385000000057, 147, 1268)))
(2097152, (155611, (0.01322246199999999, 199, 2226)))
(4194304, (295947, (0.022527768999999975, 273, 3722)))
(8388608, (564163, (0.022156999999999982, 373, 6346)))


===
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[2**e for e in range(24,32)]' +with_stats +to_pair
(16777216, (1077871, (0.06516015399999997, 511, 10235)))
(33554432, (2063689, (0.054444924000000006, 695, 16798)))
(67108864, (3957809, (0.10313130800000003, 950, 27511)))
(134217728, (7603553, (0.16844461500000008, 1297, 45105)))
(268435456, (14630843, (0.27764715399999984, 1784, 74488)))
(536870912, (28192750, (0.4179942310000002, 2445, 120301)))
(1073741824, (54400028, (0.7102053880000003, 3341, 194828)))
(2147483648, (105097565, (1.1622141590000004, 4584, 313093)))
===
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[2**e for e in range(32,37)]' +with_stats +to_pair
(4294967296, (203280221, (1.8447983140000002, 6286, 502217)))
(8589934592, (393615806, (3.1132509340000003, 8644, 807862)))
(17179869184, (762939111, (5.276228477000001, 11876, 1296831)))
(34359738368, (1480206279, (8.633271724, 16321, 2088659)))
(68719476736, (2874398515, (13.842304479000003, 22437, 3358733)))
===
#py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[2**e for e in range(37,41)]' +with_stats +to_pair
    #cellphone crash @[e==39]
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[2**e for e in range(37,41)]' +with_stats +to_pair +no_cache
(137438953472, (5586502348, (119.9659469, 30893, 43911572)))
(274877906944, (10866266172, (220.82194248899998, 42549, 81423720)))
(549755813888, (21151907950, (397.7775248660001, 58604, 151521755)))
(1099511627776, (41203088796, (755.9730056129999, 80760, 283701536)))

===
verify by:
    Table26:goto
    Table27:goto

py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[10**e for e in range(8,15)]' +with_stats +to_pair    >  /sdcard/0my_files/tmp/0tmp
(100000000, (5761455, (0.13529961699999993, 1140, 36652)))
(1000000000, (50847534, (0.7017260009999999, 3234, 185180)))
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[10**e for e in range(10,11)]' +with_stats +to_pair
(10000000000, (455052511, (3.4950083209999994, 9268, 896055)))
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[10**11]' +with_stats +to_pair
(100000000000, (4118054813, (18.701691734999997, 26668, 4324996)))

===
++kw:no_cache
    cache() --> _4stats()
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[10**8]' +with_stats +to_pair -no_cache
(100000000, (5761455, (0.14021115399999995, 1140, 36652)))
py_adhoc_call   seed.math.prime_pint.num_primes_le   ,iter_applys__num_primes_le__via_the_Meissel_formula_1871_ ='[10**8]' +with_stats +to_pair +no_cache
(100000000, (5761455, (0.25191838700000013, 1140, 73928)))
    #vs:using"cache":(100000000, (5761455, (0.13529961699999993, 1140, 36652)))
    1140 == 1140
        # num calls to _num_primes_le
    73928 > 36652
        # num calls to _num_coprimes4IIp_le
        # 节省一倍计算量
===
>>> (10**12).bit_length()
40

===
]]]

>>> xs = [2**e for e in range(16)]
>>> [*iter_applys__num_primes_le__via_the_Meissel_formula_1871_(xs, to_pair=True)]
[(1, 0), (2, 1), (4, 2), (8, 4), (16, 6), (32, 11), (64, 18), (128, 31), (256, 54), (512, 97), (1024, 172), (2048, 309), (4096, 564), (8192, 1028), (16384, 1900), (32768, 3512)]
>>> num_primes_le__via_list_primes_le__batch_(xs, to_pair=True)
((1, 0), (2, 1), (4, 2), (8, 4), (16, 6), (32, 11), (64, 18), (128, 31), (256, 54), (512, 97), (1024, 172), (2048, 309), (4096, 564), (8192, 1028), (16384, 1900), (32768, 3512))
>>> num_primes_le__via_list_primes_le__batch_(xs)
(0, 1, 2, 4, 6, 11, 18, 31, 54, 97, 172, 309, 564, 1028, 1900, 3512)

>>> [*map(num_primes_le__via_the_Meissel_formula_1871_, range(1001))] == [*num_primes_le__via_list_primes_le__batch_(1000)]
True



]]]'''#'''
__all__ = r'''
num_primes_le__via_the_Meissel_formula_1871_
    iter_applys__num_primes_le__via_the_Meissel_formula_1871_

num_primes_le__via_list_primes_le_
    num_primes_le__via_list_primes_le__batch_
'''.split()#'''
    #_icbrt
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from seed.func_tools.recur5yield import recur5yield__list__echo__echo# recur5yield__list__echo__off, recur5yield__list__0func__echo, recur5yield__list__0func__off
    #to avoid sys.setrecursionlimit()

import sys
from time import thread_time
from functools import cache
    #cache(f).cache_info()
    #CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)
    #[cache(f).cache_info().currsize :: uint]
from math import isqrt, cbrt, floor
from bisect import bisect_right
#from itertools import pairwise #islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError


def _icbrt(x, /):
    r3 = floor(cbrt(x))
    if not r3**3 <= x < (r3+1)**3:raise NotImplementedError(f'_icbrt({x})')
    return r3

def num_primes_le__via_list_primes_le__batch_(xs_or_max_x, /, *, to_pair=False):
    from seed.math.prime_pint.generate_primes import list_primes_le_
    try:
        iter(xs_or_max_x)
    except TypeError:
        whether_iterable = False
    else:
        whether_iterable = True
    if not whether_iterable:
        max_x = xs_or_max_x
        max_x = floor(max_x)
        xs = range(1+max_x)
    else:
        xs = xs_or_max_x
        xs = tuple(map(floor, xs))
        if not xs:
            return xs
        max_x = max(xs)
    max_x
    xs
    ps = list_primes_le_(max_x)
    if not whether_iterable:
        szs = []
        p_ = 0
        sz = -1
        for sz, p in enumerate(ps):
            szs += [sz]*(p-p_)
            p_ = p
        else:
            sz += 1
        sz
        szs += [sz]*(1+max_x-p_)
        assert len(szs) == len(xs)
        assert szs[-1] == szs[max_x] == len(ps)
    else:
        szs = (bisect_right(ps, x) for x in xs)
    szs
    it = zip(xs, szs) if to_pair else szs
    return tuple(it)


def num_primes_le__via_list_primes_le_(x, /):
    from seed.math.prime_pint.generate_primes import list_primes_le_
    return len(list_primes_le_(x))
def num_primes_le__via_the_Meissel_formula_1871_(x, /, *, _upperbound4using_cache=2**38, no_cache=False, with_stats=False, _verbose=False):
    r'''
    x/real -> num_primes_le(x)/uint

    the_Meissel_formula_1871
    [@[x::real{>=0}] -> [m:=num_primes_le(x**/3)] -> [m2:=num_primes_le(x**/2)] -> [s:=m2-m] -> [num_primes_le(x) == num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -[x>=1] -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]]]
    <<==:
    [@[x::real{>=1}] -> [m:=num_primes_le(x**/3)] -> [m2:=num_primes_le(x**/2)] -> [s:=m2-m] -> [num_primes_le(x) == num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -1 -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]]]
    <<==:
    [@[x::real] -> @[m::int{>=0}] -> [x < PRIMES_S1[m+1]**2] -> [num_coprimes4IIp_le(x;m) == [x>=1]+max(0,(num_primes_le(x) -m))]]
    [@[x::real{>=1}] -> [m2:=num_primes_le(x**(1/2))] -> [num_primes_le(x) == -1+m2+num_coprimes4IIp_le(x;m2)]]
    <<==:
    [[N>=1] -> [num_primes_le(N) == num_primes_le(floor_sqrt(N)) -1+sum[mu(d)*(N//d) | [[d:<-all_divisors_of(II[p | [[p::prime][p**2<=N]]])][d<=N]]]]]
    <<==:
    Eratosthenes sieve

    '''#'''
    #check_type_is(bool, no_cache)

    # [x :: real]
    x = floor(x)
    #if x < 1: return 0
    if x < 0: return 0
    # [x :: uint]
    # [x >= 0]

    using_cache = not no_cache
    if using_cache and not x <= _upperbound4using_cache:raise ValueError('too big to use cache # kw:{no_cache,_upperbound4using_cache}') # [cellphone crash at num_primes_le(2**39)]
    _cache = _4stats if not using_cache else cache
    if _verbose:
        from seed.tiny import print_err
    def __():
        from seed.math.prime_pint.generate_primes import list_primes_le_
        # !! [x >= 0]
        r2 = isqrt(x)
        ps = list_primes_le_(r2)
        return (r2, ps)
    (g_r2, g_ps) = __()
    if _verbose:
        print_err(f'@num_primes_le({x}): [g_r2 := {g_r2}][g_ps := {g_ps}]')
    def num_primes_le(x, /):
        'x/uint -> num_primes_le(x)/uint'
        if x <= g_r2:
            # [x <= g_r2]
            sz = bisect_right(g_ps, x)
        else:
            # [x > g_r2 >= 0]
            # [x >= 1]
            sz = _num_primes_le(x)
        sz
        if _verbose:
            print_err(f'num_primes_le({x}) -> {sz}')
        return sz
    #@cache#if with_stats
    @_cache#if not no_cache
    def _num_primes_le(x, /):
        'x/uint{>=1} -> num_primes_le(x)/uint'
        r2 = isqrt(x)
        r3 = _icbrt(x)
        m = num_primes_le(r3)
        m2 = num_primes_le(r2)
        s = m2 -m
        #if 0b0001:print(f'@num_primes_le({x}): [r2 := {r2}][r3 := {r3}][m := {m}][m2 := {m2}][s := {s}]')
        #   @num_primes_le(10000000000): [r2 := 100000][r3 := 2154][m := 325][m2 := 9592][s := 9267]
        if _verbose:
            print_err(f'@num_primes_le({x}): [r2 := {r2}][r3 := {r3}][m := {m}][m2 := {m2}][s := {s}]')
        if s == 0:
            #otherwise:^RecursionError: maximum recursion depth exceeded while calling a Python object
            #   !! num_primes_le <--> num_coprimes4IIp_le
            if x == 8:
                return 4
            assert x < 4, x
                #^AssertionError: 8
            return max(0, x-1)
        # [num_primes_le(x) == num_coprimes4IIp_le(x;m) +m*(s+1) +s*(s-1)///2 -[x>=1] -sum[num_primes_le(x/PRIMES_S1[j]) | [j:<-[m+1..=m2]]]]
        return (
        (num_coprimes4IIp_le(x, m)
        +m*(s+1)
        +s*(s-1)//2
        -(x>=1)
        -sum(num_primes_le(x//PRIMES_S1(j)) for j in range(m+1, 1+m2))
        ))
    #if with_stats:_num_primes_le = _4stats(_num_primes_le)

    def PRIMES_S1(m, /):
        # [PRIMES_S1[1] == 2]
        assert m >= 1
        return g_ps[m-1]
    def num_coprimes4IIp_le(x, m, /):
        'uint -> uint -> uint'
        assert m >= 0
        # [m >= 0]
        if m == 0:
            sz = x
        # [m >= 1]
        #bug:if PRIMES_S1(m+1)**2 > x:
        elif m==len(g_ps) or PRIMES_S1(m+1)**2 > x:
            #bug:sz = num_primes_le(x)
            #   bug_without_subtract_m:here
            # !! [@[x::real] -> @[m::int{>=0}] -> [x < PRIMES_S1[m+1]**2] -> [num_coprimes4IIp_le(x;m) == [x>=1]+max(0,(num_primes_le(x) -m))]]
            #sz = (x>=1) + max(0, num_primes_le(x) -m)
            # !! [m >= 1]
            sz = (x>=1) + max(0, (num_primes_le(x) -m) if x > PRIMES_S1(m) else 0)
        # [m >= 1]
        else:
            # [PRIMES_S1[m+1]**2 <= x]
            # [m >= 1]
            sz = _num_coprimes4IIp_le(x, m)
            sz
        sz
        if _verbose:
            print_err(f'num_coprimes4IIp_le({x}, {m}) -> {sz}')
        return sz
    #@cache#if with_stats
    @_cache#if not no_cache
    def _num_coprimes4IIp_le(x, m, /):
        # [PRIMES_S1[m+1]**2 <= x]
        # [num_primes_le(x**/2) >= m+1]
        assert m >= 1
        # [m >= 1]
        # [num_primes_le(x**/2) >= 2]
        # [(x**/2) >= 3]
        # [x >= 9]
        assert x >= 9, (x, m)
            #??? [x:=10**10][m too large] => ^RecursionError: maximum recursion depth exceeded in comparison
            #   @num_primes_le(10000000000): [r2 := 100000][r3 := 2154][m := 325][m2 := 9592][s := 9267]
            # why? m only 325: 325*3 > 1000(default:sys.getrecursionlimit())
            #
        #if x < 2: return x
        b_m_small = m <= g_max_m4IIp
        if b_m_small:
            IIpm = IIp_(m)
        if b_m_small and IIpm <= x:
            #division_property
            q, r = divmod(x, IIpm)
            return phi_IIp_(m)*q + num_coprimes4IIp_le(r, m)
        # [9 <= x < IIp_(m)]
        if b_m_small and 2*x > IIpm:
            #symmetry_property
            # [IIpm/2 < x < IIp_(m)]
            y = IIpm -x -1
            # [0 <= y <= IIpm/2]
            return phi_IIp_(m) -num_coprimes4IIp_le(y, m)
        # [9 <= x <= IIp_(m)/2]
        # [m >= 1]
        #recurrence_relation
        #[@[x::real] -> @[m::int{>=1}] -> [num_coprimes4IIp_le(x;m) == num_coprimes4IIp_le(x;m-1) -num_coprimes4IIp_le(floor(x/PRIMES_S1[m]);m-1)]]
        return (
        (num_coprimes4IIp_le(x, m-1)
        -num_coprimes4IIp_le(x//PRIMES_S1(m), m-1)
        ))
    #if with_stats:_num_coprimes4IIp_le = _4stats(_num_coprimes4IIp_le)


    @cache#ALWAYS
    def IIp_(m, /):
        'uint -> pint'
        assert m >= 0
        # [m >= 0]
        if m == 0:
            return 1
        # [m >= 1]
        return IIp_(m-1)*PRIMES_S1(m)
    @cache#ALWAYS
    def phi_IIp_(m, /):
        'uint -> pint'
        assert m >= 0
        # [m >= 0]
        if m == 0:
            return 1
        # [m >= 1]
        return phi_IIp_(m-1)*(PRIMES_S1(m)-1)
    def find_max_m4IIp_(x, /):
        x2 = 2*x
        for m, p in enumerate(g_ps, 1):
            if x2 < IIp_(m):
                break
        else:
            m = len(g_ps)
        m
        assert m == len(g_ps) or x*2 < IIp_(m)
        return m
    def main(x, /):
        old_recursionlimit = sys.getrecursionlimit()
        sys.setrecursionlimit(len(g_ps)*10)
        try:
            return _main(x)
        finally:
            sys.setrecursionlimit(old_recursionlimit)

    def _main(x, /):
        if not with_stats:
            return num_primes_le(x)
        t0 = thread_time()
        sz = num_primes_le(x)
        t1 = thread_time()
        dt = t1 -t0
        if not no_cache:
            sz1 = _num_primes_le.cache_info().currsize
            sz2 = _num_coprimes4IIp_le.cache_info().currsize
        else:
            sz1 = _num_primes_le.n
            sz2 = _num_coprimes4IIp_le.n
        return (sz, (dt, sz1, sz2))

    g_max_m4IIp = find_max_m4IIp_(x)
    return main(x)
class _4stats:
    def __init__(sf, f, /):
        sf.f = f
        sf.n = 0
    def __call__(sf, /, *args):
        sf.n += 1
        return sf.f(*args)
def iter_applys__num_primes_le__via_the_Meissel_formula_1871_(xs, /, to_pair=False, **kwds):
    'xs/(Iter real) -> Iter (x,num_primes_le(x))/(real,uint)'
    for x in xs:
        r = num_primes_le__via_the_Meissel_formula_1871_(x, **kwds)
        yield (r if not to_pair else (x, r))




__all__
from seed.math.prime_pint.num_primes_le import num_primes_le__via_the_Meissel_formula_1871_, iter_applys__num_primes_le__via_the_Meissel_formula_1871_

from seed.math.prime_pint.num_primes_le import num_primes_le__via_list_primes_le_, num_primes_le__via_list_primes_le__batch_
from seed.math.prime_pint.num_primes_le import *
