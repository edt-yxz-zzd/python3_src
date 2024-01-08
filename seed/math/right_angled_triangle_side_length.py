#__all__:goto
r'''[[[
e ../../python3_src/seed/math/right_angled_triangle_side_length.py




seed.math.right_angled_triangle_side_length
py -m nn_ns.app.debug_cmd   seed.math.right_angled_triangle_side_length -x
py -m nn_ns.app.doctest_cmd seed.math.right_angled_triangle_side_length:__doc__ -ff -v

[[
DONE:rename:iter_right_angled_triangle_side_length_ratios__sorted_by_L_S_M_ --> iter_right_angled_triangle_side_length_ratios__ver1_ --> iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
    ab
    .+1,$s/sorted_by_L_S_M/ver1__difference_ratio
DONE:rename:iter_right_angled_triangle_side_length_ratios__ver2_ --> iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_
    st

DONE:engine-selector
    engine_selector4iter_right_angled_triangle_side_length_ratios_(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse)
        iter_right_angled_triangle_side_length_ratios__ver0__factorisation4hypotenuse_
            iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt #ver0
        iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
        iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_
DONE:无需互素情形:kw:may_max1_hypotenuse,turnoff__coprime
    iter_right_angled_triangle_side_length_triples_(*, may_max1_hypotenuse, turnoff__coprime)
    coprime_ratio vs non_coprime_triple
DONE:猜想推论:无需互素情形 累积数量 ln?
DONE:hypotenuse_side%4==1
DONE:see:iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__
    #GaussInteger.py::effective_combinations__of__fst_key__snd_key:goto
        ==>>只有20中不同次序
    范围 side(s), s(side), side(side)
    rename:互素整数边长直角三角形的边长表达型式二 --> 互素整数边长直角三角形的边长表达型式囗囗以斜边的共轭高斯整数分解的实部虚部为参数
    以斜边平方的整数分解组合出斜边平方的所有共轭高斯整数分解并以实部虚部作为直角边边长
    iter:output fmt:
    iter:sorted by:
    * H,L:
        HOE
        LSM
        ---
        HEO
        LMS
    * O:
        OEH
        OHE
    * S:
        SML
        SLM
    * E:
        EOH
        EHO
    * M:
        MSL
        MLS
]]

[[[
DONE: 其他算法:参数: k,s,t
    # iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_():goto
===
    参数: k,s,t
    bug:[k >= 1][1 <= t < s][gcd(s,t)==1]
    [k >= 1][1 <= t < s][gcd(s,t)==1][s%2 =!= t%2]
    (len_hypotenuse, maybe_odd, must_even) := k*(s**2+t**2, s**2-t**2, 2*s*t)
===
view ../../python3_src/seed/math/GaussInteger.py
view ../../python3_src/seed/math/right_angled_triangle_infos__sorted_by.py
    # [:互素整数边长直角三角形的边长表达型式囗囗以斜边的共轭高斯整数分解的实部虚部为参数:[(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t]]:goto
[@[hypotenuse_side,short_side, middle_side :: int] -> [hypotenuse_side,short_side,middle_side > 0] -> [gcd(hypotenuse_side,short_side,middle_side) == 1] -> [hypotenuse_side**2 == short_side**2 +middle_side**2] -> [short_side <= middle_side] -> [
    [3 <= short_side < middle_side < hypotenuse_side][pairwise_coprime_(hypotenuse_side,short_side,middle_side)][hypotenuse_side%4 == 1][short_side%2 =!= middle_side%2]
    [[(odd_side,even_side) := (short_side,middle_side) if short_side%2==1 else (middle_side,short_side)] -> [s := sqrt_((hypotenuse_side +odd_side)/2)] -> [t := sqrt_((hypotenuse_side -odd_side)/2)] -> [[s%1==0][t%1==0][1 <= t < s][gcd(s,t)==1][s%2 =!= t%2][odd_side%2 == 1][even_side%4 == 0][(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t)]]]
    [[
    ###########boundary###########
    # [:boundary_about__ST__HOE]:here
    # s <~~> t
    [1 <= 1+(s%2) <= t <= s-1 < s]
        # [:boundary_of___T___with_respect_to___S]:goto
    [s >= t+1 >= 1+1 == 2]
        # [:boundary_of___S___with_respect_to___T]:goto

    # s ~~> HOE
    [5 <= s*s +1 <= s*s +(1+(s%2))**2 <= hypotenuse_side <= (2*s*(s-1) +1) == s*s +(s-1)**2]
        # [:boundary_of___hypotenuse_side___with_respect_to___S]:goto
    [3 <= s*s -(s-1)**2 == (2*s-1) <= odd_side <= s*s -(1+(s%2))**2 <= s*s -1]
        # [:boundary_of___odd_side___with_respect_to___S]:goto
    [4 <= 2*s*1 <= 2*s*(1+(s%2)) <= even_side <= 2*s*(s-1)]
        # [:boundary_of___even_side___with_respect_to___S]:goto

    # s <~~ HOE
    [(1 +sqrt_(2*hypotenuse_side -1))/2 <= (ceil_sqrt_(2*hypotenuse_side -1)//2 +1) <= s <= floor_sqrt_(((hypotenuse_side -1)//4)*4) <= sqrt_(hypotenuse_side-1)]
        # [:boundary_of___S___with_respect_to___hypotenuse_side]:goto
    [sqrt_(odd_side +1) <= ceil_sqrt_(((odd_side+4)//4)*4) <= (ceil_sqrt_(odd_side+4)//2 +ceil_sqrt_((odd_side+4)//4)) <= s <= (odd_side +1)//2 <= (odd_side +1)/2]
        # [:boundary_of___S___with_respect_to___odd_side]:goto
    [(1 +sqrt_(2*even_side +1))/2 <= (ceil_sqrt_(2*even_side +1)//2 +1) <= s <= ((even_side//4)*2) <= even_side/2]
        # [:boundary_of___S___with_respect_to___even_side]:goto

    ###### HOE <~~> HOE
    # H <~~> E
    [even_side +1 <= hypotenuse_side <= even_side**2/4 +1]
        # [:boundary_of___hypotenuse_side___with_respect_to___even_side]:goto
    [2*sqrt_(hypotenuse_side -1) <= even_side <= hypotenuse_side -1]
        # [:boundary_of___even_side___with_respect_to___hypotenuse_side]:goto

    # O <~~> E
    [sqrt_(2*even_side +1) <= odd_side <= even_side**2/4 -1]
        # [:boundary_of___odd_side___with_respect_to___even_side]:goto
    [2*sqrt_(odd_side+1) <= even_side <= (odd_side**2 -1)/2]
        # [:boundary_of___even_side___with_respect_to___odd_side]:goto

    # H <~~> O
    [sqrt_(2*hypotenuse_side -1) <= odd_side <= hypotenuse_side -2]
        # [:boundary_of___odd_side___with_respect_to___hypotenuse_side]:goto
    [odd_side +2 <= hypotenuse_side <= (odd_side**2 +1)/2]
        # [:boundary_of___hypotenuse_side___with_respect_to___odd_side]:goto
    ]]
    [[
    ###########monotone###########
    # [:monotone_about__HOE___with_respect_to___S___if_used_min_T]:here
    [[min_S2min_hypotenuse_side_(s) =[def]= s*s +(1+(s%2))**2] -> [@[s :<- [2..]] -> [min_S2min_hypotenuse_side_(s) < min_S2min_hypotenuse_side_(s+1)]]]
        # [:monotone_of___hypotenuse_side___with_respect_to___S]:goto
    [[max_S2max_odd_side_(s) =[def]= s*s -(1+(s%2))**2] -> [@[s :<- [2..]] -> [max_S2max_odd_side_(s) < max_S2max_odd_side_(s+1)]]]
        # [:monotone_of___odd_side___with_respect_to___S]:goto
    [[min_S2min_even_side____min_eq_max_(s) =[def]= 2*s*(1+(s%2))] -> [not$ [@[s :<- [2..]] -> [min_S2min_even_side____min_eq_max_(s) <= min_S2min_even_side____min_eq_max_(s+1)]]]]
        # [:monotone_of___even_side___with_respect_to___S__len_rng_eq1____non_monotonic]:goto
    [[min_S2min_even_side____min_lt_max_(s) =[def]= ((s+1)//2 *4)] -> [@[s :<- [2..]] -> [min_S2min_even_side____min_lt_max_(s) <= min_S2min_even_side____min_lt_max_(s+1)]]]
        # [:monotone_of___even_side___with_respect_to___S__len_rng_gt1]:goto
    ]]
    [[
    ###########boundary###########
    # [:boundary_about__ST__LSM]:here
    [critical_even_param4short_side_(s) =[def]= ((floor_sqrt_(2*s*s) +1)//2 *2)]

    # s ~~> LSM
    [3 <= (2*s-1) <= short_side <= [slack-since-non_coprime_S_T]:max{(s*s -(critical_even_param4short_side_(s) +1 -s)**2), 2*s*(critical_even_param4short_side_(s) -1 -s)} <= (floor_sqrt_(8*s**4)-2*s**2) < 2*(sqrt2-1)*s*s]
        # [:boundary_of___short_side___with_respect_to___S]:goto
    [2*(sqrt2-1)*s*s < (1 +floor_sqrt_(8*s**4)-2*s**2) <= [slack-since-non_coprime_S_T]:min{(s*s -(critical_even_param4short_side_(s) -1 -s)**2), 2*s*(critical_even_param4short_side_(s) +1 -s)} <= middle_side <= 2*s*(s-1)]
        # [:boundary_of___middle_side___with_respect_to___S]:goto

    # s <~~ LSM
    [sqrt_(short_side*(sqrt2+1)/2) < [slack]:ceil_sqrt_((floor_sqrt_(2*short_side**2)+short_side)//2 +1) <= s <= [slack]:(short_side+1)//2 <= (short_side+1)/2]
        # [:boundary_of___S___with_respect_to___short_side]:goto
    [(1 +sqrt_(2*middle_side +1))/2 <= [slack]:(ceil_sqrt_(2*middle_side +1)//2 +1) <= s <= [slack]:floor_sqrt_((floor_sqrt_(2*middle_side**2)+middle_side)//2) < sqrt_(middle_side*(sqrt2+1)/2)]
        # [:boundary_of___S___with_respect_to___middle_side]:goto

    # S <~~> M
    [sqrt_(2*middle_side+1) <= [slack]:ceil_sqrt_(2*middle_side+1) <= short_side <= [slack]:(middle_side -1)]
        # [:boundary_of___ short_side___with_respect_to___middle_side]:goto
    [[slack]:(short_side+1) <= middle_side <= [slack]:((short_side**2 -1)//2) <= ((short_side**2 -1)/2)]
        # [:boundary_of___ middle_side___with_respect_to___short_side]:goto

    # L <~~> M
    [(middle_side +1) <= [slack]:((middle_side+3)//4*4 +1) <= long_side <= [slack]:floor_sqrt_((middle_side-1)**2 +middle_side**2) < (sqrt2*middle_side)]
        # [:boundary_of___long_side___with_respect_to___middle_side]:goto
    [(long_side/sqrt2) < ((1 +sqrt_(2*long_side**2 -1))/2) <= [slack]:(ceil_sqrt_(2*long_side**2 -1)//2 +1) <= middle_side <= [slack]:(long_side-1)]
        # [:boundary_of___middle_side___with_respect_to___long_side]:goto

    # L <~~> S
    [sqrt_(2*long_side -1) <= [slack]:ceil_sqrt_(2*long_side -1) <= short_side <= [slack]:((-1 +floor_sqrt_(2*long_side**2 -1))//2) <= ((-1 +sqrt_(2*long_side**2 -1))/2) < (long_side/sqrt2)]
        # [:boundary_of___short_side___with_respect_to___long_side]:goto
    [(sqrt2*short_side) < [slack]:ceil_sqrt_(short_side**2 +(short_side +1)**2) <= long_side <= [slack]:(1 +short_side**2)//2 <= (1 +short_side**2)/2]
        # [:boundary_of___long_side___with_respect_to___short_side]:goto

    ]]

    ]]
===
[1 <= t < s][gcd(s,t)==1][s%2 =!= t%2]
[(hypotenuse_side,odd_side,even_side) == (s*s +t*t, s*s -t*t, 2*s*t)]
[u := (s-t)]
[u <- [1,3..]]
[gcd(u,t)==1]
[v := (s-t-1)///2]
[v <- [0..]]
[u == 2*v +1]
[s == t+u == t +2*v +1]

[hypotenuse_side5s_t_(s,t) =[def]= s*s +t*t]
[hypotenuse_side5t_u_(t,u) =[def]= (t+u)**2 +t*t]
[hypotenuse_side5t_v_(t,v) =[def]= (t +2*v +1)**2 +t*t]

[hypotenuse_side5t_u_(t,u) == 2*t*t +2*t*u +u*u]
[hypotenuse_side5t_v_(t,v) == 2*t*t +2*t*(2*v+1) +(2*v+1)**2 == 2*t*t +2*t +4*t*v +4*v*v +4*v +1]
===
[@[t,u0,u1 :: int] -> [t >= 1] -> [1 <= u0 < u1] -> [hypotenuse_side5t_u_(t,u0) < hypotenuse_side5t_u_(t,u1)]]
[@[t0,t1,u :: int] -> [1 <= t0 < t1] -> [u >= 1] -> [hypotenuse_side5t_u_(t0,u) < hypotenuse_side5t_u_(t1,u)]]
===
[hypotenuse_side5t_u_(t,u): (+0,+0) < (+0,+2)]
[hypotenuse_side5t_u_(t,1): (+0,+0) < (+1,+0)]
===
[t,u >= 1][gcd(t,u)==1][u%2==1]:
    [hypotenuse_side5t_u_: (t,u) < (t,u+2)]
    [hypotenuse_side5t_u_: (t,1) < (t+1,1)]
# iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_():goto
===
]]]





[[[[[[[
right_angled_triangle_side_length
直角三角形:边长
直角三角形:两两互素边长
直角三角形:边长差的比率
right_angled_triangle_side_length_difference_ratio
===
直角三角形:边长:等比数列:[无整数解]
  [0 < (x/y) < x < (x*y)][1 <= y][x**2 == (x*y)**2 - (x/y)**2 == x**2 * (y**2 -1/y**2)]
  [(y**2 -1/y**2) == 1]
  [z := y**2]
  !! [y >= 1]
  [z == y**2 >= y >= 1]
  !! [(y**2 -1/y**2) == 1]
  [z**2 == z+1]
  !! [z >= 1]
  [z == (1+sqrt_(5))/2]
  [y == sqrt_((1+sqrt_(5))/2)]
  [y是无理数]
直角三角形:边长:等差数列:[只有3-4-5的倍数]
  [0 < (x-y) <= x <= (x+y)][x**2 == (x+y)**2 - (x-y)**2 == 4*x*y]
  [0 <= y < x]
  [x == 4*y]
  [0 < y < x == 4*y]
  [[x-y,x,x+y] == [3*y,4*y,5*y]]
直角三角形:边长:差定比:[定比==b/a]
  [b/a =[def]= (斜边-中边)/(中边-短边)]
  [gcd(a,b) == 1][x,y是整数][a,b是整数]
  [0 < (x-a*y) < x < (x+b*y)][0 < y == gcd(a*y,b*y)]
  [x**2 == (x+b*y)**2 - (x-a*y)**2 == (a+b)*2*x*y +(b**2 -a**2)*y**2]
  [x**2 -(a+b)*2*x*y -(b**2 -a**2)*y**2 == 0]
  [D == ((a+b)*2)**2 +4*(b**2 -a**2) == 8*(a+b)*b]
  [x/y == ((a+b)*2 +/- sqrt_(8*(a+b)*b))/2]
  [x/y == ((a+b) +/- sqrt_(2*(a+b)*b))]
  !! [y > 0]
  !! [x > 0]
  [x/y > 0]
  [[x/y == ((a+b) + sqrt_(2*(a+b)*b))]or[b < a][x/y == ((a+b) - sqrt_(2*(a+b)*b))]]
  !! [0 < (x-a*y)]
  [a < x/y]
  [0 < x/y -a == (b +/- sqrt_(2*(a+b)*b))]
  !! [b < sqrt_(2*(a+b)*b)]
  [x/y == ((a+b) + sqrt_(2*(a+b)*b))]

  !! [x,y是整数]
  [x/y是有理数]
  [sqrt_(2*(a+b)*b)是有理数]
  !! [a,b是整数]
  [sqrt_(2*(a+b)*b)是整数]
  [(2*(a+b)*b)是平方数]
    # e.g. [(a,b) == (1,1)]
    # e.g. [(a,b) == (7,2)]
    # e.g. [(a,b) == (7,1)]
    # xxx e.g. [(a,b) == (N/A,3)]
  !! [gcd(a,b) == 1]
  [{a,b}%2 == {0,1}]
  [(a+b)%2 == 1]
  [a%2 == 0]:
      !! [gcd(a,b) == 1]
      [b%2 == 1]:
      [(a+b)%2 == 1]
      [(a+b)*b%2 == 1]
      [(2*(a+b)*b) %4 == 2]
      [(2*(a+b)*b)不是平方数]
      !! [(2*(a+b)*b)是平方数]
      _L
  [a%2 == 1]
  [ez4B := max_power_of_base_as_factor_of_(2;b)]
  [odd4B := b///2**ez4B]
  !! [gcd(a,b) == 1]
  [gcd(a+b,b) == 1]
  [gcd(2*(a+b)*2**ez4B,b///2**ez4B) == 1]
  [gcd(2*(a+b)*2**ez4B,odd4B) == 1]
  !! [(2*(a+b)*b)是平方数]
  [odd4B是平方数]
  [2*(a+b)*2**ez4B是平方数]
  * [b%2 == 1]:
      [ez4B == 0]
      [b是平方数]
      [(a+b)*2是平方数]
      [(a+b)%2 == 0]
      [(a+b)///2是平方数]
  * [b%2 == 0]:
      [ez4B > 0]
      !! [a%2 == 1]
      [(a+b)%2 == 1]
      !! [2*(a+b)*2**ez4B是平方数]
      [(a+b)是平方数]
      [2*2**ez4B是平方数]
      [ez4B %2 == 1]
  [[[ez4B == 0][(a+b)///2是平方数]]or[[ez4B %2 == 1][(a+b)是平方数]]]
      # 先选floor_half_sqrt__odd4B/sqrt__odd4B/odd4B: [odd4B是平方数]
      # 再选ceil_half_ez4B/ez4B: [[ez4B == 0]or[ez4B %2 == 1]]
      # 再选sqrt__plus_A_B_or_half/(a+b):[(a+b)(///2)?是平方数]
      # 求b,再求a
      # 得(x/y)
===
[[[ez4B == 0][(a+b)///2是平方数]]or[[ez4B %2 == 1][(a+b)是平方数]]]
    [floor_half_sqrt__odd4B :<- [0..]]
    [ceil_half_ez4B :<- [0..]]
    [sqrt__odd4B := 1 +2*floor_half_sqrt__odd4B]
    [ez4B := max(0, ceil_half_ez4B*2-1)]
    [pre_min_a := 1]
    [b := sqrt__odd4B**2 * 2**ez4B]
    [pre_min_sqrt__plus_A_B_or_half := ceil_sqrt_((pre_min_a + b) >> (ez4B==0)) | (ez4B > 0)]
    [gcd(a,b) == 1]
    # [gcd(a+b,b) == 1]
    # [gcd(sqrt__plus_A_B_or_half,b) == 1]
    [min_sqrt__plus_A_B_or_half := min{sqrt__plus_A_B_or_half | [[sqrt__plus_A_B_or_half :<- [pre_min_sqrt__plus_A_B_or_half..]][gcd(sqrt__plus_A_B_or_half,b) == 1]]}]
    # [(a+b) == 2**(ez4B==0) *sqrt__plus_A_B_or_half**2]
    [min__plus_A_B := (min_sqrt__plus_A_B_or_half**2) << (ez4B==0)]
    # [x/y == ((a+b) + sqrt_(2*(a+b)*b))]
    [min_y := 1]
    [min_x := min_y*(min__plus_A_B + sqrt_(2*min__plus_A_B*b))]
    [min_hypotenuse := min_x + b*min_y]
    [min__plus_A_B
    == ((min_sqrt__plus_A_B_or_half**2) << (ez4B==0))
    == ((min{sqrt__plus_A_B_or_half | [[sqrt__plus_A_B_or_half :<- [pre_min_sqrt__plus_A_B_or_half..]][gcd(sqrt__plus_A_B_or_half,b) == 1]]}**2) << (ez4B==0))
    == ???cannot simplify!!!
    ]
    [min_hypotenuse
    == min_x + b*min_y
    == (min__plus_A_B + sqrt_(2*min__plus_A_B*b)) + b
    == ???cannot simplify!!!
    ]
    ######################
    #after『change logic』:
    #   find a simple rough form for lowerbound4plus_A_B instead of exact min__plus_A_B
    [plus_A_B
    >= min__plus_A_B
    == ((min_sqrt__plus_A_B_or_half**2) << (ez4B==0))
    >= (min_sqrt__plus_A_B_or_half**2)
    >= (pre_min_sqrt__plus_A_B_or_half**2)
    == (ceil_sqrt_((pre_min_a + b) >> (ez4B==0)) | (ez4B > 0))**2
    >= (ceil_sqrt_((pre_min_a + b) /2))**2
    >= (sqrt_((1 + b) /2))**2
    >= ((1 + b) /2) #too small...
    ]
    [plus_A_B >= pre_min_a + b == 1+b]
    [lowerbound4plus_A_B(b) =[def]= pre_min_a + b]
    [lowerbound4plus_A_B(b) == 1 + b]
    [hypotenuse
    >= min_hypotenuse
    == min_x + b*min_y
    == (min__plus_A_B + sqrt_(2*min__plus_A_B*b)) + b
    >= b + lowerbound4plus_A_B(b) + sqrt_(2*b*lowerbound4plus_A_B(b))
    == b + (1+b) + sqrt_(2*b*(1+b))
    == b + (1+b) + 2*sqrt_(b*(1+b) ///2)
    >= (1+2*b) +sqrt2*b
    >= (1+(2+sqrt2)*b)
    # [sqrt2 ~= 1.4142135623730951]
    # [14142135623730950**2 == 199999999999999986196797987902500 < 2*10**32 < 14142135623730951**2 == 200000000000000014481069235364401]
    # [1.4142135623730950 < sqrt2 < 1.4142135623730951]
    > (1+b*3.4142135623730950)
    ]
    [lowerbound4hypotenuse5lowerbound4B_(b) =[def]= (1+2*b) + 2*ceil_sqrt_(b*(1+b) ///2)]
    [hypotenuse == b + (1+b) + sqrt_(2*b*(1+b)) == lowerbound4hypotenuse5lowerbound4B_(b)]:
        # [:condition4_WW1_eq_2VV~~[w**2+1==2*v**2]=>???]:goto
        [y == 1]
        [a == 1 == pre_min_a]
        [b == 7**2]:
            [hypotenuse == 169]
            [middle_side == x == hypotenuse -b*y == 120]
            [short_side == middle_side -a*y == 119]
            [119**2 + 120**2 == 28561 == 169**2]
    ######################
    [hypotenuse(a,b) == x+b*y == ((a+2*b) + sqrt_(2*(a+b)*b))]
    [[1 <= a0 < a1] -> [b >= 1] -> [hypotenuse(a0,b) < hypotenuse(a1,b)]]
    [[1 <= b0 < b1] -> [a >= 1] -> [hypotenuse(a,b0) < hypotenuse(a,b1)]]
    [hypotenuse(a,b) >= min_hypotenuse(b) >= lowerbound4hypotenuse5lowerbound4B_(b)]

    ######################
    [@[a :<- [1..]] -> @[b :<- [1..]] -> @[b0 :<- [1..]] -> [[b >= b0] -> [hypotenuse(a,b) >= lowerbound4hypotenuse5lowerbound4B_(b0)]]]
    [@[a :<- [1..]] -> @[b :<- [1..]] -> @[b0 :<- [1..]] -> [[hypotenuse(a,b) < lowerbound4hypotenuse5lowerbound4B_(b0)] -> [b < b0]]]
    ######################
    !! [b == odd4B * 2**ez4B]
    !! [odd4B >= 1]
    !! [ez4B >= 0]
    [b{odd4B,ez4B} >= b{odd4B:=1,ez4B} == 1* 2**ez4B == 2**max(0, ceil_half_ez4B*2-1) >= 2**(ceil_half_ez4B*2-1)]
    [@[odd4B :<- [1..]] -> @[ez4B :<- [0..]] -> @[b0 :<- [1..]] -> [b := odd4B * 2**ez4B] -> [[b < b0] -> [[1 <= odd4B < b0/2**ez4B][2**ez4B < b0]]]]
    [@[odd4B :<- [1..]] -> @[ez4B :<- [0..]] -> @[b0 :<- [1..]] -> [b := odd4B * 2**ez4B] -> [[b < b0] -> [[0 <= ez4B < ceil_log2_(b0)][1 <= odd4B < ceil_div_(b0,2**ez4B)]]]]
    !! [ez4B == max(0, ceil_half_ez4B*2-1)]
    !! [odd4B == sqrt__odd4B**2 == (floor_half_sqrt__odd4B*2+1)**2]
    [@[floor_half_sqrt__odd4B :<- [0..]] -> @[ceil_half_ez4B :<- [0..]] -> @[b0 :<- [1..]] -> [odd4B := (floor_half_sqrt__odd4B*2+1)**2] -> [ez4B := max(0, ceil_half_ez4B*2-1)] -> [b := odd4B * 2**ez4B] -> [[b < b0] -> [[0 <= ez4B == max(0, ceil_half_ez4B*2-1) < ceil_log2_(b0)][1 <= odd4B == (floor_half_sqrt__odd4B*2+1)**2 < ceil_div_(b0,2**ez4B)]]]]
    #
    [@[floor_half_sqrt__odd4B :<- [0..]] -> @[ceil_half_ez4B :<- [0..]] -> @[b0 :<- [1..]] -> [odd4B := (floor_half_sqrt__odd4B*2+1)**2] -> [ez4B := max(0, ceil_half_ez4B*2-1)] -> [b := odd4B * 2**ez4B] -> [[b < b0] -> [[b0 >= 2][0 <= ceil_half_ez4B < ceil_div_(ceil_log2_(b0)+1,2)][0 <= floor_half_sqrt__odd4B < ceil_div_(ceil_sqrt_(ceil_div_(b0,2**ez4B))-1,2)]]]]
    #
    ######################
    [@[a :<- [1..]] -> @[floor_half_sqrt__odd4B :<- [0..]] -> @[ceil_half_ez4B :<- [0..]] -> @[b0 :<- [1..]] -> [odd4B := (floor_half_sqrt__odd4B*2+1)**2] -> [ez4B := max(0, ceil_half_ez4B*2-1)] -> [b := odd4B * 2**ez4B] -> [[hypotenuse(a,b) < lowerbound4hypotenuse5lowerbound4B_(b0)] -> [[b0 >= 2][0 <= ceil_half_ez4B < ceil_div_(ceil_log2_(b0)+1,2)][0 <= floor_half_sqrt__odd4B < ceil_div_(ceil_sqrt_(ceil_div_(b0,2**ez4B))-1,2)]]]]
        # [:boundary_setting4enumerate_hypotenuse_side__layer_by_layer]:here
    ######################
    TODO:how many right_angled_triangles where [b < b0] ?
    TODO:how many right_angled_triangles where [hypotenuse(a,b) < lowerbound4hypotenuse5lowerbound4B_(b0)] ?
    ######################
    [b :<- [1..]]:
        [all_As___B_eq_(b) =[def]= {a | [[a :<- [1,3..]][gcd(a,b) == 1][a%2 == 1][(a+b)%2=!=b%2][sqrt__plus_A_B_or_half := sqrt_((a+b) >> (b%2==1))][sqrt__plus_A_B_or_half %1 == 0]]}]
    [b0 :<- [1..]]:
        [all_Bs_lt_(b0) =[def]= {b | [[floor_half_sqrt__odd4B :<- [0..]][ceil_half_ez4B :<- [0..]][odd4B := (floor_half_sqrt__odd4B*2+1)**2][ez4B := max(0, ceil_half_ez4B*2-1)][b := odd4B * 2**ez4B][b < b0]]}]
        [num_Bs_lt_(b0) =[def]= len(all_Bs_lt_(b0))]
            # given [1 <= b0 < b1]: (num_Bs_lt_(b1) -num_Bs_lt_(b0)) gives number of (floor_half_sqrt__odd4B,ceil_half_ez4B) pairs needed to be pushed into heap.
        [num_Bs_lt_(b0) == len{(floor_half_sqrt__odd4B,ceil_half_ez4B) | [[b0 >= 2][ceil_half_ez4B :<- [0..<ceil_div_(ceil_log2_(b0)+1,2)]][ez4B := max(0, ceil_half_ez4B*2-1)][floor_half_sqrt__odd4B :<- [0..<ceil_div_(ceil_sqrt_(ceil_div_(b0,2**ez4B))-1,2)]]]}]
        [num_Bs_lt_(b0) == sum[ceil_div_(ceil_sqrt_(ceil_div_(b0,2**ez4B))-1,2) | [[b0 >= 2][ceil_half_ez4B :<- [0..<ceil_div_(ceil_log2_(b0)+1,2)]][ez4B := max(0, ceil_half_ez4B*2-1)]]]]
        [num_Bs_lt_(b0) == [b0 >= 2]:(ceil_div_(ceil_sqrt_(b0)-1,2) +sum[ceil_div_(ceil_sqrt_(ceil_div_(b0,2**(ceil_half_ez4B*2-1)))-1,2) | [ceil_half_ez4B :<- [1..<ceil_div_(ceil_log2_(b0)+1,2)]]])]
        [num_Bs_lt_(b0) == [b0 >= 2]:(ceil_((sqrt_(b0)-1)/2) +sum[ceil_((sqrt_(b0/2**(ceil_half_ez4B*2-1))-1)/2) | [ceil_half_ez4B :<- [1..<ceil_div_(ceil_log2_(b0)+1,2)]]])]
        [num_Bs_lt_(b0)
        ~= [b0 >= 2]:(((sqrt_(b0)-1)/2) +sum[((sqrt_(b0/2**(ceil_half_ez4B*2-1))-1)/2) | [ceil_half_ez4B :<- [1..<(log2_(2*b0)/2)]]])
        ~= [b0 >= 2]:(-(log2_(2*b0)/4) +sqrt_(b0)/2 +sum[(sqrt_(b0)/2**ceil_half_ez4B/sqrt2) | [ceil_half_ez4B :<- [1..<(log2_(2*b0)/2)]]])
        == [b0 >= 2]:(-(log2_(2*b0)/4) +sqrt_(b0)*(1/2 +(1/sqrt2)*sum[(1/2**ceil_half_ez4B) | [ceil_half_ez4B :<- [1..<(log2_(2*b0)/2)]]]))
        == [b0 >= 2]:(-(log2_(2*b0)/4) +sqrt_(b0)*(1/2 +(1/sqrt2)*(1/2-1/2**ceil_(log2_(2*b0)/2))/(1-1/2)))
        == [b0 >= 2]:(-(log2_(2*b0)/4) +sqrt_(b0)*(1/2 +(1/sqrt2)*(1-2/2**ceil_(log2_(2*b0)/2))))
        ~= [b0 >= 2]:(-(log2_(2*b0)/4) +sqrt_(b0)*(1/2 +(1/sqrt2)*(1-2/sqrt_(2*b0))))
        == [b0 >= 2]:(-(log2_(2*b0)/4) +sqrt_(b0)*(1/2 +(1/sqrt2) -1/sqrt_(b0)))
        == [b0 >= 2]:(-1 -(log2_(2*b0)/4) +sqrt_(b0)*(1/2 +1/sqrt2))
        == [b0 >= 2]:(-(5+log2_(b0))/4 +sqrt_(b0)*(1 +sqrt2)/2)
        ~= [b0 >= 2]:(-(5+log2_(b0))/4 +sqrt_(b0)*1.2071067811865475)
        ~= [b0 >= 2]:(2*sqrt_(b0) +2*sqrt_(2*b0) -log2_(b0) -5)/4
        ]
        [num_Bs_lt_(b0) ~= [b0 >= 2]:(-(5+log2_(b0))/4 +sqrt_(b0)*1.2071067811865475)]
        [num_Bs_lt_(b0) ~= [b0 >= 2]:(2*sqrt_(b0) +2*sqrt_(2*b0) -log2_(b0) -5)/4]
            #num_Bs_lt__rough_():goto
            #[:cmp__exact_vs_both_vs_rough4num_Bs_lt_]:goto
        ######################
        [num_Bs_lt_(2**k)
        == sum[ceil_div_(ceil_sqrt_(ceil_div_(2**k,2**ez4B))-1,2) | [[2**k >= 2][ceil_half_ez4B :<- [0..<ceil_div_(ceil_log2_(2**k)+1,2)]][ez4B := max(0, ceil_half_ez4B*2-1)]]]
        == sum[ceil_div_(ceil_sqrt_(2**(k-max(0, ceil_half_ez4B*2-1)))-1,2) | [[k>=1][ceil_half_ez4B :<- [0..<ceil_div_(k+1,2)]]]]
        + [k==0]:
            ... == 0
        + [k==1]:
            ... == 1 # {1} < 2
        + [k==2]:
            ... == 2 # {1,1*2} < 4
        + [k>=1]:
            ... == sum[ceil_div_(ceil_sqrt_(2**(k-max(0, ceil_half_ez4B*2-1)))-1,2) | [ceil_half_ez4B := 0]]
                + sum[ceil_div_(ceil_sqrt_(2**(k-max(0, ceil_half_ez4B*2-1)))-1,2) | [ceil_half_ez4B :<- [1..<ceil_div_(k+1,2)]]]
                == ceil_div_(ceil_sqrt_(2**k)-1,2)
                + sum[ceil_div_(ceil_sqrt_(2**(k+1-2*ceil_half_ez4B))-1,2) | [ceil_half_ez4B :<- [1..<ceil_div_(k+1,2)]]]
        ]

        [sum[ceil_div_(ceil_sqrt_(2**((k+2)+1-2*ceil_half_ez4B))-1,2) | [ceil_half_ez4B :<- [1..<ceil_div_((k+2)+1,2)]]]
        == sum[ceil_div_(ceil_sqrt_(2**(k+1-2*(ceil_half_ez4B-1)))-1,2) | [ceil_half_ez4B :<- [1..<1+ceil_div_(k+1,2)]]]
        == sum[ceil_div_(ceil_sqrt_(2**(k+1-2*ceil_half_ez4B))-1,2) | [ceil_half_ez4B :<- [0..<ceil_div_(k+1,2)]]]
        ]
        [k>=1]:
            [num_Bs_lt_(2**(k+2)) -num_Bs_lt_(2**k)
            == ceil_div_(ceil_sqrt_(2**(k+2))-1,2)
            + sum[ceil_div_(ceil_sqrt_(2**((k+2)+1-2*ceil_half_ez4B))-1,2) | [ceil_half_ez4B :<- [1..<ceil_div_((k+2)+1,2)]]]
            - num_Bs_lt_(2**k)
            == ceil_div_(ceil_sqrt_(2**(k+2))-1,2)
            + sum[ceil_div_(ceil_sqrt_(2**(k+1-2*ceil_half_ez4B))-1,2) | [ceil_half_ez4B :<- [0..<ceil_div_(k+1,2)]]]
            - ceil_div_(ceil_sqrt_(2**k)-1,2)
            - sum[ceil_div_(ceil_sqrt_(2**(k+1-2*ceil_half_ez4B))-1,2) | [ceil_half_ez4B :<- [1..<ceil_div_(k+1,2)]]]
            == ceil_div_(ceil_sqrt_(2**(k+2))-1,2)
            - ceil_div_(ceil_sqrt_(2**k)-1,2)
            + sum[ceil_div_(ceil_sqrt_(2**(k+1-2*ceil_half_ez4B))-1,2) | [ceil_half_ez4B := 0]]
            == ceil_div_(ceil_sqrt_(2**(k+2))-1,2)
            + ceil_div_(ceil_sqrt_(2**(k+1))-1,2)
            - ceil_div_(ceil_sqrt_(2**k)-1,2)
            ~= (-1 +sqrt_(2**k)*(1+sqrt2))/2
            ]
        [num_Bs_lt_(2**0) == 0]
        [num_Bs_lt_(2**1) == 1]
        [num_Bs_lt_(2**2) == 2]
        [k==0]:
            [ceil_div_(ceil_sqrt_(2**(k+2))-1,2)
            + ceil_div_(ceil_sqrt_(2**(k+1))-1,2)
            - ceil_div_(ceil_sqrt_(2**k)-1,2)
            == 1+1-0
            == 2
            == 2-0
            == num_Bs_lt_(2**2) -num_Bs_lt_(2**0)
            == num_Bs_lt_(2**(k+2)) -num_Bs_lt_(2**k)
            ]
        [@[k :<- [0..]] -> [num_Bs_lt_(2**(k+2)) -num_Bs_lt_(2**k) == ceil_div_(ceil_sqrt_(2**(k+2))-1,2) + ceil_div_(ceil_sqrt_(2**(k+1))-1,2) - ceil_div_(ceil_sqrt_(2**k)-1,2)]]
        [@[k :<- [0..]] ->
            [num_Bs_lt_(2**k) -(k%2)
            == num_Bs_lt_(2**k) -num_Bs_lt_(2**(k%2))
            == sum[(ceil_div_(ceil_sqrt_(2**(i+2))-1,2) + ceil_div_(ceil_sqrt_(2**(i+1))-1,2) - ceil_div_(ceil_sqrt_(2**i)-1,2)) | [i :<- [k%2,2+k%2..<=k-2]]]
            == ceil_div_(ceil_sqrt_(2**k)-1,2) -ceil_div_(ceil_sqrt_(2**(k%2))-1,2) +sum[ceil_div_(ceil_sqrt_(2**(i+1))-1,2) | [i :<- [k%2,2+k%2..<=k-2]]]
            == ceil_div_(ceil_sqrt_(2**k)-1,2) -(k%2) +sum[ceil_div_(ceil_sqrt_(2**i)-1,2) | [i :<- [1+k%2,3+k%2..<=k-1]]]
            ]
        ]
        [@[k :<- [0..]] -> [num_Bs_lt_(2**k) == ceil_div_(ceil_sqrt_(2**k)-1,2) +sum[ceil_div_(ceil_sqrt_(2**i)-1,2) | [i :<- [1+k%2,3+k%2..<=k-1]]]]]
            #num_Bs_lt__zpow_():goto

    [b0 :<- [1..]]:
        #xxx:infinite:[num_right_angled_triangles__B_lt_(b0) =[def]= len{(a,b) | [[b :<- all_Bs_lt_(b0)][a :<- all_As___B_eq_(b)]]}]
        [num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_(b0) =[def]= len{(a,b) | [[b :<- all_Bs_lt_(b0)][a :<- all_As___B_eq_(b)][hypotenuse(a,b) < lowerbound4hypotenuse5lowerbound4B_(b0)]]}]
            # [hypotenuse{a:=23,b:=9} == hypotenuse{a:=47,b:=2}]
                # ((65, 33, 56), ((23, 9), (33, 56, 65), (1, 0, 4)))
                # ((65, 63, 16), ((47, 2), (16, 63, 65), (0, 1, 7)))
        ######################
        ######################
        ######################
        usage: [1 <= b0 < b1]:
            # [:layered_hypotenuse_generation_via_lowerbound4hypotenuse5lowerbound4B_]:here
            + heap push (floor_half_sqrt__odd4B,ceil_half_ez4B,min_a<b>) for b in [b0..<b1]
                [(total push) == (num_Bs_lt_(b1)-num_Bs_lt_(b0))]
            + yield HOE where hypotenuse(a,b) < lowerbound4hypotenuse5lowerbound4B_(b1)
                [(total yield) == (num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_(b1)-num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_(b0))]
            #
            target: [limit{(total yield)/(total push) | [[j4b0 --> +oo][b0 := bs[j4b0]][b1 := bs[j4b0+1]]]} >= C(bs) > 0]
            #
            [num_Bs_lt_(b0) ~= [b0 >= 2]:(-(5+log2_(b0))/4 +sqrt_(b0)*1.2071067811865475)]
            [num_Bs_lt_(b0) ~= [b0 >= 2]:(2*sqrt_(b0) +2*sqrt_(2*b0) -log2_(b0) -5)/4]
                #num_Bs_lt__rough_():goto
            [(total push)
            == (num_Bs_lt_(b1)-num_Bs_lt_(b0))
            ~= (-log2_(b1/b0)/4 +(sqrt_(b1) -sqrt_(b0))*(1+sqrt2)/2)
            ~= (-log2_(b1/b0)/4 +(sqrt_(b1) -sqrt_(b0))*1.2071067811865475)
            ]
            [(total push) ~= (-log2_(b1/b0)/4 +(sqrt_(b1) -sqrt_(b0))*1.2071067811865475)]
            #
            ???[hypotenuse[k-1] ~= 2*pi*k]???
            ???[num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_(b0) ~= lowerbound4hypotenuse5lowerbound4B_(b0)/(2*pi)]???
                # [:conjecture4num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_]:goto
            #
            ???[(total yield)
            == (num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_(b1)-num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_(b0))
            ~= (lowerbound4hypotenuse5lowerbound4B_(b1) -lowerbound4hypotenuse5lowerbound4B_(b0))/(2*pi)
            !!  [lowerbound4hypotenuse5lowerbound4B_(b) =[def]= (1+2*b) + 2*ceil_sqrt_(b*(1+b) ///2)]
            ~= (b1-b0)*(2+sqrt2)/(2*pi)
            ~= (b1-b0)*0.5433889652230672
            ]???
            ???[(total yield) ~= ((b1-b0)*0.5433889652230672)]???
            ???[(total yield)/(total push)
            ~= ((b1-b0)*0.5433889652230672)/(-log2_(b1/b0)/4 +(sqrt_(b1) -sqrt_(b0))*1.2071067811865475)
            ~= ((b1-b0)*0.5433889652230672)/((sqrt_(b1) -sqrt_(b0))*1.2071067811865475)
            ~= ((b1-b0)*(2+sqrt2)/(2*pi))/((sqrt_(b1) -sqrt_(b0))*(1+sqrt2)/2)
            ~= ((b1-b0)*sqrt2)/((sqrt_(b1) -sqrt_(b0))*pi)

            ~= (sqrt2/pi)*(sqrt_(b1) +sqrt_(b0))
            ~= 0.4501581580785531 *(sqrt_(b1) +sqrt_(b0))
            ~= 0.4501581580785531 *(sqrt_(bs[+oo])*2)
            !! bs growing...
            --> +oo
            ]???
            ???[(total yield)/(total push) ~= (sqrt2/pi)*(sqrt_(b1) +sqrt_(b0))]???
                # [:ratio_of_num_yields_to_num_pushes_per_layer_is_divergent______layered_hypotenuse_generation]:here
            ???[exits C(bs)]???

        ...
        ######################
    ######################
    TODO



[[
[:diff__buggy_output__correct_output]:here

py_adhoc_call   seed.math.GaussInteger   ,16:iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt  =100 +to_sort +SML_vs_HOE
py_adhoc_call   seed.math.GaussInteger   ,187907:iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt  =1180733+1 +to_sort +SML_vs_HOE
py_adhoc_call   seed.math.GaussInteger   ,1000000:iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt  =7*10**6 +to_sort +SML_vs_HOE > /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
du -h /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
    26MB

view /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.HOE.out.txt
diff /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.HOE.out.txt   /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt   > /sdcard/0my_files/tmp/out4diff/diff..1000000.HOE.out.txt
rm /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.HOE.out.txt
view /sdcard/0my_files/tmp/out4diff/diff..1000000.HOE.out.txt
187653a187654
> (1179065, 832953, 834496)
187907a187909,1000000
> (1180757, 795315, 872732)
> (1180765, 406997, 1108404)
... ...
> (6283313, 3247665, 5378912)
> (6283313, 5507055, 3025288)

view /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.out.txt
(5, 3, 4) #1line
... ...
(1179061, 698861, 949620)
(1179065, 1034343, 565976) #187654line
(1179109, 722141, 932100)
... ...
(1180721, 1066479, 506680)
(1180733, 831285, 838508) #187907line
...eof <<== raise err

view /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
(5, 3, 4) #1line
... ...
(1179061, 698861, 949620)
(1179065, 832953, 834496) #187654line
(1179065, 1034343, 565976)
(1179109, 722141, 932100)
...
(6283313, 3247665, 5378912)
(6283313, 5507055, 3025288) #1000000line
]]


copy to:
e others/数学/我的猜想.txt
[[[
view ../../python3_src/seed/math/right_angled_triangle_side_length.py
TODO:我的猜想:证明:
    coprime_ratio vs non_coprime_triple
===
######################
# coprime_ratio case:
???[coprime_ratio case][hypotenuse[k-1] ~= 2*pi*k]???
    ???[hypotenuse[2**k-1] ~= (25/4)*2**k]???
    ???[hypotenuse[10**k-1] ~= 2*pi*10**k]???
    #HOE = (hypotenuse_side, odd_side, even_side)
???[non_coprime_triple case][hypotenuse[k-1] ~= 2*pi*k/(ln_(k) -lnln_(k))]???
==>>:猜想推论:
    ???[num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_(b0) ~= lowerbound4hypotenuse5lowerbound4B_(b0)/(2*pi)]???
        # [:conjecture4num_right_angled_triangles__hypotenuse_lt_lowerbound4hypotenuse5lowerbound4B_]:here
==>>:猜想推论:
推导:???[non_coprime_triple case][hypotenuse[k-1] ~= 2*pi*k/(ln_(k) -lnln_(k))]???
[???[coprime_ratio case][hypotenuse[k-1] ~= 2*pi*k]???]:
    [num_right_angled_triangles__hypotenuse_lt_(max1_hypotenuse, case=coprime_ratio) ~= (max1_hypotenuse/(2*pi))]
    [num_right_angled_triangles__hypotenuse_lt_(max1_hypotenuse, case=non_coprime_triple)
    == sum[k*(num_right_angled_triangles__hypotenuse_lt_(max1_hypotenuse/k, case=coprime_ratio) -num_right_angled_triangles__hypotenuse_lt_(max1_hypotenuse/(k+1), case=coprime_ratio)) | [k :<- [1..]]]
    ~= sum[k*(num_right_angled_triangles__hypotenuse_lt_(max1_hypotenuse/k, case=coprime_ratio) -num_right_angled_triangles__hypotenuse_lt_(max1_hypotenuse/(k+1), case=coprime_ratio)) | [k :<- [1..<sqrt_(max1_hypotenuse)]]] + sum[max1_hypotenuse/hypotenuse[i] | [i :<- [1..][hypotenuse[i] < sqrt_(max1_hypotenuse)]]]
    ~= max1_hypotenuse/2pi*sum{1/k | [k :<- [1..<sqrt_(max1_hypotenuse)]]} + max1_hypotenuse/2pi*sum{1/i | [i :<- [1..<sqrt_(max1_hypotenuse)/2pi]]}
    ~= max1_hypotenuse/2pi*(ln_(sqrt_(max1_hypotenuse)) +ln_(sqrt_(max1_hypotenuse)/2pi))
    ~= (max1_hypotenuse/2pi)*ln_(max1_hypotenuse/2pi)
    ]
    [num_right_angled_triangles__hypotenuse_lt_(max1_hypotenuse, case=non_coprime_triple) ~= (max1_hypotenuse/2pi)*ln_(max1_hypotenuse/2pi)]
    [f(h) == h*ln_(h)][g == f**-1]:
        [k == f(g(k)) == g(k)*ln_(g(k))]
        [ln_(k) == ln_(g(k)) +ln_(ln_(g(k)))]
        [g(k) == k/ln_(g(k)) == k/(ln_(k) -ln_(ln_(g(k))))]
        [ln_(g(k)) == ln_(k) -ln_(ln_(k) -ln_(ln_(g(k)))) ~= ln_(k)]
        [g(k) ~= k/(ln_(k) -ln_(ln_(k)))]
    [[f(h) == h*ln_(h)] -> [k ~= f(k/(ln_(k) -lnln_(k))]]
    [hypotenuse[k-1] ~= 2*pi*k/(ln_(k) -lnln_(k))]

######################
# data4conjecture:
######################
view /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
######################
py -m nn_ns.app.line_selector --begin4lineno=1 --lineno_generator='2**?' -i /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
[1@0.0]:(5, 3, 4)
[2@0.1]:(13, 5, 12)
[4@0.2]:(25, 7, 24)
[8@0.3]:(53, 45, 28)
[16@0.4]:(97, 65, 72)
[32@0.5]:(197, 195, 28)
[64@0.6]:(401, 399, 40)
[128@0.7]:(797, 555, 572)
[256@0.8]:(1609, 1591, 240)
[512@0.9]:(3221, 2829, 1540)
[1024@0.10]:(6421, 3379, 5460)
[2048@0.11]:(12889, 10439, 7560)
[4096@0.12]:(25769, 25431, 4160)
[8192@0.13]:(51481, 24569, 45240)
[16384@0.14]:(102901, 22099, 100500)
[32768@0.15]:(205957, 197245, 59268)
[65536@0.16]:(411757, 60635, 407268)
[131072@0.17]:(823553, 767775, 297928)
[262144@0.18]:(1647005, 1640043, 151276)
[524288@0.19]:(3294205, 2581387, 2046516)

py -m nn_ns.app.line_selector --begin4lineno=1 --lineno_generator='10**?' -i /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
[1@0.0]:(5, 3, 4)
[10@0.1]:(65, 33, 56)
[100@0.2]:(629, 429, 460)
[1000@0.3]:(6277, 6205, 948)
[10000@0.4]:(62849, 11649, 61760)
[100000@0.5]:(628325, 334947, 531604)
[1000000@0.6]:(6283313, 5507055, 3025288)

######################
???[coprime_ratio case][hypotenuse[10**k-1] ~= 2*pi*10**k]???
    [k==0]:[HOE == (5, 3, 4)]
    [k==1]:[HOE == (65, 33, 56)]
    [k==2]:[HOE == (629, 429, 460)]
    [k==3]:[HOE == (6277, 6205, 948)]
    [k==4]:[HOE == (62849, 11649, 61760)]
    [k==5]:[HOE == (628325, 334947, 531604)]
    [k==6]:[HOE == (6283313, 5507055, 3025288)]
    ######################

???[coprime_ratio case][hypotenuse[2**k-1] ~= (25/4)*2**k]???
    [HOE[1-1] == (5, 3, 4)]
    [HOE[2-1] == (13, 5, 12)]
    [HOE[4-1] == (25, 7, 24)]
    [HOE[8-1] == (53, 45, 28)]
    [HOE[16-1] == (97, 65, 72)]
    [HOE[32-1] == (197, 195, 28)]
    [HOE[64-1] == (401, 399, 40)]
    [HOE[128-1] == (797, 555, 572)]
    [HOE[256-1] == (1609, 1591, 240)]
    [HOE[512-1] == (3221, 2829, 1540)]
    [HOE[1024-1] == (6421, 3379, 5460)]
    [HOE[2048-1] == (12889, 10439, 7560)]
    [HOE[4096-1] == (25769, 25431, 4160)]
    [HOE[8192-1] == (51481, 24569, 45240)]
    [HOE[16384-1] == (102901, 22099, 100500)]
    [HOE[32768-1] == (205957, 197245, 59268)]
    [HOE[65536-1] == (411757, 60635, 407268)]
    [HOE[131072-1] == (823553, 767775, 297928)]
    [HOE[262144-1] == (1647005, 1640043, 151276)]
    [HOE[524288-1] == (3294205, 2581387, 2046516)]
    # [HOE[1048576-1] == ???]
    ######################

######################
# non_coprime_triple case:
py_adhoc_call   seed.math.GaussInteger   ,1000000:iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt  +to_sort +SML_vs_HOE +turnoff__coprime   =6*10**5 > /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.non_coprime.out.txt
du -h /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.non_coprime.out.txt
    23MB

######################
view /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.non_coprime.out.txt
######################
???[non_coprime_triple case][hypotenuse[10**k-1] ~= ???]???
    [k==0]:[HOE == (5, 3, 4)]
    [k==1]:[HOE == (29, 21, 20)]
    [k==2]:[HOE == (170, 26, 168)]
    [k==3]:[HOE == (1108, 460, 1008)]
    [k==4]:[HOE == (8214, 7770, 2664)]
    [k==5]:[HOE == (64730, 38838, 51784)]
    [k==6]:[HOE == (531852, 116748, 518880)]
    ######################

???[non_coprime_triple case][hypotenuse[2**k-1] ~= ???]???
    [HOE[1-1] == (5, 3, 4)]
    [HOE[2-1] == (10, 6, 8)]
    [HOE[4-1] == (15, 9, 12)]
    [HOE[8-1] == (25, 15, 20)]
    [HOE[16-1] == (40, 24, 32)]
    [HOE[32-1] == (68, 60, 32)]
    [HOE[64-1] == (117, 45, 108)]
    [HOE[128-1] == (202, 198, 40)]
    [HOE[256-1] == (357, 315, 168)]
    [HOE[512-1] == (629, 595, 204)]
    [HOE[1024-1] == (1131, 405, 1056)]
    [HOE[2048-1] == (2053, 1475, 1428)]
    [HOE[4096-1] == (3754, 2970, 2296)]
    [HOE[8192-1] == (6890, 6106, 3192)]
    [HOE[16384-1] == (12740, 12348, 3136)]
    [HOE[32768-1] == (23664, 22800, 6336)]
    [HOE[65536-1] == (44145, 36855, 24300)]
    [HOE[131072-1] == (82741, 55445, 61416)]
    [HOE[262144-1] == (155600, 109392, 110656)]
    [HOE[524288-1] == (293620, 255532, 144624)]
    # [HOE[1048576-1] == ???]
    ######################
>>> from math import pi, log as ln_
>>> f=lambda h:(hh:=h/2/pi)*ln_(hh)
>>> f(293620)/2**19
0.9583667851245002
>>> f(531852)/10**6
0.9604240501866983
>>> g=lambda k:2*pi*k/(ln_(k) -ln_(ln_(k)))
>>> g(2**19)/293620
1.0592329805298375
>>> g(10**6)/531852
1.0557714287426916

]]]
[[
fail:try to proof:min_hypotenuse_is_monotone_nondecreasing_with_respect_to___floor_half_sqrt__odd4B___ceil_half_ez4B)
    ===
    fail:basic-version:
        fail:[min_hypotenuse<floor_half_sqrt__odd4B,ceil_half_ez4B> <= min_hypotenuse<floor_half_sqrt__odd4B+1,ceil_half_ez4B>]
            counterexample: see:_try_to_find_counterexample_in_src_code__between____
                ok = (all(lts) and lt_00_10 == -1 == lt_00_01 and (lt_10_01 == -1 or floor_half_sqrt__odd4B <= (ceil_half_ez4B==0)))
                if not ok:yield ((floor_half_sqrt__odd4B, ceil_half_ez4B), lts, side_length_ratio)
                ((292, 0), [1, -1, -1], (831285, 838508, 1180733))
                ((46312, 2), [1, -1, -1], (165705013500, 165712316509, 234347441509))
        [min_hypotenuse<floor_half_sqrt__odd4B,ceil_half_ez4B> <= min_hypotenuse<floor_half_sqrt__odd4B,ceil_half_ez4B+1>]
        # [(+0,+0) <= (+1,+0)]
        # [(+0,+0) <= (+0,+1)]
    ===
    fail:strong-version:
        fail:[min_hypotenuse<floor_half_sqrt__odd4B,ceil_half_ez4B> < min_hypotenuse<floor_half_sqrt__odd4B+1,ceil_half_ez4B> < min_hypotenuse<floor_half_sqrt__odd4B,ceil_half_ez4B+1>]
        # [(+0,+0) < (+1,+0) < (+0,+1)]
    ===
    fail:proof:strong-version:
    !! [sqrt__odd4B := 1 +2*floor_half_sqrt__odd4B]
    [sqrt__odd4B: [(+0,_) < (+1,_)]]
    !! [ez4B := max(0, ceil_half_ez4B*2-1)]
    [ez4B: [(_,+0) < (_,+1)]]
        # [0,  1,3,5,..]
    !! [pre_min_a := 1]
    [pre_min_a: [(_,_) == (_,_)]]
    !! [b := sqrt__odd4B**2 * 2**ez4B]
    [b: [(+0,_) < (+1,_)]]
    [b: [(_,+0) < (_,+1)]]
    fail: [b: [(+0,+0) < (+1,+0) < (+0,+1)]]
    * [ez4B(_,+0) == 0]:
        [b: [(+1,+0) < (0,+1)]]
            <==> [b(+1,+0) < 2*b(+0,+0)]
            <==> [(floor_half_sqrt__odd4B(+0,_)*2+3)**2 < 2*(floor_half_sqrt__odd4B(+0,_)*2+1)**2]
            # [1,9,25,49,81,...]
            <==> [floor_half_sqrt__odd4B(+0,_) >= 2]
    * [ez4B(_,+0) > 0]:
        [b: [(+1,+0) < (0,+1)]]
            <==> [b(+1,+0) < 4*b(+0,+0)]
            <==> [(floor_half_sqrt__odd4B(+0,_)*2+3)**2 < 4*(floor_half_sqrt__odd4B(+0,_)*2+1)**2]
            # [1,9,25,49,81,...]
            <==> [floor_half_sqrt__odd4B(+0,_) >= 1]
    [[b: [(+1,+0) < (0,+1)]] <-> [floor_half_sqrt__odd4B(+0,_) > [ez4B(_,+0) == 0]]]

    !! [pre_min_sqrt__plus_A_B_or_half := ceil_sqrt_((pre_min_a + b) >> (ez4B==0)) | (ez4B > 0)]
    * [ez4B==0]:
        [pre_min_sqrt__plus_A_B_or_half == ceil_sqrt_((pre_min_a + b) >> 1) == ceil_sqrt_((sqrt__odd4B**2+1)///2)]
            # [:condition4_WW1_eq_2VV~~[w**2+1==2*v**2]=>???]:goto
    * [ez4B > 0]:
        [ez4B %2 == 1]
        [pre_min_sqrt__plus_A_B_or_half == ceil_sqrt_(pre_min_a + b) | 1 == 1|ceil_sqrt_(1+2*sqrt__odd4B**2 *4**((ez4B-1)///2))]
            # [:condition4_2WW1_eq_VV~~[2*w**2+1==v**2]=>???]:goto

    !! [pre_min_sqrt__plus_A_B_or_half := ceil_sqrt_((pre_min_a + b) >> (ez4B==0)) | (ez4B > 0)]
    !! [[b: [(+1,+0) < (0,+1)]] <-> [floor_half_sqrt__odd4B(+0,_) > [ez4B(_,+0) == 0]]]
    [[floor_half_sqrt__odd4B(+0,_) > [ez4B(_,+0) == 0]] -> [pre_min_sqrt__plus_A_B_or_half: [(+1,+0) <= (0,+1)]]]
        # 『<=』<<==『ceil_sqrt_』
    !! [min_sqrt__plus_A_B_or_half := min{sqrt__plus_A_B_or_half | [[sqrt__plus_A_B_or_half :<- [pre_min_sqrt__plus_A_B_or_half..]][gcd(sqrt__plus_A_B_or_half,b) == 1]]}]
            # [:try_to_find_counterexample_in_src_code]:goto
    ???TODO
    ???fail
]]

#[:cmp__exact_vs_both_vs_rough4num_Bs_lt_]:here
[[[
#num_Bs_lt__rough_():goto
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,iter_nums_Bs_ex__lt_ --exact_vs_both_vs_rough=...  '=[2**k for k in range(60)]'
===
(0, 0)
(1, 0.20710678118654746)
(2, 0.6642135623730949)
(2, 1.414213562373095)
(4, 2.57842712474619)
(6, 4.32842712474619)
(9, 6.90685424949238)
(13, 10.65685424949238)
(19, 16.06370849898476)
(26, 23.81370849898476)
(38, 34.87741699796952)
(54, 50.62741699796952)
(77, 73.00483399593904)
(108, 104.75483399593904)
(154, 149.75966799187808)
(218, 213.50966799187808)
(309, 303.76933598375615)
(436, 431.51933598375615)
(618, 612.2886719675123)
(873, 868.0386719675123)
(1236, 1229.8273439350246)
(1747, 1741.5773439350246)
(2472, 2465.404687870049)
(3495, 3489.154687870049)
(4944, 4937.059375740098)
(6991, 6984.809375740098)
(9888, 9880.868751480197)
(13984, 13976.618751480197)
(19777, 19768.987502960394)
(27968, 27960.737502960394)
(39554, 39545.72500592079)
(55937, 55929.47500592079)
(79108, 79099.70001184157)
(111876, 111867.45001184157)
(158217, 158208.15002368315)
(223753, 223743.90002368315)
(316435, 316425.5500473663)
(447507, 447497.3000473663)
(632871, 632860.8500947326)
(895015, 895004.6000947326)
(1265743, 1265731.9501894652)
(1790030, 1790019.7001894652)
(2531486, 2531474.6503789304)
(3580061, 3580050.4003789304)
(5062972, 5062960.550757861)
(7160124, 7160112.300757861)
(10125945, 10125932.851515722)
(14320249, 14320236.601515722)
(20251891, 20251877.953031443)
(28640498, 28640485.703031443)
(40503782, 40503768.656062886)
(57280997, 57280984.406062886)
(81007564, 81007550.56212577)
(114561996, 114561982.31212577)
(162015129, 162015114.87425154)
(229123993, 229123978.62425154)
(324030259, 324030243.9985031)
(458247986, 458247971.7485031)
(648060518, 648060502.7470062)
(916495973, 916495958.4970062)
===
]]]
[[[
#num_Bs_lt__zpow_():goto
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,iter_nums_Bs_lt__zpow_  +validate '=range(60)'
===
0
1
2
2
4
6
9
13
19
26
38
54
77
108
154
218
309
436
618
873
1236
1747
2472
3495
4944
6991
9888
13984
19777
27968
39554
55937
79108
111876
158217
223753
316435
447507
632871
895015
1265743
1790030
2531486
3580061
5062972
7160124
10125945
14320249
20251891
28640498
40503782
57280997
81007564
114561996
162015129
229123993
324030259
458247986
648060518
916495973
===
]]]


[[
]]


]]]]]]]
[[
see also:
view ../../python3_src/seed/math/right_angled_triangle_infos__sorted_by.py
    class MAIN_MODULE_DOC.__doc__
view ../../python3_src/seed/math/GaussInteger.py
  iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq.__doc__
    def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, /):
        len_hypotenuse -> factorisation_of<len_hypotenuse>-> Iter (len_hypotenuse, odd, even)

]]




[:condition4_2WW1_eq_VV~~[2*w**2+1==v**2]=>???]:here
[:condition4_WW1_eq_2VV~~[w**2+1==2*v**2]=>???]:here
    view others/数学/condition4_WW1_eq_2VV.txt
[[[
main:
===
[@[w,v :: uint] -> [w**2+1==2*v**2] -> ?[k :: uint] -> [[v;w;] == [3,2;4,3;]**k *[1;1;]]]
[@[w,v :: uint] -> [w**2+1==2*v**2] -> ?[k :: uint] -> [[vs[k] == ((1+sqrt2)**(1+2*k) -(1-sqrt2)**(1+2*k))*sqrt2/4][ws[k] == ((1+sqrt2)**(1+2*k) +(1-sqrt2)**(1+2*k))/2]]]
[[w**2+1==2*v**2][v,w :: int][v,w > 0] -> [_v := abs(3*v-2*w)] -> [_w := abs(-4*v+3*w)] -> [[_w**2+1 == 2*_v**2][_v,_w >= 1][[1 <= _v < v]or[_v == v == 1]]]]
    # [:WW1_eq_2VV___vw_abs_decrease_until_eq1]:goto
===
[@[w,v :: uint] -> [2*w**2+1==v**2] -> ?[k :: uint] -> [[v;w;] == [3,4;2,3;]**k *[1;0;]]]
[@[w,v :: uint] -> [2*w**2+1==v**2] -> ?[k :: uint] -> [[vs[k] == 1/2*(s0**k +s1**k)][ws[k] == sqrt2/4*(s0**k -s1**k)]]]
[[2*w**2+1==v**2][v,w :: int][[v > 0][w >= 0]] -> [_v := abs(3*v-4*w)] -> [_w := abs(-2*v+3*w)] -> [[2*_w**2+1 == _v**2][_v >= 1][_w >= 0][[1 <= _v < v]or[[(v,w) == (1,0)][(_v,_w) == (3,2)]]]]]
    # [:2WW1_eq_VV___v_abs_decrease_until_eq1___loop_roots_are_1_3]:goto
===
]]]




[[[
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,20:iter_right_angled_triangle_side_length_difference_ratio__given_B_  =0 =0
===
(1, 1)
(7, 1)
(17, 1)
(31, 1)
(49, 1)
(71, 1)
(97, 1)
(127, 1)
(161, 1)
(199, 1)
(241, 1)
(287, 1)
(337, 1)
(391, 1)
(449, 1)
(511, 1)
(577, 1)
(647, 1)
(721, 1)
(799, 1)
]]]
[[[
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   @mk__right_angled_triangle_side_length_ratio5difference_ratio_ =1 =1
(3, 4, 5)
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   @mk__right_angled_triangle_side_length_ratio5difference_ratio_ =7 =1
(5, 12, 13)
===
===
===
]]]
[[[
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,5:iter_right_angled_triangle_side_length_difference_ratio__given_B_  =0 =0 +with_side_length_ratio
===
((1, 1), (3, 4, 5))
((7, 1), (5, 12, 13))
((17, 1), (7, 24, 25))
((31, 1), (9, 40, 41))
((49, 1), (11, 60, 61))
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,5:iter_right_angled_triangle_side_length_difference_ratio__given_B_  =7 =0 +with_side_length_ratio
===
((17, 225), (555, 572, 797))
((17, 225), (555, 572, 797))
((113, 225), (615, 728, 953))
((167, 225), (645, 812, 1037))
((167, 225), (645, 812, 1037))
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,5:iter_right_angled_triangle_side_length_difference_ratio__given_B_  =7 =1 +with_side_length_ratio
===
((79, 450), (1140, 1219, 1669))
((79, 450), (1140, 1219, 1669))
((79, 450), (1140, 1219, 1669))
((391, 450), (1320, 1711, 2161))
((511, 450), (1380, 1891, 2341))
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,5:iter_right_angled_triangle_side_length_difference_ratio__given_B_  =7 =2 +with_side_length_ratio
===
((49, 1800), (4380, 4429, 6229))
((49, 1800), (4380, 4429, 6229))
((409, 1800), (4620, 5029, 6829))
((601, 1800), (4740, 5341, 7141))
((601, 1800), (4740, 5341, 7141))
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,5:iter_right_angled_triangle_side_length_difference_ratio__given_B_  =7 =3 +with_side_length_ratio
===
((721, 7200), (17880, 18601, 25801))
((1081, 7200), (18120, 19201, 26401))
((2209, 7200), (18840, 21049, 28249))
((3001, 7200), (19320, 22321, 29521))
((3409, 7200), (19560, 22969, 30169))
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,5:iter_right_angled_triangle_side_length_difference_ratio__given_B_  =7 =4 +with_side_length_ratio +with_params
((1129, 28800), (70320, 71449, 100249), (7, 4, 173))
((3241, 28800), (71760, 75001, 103801), (7, 4, 179))
((3961, 28800), (72240, 76201, 105001), (7, 4, 181))
((6169, 28800), (73680, 79849, 108649), (7, 4, 187))
((7681, 28800), (74640, 82321, 111121), (7, 4, 191))
===
]]]
[[[
iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
    '#output Iter<(S, M, L)> but sorted by key (L, S, M)'
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,50:iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
(3, 4, 5)
(5, 12, 13)
(8, 15, 17)
(7, 24, 25)
(20, 21, 29)
(12, 35, 37)
(9, 40, 41)
(28, 45, 53)
(11, 60, 61)
(16, 63, 65)
(33, 56, 65)
(48, 55, 73)
(13, 84, 85)
(36, 77, 85)
(39, 80, 89)
(65, 72, 97)
(20, 99, 101)
(60, 91, 109)
(15, 112, 113)
(44, 117, 125)
(88, 105, 137)
(17, 144, 145)
(24, 143, 145)
(51, 140, 149)
(85, 132, 157)
(119, 120, 169)
(52, 165, 173)
(19, 180, 181)
(57, 176, 185)
(104, 153, 185)
(95, 168, 193)
(28, 195, 197)
(84, 187, 205)
(133, 156, 205)
(21, 220, 221)
(140, 171, 221)
(60, 221, 229)
(105, 208, 233)
(120, 209, 241)
(32, 255, 257)
(23, 264, 265)
(96, 247, 265)
(69, 260, 269)
(115, 252, 277)
(160, 231, 281)
(161, 240, 289)
(68, 285, 293)
(136, 273, 305)
(207, 224, 305)
(25, 312, 313)
===vs:
===(S,M,L) vs (L, odd, even)
view ../../python3_src/seed/math/GaussInteger.py
def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_eq(c, factorisation_of_c, /):
    .__doc__:
        result of N=100:[
(5, 3, 4)
(13, 5, 12)
(17, 15, 8)
(25, 7, 24)
(29, 21, 20)
(37, 35, 12)
(41, 9, 40)
(53, 45, 28)
(61, 11, 60)
(65, 33, 56)
(65, 63, 16)
(73, 55, 48)
(85, 77, 36)
(85, 13, 84)
(89, 39, 80)
(97, 65, 72)
]
    #fmt: (L, odd, even)
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,16:iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_ +extended_output +SML_vs_HOE
===
((5, 3, 4), ((1, 1), (3, 4, 5), (0, 0, 1)))
((13, 5, 12), ((7, 1), (5, 12, 13), (0, 0, 2)))
((17, 15, 8), ((7, 2), (8, 15, 17), (0, 1, 3)))
((25, 7, 24), ((17, 1), (7, 24, 25), (0, 0, 3)))
((29, 21, 20), ((1, 8), (20, 21, 29), (0, 2, 3)))
((37, 35, 12), ((23, 2), (12, 35, 37), (0, 1, 5)))
((41, 9, 40), ((31, 1), (9, 40, 41), (0, 0, 4)))
((53, 45, 28), ((17, 8), (28, 45, 53), (0, 2, 5)))
((61, 11, 60), ((49, 1), (11, 60, 61), (0, 0, 5)))
((65, 33, 56), ((23, 9), (33, 56, 65), (1, 0, 4)))
((65, 63, 16), ((47, 2), (16, 63, 65), (0, 1, 7)))
((73, 55, 48), ((7, 18), (48, 55, 73), (1, 1, 5)))
((85, 13, 84), ((71, 1), (13, 84, 85), (0, 0, 6)))
((85, 77, 36), ((41, 8), (36, 77, 85), (0, 2, 7)))
((89, 39, 80), ((41, 9), (39, 80, 89), (1, 0, 5)))
((97, 65, 72), ((7, 25), (65, 72, 97), (2, 0, 4)))
===
]]]


# [:try_to_find_counterexample_in_src_code]:goto
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,100000:iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_ > /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.100000.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.100000.out.txt
du -h /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.100000.out.txt
    2.3MB
rm /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.100000.out.txt

py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000000:iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_ +SML_vs_HOE -buggy_plus1__vs__layered  > /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.HOE.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.HOE.out.txt
    !!!buggy!!!
    [:diff__buggy_output__correct_output]:goto
(5, 3, 4)                   #1-th line
(13, 5, 12)
(17, 15, 8)
... ...
... ...
(1180709, 519459, 1060300)
(1180721, 1066479, 506680)
(1180733, 831285, 838508)   #187907-th line
... ERROR here
if not heap_item < news[0]: raise mk_exc_()
BaseException: found counterexample: result_ex: side_length_ratio=(831285, 838508, 1180733); ab=(7223, 342225); params=(292, 0, 418);

[[[
((292, 0), [1, -1, -1], (831285, 838508, 1180733))
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1:iter_right_angled_triangle_side_length_difference_ratio__given_B_  +with_side_length_ratio +with_params =292 =0
((7223, 342225), (831285, 838508, 1180733), (292, 0, 418))
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1:iter_right_angled_triangle_side_length_difference_ratio__given_B_  +with_side_length_ratio +with_params =293 =0
((1543, 344569), (832953, 834496, 1179065), (293, 0, 416))
    [1179065 < 1180733]
    [hypotenuse(292,0): (+1,+0) < (+0,+0)]
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1:iter_right_angled_triangle_side_length_difference_ratio__given_B_  +with_side_length_ratio +with_params =292 =1
((2791, 684450), (1654380, 1657171, 2341621), (292, 1, 829))

py_adhoc_call   seed.math.factor_pint_by_trial_division_   @factor_pint_by_trial_division_ =1180733
{1180733: 1}

>>> divmod(1180733,4)
(295183, 1)

===
]]]



py_adhoc_call   seed.math.right_angled_triangle_side_length   ,10:_try_to_find_counterexample_in_src_code__len_hypotenuse_lt =1000
    <EMPTY>
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,10000:_try_to_find_counterexample_in_src_code__len_hypotenuse_lt =500000
    <EMPTY>
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,10000:_try_to_find_counterexample_in_src_code__len_hypotenuse_lt =1180733+1
((292, 0), [1, -1, -1], (831285, 838508, 1180733))
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,10000:_try_to_find_counterexample_in_src_code__len_hypotenuse_lt =10**7    > /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length.._try_to_find_counterexample_in_src_code__len_hypotenuse_lt.pow_10_7.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length.._try_to_find_counterexample_in_src_code__len_hypotenuse_lt.pow_10_7.out.txt
((292, 0), [1, -1, -1], (831285, 838508, 1180733))
((367, 1), [1, -1, -1], (2622480, 2642431, 3722881))
((500, 1), [1, -1, -1], (4852848, 4873775, 6877777))
    ###only 3 counterexample for [hypotenuse_side < 10**7]

[[[
def _try_to_find_counterexample_in_src_code__between____(begin4floor_half_sqrt__odd4B, end4floor_half_sqrt__odd4B, begin4ceil_half_ez4B, end4ceil_half_ez4B, /):
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,_try_to_find_counterexample_in_src_code__between____ =0 =100000  =0 =10
===
((292, 0), [1, -1, -1], (831285, 838508, 1180733))
((367, 1), [1, -1, -1], (2622480, 2642431, 3722881))
((500, 1), [1, -1, -1], (4852848, 4873775, 6877777))
((742, 1), [1, -1, -1], (10668240, 10697239, 15107689))
((1193, 1), [1, -1, -1], (27545980, 27595131, 38990669))
((1522, 0), [1, -1, -1], (22414245, 22456148, 31728173))
((2131, 0), [1, -1, -1], (43913163, 43968716, 62141885))
((2177, 0), [1, -1, -1], (45818955, 45862708, 64828733))
((2902, 1), [1, -1, -1], (162818640, 162974551, 230370601))
((2932, 0), [1, -1, -1], (83089455, 83152832, 117551057))
((3172, 1), [1, -1, -1], (194486940, 194627251, 275145301))
((3412, 1), [1, -1, -1], (225033900, 225207571, 318368821))
((3454, 0), [1, -1, -1], (115290483, 115360844, 163095125))
((3685, 0), [1, -1, -1], (131225913, 131307584, 185639225))
((4075, 1), [1, -1, -1], (320953776, 321178543, 454056145))
((4567, 0), [1, -1, -1], (201527235, 201619748, 285067973))
((4819, 0), [1, -1, -1], (224386281, 224500760, 317411081))
((5347, 0), [1, -1, -1], (276262545, 276428768, 390811793))
((5428, 0), [1, -1, -1], (284659683, 284780756, 402655205))
((6517, 0), [1, -1, -1], (410302695, 410445152, 580356377))
((6604, 1), [1, -1, -1], (842681364, 843004723, 1191960085))
((7039, 0), [1, -1, -1], (478643763, 478788884, 677007125))
((7087, 0), [1, -1, -1], (485196075, 485346908, 686277533))
((7117, 1), [1, -1, -1], (978684720, 979074151, 1384344601))
((7267, 0), [1, -1, -1], (510163965, 510336788, 721603013))
((7702, 0), [1, -1, -1], (573050595, 573225788, 810539813))
((8242, 1), [1, -1, -1], (1312403820, 1312762411, 1856272861))
((8387, 1), [1, -1, -1], (1358976300, 1359335411, 1922136661))
((10177, 0), [1, -1, -1], (1000509315, 1000845692, 1415171717))
((10657, 1), [1, -1, -1], (2193995580, 2194419931, 3103078381))
((10744, 0), [1, -1, -1], (1114999743, 1115241824, 1577018945))
((10762, 1), [1, -1, -1], (2237480700, 2237971051, 3164622301))
((11212, 1), [1, -1, -1], (2428448100, 2428908691, 3434669941))
((11371, 1), [1, -1, -1], (2497818204, 2498303347, 3532791445))
((11797, 0), [1, -1, -1], (1344230745, 1344485408, 1901209433))
((11917, 0), [1, -1, -1], (1371728085, 1372005188, 1940112413))
((12022, 0), [1, -1, -1], (1395980565, 1396226612, 1974388637))
((13117, 1), [1, -1, -1], (3323659680, 3324187111, 4700737561))
((13513, 1), [1, -1, -1], (3527455932, 3528147835, 4989065293))
((14332, 0), [1, -1, -1], (1983933315, 1984240148, 2805922373))
((14437, 0), [1, -1, -1], (2013136125, 2013486668, 2847252293))
((14527, 1), [1, -1, -1], (4076648940, 4077390691, 5765776741))
((15298, 0), [1, -1, -1], (2260414569, 2260817360, 3196993769))
((15427, 1), [1, -1, -1], (4597271580, 4597920979, 6501983029))
((15592, 1), [1, -1, -1], (4696211520, 4696983391, 6641991841))
((15682, 0), [1, -1, -1], (2375302815, 2375710568, 3359473793))
((15697, 1), [1, -1, -1], (4759607580, 4760297179, 6731589229))
((15757, 0), [1, -1, -1], (2398007865, 2398322528, 3391517753))
((17242, 1), [1, -1, -1], (5742718080, 5743678471, 8122108921))
((17297, 0), [1, -1, -1], (2889616565, 2889972852, 4086786877))
((18112, 1), [1, -1, -1], (6336766800, 6337700671, 8962201921))
((18154, 0), [1, -1, -1], (3183028485, 3183404372, 4501747853))
((18232, 1), [1, -1, -1], (6420903060, 6421697539, 9081089989))
((18667, 1), [1, -1, -1], (6730903140, 6731677939, 9519482389))
((18892, 0), [1, -1, -1], (3447087765, 3447512108, 4875218333))
((18997, 1), [1, -1, -1], (6971018640, 6971873671, 9859113721))
((19267, 0), [1, -1, -1], (3585334935, 3585840728, 5070786953))
((19987, 1), [1, -1, -1], (7716614100, 7717723699, 10913724949))
((20065, 0), [1, -1, -1], (3888412983, 3888878144, 5499375305))
((20227, 1), [1, -1, -1], (7902965160, 7903993951, 11177208001))
((21004, 1), [1, -1, -1], (8521609668, 8522477395, 12051989557))
((21532, 1), [1, -1, -1], (8955452880, 8956414351, 12665602801))
((21787, 0), [1, -1, -1], (4584482175, 4585076528, 6483857153))
((22669, 0), [1, -1, -1], (4963033635, 4963480652, 7019105573))
((22885, 1), [1, -1, -1], (10116306420, 10117475659, 14307444541))
((22942, 1), [1, -1, -1], (10166831220, 10168104571, 14378971021))
((23287, 0), [1, -1, -1], (5237405325, 5237998388, 7407229013))
((23842, 1), [1, -1, -1], (10980138840, 10981518199, 15529236649))
((24667, 1), [1, -1, -1], (11752978380, 11754202771, 16622087221))
((24697, 0), [1, -1, -1], (5890699515, 5891183012, 8331049037))
((24832, 0), [1, -1, -1], (5955280485, 5955778028, 8422390253))
((25012, 0), [1, -1, -1], (6041969475, 6042533108, 8545033733))
((25336, 0), [1, -1, -1], (6199588185, 6200273048, 8768025977))
((25447, 0), [1, -1, -1], (6253926705, 6254473808, 8844774833))
((25627, 0), [1, -1, -1], (6342857505, 6343617488, 8970692513))
((25987, 1), [1, -1, -1], (13044269700, 13045335571, 18448136821))
((26218, 0), [1, -1, -1], (6638576637, 6639087116, 9388726085))
((26422, 1), [1, -1, -1], (13484564340, 13485593371, 19070781421))
((27307, 0), [1, -1, -1], (7201588515, 7202262548, 10185060773))
((27367, 0), [1, -1, -1], (7233175515, 7233718988, 10229639213))
((27709, 1), [1, -1, -1], (14830346076, 14831709643, 20974240765))
((27922, 0), [1, -1, -1], (7529748885, 7530636932, 10649300957))
((28507, 1), [1, -1, -1], (15696685620, 15697913491, 22199333941))
((28840, 1), [1, -1, -1], (16065542844, 16066806883, 22721002405))
((29542, 0), [1, -1, -1], (8428534335, 8429135288, 11920172513))
((29620, 1), [1, -1, -1], (16946480460, 16948084819, 23967076981))
((29662, 0), [1, -1, -1], (8497179075, 8497831868, 12017287493))
((30271, 0), [1, -1, -1], (8849630853, 8850253196, 12515708045))
((30387, 0), [1, -1, -1], (8917698075, 8918486332, 12612086957))
((30442, 0), [1, -1, -1], (8950034115, 8950861388, 12657844613))
((30523, 0), [1, -1, -1], (8997656283, 8998390556, 12725126765))
((31207, 0), [1, -1, -1], (9405378765, 9406072628, 13301704853))
((32077, 0), [1, -1, -1], (9937032105, 9937678928, 14053542953))
((32182, 0), [1, -1, -1], (10002256635, 10002997988, 14145851213))
((32632, 0), [1, -1, -1], (10283871315, 10284549908, 14544070133))
((32665, 1), [1, -1, -1], (20609317260, 20610613339, 29146892461))
((33082, 1), [1, -1, -1], (21139188180, 21140977291, 29896591741))
((33247, 0), [1, -1, -1], (10675173795, 10675913828, 15097498853))
((33337, 1), [1, -1, -1], (21466149600, 21467716951, 30358828201))
((33442, 1), [1, -1, -1], (21601447140, 21602833099, 30550039549))
((34402, 0), [1, -1, -1], (11429680185, 11430364832, 16164492857))
((34552, 1), [1, -1, -1], (23059509240, 23061419311, 32612421361))
((34996, 1), [1, -1, -1], (23655674196, 23657248147, 33455288245))
((35752, 1), [1, -1, -1], (24688674360, 24690223471, 34916153521))
((35857, 1), [1, -1, -1], (24834043920, 24835803511, 35121885961))
((35977, 0), [1, -1, -1], (12500238465, 12501079352, 17678601377))
((36949, 0), [1, -1, -1], (13184837883, 13185781844, 18646844045))
((37012, 0), [1, -1, -1], (13229822025, 13230747608, 18710448233))
((37087, 1), [1, -1, -1], (26567111400, 26569148431, 37573009681))
((37117, 0), [1, -1, -1], (13304916345, 13305741152, 18816576377))
((37425, 1), [1, -1, -1], (27053247228, 27054877595, 38260221997))
((39532, 0), [1, -1, -1], (15092638785, 15093668048, 21344942273))
((39682, 0), [1, -1, -1], (15207207015, 15207986048, 21506789273))
((40036, 0), [1, -1, -1], (15479792433, 15480661856, 21892347185))
((40072, 1), [1, -1, -1], (31015473840, 31017480991, 43863923041))
((40177, 1), [1, -1, -1], (31178061420, 31179849979, 44093702029))
((40237, 0), [1, -1, -1], (15635568225, 15636383528, 22112609153))
((40498, 0), [1, -1, -1], (15839044347, 15839839796, 22400353805))
((40657, 0), [1, -1, -1], (15963679485, 15964510268, 22576639493))
((40672, 1), [1, -1, -1], (31951665240, 31954379791, 45188397841))
((40687, 1), [1, -1, -1], (31974841500, 31976998531, 45220779781))
((42607, 1), [1, -1, -1], (35063586480, 35065705471, 49588897921))
((42763, 1), [1, -1, -1], (35320598352, 35322426415, 49952161873))
((43081, 0), [1, -1, -1], (17924058075, 17925169028, 25349231597))
((43207, 1), [1, -1, -1], (36058214220, 36060593731, 50995698181))
((43477, 1), [1, -1, -1], (36509969760, 36511952071, 51634296121))
((44089, 1), [1, -1, -1], (37544854620, 37546616059, 53097688141))
((44362, 0), [1, -1, -1], (19005870975, 19007113448, 26879239073))
((44467, 0), [1, -1, -1], (19095856395, 19096977932, 27006412157))
((44722, 0), [1, -1, -1], (19315379415, 19316349392, 27316757417))
((45160, 0), [1, -1, -1], (19695848865, 19697230592, 27855113633))
((45457, 1), [1, -1, -1], (39910957680, 39912956791, 56444031241))
((46177, 1), [1, -1, -1], (41185527540, 41187958651, 58246850701))
((46252, 1), [1, -1, -1], (41319023340, 41320900531, 58435250581))
((46312, 2), [1, -1, -1], (165705013500, 165712316509, 234347441509))
((46546, 1), [1, -1, -1], (41846792988, 41849851915, 59182465213))
((46777, 0), [1, -1, -1], (21131361405, 21132585308, 29885123333))
((46897, 0), [1, -1, -1], (21239971545, 21241276688, 30038778713))
((47407, 0), [1, -1, -1], (21704196465, 21705180848, 30695065073))
((47482, 1), [1, -1, -1], (43546010820, 43548215851, 61584918301))
((47785, 1), [1, -1, -1], (44103722796, 44106208603, 62373840685))
((47794, 1), [1, -1, -1], (44120058840, 44122151479, 62396665321))
((49417, 1), [1, -1, -1], (47167224720, 47169238231, 66705952681))
((49927, 0), [1, -1, -1], (24072943545, 24074031608, 34045052633))
((51082, 1), [1, -1, -1], (50399220480, 50401495111, 71276869561))
((51187, 1), [1, -1, -1], (50606419500, 50608413619, 71569694869))
((51418, 1), [1, -1, -1], (51064329372, 51066516715, 72217413853))
((51577, 1), [1, -1, -1], (51380680260, 51382956091, 72664864141))
((51772, 0), [1, -1, -1], (25885111005, 25886466548, 36608033573))
((52552, 1), [1, -1, -1], (53341628340, 53344031491, 75438153541))
((53161, 1), [1, -1, -1], (54584952324, 54587229307, 77196389965))
((53497, 1), [1, -1, -1], (55277040840, 55279225831, 78175085881))
((53527, 0), [1, -1, -1], (27669542355, 27670657748, 39131430773))
((53602, 1), [1, -1, -1], (55494453840, 55496950951, 78482775001))
((53779, 0), [1, -1, -1], (27930813561, 27932122280, 39501060761))
((53839, 0), [1, -1, -1], (27992986593, 27994037024, 39588804065))
((53854, 1), [1, -1, -1], (56017727556, 56020613083, 79223070445))
((54102, 0), [1, -1, -1], (28267149585, 28268224072, 39976546097))
((54307, 0), [1, -1, -1], (28482002835, 28483415108, 40280633333))
((54757, 0), [1, -1, -1], (28955875515, 28957176788, 40950712013))
((54862, 0), [1, -1, -1], (29066920575, 29068071512, 41107647137))
((54952, 1), [1, -1, -1], (58324825020, 58327267939, 82485485989))
((55192, 0), [1, -1, -1], (29417712885, 29418967388, 41603815613))
((55432, 0), [1, -1, -1], (29674015035, 29675146028, 41966194253))
((56192, 0), [1, -1, -1], (30493309665, 30494519008, 43124907233))
((57172, 0), [1, -1, -1], (31566195045, 31567448348, 44642227373))
((57277, 0), [1, -1, -1], (31682361795, 31683781868, 44806629893))
((58012, 0), [1, -1, -1], (32500574925, 32501866532, 45963667157))
((58327, 0), [1, -1, -1], (32854597545, 32856068648, 46464457673))
((58432, 1), [1, -1, -1], (65945984580, 65948937091, 93263793541))
((58537, 1), [1, -1, -1], (66182965800, 66185597479, 93598708729))
((58636, 0), [1, -1, -1], (33203387217, 33204537056, 46957493585))
((59377, 1), [1, -1, -1], (68096017080, 68098727239, 96304227289))
((59662, 1), [1, -1, -1], (68751723900, 68755087771, 97231999021))
((60001, 1), [1, -1, -1], (69534538320, 69536958391, 98338398409))
((60637, 0), [1, -1, -1], (35508471075, 35510057612, 50217683237))
((60700, 1), [1, -1, -1], (71164294992, 71167062415, 100643468017))
((60823, 0), [1, -1, -1], (35726385783, 35727618056, 50525610665))
((60952, 1), [1, -1, -1], (71756696340, 71759901571, 101481559621))
((60967, 1), [1, -1, -1], (71791913820, 71794972771, 101531261221))
((61132, 1), [1, -1, -1], (72181832580, 72186044371, 102083504821))
((61330, 0), [1, -1, -1], (36324460557, 36325700924, 51371421845))
((61561, 1), [1, -1, -1], (73197608484, 73200667387, 103519213645))
((61807, 0), [1, -1, -1], (36891784215, 36893181128, 52173849353))
((62092, 1), [1, -1, -1], (74465299920, 74467719631, 105311548081))
((62107, 0), [1, -1, -1], (37250960565, 37252622828, 52681989053))
((63202, 1), [1, -1, -1], (77151544560, 77154166951, 109110615001))
((63238, 1), [1, -1, -1], (77239503900, 77242190971, 109235054029))
((63562, 1), [1, -1, -1], (78032884500, 78035437771, 110356969021))
((63706, 1), [1, -1, -1], (78387025860, 78389839531, 110857984669))
((64102, 1), [1, -1, -1], (79365048840, 79368584551, 112241628601))
((64162, 0), [1, -1, -1], (39756496575, 39757775048, 56225080673))
((64627, 0), [1, -1, -1], (40335186045, 40336982228, 57043837253))
((65071, 0), [1, -1, -1], (40891060743, 40892533976, 57829734425))
((65152, 0), [1, -1, -1], (40992780255, 40994052128, 57973445153))
((65407, 1), [1, -1, -1], (82629033120, 82632234751, 116857363201))
((65782, 1), [1, -1, -1], (83579560680, 83583279271, 118201977721))
((66202, 0), [1, -1, -1], (42324714705, 42326035448, 59857119473))
((66544, 1), [1, -1, -1], (85526717892, 85530004675, 120955368517))
((66742, 0), [1, -1, -1], (43018344435, 43020176108, 60838421333))
((67102, 0), [1, -1, -1], (43483359435, 43484777012, 61495759037))
((67417, 0), [1, -1, -1], (43892702715, 43894326308, 62074803533))
((67672, 0), [1, -1, -1], (44225196855, 44226587528, 62544856553))
((68062, 1), [1, -1, -1], (89472784500, 89475548539, 126535579789))
((68722, 0), [1, -1, -1], (45608236905, 45609678608, 64500806633))
((68827, 1), [1, -1, -1], (91495424160, 91498317871, 129396115921))
((68854, 1), [1, -1, -1], (91567671624, 91571202343, 129498739705))
((69317, 1), [1, -1, -1], (92802823540, 92805765579, 131245092029))
((69322, 1), [1, -1, -1], (92816172540, 92819059051, 131263931101))
((69757, 1), [1, -1, -1], (93984558780, 93987319051, 132916189501))
((70003, 0), [1, -1, -1], (47324466105, 47326090088, 66928050137))
((71284, 0), [1, -1, -1], (49072392369, 49074204320, 69400124081))
((71347, 1), [1, -1, -1], (98317996560, 98321142991, 139044869041))
((71697, 1), [1, -1, -1], (99284977260, 99288159611, 140412411661))
((71722, 1), [1, -1, -1], (99354597240, 99358303831, 140511239881))
((72057, 1), [1, -1, -1], (100284440360, 100287543399, 141825809849))
((72484, 0), [1, -1, -1], (50738135217, 50739544544, 71755555505))
((72502, 0), [1, -1, -1], (50763495405, 50765128268, 71791578293))
((72607, 0), [1, -1, -1], (50910491205, 50911924172, 71999320397))
((72862, 0), [1, -1, -1], (51269115225, 51271120208, 72506895833))
((73027, 1), [1, -1, -1], (103002659760, 103005980431, 145670106481))
((73342, 1), [1, -1, -1], (103892878320, 103895817271, 146928795721))
((73846, 1), [1, -1, -1], (105325786020, 105328942651, 148955387149))
((74035, 1), [1, -1, -1], (105865434444, 105868359283, 149718401365))
((74917, 0), [1, -1, -1], (54201462735, 54203011928, 76653539153))
((75022, 0), [1, -1, -1], (54353651205, 54355417988, 76868920013))
((75757, 1), [1, -1, -1], (110847767940, 110851381579, 156764972029))
((76037, 0), [1, -1, -1], (55834184175, 55835791288, 78962596913))
((76177, 1), [1, -1, -1], (112080260460, 112083920251, 158508012301))
((76282, 1), [1, -1, -1], (112389143160, 112392382999, 158944541449))
((76807, 0), [1, -1, -1], (56971348665, 56973865208, 80571433433))
((77192, 1), [1, -1, -1], (115086607020, 115089942851, 162759399301))
((77647, 1), [1, -1, -1], (116447645160, 116451468751, 164684542801))
((78259, 1), [1, -1, -1], (118290173364, 118293585523, 167289980245))
((78292, 2), [1, -1, -1], (473557510140, 473567908141, 669718805941))
((78592, 1), [1, -1, -1], (119299013820, 119302499971, 168716748421))
((78697, 1), [1, -1, -1], (119618311260, 119622254011, 169168626061))
((78721, 0), [1, -1, -1], (59845816173, 59848037036, 84636335285))
((79117, 0), [1, -1, -1], (60449092935, 60450864608, 85489179833))
((79852, 0), [1, -1, -1], (61577616555, 61579654508, 87085341533))
((79942, 1), [1, -1, -1], (123433138620, 123437418811, 174563845261))
((79982, 0), [1, -1, -1], (61778003105, 61779660792, 87368462017))
((80437, 1), [1, -1, -1], (124965769500, 124969133611, 176730664861))
((80797, 0), [1, -1, -1], (63043542135, 63045406832, 89158350857))
((81217, 1), [1, -1, -1], (127401668940, 127405905019, 180176163469))
((81592, 0), [1, -1, -1], (64290157635, 64291902308, 90921246533))
((82015, 0), [1, -1, -1], (64958408403, 64960063604, 91866232565))
((82120, 0), [1, -1, -1], (65125005561, 65126898680, 92102004761))
((82372, 0), [1, -1, -1], (65525511555, 65527698548, 92668613573))
((82594, 0), [1, -1, -1], (65878859901, 65880606380, 93168012101))
((83077, 0), [1, -1, -1], (66651582855, 66653308928, 94260792953))
((83401, 0), [1, -1, -1], (67172735721, 67174843520, 94998084329))
((83527, 1), [1, -1, -1], (134751908760, 134756422831, 190571168881))
((83932, 0), [1, -1, -1], (68030480685, 68032152068, 96210810293))
((84402, 0), [1, -1, -1], (68794620895, 68796454248, 97291582273))
((84937, 1), [1, -1, -1], (139338949500, 139342539259, 197057570509))
((85312, 0), [1, -1, -1], (70286750625, 70289600672, 99402491297))
((85849, 1), [1, -1, -1], (142347399348, 142351258075, 201312351277))
((85858, 2), [1, -1, -1], (569506299180, 569517935869, 805411760581))
((86047, 1), [1, -1, -1], (143005437960, 143010265231, 202243643281))
((86212, 0), [1, -1, -1], (71776906575, 71778912608, 101509293233))
((86572, 0), [1, -1, -1], (72378246045, 72381182708, 102360373733))
((86572, 1), [1, -1, -1], (144754760640, 144758185231, 204716567281))
((86614, 0), [1, -1, -1], (72447659151, 72449422760, 102457709201))
((86677, 1), [1, -1, -1], (145107149460, 145112056651, 205215968701))
((87262, 0), [1, -1, -1], (73535934225, 73538002088, 103996977713))
((87442, 0), [1, -1, -1], (73839769815, 73842060368, 104426823593))
((88112, 1), [1, -1, -1], (149950557400, 149954153679, 212064654929))
((88561, 1), [1, -1, -1], (151483383012, 151488017755, 214233132013))
((88852, 1), [1, -1, -1], (152480130660, 152484241651, 215642375701))
((89092, 1), [1, -1, -1], (153304672080, 153308379631, 216808168081))
((89537, 1), [1, -1, -1], (154840422100, 154844831931, 218980543181))
((90205, 1), [1, -1, -1], (157159630320, 157164384679, 222260642521))
((90247, 0), [1, -1, -1], (78652681695, 78654602048, 111233047073))
((90447, 1), [1, -1, -1], (158003099540, 158006598051, 223452600101))
((90772, 1), [1, -1, -1], (159140894640, 159144796591, 225061970641))
((90967, 0), [1, -1, -1], (79912583595, 79914398972, 113014743197))
((91591, 1), [1, -1, -1], (162026096232, 162030820015, 229142842993))
((91987, 1), [1, -1, -1], (163430143800, 163434858271, 231128459521))
((92662, 0), [1, -1, -1], (82918296825, 82920097808, 117265453433))
((92767, 0), [1, -1, -1], (83106507015, 83108576408, 117531812633))
((92782, 0), [1, -1, -1], (83133305565, 83135263388, 117569632613))
((93667, 1), [1, -1, -1], (169454248920, 169459177951, 239647982401))
((93712, 0), [1, -1, -1], (84808125675, 84809987228, 119938117853))
((93742, 1), [1, -1, -1], (169724920920, 169728723271, 240029973721))
((93892, 0), [1, -1, -1], (85134395385, 85136495048, 120399701273))
((93922, 1), [1, -1, -1], (170377669140, 170381948011, 240953436061))
((94027, 1), [1, -1, -1], (170758453320, 170762213119, 241491579169))
((94087, 1), [1, -1, -1], (170977310400, 170982293791, 241801955041))
((94627, 0), [1, -1, -1], (86472691305, 86475103448, 122292558473))
((94990, 1), [1, -1, -1], (174274130844, 174278049883, 246463610605))
((95392, 1), [1, -1, -1], (175752668280, 175757128591, 248554961041))
((95497, 1), [1, -1, -1], (176140936860, 176147030971, 249105211021))
((96337, 1), [1, -1, -1], (179251718100, 179255751931, 253503063181))
((96442, 1), [1, -1, -1], (179643830520, 179649513751, 254058760201))
((97312, 1), [1, -1, -1], (182898454500, 182902685251, 258660466501))
((97345, 0), [1, -1, -1], (91511194803, 91513217804, 129417803285))
((97597, 0), [1, -1, -1], (91986229335, 91989150992, 130090239017))
((97702, 0), [1, -1, -1], (92183676585, 92185776512, 130368890537))
((97762, 0), [1, -1, -1], (92297380725, 92300116388, 130530142013))
((97954, 0), [1, -1, -1], (92659667457, 92661561224, 131041897505))
((99157, 0), [1, -1, -1], (94949850645, 94952160932, 134281000157))
((99394, 0), [1, -1, -1], (95404208403, 95406429404, 134923495925))
((99676, 0), [1, -1, -1], (95946406017, 95948741456, 135690360065))
((99781, 0), [1, -1, -1], (96148455585, 96150515528, 135975906497))
((99808, 0), [1, -1, -1], (96200422725, 96202379468, 136049326157))
===
NOTE: all above counterexample: [1, -1, -1]
===
NOTE: exists counterexample:[ceil_half_ez4B > 1]:
    ((46312, 2), [1, -1, -1], (165705013500, 165712316509, 234347441509))
    ((78292, 2), [1, -1, -1], (473557510140, 473567908141, 669718805941))
    ((85858, 2), [1, -1, -1], (569506299180, 569517935869, 805411760581))
===
#see:((292, 0), [1, -1, -1], (831285, 838508, 1180733))
((46312, 2), [1, -1, -1], (165705013500, 165712316509, 234347441509))
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1:iter_right_angled_triangle_side_length_difference_ratio__given_B_  +with_side_length_ratio +with_params =46312 =2
((7303009, 68635125000), (165705013500, 165712316509, 234347441509), (46312, 2, 261997))
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1:iter_right_angled_triangle_side_length_difference_ratio__given_B_  +with_side_length_ratio +with_params =46312+1 =2
((147089, 68638089032), (165707109444, 165707256533, 234345345565), (46313, 2, 261989))
    [234345345565 < 234347441509]
    [hypotenuse(46312,2): (+1,+0) < (+0,+0)]
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1:iter_right_angled_triangle_side_length_difference_ratio__given_B_  +with_side_length_ratio +with_params =46312 =2+1
((917089, 274540500000), (662800047000, 662800964089, 937341464089), (46312, 3, 523967))
py_adhoc_call   seed.math.factor_pint_by_trial_division_   @factor_pint_by_trial_division_ =234347441509
{317: 1, 449: 1, 1646473: 1}

>>> for k in {317: 1, 449: 1, 1646473: 1}: (k, divmod(k,4))
(317, (79, 1))
(449, (112, 1))
(1646473, (411618, 1))

===
]]]
[[[
try to search:[ceil_half_ez4B > 1]
    ...
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,_try_to_find_counterexample_in_src_code__between____ =292 =293  =0 =10000
((292, 0), [1, -1, -1], (831285, 838508, 1180733))

===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,_try_to_find_counterexample_in_src_code__between____ =0 =100  =0 =1000
    <EMPTY>

===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,_try_to_find_counterexample_in_src_code__between____ =0 =1000  =0 =100
((292, 0), [1, -1, -1], (831285, 838508, 1180733))
((367, 1), [1, -1, -1], (2622480, 2642431, 3722881))
((500, 1), [1, -1, -1], (4852848, 4873775, 6877777))
((742, 1), [1, -1, -1], (10668240, 10697239, 15107689))

===
]]]

[[[
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_ +SML_vs_HOE +buggy_plus1__vs__layered +_to_show_layer_line
===
=========[(b0,b1)==(1, 2)][size==1]
(5, 3, 4)
=========[(b0,b1)==(2, 4)][size==1]
(13, 5, 12)
=========[(b0,b1)==(4, 7)][size==2]
(17, 15, 8)
(25, 7, 24)
=========[(b0,b1)==(7, 11)][size==2]
(29, 21, 20)
(37, 35, 12)
=========[(b0,b1)==(11, 16)][size==2]
(41, 9, 40)
(53, 45, 28)
=========[(b0,b1)==(16, 21)][size==4]
(61, 11, 60)
(65, 33, 56)
(65, 63, 16)
(73, 55, 48)
=========[(b0,b1)==(21, 27)][size==3]
(85, 13, 84)
(85, 77, 36)
(89, 39, 80)
=========[(b0,b1)==(27, 33)][size==4]
(97, 65, 72)
(101, 99, 20)
(109, 91, 60)
(113, 15, 112)
=========[(b0,b1)==(33, 40)][size==2]
(125, 117, 44)
(137, 105, 88)
=========[(b0,b1)==(40, 47)][size==4]
(145, 17, 144)
(145, 143, 24)
(149, 51, 140)
(157, 85, 132)
=========[(b0,b1)==(47, 54)][size==5]
(169, 119, 120)
(173, 165, 52)
(181, 19, 180)
(185, 57, 176)
(185, 153, 104)
=========[(b0,b1)==(54, 61)][size==4]
(193, 95, 168)
(197, 195, 28)
(205, 133, 156)
(205, 187, 84)
=========[(b0,b1)==(61, 68)][size==4]
(221, 21, 220)
(221, 171, 140)
(229, 221, 60)
(233, 105, 208)
=========[(b0,b1)==(68, 76)][size==2]
(241, 209, 120)
(257, 255, 32)
=========[(b0,b1)==(76, 84)][size==5]
(265, 23, 264)
(265, 247, 96)
(269, 69, 260)
(277, 115, 252)
(281, 231, 160)
=========[(b0,b1)==(84, 92)][size==5]
(289, 161, 240)
(293, 285, 68)
(305, 207, 224)
(305, 273, 136)
(313, 25, 312)
=========[(b0,b1)==(92, 100)][size==4]
(317, 75, 308)
(325, 253, 204)
(325, 323, 36)
(337, 175, 288)
=========[(b0,b1)==(100, 108)][size==4]
(349, 299, 180)
(353, 225, 272)
(365, 27, 364)
(365, 357, 76)
=========[(b0,b1)==(108, 116)][size==5]
(373, 275, 252)
(377, 135, 352)
(377, 345, 152)
(389, 189, 340)
(397, 325, 228)
=========[(b0,b1)==(116, 124)][size==5]
(401, 399, 40)
(409, 391, 120)
(421, 29, 420)
(425, 87, 416)
(425, 297, 304)
=========[(b0,b1)==(124, 132)][size==4]
(433, 145, 408)
(445, 203, 396)
(445, 437, 84)
(449, 351, 280)
=========[(b0,b1)==(132, 141)][size==4]
(457, 425, 168)
(461, 261, 380)
(481, 31, 480)
(481, 319, 360)
=========[(b0,b1)==(141, 150)][size==7]
(485, 93, 476)
(485, 483, 44)
(493, 155, 468)
(493, 475, 132)
(505, 217, 456)
(505, 377, 336)
(509, 459, 220)
=========[(b0,b1)==(150, 159)][size==4]
(521, 279, 440)
(533, 435, 308)
(533, 525, 92)
(541, 341, 420)
=========[(b0,b1)==(159, 168)][size==6]
(545, 33, 544)
(545, 513, 184)
(557, 165, 532)
(565, 403, 396)
(565, 493, 276)
(569, 231, 520)
=========[(b0,b1)==(168, 177)][size==3]
(577, 575, 48)
(593, 465, 368)
(601, 551, 240)
=========[(b0,b1)==(177, 186)][size==5]
(613, 35, 612)
(617, 105, 608)
(625, 527, 336)
(629, 429, 460)
(629, 621, 100)
=========[(b0,b1)==(186, 195)][size==3]
(641, 609, 200)
(653, 315, 572)
(661, 589, 300)
=========[(b0,b1)==(195, 204)][size==8]
(673, 385, 552)
(677, 675, 52)
(685, 37, 684)
(685, 667, 156)
(689, 111, 680)
(689, 561, 400)
(697, 185, 672)
(697, 455, 528)
=========[(b0,b1)==(204, 213)][size==4]
(701, 651, 260)
(709, 259, 660)
(725, 333, 644)
(725, 627, 364)
=========[(b0,b1)==(213, 222)][size==4]
(733, 725, 108)
(745, 407, 624)
(745, 713, 216)
(757, 595, 468)
=========[(b0,b1)==(222, 231)][size==5]
(761, 39, 760)
(769, 481, 600)
(773, 195, 748)
(785, 273, 736)
(785, 783, 56)
=========[(b0,b1)==(231, 240)][size==5]
(793, 665, 432)
(793, 775, 168)
(797, 555, 572)
(809, 759, 280)
(821, 429, 700)
=========[(b0,b1)==(240, 249)][size==4]
(829, 629, 540)
(841, 41, 840)
(845, 123, 836)
(845, 837, 116)
=========[(b0,b1)==(249, 258)][size==6]
(853, 205, 828)
(857, 825, 232)
(865, 287, 816)
(865, 703, 504)
(877, 805, 348)
(881, 369, 800)
=========[(b0,b1)==(258, 268)][size==4]
(901, 451, 780)
(901, 899, 60)
(905, 663, 616)
(905, 777, 464)
=========[(b0,b1)==(268, 278)][size==7]
(925, 43, 924)
(925, 533, 756)
(929, 129, 920)
(937, 215, 912)
(941, 741, 580)
(949, 301, 900)
(949, 851, 420)
=========[(b0,b1)==(278, 288)][size==4]
(953, 615, 728)
(965, 387, 884)
(965, 957, 124)
(977, 945, 248)
=========[(b0,b1)==(288, 298)][size==5]
(985, 473, 864)
(985, 697, 696)
(997, 925, 372)
(1009, 559, 840)
(1013, 45, 1012)
=========[(b0,b1)==(298, 308)][size==7]
(1021, 779, 660)
(1025, 897, 496)
(1025, 1023, 64)
(1033, 1015, 192)
(1037, 315, 988)
(1037, 645, 812)
(1049, 999, 320)
=========[(b0,b1)==(308, 318)][size==4]
(1061, 861, 620)
(1069, 731, 780)
(1073, 495, 952)
(1073, 975, 448)
=========[(b0,b1)==(318, 328)][size==8]
(1093, 1085, 132)
(1097, 585, 928)
(1105, 47, 1104)
(1105, 817, 744)
(1105, 943, 576)
(1105, 1073, 264)
(1109, 141, 1100)
(1117, 235, 1092)
=========[(b0,b1)==(328, 338)][size==4]
(1129, 329, 1080)
(1145, 423, 1064)
(1145, 903, 704)
(1153, 1025, 528)
=========[(b0,b1)==(338, 348)][size==7]
(1157, 765, 868)
(1157, 1155, 68)
(1165, 517, 1044)
(1165, 1147, 204)
(1181, 1131, 340)
(1189, 611, 1020)
(1189, 989, 660)
=========[(b0,b1)==(348, 358)][size==6]
(1193, 855, 832)
(1201, 49, 1200)
(1205, 147, 1196)
(1205, 1107, 476)
(1213, 245, 1188)
(1217, 705, 992)
=========[(b0,b1)==(358, 368)][size==5]
(1229, 1221, 140)
(1237, 1075, 612)
(1241, 441, 1160)
(1241, 1209, 280)
(1249, 799, 960)
=========[(b0,b1)==(368, 378)][size==6]
(1261, 539, 1140)
(1261, 1189, 420)
(1277, 1035, 748)
(1285, 637, 1116)
(1285, 893, 924)
(1289, 1161, 560)
=========[(b0,b1)==(378, 388)][size==7]
(1297, 1295, 72)
(1301, 51, 1300)
(1313, 255, 1288)
(1313, 735, 1088)
(1321, 1271, 360)
(1325, 357, 1276)
(1325, 987, 884)
=========[(b0,b1)==(388, 398)][size==2]
(1345, 833, 1056)
(1345, 1247, 504)
=========[(b0,b1)==(398, 408)][size==6]
(1361, 561, 1240)
(1369, 1081, 840)
(1373, 1365, 148)
(1381, 931, 1020)
(1385, 663, 1216)
(1385, 1353, 296)
=========[(b0,b1)==(408, 418)][size==5]
(1405, 53, 1404)
(1405, 1333, 444)
(1409, 159, 1400)
(1417, 265, 1392)
(1417, 1175, 792)
=========[(b0,b1)==(418, 428)][size==5]
(1429, 371, 1380)
(1433, 1305, 592)
(1445, 477, 1364)
(1445, 1443, 76)
(1453, 1435, 228)
=========[(b0,b1)==(428, 438)][size==7]
(1465, 583, 1344)
(1465, 1127, 936)
(1469, 1269, 740)
(1469, 1419, 380)
(1481, 969, 1120)
(1489, 689, 1320)
(1493, 1395, 532)
=========[(b0,b1)==(438, 448)][size==6]
(1513, 55, 1512)
(1513, 1225, 888)
(1517, 165, 1508)
(1517, 795, 1292)
(1525, 1363, 684)
(1525, 1517, 156)
=========[(b0,b1)==(448, 458)][size==6]
(1537, 385, 1488)
(1537, 1505, 312)
(1549, 901, 1260)
(1553, 495, 1472)
(1565, 1173, 1036)
(1565, 1323, 836)
=========[(b0,b1)==(458, 468)][size==3]
(1585, 1007, 1224)
(1585, 1457, 624)
(1597, 715, 1428)
=========[(b0,b1)==(468, 478)][size==6]
(1601, 1599, 80)
(1609, 1591, 240)
(1613, 1275, 988)
(1621, 1421, 780)
(1625, 57, 1624)
(1625, 1113, 1184)
=========[(b0,b1)==(478, 488)][size==4]
(1637, 285, 1612)
(1649, 399, 1600)
(1649, 1551, 560)
(1657, 935, 1368)
=========[(b0,b1)==(488, 498)][size==6]
(1669, 1219, 1140)
(1681, 1519, 720)
(1685, 627, 1564)
(1685, 1677, 164)
(1693, 1045, 1332)
(1697, 1665, 328)
=========[(b0,b1)==(498, 508)][size==5]
(1709, 741, 1540)
(1717, 1325, 1092)
(1717, 1645, 492)
(1721, 1479, 880)
(1733, 1155, 1292)
=========[(b0,b1)==(508, 518)][size==8]
(1741, 59, 1740)
(1745, 177, 1736)
(1745, 1617, 656)
(1753, 295, 1728)
(1765, 413, 1716)
(1765, 1763, 84)
(1769, 969, 1480)
(1769, 1431, 1040)
=========[(b0,b1)==(518, 529)][size==5]
(1777, 1265, 1248)
(1781, 531, 1700)
(1781, 1581, 820)
(1789, 1739, 420)
(1801, 649, 1680)
=========[(b0,b1)==(529, 540)][size==2]
(1825, 767, 1656)
(1825, 1537, 984)
=========[(b0,b1)==(540, 551)][size==7]
(1853, 885, 1628)
(1853, 1845, 172)
(1861, 61, 1860)
(1865, 183, 1856)
(1865, 1833, 344)
(1873, 305, 1848)
(1877, 1485, 1148)
=========[(b0,b1)==(551, 562)][size==7]
(1885, 427, 1836)
(1885, 1003, 1596)
(1885, 1643, 924)
(1885, 1813, 516)
(1889, 1311, 1360)
(1901, 549, 1820)
(1913, 1785, 688)
=========[(b0,b1)==(562, 573)][size==8]
(1921, 671, 1800)
(1921, 1121, 1560)
(1933, 1595, 1092)
(1937, 1425, 1312)
(1937, 1935, 88)
(1945, 793, 1776)
(1945, 1927, 264)
(1949, 1749, 860)
=========[(b0,b1)==(573, 584)][size==6]
(1961, 1239, 1520)
(1961, 1911, 440)
(1973, 915, 1748)
(1985, 63, 1984)
(1985, 1887, 616)
(1993, 1705, 1032)
=========[(b0,b1)==(584, 595)][size==5]
(1997, 315, 1972)
(2005, 1037, 1716)
(2005, 1357, 1476)
(2017, 1855, 792)
(2029, 2021, 180)
=========[(b0,b1)==(595, 606)][size==6]
(2041, 1159, 1680)
(2041, 2009, 360)
(2045, 693, 1924)
(2045, 1653, 1204)
(2053, 1475, 1428)
(2069, 819, 1900)
=========[(b0,b1)==(606, 617)][size==4]
(2081, 1281, 1640)
(2089, 1961, 720)
(2105, 1593, 1376)
(2105, 1767, 1144)
=========[(b0,b1)==(617, 628)][size==8]
(2113, 65, 2112)
(2117, 195, 2108)
(2117, 2115, 92)
(2125, 1403, 1596)
(2125, 2107, 276)
(2129, 1071, 1840)
(2137, 455, 2088)
(2141, 2091, 460)
=========[(b0,b1)==(628, 639)][size==6]
(2153, 585, 2072)
(2161, 1711, 1320)
(2165, 1197, 1804)
(2165, 2067, 644)
(2173, 715, 2052)
(2173, 1525, 1548)
=========[(b0,b1)==(639, 650)][size==2]
(2197, 2035, 828)
(2213, 2205, 188)
=========[(b0,b1)==(650, 661)][size==10]
(2221, 1829, 1260)
(2225, 1647, 1496)
(2225, 2193, 376)
(2237, 1995, 1012)
(2245, 67, 2244)
(2245, 2173, 564)
(2249, 201, 2240)
(2249, 1449, 1720)
(2257, 335, 2232)
(2257, 1105, 1968)
=========[(b0,b1)==(661, 672)][size==6]
(2269, 469, 2220)
(2273, 2145, 752)
(2281, 1769, 1440)
(2285, 603, 2204)
(2285, 1947, 1196)
(2293, 1235, 1932)
=========[(b0,b1)==(672, 683)][size==7]
(2297, 1575, 1672)
(2305, 737, 2184)
(2305, 2303, 96)
(2309, 2109, 940)
(2329, 871, 2160)
(2329, 2279, 480)
(2333, 1365, 1892)
=========[(b0,b1)==(683, 694)][size==4]
(2341, 1891, 1380)
(2353, 2065, 1128)
(2353, 2255, 672)
(2357, 1005, 2132)
=========[(b0,b1)==(694, 705)][size==8]
(2377, 1495, 1848)
(2381, 69, 2380)
(2389, 1139, 2100)
(2393, 345, 2368)
(2405, 483, 2356)
(2405, 1827, 1564)
(2405, 2013, 1316)
(2405, 2397, 196)
=========[(b0,b1)==(705, 716)][size==5]
(2417, 2385, 392)
(2425, 1273, 2064)
(2425, 2183, 1056)
(2437, 2365, 588)
(2441, 759, 2320)
=========[(b0,b1)==(716, 727)][size==6]
(2465, 897, 2296)
(2465, 1407, 2024)
(2465, 1953, 1504)
(2465, 2337, 784)
(2473, 2135, 1248)
(2477, 1755, 1748)
=========[(b0,b1)==(727, 738)][size==5]
(2501, 2301, 980)
(2501, 2499, 100)
(2509, 1541, 1980)
(2509, 2491, 300)
(2521, 71, 2520)
=========[(b0,b1)==(738, 749)][size==8]
(2525, 213, 2516)
(2525, 1173, 2236)
(2533, 355, 2508)
(2533, 1885, 1692)
(2545, 497, 2496)
(2545, 2257, 1176)
(2549, 2451, 700)
(2557, 1675, 1932)
=========[(b0,b1)==(749, 760)][size==5]
(2561, 639, 2480)
(2561, 1311, 2200)
(2581, 781, 2460)
(2581, 2419, 900)
(2593, 2015, 1632)
=========[(b0,b1)==(760, 771)][size==6]
(2605, 923, 2436)
(2605, 2597, 204)
(2609, 1809, 1880)
(2617, 2585, 408)
(2621, 2379, 1100)
(2633, 1065, 2408)
=========[(b0,b1)==(771, 782)][size==7]
(2657, 2145, 1568)
(2665, 73, 2664)
(2665, 1207, 2376)
(2665, 1943, 1824)
(2665, 2537, 816)
(2669, 219, 2660)
(2669, 2331, 1300)
=========[(b0,b1)==(782, 793)][size==7]
(2677, 365, 2652)
(2689, 511, 2640)
(2693, 1725, 2068)
(2701, 1349, 2340)
(2701, 2501, 1020)
(2705, 657, 2624)
(2705, 2703, 104)
=========[(b0,b1)==(793, 804)][size==5]
(2713, 2695, 312)
(2725, 803, 2604)
(2725, 2077, 1764)
(2729, 2679, 520)
(2741, 1491, 2300)
=========[(b0,b1)==(804, 815)][size==3]
(2749, 949, 2580)
(2753, 2655, 728)
(2777, 1095, 2552)
=========[(b0,b1)==(815, 826)][size==8]
(2785, 1633, 2256)
(2785, 2623, 936)
(2789, 2211, 1700)
(2797, 2405, 1428)
(2801, 2001, 1960)
(2809, 1241, 2520)
(2813, 75, 2812)
(2813, 2805, 212)
=========[(b0,b1)==(826, 837)][size==7]
(2825, 2583, 1144)
(2825, 2793, 424)
(2833, 1775, 2208)
(2837, 525, 2788)
(2845, 1387, 2484)
(2845, 2773, 636)
(2857, 2345, 1632)
=========[(b0,b1)==(837, 848)][size==5]
(2861, 2139, 1900)
(2873, 825, 2752)
(2873, 2745, 848)
(2885, 1533, 2444)
(2885, 1917, 2156)
=========[(b0,b1)==(848, 859)][size==5]
(2897, 975, 2728)
(2909, 2709, 1060)
(2917, 2915, 108)
(2929, 1679, 2400)
(2929, 2479, 1560)
=========[(b0,b1)==(859, 870)][size==7]
(2941, 2059, 2100)
(2941, 2891, 540)
(2953, 2665, 1272)
(2957, 1275, 2668)
(2965, 77, 2964)
(2965, 2867, 756)
(2969, 231, 2960)
=========[(b0,b1)==(870, 881)][size==7]
(2977, 385, 2952)
(2977, 1825, 2352)
(2993, 1425, 2632)
(2993, 2415, 1768)
(3001, 2201, 2040)
(3005, 693, 2924)
(3005, 2613, 1484)
=========[(b0,b1)==(881, 892)][size==4]
(3029, 1971, 2300)
(3029, 3021, 220)
(3037, 2795, 1188)
(3041, 3009, 440)
=========[(b0,b1)==(892, 903)][size==6]
(3049, 1001, 2880)
(3061, 2989, 660)
(3065, 2343, 1976)
(3065, 2553, 1696)
(3077, 1155, 2852)
(3077, 1725, 2548)
=========[(b0,b1)==(903, 914)][size==5]
(3085, 2117, 2244)
(3085, 2747, 1404)
(3089, 2961, 880)
(3109, 1309, 2820)
(3121, 79, 3120)
=========[(b0,b1)==(914, 925)][size==8]
(3125, 237, 3116)
(3133, 395, 3108)
(3133, 2485, 1908)
(3137, 3135, 112)
(3145, 553, 3096)
(3145, 1463, 2784)
(3145, 2263, 2184)
(3145, 3127, 336)
=========[(b0,b1)==(925, 936)][size==4]
(3161, 711, 3080)
(3161, 3111, 560)
(3169, 2881, 1320)
(3181, 869, 3060)
=========[(b0,b1)==(936, 947)][size==8]
(3205, 1027, 3036)
(3205, 2627, 1836)
(3209, 2409, 2120)
(3217, 3055, 1008)
(3221, 2829, 1540)
(3229, 1771, 2700)
(3233, 1185, 3008)
(3233, 2175, 2392)
=========[(b0,b1)==(947, 958)][size==4]
(3253, 3245, 228)
(3257, 3015, 1232)
(3265, 1343, 2976)
(3265, 3233, 456)
=========[(b0,b1)==(958, 969)][size==9]
(3277, 1925, 2652)
(3277, 2555, 2052)
(3281, 81, 3280)
(3281, 2769, 1760)
(3293, 405, 3268)
(3293, 2325, 2332)
(3301, 1501, 2940)
(3305, 567, 3256)
(3305, 2967, 1456)
=========[(b0,b1)==(969, 980)][size==4]
(3313, 3185, 912)
(3329, 2079, 2600)
(3341, 891, 3220)
(3341, 1659, 2900)
=========[(b0,b1)==(980, 991)][size==8]
(3349, 2701, 1980)
(3349, 3149, 1140)
(3361, 2911, 1680)
(3365, 1053, 3196)
(3365, 3363, 116)
(3373, 3355, 348)
(3385, 1817, 2856)
(3385, 2233, 2544)
=========[(b0,b1)==(991, 1002)][size==2]
(3389, 3339, 580)
(3413, 3315, 812)
=========[(b0,b1)==(1002, 1013)][size==9]
(3425, 1377, 3136)
(3425, 2847, 1904)
(3433, 1975, 2808)
(3445, 83, 3444)
(3445, 2387, 2484)
(3445, 3053, 1596)
(3445, 3283, 1044)
(3449, 249, 3440)
(3457, 415, 3432)
=========[(b0,b1)==(1013, 1024)][size==8]
(3461, 1539, 3100)
(3469, 581, 3420)
(3485, 747, 3404)
(3485, 2133, 2756)
(3485, 3243, 1276)
(3485, 3477, 236)
(3497, 2775, 2128)
(3497, 3465, 472)
=========[(b0,b1)==(1024, 1035)][size==5]
(3505, 913, 3384)
(3505, 2993, 1824)
(3517, 3445, 708)
(3529, 1079, 3360)
(3533, 3195, 1508)
=========[(b0,b1)==(1035, 1047)][size==4]
(3541, 2291, 2700)
(3545, 1863, 3016)
(3545, 3417, 944)
(3557, 1245, 3332)
=========[(b0,b1)==(1047, 1059)][size==8]
(3581, 3381, 1180)
(3589, 1411, 3300)
(3589, 3139, 1740)
(3593, 2025, 2968)
(3601, 2449, 2640)
(3601, 3599, 120)
(3613, 85, 3612)
(3617, 255, 3608)
=========[(b0,b1)==(1059, 1071)][size==7]
(3625, 1577, 3264)
(3625, 3337, 1416)
(3637, 595, 3588)
(3649, 2849, 2280)
(3649, 3551, 840)
(3653, 765, 3572)
(3653, 3075, 1972)
=========[(b0,b1)==(1071, 1083)][size==5]
(3665, 1743, 3224)
(3665, 2607, 2576)
(3673, 935, 3552)
(3677, 3285, 1652)
(3697, 1105, 3528)
=========[(b0,b1)==(1083, 1095)][size==8]
(3701, 2349, 2860)
(3709, 1909, 3180)
(3721, 3479, 1320)
(3725, 3003, 2204)
(3725, 3717, 244)
(3733, 2765, 2508)
(3737, 3225, 1888)
(3737, 3705, 488)
=========[(b0,b1)==(1095, 1107)][size==4]
(3757, 2075, 3132)
(3757, 3685, 732)
(3761, 2511, 2800)
(3769, 3431, 1560)
=========[(b0,b1)==(1107, 1119)][size==9]
(3785, 87, 3784)
(3785, 3657, 976)
(3793, 1615, 3432)
(3797, 435, 3772)
(3805, 2923, 2436)
(3805, 3157, 2124)
(3809, 609, 3760)
(3809, 2241, 3080)
(3821, 3621, 1220)
=========[(b0,b1)==(1119, 1131)][size==4]
(3833, 1785, 3392)
(3845, 957, 3724)
(3845, 3843, 124)
(3853, 3835, 372)
=========[(b0,b1)==(1131, 1143)][size==9]
(3865, 2407, 3024)
(3865, 3577, 1464)
(3869, 1131, 3700)
(3869, 3819, 620)
(3877, 1955, 3348)
(3881, 3081, 2360)
(3889, 3311, 2040)
(3893, 2835, 2668)
(3893, 3795, 868)
=========[(b0,b1)==(1143, 1155)][size==4]
(3917, 3525, 1708)
(3925, 2573, 2964)
(3925, 3763, 1116)
(3929, 1479, 3640)
=========[(b0,b1)==(1155, 1167)][size==12]
(3961, 89, 3960)
(3961, 3239, 2280)
(3965, 267, 3956)
(3965, 1653, 3604)
(3965, 2997, 2596)
(3965, 3723, 1364)
(3973, 445, 3948)
(3973, 3965, 252)
(3977, 2295, 3248)
(3977, 3465, 1952)
(3985, 623, 3936)
(3985, 3953, 504)
=========[(b0,b1)==(1167, 1179)][size==4]
(3989, 2739, 2900)
(4001, 801, 3920)
(4013, 3675, 1612)
(4021, 979, 3900)
=========[(b0,b1)==(1179, 1191)][size==6]
(4033, 2465, 3192)
(4033, 3905, 1008)
(4045, 1157, 3876)
(4045, 3397, 2196)
(4049, 2001, 3520)
(4057, 2905, 2832)
=========[(b0,b1)==(1191, 1203)][size==8]
(4069, 3619, 1860)
(4069, 3869, 1260)
(4073, 1335, 3848)
(4093, 2635, 3132)
(4097, 2175, 3472)
(4097, 4095, 128)
(4105, 1513, 3816)
(4105, 4087, 384)
=========[(b0,b1)==(1203, 1215)][size==8]
(4121, 3321, 2440)
(4121, 4071, 640)
(4129, 3071, 2760)
(4133, 3555, 2108)
(4141, 91, 4140)
(4141, 1691, 3780)
(4145, 273, 4136)
(4145, 4047, 896)
=========[(b0,b1)==(1215, 1227)][size==5]
(4153, 455, 4128)
(4157, 2805, 3068)
(4177, 4015, 1152)
(4181, 819, 4100)
(4181, 1869, 3740)
=========[(b0,b1)==(1227, 1239)][size==7]
(4201, 1001, 4080)
(4205, 3237, 2684)
(4205, 3483, 2356)
(4217, 3975, 1408)
(4225, 2047, 3696)
(4225, 3713, 2016)
(4229, 4221, 260)
=========[(b0,b1)==(1239, 1251)][size==5]
(4241, 4209, 520)
(4253, 1365, 4028)
(4261, 4189, 780)
(4265, 2697, 3304)
(4265, 3927, 1664)
=========[(b0,b1)==(1251, 1263)][size==5]
(4273, 2225, 3648)
(4285, 1547, 3996)
(4285, 3403, 2604)
(4289, 4161, 1040)
(4297, 3145, 2928)
=========[(b0,b1)==(1263, 1275)][size==6]
(4321, 1729, 3960)
(4321, 3871, 1920)
(4325, 93, 4324)
(4325, 2403, 3596)
(4337, 465, 4312)
(4349, 651, 4300)
=========[(b0,b1)==(1275, 1287)][size==8]
(4357, 4355, 132)
(4369, 3569, 2520)
(4369, 4081, 1560)
(4373, 3315, 2852)
(4381, 2581, 3540)
(4381, 4331, 660)
(4385, 1023, 4264)
(4385, 3807, 2176)
=========[(b0,b1)==(1287, 1299)][size==5]
(4397, 3045, 3172)
(4405, 2093, 3876)
(4405, 4307, 924)
(4409, 1209, 4240)
(4421, 4029, 1820)
=========[(b0,b1)==(1299, 1311)][size==6]
(4441, 2759, 3480)
(4453, 2275, 3828)
(4453, 3485, 2772)
(4457, 3735, 2432)
(4469, 1581, 4180)
(4469, 3219, 3100)
=========[(b0,b1)==(1311, 1323)][size==8]
(4481, 3969, 2080)
(4493, 4485, 268)
(4505, 1767, 4144)
(4505, 2457, 3776)
(4505, 2937, 3416)
(4505, 4473, 536)
(4513, 95, 4512)
(4517, 285, 4508)
=========[(b0,b1)==(1323, 1335)][size==7]
(4525, 4187, 1716)
(4525, 4453, 804)
(4537, 665, 4488)
(4537, 3655, 2688)
(4549, 3901, 2340)
(4553, 855, 4472)
(4553, 4425, 1072)
=========[(b0,b1)==(1335, 1347)][size==6]
(4561, 2639, 3720)
(4573, 1045, 4452)
(4573, 3115, 3348)
(4589, 2139, 4060)
(4589, 4389, 1340)
(4597, 1235, 4428)
=========[(b0,b1)==(1347, 1359)][size==6]
(4621, 2821, 3660)
(4625, 3567, 2944)
(4625, 4623, 136)
(4633, 4345, 1608)
(4633, 4615, 408)
(4637, 2325, 4012)
=========[(b0,b1)==(1359, 1371)][size==5]
(4645, 3293, 3276)
(4645, 4067, 2244)
(4649, 4599, 680)
(4657, 1615, 4368)
(4673, 4575, 952)
=========[(b0,b1)==(1371, 1383)][size==9]
(4685, 3003, 3596)
(4685, 4293, 1876)
(4705, 97, 4704)
(4705, 4543, 1224)
(4709, 291, 4700)
(4709, 3741, 2860)
(4717, 485, 4692)
(4717, 3995, 2508)
(4721, 3471, 3200)
=========[(b0,b1)==(1383, 1395)][size==6]
(4729, 679, 4680)
(4733, 1995, 4292)
(4745, 873, 4664)
(4745, 2697, 3904)
(4745, 4233, 2144)
(4745, 4503, 1496)
=========[(b0,b1)==(1395, 1407)][size==7]
(4765, 1067, 4644)
(4765, 4757, 276)
(4777, 2185, 4248)
(4777, 4745, 552)
(4789, 1261, 4620)
(4793, 4455, 1768)
(4801, 3649, 3120)
=========[(b0,b1)==(1407, 1419)][size==4]
(4813, 4165, 2412)
(4817, 1455, 4592)
(4825, 3367, 3456)
(4825, 4697, 1104)
=========[(b0,b1)==(1419, 1431)][size==6]
(4849, 1649, 4560)
(4849, 4399, 2040)
(4861, 4661, 1380)
(4877, 2565, 4148)
(4885, 1843, 4524)
(4885, 3827, 3036)
=========[(b0,b1)==(1431, 1443)][size==7]
(4889, 4089, 2680)
(4901, 99, 4900)
(4901, 4899, 140)
(4909, 4891, 420)
(4913, 495, 4888)
(4925, 693, 4876)
(4925, 2037, 4484)
=========[(b0,b1)==(1443, 1455)][size==4]
(4933, 2755, 4092)
(4937, 3255, 3712)
(4957, 4565, 1932)
(4969, 2231, 4440)
=========[(b0,b1)==(1455, 1467)][size==7]
(4973, 4005, 2948)
(4981, 3731, 3300)
(4981, 4819, 1260)
(4985, 1287, 4816)
(4985, 4263, 2584)
(4993, 2945, 4032)
(5009, 3441, 3640)
=========[(b0,b1)==(1467, 1479)][size==5]
(5017, 2425, 4392)
(5017, 4505, 2208)
(5021, 4779, 1540)
(5045, 1683, 4756)
(5045, 5037, 284)
=========[(b0,b1)==(1479, 1491)][size==8]
(5057, 3135, 3968)
(5057, 5025, 568)
(5065, 3913, 3216)
(5065, 4183, 2856)
(5069, 2619, 4340)
(5069, 4731, 1820)
(5077, 5005, 852)
(5081, 1881, 4720)
=========[(b0,b1)==(1491, 1503)][size==6]
(5101, 101, 5100)
(5105, 303, 5096)
(5105, 4977, 1136)
(5113, 505, 5088)
(5125, 707, 5076)
(5125, 2813, 4284)
=========[(b0,b1)==(1503, 1515)][size==7]
(5141, 909, 5060)
(5141, 4941, 1420)
(5153, 4095, 3128)
(5161, 1111, 5040)
(5161, 4361, 2760)
(5165, 2277, 4636)
(5165, 3813, 3484)
=========[(b0,b1)==(1515, 1527)][size==9]
(5185, 1313, 5016)
(5185, 3007, 4224)
(5185, 4897, 1704)
(5185, 5183, 144)
(5189, 4611, 2380)
(5197, 3515, 3828)
(5209, 5159, 720)
(5213, 1515, 4988)
(5213, 2475, 4588)
=========[(b0,b1)==(1527, 1539)][size==6]
(5233, 5135, 1008)
(5237, 4845, 1988)
(5245, 1717, 4956)
(5245, 4277, 3036)
(5249, 3201, 4160)
(5249, 3999, 3400)
=========[(b0,b1)==(1539, 1551)][size==4]
(5261, 4539, 2660)
(5273, 3705, 3752)
(5281, 1919, 4920)
(5297, 4785, 2272)
=========[(b0,b1)==(1551, 1563)][size==9]
(5305, 103, 5304)
(5305, 5063, 1584)
(5309, 309, 5300)
(5317, 515, 5292)
(5317, 3395, 4092)
(5321, 2121, 4880)
(5321, 2871, 4480)
(5329, 721, 5280)
(5333, 5325, 292)
=========[(b0,b1)==(1563, 1575)][size==8]
(5345, 927, 5264)
(5345, 5313, 584)
(5353, 3895, 3672)
(5353, 5015, 1872)
(5365, 1133, 5244)
(5365, 2323, 4836)
(5365, 4717, 2556)
(5365, 5293, 876)
=========[(b0,b1)==(1575, 1587)][size==6]
(5381, 3069, 4420)
(5389, 1339, 5220)
(5389, 3589, 4020)
(5393, 5265, 1168)
(5413, 2525, 4788)
(5417, 1545, 5192)
=========[(b0,b1)==(1587, 1599)][size==5]
(5429, 4371, 3220)
(5429, 5229, 1460)
(5437, 4085, 3588)
(5441, 4641, 2840)
(5449, 1751, 5160)
=========[(b0,b1)==(1599, 1611)][size==8]
(5465, 2727, 4736)
(5465, 3783, 3944)
(5473, 4895, 2448)
(5473, 5185, 1752)
(5477, 5475, 148)
(5485, 1957, 5124)
(5485, 5467, 444)
(5501, 5451, 740)
=========[(b0,b1)==(1611, 1623)][size==7]
(5513, 105, 5512)
(5513, 3465, 4288)
(5521, 2929, 4680)
(5525, 2163, 5084)
(5525, 4557, 3124)
(5525, 5133, 2044)
(5525, 5427, 1036)
=========[(b0,b1)==(1623, 1635)][size==6]
(5545, 3977, 3864)
(5545, 4823, 2736)
(5557, 5395, 1332)
(5569, 2369, 5040)
(5573, 1155, 5452)
(5581, 3131, 4620)
=========[(b0,b1)==(1635, 1647)][size==6]
(5585, 3663, 4216)
(5585, 5073, 2336)
(5597, 1365, 5428)
(5597, 5355, 1628)
(5617, 2575, 4992)
(5617, 4465, 3408)
=========[(b0,b1)==(1647, 1659)][size==7]
(5629, 4171, 3780)
(5629, 5621, 300)
(5641, 5609, 600)
(5645, 3333, 4556)
(5645, 5307, 1924)
(5653, 5005, 2628)
(5657, 1785, 5368)
=========[(b0,b1)==(1659, 1671)][size==4]
(5669, 2781, 4940)
(5689, 5561, 1200)
(5693, 1995, 5332)
(5701, 5251, 2220)
=========[(b0,b1)==(1671, 1683)][size==9]
(5713, 3535, 4488)
(5713, 4655, 3312)
(5717, 4365, 3692)
(5725, 107, 5724)
(5725, 2987, 4884)
(5729, 321, 5720)
(5729, 4929, 2920)
(5737, 535, 5712)
(5741, 4059, 4060)
=========[(b0,b1)==(1683, 1695)][size==9]
(5749, 749, 5700)
(5765, 963, 5684)
(5765, 5187, 2516)
(5777, 2415, 5248)
(5777, 5775, 152)
(5785, 1177, 5664)
(5785, 3193, 4824)
(5785, 3737, 4416)
(5785, 5767, 456)
=========[(b0,b1)==(1695, 1707)][size==7]
(5801, 5751, 760)
(5809, 1391, 5640)
(5809, 4559, 3600)
(5813, 4845, 3212)
(5821, 5429, 2100)
(5825, 4257, 3976)
(5825, 5727, 1064)
=========[(b0,b1)==(1707, 1719)][size==6]
(5837, 1605, 5612)
(5837, 5115, 2812)
(5849, 3399, 4760)
(5857, 5695, 1368)
(5861, 3939, 4340)
(5869, 1819, 5580)
=========[(b0,b1)==(1719, 1731)][size==4]
(5881, 5369, 2400)
(5897, 5655, 1672)
(5905, 2033, 5544)
(5905, 4753, 3504)
=========[(b0,b1)==(1731, 1743)][size==10]
(5917, 3605, 4692)
(5917, 5035, 3108)
(5933, 3045, 5092)
(5933, 5925, 308)
(5941, 109, 5940)
(5941, 4141, 4260)
(5945, 327, 5936)
(5945, 2247, 5504)
(5945, 5607, 1976)
(5945, 5913, 616)
=========[(b0,b1)==(1743, 1755)][size==8]
(5953, 545, 5928)
(5965, 763, 5916)
(5965, 5893, 924)
(5981, 981, 5900)
(5989, 2461, 5460)
(5989, 3811, 4620)
(5993, 3255, 5032)
(5993, 5865, 1232)
=========[(b0,b1)==(1755, 1767)][size==7]
(6001, 1199, 5880)
(6001, 5551, 2280)
(6005, 4653, 3796)
(6005, 4947, 3404)
(6025, 1417, 5856)
(6025, 4343, 4176)
(6029, 5829, 1540)
=========[(b0,b1)==(1767, 1779)][size==5]
(6037, 2675, 5412)
(6053, 1635, 5828)
(6065, 4017, 4544)
(6065, 5487, 2584)
(6073, 5785, 1848)
=========[(b0,b1)==(1779, 1791)][size==7]
(6085, 1853, 5796)
(6085, 6083, 156)
(6089, 2889, 5360)
(6101, 4851, 3700)
(6109, 5141, 3300)
(6109, 6059, 780)
(6113, 4545, 4088)
=========[(b0,b1)==(1791, 1803)][size==4]
(6121, 2071, 5760)
(6133, 6035, 1092)
(6145, 3103, 5304)
(6145, 4223, 4464)
=========[(b0,b1)==(1803, 1815)][size==6]
(6161, 111, 6160)
(6161, 2289, 5720)
(6173, 555, 6148)
(6185, 777, 6136)
(6185, 5673, 2464)
(6197, 3885, 4828)
=========[(b0,b1)==(1815, 1827)][size==7]
(6205, 2507, 5676)
(6205, 3317, 5244)
(6205, 4747, 3996)
(6205, 5963, 1716)
(6217, 5335, 3192)
(6221, 1221, 6100)
(6229, 4429, 4380)
=========[(b0,b1)==(1827, 1839)][size==7]
(6245, 1443, 6076)
(6245, 6237, 316)
(6253, 2725, 5628)
(6253, 5605, 2772)
(6257, 6225, 632)
(6269, 3531, 5180)
(6277, 6205, 948)
===
]]]
[[[
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000000:iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_ +SML_vs_HOE +buggy_plus1__vs__layered  > /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.layered.HOE.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.layered.HOE.out.txt
diff /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.layered.HOE.out.txt   /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
    ok!
rm /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_.1000000.layered.HOE.out.txt
===
]]]

[[[
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_ +SML_vs_HOE
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000000:iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_ +SML_vs_HOE  > /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_.1000000.HOE.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_.1000000.HOE.out.txt
diff /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_.1000000.HOE.out.txt   /sdcard/0my_files/tmp/out4py/seed.math.GaussInteger..iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt.1000000.HOE.out.txt
    ok!
du -h /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_.1000000.HOE.out.txt
    26MB
rm /sdcard/0my_files/tmp/out4py/seed.math.right_angled_triangle_side_length..iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_.1000000.HOE.out.txt
===
]]]


[[[
iter_right_angled_triangle_side_length_triples_
def iter_right_angled_triangle_side_length_triples_(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse=2, /, *, SML_vs_HOE=True, may_max1_hypotenuse=None, turnoff__coprime=False):
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ =0
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ =1
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ =2
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ =3
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ -SML_vs_HOE
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ +SML_vs_HOE
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ --may_max1_hypotenuse=100
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ --may_max1_hypotenuse=98
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ --may_max1_hypotenuse=97
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ +turnoff__coprime
===
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ -uniform =0
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ -uniform =1
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ -uniform =2
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ -uniform =3

py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ +uniform =0
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ +uniform =1
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ +uniform =2
py_adhoc_call   seed.math.right_angled_triangle_side_length   ,1000:iter_right_angled_triangle_side_length_triples_ +uniform =3
===
]]]


#]]]'''
__all__ = r'''
Bad
    Bad___gcd_A_B__gt1
    Bad___A_lt1

iter_right_angled_triangle_side_length_difference_ratio__given_B_
    mk__min_sqrt__plus_A_B_or_half__and_step___care_odd_
        mk__min_sqrt__plus_A_B_or_half_
    mk__right_angled_triangle_side_length_difference_ratio_
        check_odd_pint
        check_ez4B
        mk____plus_A_B_
            mk____B_ex_
                mk____sqrt__odd4B_
                mk____ez4B_
                mk____odd4B_and_b_

mk__right_angled_triangle_side_length_ratio5difference_ratio_


iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
    layered_______iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
    buggy_plus1_______iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
        lowerbound4hypotenuse5lowerbound4B_
        max1__ceil_half_ez4B_
        max1__floor_half_sqrt__odd4B_
    iter_nums_Bs_ex__lt_
        num_Bs_ex__lt_
            num_Bs_lt__exact_and_rough_
            num_Bs_lt__exact_
            num_Bs_lt__rough_
        iter_nums_Bs_lt__zpow_
            num_Bs_lt__zpow_
_SML5LSM
_LSM5SML
_LSM5HOE
_HOE5LSM

iter_coprime_pints_to_
iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_
    mk__right_angled_triangle_side_length_ratio5s_t_



engine_selector4iter_right_angled_triangle_side_length_ratios_
    iter_right_angled_triangle_side_length_ratios__ver0__factorisation4hypotenuse_
    iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
    iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_
    iter_right_angled_triangle_side_length_ratios__ver3__GaussInteger_decompose4hypotenuse__arbitrary_order_

limit_hypotenuse4iter_right_angled_triangle_side_length_triples_
    hypotenuse5HOE_
    hypotenuse5SML_

iter_right_angled_triangle_side_length_triples5primitive_ratio_
    add_key4iter_right_angled_triangle_side_length_triples_
        key5HOE_
        key5SML_

iter_right_angled_triangle_side_length_triples_
    iter_right_angled_triangle_side_length_triples__
        engine_selector4iter_right_angled_triangle_side_length_ratios_
        iter_right_angled_triangle_side_length_triples5primitive_ratio_
        limit_hypotenuse4iter_right_angled_triangle_side_length_triples_

'''.split()#'''
__all__

