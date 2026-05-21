#__all__:goto
r'''[[[
e ../../python3_src/seed/math/floor_ceil_tools/fc_log.py

seed.math.floor_ceil_tools.fc_log
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil_tools.fc_log -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil_tools.fc_log:__doc__ -ht # -ff -df
#######

[[
move_from:
e ../../python3_src/seed/math/floor_ceil.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.floor_ceil_tools.fc_log   @f
]]]'''#'''
__all__ = r'''

ceil_log_
floor_log_
ceil_log2
floor_log2
floor_ceil_log_
floor_ceil_log2
imay_floor_log2
    extended_imay_floor_log2
    count_num_high_same_bits_of_two_uints


floor_log2_kth_root_
ceil_log2_kth_root_
    floor_log2_sqrt
    ceil_log2_sqrt



ceil_log2_div
floor_log2_div
'''.split()#'''
    #TODO:floor_log2_pow
    #TODO:floor_lshift_log2_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_div import ceil_div
___end_mark_of_excluded_global_names__0___ = ...

def ceil_log2(pint, /):
    r'''ceil_log2(p) = ceil(log2(p)) where p > 0

ceil_log2(p)
    | p == 2**power = power = floor_log2(p)
                    = floor_log2(2*p-1)
    | otherwise     = floor_log2(p)+1
                    = floor_log2(2*p-1)
==>> ceil_log2(p) = floor_log2(2*p-1)

example:
    >>> ceil_log2(1)
    0
    >>> ceil_log2(2)
    1
    >>> ceil_log2(3)
    2
    >>> ceil_log2(4)
    2
    >>> ceil_log2(5)
    3
    >>> ceil_log2(6)
    3
    >>> ceil_log2(7)
    3
    >>> ceil_log2(8)
    3
    >>> ceil_log2(9)
    4
'''
    assert pint > 0
    if 0:
        return floor_log2((pint<<1) -1)
    if 0:
        if pint == 1:
            return 0
        return 1+floor_log2(pint-1)
    if 1:
        e = floor_log2(pint)
        if not pint == (1<<e):
            e += 1
        return e
    raise logic-err

def floor_ceil_log_(base, pint, /, *, with_floor_pow:bool):
    #check_type_is(bool, with_floor_pow)
    if base == 2:
        #return floor_ceil_log2(pint, with_floor_pow=with_floor_pow)
        e0 = floor_log2(pint)
        fl_pw = (1<<e0)
    else:
        e0 = floor_log_(base, pint)
        fl_pw = base**e0
    # e0, fl_pw
    e1 = e0 + (not pint == fl_pw)
    if with_floor_pow:
        return (e0, e1, fl_pw)
    return (e0, e1, )
def floor_ceil_log2(pint, /, *, with_floor_pow:bool):
    return floor_ceil_log_(2, pint, with_floor_pow=with_floor_pow)

def floor_log2(pint, /):
    r'''floor_log2(p) = floor(log2(p)) where p > 0

assume:
    u >= 0
    p > 0
u < 2**u.bit_length()
2**(p.bit_length()-1) <= p < 2**p.bit_length()

==>> floor_log2(p) = p.bit_length()-1

example:
    >>> floor_log2(1)
    0
    >>> floor_log2(2)
    1
    >>> floor_log2(3)
    1
    >>> floor_log2(4)
    2
    >>> floor_log2(5)
    2
    >>> floor_log2(6)
    2
    >>> floor_log2(7)
    2
    >>> floor_log2(8)
    3
'''
    assert pint > 0
    return pint.bit_length()-1
assert (0).bit_length() == 0
assert (1).bit_length() == 1
assert (2).bit_length() == 2
assert (3).bit_length() == 2
assert (4).bit_length() == 3




def floor_log2_kth_root_(k, n, /):
    r'''[[[
    :: k{>=1} -> n{>=1} -> floor(log2(n**(1/k)))

    [k >= 1]
    [n >= 1]
    [w**k == n]
    [result := floor_log2(w)]
    [2**result <= w < 2**(result+1)]
    [2**(k*result) <= w**k < 2**(k*(result+1))]
    [(2**k)**result <= n < (2**k)**(result+1)]
    [result == floor_log_(2**k, n) == floor_log2(n)//k]

    #]]]'''
    assert k >= 1
    assert n >= 1
    e = floor_log2(n)//k
    assert (1<<(k*e)) <= n < (1<<(k*(e+1)))
    return e
def __():
  if 1:
    r'''[[[
    to proof correctness
    #]]]'''#'''
    check_type_is = None
  def floor_log2_kth_root_(k, n, /):
    check_type_is(int, k)
    if not k >= 1:raise ValueError(k)
    check_type_is(int, n)
    if not n >= 1:raise ValueError(n)
    # [k >= 1]
    # [n >= 1]

    lb_n = floor_log2(n)
    # [2**lb_n <= n < 2**(lb_n+1)]
    # [2**(lb_n/k) <= n**(1/k) < 2**((lb_n+1)/k)]
    # [rt := n**(1/k)]
    # [2**(lb_n/k) <= rt < 2**((lb_n+1)/k)]
    # [(lb_n/k) <= floor_log2(rt) < ((lb_n+1)/k)]
    # [(lb_n/k) <= floor_log2(rt) < ((lb_n+1)/k)]
    # [floor(lb_n/k) <= floor_log2(rt) < ceil((lb_n+1)/k)]
    # [(lb_n//k) <= floor_log2(rt) < (lb_n//k +1)]
    # [floor_log2(rt) == (lb_n//k)]
    lb_rt = lb_n//k
    #assert lb_rt >= 0
    # [lb_rt >= 0]
    return lb_rt


def ceil_log2_kth_root_(k, n, /):
    r'''[[[
    [k >= 1]
    [n >= 1]
    [w**k == n]
    [result := ceil_log2(w)]
    [2**(result-1) < w <= 2**result]
    [2**(k*(result-1)) < w**k <= 2**(k*result)]
    [(2**k)**(result-1) < n <= (2**k)**result]
    [result == ceil_log_(2**k, n) == ceil_div(ceil_log2(n), k)]
    [result == if n==1 then 0 else 1+floor_log2_kth_root_(k,n-1)]

    #]]]'''
    assert k >= 1
    assert n >= 1
    if 0:
        e = 0 if n == 1 else 1+floor_log2_kth_root_(k,n-1)
    else:
        e = ceil_div(ceil_log2(n), k)
    assert n==1 if e==0 else (1<<(k*(e-1))) < n <= (1<<(k*e))
    return e
