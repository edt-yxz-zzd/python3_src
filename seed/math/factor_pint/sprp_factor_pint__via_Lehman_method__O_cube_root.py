#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/sprp_factor_pint__via_Lehman_method__O_cube_root.py
view ../../python3_src/seed/math/factor_pint/sprp_factor_pint_framework.py
Lehman_method - O(n**/3)
    cbrt - cube root
here:layered_version:layered_Lehman_method

seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root:__doc__ -ht # -ff -df


[[[[[
layered_Lehman_method
<<==:
源起:
以下复制自:view script/整数分解牜平方差牜尝试平衡两因子.py
===
[[
Lehman method
    '/sdcard/0my_files/book/math/factorint/202308/Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
        Squares:page227:Lehman method (Algorithm 5.1.2)

[TIME{Lehman_method(n)} = O(n**/3 * TIME{sqrt(n)})]

[21 < n==p*q][floor(n**/3) < p <= q]:
    [floor(n**/3) < p <= q < ceil(n**(2/3))]
    [k :<- [1..=ceil(n**/3)]]
    [a :<- [ceil((4*k*n)**/2)..=ceil((4*k*n)**/2)+floor((n/(4*k)**3)**/6)]]
    [b := sqrt(a**2-4*k*n)]
    [b%1 == 0] => [gcd(a+b,n) is factor of n]
        # !! [(a+b) < n]

已知:[@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    [abs(u*q - p*v) < q/B]

证明:算法中(k,a)的范围合理
    # let [(u,v) :=> [k==u*v]]
    # [4*k*n == (2*u*q)*(2*p*v) == a**2-b**2 == (a+b)*(a-b)][a>=b]
    # [(2*b) == (a+b)-(a-b) == 2*abs(u*q - p*v) SHOULD_BE small enough]
    # [a**2 == 4*k*n + b**2 >= 4*k*n]
    # [a >= sqrt(4*k*n) == min_A]
    !! [@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    # [b == abs(u*q - p*v) < q/B < (n**(2/3))/B < (n**(2/3))]
    # [4*k*n <= min_A**2 <= a**2 == (min_A+dA)**2 == 4*k*n + b**2]
    # [2*min_A*dA+dA**2 == b**2 <= q**2/B**2]
    # [dA <= q**2/B**2/2/min_A == q**2/B**2/2/sqrt(4*k*n) == max_dA]
    ####bug:let [max_dA <= n**/3]
    #       !! max_dA(B) #see below:『let [max_k(B) <= n**/3]』
    #
    #
    # [k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**2*p/q+1) == max_k]
    # [max_k(B) == ceil(B**2*p/q)]
    # 太大:[max_b(B) == floor(q/B)]
    # [max_dA(B,k) == q**2/B**2/2/sqrt(4*k*n)]
    # [最小化循环步骤]<->[最小化:sum[1+ max_b(B) | [k :<- [1..=max_k(B)]]]]<->[最小化:sum[1+ max_dA(B;k) | [k :<- [1..=max_k(B)]]]]
    #       『+1』 <<== 最外层循环 数量，因为[max_dA==0]时仍旧要加1每循环
    # [SUM <= sum[1+ q**2/B**2/2/sqrt(4*k*n) | [k :<- [1..<=(B**2*p/q)]]]]
    # let [max_k(B) <= n**/3]
    # [(B**2*p/q) <= n**/3]
    # [B <= n**/6 * sqrt(q/p)]
    # let [B := n**/6 * sqrt(q/p)]
    # [max_k(B) <= n**/3]
    # [max_dA == q**2/B**2/2/sqrt(4*k*n) == (n**/6)/4/sqrt(k)]
    # [SUM <= sum[1+ (n**/6)/4/sqrt(k) | [k :<- [1..<=n**/3]]] ~= (n**/3)+ (n**/6)/4 * Integral[1/sqrt(k) | [k :<- [1..<=n**/3]]] ~= (n**/3)+ (n**/6)/4 * 2*sqrt(k:=n**/3) ~= O(n**/3)]
    # DONE
    # ??? [(a+b)<n] <<== [n>=21]
    ##################
    ##################
    ##################
    ##################
    # 尝试 let [max_k(B) <= n**/4]
    #   虽然 前提试除 已经 O(n**/3)，但仍可以强行假设，试图分解
    # [(B**2*p/q) <= n**/4]
    # [B <= n**/8 * sqrt(q/p)]
    # let [B := n**/8 * sqrt(q/p)]
    # [max_k(B) == (B**2*p/q) == n**/4]
    # [max_dA(B,k) == q**2/B**2/2/sqrt(4*k*n) == (n**/4)/4/sqrt(k)]
    # [SUM <= sum[1+ (n**/4)/4/sqrt(k) | [k :<- [1..<=n**/4]]] ~= (n**/4)+ (n**/4)/4 * Integral[1/sqrt(k) | [k :<- [1..<=n**/4]]] ~= (n**/4)+ (n**/4)/4 * 2*sqrt(k:=n**/4) ~= O(n**(3/8)) > O(n**/3)]
    ##################
    ##################
    ##################
    # 尝试 let [max_k(B) <= n**/2]
    #   虽然 这样一来 外层循环 已经 O(n**/2)，但可以看看是否大量max_dA(B,k)小于1 # 其实[k:=n]直接就有[a==2*n][b==0][dA==0]
    # [(B**2*p/q) <= n**/2]
    # [B <= n**/4 * sqrt(q/p)]
    # let [B := n**/4 * sqrt(q/p)]
    # [max_k(B) == (B**2*p/q) == n**/2]
    # [max_dA(B,k) == q**2/B**2/2/sqrt(4*k*n) == 1/4/sqrt(k)] # ===0???
    # [SUM <= sum[1+ 1/4/sqrt(k) | [k :<- [1..<=n**/2]]] ~= (n**/2)+ 1/4 * Integral[1/sqrt(k) | [k :<- [1..<=n**/2]]] ~= (n**/2)+ 1/4 * 2*sqrt(k:=n**/2) ~= O(n**/2) > O(n**/3)] # >_<
    ##################
    ##################
    ##################
    ##################
    ##################
    ######################
    重头再来:
    [k == u*v]
    [a+b == 2*u*q]
    [a-b == 2*v*p > 0]
    [a > b >= 0]
    [4*k*n == (2*u*q)*(2*v*p) == (a+b)*(a-b)]
    [a >= (4*k*n)**/2]
    [b < (a+b)/2 == u*q < k*n**/2]
    !! [@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    [b == abs(u*q - p*v) < q/B]
    [4*k*n <= min_A**2 <= a**2 == (min_A+dA)**2 == 4*k*n + b**2]
    [2*min_A*dA+dA**2 == b**2 <= (q/B)**2]
    [dA <= (q/B)**2/2/min_A == (q/B)**2/2/sqrt(4*k*n) == max_dA]
    [max_dA == (q/B)**2/2/sqrt(4*k*n)]
    [k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**2*p/q+1) == max_k]
    [max_k(B) == (1+B**2*p/q)]
    [max_dA(B,k) == (q/B)**2/2/sqrt(4*k*n)]
    [最小化循环步骤]<->[最小化:sum[1+ max_b(B) | [k :<- [1..=max_k(B)]]]]<->[最小化:sum[1+ max_dA(B;k) | [k :<- [1..=max_k(B)]]]]
        # 『+1』 <<== 最外层循环 数量，因为[max_dA==0]时仍旧要加1每循环
    [SUM <= sum[1+ (q/B)**2/2/sqrt(4*k*n) | [k :<- [1..<=(1+B**2*p/q)]]]]
    [max_k(B) <= 1+n**z]:
        [(1+B**2*p/q) <= 1+n**z]
        [B <= n**(z/2) * sqrt(q/p)]
    let [B := n**(z/2) * sqrt(q/p)]
    [max_k(B) == 1+n**z]
    [max_dA == (q/B)**2/2/sqrt(4*k*n) == n**(1/2-z)/4/sqrt(k)]
    [SUM <= sum[1+ n**(1/2-z)/4/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-z)/4 * Integral[1/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-z)/4 * 2*sqrt(k:=1+n**z) ~= O(n**z + n**(1/2-z/2))]
    [z == 1/2-z/2]:
        [z == 1/3]
    #######
    [gcd(a+b,n) < n]
        <<== [(a+b) < n]
    [a+b
    <= a + q/B
    == a + q / (n**(z/2) * sqrt(q/p))
    == a + n**(1/2-z/2)
    <= sqrt(4*k*n)+max_dA + n**(1/2-z/2)
    == sqrt(4*k*n) + n**(1/2-z)/4/sqrt(k) + n**(1/2-z/2)
    <= sqrt(4*max_k*n) + n**(1/2-z)/4/min_k + n**(1/2-z/2)
    == sqrt(4*(1+n**z)*n) + n**(1/2-z)/4/1 + n**(1/2-z/2)
    <= 2*n**/2 +2*n**(z/2+1/2) + n**(1/2-z)/4 + n**(1/2-z/2)
    == n**/2 *(2 +2*n**(z/2) + n**(-z)/4 + n**(-z/2))
    <= n**/2 *(2 +2*n**(z/2) +2)
    == 2*n**/2 *(2 +n**(z/2))
    ]
    [a+b <= 2*n**/2 *(2 +n**(z/2))]
    [a+b < n] <<==:
        [2*n**/2 *(2 +n**(z/2)) < n]
        [2*(2 +n**(z/2)) < n**/2]
        * [z==1/3]:
            [2*(2 +n**/6) < n**/2]
            [x := n**/6]
            [4 +2*x < x**3]
            [x==2]:
                [4 +2*x == x**3]
            [x > 2]
            [n**/6 > 2]
            [n > 2**6]
            [n > 64] #21???
    [a+b < n] <<== [2*(2 +n**(z/2)) < n**/2]
    # DONE
    ######################
    ######################


]]
[[[
改进搜索次序，一层一层搜索
    =>每一层结束，可以中断；不必非得一次性O(n**/3)
    ######################
    # 以下内容，是复制上面的
    #   再尝试『偷懒』或者说调整为更有高效的搜索次序:
    #       窜改公式『1/(v*B)』-->『1/v/B**t』
    #       或者说:窜改公式『v<=B』-->『v**t<=B』
    ######################
    [k == u*v]
    [a+b == 2*u*q]
    [a-b == 2*v*p > 0]
    [a > b >= 0]
    [4*k*n == (2*u*q)*(2*v*p) == (a+b)*(a-b)]
    [a >= (4*k*n)**/2]
    [b < (a+b)/2 == u*q < k*n**/2]
    原:!! [@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v <= B][abs(u/v - p/q) < 1/(v*B)]]]
    窜改: [t>=1][@[p,q :: pint] -> @[B>1] -> ?[u,v :: pint] -> [[v**t <= B][abs(u/v - p/q) < 1/(v*B)]]]
    [b == abs(u*q - p*v) < q/B]
    [4*k*n <= min_A**2 <= a**2 == (min_A+dA)**2 == 4*k*n + b**2]
    [2*min_A*dA+dA**2 == b**2 <= (q/B)**2]
    [dA <= (q/B)**2/2/min_A == (q/B)**2/2/sqrt(4*k*n) == max_dA]
    [max_dA == (q/B)**2/2/sqrt(4*k*n)]
    原:[k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**2*p/q+1) == max_k]
    窜改:[k == u*v == (u/v)*v**2 < (p/q+1/(v*B))*v**2 == (p/q*v**2+v/B) <= (v**2*p/q+1) <= (B**(2/t)*p/q+1) == max_k]
    [max_k(B) == (1+B**(2/t)*p/q)]
    [max_dA(B,k) == (q/B)**2/2/sqrt(4*k*n)]
    [最小化循环步骤]<->[最小化:sum[1+ max_b(B) | [k :<- [1..=max_k(B)]]]]<->[最小化:sum[1+ max_dA(B;k) | [k :<- [1..=max_k(B)]]]]
        # 『+1』 <<== 最外层循环 数量，因为[max_dA==0]时仍旧要加1每循环
    [SUM <= sum[1+ (q/B)**2/2/sqrt(4*k*n) | [k :<- [1..<=(1+B**(2/t)*p/q)]]]]
    [max_k(B) <= 1+n**z]:
        [(1+B**(2/t)*p/q) <= 1+n**z]
        [B <= n**(t*z/2) * sqrt(q/p)**t]
    let [B := n**(t*z/2) * sqrt(q/p)**t]
    [max_k(B) == 1+n**z]
    [max_dA == (q/B)**2/2/sqrt(4*k*n)
    == (q/n**(t*z/2) / sqrt(q/p)**t)**2/2/sqrt(4*k*n)
    == (q**2/n**(t*z) / (q/p)**t)/4/sqrt(k*n)
    == (q**(2-t) * p**t/n**(t*z))/4/sqrt(k*n)
    == (n**(t-t*z-1/2))/q**(2*t-2)/4/sqrt(k)
    <= (n**(t-t*z-1/2))/n**(t-1)/4/sqrt(k)
    == (n**(1/2-t*z))/4/sqrt(k)
    ]
    [max_dA == (n**(1/2-t*z))/4/sqrt(k)]
    [SUM <= sum[1+ n**(1/2-t*z)/4/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-t*z)/4 * Integral[1/sqrt(k) | [k :<- [1..<=1+n**z]]] ~= (n**z)+ n**(1/2-t*z)/4 * 2*sqrt(k:=1+n**z) ~= O(n**z + n**(1/2+z/2-t*z))]
    [z == 1/2+z/2-t*z]:
        [z == 1/(1+2*t)]
        !! [t >= 1]
        [z <= 1/3]
        计算量:O(n**z)
        计算量:O(n**/(1+2*t))
        计算量翻倍:
            ?_t :=> [n**/(1+2*_t) == ZZZ*n**/(1+2*t)]
            [1/(1+2*_t) == log(n;ZZZ) + 1/(1+2*t)]
            [(1+2*_t) == (1+2*t)/(log(n;ZZZ)*(1+2*t) + 1)]
            [_t == (1/2+t)/(log(n;ZZZ)*(1+2*t) + 1) -1/2]
            [_t - t
            == (1/2+t)/(log(n;ZZZ)*(1+2*t) + 1) -1/2 -t
            == (1/2+t)*log(ZZZ;n)/((1+2*t) + log(ZZZ;n)) -1/2 -t
            == ((log(ZZZ;n)/2+t*log(ZZZ;n)) -((1+2*t)*t + t*log(ZZZ;n)))/((1+2*t) + log(ZZZ;n)) -1/2
            == (log(ZZZ;n)/2 -(1+2*t)*t)/((1+2*t) + log(ZZZ;n)) -1/2
            == (-2*(1+2*t)*t -(1+2*t))/2/((1+2*t) + log(ZZZ;n))
            == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))
            ]
        计算量翻倍公式: [_t -t == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))]
    #######
    [gcd(a+b,n) < n]
        <<== [(a+b) < n]
    [a+b
    <= a + q/B
    == a + q / (n**(t*z/2) * sqrt(q/p)**t)
    == a + n**(t/2*(1-z)) /q**(t-1)
    <= sqrt(4*k*n)+max_dA + n**(t/2*(1-z)) /q**(t-1)
    == sqrt(4*k*n) + (n**(1/2-t*z))/4/sqrt(k) + n**(t/2*(1-z)) /q**(t-1)
    <= sqrt(4*max_k*n) + n**(1/2-t*z)/4/min_k + n**(t/2*(1-z)) /q**(t-1)
    == sqrt(4*(1+n**z)*n) + n**(1/2-t*z)/4/1 + n**(t/2*(1-z)) /q**(t-1)
    <= 2*n**/2 +2*n**(z/2+1/2) + n**(1/2-t*z)/4 + n**(t/2*(1-z)) /q**(t-1)
    == n**/2 *(2 +2*n**(z/2) + n**(-t*z)/4 + n**(((t-1)-t*z)/2) /q**(t-1))
    # t消失，归同
    <= n**/2 *(2 +2*n**(z/2) +2)
    == 2*n**/2 *(2 +n**(z/2))
    ]
    [a+b <= 2*n**/2 *(2 +n**(z/2))]
    [a+b < n] <<==:
        [2*n**/2 *(2 +n**(z/2)) < n]
        [2*(2 +n**(z/2)) < n**/2]
        * [z==1/3]:
            [2*(2 +n**/6) < n**/2]
            [x := n**/6]
            [4 +2*x < x**3]
            [x==2]:
                [4 +2*x == x**3]
            [x > 2]
            [n**/6 > 2]
            [n > 2**6]
            [n > 64] #21???
    [a+b < n] <<== [2*(2 +n**(z/2)) < n**/2]
    # DONE
    ######################
    上面的[t>=1]可以从大值开始尝试，直至1:
    [t :<- [100,99..=1]]:
        # 也不必非得整数t，可按计算量翻倍逐次降低t
        # 计算量翻倍公式: [_t -t == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))]
        [z == 1/(1+2*t)]
        [max_k(B) == 1+n**z]
        [max_dA(B,k) == (n**(1/2-t*z))/4/sqrt(k)]
    ######################

===
]]]




]]]]]