from itertools import count as count_
from itertools import takewhile
from math import sqrt as sqrt_, log2 as log2_

from seed.math.gcd import gcd
from seed.math.gcd import gcd_ex

from seed.math.floor_ceil import ceil_log2 as ceil_log2_
from seed.math.floor_ceil import ceil_sqrt as ceil_sqrt_
from seed.math.floor_ceil import ceil_div as ceil_div_
#xxx from seed.math.floor_ceil import perfect_sqrt as perfect_sqrt_
from seed.math.floor_ceil import perfect_kth_root_
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny import fst
from seed.math.sign_of import sign_of
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
from seed.math.GaussInteger import iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt
#def iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt(may_max1_hypotenuse, /, *, SML_vs_HOE, to_sort, turnoff__coprime):
from seed.math.right_angled_triangle_infos__sorted_by import iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__
#def iter_right_angled_triangles_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, /, *, raw_output=False, may_ST4continue=None):
from seed.math.right_angled_triangle_infos__sorted_by import iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__
#def iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, output_fmt__or__output_formatter__or__SML_vs_HOE, /, *, may_ST4continue=None):


from seed.types.Heap import Heap, HeapWithKey
#class Heap(IHeap):
#    def __init__(self, iterable, *
#            , sorted=False, copy=False, are_heap_items=True
#            , obj2item=None, item2obj=None):
#class HeapWithKey(IHeap):
#    def __init__(self, obj2key, iterable, *
#            , sorted=False, copy=True, are_heap_items=False):











