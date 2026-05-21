#__all__:goto
#公式牜两位数乘法牜初进位牜平方根附近:goto
#   公式牜估算已扫描区域纟两位数乘法牜初进位牜平方根附近:goto
#   凑到平方根附近:goto
#公式牜两位数乘法牜初进位牜偏离平方根:goto
#公式牜步长估计纟两位数乘法牜初进位牜偏离平方根:goto
#   步长衰减规律纟两位数乘法牜初进位牜偏离平方根:goto
#公式牜两位数乘法牜再进位:goto
#公式牜两位数乂三位数乘法牜再进位:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__near_sqrtN.py
分解成两个两位数

seed.math.factor_pint.factor_pint__near_sqrtN
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__near_sqrtN -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__near_sqrtN:__doc__ -ht # -ff -df
#######

[[
@20260513:ver1:___ver1__factor_pint__near_sqrtN_
===
只能在平方根附近:
[N==(z-a)*(z+a)][a**2 < k*z]:
  [N == z**2 -a**2 > z**2 -k*z]
  [z**2 -k*z -N < 0]
  #最大化z
  [z == (k+sqrt(k**2+4*N))/2]
  [z**2 == ((k**2+4*N)+k**2+2*k*sqrt(k**2+4*N))/4 == N +(k**2+k*sqrt(k**2+4*N))/2]
  [a == sqrt(z**2 -N)]
  [a == sqrt((k**2+k*sqrt(k**2+4*N))/2)] # O(N**/4)
    只能在N平方根的附近，距离不超过N四次根

  [N==(z-A)*(z+B)==z**2 +(B-A)*z -A*B][0 < A < a][-a < -A <= B <= A < a]
  [B<=A]
  maybe:[B <= 0]
  [B-A <= 0]
  [A-B >= 0]
  [z**2 -N == (A-B)*z +A*B < (A-B+k)*z]

  往下搜索: [x-b < z-a < z+a < x+b]

  * 往下搜索: [x-b < z-a < z+a < x < x+b]
    ???不行
  * 往下搜索: [x-b < z-a < x < z+a < x+b]
  [N==(x-b)*(x+b)][0 < b**2 -(x-(z-a))*((z+a)-x) < t*x]:
    [N == x**2 -b**2]
    [b**2 == x**2 -N]
    [0 < x**2 -N -(x-(z-a))*((z+a)-x) < t*x]
    [0 < x**2 -N +(x-z+a)*(x-z-a) < t*x]
    [0 < x**2 -N +(x-z)**2 -a**2 < t*x]
    [0 < 2*x**2 -2*x*z +(z**2 -a**2 -N) < t*x]
    [Dz := (z**2 -a**2 -N)]
    [Dz ~= 0]
    [0 < 2*x**2 -2*x*z +Dz < t*x]
    * [Dz == 0]:
      [0 < 2*x**2 -2*x*z < t*x]
      [0 < x -z < t/2]
      感觉不太行
    不能继续扩张

上面是紧凑低端，下面看看最大概率:
[进位来源扌(k;d) =[def]= len{(a,b) | [a,b:<-[1..<d]][a*b//d == k]}]
[进位牜最高概率扌(d) =[def]= snd(max({(进位来源扌(k;d), k) | [k:<-[0..=d-2]]}))]

[进位来源扌(k;d)
== sum[sum{[a*b//d == k] | [b:<-[1..<d]]} | [a:<-[1..<d]]]
== sum[sum{[(k*d)/a <= b <= (k*d+d-1)/a] | [b:<-[1..<d]]} | [a:<-[1..<d]]]
== sum[(max(d, 1+(k*d+d-1)//a) - max(d, (1+(-1+k*d)//a))) | [a:<-[1..<d]]]
  [(1+(-1+k*d)/a) <= d]
  [(-1+k*d) <= (d-1)*a]
  [a >= (-1+k*d)/(d-1)]
== ...

bug:
== sum[((k*d+d-1)//a +1 - (1+(-1+k*d)//a)) | [a:<-[1..<d]]]
== sum[((-1+k*d+d)//a - (-1+k*d)//a) | [a:<-[1..<d]]]
~= d*sum[1/a | [a:<-[1..<d]]]
  ??? ~= d*(ln(d) +0.577215665....)
  ??? ~= (d-1) #k无关
  感觉不太对
]
def f(d, /):
    k2n = dict.fromkeys(range(d-1), 0)
    for a in range(d):
      for b in range(d):
        k = a*b//d
        k2n[k] += 1
    return k2n

f(7)
{0: 27, 1: 9, 2: 7, 3: 3, 4: 2, 5: 1}
f(8)
{0: 31, 1: 13, 2: 7, 3: 7, 4: 3, 5: 2, 6: 1}
f(9)
{0: 37, 1: 14, 2: 11, 3: 8, 4: 5, 5: 3, 6: 2, 7: 1}
f(12)
{0: 52, 1: 23, 2: 19, 3: 13, 4: 11, 5: 9, 6: 7, 7: 4, 8: 3, 9: 2, 10: 1}

看来0是最佳的，即 低端已然最优


===
]]
[[
@20260516:ver2:_ver2__factor_pint__near_sqrtN_
感觉上面太繁琐，z直接设定floor_sqrt就可以了，以避免[k==-1][B<0]
[z:=floor_sqrt(N)][N==(z-A)*(z+B)][0 <= A <= B][A*B < k*z][N%z =!= 0]:
    [A*B%z == (-N)%z]
    [A*B%z =!= 0]
    [t:=A*B//z]
    [0 <= t*z < A*B < (t+1)*z <= k*z]
    [0 <= t < k]
    [0 < ((t+1)*z-A*B) < z]
    [N == z**2 +(-A+B-(t+1))*z +((t+1)*z-A*B)]
    [N%z == ((t+1)*z-A*B)]
    [N//z == z +(-A+B-(t+1))]

    [A*B == ((t+1)*z-N%z)]
    [(B-A) == (N//z -z +(t+1))]
    [0 <= t < k]
    #公式牜两位数乘法牜初进位牜平方根附近:here

估算:已扫描区域:
[z:=floor_sqrt(N)][N==(z-A)*(z+B)][0 <= A <= B][A*B == k*z]:
    [N == z**2 +(B-A)*z -A*B == z**2 +(B-A)*z -k*z]
    [(B-A) == (N/z -z +k)]
    [B*(-A) == (-k*z)]
    [D:=sqrt((N/z -z +k)**2 +4*k*z)]
    [D==B+A]
    [B==((N/z -z +k) +D)/2]
    [-A==((N/z -z +k) -D)/2]
    [A==(-(N/z -z +k) +D)/2]

    [A==(D -(N/z -z +k))/2]
    [B==(D +(N/z -z +k))/2]

    [A{N;k}==(sqrt((N/z -z +k)**2 +4*k*z) -(N/z -z +k))/2]
    #公式牜估算已扫描区域纟两位数乘法牜初进位牜平方根附近:here
===
]]
[[
@20260516
===
剋的含义:here
参数k的原意:
    [A*B < k*z]
    即 进位上界

参数k的别解:
[N==(z-A)*(z+B)]
[N/k**2==(z/k-A/k)*(z/k+B/k)]
[A/k*B/k < z/k]
[A*B < k*z]

放大[N --> N*c**2]可能导致失败:
    [A*B < k*z] --> [(A*c)*(B*c) >= k*(z*c)]
反之缩小N则更容易成功，而k就是缩小系数
===
]]
[[
凑到平方根附近:here
view others/数学/factor_pint/Lehman_method.txt
[@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    [abs(u*q - p*v) < q/B]
[w:=u*v]
[N:=p*q]
[p < q] => [u < v]
希望(w*N)凑到平方根附件:
  [v <= B][abs(u*q - p*v) < q/B <= (w*N)**/4]:
    [u < v <= B]
    [(u*v*p*q) >= q**4/B**4]
    [(u*v*p)*B**4 >= q**3]
    [u/v ~ p/q]
    [v ~ (q/p*u)]
    [(u*(q/p*u)*p)*B**4 >= q**3]
    [(u*u)*B**4 >= q**2]
    [B**4 >= q**2]
    [B >= q**/2]

    [p:=N**/3]:
        [q ~= N**(2/3)]
        [B >= N**/3]
    [p:=N**/2 /2]:
        [q ~= N**/2 *2]
        [B >= N**/4 *sqrt2]
        也就是说:小因子位于平方根一半的话，只需O(N**/4)
]]
[[
@20260516
偏离平方根，往下搜索
===
[N==x*y][1 < z <= x <= y]:
    定点z在x附近
    [a := x-z]
    !! [z <= x]
    [a >= 0]
    [(q,b):=y/%z]
    [0<=b<z]
    !! [z <= y]
    [q>=1]
    [N==x*y==(z+a)*(q*z+b)]
    [N==q*z**2 +(a*q+b)*z+a*b]
    [q*N==(q*z+q*a)*(q*z+b)]
    [_N:=q*N]
    [_z:=q*z]
    [_a:=q*a]
    [_N==(_z+_a)*(_z+b)]
    [a*b < k*z] <==> [_a*b < k*_z]
    通过q放大z至_z即_N的平方根附近
    #公式牜两位数乘法牜初进位牜偏离平方根:here
===
哪些A的相应(z-A)是被完全确认非N因子？
?_B => [N==(z-A)*(z+_B)][A*_B < k*z]
[_B == (N/(z-A) -z)]
!! [A*_B < k*z]
[A*(N/(z-A) -z) < k*z]
[A*N/(z-A) < (A+k)*z]
[A*N/z - (A+k)*(z-A) < 0]
[A**2 +A*(N/z-z+k) -k*z < 0]
[A < (-(N/z-z+k) +sqrt((N/z-z+k)**2 +4*k*z))/2]
[A < (-(N-z**2+k*z) +sqrt((N-z**2+k*z)**2 +4*k*z**3))/(2*z)]
    <<==:充分条件:
    [A < max1_A{N,z,k,q:=1}:=floor_div((-(N-z**2+k*z) +floor_sqrt((N-z**2+k*z)**2 +4*k*z**3)),(2*z))]]
    # 所有[0..<max1_A]的A已检查过
    # 所有[z-(-1+max1_A)..=z]的N的候选因子已检查过
    [next_z := z -max1_A]

版本:[q*N==(q*z+q*a)*(q*z+b)]:
[max1_A{N,z,k,q}
==1/q*max1_A{q*N,q*z,k,q:=1}
==1/q*(-((q*N)/(q*z)-(q*z)+k) +sqrt(((q*N)/(q*z)-(q*z)+k)**2 +4*k*(q*z)))/2
==(-(N/z/q-z+k/q) +sqrt((N/z/q-z+k/q)**2 +4*k*z/q**2))/2
]
[max1_A{N,z,k,q} ==(-(N/z/q-z+k/q) +sqrt((N/z/q-z+k/q)**2 +4*k*z/q**2))/2]
    取消k，更甚！
[max1_A{N,z,k,q} ==(-(N-q*z**2+k*z) +sqrt((N-q*z**2+k*z)**2 +4*k*z**3))/(2*q*z)]
    #公式牜步长估计纟两位数乘法牜初进位牜偏离平方根:here
[q==1] <==> [N < 2*z**2]
    <==> [z**2 <= N < 2*z**2]
    <==> [z <= sqrtN < sqrt2*z]
    <==> [sqrtN/sqrt2 < z <= sqrtN]
        意义不大
===
上面假设q,z已知，或者设定[q:=N//z**2]
但是考虑二次进位:
[N==x*y==(z-a)*(q*z+b)]
已知:z
未知:a,q,b
[N==q*z**2 +(-a*q+b)*z-a*b]
[-_k0*z <= a*b < k0*z][-_k1*z <= a*q < k1*z][0 <= a,b,q < z]:
    [s0:=ceil_div(a*b,z)]#指定范围枚举
    [s1:=ceil_div(a*q,z)]#指定范围枚举
    !! [0 <= a,b,q < z]
    [max(a*b,a*q)/z <= (z-1)**2/z == z-2 +1/z]
    [0 <= s0,s1 <= z-1]

    !! [-_k0*z <= a*b < k0*z]
    [-_k0*z <= a*b <= s0*z <= k0*z]
    [_k0*z <?> (s0-1)*z <  a*b <= s0*z <= k0*z]
    [_k1*z <?> (s1-1)*z <  a*q <= s1*z <= k1*z]
    [_k0 <= s0 <= k0]
    [_k1 <= s1 <= k1]
    [(-a*b)//z == -ceil_div(a*b,z) == -s0]
    [(-a*b)%z == N%z]
    [-a*b == N%z +z*(-s0)]
    [a*b == (-N%z +z*s0)]


    [N == (q-s1)*z**2 +((s1*z-a*q)+b-s0)*z +(s0*z-a*b)]
    ?c1 :=> [(-c1*z+(s1*z-a*q)+b-s0) == (-c1*z+(s1*z-a*q)+b-s0)%z]
    [N == (q-s1+c1)*z**2 +(-c1*z+(s1*z-a*q)+b-s0)*z +(s0*z-a*b)]
    [c1 == ((s1*z-a*q)+b-s0)//z]
    [(c1+s0//z) == ((s1*z-a*q)+b-s0%z)//z]
    !! [-z < ((s1*z-a*q)+b-s0%z) < 2*z]
    [-1 <= (c1+s0//z) <= 1]
    !! [0 <= s0,s1 <= z-1]
    [-1 <= c1 <= 1]
    [N的三位z进制表达 == d2*z**2 +d1*z +d0 == (q-s1+c1)*z**2 +(-c1*z+(s1*z-a*q)+b-s0)*z +(s0*z-a*b)]
    [d2 == N//z**2]
    [d1 == N//z%z]
    [d0 == N%z]

    [d2 == (q-s1+c1)]
    [d1 == (-c1*z+(s1*z-a*q)+b-s0)]
    [d0 == (s0*z-a*b)]

    ==>>:
    #直接迭代枚举数据:s0,s1,c1
    [d2 == N//z**2]
    [d1 == N//z%z]
    [d0 == N%z]
    [_k0 <= s0 <= k0]
    [_k1 <= s1 <= k1]
    [0 <= s0,s1 <= z-1]
    [-1 <= c1 <= 1]
    [q == d2 -(-s1+c1)]
    #已知:N,z,d2,d1,d0,s0,s1,c1,q
    #未知:a,b
    [b-(a*q) == d1 -(-c1*z+s1*z-s0)]
    [(q*a)*b == q*(-d0 +s0*z)]
    #公式牜两位数乘法牜再进位:here


    [q == d2 +(s1-c1)]
    [q >= d2 -1]
    [d2 := q7approx]
    [q >= (q7approx-1)]
    [q7approx SHOULDNOT too large]
===
]]
[[
===
===
]]
[[
@20260516
===
从两位数进化为三位数:
立方根附近:
[N==(z-a)*(z**2+b)][0 <= a < z]:
    [-k0*z < b < +k1*z]:
        [N==z**2*(z-a) +b*(z-a)]
        [N//z**2 == (z-a) +b*(z-a)//z**2]
        [a == (z-N//z**2) +b*(z-a)//z**2]
        [-k0*z**2 < b*(z-a) < k1*z**2]
        [-k0 < b*(z-a)/z**2 < k1]
        [-k0 <= b*(z-a)//z**2 < k1]
        [a == (z-N//z**2) +(-k0..<k1)]
        还不如直接试除！
    [0 < a*b < k*z]:
        [N==(z**3-a*z**2+b*z-a*b)]
        [N==(z**3-(a*z+b-(t+1))*z+((t+1)*z-a*b))]
        问题是:b大概率大于z
            这里要求十分严格:即z**2在大因子附近

===
[N==x*y][1 < x <= z <= y]:
    定点z在x附近
    [z >= 2]
    [a := z-a]
    !! [x <= z]
    [a >= 0]
    ?b2,b1,b0 :=> [y==b2*z**2 +b1*z +b0][0 <= b0,b1 < z]
    [b0 == y%z]
    [b1 == y//z%z]
    [b2 == y//z**2]
    !! [z <= y]
    [b2 >= 0]
    [b1 >= 1]
    [N==x*y==(z-a)*(b2*z**2+b1*z+b0)]
    [N==(b2*z**3+b1*z**2+b0*z)-(a*b2*z**2+a*b1*z+a*b0)]
    [N == (b2*z**3 +(b1-a*b2)*z**2 +(b0-a*b1)*z -a*b0)]

    [_k0*z <= a*b0 < k0*z][_k1*z <= a*b1 < k1*z][_k2*z <= a*b2 < k2*z]:
        #初进位:
        [s0:=ceil_div(a*b0,z)]
        [s1:=ceil_div(a*b1,z)]
        [s2:=ceil_div(a*b2,z)]
        [_k0*z <?> (s0-1)*z <  a*b0 <= s0*z <= k0*z]
        [_k1*z <?> (s1-1)*z <  a*b1 <= s1*z <= k1*z]
        [_k2*z <?> (s2-1)*z <  a*b2 <= s2*z <= k2*z]
        [_k0 <= s0 <= k0]
        [_k1 <= s1 <= k1]
        [_k2 <= s2 <= k2]

        [(-a*b0)//z == -ceil_div(a*b0,z) == -s0]
        [(-a*b0)%z == N%z]
        [-a*b0 == N%z +z*(-s0)]
        [a*b0 == (-N%z +z*s0)]

        !! [N == (b2*z**3 +(b1-a*b2)*z**2 +(b0-a*b1)*z -a*b0)]
        [N == ((b2-s2)*z**3 +(b1+(s2*z -a*b2)-s1)*z**2 +(b0+(s1*z -a*b1)-s0)*z +(s0*z -a*b0))]
        #再进位:
        ?c1 :=> [(-c1*z+b0+(s1*z -a*b1)-s0) == (b0+(s1*z -a*b1)-s0)%z]
        ?c2 :=> [(-c2*z+b1+(s2*z -a*b2)-s1+c1) == (b1+(s2*z -a*b2)-s1+c1)%z]
        [N == ((b2-s2+c2)*z**3 +(-c2*z+b1+(s2*z -a*b2)-s1+c1)*z**2 +(-c1*z+b0+(s1*z -a*b1)-s0)*z +(s0*z -a*b0))]
        [c1 == (b0+(s1*z -a*b1)-s0)//z]
        [c2 == (b1+(s2*z -a*b2)-s1+c1)//z]

        [c1+s0//z == (b0+(s1*z -a*b1)-s0%z)//z]
        !! [-z < (b0+(s1*z -a*b1)-s0%z) < 2*z]
        [-1 <= (c1+s0//z) <= 1]

        [c2 == (b1+(s2*z -a*b2)-(s1+s0//z)+(c1+s0//z))//z]
        [c2+(s1+s0//z)//z == (b1+(s2*z -a*b2)-(s1+s0//z)%z+(c1+s0//z))//z]
        !! [z >= 2]
        !! [-1 <= c1+s0//z <= 1]
        !! [-z <= (b1+(s2*z -a*b2)-(s1+s0//z)%z+(c1+s0//z)) < 2*z]
        [-1 <= (c2+(s1+s0//z)//z) <= 1]
        [d3 := N//z**3] #允许超过z，但是太大的话，意味b2大，s2也大，不利于数据枚举
        [d2 := N//z**2 %z]
        [d1 := N//z %z]
        [d0 := N%z]
        [N的四位数z进制表达 == d3*z**3 +d2*z**2 +d1*z +d0 == ((b2-s2+c2)*z**3 +(-c2*z+b1+(s2*z -a*b2)-s1+c1)*z**2 +(-c1*z+b0+(s1*z -a*b1)-s0)*z +(s0*z -a*b0))]
        [d3 == (b2-s2+c2)]
        [d2 == (-c2*z+b1+(s2*z -a*b2)-s1+c1)]
        [d1 == (-c1*z+b0+(s1*z -a*b1)-s0)]
        [d0 == (s0*z -a*b0)]

        ==>>:
        [b2 == d3 -(-s2+c2)]
        [b1 == d2 -(-c2*z+(s2*z -a*b2)-s1+c1)]
        [b0 == d1 -(-c1*z+(s1*z -a*b1)-s0)]
        [a*b0 == (s0*z -d0)] #<==> [a*b0 == (-N%z +z*s0)]
            #2 unknowns:a,b0:一元三次方程
            #怎么用整数运算解这个方程...???
        #直接迭代枚举数据:(s0,s1,s2,c1,c2)
        [-1 <= (c1+s0//z) <= 1]
        [-1 <= (c2+(s1+s0//z)//z) <= 1]
        [_k0 <= s0 <= k0]
        [_k1 <= s1 <= k1]
        [_k2 <= s2 <= k2]
        #公式牜两位数乂三位数乘法牜再进位:here

    ... ...
===
]]




'#'; __doc__ = r'#'

__all__
>>> [*_ver2__iter_factor_pint__near_sqrtN_(12, verbose=False)]
[(3, 4), (2, 6), None, None, None, None]
>>> [*_ver2__iter_factor_pint__near_sqrtN_(12, verbose=True)]
[(12, 3, 0, 0, 1, 3, 4), (12, 3, 1, 1, 3, 2, 6), None, None, None, None]
>>> [*_ver2__iter_factor_pint__near_sqrtN_(27, verbose=False)]
[None, None, (3, 9), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> [*_ver2__iter_factor_pint__near_sqrtN_(27, verbose=True)]
[None, None, (27, 5, 2, 2, 4, 3, 9), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> [*_ver2__iter_factor_pint__near_sqrtN_(64, verbose=False)]
[(8, 8), None, None, None, (4, 16), None, None, None, None, None, None, None, None, None, None, None, None, None, (2, 32), None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]



fail:14,22,26,27 # < 33
>>> for N in [14,22,26,27]:
...     print(N, factor_pint__near_sqrtN_(N, ..., with_num_loops=True), sep=':')
14:(2, 2, 7)
22:(4, 2, 11)
26:(5, 2, 13)
27:(2, 3, 9)
>>> for N in [14,22,26,27]:
...     for k in range(1, N):
...         m = factor_pint__near_sqrtN_(N, k)
...         if m:
...             print(N, k, m, sep=':')
...             break
...     else:
...             print(N, 'fail', sep=':')
14:2:(2, 7)
22:4:(2, 11)
26:5:(2, 13)
27:2:(3, 9)

>>> for N in range(1, 33):
...     print(N, factor_pint__near_sqrtN_(N), sep=':')
1:None
2:None
3:None
4:(2, 2)
5:None
6:(2, 3)
7:None
8:(2, 4)
9:(3, 3)
10:(2, 5)
11:None
12:(3, 4)
13:None
14:None
15:(3, 5)
16:(4, 4)
17:None
18:(3, 6)
19:None
20:(4, 5)
21:(3, 7)
22:None
23:None
24:(4, 6)
25:(5, 5)
26:None
27:None
28:(4, 7)
29:None
30:(5, 6)
31:None
32:(4, 8)

>>> factor_pint__near_sqrtN_(35668877**2)
(35668877, 35668877)
>>> factor_pint__near_sqrtN_(35668877*(35668877+1))
(35668877, 35668878)
>>> factor_pint__near_sqrtN_(35668877*(35668877+4))
(35668877, 35668881)
>>> factor_pint__near_sqrtN_(35668877*(35668877+9))
(35668877, 35668886)
>>> factor_pint__near_sqrtN_(35668877*(35668877+5972))
(35668877, 35674849)
>>> factor_pint__near_sqrtN_(35668877*(35668877+11945))
(35668877, 35680822)
>>> factor_pint__near_sqrtN_(35668877*(35668877+11946)) #fail
>>> factor_pint__near_sqrtN_(35668877*(35668877+11945)*4) #fail:scale
>>> factor_pint__near_sqrtN_(35668877*(35668877+11945)*4, 2) #剋的含义:goto
(71337754, 71361644)
>>> factor_pint__near_sqrtN_(35668877*(35668877+1)*4**60) #fail:scale

>>> factor_pint__near_sqrtN_(35668877*(35668877+11945//2+0)*16) # N**/4
(142675508, 142699396)
>>> factor_pint__near_sqrtN_(35668877*(35668877+11945//2+1)*16) #fail:scale

>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__:=35668877*(35668877+11945//2+1)*16) # [max_num_outer_loops:=100]
(True, (142675508, 142699400))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 1) #第一步
(False, (11944, 142675509))
>>> 142675509 -35668877*4
1
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, 142675509, 1) #第二步
(True, (142675508, 142699400))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 5, 1, with_num_loops=True)
(True, ((142675508, 142699400), (2, (2, 1, 1))))



>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__:=(23467777*(23467777+4*floor_sqrt(23467777))), ..., 5, with_num_loops=True)
(True, ((23467777, 23487153), (4, (4, 1, 1))))


>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__:=(23467777*(23467777+400*floor_sqrt(23467777))), ..., 500, with_num_loops=True) #fail...
(False, ((110, 24307289), (500, (500, 1))))
>>> 24307289 -23467777
839512
>>> (24307289 -23467777)/110
7631.927272727273
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, 24307289, 1, with_num_loops=True)
(False, ((110, 24307179), (1, (1, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, 24307289, 500, with_num_loops=True)
(False, ((77, 24261938), (500, (500, 1))))
>>> (24261938 -23467777)/77
10313.77922077922


步长衰减规律纟两位数乘法牜初进位牜偏离平方根:here
    步长每衰减一半，搜索步数翻四倍
    [num_loops == num_steps]
    [num_steps{min_step:=(N**/4 /2**k)} ~= (2**(-2+2*k))]
    [len_interval7checked >= (num_steps{min_step:=(N**/4 /2**k)}*min_step) ~= (2**(-2+2*k))*(N**/4 /2**k) == (N**/4 *2**k /4)]
    [len_interval7checked{k} >= len_interval7checked{k-1} + 3/4*(N**/4 *2**k /4) >= ... ~= 3/8*(N**/4)*(1-1/2**k)]
        可是起步阶段就有(N**/4)
        但也看出增加搜索次数多半没用
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 500, 1, with_num_loops=True, min_step=(__rr:=floor_sqrt(floor_sqrt(__)))//2) #fail...
(False, ((2046, 24410379), (2, (2, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 500, 1, with_num_loops=True, min_step=__rr//4) #fail...
(False, ((1166, 24406320), (5, (5, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 500, 1, with_num_loops=True, min_step=__rr//8) #fail...
(False, ((607, 24397005), (17, (17, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 500, 1, with_num_loops=True, min_step=__rr//16) #fail...
(False, ((307, 24377581), (65, (65, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 500, 1, with_num_loops=True, min_step=__rr//32) #fail...
(False, ((153, 24338362), (257, (257, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 2000, 1, with_num_loops=True, min_step=__rr//64) #fail...
(False, ((76, 24260245), (1022, (1022, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 8000, 1, with_num_loops=True, min_step=__rr//128) #fail...   #doctest: +SKIP
(False, ((37, 24102246), (4156, (4156, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 1_7000, 1, with_num_loops=True, min_step=__rr//256) #fail...   #doctest: +SKIP
(False, ((18, 23799093), (16342, (16342, 1))))
>>> divmod(__, 23467777)
(25405377, 0)
>>> 16342**2/23799093
11.221476549547498
>>> 23799093 -23467777
331316
>>> 23799093 /23467777
1.0141179115516565







useless: factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_
    !! 还不如直接增加k!
    不过可以用于观察:步长衰减规律纟两位数乘法牜初进位牜偏离平方根
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 500, 1, with_num_loops=True) #fail...
(False, ((110, 24307289), (500, (500, 1))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 50, 10, with_num_loops=True) #fail...
(False, ((1105, 24307140), (500, (50, 10))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 10, 50, with_num_loops=True) #fail...
(False, ((5645, 24307125), (500, (10, 50))))
>>> factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_(__, ..., 1, 500, with_num_loops=True) #fail...
(False, ((110243, 24307122), (500, (1, 500))))















>>> factor_pint__two_digit_number_multiplication_with_second_carry_(6666*6667, ..., max_fst_carry=1, max_snd_carry=1, with_num_loops=True)
(True, ((6666, 6667), (2, 0, 0, 0)))

>>> _2x3 = (356634677-3564)*(34*356634677+677)
>>> z = 356634677
>>> (d21, d0) = divmod(_2x3, z)
>>> (d2, d1) = divmod(d21, z)
>>> ((d2, d1, d0), z, _2x3)
((33, 356514177, 354221849), 356634677, 4324358982398050535)
>>> d2*z**2 +d1*z +d0
4324358982398050535
>>> (356634677-3564)
356631113
>>> (34*356634677+677)
12125579695
>>> a = 3564
>>> q = 34
>>> b = 677

((N, z), (d2, d1, d0), (a, q, b), (s0, s1, c1), (Q, BsubQA, BmulQA), (q, b-q*a, b*q*a))
    BsubQA = d2 -((-c1+s1)*z-s0)
>>> ttt = _debug_2x3((356634677-3564), (34*356634677+677), 356634677)
>>> ttt
((4324358982398050535, 356634677), (33, 356514177, 354221849), (3564, 34, 677), (1, 1, 0), (34, -120499, 82036152), (34, -120499, 82036152))
>>> ((N, z), (d2, d1, d0), (a, q, b), (s0, s1, c1), (Q, BsubQA, BmulQA), _) = ttt

>>> _debug_2x3((356634677-3564), (34*356634677+677), 356632904)
((4324358982398050535, 356632904), (34, 64, 247455335), (1791, 34, 60959), (1, 1, 1), (34, 65, 3712037346), (34, 65, 3712037346))


>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., max_fst_carry=1, max_snd_carry=1, with_num_loops=True)
(False, (2079509312, 1, 1, 1))
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., max_fst_carry=100, max_snd_carry=100, with_num_loops=True)
(False, (2079509312, 100, 100, 1))

得猜近q才行:
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, floor_sqrt(_2x3//34), max_fst_carry=1, max_snd_carry=1, with_num_loops=True)
(True, ((356631113, 12125579695), (8, 1, 0, 0)))
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, floor_sqrt(_2x3//34), max_fst_carry=10, max_snd_carry=10, with_num_loops=True)
(True, ((356631113, 12125579695), (35, 1, 0, 0)))
>>> 356632904 -z
-1773
>>> 356632904 > (356634677-3564)
True



!! [q >= (q7approx-1)]
[q7approx SHOULDNOT too large]
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., 34, max_fst_carry=1, max_snd_carry=1, with_num_loops=True)
(True, ((356631113, 12125579695), (8, 1, 0, 0)))
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., 32, max_fst_carry=5, max_snd_carry=5, with_num_loops=True)
(False, (367608784, 5, 5, 1))
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., 36, max_fst_carry=5, max_snd_carry=5, with_num_loops=True)
(False, (346584885, 5, 5, 1))

>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., 32, max_fst_carry=50, max_snd_carry=50, with_num_loops=True)
(False, (367608784, 50, 50, 1))
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., 36, max_fst_carry=50, max_snd_carry=50, with_num_loops=True)
(False, (346584885, 50, 50, 1))



>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., 33, max_fst_carry=50, max_snd_carry=50, with_num_loops=True)
(False, (361996106, 50, 50, 1))
>>> factor_pint__two_digit_number_multiplication_with_second_carry_(_2x3, ..., 35, max_fst_carry=50, max_snd_carry=50, with_num_loops=True)
(False, (351501228, 50, 50, 1))




[[
_ver2__iter_factor_pint__two_digit_number_multiplication_with_second_carry_
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   ,_ver2__iter_factor_pint__two_digit_number_multiplication_with_second_carry_  =4324358982398050535  =... =32  --max_fst_carry=3 --max_snd_carry=3
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   ,_debug_2x3  ='(356634677-3564)' ='(34*356634677+677)'  =367608784
    (4324358982398050535, 367608784)
    (32, 10, 355285703)
    (10977671, 32, 362098607)
    (10813125, 1, 1) # s0超大！看来q得猜的及其准才行！
    (32, 10813135, 127199980070537504)
    (32, 10813135, 127199980070537504)

py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   ,_debug_2x3  ='(356634677-3564)' ='(34*356634677+677)'  =351501228
    (4324358982398050535, 351501228)
    (35, 49, 181710923)
    (-5129885, 34, 174537943)
    (-2547244, 0, 1) #s0下溢:<<==[35>34]
    (34, 348954033, -30442225574702870)
    (34, 348954033, -30442225574702870)
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   ,_debug_2x3  ='(356634677-3564)' ='(34*356634677+677)'  =361996106
    (4324358982398050535, 361996106)
    (33, 47, 331846765)
    (5364993, 33, 179708197)
    (2663381, 1, 1) #s0超大:[a*b超大，并非q!，但...]
    (33, 2663428, 31816396225271493)
    (33, 2663428, 31816396225271493)

]]




[[
next_probable_prime ='(2**28)'
    268435459
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*268435459' =4 +to_show_num_bits6fail
    fail: 23999 bits
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*268435459' =4 +to_show_num_bits6fail +composite_ok
    fail: 18407 bits
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*268435459' =4 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((65537, 268435459), (4094, 4095))
next_probable_prime ='(2**16+2**11)'
    67589
next_probable_prime ='(2**28+2**17)'
    268566559
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='67589*268566559' =4 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((67589, 268566559), (3972, 3973))
next_probable_prime ='(2**16+2**15+3567)'
    101873
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='101873*268566559' =4 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((101873, 268566559), (2635, 2636))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='101873*268566559' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((101873, 268566559), (2635, 2636))
next_probable_prime ='(2**16+1)*2**14+2**15'
    1073790979
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='101873*1073790979' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((101873, 1073790979), (10539, 10540))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1073790979' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((65537, 1073790979), (16383, 16384))
        #最难情形:[q%p ~= p/2]

py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1073790979*2' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((131074, 1073790979), (8191, 8192))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1073790979*2**6' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((4194368, 1073790979), (255, 256))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1073790979*2**12' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((268439552, 1073790979), (3, 4))
next_probable_prime ='(2**16+1)*(2**14+3576)+2**15'
    1308151301
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1308151301*2**12' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((4194368, 83721683264), (79841, 79842))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1308151301*2**6' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((2097184, 2616302602), (4989, 4990))
        #竟然有用！！
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1308151301*2**1' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((131074, 1308151301), (9979, 9980))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @_try_factor_pint__near_sqrtNmulIIps_  ='(2**16+1)*1308151301*2**0' =1 +to_show_num_bits6fail +composite_ok +no_II +with_position6ok
    ((65537, 1308151301), (19959, 19960))


]]
[[
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**13)'
    None

>13
: {8191: 1}
>65
: {31: 1, 8191: 1, 145295143558111: 1}
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**65)'
    ((31, 1190112520884487201), (False, (11, 31)))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='1190112520884487201'
    ((8191, 145295143558111), (False, (1028, 8191)))

view ../../python3_src/nn_ns/math_nn/factor_Mersenne_number_into_prime2exp.py.cached.txt
>57
: {7: 1, 32377: 1, 524287: 1, 1212847: 1}
>59
: {179951: 1, 3203431780337: 1}
>62
: {3: 1, 715827883: 1, 2147483647: 1}
>67
: {193707721: 1, 761838257287: 1}
>>> 193707721*761838257287==-1+2**67
True
>>> 761838257287/193707721
3932.9266451232475

py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**57)'
    ((7, 20587884010836553), (False, (4, 7)))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='20587884010836553' -verbose
    ((32377, 635879915089), (False, (3475, 32377)))
py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='635879915089' -verbose
    ((524287, 1212847), (True, (37, 4)))

py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**67)'
    超过5分钟
    ^C #KeyboardInterrupt
    try_factor_pint__near_sqrtNmulCmulZpow_(147573952589676412927):[last_c =3685][log2(N) ~= 67]
    total::duration: 4.573469 *(unit: 0:00:01)


py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**67)' --ground_scale=3932
    ^C
    try_factor_pint__near_sqrtNmulCmulZpow_(147573952589676412927):[last_c =26532][log2(N) ~= 67][ground_scale == 3932]
    total::duration: 31.824571770999995 *(unit: 0:00:01)
py_adhoc_call { +to_show_total_timedelta }  seed.math.factor_pint.factor_pint__near_sqrtN   @try_factor_pint__near_sqrtNmulCmulZpow_ +with_position6ok   ='(-1+2**67)' --ground_scale=3933
    #即使猜得极准，也得迭代许多次
    ((193707721, 761838257287), (True, (10035, 16, 3933)))
    total::duration: 12.051795262 *(unit: 0:00:01)


]]



py_adhoc_call   seed.math.factor_pint.factor_pint__near_sqrtN   @factor_pint__near_sqrtN_

]]]'''#'''
__all__ = r'''
factor_pint__two_digit_number_multiplication_with_second_carry_
factor_pint__near_sqrtN_








factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_


try_factor_pint__near_sqrtNmulCmulZpow_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.primality_test.errors import IsStrongProbablePrimeError

    from seed.debug.print_err import print_err
    from itertools import islice, chain
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt
    from seed.math.gcd import gcd
    from seed.math.floor_ceil_tools.fc_div import floor_div, ceil_div
    from seed.math.floor_ceil_tools.fc_perfect import may_perfect_div
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt
    from seed.math.floor_ceil_tools.fc_log import floor_log2
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4primes_ge_
    from seed.math.primality_test.strong_probable_prime import detect_strong_probable_prime__not_waste_too_much_time_

#.with mk_ctx4lazy_import4funcs_(__name__, 'isqrt:floor_sqrt'):
#.    from math import isqrt as floor_sqrt
def __():
    from math import isqrt as floor_sqrt
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt
#.#################################
___end_mark_of_excluded_global_names__0___ = ...



def _ver2__factor_pint__near_sqrtN_(N, emay_max_num_inner_loops=1, emay_z=..., /, *, with_num_loops=False):
    #with_max1_carry --> with_num_loops
    'N/int{>=1} -> emay k/max_num_inner_loops/int{>0} -> may (n0, n1) # O(k) # [N==n0*n1][0 <= (n1-n0) <= O(N**/4)]'
    check_int_ge(1, N)
    k = emay_max_num_inner_loops
    if not k is ...:
        check_int_ge(0, k)
    it = _ver2__iter_factor_pint__near_sqrtN_(N, emay_z)
    if not k is ...:
        it = islice(it, 0, 1+k)
            # 『1+』 for [_k==0]
    for _k, m in enumerate(it):
        match m:
            case (n0, n1):
                return (n0, n1) if not with_num_loops else (_k, n0, n1)
    return None
def _ver2__factor_pint__depart_from_sqrtN_(N, emay_upperbound4small_factor=..., /, max_num_outer_loops=100, max_num_inner_loops=1, *, with_num_loops=False, min_step=1):
    'N/int{>=1} -> emay z/upperbound4small_factor/uint{1<=z<=sqrt(N)} -> max_num_outer_loops/int{>0} -> k/max_num_inner_loops/int{>0} -> may (n0, n1) # O(k) # [N==n0*n1][0 <= (n1-n0) <= O(N**/4)]'
    #公式牜两位数乘法牜初进位牜偏离平方根:goto
    check_int_ge(1, N)
    check_int_ge(1, min_step)
    if N < 4:
        #on fail:
        return (False, (max1_A:=0, next_z:=1))
    if emay_upperbound4small_factor is ...:
        upperbound4small_factor = floor_sqrt(N)
    else:
        upperbound4small_factor = emay_upperbound4small_factor
    check_int_ge(1, upperbound4small_factor)
    check_int_ge(1, max_num_inner_loops)
    check_int_ge(1, max_num_outer_loops)
    z = upperbound4small_factor
    k = max_num_inner_loops
    num_loops = 0
    check_int_ge(z**2, N)
    ok = False
    # [1 <= z <= sqrt(N)]
    for j in range(max_num_outer_loops):
        if z < 2:break
        # [2 <= z <= sqrt(N)]
        q = N//z**2
        m = _ver2__factor_pint__near_sqrtN_(q*N, k, z, with_num_loops=True)
        match m:
            case (_k, n0, n1):
                num_loops += _k
                n2 = gcd(n0, N)
                if 1 < n2 < N:
                    n3 = N//n2
                    (n0, n1) = sorted([n2,n3])
                    data = (n0, n1)
                    stat = (num_loops, (num_outer_loops:=1+j, k, _k))
                    ok = True
                    break
                else:
                    pass
            case None:
                num_loops += k
                pass
            case _:
                raise 000
        #########
        (max1_A, next_z) = _calc_max1_A5N_z_q_k_(N, z, q, k)
        # [max1_A >= 0]
        # [next_z == z -max1_A]
        if max1_A < min_step:break
        # [max1_A >= min_step >= 1]
        # [next_z < z]
        # !! [2 <= z <= sqrt(N)]
        # [next_z < z <= sqrt(N)]
        if next_z < 2:break
        # [2 <= next_z < z <= sqrt(N)]
        z = next_z
        # [2 <= z <= sqrt(N)]
        #########
    if not ok:
        #on fail:
        data = (max1_A, next_z)
        stat = (num_loops, (num_outer_loops:=1+j, k))
        ok = False
    r = data if not with_num_loops else (data, stat)
    return (ok, r)

factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_ = _ver2__factor_pint__depart_from_sqrtN_
def _calc_max1_A5N_z_q_k_(N, z, q, k, /):
    #公式牜步长估计纟两位数乘法牜初进位牜偏离平方根:goto
    # [max1_A{N,z,k,q} ==(-(N/z/q-z+k/q) +sqrt((N/z/q-z+k/q)**2 +4*k*z/q**2))/2]
    # [max1_A{N,z,k,q} ==(-(N-q*z**2+k*z) +sqrt((N-q*z**2+k*z)**2 +4*k*z**3))/(2*q*z)]
    # [next_z := z -max1_A]
    z2 = z**2
    kz = k*z
    kz3 = kz*z2
    vb = (N-q*z2+kz)
    max1_A = floor_div((-vb +floor_sqrt(vb**2 +4*kz3)),(2*q*z))
    next_z = z -max1_A
    return (max1_A, next_z)
def _ver2__iter_factor_pint__near_sqrtN_(N, emay_z=..., /, *, verbose:bool=False):
    'N -> Iter (may ((n0, n1) if not verbose else (N, z, _k:=1+t, A, B, n0, n1)))'
    #公式牜两位数乘法牜初进位牜平方根附近:goto
    check_int_ge(1, N)
    if N < 4:
        return None
    # [N >= 4]

    if emay_z is ...:
        z = floor_sqrt(N)
        # !! [N >= 4]
        # [2 <= z <= 2*z <= z**2 <= N]
        assert 2 <= z < N, (N, z)
    else:
        z = emay_z
        check_int_ge(2, z)
        check_int_ge(z**2, N)
        # [2 <= z <= 2*z <= z**2 <= N]
    # [2 <= z <= 2*z <= z**2 <= N]




    (NdivZ, NmodZ) = divmod(N, z)
    if NmodZ == 0:
        #.return (z, NdivZ)
        n0 = z
        n1 = NdivZ
        yield (n0, n1) if not verbose else (N, z, _k:=0, A:=0, B:=n1-z, n0, n1)
    else:
        yield None#@[_k:=0]
    #
    # old:[N%z =!= 0]
    # old:[2 <= z <= 2*z <= z**2 < N]
    # now:assume:[A*B > 0]

    # [z:=floor_sqrt(N)][N==(z-A)*(z+B)][0 <= A <= B][A*B < k*z]

    # [A*B == ((t+1)*z-N%z)]
    # [(B-A) == (N//z -z +(t+1))]
    # [0 <= t < k]
    t = -1
    while 1:
        t += 1
        #for t in range(k):
        if t == 0:
            BmulA = z -NmodZ
            BsubA = NdivZ -z +1
        else:
            BmulA += z
            BsubA += 1
        #if 0b0001:print_err(N, z, t, (BsubA, BmulA), sep=':')
        m = _solve(BsubA, BmulA)
        if m:
            (B,A) = m
            #break
            n0 = z-A
            n1 = z+B
            assert n0*n1 == N, (N, z, t, (BsubA, BmulA), (A, B), (n0, n1))
            assert 1 <= n0 <= n1 <= N, (N, z, t, (BsubA, BmulA), (A, B), (n0, n1))
            if n0 == 1:
                return None
            #.return (n0, n1)
            yield (n0, n1) if not verbose else (N, z, _k:=1+t, A, B, n0, n1)
        else:
            yield None#@[_k:=1+t]
    else:
        return None
factor_pint__near_sqrtN_ = _ver2__factor_pint__near_sqrtN_

def _solve(AsubB, AmulB, /):
    '(A-B) -> (A*B) -> may (A, B)'
    square4AaddB = AsubB**2 +4*AmulB
    if square4AaddB < 0:
        return None
    AaddB = floor_sqrt(square4AaddB)
    if not AaddB**2 == square4AaddB:
        return None
    A = (AaddB +AsubB)//2
    B = (AaddB -AsubB)//2
    assert A-B == AsubB
    assert A*B == AmulB
    #assert A <= B
    return (A,B)
__all__

r'''[[[
def ___ver1__factor_pint__near_sqrtN_(N, k=1, /):
    'N/int{>=1} -> k/int{>0} -> may (n0, n1) # O(k) # [N==n0*n1][0 <= (n1-n0) <= O(N**/4)]'
    check_int_ge(1, N)
    check_int_ge(1, k)
    if N < 4:
        return None
    # [z == floor((k+sqrt(k**2+4*N))/2)]
    z = (k+floor_sqrt(k**2+4*N))//2
    assert 1 <= z <= N, (N, z)
    #assert 1 <= z < N, (N, z)
        # ^AssertionError: (2, 2)
    if z == 1:
        return None
    zz = z**2
    if zz == N:
        return (z, z)
    #assert zz > N, (N, z, zz)
        # ^AssertionError: (11, 3, 9)
        # ^AssertionError: (10, 3, 9)
        # ^AssertionError: (5, 2, 4)

    # maybe:[B <= 0]
    # [A-B >= 0]
    # [z**2 -N == (A-B)*z +A*B < (A-B+k)*z]
    (AsubB, AmulB) = divmod(zz-N, z)
    if 1:
        # [-z <= AmulB < 0]
        AmulB -= z
        AsubB += 1
    for _k in range(0,1+k):
        # [(_k-1)*z <= AmulB < _k*z]
        m = _solve(AsubB, AmulB)
        if m:
            (A,B) = m
            n0 = z-A
            n1 = z+B
            assert n0*n1 == N, (N, z, k, _k, (AsubB, AmulB), (A, B), (n0, n1))
            assert 1 <= n0 <= n1 <= N, (N, z, k, _k, (AsubB, AmulB), (A, B), (n0, n1))
            if n0 == 1:
                return None
            return (n0, n1)
        AmulB += z
        AsubB -= 1
    return None
#]]]'''#'''



__all__

def _ver2__factor_pint__two_digit_number_multiplication_with_second_carry_(N, emay_z=..., q7approx=1, /, *, with_num_loops=False, min_fst_carry=0, max_fst_carry=1, min_snd_carry=0, max_snd_carry=1):
    'N/int{>=1} -> emay z/upperbound4small_factor/int{>0} -> q7approx/int{>=1}{~=N//z**2} -> ((False, may (z, s0, s1, c1))|(True, ((n0, n1) if not with_num_loops else ((n0, n1), (sz, s0, s1, c1))))) # O((max_fst_carry-min_fst_carry)*(max_snd_carry-min_snd_carry)) # [N==n0*n1] # [q >= (q7approx-1)] => [q7approx SHOULDNOT too large]'
    check_int_ge(1, N)
    check_int_ge(1, q7approx)
    check_int_ge(0, min_fst_carry)
    check_int_ge(min_fst_carry, max_fst_carry)
    check_int_ge(0, min_snd_carry)
    check_int_ge(min_snd_carry, max_snd_carry)
    it = _ver2__iter_factor_pint__two_digit_number_multiplication_with_second_carry_(N, emay_z, q7approx, min_fst_carry=min_fst_carry, max_fst_carry=max_fst_carry, min_snd_carry=min_snd_carry, max_snd_carry=max_snd_carry)
    m = None
    for sz, m in enumerate(it, 1):
        match m:
            case (True, ((n0, n1), (N, z, s0, s1, c1, A, Q, B))):
                r = (n0, n1) if not with_num_loops else ((n0, n1), (sz, s0, s1, c1))
                return (True, r)
            case (False, (z, s0, s1, c1, Q, BsubQA, BmulQA)):
                m = (z, s0, s1, c1)
                pass
            case _:
                raise 000
    return (False, m)

def _ver2__iter_factor_pint__two_digit_number_multiplication_with_second_carry_(N, emay_z=..., q7approx=1, /, *, verbose:bool=False, min_fst_carry=0, max_fst_carry=1, min_snd_carry=0, max_snd_carry=1):
    'N -> Iter ((False, (z, s0, s1, c1)) | (True, ((n0, n1), (N, z, s0, s1, c1, A, Q, B))))'
    #公式牜两位数乘法牜再进位:goto
    # #直接迭代枚举数据:s0,s1,c1
    # [d2 == N//z**2]
    # [d1 == N//z%z]
    # [d0 == N%z]
    # [_k0 <= s0 <= k0]
    # [_k1 <= s1 <= k1]
    # [0 <= s0,s1 <= z-1]
    # [-1 <= c1 <= 1]
    # [q == d2 -(-s1+c1)]
    # #已知:N,z,d2,d1,d0,s0,s1,c1,q
    # #未知:a,b
    # [b-(a*q) == d1 -(-c1*z+s1*z-s0)]
    # [(q*a)*b == q*(-d0 +s0*z)]
    check_int_ge(1, N)
    check_int_ge(1, q7approx)
    if N < 4:
        return None
    # [N >= 4]

    if emay_z is ...:
        z = floor_sqrt(N//q7approx)
        # !! [N >= 4]
        # old:[2 <= z <= 2*z <= z**2 <= N]
        #assert 2 <= z < N, (N, z)
        # [z**2 < N/q7approx]
        if not 2 <= z < N: raise ValueError(N, z, q7approx)
    else:
        z = emay_z
        check_int_ge(2, z)
        check_int_ge(z**2, N)
        # [2 <= z <= 2*z <= z**2 <= N]
    # [2 <= z <= 2*z <= z**2 <= N]


    check_int_ge(0, min_fst_carry)
    check_int_ge_lt(min_fst_carry, z, max_fst_carry)
    check_int_ge(0, min_snd_carry)
    check_int_ge_lt(min_snd_carry, z, max_snd_carry)

    (NdivZ, d0) = divmod(N, z)
    (d2, d1) = divmod(NdivZ, z)
    if not d2 > 0:raise 000
    def __():
        ranges4s0 = range(min_fst_carry, 1+max_fst_carry)
        ranges4s1 = range(min_snd_carry, 1+max_snd_carry)
        ranges4c1 = range(-1, 2)
        for s0 in ranges4s0:
            #if not 0 <= s0 < z:raise 000
            v00 = (-d0 +s0*z)
            for s1 in ranges4s1:
                #if not 0 <= s1 < z:raise 000
                for c1 in ranges4c1:
                    Q = d2 -(-s1+c1)
                    #bug:BsubQA = d2 -((-c1+s1)*z-s0)
                    BsubQA = d1 -((-c1+s1)*z-s0)
                    #BmulQA = Q*(-d0 +s0*z)
                    BmulQA = Q*v00
                    yield (s0, s1, c1, Q, BsubQA, BmulQA)
    for (s0, s1, c1, Q, BsubQA, BmulQA) in __():
        if not Q > 0:continue
        # [b-(a*q) == d1 -(-c1*z+s1*z-s0)]
        # [(q*a)*b == q*(-d0 +s0*z)]
        m = _solve(BsubQA, BmulQA)

        if not None is m:
            (B,QA) = m
            m = may_perfect_div(QA, Q)
        if not None is m:
            A = m
            n0 = z-A
            n1 = (Q*z+B)
            assert n0*n1 == N, (N, z, (s0, s1, c1, Q, BmulQA, BsubQA), (A, Q, B), (n0, n1))
            assert 1 <= n0 <= n1 <= N, (N, z, (s0, s1, c1, Q, BmulQA, BsubQA), (A, Q, B), (n0, n1))
            if n0 == 1:
                return None
            yield (True, ((n0, n1), (N, z, s0, s1, c1, A, Q, B)))#@each succ step
        else:
            yield (False, (z, s0, s1, c1, Q, BsubQA, BmulQA))#@each fail step
    else:
        return None
factor_pint__two_digit_number_multiplication_with_second_carry_ = _ver2__factor_pint__two_digit_number_multiplication_with_second_carry_
def _debug_2x3(ZsubA, QZaddB, z, /):
    a = z -ZsubA
    (q, b) = divmod(QZaddB, z)
    s0 = ceil_div(a*b, z)
    s1 = ceil_div(a*q, z)
    c1 = ((s1*z-a*q)+b-s0)//z
    (s0, s1, c1)

    N = ZsubA*QZaddB
    (d21, d0) = divmod(N, z)
    (d2, d1) = divmod(d21, z)
    (d2, d1, d0)

    Q = d2 -(-s1+c1)
    BsubQA = d1 -((-c1+s1)*z-s0)
    BmulQA = Q*(-d0 +s0*z)

    return ((N, z), (d2, d1, d0), (a, q, b), (s0, s1, c1), (Q, BsubQA, BmulQA), (q, b-q*a, b*q*a))



def _try_factor_pint__near_sqrtNmulIIps_(N, k=1, /, *, to_show_num_bits6fail=False, composite_ok=False, no_II=False, with_position6ok=False):
    'N/uint -> may (n0, n1) # via factor_pint__near_sqrtN_(N*II[p | [p:<-PRIMRES[:sz]]]) where [sz:<-[0..=floor_log2(n)**2]] # [[log2(N)**4 == N] -> [N == 2**16]]'
    max_sz = floor_log2(N)**(2 if not no_II else 3)
    if composite_ok:
        vs = range(1, 2+max_sz)
    else:
        ps = islice(iter_sieve4primes_ge_(0), 0, max_sz)
        vs = chain([1], ps)
    vs
    u = N
    for j, v in enumerate(vs):
        if no_II:
            u = v*N
        else:
            u *= v
        m = factor_pint__near_sqrtN_(u, k)
        match m:
            case (n0, n1):
                n2 = gcd(n0, N)
                if 1 < n2 < N:
                    n3 = N//n2
                    (n0, n1) = sorted([n2,n3])
                    return (n0, n1) if not with_position6ok else ((n0, n1), (j, v))
    if to_show_num_bits6fail:
        print('fail:', floor_log2(u), 'bits')
            #23999
    return None

def try_factor_pint__near_sqrtNmulCmulZpow_(N, k=1, /, *, force6sprp=False, with_position6ok=False, verbose=False, ground_scale=1):
    'N/uint -> may (n0, n1) # via factor_pint__near_sqrtN_(N*c*2**ez) where [c:<-[1..]][ez:<-[0..=floor_log2(n)**2]]'
    #TODO:trial_division split out to iter both
    check_int_ge(1, N)
    check_int_ge(1, ground_scale)
    if N < 4:
        if verbose:print_err('N < 4')
        return None
    ###########################
    trbl = detect_strong_probable_prime__not_waste_too_much_time_(N)
    match trbl:
        case 0:
            #composite
            pass
        case 1:
            #prime
            if verbose:print_err('N is prime')
            return None
        case -1:
            #sprp
            if verbose:print_err('N is sprp')
            if force6sprp:
                #sprp ok
                pass
            else:
                #reject sprp
                raise IsStrongProbablePrimeError(N)
        case _:
            raise 000
        #case _:
    ###########################
    ps = iter_sieve4primes_ge_(0)
    it = enumerate(ps, 1)
    lbN = 1+floor_log2(N)
    assert lbN > 0
    #ez2NmulZpow = None
    last_c = 0
    gNmulC = 0 # [c==0]
    gN = ground_scale*N
    done = False
    try:
      while 1:
        if verbose:print_err(f'trial_division: from PRIMRES[{last_c}]')
        #######################
        for c, pc in islice(it, 0, lbN):
            if verbose:print_err(f'trial_division: @PRIMRES[{c-1}]=={pc}')
            if N%pc == 0:
                if pc < N:
                    if verbose:print_err(f'trial_division: @PRIMRES[{c-1}]=={pc}')
                    n0 = pc
                    n1 = N//n0
                    777;done = True
                    777;position = (False, (c, pc))
                else:
                    if verbose:print_err(f'trial_division: [N is prime]@PRIMRES[{c-1}]=={pc}')
                break
        if done:break
        if pc**2 > N: break
        #if not ez2NmulZpow: ez2NmulZpow = [N<<ez for ez in range(lbN)]
        if verbose:print_err(f'trial_division: fail@PRIMRES[{last_c}:{c}]')
        #######################
        c
        assert last_c < c
        for c in range(1+last_c, 1+c):
            gNmulC += gN
            if verbose:print_err(f'factor_pint__near_sqrtN_(N*{c})')
            for ez in range(lbN):
                gNmulCmulZpow = gNmulC << ez
                if verbose:print_err(f'factor_pint__near_sqrtN_(N*{c}*2**{ez})')
                m = factor_pint__near_sqrtN_(gNmulCmulZpow, k)
                if m:
                    #bug:(n0, n1) = m
                        #here cause bug:once pre-『done』 using『if n0:break』
                    (u0, u1) = m
                    n2 = gcd(u0, N)
                    if 1 < n2 < N:
                        if verbose:print_err(f'factor_pint__near_sqrtN_(N*{c}*2**{ez}):succ')
                        n3 = N//n2
                        (n0, n1) = sorted([n2,n3])
                        777;done = True
                        777;position = (True, (c, ez, ground_scale))
                        break
            else:
                continue
            break
        else:
            last_c = c
            continue
        break
        #######################
      #while 1:
    except KeyboardInterrupt:
        print_err(f'try_factor_pint__near_sqrtNmulCmulZpow_({N}):[last_c ={last_c}][log2(N) ~= {lbN}][ground_scale == {ground_scale}]')
        raise
    #try:
    if done:
        assert 1 < n0 <= n1 < N == n0*n1, (N, (n0, n1), n0*n1)
        return (n0, n1) if not with_position6ok else ((n0, n1), position)
    return None


__all__
from seed.math.factor_pint.factor_pint__near_sqrtN import factor_pint__two_digit_number_multiplication_with_second_carry_
from seed.math.factor_pint.factor_pint__near_sqrtN import factor_pint__near_sqrtN_
    #useless: factor_pint__depart_from_sqrtN__via_scaled_to_near_sqrtN_
from seed.math.factor_pint.factor_pint__near_sqrtN import *