>>> for x in _iter_dt_t_pairs(20, 1000, 100):x
(-16.819733555370526, 83.18026644462947)
(-11.996956886854864, 71.1833095577746)
(-8.988362583351652, 62.194946974422955)
(-6.9854126063520035, 55.20953436807095)
(-5.584846088769206, 49.62468827930174)
(-4.567118016382435, 45.057570262919306)
(-3.804350487264969, 41.25321977565434)
(-3.217943702034709, 38.03527607361963)
(-2.7574191850471856, 35.277856888572444)
(-2.3891525696355687, 32.888704318936874)
(-2.0900434656201528, 30.798660853316722)
(-1.8437956716051174, 28.954865181711604)
(-1.6386459732975454, 27.316219208414058)
(-1.4659307972971225, 25.850288411116935)
(-1.3191551608056047, 24.53113325031133)
(-1.1933723394953932, 23.337760910815938)
(-1.0847611372139467, 22.252999773601992)
(-0.9903319520342139, 21.262667821567778)
(-0.9077186619911025, 20.354949159576677)
(-0.8350288408515761, 19.519920318725102)
>>> for x in _iter_dt_t_pairs(5, 1000, 5):x
(-0.05984174085064293, 4.940158259149357)
(-0.058553562476167255, 4.8816046966731905)
(-0.0573065359761908, 4.8242981606969995)
(-0.05609892698052394, 4.768199233716476)
(-0.05492909153638032, 4.713270142180095)
>>> for i, x in [*enumerate(_iter_dt_t_pairs(330, 1000, 100))][-10:]:print(i, x, sep=':')
320:(-0.004719928567658735, 1.0338593733306887)
321:(-0.0046910583067993755, 1.0291683150238893)
322:(-0.004662452123231678, 1.0245058629006576)
323:(-0.004634106806046706, 1.019871756094611)
324:(-0.004606019192989324, 1.0152657369016216)
325:(-0.004578186169576197, 1.0106875507320454)
326:(-0.004550604668232369, 1.006136946063813)
327:(-0.0045232716674460105, 1.001613674396367)
328:(-0.004496184190940874, 0.9971174902054262)
329:(-0.004469339306866046, 0.9926481508985602)