class Bad(Exception):pass
class Bad___gcd_A_B__gt1(Bad):pass
class Bad___A_lt1(Bad):pass

def check_odd_pint(u, /):
    check_int_ge(1, u)
    if not u&1 == 1: raise TypeError

def check_ez4B(ez4B, /):
    check_type_is(int, ez4B)
    if ez4B:
        check_odd_pint(ez4B)
def mk__min_sqrt__plus_A_B_or_half__and_step___care_odd_(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    '-> (min_sqrt__plus_A_B_or_half, step) # !!!result diff from mk__min_sqrt__plus_A_B_or_half_!!! 『|=1』if necessary'
    min_sqrt__plus_A_B_or_half = mk__min_sqrt__plus_A_B_or_half_(floor_half_sqrt__odd4B, ceil_half_ez4B)
    ez4B = max(0, ceil_half_ez4B*2-1)
    MUSTBE_odd4sqrt__plus_A_B = ez4B > 0
    if MUSTBE_odd4sqrt__plus_A_B:
        min_sqrt__plus_A_B_or_half |= 1
            #!!!updated!!!
        step = 2
        assert min_sqrt__plus_A_B_or_half&1 == 1
    else:
        step = 1
    return (min_sqrt__plus_A_B_or_half, step)
def mk____sqrt__odd4B_(floor_half_sqrt__odd4B, /):
    '-> sqrt__odd4B'
    check_int_ge(0, floor_half_sqrt__odd4B)
    sqrt__odd4B = 1 +2*floor_half_sqrt__odd4B
    #check_odd_pint(sqrt__odd4B)
    # [sqrt__odd4B %2 == 1]
    # [sqrt__odd4B >= 1]
    return sqrt__odd4B
def mk____ez4B_(ceil_half_ez4B, /):
    '-> ez4B'
    check_int_ge(0, ceil_half_ez4B)
    ez4B = max(0, ceil_half_ez4B*2-1)
    #check_ez4B(ez4B)
    # [ez4B >= 0]
    # [[ez4B == 0]or[ez4B %2 == 1]]
    return ez4B

def mk____odd4B_and_b_(sqrt__odd4B, ez4B, /):
    '-> (odd4B, b)'
    check_odd_pint(sqrt__odd4B)
    check_ez4B(ez4B)
    odd4B = sqrt__odd4B**2
    b = odd4B << ez4B
    # [odd4B >= 1]
    # [odd4B %2 == 1]
    # [odd4B == sqrt__odd4B**2]
    # [b == odd4B*2**ez4B]
    return (odd4B, b)

def mk____B_ex_(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    '-> (sqrt__odd4B, odd4B, ez4B, b)'
    sqrt__odd4B = mk____sqrt__odd4B_(floor_half_sqrt__odd4B)
    # [sqrt__odd4B >= 1]
    # [sqrt__odd4B %2 == 1]

    ez4B = mk____ez4B_(ceil_half_ez4B)
    # [ez4B >= 0]
    # [[ez4B == 0]or[ez4B %2 == 1]]
    (odd4B, b) = mk____odd4B_and_b_(sqrt__odd4B, ez4B)
    # [odd4B >= 1]
    # [odd4B %2 == 1]
    # [odd4B == sqrt__odd4B**2]
    # [b == odd4B*2**ez4B]
    return (sqrt__odd4B, odd4B, ez4B, b)
def mk____plus_A_B_(ez4B, sqrt__plus_A_B_or_half, /):
    '-> plus_A_B/(a+b)'
    check_int_ge(1, sqrt__plus_A_B_or_half)
    #min_sqrt__plus_A_B_or_half = mk__min_sqrt__plus_A_B_or_half_(floor_half_sqrt__odd4B, ceil_half_ez4B)
    #check_int_ge(min_sqrt__plus_A_B_or_half, sqrt__plus_A_B_or_half)

    # [a%2 == 1]
    # [(a+b)%2 =!= b%2]
    if ez4B:
        # [b%2 == 0]
        # [(a+b)%2 == 1]
        sqrt__plus_A_B = sqrt__plus_A_B_or_half
        check_odd_pint(sqrt__plus_A_B)
        plus_A_B = sqrt__plus_A_B**2
        # [(a+b) == sqrt__plus_A_B_or_half**2]
    else:
        # [b%2 == 1]
        # [(a+b)%2 == 0]
        sqrt__half_of_plus_A_B = sqrt__plus_A_B_or_half
        half_of_plus_A_B = sqrt__half_of_plus_A_B**2
        plus_A_B = 2*half_of_plus_A_B
        # [(a+b) == 2*sqrt__plus_A_B_or_half**2]
    plus_A_B
    #assert not plus_A_B&1 == b&1
    assert (plus_A_B&1 == 0) is (ez4B == 0)
    # [(a+b)%2 =!= b%2]
    # [(a+b) == 2**(ez4B==0) *sqrt__plus_A_B_or_half**2]
    return plus_A_B





def mk__min_sqrt__plus_A_B_or_half_(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    '-> min sqrt__plus_A_B_or_half'
    (sqrt__odd4B, odd4B, ez4B, b) = mk____B_ex_(floor_half_sqrt__odd4B, ceil_half_ez4B)
    # [sqrt__odd4B >= 1]
    # [sqrt__odd4B %2 == 1]
    # [odd4B >= 1]
    # [odd4B %2 == 1]
    # [odd4B == sqrt__odd4B**2]
    # [ez4B >= 0]
    # [[ez4B == 0]or[ez4B %2 == 1]]
    # [b == odd4B*2**ez4B]

    ######################
    if 0:
        min_sqrt__plus_A_B_or_half = ceil_sqrt_((sqrt__odd4B**2 * 2**ez4B + 1) >> (ez4B==0))
        min_sqrt__plus_A_B_or_half = ceil_sqrt_((sqrt__odd4B**2 * 2**ez4B + 1) >> 1) if (ez4B==0) else ceil_sqrt_((sqrt__odd4B**2 * 2**ez4B + 1))
        min_sqrt__plus_A_B_or_half = ceil_sqrt_((sqrt__odd4B**2 + 1) >> 1) if (ez4B==0) else ceil_sqrt_((sqrt__odd4B * 2**((ez4B-1)//2))**2 *2 + 1)
        min_sqrt__plus_A_B_or_half = ceil_div_(ceil_sqrt_((sqrt__odd4B**2 + 1) *2), 2) if (ez4B==0) else ceil_sqrt_((sqrt__odd4B * 2**((ez4B-1)//2))**2 *2)
        # [:condition4_WW1_eq_2VV~~[w**2+1==2*v**2]=>???]:goto
        #
        # !! [ceil_sqrt_(x**2 *2) is irrational]
        # [ceil_sqrt_(x**2 *2 +1) == ceil_sqrt_(x**2 *2)]
        # [ceil_sqrt_((sqrt__odd4B * 2**((ez4B-1)///2))**2 *2 +1) == ceil_sqrt_((sqrt__odd4B * 2**((ez4B-1)///2))**2 *2)]
        #   [sqrt__odd4B := 1][ceil_half_ez4B :<- [1..]] => [rhs == ceil_(sqrt_(2) *2**(ceil_half_ez4B-1))]
        #       #无法简化
        #
        # !! [ceil_sqrt_(x /2) == ceil_(sqrt_(x*2) /2) == ceil_(ceil_sqrt_(x*2) /2)]
        # [ceil_sqrt_((sqrt__odd4B**2 + 1) ///2) === ceil_(ceil_sqrt_((sqrt__odd4B**2 + 1) *2) /2)]
            # [ceil_sqrt_((1**2 + 1) ///2) == 1 == ceil_(ceil_sqrt_((1**2 + 1) *2) /2)]
            # [ceil_sqrt_((3**2 + 1) ///2) == 3 == ceil_(ceil_sqrt_((3**2 + 1) *2) /2)]
            # [ceil_sqrt_((5**2 + 1) ///2) == 4 == ceil_(ceil_sqrt_((5**2 + 1) *2) /2)]
        return min_sqrt__plus_A_B_or_half
    ######################
    # [a%2 == 1]
    min_a = 1
    min_plus_A_B = min_a + b
    if ez4B:
        # [b%2 == 0]
        # [min_plus_A_B%2 == 1]
        min_plus_A_B_or_half = min_plus_A_B
    else:
        # [b%2 == 1]
        # [min_plus_A_B%2 == 0]
        min_plus_A_B_or_half = min_plus_A_B >>1
    min_sqrt__plus_A_B_or_half = ceil_sqrt_(min_plus_A_B_or_half)
    return min_sqrt__plus_A_B_or_half

def _std_with_xxx_(with_side_length_ratio, with_params, /):
    with_params = bool(with_params)
    if with_params:
        with_side_length_ratio = True
    with_side_length_ratio = bool(with_side_length_ratio)
    return (with_side_length_ratio, with_params)
def iter_right_angled_triangle_side_length_difference_ratio__given_B_(floor_half_sqrt__odd4B, ceil_half_ez4B, /, *, with_side_length_ratio=False, with_params=False):
    '-> iter result_ex/(if not with_side_length_ratio then (a,b) elif not with_params then ((a,b), side_length_ratio) else ((a,b), side_length_ratio, params)) #side_length_ratio/(short_side, middle_side, long_side) #params/(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half)'
    (with_side_length_ratio, with_params) = _std_with_xxx_(with_side_length_ratio, with_params)

    (min_sqrt__plus_A_B_or_half, step) = mk__min_sqrt__plus_A_B_or_half__and_step___care_odd_(floor_half_sqrt__odd4B, ceil_half_ez4B)
    for sqrt__plus_A_B_or_half in count_(min_sqrt__plus_A_B_or_half, step):
        try:
            (a, b) = mk__right_angled_triangle_side_length_difference_ratio_(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half)
            # [[gcd(a,b) == 1][sqrt_(2*(a+b)*b) %1 == 0][a%2 == 1][a >= 1][b >= 1]]
        except Bad___gcd_A_B__gt1:
            continue
            pass

        (a,b)
        result_ex = _mk_result_ex5A_B_(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half, a, b, with_side_length_ratio=with_side_length_ratio, with_params=with_params)
        yield result_ex
def _mk_result_ex5A_B_(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half, a, b, /, *, with_side_length_ratio, with_params):
    '-> (a,b) | ((a,b), side_length_ratio) | ((a,b), side_length_ratio, params)'
    # [[gcd(a,b) == 1][sqrt_(2*(a+b)*b) %1 == 0][a%2 == 1][a >= 1][b >= 1]]
    #(with_side_length_ratio, with_params) = _std_with_xxx_(with_side_length_ratio, with_params)

    if not with_side_length_ratio:
        return (a,b)
    else:
        (short_side, middle_side, long_side) = SML = side_length_ratio = mk__right_angled_triangle_side_length_ratio5difference_ratio_(a,b)
        # [(b/a) == (long_side-middle_side)/(middle_side-short_side)]
        # [short_side**2 +middle_side**2 == long_side**2]
        # [0 < short_side < middle_side < long_side]
        # [are_pairwise_coprime_([short_side, middle_side, long_side])]
        if not with_params:
            return ((a,b), side_length_ratio)
        else:
            params = (floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half)
            return ((a,b), side_length_ratio, params)


def mk__right_angled_triangle_side_length_difference_ratio_(floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half, /):
    '-> right_angled_triangle_side_length_difference_ratio/(a,b) #[b/a =[def]= (斜边-中边)/(中边-短边)] #[[gcd(a,b) == 1][sqrt_(2*(a+b)*b) %1 == 0][a%2 == 1][a >= 1][b >= 1]]'
    (sqrt__odd4B, odd4B, ez4B, b) = mk____B_ex_(floor_half_sqrt__odd4B, ceil_half_ez4B)
    # [sqrt__odd4B >= 1]
    # [sqrt__odd4B %2 == 1]
    # [odd4B >= 1]
    # [odd4B %2 == 1]
    # [odd4B == sqrt__odd4B**2]
    # [ez4B >= 0]
    # [[ez4B == 0]or[ez4B %2 == 1]]
    # [b == odd4B*2**ez4B]

    ######################
    plus_A_B = mk____plus_A_B_(ez4B, sqrt__plus_A_B_or_half)
    # [(a+b)%2 =!= b%2]
    # [(a+b) == 2**(ez4B==0) *sqrt__plus_A_B_or_half**2]

    ######################
    # [(2*(a+b)*b) == (2 * 2**(ez4B==0) *sqrt__plus_A_B_or_half**2 * odd4B*2**ez4B)]
    # [(2*(a+b)*b) == (2**(1+ez4B+(ez4B==0)) *(sqrt__plus_A_B_or_half*sqrt__odd4B)**2)]
    # !! [[ez4B == 0]or[ez4B %2 == 1]]
    # [(1+ez4B+(ez4B==0)) %2 == 0]
    # [(2*(a+b)*b) == (2**((1+ez4B+(ez4B==0))///2) *sqrt__plus_A_B_or_half*sqrt__odd4B)**2]
    # [sqrt_(2*(a+b)*b) == (2**((1+ez4B+(ez4B==0))///2) *sqrt__plus_A_B_or_half*sqrt__odd4B)]
    # [sqrt_(2*(a+b)*b) %1 == 0]

    ######################
    a = plus_A_B -b
    # [a%2 == 1]
    # [a >= 1]
    if not a >= 1: raise Bad___A_lt1
    #check_int_ge(1, a)
    assert a&1 == 1
    check_odd_pint(a)

    ######################
    if not gcd(a,odd4B) == 1: raise Bad___gcd_A_B__gt1
    #if not gcd(a,b) == 1: raise Bad___gcd_A_B__gt1
    # [gcd(a,odd4B) == 1]
    # !! [a%2 == 1]
    # !! [b == odd4B*2**ez4B]
    # [gcd(a,b) == 1]

    ######################
    # [b >= 1]
    # [a >= 1]
    # [a%2 == 1]
    # [gcd(a,b) == 1]
    # [sqrt_(2*(a+b)*b) %1 == 0]
    return (a, b)

def mk__right_angled_triangle_side_length_ratio5difference_ratio_(a, b, /):
    '-> side_length_ratio/(short_side, middle_side, long_side) # [[(b/a) == (long_side-middle_side)/(middle_side-short_side)][short_side**2 +middle_side**2 == long_side**2][0 < short_side < middle_side < long_side][are_pairwise_coprime_([short_side, middle_side, long_side])]]'
    ######################precondition:
    # [b >= 1]
    # [a >= 1]
    # [a%2 == 1]
    # [gcd(a,b) == 1]
    # [sqrt_(2*(a+b)*b) %1 == 0]
    check_odd_pint(a)
    check_int_ge(1, b)
    assert gcd(a, b) == 1
    ######################
    # [x/y == ((a+b) + sqrt_(2*(a+b)*b))]
    ######################
    plus_A_B = a+b
    mul_2B_plus_A_B = 2*b*plus_A_B
    #sqrt__mul_2B_plus_A_B = perfect_sqrt_(mul_2B_plus_A_B)
    sqrt__mul_2B_plus_A_B = perfect_kth_root_(2, mul_2B_plus_A_B)
        # !! [sqrt_(2*(a+b)*b) %1 == 0]
    #assert (plus_A_B > sqrt__mul_2B_plus_A_B) is (a > b)
    assert (b < sqrt__mul_2B_plus_A_B)
    div_x_y = plus_A_B +sqrt__mul_2B_plus_A_B
        #[short_side > 0] ==>> [x/y - a > 0]
        #[short_side > 0] ==>> [exclude [div_x_y == plus_A_B -sqrt__mul_2B_plus_A_B]]

    y = 1
    x = div_x_y
    short_side = x-a*y
    middle_side = x
    long_side = x+b*y
    ######################
    # [x/y == ((a+b) - sqrt_(2*(a+b)*b))]:
    #   [x/y -a == (b - sqrt_(2*(a+b)*b)) < 0]
    #   [x/y -a < 0]
    #   [short_side == x-a*y < 0]
    ######################
    # !! [x/y == ((a+b) + sqrt_(2*(a+b)*b))]
    # [x/y -a == (b + sqrt_(2*(a+b)*b)) > 0]
    # [x/y -a > 0]
    # [short_side == x-a*y > 0]
    # [0 < x-a*y < x < x+b*y]
    # [0 < short_side < middle_side < long_side]
    ######################
    # [middle_side**2 == x**2 == div_x_y**2 == ((a+b) + sqrt_(2*(a+b)*b))**2 == (a+b)**2 +(2*(a+b)*b) +2*((a+b) * sqrt_(2*(a+b)*b)) == (a+b)* ((a+b) +2*b +2*sqrt_(2*(a+b)*b))]
    # [long_side**2 -short_side**2 == (b+a)*y * (2*x +(b-a)*y) == (b+a) * (2*div_x_y +(b-a)) == (b+a) * (2*((a+b) + sqrt_(2*(a+b)*b)) +(b-a)) == (b+a) * (a+3*b + 2*sqrt_(2*(a+b)*b)) == middle_side**2]
    # [long_side**2 -short_side**2 == middle_side**2]
    # [short_side**2 +middle_side**2 == long_side**2]
    ######################
    # !! [x/y == ((a+b) + sqrt_(2*(a+b)*b))]
    # [gcd(short_side, middle_side) == gcd(x-a*y,x) == gcd(a*y,x) == gcd(a*1,div_x_y) == gcd(a,((a+b) + sqrt_(2*(a+b)*b))) == gcd(a,(b + sqrt_(2*(a+b)*b)))]
    # !! [gcd(a,b) == 1]
    # [gcd(a,(b + sqrt_(2*(a+b)*b))*(b - sqrt_(2*(a+b)*b))) == gcd(a,(b**2 - (2*(a+b)*b))) == gcd(a,b*(2*a+b)) == 1]
    # [0 < gcd(a,(b + sqrt_(2*(a+b)*b))) <= gcd(a,(b + sqrt_(2*(a+b)*b))*(b - sqrt_(2*(a+b)*b))) == 1]
    # [gcd(a,(b + sqrt_(2*(a+b)*b))) == 1]
    # [gcd(short_side, middle_side) == 1]
    ######################
    # !! [gcd(short_side, middle_side) == 1]
    # [gcd(short_side**2, middle_side**2) == 1]
    # !! [short_side**2 +middle_side**2 == long_side**2]
    # [gcd(short_side**2, long_side**2) == gcd(short_side**2, short_side**2 + middle_side**2) == 1]
    # [gcd(long_side**2, middle_side**2) == gcd(short_side**2 +middle_side**2, middle_side**2) == 1]
    # [are_pairwise_coprime_([short_side, middle_side, long_side])]
    ######################

    assert 0 < short_side < middle_side < long_side, (short_side, middle_side, long_side)
    assert short_side**2 +middle_side**2 == long_side**2
    assert gcd(short_side, middle_side) == 1
    ######################postcondition:
    # [(b/a) == (long_side-middle_side)/(middle_side-short_side)]
    # [short_side**2 +middle_side**2 == long_side**2]
    # [0 < short_side < middle_side < long_side]
    # [are_pairwise_coprime_([short_side, middle_side, long_side])]
    return (short_side, middle_side, long_side)


def _key5result_ex_(result_ex, /, *, SML_vs_HOE):
    ab, side_length_ratio, params = result_ex
    #xxx:key = side_length_ratio[::-1]
    SML = side_length_ratio
    return _key5SML(SML, SML_vs_HOE=SML_vs_HOE)
def _key5SML(SML, /, *, SML_vs_HOE):
    #see:key5SML_
    #see:_key5SML
    LSM = _LSM5SML(SML)
    if SML_vs_HOE is False:
        #SML
        key = LSM
    elif SML_vs_HOE is True:
        #HOE
        HOE = _HOE5LSM(LSM)
        key = HOE
    else:
        raise 000
    key
    return key
def _LSM5SML(SML, /):
    #see:_SML5LSM
    #see:_LSM5SML
    (short_side, middle_side, long_side) = side_length_ratio = SML
    LSM = (long_side, short_side, middle_side)
    return LSM
def _SML5LSM(LSM, /):
    #see:_LSM5SML
    #see:_SML5LSM
    (long_side, short_side, middle_side) = LSM
    side_length_ratio = SML = (short_side, middle_side, long_side)
    return SML
def _HOE5LSM(LSM, /):
    #see:_LSM5HOE
    #see:_HOE5LSM
    (long_side, short_side, middle_side) = LSM
    hypotenuse_side = long_side
    if short_side&1 == 1:
        odd_side = short_side
        even_side = middle_side
    else:
        odd_side = middle_side
        even_side = short_side
    HOE = (hypotenuse_side, odd_side, even_side)
    return HOE
def _hypotenuse_side5heap_item_(heap_item, /):
    (key, on_start, result_ex, it) = heap_item
    return _hypotenuse_side5result_ex_(result_ex)
def _mk_heap_item_(floor_half_sqrt__odd4B, ceil_half_ez4B, /, *, SML_vs_HOE):
    it = iter_right_angled_triangle_side_length_difference_ratio__given_B_(floor_half_sqrt__odd4B, ceil_half_ez4B, with_side_length_ratio=True, with_params=True)
    heap_item = _mk_heap_item__continued_(it, on_start=True, SML_vs_HOE=SML_vs_HOE)
    return heap_item
def _mk_heap_item__continued_(it, /, *, on_start, SML_vs_HOE):
    for result_ex in it:
        break
    else:
        raise 000
    key = _key5result_ex_(result_ex, SML_vs_HOE=SML_vs_HOE)
    heap_item = (key, on_start, result_ex, it)
    return heap_item
def _b5heap_item_(heap_item, /):
    (key, on_start, result_ex, it) = heap_item
    ab, side_length_ratio, params = result_ex
    (a, b) = ab
    return b

def _mk_extended_output_(key, side_length_ratio, result_ex_XXX, /, *, SML_vs_HOE, extended_output):
    if SML_vs_HOE is False:
        LSM = key
        SML = side_length_ratio
        #yield side_length_ratio
        r = side_length_ratio
    elif SML_vs_HOE is True:
        HOE = key
        #yield HOE
        r = HOE
    else:
        raise 000
    r
    if not extended_output:
        ex_r = r
    else:
        ex_r = r, result_ex_XXX
    ex_r
    return ex_r
#def iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_(*, buggy_plus1__vs__layered, extended_output=False, SML_vs_HOE=False, **kwds):
def iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_(*, SML_vs_HOE, extended_output=False, buggy_plus1__vs__layered=True, **kwds):
    #see:engine_selector4iter_right_angled_triangle_side_length_ratios_
    r'''[[[
[[
bug fixed by [buggy_plus1__vs__layered := True]
===
buggy:logic-err:[not$ min_hypotenuse_is_monotone_nondecreasing_with_respect_to___floor_half_sqrt__odd4B___ceil_half_ez4B]
    # [:try_to_find_counterexample_in_src_code]:goto
        false: [(+0,+0) <= (+1,+0)]
        counterexample: see:_try_to_find_counterexample_in_src_code__between____
===
change logic of iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_:
from:
    [(+0,+0) <= (+1,+0)]
    [(+0,+0) <= (+0,+1)]
to:
    [hypotenuse(floor_half_sqrt__odd4B >= ???vf, ceil_half_ez4B >= ???vc) >= ???vh]
    list all hypotenuse(floor_half_sqrt__odd4B < ???vf, ceil_half_ez4B < ???vc) and output all [hypotenuse < ???vh], ..., layer by layer for diff ???vh boundary
# [:layered_hypotenuse_generation_via_lowerbound4hypotenuse5lowerbound4B_]:goto
===
DONE
]]
    ######################
    #output fmt:
    * [SML_vs_HOE is False]:
        output Iter<(S, M, L)> but sorted by key (L, S, M)/(long,short,middle)
    * [SML_vs_HOE is True]:
        output Iter<(hypotenuse,odd,even)> sorted by key echo
    ######################
    #]]]'''#'''
    check_type_is(bool, buggy_plus1__vs__layered)
    if buggy_plus1__vs__layered is False:
        f = buggy_plus1_______iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
    elif buggy_plus1__vs__layered is True:
        f = layered_______iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
    else:
        raise 000
    return f(extended_output=extended_output, SML_vs_HOE=SML_vs_HOE, **kwds)
    return
    if not buggy_plus1__vs__layered is False: raise NotImplementedError('layered [hypotenuse(a,b) < lowerbound4hypotenuse5lowerbound4B_(b0)]')
        # [:layered_hypotenuse_generation_via_lowerbound4hypotenuse5lowerbound4B_]:goto
def layered_______iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_(*, extended_output, SML_vs_HOE, _to_show_layer_line=False):
    #mk_exc_ = lambda:BaseException(f'found counterexample: result_ex: side_length_ratio={side_length_ratio}; ab={ab}; params={params};')
    hp = HeapWithKey(fst, [])
    #ls = hp.the_heap

    #b0, b1 = 1, 2
    b0, b1 = 0, 1
    while 1:
        b0 = b1
        #bug:b1 += ceil_log2_(b1)
        #   [ceil_log2_(1) == 0]
        b1 += 1+ceil_log2_(b1)
            # !! [:ratio_of_num_yields_to_num_pushes_per_layer_is_divergent______layered_hypotenuse_generation]:goto
            # ==>> [(b1-b0) as small as possible]
            # see:_iter_basic_params__bound_by_b0_b1_:『for ceil_half_ez4B in range(max1__ceil_half_ez4b1):』==>> 『b1 += 1+ceil_log2_(b1)』
            #

        for (floor_half_sqrt__odd4B, ceil_half_ez4B) in _iter_basic_params__bound_by_b0_b1_(b0, b1):
            #if 0b001:print(f'(floor_half_sqrt__odd4B, ceil_half_ez4B)={(floor_half_sqrt__odd4B, ceil_half_ez4B)}')
            heap_item = _mk_heap_item_(floor_half_sqrt__odd4B, ceil_half_ez4B, SML_vs_HOE=SML_vs_HOE)
            hp.push(heap_item)
        #assert ls

        low_h0 = lowerbound4hypotenuse5lowerbound4B_(b0)
        low_h1 = lowerbound4hypotenuse5lowerbound4B_(b1)
        layer4output = []
        #while (hypotenuse_side := _hypotenuse_side5heap_item_(ls[0])) < low_h1:
        while (hypotenuse_side := _hypotenuse_side5heap_item_(hp.peek())) < low_h1:
            assert low_h0 <= hypotenuse_side < low_h1
            eqvs = hp.pop_eqvs()
            assert len(eqvs) == 1
            [heap_item] = eqvs
            #
            (key, on_start, result_ex, it) = heap_item
            #if 0b001:print(f'key={key}')
            heap_item4next_A = _mk_heap_item__continued_(it, on_start=False, SML_vs_HOE=SML_vs_HOE)
                # (a,b) --> (next_a, b)
            hp.push(heap_item4next_A)
            #
            layer4output.append(heap_item)
        if _to_show_layer_line:
            layer_line = f'=========[(b0,b1)=={(b0,b1)}][size=={len(layer4output)}]'
            print(layer_line)
            #yield layer_line
        layer4output.sort()
        for heap_item in layer4output:
            (key, on_start, result_ex, it) = heap_item
            ab, side_length_ratio, params = result_ex
            (floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half) = params
            yield _mk_extended_output_(key, side_length_ratio, result_ex, SML_vs_HOE=SML_vs_HOE, extended_output=extended_output)
        #yield from layer4output
    #end-while 1
    raise 000



def lowerbound4hypotenuse5lowerbound4B_(b, /):
    # [lowerbound4hypotenuse5lowerbound4B_(b) =[def]= (1+2*b) + 2*ceil_sqrt_(b*(1+b) ///2)]
    return (1+2*b) + 2*ceil_sqrt_(b*(1+b) //2)
def max1__ceil_half_ez4B_(b0, /):
    return ceil_div_(ceil_log2_(b0)+1,2) if b0 >= 2 else 0
def max1__floor_half_sqrt__odd4B_(b0, ez4B, /):
    return ceil_div_(ceil_sqrt_(ceil_div_(b0,2**ez4B))-1,2)
def _iter_basic_params__bound_by_b0_b1_(b0, b1, /):
    ######################
    # [all_As___B_eq_(b) =[def]= {a | [[a :<- [1,3..]][gcd(a,b) == 1][a%2 == 1][(a+b)%2=!=b%2][sqrt__plus_A_B_or_half := sqrt_((a+b) >> (b%2==1))][sqrt__plus_A_B_or_half %1 == 0]]}]
    # [all_Bs_lt_(b0) =[def]= {b | [[floor_half_sqrt__odd4B :<- [0..]][ceil_half_ez4B :<- [0..]][odd4B := (floor_half_sqrt__odd4B*2+1)**2][ez4B := max(0, ceil_half_ez4B*2-1)][b := odd4B * 2**ez4B][b < b0]]}]
    # [num_Bs_lt_(b0) == len{(floor_half_sqrt__odd4B,ceil_half_ez4B) | [[b0 >= 2][ceil_half_ez4B :<- [0..<ceil_div_(ceil_log2_(b0)+1,2)]][ez4B := max(0, ceil_half_ez4B*2-1)][floor_half_sqrt__odd4B :<- [0..<ceil_div_(ceil_sqrt_(ceil_div_(b0,2**ez4B))-1,2)]]]}]
        # ==>> max1__ceil_half_ez4B_()
        # ==>> max1__floor_half_sqrt__odd4B_()
    ######################
    max1__ceil_half_ez4b0 = max1__ceil_half_ez4B_(b0)
    max1__ceil_half_ez4b1 = max1__ceil_half_ez4B_(b1)
    #if 0b001:print(f'max1__ceil_half_ez4b0={max1__ceil_half_ez4b0}')
    #if 0b001:print(f'max1__ceil_half_ez4b1={max1__ceil_half_ez4b1}')
    for ceil_half_ez4B in range(max1__ceil_half_ez4b1):
        # 『for ceil_half_ez4B in range(max1__ceil_half_ez4b1):』==>> 『b1 += 1+ceil_log2_(b1)』
        ez4B = max(0, ceil_half_ez4B*2-1)
        max1__floor_half_sqrt__odd4b0 = max1__floor_half_sqrt__odd4B_(b0, ez4B) if ceil_half_ez4B < max1__ceil_half_ez4b0 else 0
        max1__floor_half_sqrt__odd4b1 = max1__floor_half_sqrt__odd4B_(b1, ez4B)
        #if 0b001:print(f'max1__floor_half_sqrt__odd4b0={max1__floor_half_sqrt__odd4b0}')
        #if 0b001:print(f'max1__floor_half_sqrt__odd4b1={max1__floor_half_sqrt__odd4b1}')
        for floor_half_sqrt__odd4B in range(max1__floor_half_sqrt__odd4b0, max1__floor_half_sqrt__odd4b1):
            #basic_params = (floor_half_sqrt__odd4B, ceil_half_ez4B)
            yield (floor_half_sqrt__odd4B, ceil_half_ez4B)


def buggy_plus1_______iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_(*, extended_output, SML_vs_HOE):
    floor_half_sqrt__odd4B = 0
    ceil_half_ez4B = 0
    heap_item0 = _mk_heap_item_(floor_half_sqrt__odd4B, ceil_half_ez4B, SML_vs_HOE=SML_vs_HOE)
    hp = HeapWithKey(fst, [heap_item0])
    mk_exc_ = lambda:BaseException(f'found counterexample: result_ex: side_length_ratio={side_length_ratio}; ab={ab}; params={params};')
    while 1:
        # bug: heap_item = hp.pop()
        #   since each dst_vtx there are two src_vtx, i.e. duplicated
        #       (floor_half_sqrt__odd4B, ceil_half_ez4B) --> {(floor_half_sqrt__odd4B+1, ceil_half_ez4B),(floor_half_sqrt__odd4B, ceil_half_ez4B+1)} --> (floor_half_sqrt__odd4B+1, ceil_half_ez4B+1)
        # view ../../python3_src/seed/types/frontier.py
        # view ../../python3_src/seed/math/generate_partition4additive_semigroup__total_ordering__increasing.py
        # view ../../python3_src/seed/types/Heap.py
        #
        eqvs = hp.pop_eqvs()
        heap_item = eqvs[0]
        assert 1 <= len(eqvs) <= 2
        #
        (key, on_start, result_ex, it) = heap_item
        assert all(result_ex == _result_ex for (key, on_start, _result_ex, it) in eqvs)

        ab, side_length_ratio, params = result_ex
        #bug:assert not any(on_start for (key, on_start, result_ex, it) in eqvs) or len(eqvs) == 1, eqvs
        (floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half) = params
        assert (len(eqvs) == 1) is (not on_start or not (floor_half_sqrt__odd4B > 0 and ceil_half_ez4B > 0)), eqvs
        assert (len(eqvs) == 2) is (all(on_start for (key, on_start, _result_ex, it) in eqvs) and (floor_half_sqrt__odd4B > 0 and ceil_half_ez4B > 0)), eqvs
        yield _mk_extended_output_(key, side_length_ratio, result_ex, SML_vs_HOE=SML_vs_HOE, extended_output=extended_output)

        heap_item4next_A = _mk_heap_item__continued_(it, on_start=False, SML_vs_HOE=SML_vs_HOE)
        hp.push(heap_item4next_A)
        if not on_start:
            continue

        (a, b) = ab
        (short_side, middle_side, long_side) = side_length_ratio
        (floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half) = params
        ######################
        news = [_mk_heap_item_(floor_half_sqrt__odd4B+1, ceil_half_ez4B, SML_vs_HOE=SML_vs_HOE)
            ,_mk_heap_item_(floor_half_sqrt__odd4B, ceil_half_ez4B+1, SML_vs_HOE=SML_vs_HOE)
            ]
        ######################
        # [:try_to_find_counterexample_in_src_code]:here
        if not heap_item < news[0]: raise mk_exc_()
        if not heap_item < news[1]: raise mk_exc_()
        #if not news[0] < news[1]: raise BaseException(f'found counterexample: side_length_ratio={side_length_ratio}; ab={ab}; params={params};')
            # BaseException: found counterexample: side_length_ratio=(3, 4, 5); ab=(1, 1); params=(0, 0, 1);
        b0 = _b5heap_item_(news[0])
        b1 = _b5heap_item_(news[1])
        if b0 == b1: raise mk_exc_()
        if not (b0 < b1) is (floor_half_sqrt__odd4B > (ceil_half_ez4B==0)): raise mk_exc_()
        if not news[0] < news[1] and floor_half_sqrt__odd4B > (ceil_half_ez4B==0): raise mk_exc_()
        ######################
        for heap_item in news:
            try:
                hp.push(heap_item)
            except TypeError:
                # TypeError: '<' not supported between instances of 'generator' and 'generator'
                print(hp.the_heap)
                    # [((73, 48, 55), True, ((7, 18), (48, 55, 73), (1, 1, 5)), <generator>), ...]
                print(heap_item)
                    # ((73, 48, 55), True, ((7, 18), (48, 55, 73), (1, 1, 5)), <generator>)
                raise

    raise 000

def _LSM5HOE(HOE, /):
    #see:_HOE5LSM
    #see:_LSM5HOE
    (hypotenuse_side, odd_side, even_side) = HOE
    LSM = (long_side, short_side, middle_side) = (hypotenuse_side, *sorted([odd_side, even_side]))
    return LSM
def _check_LSM(LSM, /):
    (long_side, short_side, middle_side) = LSM
    assert long_side&1 == 1
    assert not short_side&1 == middle_side&1
    assert 3 <= short_side < middle_side < long_side
    assert long_side**2 == short_side**2 +middle_side**2
    assert gcd(short_side, middle_side) == 1
def _check_HOE(HOE, /):
    (hypotenuse_side, odd_side, even_side) = HOE
    assert hypotenuse_side&1 == 1
    assert odd_side&1 == 1
    assert even_side&1 == 0
    assert min(hypotenuse_side, odd_side, even_side) >= 3
    assert hypotenuse_side**2 == odd_side**2 +even_side**2
    assert gcd(odd_side, even_side) == 1
def _LSM2basic_params_ex(LSM, /):
    (long_side, short_side, middle_side) = LSM
    x = middle_side
    a_y = middle_side -short_side
    b_y = long_side -middle_side
    a, y, b = gcd_ex(a_y, b_y)
    assert y == 1
    assert a_y == a
    assert b_y == b
    ez4B, odd4B = factor_pint_out_power_of_base_(2, b)
    assert ez4B == 0 or ez4B&1 == 1
    sqrt__odd4B = perfect_kth_root_(2, odd4B)
    floor_half_sqrt__odd4B = sqrt__odd4B//2
    #bug:ceil_half_ez4B = ceil_div_(2, ez4B)
    ceil_half_ez4B = ceil_div_(ez4B, 2)
    basic_params = (floor_half_sqrt__odd4B, ceil_half_ez4B)
    ab = (a, b)
    side_length_ratio = SML = _SML5LSM(LSM)
    basic_params_ex = (basic_params, (ab, side_length_ratio))
    return basic_params_ex
def _iter_basic_paramss__len_hypotenuse_lt(max1_len_hypotenuse, /):
    it = iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt(max1_len_hypotenuse)
    for HOE in it:
    #for (hypotenuse_side, odd_side, even_side) in [(1180733, 831285, 838508)]:
        LSM = _LSM5HOE(HOE)
        _check_LSM(LSM)
        basic_params_ex = _LSM2basic_params_ex(LSM)
        #(basic_params, (ab, side_length_ratio)) = basic_params_ex
        yield basic_params_ex

def _try_to_find_counterexample_in_src_code__len_hypotenuse_lt(max1_len_hypotenuse, /):
    # [:try_to_find_counterexample_in_src_code]:here:isolated
    from collections import defaultdict

    # s = set()
    floor2ceils = defaultdict(set)
    for basic_params, (ab, side_length_ratio) in _iter_basic_paramss__len_hypotenuse_lt(max1_len_hypotenuse):
        #(a,b) = ab
        (floor_half_sqrt__odd4B, ceil_half_ez4B) = basic_params
        cs = floor2ceils[floor_half_sqrt__odd4B]
        if ceil_half_ez4B in cs:
            # [a =!= min_a<basic_params>]
            continue
        cs.add(ceil_half_ez4B)
        # if basic_params in s:
        #     # [a =!= min_a<basic_params>]
        #     continue
        # s.add(basic_params)
        ######################
        # [a == min_a<basic_params>]
        #
        (floor_half_sqrt__odd4B, ceil_half_ez4B), result_exs, lts, ok = _try_to_find_counterexample_in_src_code__at_(floor_half_sqrt__odd4B, ceil_half_ez4B)
        [result_ex___0_0, result_ex___1_0, result_ex___0_1] = result_exs
        [lt_00_10, lt_00_01, lt_10_01] = lts
        assert ab == result_ex___0_0[0]
        assert side_length_ratio == result_ex___0_0[1]
        if not ok:
            yield ((floor_half_sqrt__odd4B, ceil_half_ez4B), lts, side_length_ratio)

def _try_to_find_counterexample_in_src_code__at_(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    result_ex___0_0 = _mk_result_ex5basic_params___suppose_min_A__(floor_half_sqrt__odd4B, ceil_half_ez4B)
    result_ex___1_0 = _mk_result_ex5basic_params___suppose_min_A__(floor_half_sqrt__odd4B+1, ceil_half_ez4B)
    result_ex___0_1 = _mk_result_ex5basic_params___suppose_min_A__(floor_half_sqrt__odd4B, ceil_half_ez4B+1)
    lt_00_10 = _cmp_hypotenuse_side4result_ex_(result_ex___0_0, result_ex___1_0)
    lt_00_01 = _cmp_hypotenuse_side4result_ex_(result_ex___0_0, result_ex___0_1)
    lt_10_01 = _cmp_hypotenuse_side4result_ex_(result_ex___1_0, result_ex___0_1)
    lts = [lt_00_10, lt_00_01, lt_10_01]
    result_exs = [result_ex___0_0, result_ex___1_0, result_ex___0_1]
    ok = (all(lts) and lt_00_10 == -1 == lt_00_01 and (lt_10_01 == -1 or floor_half_sqrt__odd4B <= (ceil_half_ez4B==0)))
    return (floor_half_sqrt__odd4B, ceil_half_ez4B), result_exs, lts, ok
def _try_to_find_counterexample_in_src_code__between____(begin4floor_half_sqrt__odd4B, end4floor_half_sqrt__odd4B, begin4ceil_half_ez4B, end4ceil_half_ez4B, /):
    # [:try_to_find_counterexample_in_src_code]:here:isolated
    for floor_half_sqrt__odd4B in range(begin4floor_half_sqrt__odd4B, end4floor_half_sqrt__odd4B):
      for ceil_half_ez4B in range(begin4ceil_half_ez4B, end4ceil_half_ez4B):
        (floor_half_sqrt__odd4B, ceil_half_ez4B), result_exs, lts, ok = _try_to_find_counterexample_in_src_code__at_(floor_half_sqrt__odd4B, ceil_half_ez4B)
        [result_ex___0_0, result_ex___1_0, result_ex___0_1] = result_exs
        [lt_00_10, lt_00_01, lt_10_01] = lts
        if not ok:
            (ab, side_length_ratio, params) = result_ex___0_0
            yield ((floor_half_sqrt__odd4B, ceil_half_ez4B), lts, side_length_ratio)


def _cmp_hypotenuse_side4result_ex_(lhs_result_ex, rhs_result_ex, /):
    return sign_of(_hypotenuse_side5result_ex_(lhs_result_ex) - _hypotenuse_side5result_ex_(rhs_result_ex))

def _hypotenuse_side5result_ex_(result_ex, /):
        ab, side_length_ratio, params = result_ex
        (a, b) = ab
        (short_side, middle_side, long_side) = side_length_ratio
        (floor_half_sqrt__odd4B, ceil_half_ez4B, sqrt__plus_A_B_or_half) = params
        hypotenuse_side = long_side
        return hypotenuse_side

def _mk_result_ex5basic_params___suppose_min_A__(floor_half_sqrt__odd4B, ceil_half_ez4B, /):
    it = iter_right_angled_triangle_side_length_difference_ratio__given_B_(floor_half_sqrt__odd4B, ceil_half_ez4B, with_side_length_ratio=True, with_params=True)
    for result_ex in it:
        # [fst result_ex derived from min_a]
        break
    else:
        raise 000
    return result_ex

def iter_nums_Bs_ex__lt_(b0_iter, /, *, exact_vs_both_vs_rough):
    return (num_Bs_ex__lt_(b0, exact_vs_both_vs_rough=exact_vs_both_vs_rough) for b0 in b0_iter)
def num_Bs_ex__lt_(b0, /, *, exact_vs_both_vs_rough):
    if exact_vs_both_vs_rough is ...:
        f = num_Bs_lt__exact_and_rough_
    elif exact_vs_both_vs_rough is False:
        f = num_Bs_lt__exact_
    elif exact_vs_both_vs_rough is True:
        f = num_Bs_lt__rough_
    else:
        raise 000
    return f(b0)

def num_Bs_lt__exact_and_rough_(b0, /):
    return (num_Bs_lt__exact_(b0), num_Bs_lt__rough_(b0))
def num_Bs_lt__exact_(b0, /):
    '[num_Bs_lt_(b0) == [b0 >= 2]:(ceil_div_(ceil_sqrt_(b0)-1,2) +sum[ceil_div_(ceil_sqrt_(ceil_div_(b0,2**(ceil_half_ez4B*2-1)))-1,2) | [ceil_half_ez4B :<- [1..<ceil_div_(ceil_log2_(b0)+1,2)]]])]'
    if not b0 >= 2:
        return 0
    return ceil_div_(ceil_sqrt_(b0)-1,2) +sum(ceil_div_(ceil_sqrt_(ceil_div_(b0,2**(ceil_half_ez4B*2-1)))-1,2) for ceil_half_ez4B in range(1,ceil_div_(ceil_log2_(b0)+1,2)))
def num_Bs_lt__rough_(b0, /):
    '[num_Bs_lt_(b0) ~= [b0 >= 2]:(2*sqrt_(b0) +2*sqrt_(2*b0) -log2_(b0) -5)/4]'
    '[num_Bs_lt_(b0) ~= [b0 >= 2]:(-(5+log2_(b0))/4 +sqrt_(b0)*1.2071067811865475)]'
    if not b0 >= 2:
        return 0
    return (-(5+log2_(b0))/4 +sqrt_(b0)*1.2071067811865475)
def iter_nums_Bs_lt__zpow_(ks, /, *, validate):
    return (num_Bs_lt__zpow_(k, validate=validate) for k in ks)
    return map(num_Bs_lt__zpow_, ks)
def num_Bs_lt__zpow_(k, /, *, validate):
    '[@[k :<- [0..]] -> [num_Bs_lt_(2**k) == ceil_div_(ceil_sqrt_(2**k)-1,2) +sum[ceil_div_(ceil_sqrt_(2**i)-1,2) | [i :<- [1+k%2,3+k%2..<=k-1]]]]]'
    assert k >= 0
    r = ceil_div_(ceil_sqrt_(2**k)-1,2) +sum(ceil_div_(ceil_sqrt_(2**i)-1,2) for i in range(1+k%2,1+k,2))
    if validate:
        if not r == num_Bs_lt__exact_(2**k): raise 000
    return r

def iter_coprime_pints_to_(t, step, /):
    check_int_ge(1, t)
    for u in count_(1, step):
        if gcd(t,u) == 1:
            yield u
def _mk_heap_item__ver2_(t, /, *, SML_vs_HOE):
    it = iter_coprime_pints_to_(t, 2)
    heap_item = _mk_heap_item__continued__ver2_(t, it, SML_vs_HOE=SML_vs_HOE)
    return heap_item
def _mk_heap_item__continued__ver2_(t, it, /, *, SML_vs_HOE):
    for u in it:
        break
    else:
        raise 000
    s = t+u
    st = s,t
    SML = side_length_ratio = mk__right_angled_triangle_side_length_ratio5s_t_(s,t)
    result_ex2 = st, side_length_ratio, u
    key = _key5SML(SML, SML_vs_HOE=SML_vs_HOE)
    heap_item = (key, result_ex2, it)
    return heap_item
def mk__right_angled_triangle_side_length_ratio5s_t_(s,t, /):
    ss = s*s
    st = s*t
    tt = t*t
    HOE = (hypotenuse_side, odd_side, even_side) = (ss +tt, ss -tt, 2*st)
    LSM = _LSM5HOE(HOE)
    side_length_ratio = SML = _SML5LSM(LSM)
    return side_length_ratio

def iter_right_angled_triangle_side_length_ratios__ver0__factorisation4hypotenuse_(*, SML_vs_HOE, to_sort=True, may_max1_hypotenuse=None, turnoff__coprime=False):#, extended_output=False
    '[kw:turnoff__coprime =[def]= coprime_ratio vs non_coprime_triple]'
    #see:engine_selector4iter_right_angled_triangle_side_length_ratios_
    return iter_right_angled_triangles_with_coprime_side_length__len_hypotenuse_lt(may_max1_hypotenuse, SML_vs_HOE=SML_vs_HOE, to_sort=to_sort, turnoff__coprime=turnoff__coprime)
def iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_(*, SML_vs_HOE, extended_output=False):
    #see:engine_selector4iter_right_angled_triangle_side_length_ratios_
    t0 = 1
    heap_item0 = _mk_heap_item__ver2_(t0, SML_vs_HOE=SML_vs_HOE)
    hp = HeapWithKey(fst, [heap_item0])
    prev_key = (0,0,0)
    while 1:
        heap_item = hp.pop()
        #
        (key, result_ex2, it) = heap_item
        assert prev_key < key
        prev_key = key

        st, side_length_ratio, u = result_ex2
        yield _mk_extended_output_(key, side_length_ratio, result_ex2, SML_vs_HOE=SML_vs_HOE, extended_output=extended_output)

        ######################
        # [t,u >= 1][gcd(t,u)==1][u%2==1]:
        #   [hypotenuse_side5t_u_: (t,u) < (t,u+2)]
        #   [hypotenuse_side5t_u_: (t,1) < (t+1,1)]
        ######################
        (s, t) = st
        heap_item4next_U = _mk_heap_item__continued__ver2_(t, it, SML_vs_HOE=SML_vs_HOE)
        hp.push(heap_item4next_U)
        on_start = u==1
        if not on_start:
            continue

        (s, t) = st
        (short_side, middle_side, long_side) = side_length_ratio
        u
        ######################
        heap_item4next_T = _mk_heap_item__ver2_(t+1, SML_vs_HOE=SML_vs_HOE)
        hp.push(heap_item4next_T)
    raise 000

def iter_right_angled_triangle_side_length_ratios__ver3__GaussInteger_decompose4hypotenuse__arbitrary_order_(may_nm4fst_key=None, may_nm4snd_key=None, may____output_fmt__or__output_formatter=None, /, *, SML_vs_HOE, may_ST4continue=None):
    #see:engine_selector4iter_right_angled_triangle_side_length_ratios_
    if SML_vs_HOE is False:
        # export as SML
        # default sorted by LSM
        nm4fst_key = 'long_side'
        nm4snd_key = 'short_side'
    elif SML_vs_HOE is True:
        # export as HOE
        # default sorted by HOE
        nm4fst_key = 'hypotenuse_side'
        nm4snd_key = 'odd_side'
    else:
        raise 000
    fmt = SML_vs_HOE

    fmt, nm4fst_key, nm4snd_key
    if not may____output_fmt__or__output_formatter is None:
        fmt = may____output_fmt__or__output_formatter
    if not may_nm4fst_key is None:
        nm4fst_key = may_nm4fst_key
    if not may_nm4snd_key is None:
        nm4snd_key = may_nm4snd_key
    fmt, nm4fst_key, nm4snd_key

    return iter_right_angled_triangle_infos_with_coprime_side_length___ST_HOE_LSM__sorted_by__(nm4fst_key, nm4snd_key, fmt, may_ST4continue=may_ST4continue)

def __():
    j2nm = (
        ('factorisation4hypotenuse'
        ,'difference_ratio'
        ,'GaussInteger_decompose4hypotenuse'
        ,'GaussInteger_decompose4hypotenuse__arbitrary_order'
        ))
    j2func = (
        (iter_right_angled_triangle_side_length_ratios__ver0__factorisation4hypotenuse_
        ,iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
        ,iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_
        ,iter_right_angled_triangle_side_length_ratios__ver3__GaussInteger_decompose4hypotenuse__arbitrary_order_
        ))
    def engine_selector4iter_right_angled_triangle_side_length_ratios_(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse, /):
        #see: iter_right_angled_triangle_side_length_triples__
        ##########
        #see:iter_right_angled_triangle_side_length_ratios__ver0__factorisation4hypotenuse_
        #see:iter_right_angled_triangle_side_length_ratios__ver1__difference_ratio_
        #see:iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_
        #see:iter_right_angled_triangle_side_length_ratios__ver3__GaussInteger_decompose4hypotenuse__arbitrary_order_
        ##########
        nm_or_ver = factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse
        cls = type(nm_or_ver)
        if cls is str:
            nm = nm_or_ver
            j = j2nm.index(nm)
                # ^IndexError
            nm_or_ver = ver = j
            cls = type(nm_or_ver)
        else:
            pass
        if cls is int:
            ver = nm_or_ver
            f = j2func[ver]
                # ^IndexError
            return f
        raise LookupError(nm_or_ver)
        raise TypeError(nm_or_ver)
    #end-def engine_selector4iter_right_angled_triangle_side_length_ratios_(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse, /):
    return engine_selector4iter_right_angled_triangle_side_length_ratios_
engine_selector4iter_right_angled_triangle_side_length_ratios_ = __()


def key5HOE_(triple, /):
    HOE = triple
    key = HOE
    return key
def key5SML_(triple, /):
    #see:_key5SML
    #see:key5SML_
    SML = triple
    #key = _key5SML(SML, SML_vs_HOE=False)
    LSM = _LSM5SML(SML)
    key = LSM
    return key
def _mk__key5triple_(*, SML_vs_HOE):
    # vs: _key5SML: input is SML
    #   but _key5triple_: input is (SML|HOE)
    if SML_vs_HOE is True:
        _key5triple_ = key5HOE_
    elif SML_vs_HOE is False:
        _key5triple_ = key5SML_
    else:
        raise 000
    _key5triple_
    return _key5triple_
def hypotenuse5HOE_(triple, /):
    HOE = triple
    hypotenuse = HOE[0]
    return hypotenuse
def hypotenuse5SML_(triple, /):
    SML = triple
    hypotenuse = SML[2]
    return hypotenuse
def _mk__hypotenuse5triple_(*, SML_vs_HOE):
    if SML_vs_HOE is True:
        _hypotenuse5triple_ = hypotenuse5HOE_
    elif SML_vs_HOE is False:
        _hypotenuse5triple_ = hypotenuse5SML_
    else:
        raise 000
    _hypotenuse5triple_
    return _hypotenuse5triple_

def add_key4iter_right_angled_triangle_side_length_triples_(right_angled_triangle_side_length_triples, /, *, SML_vs_HOE):
    _key5triple_ = _mk__key5triple_(SML_vs_HOE=SML_vs_HOE)
    return ((_key5triple_(triple), triple) for triple in right_angled_triangle_side_length_triples)
def limit_hypotenuse4iter_right_angled_triangle_side_length_triples_(max1_hypotenuse, right_angled_triangle_side_length_triples, /, *, SML_vs_HOE):
    check_type_is(int, max1_hypotenuse)
    _hypotenuse5triple_ = _mk__hypotenuse5triple_(SML_vs_HOE=SML_vs_HOE)
    return takewhile(lambda triple:_hypotenuse5triple_(triple) < max1_hypotenuse, right_angled_triangle_side_length_triples)
#bug:return (triple for triple in right_angled_triangle_side_length_triples if ...)

def _mk_heap_item____turnoff__coprime_(t, /, *, SML_vs_HOE):
    it = iter_coprime_pints_to_(t, 2)
    heap_item = _mk_heap_item__continued____turnoff__coprime_(t, it, SML_vs_HOE=SML_vs_HOE)
    return heap_item
def _mk_heap_item__continued____turnoff__coprime_(t, it, /, *, SML_vs_HOE):
    for u in it:
        break
    else:
        raise 000
    s = t+u
    st = s,t
    SML = side_length_ratio = mk__right_angled_triangle_side_length_ratio5s_t_(s,t)
    result_ex2 = st, side_length_ratio, u
    key = _key5SML(SML, SML_vs_HOE=SML_vs_HOE)
    heap_item = (key, result_ex2, it)
    return heap_item

def iter_right_angled_triangle_side_length_triples5primitive_ratio_(right_angled_triangle_side_length_primitive_ratios, /, *, SML_vs_HOE):
    keyed_ps = add_key4iter_right_angled_triangle_side_length_triples_(right_angled_triangle_side_length_primitive_ratios, SML_vs_HOE=SML_vs_HOE)
    def _extract1():
        eof = False
        for (key4next, primitive_triple4next) in keyed_ps:
            break
        else:
            eof = True
            (key4next, primitive_triple4next) = (None, None)
        return (eof, key4next, primitive_triple4next)


    _key5triple_ = _mk__key5triple_(SML_vs_HOE=SML_vs_HOE)
    def mk_heap_item5primitive_triple_(eof, key4next, primitive_triple4next, /):
        assert not eof
        scale = 1
        output_triple = primitive_triple4next
        heap_item = (key4next, output_triple, scale, primitive_triple4next)
        (eof, key4next, primitive_triple4next) = _extract1()
        return (heap_item, eof, key4next, primitive_triple4next)
    def push4next_scale_(hp, heap_item, /):
        (key, output_triple, scale, primitive_triple) = heap_item
        next_scale = scale + 1
        output_triple4next_scale = (*map(int.__add__, output_triple, primitive_triple),)
        key4next_scale = _key5triple_(output_triple4next_scale)
        heap_item4next_scale = (key4next_scale, output_triple4next_scale, next_scale, primitive_triple)
        hp.push(heap_item4next_scale)
        return

    (eof, key4next, primitive_triple4next) = _extract1()
    if eof:
        return
    (heap_item, eof, key4next, primitive_triple4next) = mk_heap_item5primitive_triple_(eof, key4next, primitive_triple4next)

    hp = HeapWithKey(fst, [heap_item])
        # [len(hp) > 0]
    prev_key = (0,0,0)
    while 1:
        # [len(hp) > 0]
        assert hp
        #if not hp:
        if not (eof or hp.peek()[0] < key4next):
            (heap_item, eof, key4next, primitive_triple4next) = mk_heap_item5primitive_triple_(eof, key4next, primitive_triple4next)
            # [heap_item <= hp.peek()]
        else:
            heap_item = hp.pop()
            # [heap_item <= hp.peek()]
            # [len(hp) >= 0]
        # [len(hp) >= 0]
        heap_item
        # [heap_item <= hp.peek()]
        #
        (key, output_triple, scale, primitive_triple) = heap_item
        assert prev_key < key
        prev_key = key

        yield output_triple

        push4next_scale_(hp, heap_item)
        # [len(hp) > 0]
        # [heap_item <= hp.peek()]
            # ==>> logic<testing via prev_key>   is ok
    return

def iter_right_angled_triangle_side_length_triples__(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse, /, *, SML_vs_HOE, may_max1_hypotenuse, turnoff__coprime, uniform):
    '[kw:turnoff__coprime =[def]= coprime_ratio vs non_coprime_triple]'
    f = engine_selector4iter_right_angled_triangle_side_length_ratios_(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse)
    if not uniform:
        try:
            triples = f(SML_vs_HOE=SML_vs_HOE, may_max1_hypotenuse=may_max1_hypotenuse, turnoff__coprime=turnoff__coprime)
        except TypeError:
            # ver1,ver2,ver3
            pass
        else:
            # ver0
            return triples
        # ver1,ver2,ver3
        assert not f is iter_right_angled_triangle_side_length_ratios__ver0__factorisation4hypotenuse_
    assert uniform or not f is iter_right_angled_triangle_side_length_ratios__ver0__factorisation4hypotenuse_
    ######################
    # ver0,ver1,ver2,ver3
    triples = f(SML_vs_HOE=SML_vs_HOE)
    if turnoff__coprime:
        triples = iter_right_angled_triangle_side_length_triples5primitive_ratio_(triples, SML_vs_HOE=SML_vs_HOE)
    if not may_max1_hypotenuse is None:
        max1_hypotenuse = may_max1_hypotenuse
        triples = limit_hypotenuse4iter_right_angled_triangle_side_length_triples_(max1_hypotenuse, triples, SML_vs_HOE=SML_vs_HOE)
    return triples
#end-def iter_right_angled_triangle_side_length_triples__(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse, /, *, SML_vs_HOE, may_max1_hypotenuse, turnoff__coprime, uniform):
def iter_right_angled_triangle_side_length_triples_(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse=2, /, *, SML_vs_HOE=True, may_max1_hypotenuse=None, turnoff__coprime=False, uniform=False):
    '[kw:turnoff__coprime =[def]= coprime_ratio vs non_coprime_triple]'
    return iter_right_angled_triangle_side_length_triples__(factorisation4hypotenuse__vs__difference_ratio__vs__GaussInteger_decompose4hypotenuse, SML_vs_HOE=SML_vs_HOE, may_max1_hypotenuse=may_max1_hypotenuse, turnoff__coprime=turnoff__coprime, uniform=uniform)

if __name__ == "__main__":
    pass
__all__


from seed.math.right_angled_triangle_side_length import iter_right_angled_triangle_side_length_ratios__ver2__GaussInteger_decompose4hypotenuse_
from seed.math.right_angled_triangle_side_length import engine_selector4iter_right_angled_triangle_side_length_ratios_
from seed.math.right_angled_triangle_side_length import iter_right_angled_triangle_side_length_triples_

from seed.math.right_angled_triangle_side_length import *