def floor_log2_sqrt(n, /):
    return floor_log2_kth_root_(2, n)
def ceil_log2_sqrt(n, /):
    return ceil_log2_kth_root_(2, n)






def ceil_log2_div(n, d, /):
    return -floor_log2_div(d,n)
def floor_log2_div(n, d, /):
    '[floor_log2_div(n,d) =[def]= floor(log2(n/d)) = floor(log2(n)-log2(d)) = -ceil(log2(d)-log2(n)) = -ceil_log2_div(d,n)]'
    assert not d==0
    assert not n==0
    if d < 0:
        d = -d
        n = -n
    assert d > 0
    assert n > 0

    s = +1
    if n < d:
        # return -ceil_log2_div(d,n)
        n,d = d,n
        s = -1
    assert n >= d > 0

    diff_flb = floor_log2(n) - floor_log2(d)
    if s > 0:
        #floor
        #not_bug:
        r = diff_flb - ((n>>diff_flb) < d)
            # <==>
            #   r = diff_flb - (n < (d<<diff_flb))
    else:
        #ceil
        #bug:r = diff_flb + ((n>>diff_flb) > d)
        r = diff_flb + (n > (d<<diff_flb))

    assert r >= 0
    r *= s
    return r

def floor_log2_pow(n, k, /):
    '[floor_log2_pow(n,k) =[def]= floor_log2(pow(n,k))] # [floor_lshift_log2_(k,n) =[def]= floor(2**k * log2(n)) = floor(log2(n**2**k)) = floor_log2_pow(n,2**k)]'
    raise NotImplementedError
    vs-floor_lshift_log2_
    vs-floor_lshift_kth_root_
    TODO
def imay_floor_log2(n, /):
    assert n >= 0
    if n == 0:
        return -1
    return floor_log2(n)
def extended_imay_floor_log2(n, /):
    if n > 0:
        return floor_log2(n)
    return -1-ceil_log2(1-n)

def count_num_high_same_bits_of_two_uints(u, v, /):
    '求最高有效位数目'
    # [count_num_high_1bits_of_uint u =[def]= if n==0 then 0 else (1+floor_log2(n>>min{i<-[0..] | [n_i := (n>>i)][floor_log2(n_i+1)==floor_log2(n_i)+1]}))]
    # [count_num_high_same_bits_of_two_uints u v =[def]= max{0, imay_floor_log2(u)-imay_floor_log2(u^v)}]
    assert u >= 0
    assert v >= 0
    return max(0, imay_floor_log2(u)-imay_floor_log2(u^v))
    return imay_floor_log2(max(u,v))-imay_floor_log2(u^v)
    if u > v:
        u, v = v, u
    #assert 0 <= u <= v
    v-u
    0b11_1000 - 0b11_0000 == 0b00_1000
    0b11_1000 - 0b11_0111 == 0b00_0001