>>> _count_num_dt_t_pairs_until(1.0, 44**2, 100)
636
>>> _count_num_dt_t_pairs_until(1.0, 66**2, 100)
1431
>>> _count_num_dt_t_pairs_until(1.0, 88**2, 100)
2543
>>> for i in range(12):_count_num_dt_t_pairs_until(1.0, 2**i, 100)
1
1
2
3
6
11
22
43
85
169
337
673


>>> try_factor1_pint__via_Lehman_method__original_(9999)
3
>>> try_factor1_pint__via_Lehman_method__original_(9999, to_output_statistics=True) # trial_division only
(3, 0, 2)
>>> try_factor1_pint__via_Lehman_method__original_(15, to_output_statistics=True) # _ge1_le21 # trial_division only
(3, 0, 0)

for i in {17..100} ; do echo $i ; factor $[$i**2-2] $[$i**2+2] ; done
for i in {17..30} ; do { if [[ "$i: $i" == $(factor $i) ]] ; then echo $i ; fi } done
for i in {17..100} ; do { if [[ "$i: $i" == $(factor $i) ]] ; then for j in $[$i**2-2] $[$i**2+2] ; do { if [[ "$j: $j" == $(factor $j) ]] ; then echo $i $j ; fi } done ; fi } done
19 359
29 839
37 1367
43 1847
47 2207
61 3719
71 5039
89 7919
>>> pq_ls = [(19, 359), (29, 839), (37, 1367), (43, 1847), (47, 2207), (61, 3719), (71, 5039), (89, 7919)]
>>> for (p,q) in pq_ls:((p,q), try_factor1_pint__via_Lehman_method__original_(p*q, to_output_statistics=True)) # [num_steps ~<= 5*n**/3]
((19, 359), (359, 17, 72))
((29, 839), (839, 27, 115))
((37, 1367), (1367, 35, 151))
((43, 1847), (1847, 41, 176))
((47, 2207), (2207, 45, 193))
((61, 3719), (3719, 59, 254))
((71, 5039), (5039, 69, 298))
((89, 7919), (7919, 87, 377))


