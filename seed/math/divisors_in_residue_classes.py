#__all__:goto
#DONE:++kX,++kw:_fixed_kX_eq1
#TODO:原文cbrt vs 我版sqrt 是怎么回事？
r'''[[[
e ../../python3_src/seed/math/divisors_in_residue_classes.py

seed.math.divisors_in_residue_classes
py -m nn_ns.app.debug_cmd   seed.math.divisors_in_residue_classes -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.divisors_in_residue_classes:__doc__ -ht # -ff -df
#######

[x**/y =[def]= x**(1/y)]
[[
view others/数学/prime/finite_field_primality_test.txt
Theorem__4_2_12:goto
  Algorithm__4_2_11:goto
    #算法牜快速找出所有因子乊特定剩余类:goto
]]
[[[[[
@20260425:copy from:
    view others/数学/prime/finite_field_primality_test.txt
===
'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
[[
===
page186[198/604]
Chapter 4 PRIMALITY PROVING
4.2 The n + 1 test
4.2.3 Divisors in residue classes
  #算法牜快速找出所有因子乊特定剩余类:here
  #算法:快速找出形如(q*F+r)的因子
  #用于 [n**/3 < F < n**/2]@Theorem 4.2.10
  #     或者:when F/n**/3 is not too small.
Algorithm__4_2_11:here
Theorem__4_2_12:goto
Algorithm 4.2.11 (Divisors in residue classes).
  We are given positive integers n,r,s with r < s < n and gcd(r,s) = 1.#补丁:[n%s =!= 0]
  This algorithm creates a list of all divisors of n that are congruent to r (mod s).
  1. [Initialize]
    rv := r**-1 mod s;
      # 1/r %s
    r_ := n*rv mod s;
      # n/r %s
    (a0,a1) := (s,r_*rv mod s);
      # (s, n/r**2 %s)
      # [a0 > a1 > 0]
      #   这里得有:[n%s =!= 0] => [a1>0]
      # [s > a1 >= a[t-1] == gcd(n,s)]
      # [gcd(n,s)][r:=n**j%s for all j] => [min min_AB6odd == 1]
    (b0,b1) := (0,1);
    ???bug??? 原文: (c0,c1) := (0,(n*rv -r*a1)/s mod s);
      # (0,(n/r%s -r*(n/r**2%s))///s %s)
    改为 (c0,c1) := (0,(n*rv -r*r_*rv)///s mod s);
  2. [Euclidean chains]
    Develop the Euclidean sequences (a[i]),(q[i]), where
      a[i] := a[i-2] -q[i]*a[i-1]
      and
        0 ≤ a[i] < a[i-1] for i even,
        0 < a[i] ≤ a[i-1] for i odd,
        terminating at a[t]= 0 with t even;
      <==>:
      * [a[i-1] == 0]:
        [t := i-1]
        [t%2==0]
      * [a[i-1] =!= 0]:
        [i-1 < t]
        * [i%2==0]:
          [(q[i],a[i]) := divmod(a[i-2],a[i-1])]
          [0 <= a[i] < a[i-1]] # [i>=2]
          [q[i] > 0] # [i>=2]
        * [i%2==1]:
          [(q[i],a[i]-1) := divmod(a[i-2]-1,a[i-1])]
          [0 <= a[i]-1 < a[i-1]]
          [0 < a[i] <= a[i-1]] # [i>=3]
          !! [a0 > a1 > 0]
          [0 < a[1] <= a[0]]
          [0 < a[i] <= a[i-1]] # [i>=1]
            # => [t%2==0]
          [q[i] > 0] # [i>=3]
        [q[i] > 0] # [i>=2]
        [0 +[i%2==1] <= a[i] < a[i-1] +[i%2==1]] # [i>=1]
    Develop the sequences (b[i]),(c[i]) for i = 0,1,...,t with the rules
      b[i] := b[i-2] -q[i]*b[i-1],
      c[i] := c[i-2] -q[i]*c[i-1];
  3. [Loop]
    for(0 ≤ i ≤ t) {
      For each integer c ≡ c[i] (mod s) with
          |c| < s if i is even,
          ???bug??? 原文:2*a[i]*b[i] < c < a[i]*b[i] + n/s**2 if i is odd,
          改为:2*a[i]*b[i] <= c <= a[i]*b[i] + n/s**2 if i is odd,
        attempt to solve the following system for x,y:
          x*a[i] +y*b[i] == c,
          (x*s + r)*(y*s + r_) == n;
            # (4.16)
        If a nonnegative integral solution (x,y) is found, report (x*s + r) as a divisor of n that is also ≡ r (mod s);
    }
The theoretical justification for this algorithm is as follows:
===
page187[199/604]
Theorem__4_2_12:here
Algorithm__4_2_11:goto
Theorem 4.2.12 (Lenstra).
  Algorithm 4.2.11 creates the list of all divisors of n that are congruent to r (mod s).
  Moreover, if s ≥ n**/3, then the running time is O(ln(n)) arithmetic operations on integers of size O(n) and O(ln(n)) evaluations of the integer part of square root for arguments of size O(n**7).

===
ie. Theorem__4_2_12 ==:
  Algorithm__4_2_11 输出n的所有型如(x*s+r)的因子
    [[s**3 > n] -> [耗时:O(ln(n)) * (__mul__{n} + sqrt{n**7})]]
~~<==>:
[@[n,s,r::uint] -> [0 < r < s < n] -> [gcd(r,s) = 1] -> [n%s =!= 0] -> []
  -> [rv := r**-1%s]
  -> [r_ := n*rv%s]
  -> [(a[0],a[1]) := (s,r_*rv%s)]
  -> [(b[0],b[1]) := (0,1)]
  -> [(c[0],c[1]) := (0,(n*rv -r*r_*rv)///s%s)]
  -> [(q[0],q[1]) := (-oo,-oo)]
  -> [?[t::uint] -> [[t>=2][a[t]==0][@[i:<-2..=t] -> [(q[i],a[i]-[i%2==1]) := divmod(a[i-2]-[i%2==1],a[i-1])]]]]
  -> [@[i:<-2..=t] -> [b[i] := b[i-2] -q[i]*b[i-1]][c[i] := c[i-2] -q[i]*c[i-1]]]
  -> [B := max{abs(b[i]) | [i:<-[0..=t]]}]
  -> @[kX::real{>0}]
  -> [@[i:<-[0..=t]] -> [i2LB4c[i] := if [i%2==0] then -(ceil(kX*s)-1) else ceil(2*kX*a[i]*b[i])]]
  -> [@[i:<-[0..=t]] -> [i2UB4c[i] := if [i%2==0] then +(ceil(kX*s)-1) else floor(kX*a[i]*b[i] + n/s**2/kX)]]
  -> [@[i:<-[0..=t]] -> [i2cs[i] := range(c[i]+ceil_div(i2LB4c[i]-c[i],s)*s, 1+i2UB4c[i], s)]]
    # [i2cs[i] := {c | [[c::int][c =[%s]= c[i]][i2LB4c[i] <= c <= i2UB4c[i]]]}]
  -> [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [ij2eqn_system4XY[i,j] := [[X*a[i] +Y*b[i] == i2cs[i][j]][(X*s + r)*(Y*s + r_) == n]]]]
  -> [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [ij2eqn4Z[i,j] := [z**2 -(i2cs[i][j]*s + r*a[i] + r_*b[i])*z +(n*a[i]*b[i]) == 0]]]
  -> [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [ij2DET4eqn4Z[i,j] := (i2cs[i][j]*s + r*a[i] + r_*b[i])**2 -4*n*a[i]*b[i]]] # def:DET{ij2eqn4Z[i,j]}
  -> [
    #bug:[t <= 1+log_((1+sqrt5)/2;s)]
    [t <= 2+log_((1+sqrt5)/2;sqrt5*s)]
    [t == O(ln(n))]
    [t%2==0]
    [b[t] < 0]
    [B == -b[t]]
    #bug:[s**(3/2) > 2**t]
    [s**(3/2) > 2**(t-3.672276) > 2**t /12.748681]
    [[s**3 >= n] -> [B <= 2**t*s < 12.748681*s**(5/2)]]

    [[i:<-[1..=t]] -> [0 +[i%2==1] <= a[i] < a[i-1] +[i%2==1]]]
    [[i:<-[2..=t]] -> [q[i] > 0]]
    [[i:<-[0..=t]] -> [if i==t then [a[i] == 0] else [a[i] > 0]]]
    [[i:<-[0..=t]] -> [sign_of(b[i]) == if i==0 then 0 else (-1)**(i+1)]]
    [[i:<-[0..<t]] -> [b[i+1]*a[i] -a[i+1]*b[i] == s*(-1)**i]]

    [[kX==1] -> @[i:<-[0..=t]] -> [len(i2cs[i]) <= [i%2==0]2 + [i%2==1](1+floor(n/s**3))]]
    [[kX==1] -> [s**3 >= n] -> @[i:<-[0..=t]] -> [len(i2cs[i]) <= 2]]

    [@[x::uint] -> [n%(x*s+r) == 0] -> [y := n///(x*s+r) %s]
    -> [@[i:<-[0..=t]] -> [i2c6xy[i] := (x*a[i] +y*b[i])]] # def:c#c[i]的某个解压值
    #bug: [@[i:<-[0..=t]] -> [i2eqn_system4xy[i] := [[x*a[i] +y*b[i] == i2c6xy[i]][(x*s + r)*(y*s + r_) == n]]]]
    #bug: [i2eqn4z[i] := [z**2 -(c*s + r*a[i] + r_*b[i])*z +(n*a[i]*b[i]) == 0]]
    #bug: [@[i:<-[0..=t]] -> [i2DET6z[i] := (i2c6xy[i]*s + r*a[i] + r_*b[i])**2 -4*n*a[i]*b[i]]] # def:DET{i2eqn4z[i]}
    -> [
      [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [i2cs[i][j] == i2c6xy[i]] -> [[roots_of(ij2eqn4Z[i,j]) == {(x*s + r)*a[i], (y*s + r_)*b[i]}][sqrt(ij2DET4eqn4Z[i,j]) %1.0 == 0.0]]]
      [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [O(sqrt{ij2DET4eqn4Z[i,j]}) == O(sqrt{s**7}) == O(sqrt{n**7})]]

      [?[k:<-[0..=t]] -> [i2c6xy[k] <- i2cs[k]]]
        # [[@[i:<-[0..=t]] -> [i2c6xy[i] =[%s]= c[i]]][?[j:<-[0..=t]] -> [[[j%2==0][abs(i2c6xy[i]) < kX*s]]or[[j%2==1][2*kX*a[j]*b[j] <= i2c6xy[i] <= n/s**2/kX +kX*a[j]*b[j]]]]]]
        # let [min_AB6odd := min{(a[1+2*j]*b[1+2*j]) | [j:<-[0..<t///2]]}]
        # [min_AB6odd > 0]
        # !! [2*kX*s == n/s**2/kX -kX*min_AB6odd] => [kX == sqrt(n/s**2/(s+min_AB6odd))]
        # let [kX := sqrt(n/s**2/(2*s+min_AB6odd))]
        # [len(i2cs[i]) <= 1+floor(2*kX)]
        # [len(i2cs[i]) <= 1+floor(2*kX) == 1+floor_sqrt(4*n/s**2/(2*s+min_AB6odd))]
        # !! [gcd(n,s)][r:=n**j%s for all j] => [min min_AB6odd == 1]
        # [len(i2cs[i]) <= 1+floor_sqrt(4*n/s**2/(2*s+1))]
        # [len(i2cs[i]) == O(sqrt(n/s**3))]
      ]
    ]
  ]
]
  #原文:无[n%s =!= 0] 无法保证 [a1>0]
  #原文:[(c0,c1) := (0,(n*rv -r*a1)///s%s)] 但是 [a1==r_*rv%s =[未必]= r_*rv%s**2 == r_*rv]
  #原文:[2*a[j]*b[j] < (x*a[j] + y*b[j]) < n/s**2 +a[j]*b[j]] 使用『<』而非『<=』但是[a[t] == 0][b[0] == 0] #[j%2==1]:i2UB4c,i2LB4c
  #原文:(n**/3/s)而非(n/s**3)
===
proof:
  [[i:<-[1..=t]] -> [0 +[i%2==1] <= a[i] < a[i-1] +[i%2==1]]]
  [[i:<-[2..=t]] -> [q[i] > 0]]

  [a[t] == 0]
  [[i:<-[0..<t]] -> [a[i] > 0]]

  [[i:<-[0..=t]] -> [if i==t then [a[i] == 0] else [a[i] > 0]]]
    # (4.17)

  !! 归纳法:
  * [i==0]:
    [b[1]*a[0] -a[1]*b[0] == 1*s -a1*0 == s == s*(-1)**0]
  * [i>0][b[i]*a[i-1] -a[i]*b[i-1] == s*(-1)**(i-1)]:
    [b[i+1]*a[i] -a[i+1]*b[i] == (b[i-1] -q[i+1]*b[i])*a[i] -(a[i-1] -q[i+1]*a[i])*b[i] == b[i-1]*a[i] -a[i-1]*b[i] == -s*(-1)**(i-1) == s*(-1)**i]
    [b[i+1]*a[i] -a[i+1]*b[i] == s*(-1)**i]
  !! induction
  [[i:<-[0..<t]] -> [b[i+1]*a[i] -a[i+1]*b[i] == s*(-1)**i]]
    # (4.18)

  * [i==0]:
    [b0 == 0]
    [sign_of(b[i]) == 0]
  * [i==1]:
    [b1 == 1]
    [sign_of(b[i]) == +1 == (-1)**(i+1)]
  * [i>=2][[j:<-[0..<i]] -> [sign_of(b[j]) == if j==0 then 0 else (-1)**(j+1)]]:
    !! [[i:<-[2..=t]] -> [q[i] > 0]]
    [q[i] > 0]

    !! [[j:<-[0..<i]] -> [sign_of(b[j]) == if j==0 then 0 else (-1)**(j+1)]]
    [sign_of(b[i-2]) == (-1)**(i-2+1) == -(-1)**i]
    [sign_of(b[i-1]) == (-1)**(i-1+1) == (-1)**i]
    !! [b[i] := b[i-2] -q[i]*b[i-1]]
    !! [q[i] > 0]
    [sign_of(b[i]) == sign_of(b[i-2]) == -(-1)**i]
  !! induction
  [[i:<-[0..=t]] -> [sign_of(b[i]) == if i==0 then 0 else (-1)**(i+1)]]
    # (4.19)
  !! [t%2==0]
  !! [t > 0]
  [t >= 2]
  [sign_of(b[t]) == -1]
  [b[t] < 0]

  [x::uint][n%(x*s+r) == 0]:
    ?y :=> [y::uint][n == (x*s+r)*(y*s+r_)]
    [n == x*y*s**2 + (x*r_+y*r)*s + r*r_]
    [n =[%s**2]= (x*r_+y*r)*s + r*r_]
    [n - r*r_ =[%s**2]= (x*r_+y*r)%s*s]
    [n*rv - r*r_*rv =[%s**2]= (x*r_*rv+y*r*rv)%s*s =[%s**2]= (x*n*rv**2+y*1)%s*s]
    [(n*rv - r*r_*rv)///s =[%s]= (x*n*rv**2+y*1)]
    ...原文c1定义 无法继续推导...
    ...使用改动后的c1定义:
    [c1 == (n*rv - r*r_*rv)///s =[%s]= (x*n*rv**2+y*1)]
    [c1 =[%s]= (x*n*rv**2+y*1)]


    * [i==0]:
      [x*a[0] +y*b[0] == x*s +y*0 == x*s =[%s]= 0 == c[0]]
      [x*a[i] +y*b[i] =[%s]= c[i]]
    * [i==1]:
      !! [c1 =[%s]= (x*n*rv**2+y*1)]
      [x*a[1] +y*b[1] == x*(n*rv**2 %s) +y*1 =[%s]= c1]
      [x*a[i] +y*b[i] =[%s]= c[i]]
    * [i>=2][[j:<-[0..<i]] -> [x*a[j] +y*b[j] =[%s]= c[j]]]:
      [x*a[i] +y*b[i]
      == x*(a[i-2] -q[i]*a[i-1]) +y*(b[i-2] -q[i]*b[i-1])
      == x*a[i-2] +y*b[i-2] -q[i]*(x*a[i-1] +y*q[i]*b[i-1])
      =[%s]= c[i-2] -q[i]*c[i-1]
      == c[i]
      ]
      [x*a[i] +y*b[i] =[%s]= c[i]]
    !! induction
    [[i:<-[0..=t]] -> [x*a[i] +y*b[i] =[%s]= c[i]]]
        #接下来，找出c[i]的取值范围，以便去掉『%s』

    !! [a0 == s]
    !! [s > 0]
    [a0 > 0]
    !! [b0 == 0]
    !! [x >= 0]
    !! [a0 > 0]
    [x*a[0] + y*b[0] == x*a0 >= 0]

    !! [a[t] == 0]
    !! [y >= 0]
    !! [b[t] < 0]
    [x*a[t] + y*b[t] == y*b[t] <= 0]

    !! [t%2==0]
    !! [t > 0]
    ### ?j :=> [j:<-[0,2..<t]][j%2==0][x*a[j] + y*b[j] >= 0][x*a[j+2] + y*b[j+2] <= 0]
    ?k :=> [k:<-[0..<t///2]][x*a[2*k] + y*b[2*k] >= 0][x*a[2*k+2] + y*b[2*k+2] <= 0]

    [2*k+2 <= t]
    [2*k+1 < t]
    !! [[i:<-[0..=t]] -> [if i==t then [a[i] == 0] else [a[i] > 0]]]
    [a[2*k+1] > 0]
    [a[2*k] > 0]
    [a[2*k+2] >= 0]

    !! [[i:<-[0..=t]] -> [sign_of(b[i]) == if i==0 then 0 else (-1)**(i+1)]]
    [b[2*k] <= 0]
    [b[2*k+1] > 0]
    [b[2*k+2] < 0]

    !! [[i:<-[0..<t]] -> [b[i+1]*a[i] -a[i+1]*b[i] == s*(-1)**i]]
    [b[2*k+1]*a[2*k] -a[2*k+1]*b[2*k] == s*(-1)**(2*k) == s]
    [b[2*k+2]*a[2*k+1] -a[2*k+2]*b[2*k+1] == s*(-1)**(2*k+1) == -s]

    [x*a[2*k] + y*b[2*k] >= +s][x*a[2*k+2] + y*b[2*k+2] <= -s]:
      #改进版:『[x*a[2*k] + y*b[2*k] >= +sU == +s*kU][x*a[2*k+2] + y*b[2*k+2] <= -sL == -s*kL]:』
      [x*a[2*k]
      !! [y >= 0]
      !! [b[2*k] <= 0]
      >= x*a[2*k] + y*b[2*k]
      !! [x*a[2*k] + y*b[2*k] >= +s]
      #改进版:『[x*a[2*k] + y*b[2*k] >= +sU == +s*kU]』
      >= +s
      !! [b[2*k+1]*a[2*k] -a[2*k+1]*b[2*k] == s]
      == b[2*k+1]*a[2*k] -a[2*k+1]*b[2*k]
      !! [b[2*k] <= 0]
      !! [a[2*k+1] > 0]
      >= b[2*k+1]*a[2*k]
      #改进版:『>= kU*b[2*k+1]*a[2*k]』
      ]
      [x*a[2*k] >= b[2*k+1]*a[2*k]]
      !! [a[2*k] > 0]
      [x >= b[2*k+1]]
      #改进版:『[x >= kU*b[2*k+1]]』


      [y*b[2*k+2]
      !! [x >= 0]
      !! [a[2*k+2] >= 0]
      <= x*a[2*k+2] + y*b[2*k+2]
      !! [x*a[2*k+2] + y*b[2*k+2] <= -s]
      #改进版:『[x*a[2*k+2] + y*b[2*k+2] <= -sL == -s*kL]』
      <= -s
      !! [b[2*k+2]*a[2*k+1] -a[2*k+2]*b[2*k+1] == -s]
      == b[2*k+2]*a[2*k+1] -a[2*k+2]*b[2*k+1]
      !! [a[2*k+2] >= 0]
      !! [b[2*k+1] > 0]
      <= b[2*k+2]*a[2*k+1]
      #改进版:『<= kL*b[2*k+2]*a[2*k+1]』
      ]
      [y*b[2*k+2] <= b[2*k+2]*a[2*k+1]]
      !! [b[2*k+2] < 0]
      [y >= a[2*k+1]]
      #改进版:『[y >= kL*a[2*k+1]]』

      !! [x >= b[2*k+1]]
      !! [y >= a[2*k+1]]
      !! [a[2*k+1] > 0]
      !! [b[2*k+1] > 0]
      [x*a[2*k+1] + y*b[2*k+1] >= 2*a[2*k+1]*b[2*k+1]]
      #改进版:『[x*a[2*k+1] + y*b[2*k+1] >= (kU+kL)*a[2*k+1]*b[2*k+1]]』
      #or:改进版:『[kL*x*a[2*k+1] + kU*y*b[2*k+1] >= 2*kL*kU*a[2*k+1]*b[2*k+1]]』

      !! [x >= b[2*k+1]]
      !! [y >= a[2*k+1]]
      [(x -b[2*k+1])*(y -a[2*k+1]) >= 0]
      #改进版:『[(x -kU*b[2*k+1])*(y -kL*a[2*k+1]) >= 0]』
      [x*a[2*k+1] + y*b[2*k+1] <= x*y +a[2*k+1]*b[2*k+1]]
      #改进版:『[kL*x*a[2*k+1] + kU*y*b[2*k+1] <= x*y +kL*kU*a[2*k+1]*b[2*k+1]]』
      !
      !! [n == x*y*s**2 + (x*r_+y*r)*s + r*r_]
      [n >= x*y*s**2]
      !! [s > 0]
      [x*y <= n/s**2]
      [x*a[2*k+1] + y*b[2*k+1] <= n/s**2 +a[2*k+1]*b[2*k+1]]
      #改进版:『[kL*x*a[2*k+1] + kU*y*b[2*k+1] <= n/s**2 +kL*kU*a[2*k+1]*b[2*k+1]]』
      [2*a[2*k+1]*b[2*k+1] <= x*a[2*k+1] + y*b[2*k+1] <= n/s**2 +a[2*k+1]*b[2*k+1]]
      #改进版:『[2*kL*kU*a[2*k+1]*b[2*k+1] <= kL*x*a[2*k+1] + kU*y*b[2*k+1] <= n/s**2 +kL*kU*a[2*k+1]*b[2*k+1]]』
        #c[k]解压范围:『<=』
        #???bug???原文:『<』:[2*a[2*k+1]*b[2*k+1] < x*a[2*k+1] + y*b[2*k+1] < n/s**2 +a[2*k+1]*b[2*k+1]]
    [[[x*a[2*k] + y*b[2*k] >= +s][x*a[2*k+2] + y*b[2*k+2] <= -s]] -> [2*a[2*k+1]*b[2*k+1] <= x*a[2*k+1] + y*b[2*k+1] <= n/s**2 +a[2*k+1]*b[2*k+1]]]
    #改进版:『[kX==kL==kU] => [2*kX*a[2*k+1]*b[2*k+1] <= x*a[2*k+1] + y*b[2*k+1] <= n/s**2/kX +kX*a[2*k+1]*b[2*k+1]]』
    [[?[j:<-[0..=t]] -> [[j%2==0][abs(x*a[j] + y*b[j]) < s]]]or[?[j:<-[0..=t]] -> [[j%2==1][2*a[j]*b[j] <= (x*a[j] + y*b[j]) <= n/s**2 +a[j]*b[j]]]]]
    [?[j:<-[0..=t]] -> [[[j%2==0][abs(x*a[j] + y*b[j]) < s]]or[[j%2==1][2*a[j]*b[j] <= (x*a[j] + y*b[j]) <= n/s**2 +a[j]*b[j]]]]]
    #改进版:『[kX==kL==kU] => [?[j:<-[0..=t]] -> [[[j%2==0][abs(x*a[j] + y*b[j]) < kX*s]]or[[j%2==1][2*kX*a[j]*b[j] <= (x*a[j] + y*b[j]) <= n/s**2/kX +kX*a[j]*b[j]]]]]』
    [[i:<-[0..=t]] -> [x*a[i] +y*b[i] =[%s]= c[i]]]

  [@[x::uint] -> [n%(x*s+r) == 0] -> [y := n///(x*s+r) %s] -> [[[i:<-[0..=t]] -> [x*a[i] +y*b[i] =[%s]= c[i]]][?[j:<-[0..=t]] -> [[[j%2==0][abs(x*a[j] + y*b[j]) < s]]or[[j%2==1][2*a[j]*b[j] <= (x*a[j] + y*b[j]) <= n/s**2 +a[j]*b[j]]]]]]]
        #c[k]压缩值 暨 #c[k]解压范围
  #改进版:『[@[x::uint] -> [n%(x*s+r) == 0] -> [y := n///(x*s+r) %s] -> @[kX::real] -> [kX > 0] -> [[[i:<-[0..=t]] -> [x*a[i] +y*b[i] =[%s]= c[i]]][?[j:<-[0..=t]] -> [[[j%2==0][abs(x*a[j] + y*b[j]) < kX*s]]or[[j%2==1][2*kX*a[j]*b[j] <= (x*a[j] + y*b[j]) <= n/s**2/kX +kX*a[j]*b[j]]]]]]]』
      # let [min_AB6odd := min{(a[1+2*j]*b[1+2*j]) | [j:<-[0..<t///2]]}]
      # [min_AB6odd > 0]
      # !! [kX*s == n/s**2/kX -kX*min_AB6odd] => [kX == sqrt(n/s**2/(s+min_AB6odd))]
      # let [kX := sqrt(n/s**2/(s+min_AB6odd))]
      # [len(i2cs[i]) <= 1+floor(2*kX)]
      # [len(i2cs[i]) <= 1+floor(2*kX) == 1+floor_sqrt(4*n/s**2/(2*s+min_AB6odd))]
      # !! [gcd(n,s)][r:=n**j%s for all j] => [min min_AB6odd == 1]
      # [len(i2cs[i]) <= 1+floor_sqrt(4*n/s**2/(2*s+1))]
      # [len(i2cs[i]) == O(sqrt(n/s**3))]
  #This completes the proof of correctness.
  #以上是 正确性证明
  #以下是 耗时:
  #bug:[t <= 1+log_((1+sqrt5)/2;s)]
  [t <= 2+log_((1+sqrt5)/2;sqrt5*s)]
      # 『+1』: Fibonacci_number:交替大小 比之于 inv_golden_ratio**n/sqrt5
      #     [fibonacci[n] == (inv_golden_ratio**n -neg_golden_ratio**n) / (inv_golden_ratio**1-neg_golden_ratio**1)]
      # 再『+1』: odd_i调整，强行保证[t%2==0]#至多发生一次并且下一步结束
  [t-1 <= log_(inv_golden_ratio;s) < ceil_log_(76;(sqrt5*s)**9) == ceil_log_(76;s**9 * 5**4*sqrt5) < ceil_log_(76;s**9 * 625*3)]
      #view others/数学/math_constants/golden_ratio.txt
          #[[x > 1] -> [floor_log_(47;x**8) < log_(inv_golden_ratio; x) < ceil_log_(76;x**9)]]
            # [绝对误差{x} ~< 2+0.00032756*ln(x)]
            # [相对误差{x} ~< 0.0006806944025241034 +2/ln(x)]
  [t-1 < ceil_log_(76;s**9 * 1875)]
  [t <= ceil_log_(76;1875*s**9)]

  [t == O(ln(n))] # 辗转相除法 循环次数
  !! [t <= 2+log_((1+sqrt5)/2;sqrt5*s)]
  [t <= 2+log_((1+sqrt5)/2;sqrt5)+log_((1+sqrt5)/2;s) ~= 3.6722759381845549 +log_((1+sqrt5)/2;s) < 3.672276 +log_((1+sqrt5)/2;s)]
  [t-3.672276 <= log2(s) / log2((1+sqrt5)/2) ~= log2(s) / 0.6942419136306174]
  [2**((t-3.672276)*0.6942) <= s]
  * [t-3.672276 > 0]:
    [s**(3/2) >= 2**((t-3.672276)*0.6942*3/2) > 2**((t-3.672276)*1.0413) > 2**(t-3.672276)]
    [s**(3/2) > 2**(t-3.672276)]
  * [t-3.672276 <= 0]:
    [s**(3/2) > 1 >= 2**(t-3.672276)]
    [s**(3/2) > 2**(t-3.672276)]
  [s**(3/2) > 2**(t-3.672276) > 2**t /12.748681]
  #bug:[s**(3/2) > 2**t]

  [(i,c[i],c) :=> 方程组(4.16)中的c取值(c[i]解压值) 存在]:
    * [i%2==0]:
      [abs(c) < s]
      !! [c =[%s]= c[i]]
      方程组(4.16)中的c取值(c[i]解压值) 至多2个

    * [i%2==1]:
      !! [i%2==1]
      [a[i] > 0]
      [b[i] > 0]
      [a[i]*b[i] > 0]

      [2*a[i]*b[i] <= c <= a[i]*b[i] + n/s**2]
      [a[i]*b[i] <= n/s**2]
      [0 < a[i]*b[i] <= n/s**2]
      [0 <= n/s**2]
      [c取值范围 <= a[i]*b[i] +n/s**2 -2*a[i]*b[i] == n/s**2 -a[i]*b[i] <= n/s**2]
      !! [c =[%s]= c[i]]
      方程组(4.16)中的c取值(c[i]解压值) 至多(1+floor(n/s**3))个
        => O((n/s**3)*t)
        => O((n/s**3)*ln(n))

  [s**3 >= n]:
    每个i => 方程组(4.16)中的c取值(c[i]解压值) 至多 2个
    * [i%2==0]:
      !! [abs(c) < s]
      [abs(c) <= 2*s]
    * [i%2==1]:
      !! [s**3 >= n]
      [s >= n/s**2]
      !! [a[i]*b[i] <= n/s**2]
      [0 < a[i]*b[i] <= s]
      [0 < 2*a[i]*b[i] <= c <= a[i]*b[i] + n/s**2 <= s +s]
      [0 < c <= 2*s]
      [abs(c) <= 2*s]
    [abs(c) <= 2*s]

    [B := max{abs(b[i]) | [i:<-[0..=t]]}]
    !! [q[i] > 0]
    !! [t%2==0]
    [B == -b[t]]
    !! [b0 == 1]
    !! [q[i] >= 1]
    [B <= b0*II[(1+q[i]) | [i:<-[2..=t]]] <= 2**t * II[q[i] | [i:<-[2..=t]]]]
    !! [0 <= a[i] == a[i-2] -q[i]*a[i-1]]
    [a[i-2] >= q[i]*a[i-1]]
    [s == a0 >= q2*a1 >= q2*q3*a2 >= ... >= q2*...*q[t]*a[t-1] >= II[q[i] | [i:<-[2..=t]]]]
    [B <= 2**t*s]
    #bug:[s**(3/2) > 2**t]
            !! [s**(3/2) > 2**t]
            [B < s**(5/2)]
    !! [s**(3/2) > 2**(t-3.672276) > 2**t /12.748681]
    [2**t < 12.748681*s**(3/2)]
    [B <= 2**t*s < 12.748681*s**(3/2)*s == 12.748681*s**(5/2)]
    [B < 12.748681*s**(5/2)]

    解方程组:
      # (4.16)
      x*a[i] +y*b[i] == c
      (x*s + r)*(y*s + r_) == n
      ==>>:
      x*s*a[i] +y*s*b[i] == c*s
      ==>>:
      (x*s*a[i] + r*a[i])*(y*s*b[i] + r_*b[i]) == n*a[i]*b[i]
      (x*s*a[i] + r*a[i]) + (y*s*b[i] + r_*b[i]) == c*s + r*a[i] + r_*b[i]
      [根集纟方程组:={(x*s*a[i] + r*a[i]), (y*s*b[i] + r_*b[i])}]
      [根集纟方程组=={(x*s + r)*a[i], (y*s + r_)*b[i]}]
      bug:原文:DET = (c*s + r*a[i] + r_*b[i])**2 -4*a[i]*b[i]
      改为:DET = (c*s + r*a[i] + r_*b[i])**2 -4*n*a[i]*b[i]
      !! [abs(c) <= 2*s]
      !! [B < s**(5/2)]
      [O(sqrt{DET}) == O(sqrt{s**7}) == O(sqrt{n**7})]
end-proof
===
Remark.
  If s < n**/3, Algorithm 4.2.11 still works, but the number of square root steps is then O(n**/3*s**-1*ln(n)).
    # 应当是O((n/s**3)*ln(n))
    #   ???bug??? 原文:O(cbrt(n/s**3)*ln(n))
    #   我:改进版:最糟况态[min_AB6odd==1]=>最优kX=>O(sqrt(n/s**3)*ln(n))
  Note that if F in Theorem 4.2.10 is such that F/n**/3 is not very small, we can use that theorem and Algorithm 4.2.11 as a speedy primality test.
      In general, we can use Algorithm 4.2.11 in a primality test if we have learned that each prime factor of n is congruent to r[i](mod s) for some i ∈ [1,k], where each gcd(r[i],s) = 1, 0 < r[i] < s, and s ≥ n**/3.
      Then with k calls to Algorithm 4.2.11 we will either find a nontrivial factor of n, or failing this, prove that n is prime.
      However, if s ≥ √n, there is no need to use Algorithm 4.2.11.
      Indeed, if none of the integers r[i] are proper factors of n, then every prime dividing n exceeds √n, so n is prime.

===
]]
]]]]]

'#'; __doc__ = r'#'
>>> list_divisors_in_residue_class_(60, 7, 3)
(3, 10)
>>> list_divisors_in_residue_class_(60, 7, 3, dup_ok=True)
(3, 3, 10, 10)
>>> [*iter_divisors_in_residue_class_(60, 7, 3)]
[3, 3, 10, 10]
>>> [*iter_divisors_in_residue_class_(60, 7, 3, dup_ko=True)]
[3, 10]
>>> for x in iter_divisors_in_residue_class_(60, 7, 3, with_more_info=True):
...     print(x)
...     #(d, ((n,s,r,r_), (t,i,ai,bi,ci), (len(cs6i), j4c, c6ij,x,y), (d,_d)))
(3, ((60, 7, 3, 6), (4, 0, 7, 0, 0), (1, 0, 0, 0, 2), (3, 20)))
(3, ((60, 7, 3, 6), (4, 2, 1, -3, -6), (2, 0, -6, 0, 2), (3, 20)))
(10, ((60, 7, 3, 6), (4, 2, 1, -3, -6), (2, 1, 1, 1, 0), (10, 6)))
(10, ((60, 7, 3, 6), (4, 4, 0, -7, -14), (1, 0, 0, 1, 0), (10, 6)))


[[
test:dynamic_choose_kX
===
py_adhoc_call   seed.math.divisors_in_residue_classes   @list_divisors_in_residue_class_  =1645504791793036001885786959444903773919505766647628164998185179    =1152921504606847009     =10698823624572768
    (1532495754953053534987034606266580480262417649720213577,)

===
py_adhoc_call   seed.math.divisors_in_residue_classes   @list_divisors_in_residue_class_  =1645504791793036001885786959444903773919505766647628164998185179    =1152921504606847009     =856845977202
    (1237940102696063920555167113,)


===
<<==:
prepare data 4 test:dynamic_choose_kX
    # [len(i2cs[i]) == O(sqrt(n/s**3))]
    [sqrt(n/s**3) ~= 2**20]:
        [(n/s**3) ~= 2**40]
        [s ~= 2**60]:
            [n ~= 2**220]
[s:=1152921504606847009]
[n:=1645504791793036001885786959444903773919505766647628164998185179]
[d1:=1532495754953053534987034606266580480262417649720213577]
[d2:=1237940102696063920555167113]
# [r1:=d1%s]
# [r2:=d2%s]
[r1:=10698823624572768]
[r2:=856845977202]

<<==:
next_probable_prime ='2**60'
    115292150460684700
iter_next_probable_primes ='2**30' | head
    1073741827
    1073741831
    1073741833
    1073741839
    1073741843
    1073741857
    1073741891
    1073741909
    1073741939
    1073741953

[1073741827*1073741831*1073741833*1073741839*1073741843*1073741857*1073741891 == 1645504791793036001885786959444903773919505766647628164998185179]
    .bit_length() == 211
[1         *1073741831*1073741833*1073741839*1073741843*1073741857*1073741891 == 1532495754953053534987034606266580480262417649720213577]
    .bit_length() == 181
[1         *1073741831*1         *1073741839*1         *1073741857*         1 == 1237940102696063920555167113]
    .bit_length() == 91

]]

[[
===
py_adhoc_call   seed.math.divisors_in_residue_classes   @_test  +verbose =20
    ...
    732:(20, 19, 18):()
    733
    ok!
===
py_adhoc_call   seed.math.divisors_in_residue_classes   @_test  +verbose =50
    ...
    12177:(50, 49, 48):()
    12178
    ok!
===
py_adhoc_call   seed.math.divisors_in_residue_classes   @_test  +verbose =100
    ...
    99308:(100, 99, 98):()
    99309
    ok!
===
py_adhoc_call   seed.math.divisors_in_residue_classes   @_test  +verbose =200 +_fixed_kX_eq1 +force_fancy
py_adhoc_call   seed.math.divisors_in_residue_classes   @_test  +verbose =200 -_fixed_kX_eq1 +force_fancy
py_adhoc_call   seed.math.divisors_in_residue_classes   @_test  +verbose =200 -_fixed_kX_eq1 -force_fancy
    ...
    802754:(200, 199, 198):()
    802755
    ok! global:fixed_kX_eq1 # [kw:_fixed_kX_eq1=True][force_fancy=True]
    ok! allow:dynamic_choose_kX # [kw:_fixed_kX_eq1=False][force_fancy=True]
    ok! allow:dynamic_choose_kX # [kw:_fixed_kX_eq1=False][force_fancy=False]
===
py_adhoc_call   seed.math.divisors_in_residue_classes   @_tests  +verbose ='range(3,1+10)' ='range(1+10,1+15)'
    ... ...
    79:(10, 9, 8):()
    continue...
    ... ...
    296:(15, 14, 13):()
    continue...
    297
    ok!
===
py_adhoc_call   seed.math.divisors_in_residue_classes   @_tests  +verbose   ='range(3,1+20)'   ='range(1+20,1+50)'   ='range(1+50,1+100)'   ='range(1+100,1+200)'
    ... ...
    732:(20, 19, 18):()
    continue...
    ... ...
    12177:(50, 49, 48):()
    continue...
    ... ...
    99308:(100, 99, 98):()
    continue...
    ... ...
    802754:(200, 199, 198):()
    continue...
    802755
    ok!

===
]]


]]]'''#'''
__all__ = r'''
iter_divisors_in_residue_class_
    list_divisors_in_residue_class_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.debug.print_err import print_err
    from seed.math.list_all_factors5factorization_ import list_all_factors5factorization_
    from seed.math.factor_pint_as_pefect_power_ import may_perfect_kth_root_, may_perfect_sqrt_, may_perfect_cbrt_
    from seed.math.perfect_div import may_perfect_div, tmay_perfect_div
    from seed.math.perfect_div import perfect_div, perfect_kth_root_
    from seed.math.floor_ceil import ceil_div, floor_sqrt
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.inv_mod__py_ import inv_mod__py_
    from seed.math.gcd import gcd, are_coprime# gcd_many
    from math import log, ceil, floor

    #view others/数学/math_constants/golden_ratio.txt
        #[[x > 1] -> [floor_log_(47;x**8) < log_(inv_golden_ratio; x) < ceil_log_(76;x**9)]]
          # [绝对误差{x} ~< 2+0.00032756*ln(x)]
          # [相对误差{x} ~< 0.0006806944025241034 +2/ln(x)]
    from seed.math.floor_ceil_log__via_div_log2 import FloorLogarithm, floor_log__via_div_log2_, floor_ceil_log__via_div_log2_, ceil_log__via_div_log2_
        #.class FloorLogarithm:
        #.    def __new__(cls, base4logarithm, /):
        #.    def floor_ceil_log_(sf, x, /, *, with_floor_pow:bool):
        #.    def ceil_log_(sf, x, /, *, with_floor_pow:bool):
        #.    def floor_log_(sf, x, /, *, with_floor_pow:bool):

    from fractions import Fraction
    from itertools import count #islice
#.    from functools import cached_property
___end_mark_of_excluded_global_names__0___ = ...
if 0:
    _tests
    _test
    #
    _test1_ex_
    #
    _gen_args5may_max_n_or_ns_
    _gen_args5ns_
    _gen_args6n_
    _gen_args6nm_
    _iter_ms6n_
    _iter_rs6nm_

def _tests(*nss, verbose=False, j0=0, _fixed_kX_eq1=False, force_fancy=False):
    j = j0
    for ns in nss:
        ns = iter(ns)
        j = _test(ns, verbose=verbose, j0=j, _fixed_kX_eq1=_fixed_kX_eq1, force_fancy=force_fancy)
        input('continue...')
    j
    return j
def _test(may_max_n_or_ns=None, /, *, verbose=False, j0=0, _fixed_kX_eq1=False, force_fancy=False):
    prev_n = -1
    ds4n = None
    j = j0-1
    for j, (n, m, r) in enumerate(_gen_args5may_max_n_or_ns_(may_max_n_or_ns), j0):
        if verbose:print_err(j, (n, m, r), sep=':')
        if not n == prev_n:
            prev_n = n
            ds4n = list_all_factors5factorization_(n)
        ds4n
        ds4n6r = _test1_ex_(n, m, r, ds4n, _fixed_kX_eq1, force_fancy)
        if verbose:print_err(j, (n, m, r), ds4n6r, sep=':')
    else:
        j += 1
    j
    return j
def _test1_ex_(n, m, r, ds4n, _fixed_kX_eq1, force_fancy, /):
    ds4n6r = tuple(d for d in ds4n if d%m == r)
    ds = list_divisors_in_residue_class_(n, m, r, _fixed_kX_eq1=_fixed_kX_eq1, force_fancy=force_fancy)
    assert ds == ds4n6r, ((n, m, r), (ds4n6r, ds))
        # +force_fancy => ^AssertionError: ((5, 3, 1), ((1,), (-5, 1)))
        # -force_fancy => ^AssertionError: ((11, 2, 1), ((1, 11), (1,)))
        # -force_fancy => ^AssertionError: ((46, 4, 1), ((1,), (1, 23)))
    return ds4n6r
#def _test1(n, m, r, /):
def _gen_args5may_max_n_or_ns_(may_max_n_or_ns, /):
    match may_max_n_or_ns:
        case None:
            ns = count(3)
        case int(max_n):
            ns = range(3, 1+max_n)
        case ns:
            pass
    ns = iter(ns)
    return _gen_args5ns_(ns)
def _gen_args5ns_(ns, /):
    'Iter n -> Iter (n, m, r)'
    for n in ns:
        check_int_ge(3, n)
        yield from _gen_args6n_(n)
def _gen_args6n_(n, /):
    'n -> Iter (n, m, r)'
    for m in _iter_ms6n_(n):
        yield from _gen_args6nm_(n, m)
def _iter_ms6n_(n, /):
    'n -> Iter m'
    check_int_ge(3, n)
    for m in range(2, n):
        if not n%m == 0:
            yield m
def _gen_args6nm_(n, m, /):
    'n -> m -> Iter (n, m, r)'
    for r in _iter_rs6nm_(n, m):
        yield (n, m, r)
def _iter_rs6nm_(n, m, /):
    'n -> m -> Iter r'
    check_int_ge(2, m)
    check_int_ge(1+m, n)
    if n%m == 0:raise ValueError(n,m)
    for r in range(1, m):
        if are_coprime(m,r):
            yield r

def list_divisors_in_residue_class_(n, m, r, /, *, dup_ok=False, _fixed_kX_eq1=False, force_fancy=False):
    return tuple(sorted(iter_divisors_in_residue_class_(n, m, r, dup_ko=not dup_ok, _fixed_kX_eq1=_fixed_kX_eq1, force_fancy=force_fancy)))
def iter_divisors_in_residue_class_(n, m, r, /, *, dup_ko=False, with_more_info=False, _fixed_kX_eq1=False, force_fancy=False):
    'n/int{3..} -> m/int{2..<n}{[n%s=!=0]} -> r/int{1..<m}{[gcd(r,s)==1]} -> Iter (d/int{[d>0][d%m==r][n%d==0]} if not with_more_info else (d, ((n,s,r,r_), (t,i,ai,bi,ci), (len(cs6i), j4c, c6ij,x,y), (d,_d)))) # [0 < r < m < n] # [平常版[kX:=1]:O(max(1,(n/s**3)**/1)*ln(n)) > 私版最优kX:O(max(1,(n/s**3)**/2)*ln(n)) > 原文提及:O(max(1,(n/s**3)**/3)*ln(n))]'
    return (_iter_divisors_in_residue_class__dup_ko_ if dup_ko else _iter_divisors_in_residue_class__dup_ok_)(n, m, r, with_more_info, _fixed_kX_eq1, force_fancy)
def _iter_divisors_in_residue_class__dup_ko_(n, m, r, with_more_info, _fixed_kX_eq1, force_fancy, /):
    s = set()
    for d in _iter_divisors_in_residue_class__dup_ok_(n, m, r, with_more_info, _fixed_kX_eq1, force_fancy):
        if not d in s:
            yield d
            s.add(d)
# !! [1/φ == inv_phi == inv_golden_ratio == (1+sqrt5)/2 ~= 1.618033988749895]
_inv_golden_ratio = 1.618033988749895
_76 = FloorLogarithm(76)
def _iter_divisors_in_residue_class__dup_ok_(n, s, r, with_more_info, _fixed_kX_eq1, force_fancy, /):
    nsr = (n, s, r)
    check_int_ge(1, r)
    check_int_ge(1+r, s)
    check_int_ge(1+s, n)
    # [n > s > r > 1]
    if n%s == 0:raise ValueError(n,s)
    #if not gcd(s,r) == 1:raise ValueError(s,r)
    if not are_coprime(s,r):raise ValueError(s,r)
    ######
    force_fancy = force_fancy or with_more_info
    if not force_fancy:
        max1_x = max1_y = 5
    ######
    if not force_fancy:
        if n < (max1_d:=max1_x*s+r):
            #for d in range(r, max1_d, s):
            for d in range(r, 1+n, s):
                if n%d == 0:
                    yield d
            return
    ######
    # !! [s > r > 1]
    # [s >= 3]
    # !! [[x > 1] -> [floor_log_(47;x**8) < log_(inv_golden_ratio; x) < ceil_log_(76;x**9)]]
        #view others/数学/math_constants/golden_ratio.txt
    #########
    #bug:
        #xxx# !! [t <= log_((1+sqrt5)/2;s)]
        #xxx# [t <= log_(inv_golden_ratio;s) < ceil_log_(76;s**9)]
        #xxx#UB4t = -1+_76.ceil_log_(s**9, with_floor_pow=False)
            # ^Exception('bad UB4t:', UB4t, nsr)
                # ^Exception: ('bad UB4t:', 1, (3, 2, 1), [2, 1])
    #########
    #bug:
        #xxx# !! [t <= 1+log_((1+sqrt5)/2;s)]
        #xxx# [t-1 <= log_(inv_golden_ratio;s) < ceil_log_(76;s**9)]
        #xxx# [t-1 < ceil_log_(76;s**9)]
        #xxx# [t <= ceil_log_(76;s**9)]
        #xxx# UB4t = _76.ceil_log_(s**9, with_floor_pow=False)
                # ^Exception: ('bad UB4t:', 3, (5, 3, 1), [3, 2, 1, 1])
    #########
    #.UB4t = _76.ceil_log_(s**9, with_floor_pow=False)
    #.777; UB4t += (UB4t&1)
    #########
    # !! [t <= 2+log_((1+sqrt5)/2;sqrt5*s)]
    #   『+1』: Fibonacci_number:交替大小 比之于 inv_golden_ratio**n/sqrt5
    #       [fibonacci[n] == (inv_golden_ratio**n -neg_golden_ratio**n) / (inv_golden_ratio**1-neg_golden_ratio**1)]
    #   再『+1』: odd_i调整，强行保证[t%2==0]#至多发生一次并且下一步结束
    # [t-1 <= log_(inv_golden_ratio;s) < ceil_log_(76;(sqrt5*s)**9) == ceil_log_(76;s**9 * 5**4*sqrt5) < ceil_log_(76;s**9 * 625*3)]
    # [t-1 < ceil_log_(76;s**9 * 1875)]
    # [t <= ceil_log_(76;1875*s**9)]
    UB4t = 2+_76.ceil_log_(1875*s**9, with_floor_pow=False)
    #########

    rv = inv_mod__py_(s, r) # r**-1%s
        #^ValueError: base is not invertible for the given modulus
    assert rv*r%s == 1
    r_ = n*rv%s
    ######
    if not force_fancy:
        if n < (max1_dx:=max1_x*s+r)*(max1_dy:=max1_y*s+r_):
            for d in range(r, min(1+n, max1_dx), s):
                if n%d == 0:
                    yield d

            #bug:if r == r_: return
                # ^AssertionError: ((11, 2, 1), ((1, 11), (1,)))
            for _d in range(r_, max1_dy, s):
                (d, _0) = divmod(n, _d)
                #bug:if _0 == 0 and not d < max1_dx:
                    # ^AssertionError: ((46, 4, 1), ((1,), (1, 23)))
                if _0 == 0 and not d < max1_dx and d%s == r:
                    yield d
            return
    ######
    (a0,a1) = (s, r_*rv%s)
    (b0,b1) = (0, 1)
    (c0,c1) = (0, perfect_div(n*rv -r*r_*rv, s)%s)
    (q0,q1) = (None, None)

    #assert not a0 == 0
    #assert not a1 == 0
    assert 0 < a1 < a0
    ls4Q = [q0, q1]
    ls4A = [a0, a1]
    ls4B = [b0, b1]
    ls4C = [c0, c1]
    for i in range(2, 1+UB4t):
        # [?[t::uint] -> [[t>=2][a[t]==0][@[i:<-2..=t] -> [(q[i],a[i]-[i%2==1]) := divmod(a[i-2]-[i%2==1],a[i-1])]]]]
        odd_i = (i&1) == 1
        (qi, ai) = divmod(ls4A[-2] -odd_i, ls4A[-1])
        777; ai += odd_i
        # [@[i:<-2..=t] -> [b[i] := b[i-2] -q[i]*b[i-1]][c[i] := c[i-2] -q[i]*c[i-1]]]
        bi = ls4B[-2] -qi*ls4B[-1]
        ci = ls4C[-2] -qi*ls4C[-1]
        ls4Q.append(qi)
        ls4A.append(ai)
        ls4B.append(bi)
        ls4C.append(ci)
        if ai == 0:
            t = i
            break
    else:
        raise Exception('bad UB4t:', UB4t, nsr, ls4A)
            # ^Exception: ('bad UB4t:', 1, (3, 2, 1), [2, 1])
            #   => bug: 多出『-1+』
            # ^Exception: ('bad UB4t:', 3, (5, 3, 1), [3, 2, 1, 1])
            #   => bug: odd_i [r==0] ==>> [q-=1][r:=a[i-1]]
            #       这样一来 下一步就是0，即[t==i+1]
            #       添上『1+』，但考虑到[t%2==0]:只有奇数UB4t才涨一

    assert len(ls4Q) == 1+t
    assert len(ls4A) == 1+t
    assert len(ls4B) == 1+t
    assert len(ls4C) == 1+t

    B = max(map(abs, ls4B))
    assert B == -ls4B[t]
    assert t&1 == 0
    # [s**(3/2) > 2**(t-3.672276) > 2**t /12.748681]
    # [[s**3 >= n] -> [B <= 2**t*s < 12.748681*s**(5/2)]]
    s3 = s**3
    assert 163*s3 > (1<<(2*t)), (nsr, s3, t, 163*s3, (1<<(2*t)), ls4A)
    assert not s3 >= n or B**2 < 163*s**5

    # [[i:<-[2..=t]] -> [q[i] > 0]]
    assert all(ls4Q[i] > 0 for i in range(2, 1+t))

    # [[i:<-[1..=t]] -> [0 +[i%2==1] <= a[i] < a[i-1] +[i%2==1]]]
    assert all(0 < ls4A[i] <= ls4A[i-1] for i in range(1, 1+t, 2))
        # [odd i]
    assert all(0 <= ls4A[i] < ls4A[i-1] for i in range(2, 1+t, 2))
        # [even i] except 0

    # [[i:<-[0..=t]] -> [if i==t then [a[i] == 0] else [a[i] > 0]]]
    assert all(ls4A[i] > 0 for i in range(t))
    assert ls4A[t] == 0

    # [[i:<-[0..=t]] -> [sign_of(b[i]) == if i==0 then 0 else (-1)**(i+1)]]
    assert ls4B[0] == 0
    assert all(ls4B[i] > 0 for i in range(1, 1+t, 2))
        # [odd i]
    assert all(ls4B[i] < 0 for i in range(2, 1+t, 2))
        # [even i] except 0

    # [[i:<-[0..<t]] -> [b[i+1]*a[i] -a[i+1]*b[i] == s*(-1)**i]]
    assert all(ls4B[i+1]*ls4A[i] -ls4A[i+1]*ls4B[i] == -s for i in range(1, t, 2))
        # [odd i]
    assert all(ls4B[i+1]*ls4A[i] -ls4A[i+1]*ls4B[i] == +s for i in range(0, t, 2))
        # [even i] except t

    # [@[i:<-[0..=t]] -> [i2LB4c[i] := if [i%2==0] then -(ceil(kX*s)-1) else ceil(2*kX*a[i]*b[i])]]
    # [@[i:<-[0..=t]] -> [i2UB4c[i] := if [i%2==0] then +(ceil(kX*s)-1) else floor(kX*a[i]*b[i] + n/s**2/kX)]]
    # [@[i:<-[0..=t]] -> [i2cs[i] := range(c[i]+ceil_div(i2LB4c[i]-c[i],s)*s, 1+i2UB4c[i], s)]]
        # [i2cs[i] := {c | [[c::int][c =[%s]= c[i]][i2LB4c[i] <= c <= i2UB4c[i]]]}]

    s3_ge_n = s3 >= n
    if s3_ge_n or _fixed_kX_eq1:
        # fixed_kX_eq1
        kX = 1
    else:
        # dynamic_choose_kX
        Fraction
        min_AB6odd = min(ls4A[i]*ls4B[i] for i in range(1, 1+t, 2))
        assert min_AB6odd >= 1
        # [min_AB6odd > 0]
        # !! [2*kX*s == n/s**2/kX -kX*min_AB6odd] => [kX == sqrt(n/s**2/(s+min_AB6odd))]
        # let [kX := sqrt(n/s**2/(2*s+min_AB6odd))]

        #.kX_kX = Fraction(n, s**2*(2*s+min_AB6odd)) # == kX**2
        kX_s_kX_s = Fraction(n, (2*s+min_AB6odd)) # == (kX*s)**2
        #.kX_kX = kX_s_kX_s/s**2 # == kX**2
        #.kX = floor_sqrt(kX_kX)
        PAD = 1<<64
        kX = Fraction(floor_sqrt(ceil(kX_s_kX_s * PAD**2)), PAD*s)

        # [len(i2cs[i]) <= 1+floor(2*kX)]
        # [len(i2cs[i]) <= 1+floor(2*kX) == 1+floor_sqrt(4*n/s**2/(2*s+min_AB6odd))]
        max_len4cs4even_i_if_kX_ne1 = 1+floor(2*kX) # 2*kX==2*kX*s/s
        max_len4cs4odd_i_if_kX_ne1 = 1+floor((n/(s**2*kX) -kX*min_AB6odd)/s)
        (small_maxL, big_maxL) = sorted([max_len4cs4even_i_if_kX_ne1, max_len4cs4odd_i_if_kX_ne1])
        diff_maxL = big_maxL -small_maxL
        assert diff_maxL < 4 or Fraction(diff_maxL, small_maxL) < Fraction(1, 100)
            #<<== guess...

        # !! [gcd(n,s)][r:=n**j%s for all j] => [min min_AB6odd == 1]
        # [len(i2cs[i]) <= 1+floor_sqrt(4*n/s**2/(2*s+1))]
        # [len(i2cs[i]) == O(sqrt(n/s**3))]
    kX_kX = kX**2

    kX_eq_1 = kX == 1
    if kX_eq_1:
        max_len4cs4odd_i_if_kX_eq1 = (1+(n//s3)) # (1+floor(n/s**3))
    for i in range(1+t):
        ai = ls4A[i]
        bi = ls4B[i]
        ci = ls4C[i]
        ciM = ci%s
        ai_bi = ai*bi
        odd_i = (i&1) == 1
        LB4c6i = -(ceil(kX*s)-1) if not odd_i else ceil(2*ai_bi*kX)
        UB4c6i = -LB4c6i if not odd_i else floor((ai_bi*s**2*kX_kX + n)//(kX*s**2))
        #bug:min_c = (1 +(LB4c6i-1)//s)*s
        #bug:max_c = (UB4c6i//s)*s
        #bug:cs6i = range(min_c, 1+max_c, s)
        min_c = ciM+ceil_div(LB4c6i-ciM,s)*s
        assert min_c >= LB4c6i
        assert min_c%s == ciM
        cs6i = range(min_c, 1+UB4c6i, s)
        #########
        len(cs6i)
        if kX_eq_1:
            # [[kX==1] -> @[i:<-[0..=t]] -> [len(i2cs[i]) <= [i%2==0]2 + [i%2==1](1+floor(n/s**3))]]
            # [[kX==1] -> [s**3 >= n] -> @[i:<-[0..=t]] -> [len(i2cs[i]) <= 2]]
            if s3_ge_n or not odd_i:
                assert len(cs6i) <= 2
            if odd_i:
                assert len(cs6i) <= max_len4cs4odd_i_if_kX_eq1
        else:
            if odd_i:
                assert len(cs6i) <= max_len4cs4odd_i_if_kX_ne1
            else:
                assert len(cs6i) <= max_len4cs4even_i_if_kX_ne1
        #########

        # !! [roots_of(ij2eqn4Z[i,j]) == {(x*s + r)*a[i], (y*s + r_)*b[i]}]
        s_ai = s*ai
        s_bi = s*bi
        r_ai = r*ai
        r_bi = r_*bi
        # !! [ij2DET4eqn4Z[i,j] := (i2cs[i][j]*s + r*a[i] + r_*b[i])**2 -4*n*a[i]*b[i]]
        _1_4DET = (r_ai + r_bi)
        _2_4DET = (4*n*ai_bi)
        for j4c, c6ij in enumerate(cs6i):
            # [@[i:<-[0..=t]] -> [i2c6xy[i] := (x*a[i] +y*b[i])]] # def:c#c[i]的某个解压值
            # [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [ij2eqn_system4XY[i,j] := [[X*a[i] +Y*b[i] == i2cs[i][j]][(X*s + r)*(Y*s + r_) == n]]]]
            assert LB4c6i <= c6ij <= UB4c6i
            assert c6ij%s == ciM
            dd_pairs = []
            if ai == 0:
                assert 0 < i == t
                assert not bi == 0
                # [y*bi == c6ij]
                #perfect_div(c6ij, bi)
                if not None is (y:=may_perfect_div(c6ij, bi)) and y >= 0:
                    _d = y*s +r_
                    if not None is (d:=may_perfect_div(n, _d)):
                        d
                        # [d%s =!= r] => 下面: ^AssertionError: ((8, 6, 5), [(2, 4)], (2, 4), (0, 2, 5), (0, 4, 4))
                        if d%s == r:
                            dd_pairs.append((d, _d))
            elif bi == 0:
                assert 0 == i < t
                assert not ai == 0
                # [x*ai == c6ij]
                if not None is (x:=may_perfect_div(c6ij, ai)) and x >= 0:
                    d = x*s +r
                    if not None is (_d:=may_perfect_div(n, d)):
                        _d
                        dd_pairs.append((d, _d))
            else:
                assert 0 < i < t
                assert not ai == 0
                assert not bi == 0

                # [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [ij2eqn4Z[i,j] := [z**2 -(i2cs[i][j]*s + r*a[i] + r_*b[i])*z +(n*a[i]*b[i]) == 0]]]
                # [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [ij2DET4eqn4Z[i,j] := (i2cs[i][j]*s + r*a[i] + r_*b[i])**2 -4*n*a[i]*b[i]]] # def:DET{ij2eqn4Z[i,j]}
                DET4z6ij = (_negB4z:=c6ij*s + _1_4DET)**2 -_2_4DET
                # [?[k:<-[0..=t]] -> [i2c6xy[k] <- i2cs[k]]]
                # [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [i2cs[i][j] == i2c6xy[i]] -> [[roots_of(ij2eqn4Z[i,j]) == {(x*s + r)*a[i], (y*s + r_)*b[i]}][sqrt(ij2DET4eqn4Z[i,j]) %1.0 == 0.0]]]
                # [@[i:<-[0..=t]] -> @[j:<-[0..<len(i2cs[i])]] -> [O(sqrt{ij2DET4eqn4Z[i,j]}) == O(sqrt{s**7}) == O(sqrt{n**7})]]

                #perfect_kth_root_(2, DET4z6ij)
                assert 0 == (_negB4z&1)^(DET4z6ij&1)
                if not None is (sqrtDET:=may_perfect_sqrt_(DET4z6ij)):
                    # [sqrt(ij2DET4eqn4Z[i,j]) %1.0 == 0.0]
                    #if 0 == (_negB4z&1)^(DET4z6ij&1) and not None is (sqrtDET:=may_perfect_sqrt_(DET4z6ij)):
                    assert 0 == (_negB4z&1)^(sqrtDET&1)
                    # [ij2eqn4Z[i,j] := [z**2 -(i2cs[i][j]*s + r*a[i] + r_*b[i])*z +(n*a[i]*b[i]) == 0]]
                    # [roots_of(ij2eqn4Z[i,j]) == {(x*s + r)*a[i], (y*s + r_)*b[i]}]
                    _z0 = perfect_div(_negB4z +sqrtDET, 2)
                    _z1 = perfect_div(_negB4z -sqrtDET, 2)
                    for (z0, z1) in [(_z0, _z1), (_z1, _z0)]:
                        if z0 < 0:
                            continue
                        (q_0a, r_0a) = divmod(z0, s_ai)
                        (q_1b, r_1b) = divmod(z1, s_bi)
                        if r_0a == r_ai and r_1b == r_bi:
                            x = q_0a
                            y = q_1b
                            assert x >= 0
                            assert y >= 0
                            d = x*s +r
                            _d = y*s +r_
                            assert n == d*_d
                            assert d*ai == z0
                            assert _d*bi == z1
                            dd_pairs.append((d, _d))
            dd_pairs
            c6ij
            # [i2cs[i][j] == i2c6xy[i]]
            # !! [i2c6xy[i] := (x*a[i] +y*b[i])]
            # [c6ij == (x*ai +y*bi)]
            for (d, _d) in dd_pairs:
                assert n == d*_d
                (x, _r) = divmod(d, s)
                (y, _r_) = divmod(_d, s)
                assert _r == r, (nsr, dd_pairs, (d, _d), (x, _r, r), (y, _r_, r_))
                    # ^AssertionError: ((8, 6, 5), [(2, 4)], (2, 4), (0, 2, 5), (0, 4, 4))
                assert _r_ == r_
                assert c6ij == (x*ai +y*bi)
                assert x >= 0
                assert y >= 0
                assert d >= 1
                assert _d >= 1
                yield d if not with_more_info else (d, ((n,s,r,r_), (t,i,ai,bi,ci), (len(cs6i), j4c, c6ij,x,y), (d,_d)))


#end-def _iter_divisors_in_residue_class__dup_ok_(n, s, r, /):

__all__
from seed.math.divisors_in_residue_classes import iter_divisors_in_residue_class_, list_divisors_in_residue_class_
from seed.math.divisors_in_residue_classes import *