def floor_lshift_log2_(k, n, /):
    r'''[[[
    [floor_lshift_log2_(k,n) =[def]= floor(2**k * log2(n))]
    [floor_lshift_log2_(k,n) == floor_log2(n**2**k)]
        #一次平方，才得1bit，太慢！
    [flbN := floor_log2(n)]
    [clbN := ceil_log2(n)]
    [2**flbN <= n <= 2**clbN]
    [0 <= clbN-flbN <= 1]
    [2**(flbN*2**k) <= n**2**k <= 2**(clbN*2**k)]
    [flbNk := floor_log2(n**2**k)]
    [clbNk := ceil_log2(n**2**k)]
    [2**flbNk <= n**2**k <= 2**clbNk]
    [0 <= clbNk-flbNk <= 1]
    [2**(flbN*2**k) <= 2**flbNk <= n**2**k <= 2**clbNk <= 2**(clbN*2**k)]
    [2**flbN <= 2**(flbNk/2**k) <= n <= 2**(clbNk/2**k) <= 2**clbN]
    [flbN == floor_div(flbNk, 2**k)]
    [clbN == ceil_div(clbNk, 2**k)]

    [flbNk
    == max{i <- [flbN*2**k..=clbN*2**k] | [2**i <= n**2**k]}
    == max{i <- [flbN*2**k..=clbN*2**k] | [floor_kth_root_(2**k, 2**i) <= n]}
    ]
        search (flbNk,clbNk) between [flbN*2**k..=clbN*2**k]
        需要求 kth_root_(2**k, 2**i) for i <- [flbN*2**k..=clbN*2**k]
        [kth_root_(2**k, 2**i)
        == kth_root_(2**k, 2**((i//2**k)*2**k + (i%2**k)))
        == kth_root_(2**k, 2**((i//2**k)*2**k) * 2**(i%2**k))
        == kth_root_(2**k, 2**((i//2**k)*2**k)) * kth_root_(2**k, 2**(i%2**k))
        == 2**(i//2**k) * kth_root_(2**k, 2**(i%2**k))
        ]
        [floor_kth_root_(2**k, 2**i)
        == floor(2**(i//2**k) * kth_root_(2**k, 2**(i%2**k)))
        == floor_lshift_kth_root_((i//2**k), 2**k, 2**(i%2**k))
        ]
        另:[floor_kth_root_<2**k> === (floor_sqrt**k)]

        !![flbN*2**k <= i <= clbN*2**k]
        [flbN <= i//2**k <= clbN]
            # kth_root_精度要求小数点后clbN比特
        [kth_root_(2**k, 2**(i%2**k)) == (floor_sqrt**k)(2**(i%2**k))]
            #但是 (2**(i%2**k))有O(2**k)bit，还是 太大！


    [(e, odd) := factor_pint_out_2_powers(n)]
    [n==(odd*2**e)]
    [e>=0]
    [odd%2==1]
    [floor_lshift_log2_(k,n)
    == floor_log2(n**2**k)
    == floor_log2((odd*2**e)**2**k)
    == floor_log2(odd**2**k * (2**e)**2**k)
    == floor_log2(odd**2**k) + (e*2**k)
    == floor_lshift_log2_(k,odd) + (e*2**k)
    ]
    [floor_lshift_log2_(k,1) == 0]
    [floor_lshift_log2_(k,2) == 2**k]
    [floor_lshift_log2_(k,4) == 2*2**k]
    [floor_lshift_log2_(k,2**e) == e*2**k]
    #n翻倍，则输出增加2**k

    [floor_lshift_log2_(k,odd-1) <= floor_lshift_log2_(k,odd) <= floor_lshift_log2_(k,odd+1)]
        #范围大小 约为 1+2**k*(2/2**floor_log2(odd)) = 1+2**(k+1-floor_log2(odd))
        #比如:[2**k == floor_lshift_log2_(k,3-1) <= floor_lshift_log2_(k,3) <= floor_lshift_log2_(k,3+1) == 2*2**k]
    [(odd-1)%2==0]
    [(odd+1)%2==0]
        #recur!
        #n reduced, but k unchanged
    #缩小范围:
    [floor_lshift_log2_(k,odd)
    == floor_lshift_log2_(k-1, odd**2)
    == floor_lshift_log2_(k-s, odd**2**s)
    #until [((k-s)+1-floor_log2(odd**2**s)) <= -t]
    # <==> [floor_log2(odd**2**s) >= (k-s+1+t)]
    # <<== [floor_log2(odd)*2**s >= (k+1+t)]
    # <<== [2**s >= ceil_div((k+1+t), floor_log2(odd))]
    # <<== [s >= ceil_log2(ceil_div((k+1+t), floor_log2(odd)))]
    ]




    #]]]'''

    r'''[[[

[imay_floor_log2 :: uint -> imay]
[imay_floor_log2(n) =[def]= if n==0 then -1 else floor_log2(n)]
[count_num_high_1bits_of_uint u =[def]= if n==0 then 0 else (1+floor_log2(n>>min{i<-[0..] | [n_i := (n>>i)][floor_log2(n_i+1)==floor_log2(n_i)+1]}))]
[count_num_high_same_bits_of_two_uints u v =[def]= max{0, imay_floor_log2(u)-imay_floor_log2(u^v)}]
[n, e :: uint][d :: int]:
    [approximate(n,e,d) =[def]= (n//2**e +d) *2**e]

@[f::uint->uint] -> [f单调递增][@[n::uint] -> [f(n) <= f(n+1)]] -> [
    [@[n::uint] -> @[e::uint] -> [n_e0 := approximate(n,e,0)][n_e1 := approximate(n,e,1)][#n_e0<=n<n_e1#][#f(n_e0)<=f(n)<=f(n_e1)#] -> [f(n_e0) >= 1] -> [Lh_n_e := count_num_high_same_bits_of_two_uints(f(n_e0),f(n_e1))] -> [L_n_e := 1+imay_floor_log2(f(n_e0))][L_n := 1+imay_floor_log2(f(n))][#L_n == count_num_high_same_bits_of_two_uints(f(n),f(n)) >= L_n_e>=Lh_n_e#] -> [
        #大端序计算floor高位有效精度
        [(f(n_e0)>>(L_n_e-Lh_n_e)) == (f(n)>>(L_n-Lh_n_e))][#floor_div(x,2**y)#]
        #bug:???精度提高:追加的输入比特里必须含零
        [@[de::uint] -> [n_ed0 := approximate(n,e+de,0)][n_ed1 := approximate(n,e+de,1)] -> [n_ed0//2**(e+de) %2**de == 2**de -1][#全一#] -> [n_ed1 == n_e1]]
    ]]
]



floor_lshift_log2_
    floor_log2(n**2) 并非一定要完整计算〖n**2〗
    [floor_log2(n**2) == floor_log2((n/2**floor_log2(n))**2) +2*floor_log2(n)]
    [1 <= (n/2**floor_log2(n)) < 2]
    [1 <= (n/2**floor_log2(n))**2 < 4]
    [0 <= floor_log2((n/2**floor_log2(n))**2) < 2]
    [floor_log2((n/2**floor_log2(n))**2)
    == [(n/2**floor_log2(n)) >= sqrt_2]
    == [n >= (sqrt_2*2**floor_log2(n))]
    == [n >= ceil(sqrt_2*2**floor_log2(n)) == 1+floor_sqrt(2**(1+2*floor_log2(n)))]
    ]
    只要n与(sqrt_2*2**floor_log2(n))不是太接近，则只需比较前几位

    与其计算sqrt_2，不如计算n前几位的平方
        #通过floor_sqrt(或连分数+floor_lshift_div_) 计算sqrt_2，也不难，但关键是，从n**2**1 推广至 n**2**k (相应地，从sqrt_2<-{kth_root_(2**1; 2**(i%2**1))}推广到{kth_root_(2**k;2**(i%2**k))}。)
    [L>=0]:
        [floor_log2((n/2**floor_log2(n))**2)
        == [(n/2**floor_log2(n)) >= sqrt_2]
        == [(n/2**(floor_log2(n)-L)) >= sqrt_2*2**L]
        == [(n/2**(floor_log2(n)-L))**2 >= 2**(1+2*L)]
        * ... <= [(ceil(n/2**(floor_log2(n)-L)))**2 >= 2**(1+2*L)]
            <= [(1+(n>>(floor_log2(n)-L)))**2 >= 2**(1+2*L)]
            == [floor_log2((1+(n>>(floor_log2(n)-L)))**2) >= (1+2*L)]

        * ... >= [(floor(n/2**(floor_log2(n)-L)))**2 >= 2**(1+2*L)]
            == [(n>>(floor_log2(n)-L))**2 >= 2**(1+2*L)]
            == [imay_floor_log2((n>>(floor_log2(n)-L))**2) >= (1+2*L)]
        ]
    !![n>=1]
    [@[L>=0] -> [imay_floor_log2((n>>(floor_log2(n)-L))**2) >= (1+2*L)] -> [floor_log2((n/2**floor_log2(n))**2) == 1]]
    [@[L>=0] -> [floor_log2((1+(n>>(floor_log2(n)-L)))**2) < (1+2*L)] -> [floor_log2((n/2**floor_log2(n))**2) == 0]]

    [@[L>=0] -> [imay_floor_log2((n>>(floor_log2(n)-L))**2) >= (1+2*L)] -> [floor_log2(n**2) == 1+2*floor_log2(n)]]
    [@[L>=0] -> [floor_log2((1+(n>>(floor_log2(n)-L)))**2) < (1+2*L)] -> [floor_log2(n**2) == 0+2*floor_log2(n)]]

    计算量逐次翻倍，最终整体计算量只是最后一次的计算量的两倍
    计划一下前面L应有的增长速率:
        [计算量(mul<bit_length>) == O(bit_length**2)]:
            [imay_floor_log2(n>>(floor_log2(n)-L)) ~= bit_length(n)]
            [计算量(每次迭代<L>) == 计算量(mul<bit_length=L>) = O(L**2)]
            [2 == 计算量(每次迭代<L[i+1]>)/计算量(每次迭代<L[i]>) == O((L[i+1]>/L[i]>)**2)]
            [(L[i+1]>/L[i]>) ~= sqrt_2 = 连分数[]]
            x**2 = 2
            [sqrt_2
            == 1+(sqrt_2-1)
            == 1+1/(1/(sqrt_2-1))
            == 1+1/(sqrt_2+1)
            ]
            [(sqrt_2+1) == 2+1/(sqrt_2+1) == 连分数[2; 2,2..]]
                # limit[2, 5/2, 12/5, 29/12, 70/29, 169/70, 408/169, 985/408, ...]
            [sqrt_2 == 连分数[1; 2,2..]]
                # limit[1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, ...]


===递推关系与增长速率
[A[n] := A[n-1]+A[n-2]][x := limit[A[n]/A[n-1] | [n --> +oo]]]:
    [A[n]/A[n-1] == 1+1/(A[n-1]/A[n-2])]
    [x == 1+1/x]
    [x**2 -x -1 ==0]
    [x == (1+sqrt_5)/2 == golden_ratio = 1.618... = 连分数[1; 1,1..]]
    # golden section:黄金分割
    # extreme and mean ratio??: 中外比
[L >= 0][len(K)==L+1][K[0] > 0][K[0]*A[n] := sum{K[i]*A[n-i] | [i :<- [1..=L]]}][x := limit[A[n]/A[n-1] | [n --> +oo]]]
    #有限长线性递推关系与增长速率
    [A[n] ~= A[n-1]*x ~= A[n-i]*x**i]
    [A[n-i] ~= A[n]/x**i]
    [K[0]*A[n] ~= sum{K[i]*A[n]/x**i | [i :<- [1..=L]]}]
    [K[0] == sum{K[i]/x**i | [i :<- [1..=L]]}]
    [K[0]*x**L == sum{K[i]*x**(L-i) | [i :<- [1..=L]]}]
    [0 == sum{(-1)**[i==0] * K[i]*x**(L-i) | [i :<- [0..=L]]}]
    这个多项式的根的大小？？


[n>=1][x := 连分数[n; n, n..]]:
    [x == n+1/x]
    [x**2 -n*x -1 ==0]
    !![x > n >= 1 > 0]
    [x == (n+sqrt(n**2+4))/2]
    [x(n=1) == (1+sqrt(5))/2] #黄金比例
    [x(n=2) == (2+sqrt(8))/2 == 1+sqrt_2]
    [x(n=3) == (3+sqrt(13))/2]
    [x(n=4) == (4+sqrt(20))/2 == 2+sqrt_5]
    [x(n=11) == (11+sqrt(125))/2 == (11+5*sqrt_5)/2]
    [x(n=14) == (14+sqrt(200))/2 == 7+5*sqrt_2]
    [x(n=19) == (19+sqrt(365)/2]
    [x(n=20) == (20+sqrt(404))/2 == 10+sqrt_101]
    [n==2*k]:
        [x == (n+sqrt(n**2+4))/2 == (2*k+sqrt(4*k**2+4))/2 == k+sqrt(k**2+1)]
        [k+sqrt(k**2+1) == 连分数[2*k; 2*k, 2*k..]]
        [sqrt(k**2+1) == 连分数[k; 2*k, 2*k..]]
            # k**2+1 <- [2,5,10,17,26,37,50,65,82,101,122,145,170,197,226,257,290,325,362,401,...]

[m,n>=1][x := 连分数[m; n, m, n, m, n, ...]]:
    [x == m + 1/(n+1/x) == m + x/(n*x+1)]
    [n*x**2+x == m*n*x+m + x]
    [n*x**2 -m*n*x -m ==0]
    !![x > m]
    [x == (m*n +sqrt(m**2*n**2+4*m*n))/2]
    [x == (m*n +sqrt((m*n+4)*m*n))/(2*n)]
    [m == 2*k*n]:
        [x == (m*n +sqrt((m*n+4)*m*n))/(2*n)
        == (2*k*n*n +sqrt((2*k*n*n+4)*2*k*n*n))/(2*n)
        == (k*n +sqrt((k*n**2+2)*k))
        == (k*n +sqrt((k*n)**2+2*k))
        ]
        [(k*n +sqrt((k*n)**2+2*k)) == 连分数[2*k*n; n, 2*k*n, n, 2*k*n, ...]]
        [sqrt((k*n)**2+2*k) == 连分数[k*n; n, 2*k*n, n, 2*k*n, ...]]




#TODO:其他
    #整数表达为(bit_length, Iter (bit_length, uint))
        #无限长浮点数连续开平方
#TODO:实现floor_lshift_log2_
    部分平方求[floor_log2_square(n) =[def]= floor_log2(n**2)]
        当[(n>>flbN) ~= kth_root_(2**k,2)]时，计算量最大，等价于直接求[floor_log2(n**2**k)]


    #]]]'''
    if 0:
        return floor_log2(n**2**k) #太慢！
    raise NotImplementedError('waiting floor_sqrt')
    if 0:
        return floor_log2_pow(n, 2**k)