for i in {11..100} ; do { if [[ "$i: $i" == $(factor $i) && "$[i+2]: $[i+2]" == $(factor $[i+2]) ]] ; then echo $i ; fi } done
11
17
29
41
59
71
>>> p_ls =[11, 17, 29, 41, 59, 71]
>>> for p in p_ls:((p,q:=p+2), try_factor1_pint__via_Lehman_method__original_(p*q, to_output_statistics=True))
((11, 13), (13, 1, 6))
((17, 19), (19, 1, 7))
((29, 31), (31, 1, 10))
((41, 43), (43, 1, 13))
((59, 61), (61, 1, 16))
((71, 73), (73, 1, 18))








try_factor1_pint__via_Lehman_method__layered_
    :: n/int{>64} -> old_t/T -> new_ts/(Iter T) -> (imay_proper_factor/int, last_t/T, num_scales, num_steps, sts/[info_per_round])
>>> for (p,q) in pq_ls:((p,q), try_factor1_pint__via_Lehman_method__layered_(p*q, -1, range(1, 6)[::-1]))
((19, 359), (19, 1, 6, 36, [((None, 5), (3, 11)), ((5, 4), (0, 0)), ((4, 3), (1, 4)), ((3, 2), (2, 8)), ((2, 1), (0, 13))]))
((29, 839), (29, 1, 8, 52, [((None, 5), (3, 11)), ((5, 4), (1, 4)), ((4, 3), (1, 4)), ((3, 2), (3, 12)), ((2, 1), (0, 21))]))
((37, 1367), (37, 1, 9, 63, [((None, 5), (3, 11)), ((5, 4), (1, 4)), ((4, 3), (1, 4)), ((3, 2), (4, 16)), ((2, 1), (0, 28))]))
((43, 1847), (43, 1, 10, 72, [((None, 5), (3, 11)), ((5, 4), (1, 4)), ((4, 3), (2, 8)), ((3, 2), (4, 16)), ((2, 1), (0, 33))]))
((47, 2207), (47, 1, 11, 79, [((None, 5), (3, 11)), ((5, 4), (1, 4)), ((4, 3), (2, 8)), ((3, 2), (5, 20)), ((2, 1), (0, 36))]))
((61, 3719), (61, 1, 12, 96, [((None, 5), (4, 15)), ((5, 4), (0, 0)), ((4, 3), (2, 8)), ((3, 2), (6, 24)), ((2, 1), (0, 49))]))
((71, 5039), (71, 1, 13, 109, [((None, 5), (4, 15)), ((5, 4), (1, 4)), ((4, 3), (2, 8)), ((3, 2), (6, 24)), ((2, 1), (0, 58))]))
((89, 7919), (89, 1, 15, 133, [((None, 5), (4, 15)), ((5, 4), (1, 4)), ((4, 3), (2, 8)), ((3, 2), (8, 32)), ((2, 1), (0, 74))]))

>>> for p in p_ls:((p,q:=p+2), try_factor1_pint__via_Lehman_method__layered_(p*q, -1, range(1, 6)[::-1]))
((11, 13), (13, 5, 1, 3, [((None, 5), (1, 3))]))
((17, 19), (19, 5, 1, 3, [((None, 5), (1, 3))]))
((29, 31), (31, 5, 1, 3, [((None, 5), (1, 3))]))
((41, 43), (43, 5, 1, 3, [((None, 5), (1, 3))]))
((59, 61), (61, 5, 1, 4, [((None, 5), (1, 4))]))
((71, 73), (73, 5, 1, 4, [((None, 5), (1, 4))]))