r'''[[[
def _mk__floor_lshift_log2_(t, /):
  @recur5yield__list__echo__echo
  def floor_lshift_log2_(k, n, /):
    assert k >= 0
    assert n >= 1
    if k == 0:
        r = floor_log2(n)
    elif n&1 == 0:
        r = yield recur_even(k, n)
    else:
        r = yield recur_odd(k, n)
    return True, r;yield
  def recur_even(k, even, /):
    assert k >= 1
    assert even&1==0
    (e, odd) = factor_pint_out_2_powers(even)
    assert e >= 1
    r_ = yield recur_odd(k, odd)
    r = r_ + (e<<k)
    return True, r;yield

  def recur_odd(k, odd, /):
    assert k >= 1
    assert odd&1==1
    if odd==1:
        r = 0
    else:
        while not (k+1-floor_log2(odd)) <= -t:
            k -= 1
            odd **= 2
            if k == 0:
                break
        else:
            while k:
                rL = recur_even(k, odd-1)
                rR = recur_even(k, odd+1)
                if rL == rR:
                    r = rL
                    break
                k -= 1
                odd **= 2
            else:
                pass
        if k == 0:
            r = floor_log2(odd)

    return True, r;yield
  return floor_lshift_log2_
if 0:floor_lshift_log2_ = _mk__floor_lshift_log2_()
    #还是太慢
#_floor_lshift_log2__via_even_odd_ = _mk__floor_lshift_log2_()
#]]]'''#'''




def ceil_log_(B, n, /):
    r'''
>>> ceil_log_(2, 1)
0
>>> ceil_log_(2, 2)
1
>>> ceil_log_(2, 3)
2
>>> ceil_log_(2, 4)
2
>>> ceil_log_(2, 5)
3
>>> ceil_log_(2, 7)
3
>>> ceil_log_(2, 8)
3
>>> ceil_log_(2, 9)
4

>>> ceil_log_(3, 1)
0
>>> ceil_log_(3, 2)
1
>>> ceil_log_(3, 3)
1
>>> ceil_log_(3, 4)
2
>>> ceil_log_(3, 8)
2
>>> ceil_log_(3, 9)
2
>>> ceil_log_(3, 10)
3


    #'''
    assert B >= 2
    assert n >= 1
    if n == 1:
        e = 0
        assert n == B**e
    else:
        e = 1+floor_log_(B, n-1)
    assert (B**(e-1) if e else 0) < n <= B**e
    return e
def floor_log_(B, n, /):
    r'''
>>> floor_log_(2, 1)
0
>>> floor_log_(2, 2)
1
>>> floor_log_(2, 3)
1
>>> floor_log_(2, 4)
2
>>> floor_log_(2, 5)
2
>>> floor_log_(2, 7)
2
>>> floor_log_(2, 8)
3
>>> floor_log_(2, 9)
3

>>> floor_log_(3, 1)
0
>>> floor_log_(3, 2)
0
>>> floor_log_(3, 3)
1
>>> floor_log_(3, 4)
1
>>> floor_log_(3, 8)
1
>>> floor_log_(3, 9)
2
>>> floor_log_(3, 10)
2

>>> floor_log_(3, 10**100)
209
>>> floor_log_(3, 11**1000)
2182
>>> floor_log_(3, 12**1000_000)
2261859
>>> floor_log_(3, 1<<1000_000)
630929

>>> floor_log_(5, 12**1000_000)
1543959
>>> floor_log_(6, 1<<1000_000)
386852
>>> floor_log_(8, 1<<1000_000)
333333
>>> floor_log_(9, 1<<1000_000)
315464
>>> floor_log_(29, 1<<1000_000)
205846



[log_(B;n)
== log2(n)/log2(B)
== (log2(n)*2**k)/(log2(B)*2**k)
== (log2(n)*2**k_)*2**(k-k_)/(log2(B)*2**k)
    * > (floor_lshift_log2_(k_;n))*2**(k-k_)/(1+floor_lshift_log2_(k;B))
    * < (1+floor_lshift_log2_(k_;n))*2**(k-k_)/floor_lshift_log2_(k;B)
]
[floor_lshift_log2_(k_;n)*2**(k-k_)//(1+floor_lshift_log2_(k;B)) <= floor_log_(B;n) <= (1+floor_lshift_log2_(k_;n))*2**(k-k_)//floor_lshift_log2_(k;B)]
[floor_log2(B)*2**k <= floor_lshift_log2_(k;B) < (1+floor_log2(B))*2**k]


[??? -> [u <= (n+dn)//d - n//(d+dd) <= v]]

view others/数学/divmod加速.txt
[[n_,dn,d_ :: int][d_>=1] -> [-d_ -(d_+1)*dn <= n_ <= (d_+1)**2 -2 -(d_+1)*dn] -> [0 <= ((n_+dn)//d_ - n_//(d_+1)) <= 1]]

[0 <= k_ <= k][B>=2][n_ := floor_lshift_log2_(k_;n)*2**(k-k_)][dn := 2**(k-k_)][d_ := floor_lshift_log2_(k;B)]:
    [n_ > (d_+1)**2 -2 -(d_+1)*dn]:
        [floor_lshift_log2_(k_;n)*2**(k-k_) > (floor_lshift_log2_(k;B)+1)**2 -2 -(floor_lshift_log2_(k;B)+1)*2**(k-k_)]
        [(1+floor_log2(n))*2**k_
        >= floor_lshift_log2_(k_;n)
        > (floor_lshift_log2_(k;B)+1)**2/2**(k-k_) -2/2**(k-k_) -(floor_lshift_log2_(k;B)+1)
        == (floor_lshift_log2_(k;B)+1)*((floor_lshift_log2_(k;B)+1)/2**(k-k_) -1) -2/2**(k-k_)
        >= (floor_log2(B)*2**k+1)*((floor_log2(B)*2**k+1)/2**(k-k_) -1) -2/2**(k-k_)
        == 2**k*(floor_log2(B)+1/2**k)*(2**k_*(floor_log2(B)+1/2**k) -1) -2/2**(k-k_)
        ]
        [(1+floor_log2(n))*2**k_ > 2**k*(floor_log2(B)+1/2**k)*(2**k_*(floor_log2(B)+1/2**k) -1) -2/2**(k-k_)]
        [(1+floor_log2(n)) > 2**k*(floor_log2(B)+1/2**k)*(floor_log2(B) +1/2**k -1/2**k_) -2/2**k]
        [[B<-{2,3}][k_==0]]:
            [(floor_log2(B) +1/2**k -1/2**k_) == 1/2**k]
        [[B>=4]or[k_>=1]]:
            [floor_log2(B)/2 >= 1/2**k_]
            [(floor_log2(B) +1/2**k -1/2**k_) >= (floor_log2(B)/2 +1/2**k)]
            [(1+floor_log2(n))
            > 2**k*(floor_log2(B)+1/2**k)*(floor_log2(B) +1/2**k -1/2**k_) -2/2**k
            >= 2**k*(floor_log2(B)+1/2**k)*(floor_log2(B)/2 +1/2**k) -2/2**k
            == 2**k*(floor_log2(B)**2 /2 +3/2*floor_log2(B)/2**k +1/4**k) -2/2**k
            == 2**k*floor_log2(B)**2 /2 +3/2*floor_log2(B) -1/2**k
            ]
            [2**k*floor_log2(B)**2 /2 < (floor_log2(n) +1 +1/2**k -3/2*floor_log2(B))]
            [2**k*floor_log2(B)**2 < (2*floor_log2(n) +2 +2/2**k -3*floor_log2(B))]
            [2**k < (2*floor_log2(n) +2 +2/2**k -3*floor_log2(B))/floor_log2(B)**2]
            [2**k < (2*floor_log2(n) +4 -3*floor_log2(B))/floor_log2(B)**2]
    [[[B>=4]or[k_>=1]] -> [n_ > (d_+1)**2 -2 -(d_+1)*dn] -> [2**k < (2*floor_log2(n) +4 -3*floor_log2(B))/floor_log2(B)**2]]
    #逆否:
    [[[B>=4]or[k_>=1]] -> [2**k >= (2*floor_log2(n) +4 -3*floor_log2(B))/floor_log2(B)**2] -> [n_ <= (d_+1)**2 -2 -(d_+1)*dn]]

    !![[n_,dn,d_ :: int][d_>=1] -> [-d_ -(d_+1)*dn <= n_ <= (d_+1)**2 -2 -(d_+1)*dn] -> [0 <= ((n_+dn)//d_ - n_//(d_+1)) <= 1]]
    !![0 <= k_ <= k][B>=2][n_ := floor_lshift_log2_(k_;n)*2**(k-k_)][dn := 2**(k-k_)][d_ := floor_lshift_log2_(k;B)]
    [[[B>=4]or[k_>=1]] -> [2**k >= (2*floor_log2(n) +4 -3*floor_log2(B))/floor_log2(B)**2] -> [
        [n_ <= (d_+1)**2 -2 -(d_+1)*dn]
        !![n_ := floor_lshift_log2_(k_;n)*2**(k-k_)][n_ >= 0]
        [0 <= n_ <= (d_+1)**2 -2 -(d_+1)*dn]
        !![0 <= k][B>=2][d_ := floor_lshift_log2_(k;B)][d_ >= 1]
        [0 <= ((n_+dn)//d_ - n_//(d_+1)) <= 1]
        [0 <= ((floor_lshift_log2_(k_;n)+1)*2**(k-k_)//floor_lshift_log2_(k;B) - floor_lshift_log2_(k_;n)*2**(k-k_)//(floor_lshift_log2_(k;B)+1)) <= 1]

        !![floor_lshift_log2_(k_;n)*2**(k-k_)//(1+floor_lshift_log2_(k;B)) <= floor_log_(B;n) <= (1+floor_lshift_log2_(k_;n))*2**(k-k_)//floor_lshift_log2_(k;B)]
        [0 <= floor_log_(B;n)-floor_lshift_log2_(k_;n)*2**(k-k_)//(1+floor_lshift_log2_(k;B)) <= 1]
        ]]

[[0 <= k_ <= k] -> [[B>=4]or[k_>=1]] -> [2**k >= (2*floor_log2(n) +4 -3*floor_log2(B))/floor_log2(B)**2] -> [0 <= floor_log_(B;n)-floor_lshift_log2_(k_;n)*2**(k-k_)//(1+floor_lshift_log2_(k;B)) <= 1]]


    #'''
    assert B >= 2
    assert n >= 1
    e = _2_floor_log_(B, n)
    assert e >= 0
    #assert 1 <= n//B**e < B
    assert B**e <= n < B**(e+1)
    return e