2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667
>>> try_factor1_pint__via_Lehman_method__layered_((2**13-1)*(2**17-1), -1, range(1, 6)[::-1])
(131071, 3, 17, 68, [((None, 5), (7, 27)), ((5, 4), (4, 16)), ((4, 3), (6, 25))])
>>> try_factor1_pint__via_Lehman_method__layered_((2**17-1)*(2**31-1), -1, range(1, 6)[::-1]) # worse_case_near_cube_root:[log2(118934) ~= 16.9]
(2147483647, 1, 17210, 122154, [((None, 5), (21, 84)), ((5, 4), (20, 80)), ((4, 3), (76, 302)), ((3, 2), (709, 2754)), ((2, 1), (16384, 118934))])

float:
>>> try_factor1_pint__via_Lehman_method__layered_((2**13-1)*(2**17-1), -1.0, map(float, range(1, 6)[::-1]))
(131071, 3.0, 17, 68, [((None, 5.0), (7, 27)), ((5.0, 4.0), (4, 16)), ((4.0, 3.0), (6, 25))])
>>> try_factor1_pint__via_Lehman_method__layered_((2**17-1)*(2**31-1), -1.0, map(float, range(1, 6)[::-1]))
(2147483647, 1.0, 17210, 122154, [((None, 5.0), (21, 84)), ((5.0, 4.0), (20, 80)), ((4.0, 3.0), (76, 302)), ((3.0, 2.0), (709, 2754)), ((2.0, 1.0), (16384, 118934))])









py_adhoc_call   seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root   ,iter_try_factor1_pint__via_Lehman_method__layered_   ='(2**17-1)*(2**31-1)' =-1 ='range(1, 6)[::-1]'
((None, 5), (21, 84))
((5, 4), (20, 80))
((4, 3), (76, 302))
((3, 2), (709, 2754))
((2, 1), (16384, 118934))


py_adhoc_call  { +to_show_StopIteration_value } seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root   ,iter_try_factor1_pint__via_Lehman_method__layered__easy_   ='(2**17-1)*(2**31-1)'
((None, 2.50211826831969), (255, 1038))
((2.50211826831969, 2.169180468784931), (262, 1035))
((2.169180468784931, 1.9016954462071483), (525, 2072))
((1.9016954462071483, 1.6830786952006025), (1033, 4111))
((1.6830786952006025, 1.50111812611176), (2067, 8228))
((1.50111812611176, 1.3470813450750774), (4134, 16459))
((1.3470813450750774, 1.2150745478056086), (8269, 32924))
((1.2150745478056086, 1.1006823948238753), (298, 17138))
(2147483647, 1.1006823948238753, 16843, 83005, [((None, 2.50211826831969), (255, 1038)), ((2.50211826831969, 2.169180468784931), (262, 1035)), ((2.169180468784931, 1.9016954462071483), (525, 2072)), ((1.9016954462071483, 1.6830786952006025), (1033, 4111)), ((1.6830786952006025, 1.50111812611176), (2067, 8228)), ((1.50111812611176, 1.3470813450750774), (4134, 16459)), ((1.3470813450750774, 1.2150745478056086), (8269, 32924)), ((1.2150745478056086, 1.1006823948238753), (298, 17138))])




from seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root import *
]]]'''#'''
__all__ = r'''
try_factor1_pint__via_Lehman_method__original_
try_factor1_pint__via_Lehman_method__layered_
    iter_try_factor1_pint__via_Lehman_method__layered_
    iter_try_factor1_pint__via_Lehman_method__layered__easy_


icbrt
calc_max_k__float_
calc_max_k__int_
calc_t5max_k_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from seed.math.factor_pint.sprp_factor_pint_framework import IFramework4sprp_factor_pint
from seed.iters.generator_iterator_capturer import GeneratorIteratorCapturer
from seed.math.floor_ceil import floor_kth_root_, ceil_kth_root_
from math import isqrt, gcd, floor, log
from decimal import Decimal, Context, localcontext

from seed.tiny_.check import check_type_is, check_int_ge
#from itertools import islice
#
#from seed.abc.abc__ver1 import abstractmethod, override, ABC
#from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#TODO:IFramework4sprp_factor_pint
#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError


isqrt
def icbrt(n, /):
    return floor_kth_root_(3, n)


def _ge1_le21(n, /):
    # [1 <= n <= 21]
    if n < 4:
        # [1 <= n <= 3]
        return -1 # [n==1]or[is_prime(n)]
    # [4 <= n <= 21 < 5**2]
    if n&1 == 0:
        return 2
    elif n%3 == 0:
        return 3
    return -1 # [is_prime(n)]
def try_factor1_pint__via_Lehman_method__original_(n, /, *, to_output_statistics=False, min_divisor4trial_division=2):
    'O(n**/3) => n/int{>=1} -> imay proper_factor{n} if not to_output_statistics else (imay_proper_factor, num_scales, num_steps) # [[imay_proper_factor == -1] <-> [[n==1]or[is_prime(n)]]] # [num_steps ~<= 5*n**/3]'
    check_type_is(bool, to_output_statistics)
    check_type_is(int, min_divisor4trial_division)
    check_int_ge(1, n)
    # [n >= 1]
    num_scales = 0
    num_steps = 0
    def _mk_result(imay_proper_factor, /):
        assert imay_proper_factor == -1 or (1 < imay_proper_factor < n and n%imay_proper_factor==0)
        return (imay_proper_factor, num_scales, num_steps) if to_output_statistics else imay_proper_factor

    # [n >= 1]
    if n <= 21:
        # [1 <= n <= 21]
        imay_proper_factor = _ge1_le21(n)
        return _mk_result(imay_proper_factor)
    # [n > 21]

    icbrtN = icbrt(n) # == floor(n**/3)
    for d in range(max(2,min_divisor4trial_division), icbrtN+1):
        num_steps += 1
        if n%d == 0:
            assert 1 < d < n
            return _mk_result(d)
    # [@[d :<- [2..=floor(n**/3)]] -> [n%d =!= 0]]
    # [n > 21]
    # [[not is_prime(n)] -> ?[p,q :: int] -> [n==p*q][floor(n**/3) < p <= q]]
    for k in range(1, icbrtN+1):
        # [k :<- [1..=ceil(n**/3)]]
        num_scales += 1
        _4kn = 4*k*n
        lowB4min_A = isqrt(_4kn)
        upB4min_A = lowB4min_A+1
        upB4max_dA = 1+icbrt(isqrt(n//(4*k)**3))
        upB4max_A = upB4min_A + upB4max_dA
        for a in range(lowB4min_A, 1+upB4max_A):
            # [a :<- [ceil((4*k*n)**/2)..=ceil((4*k*n)**/2)+floor((n/(4*k)**3)**/6)]]
            num_steps += 1
            bb = a**2-_4kn
            if bb < 0:
                # due to [lowB4min_A < min_A]
                continue
            b = isqrt(bb)
            if b**2 == bb:
                # [b := sqrt(a**2-4*k*n)]
                ft_of_4kn = a+b
                assert 1 < ft_of_4kn < n, (n, k, a, b, ft_of_4kn)
                ft4n = gcd(ft_of_4kn, n)
                assert 1 < ft4n < n, (n, k, a, b, ft_of_4kn, ft4n)
                return _mk_result(ft4n)
            #end-if b**2 == bb:
        #end-for a in range(lowB4min_A, 1+upB4max_A):
    #end-for k in range(1, icbrtN+1):
    # ==>>:
    # !! [n > 21]
    # [not$ [?[p,q :: int] -> [n==p*q][floor(n**/3) < p <= q]]]
    #
    # !! [[not is_prime(n)] -> ?[p,q :: int] -> [n==p*q][floor(n**/3) < p <= q]]
    # [is_prime(n)]
    #
    return _mk_result(-1) # [is_prime(n)]
#end-def try_factor1_pint__via_Lehman_method__original_(n, /):


def _count_num_dt_t_pairs_until(min_t, c, t, /):
    'min_t{>0} -> c -> t -> len([*_iter_dt_t_pairs_until(min_t, c, t)])'
    sz = 0
    for sz, _ in enumerate(_iter_dt_t_pairs_until(min_t, c, t), 1): pass
    return sz
def _iter_dt_t_pairs_until(min_t, c, t, /):
    'min_t{>0} -> c -> t -> (Iter (dt, t)){only last t < min_t}'
    assert min_t > 0
    while 1:
        dt = _diff_t(c, t)
        t += dt
        yield (dt, t)
        if t < min_t:break
def _iter_dt_t_pairs(sz, c, t, /):
    'sz -> c -> t -> (Iter (dt, t)){len=sz}'
    for _ in range(sz):
        dt = _diff_t(c, t)
        t += dt
        yield (dt, t)
def _diff_t(c, t, /):
    'c -> t -> dt # [dt == (_t-t) == (-(1+2*t)**2/2/((1+2*t) + c))] # [c:=log(ZZZ;n)] #计算量翻倍公式: [_t -t == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))]'
    x = (1+2*t)
    dt = (-x**2/(x + c)/2)
    return dt

def calc_t5max_k_(n, max_k, /):
    'n/pint{>=27} -> max_k/pint{>=3} -> t{n,max_k:=min(max_k,n**/3)}/float{>=1}'
    check_int_ge(3, max_k)
    check_int_ge(27, n)
        # !! [min_n >= min_k**3 == 3**3]
    # [max_k >= 3]
    # [n >= 27]


    # [z == 1/(1+2*t)]
    # [max_k(B) == 1+n**z]
    # [z == log(n;max_k-1)]
    # [(1+2*t) == log(max_k-1;n)]
    # [t == (log(max_k-1;n)-1)/2]
    r = log(n, max_k-1) # ==log(max_k-1;n)
    t = (r-1)/2
    if t < 1:
        # [[t < 1] -> [max_k > n**/3]]
        #assert max_k**3 > n
        assert max_k > icbrt(n)
        t = 1.0
    check_type_is(float, t)
    return t


def calc_max_k__float_(n, t, /):
    # calc_max_k_
    'n->t->max_k # [t :: float]'
    # [z == 1/(1+2*t)]
    # [max_k(B) == 1+n**z]
    ctx = Context(prec=max(4*len(t.hex()), n.bit_length()))
    with localcontext(ctx):
        t = Decimal.from_float(t)
        n = Decimal(n)
        rt = (n.ln()/(1+2*t)).exp()
        rt = floor(rt)
    check_type_is(int, rt)
    max_k = 1+rt
    return max_k
def calc_max_k__int_(n, t, /):
    # calc_max_k_
    'n->t->max_k # [t :: pint]'
    # [z == 1/(1+2*t)]
    # [max_k(B) == 1+n**z]
    max_k = 1+floor_kth_root_(1+2*t, n)
    return max_k
def _calc_main_term4max_dA__int_(n, t, /):
    # calc_main_term4max_dA_
    # it turnout that calc_main_term4max_dA_ is almost the same as calc_max_k_
    'n->t->main_term4max_dA # [t :: pint]'
    # [z == 1/(1+2*t)]
    # [max_dA(B,k) == (n**(1/2-t*z))/4/sqrt(k)]
    #   [main_term4max_dA =[def]= (n**(1/2-t*z))**2]
    # == (n**(1-2*t*z))
    # == (n**(1-2*t/(1+2*t)))
    # == (n**/(1+2*t))
    # == (n**z)
    main_term4max_dA = 1+floor_kth_root_(1+2*t, n)
    return main_term4max_dA
def _raw_try_factor1_pint__via_Lehman_method__layered_(may_old_t, new_t, n, calc_max_k_, min_divisor4trial_division, /):
  ''\
    'may old_t -> new_t -> n/int{>64} -> (calc_max_k_/(n->t->max_k)) ->  (imay_proper_factor, num_scales, num_steps) # see:calc_max_k__int_,calc_max_k__float_'
    #'may old_t -> new_t -> n -> (calc_max_k_/(n->t->max_k)) -> (calc_main_term4max_dA_/(n->t->main_term4max_dA)) -> (imay_proper_factor, num_scales, num_steps) # [z == 1/(1+2*t)][main_term4max_dA =[def]= (n**(1/2-t*z))**2]'
  # main():goto
  if 1:
    #max_k = calc_max_k_(n, t)
    #max_dA = calc_max_dA_(n, t, k)
    #main_term4max_dA = calc_main_term4max_dA_(n, t)
    #   [main_term4max_dA =[def]= (n**(1/2-t*z))**2]
    # it turnout that calc_main_term4max_dA_ is almost the same as calc_max_k_
    #   see:_calc_main_term4max_dA__int_ vs calc_max_k_
    #   NOTE: one ceil and the other floor_kth_root_
    calc_main_term4max_dA_ = calc_max_k_
  if 1:
    #[z == 1/(1+2*t)]:
    #    计算量:O(n**z)
    #    计算量:O(n**/(1+2*t))
    #[t :<- [100,99..=1]]:
    #    # 也不必非得整数t，可按计算量翻倍逐次降低t
    #    # 计算量翻倍公式: [_t -t == -(1+2*t)**2/2/((1+2*t) + log(ZZZ;n))]
    #    [z == 1/(1+2*t)]
    #    [max_k(B) == 1+n**z]
    #    [max_dA(B,k) == (n**(1/2-t*z))/4/sqrt(k)]

    ######################
    # !! [num_steps ~<= 5*n**/3]
    # => [TIME(trial_division_part)/TIME(loop_loop_part) ~= 1/4]
    ######################
    #check_int_ge(21, n)
    # [n > 21]
    check_int_ge(64, n)
    # [n > 64]
    if not may_old_t is None:
        old_t = may_old_t
    old_max_k = calc_max_k_(n, old_t) if not may_old_t is None else 0
    new_max_k = calc_max_k_(n, new_t)
    check_int_ge(0, old_max_k)
    check_int_ge(1, new_max_k)
    old_main_term4max_dA = calc_main_term4max_dA_(n, old_t) if not may_old_t is None else None
    new_main_term4max_dA = calc_main_term4max_dA_(n, new_t)
    def calc_max_dA_(n, t, k, /):
        'n->t->k->max_dA'
        # [z == 1/(1+2*t)]
        # [max_dA(B,k) == (n**(1/2-t*z))/4/sqrt(k)]
        # [main_term4max_dA =[def]= (n**(1/2-t*z))**2]
        if t is new_t:
            main_term4max_dA = new_main_term4max_dA
        elif t is old_t:
            main_term4max_dA = old_main_term4max_dA
        else:
            raise 000
        main_term4max_dA
        max_dA = 1+isqrt(main_term4max_dA//16//k)
        return max_dA
    #end-def calc_max_dA_(n, t, k, /):

    num_scales = 0
    num_steps = 0
    def _mk_result(imay_proper_factor, /):
        assert imay_proper_factor == -1 or (1 < imay_proper_factor < n and n%imay_proper_factor==0)
        return (imay_proper_factor, num_scales, num_steps)

    # [n > 64]

    for d in range(max(2, min_divisor4trial_division,1+old_max_k), 1+new_max_k):
        num_steps += 1
        if n%d == 0:
            assert 1 < d < n
            return _mk_result(d)
    # [n > 64]
    def _on_k_mix(k):
        '-> (_4kn, (old_upB4max_A|lowB4min_A), new_upB4max_A)'
        _4kn = 4*k*n
        lowB4min_A = isqrt(_4kn)
        upB4min_A = lowB4min_A+1
        old_max_dA = calc_max_dA_(n, old_t, k)
        new_max_dA = calc_max_dA_(n, new_t, k)
        old_upB4max_A = upB4min_A + old_max_dA
        new_upB4max_A = upB4min_A + new_max_dA
        return (_4kn, old_upB4max_A, new_upB4max_A)
    def _on_k_new(k):
        '-> (_4kn, (old_upB4max_A|lowB4min_A), new_upB4max_A)'
        _4kn = 4*k*n
        lowB4min_A = isqrt(_4kn)
        upB4min_A = lowB4min_A+1
        #old_max_dA = calc_max_dA_(n, old_t, k)
        new_max_dA = calc_max_dA_(n, new_t, k)
        #old_upB4max_A = upB4min_A + old_max_dA
        new_upB4max_A = upB4min_A + new_max_dA
        return (_4kn, lowB4min_A, new_upB4max_A)
    def _iter_k_exs():
        '-> Iter (k, _4kn, (old_upB4max_A|lowB4min_A), new_upB4max_A)'
        for k in range(1,1+old_max_k):
            (_4kn, old_upB4max_A, new_upB4max_A) = _on_k_mix(k)
            if not old_upB4max_A < new_upB4max_A:
                break
            yield (k, _4kn, old_upB4max_A, new_upB4max_A)
        for k in range(max(1,1+old_max_k), 1+new_max_k):
            # [k :<- [1..=ceil(n**/3)]]
            (_4kn, lowB4min_A, new_upB4max_A) = _on_k_new(k)
            yield (k, _4kn, lowB4min_A, new_upB4max_A)
    #def _iter_k_exs():
  def main():
    nonlocal num_scales, num_steps
    for (k, _4kn, lowB4min_A, new_upB4max_A) in _iter_k_exs():
        # (k, _4kn, (old_upB4max_A|lowB4min_A), new_upB4max_A)
        num_scales += 1
        for a in range(lowB4min_A, 1+new_upB4max_A):
            # [a :<- [ceil((4*k*n)**/2)..=ceil((4*k*n)**/2)+floor((n/(4*k)**3)**/6)]]
            num_steps += 1
            bb = a**2-_4kn
            if bb < 0:
                # due to [lowB4min_A < min_A]
                continue
            b = isqrt(bb)
            if b**2 == bb:
                # [b := sqrt(a**2-4*k*n)]
                ft_of_4kn = a+b
                assert 1 < ft_of_4kn < n, (n, k, a, b, ft_of_4kn)
                ft4n = gcd(ft_of_4kn, n)
                assert 1 < ft4n < n, (n, k, a, b, ft_of_4kn, ft4n)
                return _mk_result(ft4n)
            #end-if b**2 == bb:
        #end-for a in range(lowB4min_A, 1+upB4max_A):
    #end-for k in range(1, icbrtN+1):

    return _mk_result(-1) # fail # (prime or compisite) both possible
  if 1:
    return main()
#end-def _raw_try_factor1_pint__via_Lehman_method__layered_(may_old_t, new_t, n, calc_max_k_, calc_max_dA_, /):
#
_inf = float('inf')
def try_factor1_pint__via_Lehman_method__layered_(n, old_t, new_ts, /, *, min_divisor4trial_division=2):
    r'''[[[
    :: n/int{>64} -> old_t/T -> new_ts/(Iter T) -> (imay_proper_factor/int, last_t/T, num_scales, num_steps, sts/[info_per_round])
    [T <- {int,float}]
    O(sum{n**/(1+2*t) | t<-new_ts} -[old_t>1]n**/(1+2*old_t))

    :: n/int{>64}
    -> old_t/T{[not 0<=old_t<=1]}
    -> new_ts/(Iter T{new_t<old_t or old_t<0}){strict_decreasing}
    -> (imay_proper_factor, last_t/T, num_scales, num_steps, sts/[((may_old_t,new_t), (_num_scales,_num_steps))])

    [[imay_proper_factor == -1][last_t==1] -> [[n==1]or[is_prime(n)]]]
    [num_steps ~<= sum [5*n**/(1+2*t) | [t :<- new_ts]] -[old_t>1]5*n**/(1+2*old_t)]

    #]]]'''#'''
    #, to_output_statistics=False
    #, to_output_last_t=False
    'O(sum{n**/(1+2*t) | t<-new_ts} -[old_t>1]n**/(1+2*old_t)) => [T <- {int,float}] => n/int{>64} -> old_t/T{[not 0<=old_t<=1]} -> new_ts/(Iter T{new_t<old_t or old_t<0}){decreasing} -> (imay_proper_factor, last_t/T, num_scales, num_steps, sts/[((may_old_t,new_t), (_num_scales,_num_steps))]) # [[imay_proper_factor == -1][last_t==1] -> [[n==1]or[is_prime(n)]]] # [num_steps ~<= sum [5*n**/(1+2*t) | [t :<- new_ts]] -[old_t>1]5*n**/(1+2*old_t)]'
    g = iter_try_factor1_pint__via_Lehman_method__layered_(n, old_t, new_ts, min_divisor4trial_division=min_divisor4trial_division)
    g = GeneratorIteratorCapturer(g)
    for _ in g:pass
    [r] = g.get_tmay_result()
    return r
def iter_try_factor1_pint__via_Lehman_method__layered__easy_(n, may_old_t=None, /, *, min_divisor4trial_division=2, amplifier=2.0, default_max_k=256):
    '-> (Iter ((may_old_t,new_t), (_num_scales, _num_steps))){generator-return (imay_proper_factor, last_t, num_scales, num_steps, sts)}'
    calc_max_k_ = calc_max_k__float_
    def __(n, may_old_t, /):
        if may_old_t is None:
            old_t = -1.0
            new_max_k = default_max_k
        else:
            old_t = may_old_t
            check_type_is(float, old_t)
            assert old_t > 1
            old_max_k = calc_max_k_(n, old_t)
            new_max_k = floor(amplifier*old_max_k)
        old_t
        new_max_k
        new_t = calc_t5max_k_(n, new_max_k)
        return (old_t, new_t)
    def iter_new_ts(n, new_t, /):
        while 1:
            yield new_t
            if new_t <= 1.0:
                break
            new_max_k = calc_max_k_(n, new_t)
            new_max_k = floor(amplifier*new_max_k)
            new_t = calc_t5max_k_(n, new_max_k)
    def main(n, /):
        (old_t, new_t) = __(n, may_old_t)
        new_ts = iter_new_ts(n, new_t)
        it = iter_try_factor1_pint__via_Lehman_method__layered_(n, old_t, new_ts, min_divisor4trial_division=min_divisor4trial_division)
        return it
        #return (yield from it)
    return main(n)

def iter_try_factor1_pint__via_Lehman_method__layered_(n, old_t, new_ts, /, *, min_divisor4trial_division=2):
    '-> (Iter ((may_old_t,new_t), (_num_scales, _num_steps))){generator-return (imay_proper_factor, last_t, num_scales, num_steps, sts)}'
    #check_type_is(bool, to_output_statistics)
    #check_type_is(bool, to_output_last_t)
    check_type_is(int, min_divisor4trial_division)
    check_int_ge(64, n)
    # [n > 64]
    min_divisor4trial_division = max(2, min_divisor4trial_division)
    sts = []

    T = type(old_t)
    if not T in (int,float):raise TypeError(T)
    calc_max_k_ = calc_max_k__int_ if T is int else calc_max_k__float_

    if 0 <= old_t <= 1: raise ValueError(old_t)
    # [not 0<=old_t<=1]
    may_old_t = None if old_t < 0 else old_t
    777; saved_old_t = old_t
    777; old_t = _inf if old_t < 0 else old_t
    # [old_t==+oo]or[old_t>1]
    # [may_old_t is None]or[may_old_t>1]
    num_scales = 0
    num_steps = 0
    for new_t in new_ts:
        # !! initial:[old_t==+oo]or[old_t>1]
        # !! [prev-new_t >= 1]
        # [old_t >= 1]
        # [may_old_t is None]or[may_old_t>1]or[old_t==1]
        check_type_is(T, new_t)
        if not 1 <= new_t <= old_t:raise ValueError(old_t, new_t)
        # [1 <= new_t < old_t]
        # [1 < old_t]
        # => [may_old_t is None]or[may_old_t>1]
        #
        # [n > 64]
        # [may_old_t is None]or[may_old_t>1]
        (imay_proper_factor, _num_scales, _num_steps) = _raw_try_factor1_pint__via_Lehman_method__layered_(may_old_t, new_t, n, calc_max_k_, min_divisor4trial_division)
        777; sts.append(st:=((may_old_t,new_t), (_num_scales, _num_steps)))
        777; yield st
        777; may_old_t = old_t = new_t
        777; num_scales += _num_scales
        777; num_steps += _num_steps
        if not imay_proper_factor == -1: break
        # [new_t >= 1]
        # [old_t>=1]
        # [may_old_t>=1]
        # [may_old_t is None]or[may_old_t>1]or[old_t==1]
    else:
        imay_proper_factor = -1
    imay_proper_factor
    last_t = saved_old_t if old_t is _inf else old_t
    return (imay_proper_factor, last_t, num_scales, num_steps, sts)#if to_output_statistics else imay_proper_factor
    #return _mk_result(imay_proper_factor)
#end-def try_factor1_pint__via_Lehman_method__layered_(n, /):

__all__
from seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root import *