def _2_floor_log_(B, n, /):
    if n < B: return 0
    # [n >= B]
    flbN = floor_log2(n)
    if B == 2:
        return flbN
    clbB = ceil_log2(B)
    assert clbB >= 2
    q = flbN//clbB
    if B == (1<<clbB):
        return q
    # [(1<<(clbB-1)) < B < (1<<clbB)]

    # [1 <= clbB-1 < log2(B) < clbB]
    # [log2(n)/clbB < log(B;n)==log2(n)/log2(B) < log2(n)/(clbB-1)]
    # [flbN//clbB <= floor_log_(B;n) <= flbN/(clbB-1)]
    q1 = flbN//(clbB-1)
    if q==q1:
        # [0 <= flbN-clbB*q < clbB]
        # [0 <= flbN-(clbB-1)*q1 < (clbB-1)]
        # [0 <= flbN-clbB*q < clbB-1-q]
        return q
    # [flbN >= (clbB-1) >= 1]
    #   since:[0 <= flbN < (clbB-1)] ==>> [q==0==q1]
    # xxx [flbN >= clbB*(clbB-1)]
    # xxx [n >= B**2]


    n0 = n; del n
    n_ = n0
    e_ = 0
    Bpow_clb_pairs = None
    while q1 - q > 32:
        n0_ = n_
        #_clb_Bpow = ceil_sqrt(flbN)
        #_clb_Bpow = 1<<ceil_log2_sqrt(flbN)
        #_clb_clb_Bpow = ceil_div(ceil_log2(flbN), 2)
        _clb_clb_Bpow = ceil_log2_sqrt(flbN)
        _clb_Bpow = (1<<_clb_clb_Bpow)
        # [(_clb_Bpow//2)**2 < flbN <= _clb_Bpow**2]
        assert (_clb_Bpow//2)**2 < flbN <= _clb_Bpow**2

        if Bpow_clb_pairs is None:
            Bpow_clb_pairs = [(B, clbB)]
            while Bpow_clb_pairs[-1][1] < _clb_Bpow:
                Bpow = Bpow_clb_pairs[-1][0]**2
                clb_Bpow = ceil_log2(Bpow)
                Bpow_clb_pairs.append((Bpow, clb_Bpow))
            idx4Bpow_clb_pairs = len(Bpow_clb_pairs)-1
        else:
            for j in reversed(range(idx4Bpow_clb_pairs)):
                if Bpow_clb_pairs[j][1] < _clb_Bpow:
                    break
            else:
                j = -1
            idx4Bpow_clb_pairs = j+1

        #(Bpow, clb_Bpow) = Bpow_clb_pairs[idx4Bpow_clb_pairs]
        #assert clb_Bpow >= _clb_Bpow
        #   #由于下面再次微调，不一定有[clb_Bpow >= _clb_Bpow]
        # [ceil_div(clb_Bpow,2) < _clb_Bpow <= clb_Bpow]
        # [ceil_div(clb_Bpow,2)//2 <= _clb_Bpow//2 <= ceil_div(clb_Bpow,2) < _clb_Bpow <= clb_Bpow]
        # [(_clb_Bpow//2)**2 < flbN <= _clb_Bpow**2]
        # [((clb_Bpow+1)//4)**2 == (ceil_div(clb_Bpow,2)//2)**2 < flbN <= clb_Bpow**2]
        # [flbN//clb_Bpow >= ((clb_Bpow+1)//4)**2//clb_Bpow >= ((clb_Bpow+1-3)/4)**2/clb_Bpow//1 == (clb_Bpow-4+4/clb_Bpow)/16//1 >= ((clb_Bpow-4)//16)]
        # [[clb_Bpow >= 20] -> [clb_Bpow <= flbN]]


        if 1:
            for j in reversed(range(idx4Bpow_clb_pairs)):
                if Bpow_clb_pairs[j][1]**2 < flbN:
                    break
            else:
                j = -1
            idx4Bpow_clb_pairs = j+1
        (Bpow, clb_Bpow) = Bpow_clb_pairs[idx4Bpow_clb_pairs]
        assert flbN <= clb_Bpow**2
        exp4Bpow = (1<<idx4Bpow_clb_pairs)
        assert Bpow == B**exp4Bpow
        if not exp4Bpow >= 2:
            break
        assert clb_Bpow >= 4 # == ceil_log2(3**2)
        if not clb_Bpow <= flbN:
            #if not Bpow <= n0_:
            # [[clb_Bpow >= 20] -> [clb_Bpow <= flbN]]
            # [[not$ [clb_Bpow <= flbN]] -> [clb_Bpow < 20]]
            assert clb_Bpow < 20
            break
        # [clb_Bpow <= flbN]

        assert not (B==3 and n0_ <= 31)
        #if not clb_Bpow == 2:原条件，更改如下：
        if not (B==3 and n0_ <= 31):
            # 粗略计算floor_log_Bpow_n
            assert clb_Bpow >= 3 #[保留]对应原条件:[not clb_Bpow == 2]
            q_pow = flbN//clb_Bpow
            q1_pow = flbN//(clb_Bpow-1)
            assert q_pow >= 1 # since [clb_Bpow <= flbN]
            assert 0 <= q1_pow-q_pow <= 2
            approximate_floor_log_Bpow_n = q_pow
            n_ = n0_//Bpow**approximate_floor_log_Bpow_n
            e_ += exp4Bpow*approximate_floor_log_Bpow_n
            #assert 1 <= n_ < Bpow**3
            for i in range(2):
                if n_ < Bpow:
                    break
                n_ //= Bpow
                e_ += exp4Bpow
            assert 1 <= n_ < Bpow

            flbN_ = floor_log2(n_)
            # [n0_//n_ >= Bpow**approximate_floor_log_Bpow_n == (B**exp4Bpow)**q_pow >= (3**2)**(flbN//clb_Bpow) >= 9**((clb_Bpow-4)//16) >= 1]
            assert clb_Bpow >= 4 # == ceil_log2(3**2)
            if 0b00:
                print((clb_Bpow, flbN, flbN_, flbN-flbN_))
            if not flbN_<<2 <= flbN:
                break


        elif not (B==3 and n0_ <= 31):
            raise logic-err #since 相同条件在上面分支
            #
            # 精确计算floor_log_Bpow_n没有意义，见上面:粗略计算
            # 见下面:[[clb_Bpow==2] ==>> [[B==3][3 <= n0_ <= 31]]]
            #   ==>> [[not$ [B==3][3 <= n0_ <= 31]] ==>> [not$ [clb_Bpow==2]]]
            assert clb_Bpow >= 3
            # eval [floor_log_Bpow_n := floor_log_(Bpow, n0_)]
            q_pow = flbN//clb_Bpow
            q1_pow = flbN//(clb_Bpow-1)
            q11_pow = (1+flbN)//(clb_Bpow-1)
            # bug:[q_pow <= floor_log_Bpow_n <= q1_pow]
            # [q_pow <= floor_log_Bpow_n <= q11_pow]
            #(q1_pow, r1_pow) = divmod(flbN, (clb_Bpow-1))
            # [flbN == q1_pow*(clb_Bpow-1) + r1_pow == q1_pow*clb_Bpow + (r1_pow-q1_pow)]
            # [q1_pow + (r1_pow-q1_pow)//clb_Bpow == q_pow]
            #
            # [clb_Bpow >= clbB >= 2]
            # [flbN <= clb_Bpow**2]
            #
            # [q1_pow = flbN//(clb_Bpow-1) <= clb_Bpow**2//(clb_Bpow-1) <= if clb_Bpow == 2 then 4 else clb_Bpow+1]
            # [clb_Bpow >= 3]
            # [0 <= q1_pow <= (clb_Bpow+1)]
            # [0 <= r1_pow < (clb_Bpow-1)]
            # [-(clb_Bpow+1) <= r1_pow-q1_pow < (clb_Bpow-1)]
            # [-2 <= (r1_pow-q1_pow)//clb_Bpow <= 0]
            # [q1_pow + (r1_pow-q1_pow)//clb_Bpow == q_pow]
            # [0 <= q1_pow-q_pow <= 2]
            assert 0 <= q1_pow-q_pow <= 2
            #
            assert clb_Bpow >= 4 # == ceil_log2(3**2)
            #(q11_pow, r11_pow) = divmod(1+flbN, (clb_Bpow-1))
            # [flbN == q11_pow*(clb_Bpow-1) + r11_pow-1 == q11_pow*clb_Bpow + (r11_pow-q11_pow-1)]
            # [q11_pow + (r11_pow-q11_pow-1)//clb_Bpow == q_pow]
            #
            # [q11_pow = (1+flbN)//(clb_Bpow-1) <= (1+clb_Bpow**2)//(clb_Bpow-1) <= if clb_Bpow == 2 then 5 elif clb_Bpow==3 then 5 else clb_Bpow+1]
            # [clb_Bpow >= 4]
            # [0 <= q11_pow <= (clb_Bpow+1)]
            # [0 <= r11_pow < (clb_Bpow-1)]
            # [-(clb_Bpow+2) <= r11_pow-q11_pow-1 < (clb_Bpow-2)]
            # [-2 <= (r11_pow-q11_pow-2)//clb_Bpow <= 0]
            # [q11_pow + (r11_pow-q11_pow-2)//clb_Bpow == q_pow]
            # [0 <= q11_pow-q_pow <= 2]
            assert 0 <= q11_pow-q_pow <= 2
            #
            # bug:[q_pow <= floor_log_Bpow_n <= q1_pow]
            # [q_pow <= floor_log_Bpow_n <= q11_pow]
            if q_pow == q11_pow:
                floor_log_Bpow_n = q_pow
            else:
                Bpowpow = Bpow**(q_pow+1)
                if n0_ < Bpowpow:
                    floor_log_Bpow_n = q_pow+0
                elif q_pow+1 == q11_pow or n0_ == Bpowpow or n0_ < Bpowpow*Bpow:
                    floor_log_Bpow_n = q_pow+1
                else:
                    floor_log_Bpow_n = q_pow+2
            #assert Bpow**floor_log_Bpow_n <= n0_ < Bpow**(floor_log_Bpow_n+1)
            n_ = n0_//Bpow**floor_log_Bpow_n
            assert 1 <= n_ < Bpow
            e_ += exp4Bpow*floor_log_Bpow_n
            if 0b00:
                flbN_ = floor_log2(n_)
                print((clb_Bpow, flbN, flbN_, flbN-flbN_))


        else:
            raise logic-err #since [(q1-q > 32)] ==>> [n>32]
            ############
            assert (B==3 and n0_ <= 31)
            n_ = n0_
            e_ += 0
            break
        if 0:
            #推导自:[clb_Bpow==2]
          if clb_Bpow == 2:
            assert clb_Bpow == 2
            # [(1<<(clbB-1)) < B < (1<<clbB)]
            assert B == 3
            # [flbN >= (clbB-1) >= 1]
            assert 1 <= flbN <= 4
            # [n0_ >= B]
            assert 3 <= n0_ <= 31
            n_ = n0_
            e_ += 0
            # [[clb_Bpow==2] ==>> [[B==3][3 <= n0_ <= 31]]]
            # [[not$ [B==3][3 <= n0_ <= 31]] ==>> [not$ [clb_Bpow==2]]]
        ###########################
        ###########################
        ###########################
        flbN = floor_log2(n_)
        q = flbN//clbB
        q1 = flbN//(clbB-1)
    else:
        pass
    #end-while
    (n_, e_)



    if 0:
        e = 0
        _n = n
    else:
        e = e_
        _n = n_
    q = q0 = 1<<3
    while not (q < q0):
        flbN = floor_log2(_n)
        q = flbN//clbB
        _n //= B**q
        if not _n >= 1: raise logic-err
        e += q
    e += _1_floor_log_(B, _n)
    return e


def _1_floor_log_(B, n, /):
    #assert B >= 2
    #assert n >= 1
    #if n < B: return 0
    B_pows = [B] # [B**2**i | [i :<- [0..]]]
    while not (n < B_pows[-1]):
        B_pows.append(B_pows[-1]**2)
    B_pows.pop()
    e = 0
    while B_pows:
        last = B_pows.pop()
        if not (n < last):
            n //= last
            e |= 1<<len(B_pows)
    return e
if 0:
    _1_floor_log_.__doc__ = fr'''
>>> floor_log_ = _1_floor_log_
{floor_log_.__doc__!s}

#'''

if 0:
    _1_floor_log_.__doc__ = floor_log_.__doc__.replace('floor_log_', '_1_floor_log_')

def _t1__floor_log_():
    for B in range(2,20):
        for n in range(1,10_0001):
            floor_log_(B, n)
def _t2__floor_log_():
    for B in range(2,20):
        for e in range(0,1001):
            floor_log_(B, 7**e)
    floor_log_(3, 7**2_0000)



def __():
    if 0 and __name__ == "__main__":
        _t2__floor_log_()
        _t1__floor_log_()

__all__
from seed.math.floor_ceil_tools.fc_log import ceil_log2_div, floor_log2_div
from seed.math.floor_ceil_tools.fc_log import imay_floor_log2, extended_imay_floor_log2, count_num_high_same_bits_of_two_uints
from seed.math.floor_ceil_tools.fc_log import ceil_log_, floor_log_
from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2, floor_ceil_log_, floor_ceil_log2
from seed.math.floor_ceil_tools.fc_log import floor_log2_kth_root_, ceil_log2_kth_root_, floor_log2_sqrt, ceil_log2_sqrt
from seed.math.floor_ceil_tools.fc_log import *
