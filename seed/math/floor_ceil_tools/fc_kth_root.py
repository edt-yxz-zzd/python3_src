#__all__:goto
r'''[[[
e ../../python3_src/seed/math/floor_ceil_tools/fc_kth_root.py

seed.math.floor_ceil_tools.fc_kth_root
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil_tools.fc_kth_root -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil_tools.fc_kth_root:__doc__ -ht # -ff -df
#######

[[
move_from:
    e ../../python3_src/seed/math/floor_ceil.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root   @f
]]]'''#'''
__all__ = r'''
floor_sqrt
ceil_sqrt
floor_kth_root_
ceil_kth_root_

floor_lshift_kth_root_
floor_lshift_sqrt_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.math.floor_ceil_tools.fc_log import floor_log2_kth_root_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...



def ceil_sqrt(n, /):
    fsqrtN = floor_sqrt(n)
    csqrtN = fsqrtN if (n==fsqrtN**2) else 1+fsqrtN
    assert csqrtN==0 if n==0 else (csqrtN-1)**2 < n <= csqrtN**2
    return csqrtN
def floor_sqrt(n, /):
    r'''[[[
    [floor_sqrt(n) =[def]= floor(sqrt(n))]
    # O(log2(n)**2)


    [n>=0]
[n>=1]:
    #floor_sqrt不使用 牛顿迭代，但感觉本质一样
    [(q,r) := divmod(n, 2**(2*e))]
    [fsqrtN := floor_sqrt(n)]
    [fsqrtQ := floor_sqrt(q)]
    #由(e,q,r,fsqrtQ)求fsqrtN
    [fsqrtQ**2 <= q < (fsqrtQ+1)**2]
    [n == q*2**(2*e) + r >= q*2**(2*e) >= (fsqrtQ*2**e)**2]
    [n == q*2**(2*e) + r < (q+1)*2**(2*e) <= ((1+fsqrtQ)*2**e)**2]
    [(fsqrtQ*2**e) <= fsqrtN < ((1+fsqrtQ)*2**e)]
    [fsqrtQ == fsqrtN//2**e]
    [dd := fsqrtN - (fsqrtQ*2**e)]
    [0 <= dd < 2**e]
    [dd == fsqrtN%2**e]
    [fsqrtN == (fsqrtQ*2**e+dd)]
    #由(e,q,r,fsqrtQ)先求dd再求fKrtN

    [D := n -(fsqrtQ*2**e)**2]
    [D == n -(fsqrtQ*2**e)**2 == (q*2**(2*e) + r) -(fsqrtQ*2**e)**2 == ((q-fsqrtQ**2)*2**(2*e) + r)]

    [n >= fsqrtN**2 == (fsqrtQ*2**e+dd)**2]
    [D == n -(fsqrtQ*2**e)**2 >= (2*fsqrtQ*2**e+dd)*dd == (2*fsqrtQ+dd/2**e)*2**e*dd]
    [floor(2*fsqrtQ+dd/2**e) == (2*fsqrtQ)]

    [n < (1+fsqrtN)**2 == (fsqrtQ*2**e+dd+1)**2]
    [D == n -(fsqrtQ*2**e)**2 < (2*fsqrtQ*2**e+(dd+1))*(dd+1) == (2*fsqrtQ+(dd+1)/2**e)*2**e*(dd+1)]
    [ceil(2*fsqrtQ+(dd+1)/2**e) == (2*fsqrtQ+1)]

    [(2*fsqrtQ)*2**e*dd <= D < (2*fsqrtQ+1)*2**e*(dd+1)]
    [dd <= D/((2*fsqrtQ)*2**e)]
    [dd+1 > D/((2*fsqrtQ+1)*2**e)]
    [-1 +D/2**e /(2*fsqrtQ+1) < dd <= D/2**e /(2*fsqrtQ)]
    [D//2**e //(2*fsqrtQ+1) <= dd <= D//2**e //(2*fsqrtQ)]

    [0 <= D//2**e <= (2*fsqrtQ+1)**2-2]:
        #view others/数学/divmod加速.txt
        !![[d>=2] -> [-(d-1) <= n <= d**2-2] -> [0 <= n//(d-1) - n//d <= 1]]
        #   [outer_txt.n := D//2**e]
        #   [outer_txt.d := (2*fsqrtQ+1)]
        [upper_dd := D//2**e //(2*fsqrtQ)]
        [-1 +upper_dd <= dd <= upper_dd]

        [(2*fsqrtQ+1)**2-2
        >= D//2**e
        == ((q-fsqrtQ**2)*2**(2*e) + r)//2**e
        == ((q-fsqrtQ**2)*2**e + r//2**e)
        ]
        [(q-fsqrtQ**2) < (fsqrtQ+1)**2 -fsqrtQ**2 == 2*fsqrtQ+1]
        [(q-fsqrtQ**2) <= (2*fsqrtQ)]
        #充分条件:
        [(2*fsqrtQ+1)**2-2 >= D//2**e]
        <<== [(2*fsqrtQ+1)**2-2 >= ((2*fsqrtQ)*2**e + r//2**e)]
        <<== [(2*fsqrtQ+1)**2-2 >= ((2*fsqrtQ)*2**e + 2**e-1)]
        <<== [(2*fsqrtQ+1)**2 >= (1 + (2*fsqrtQ+1)*2**e)]
        <<== [(2*fsqrtQ+1) >= (1/(2*fsqrtQ+1) + 2**e)]
        <<== [(2*fsqrtQ+1) >= (1 + 2**e)]
        <<== [fsqrtQ >= (2**(e-1))]
        <<== [floor_log2(q)//2 == floor_log2_sqrt(q) == floor_log2(sqrt(q)) == floor_log2(fsqrtQ) >= (e-1)]
        <<== [floor_log2(q) >= 2*(e-1)]
        !![(q,r) := divmod(n, 2**(2*e))]
        !![q >= 1] # ==>> [2*e <= floor_log2(n)]
        <<== [2*e <= floor_log2(n) == floor_log2(q)+2*e >= 2*(e-1)+2*e == 4*e-2]
        <<== [floor_log2(n) >= 4*e-2][e >= 1]
        <<== [1 <= e <= (floor_log2(n)+2)//4][n>=4]
            # 2**e 占 约1/4
            # 2**(2*e) 占 约1/2
            # q 占 约1/2
            # 由q到n(由fsqrtQ到fsqrtN)，比特数大约翻倍
    [flbN := floor_log2(n)]
    [1 <= e <= (flbN+2)//4][n>=4]:
        [0 <= D//2**e <= (2*fsqrtQ+1)**2-2]
        #dd只有2个可能的取值
        [-1 +D//2**e //(2*fsqrtQ) <= dd <= D//2**e //(2*fsqrtQ)]
        [fsqrtN == (fsqrtQ*2**e+dd)]
        #通过dd求fsqrtN
        [upper_dd := D//2**e //(2*fsqrtQ)]
        [upper_dd ==  ((q-fsqrtQ**2)*2**e + r//2**e)//(2*fsqrtQ)]

        [n >= 2**(4*e-2) == 4**(2*e-1)]
        [[1 <= (flbN+2)//4] -> [n>=4]]
        [[2 <= (flbN+2)//4] -> [n>=64]]
        [[3 <= (flbN+2)//4] -> [n>=1024]]


#>>> from seed.debug.print_err import print_err
>>> from math import isqrt
>>> floor_sqrt(0)
0
>>> floor_sqrt(1)
1
>>> floor_sqrt(2)
1
>>> floor_sqrt(3)
1
>>> floor_sqrt(4)
2
>>> floor_sqrt(5)
2
>>> floor_sqrt(6)
2
>>> floor_sqrt(7)
2
>>> floor_sqrt(8)
2
>>> floor_sqrt(9)
3
>>> for n in range(200):
...     #print_err(n)
...     if not floor_sqrt(n) == isqrt(n):
...         print(n, floor_sqrt(n), isqrt(n), floor_sqrt(n)**2, isqrt(n)**2)



    #]]]'''
    assert n >= 0
    if 0:
        if n < 4:
            fsqrtN = 0 if n==0 else 1
    while 1: # not loop indeed, just to use "break" instead of "return"
        if n == 0:
            fsqrtN = 0
            break

        # [n >= 1]
        flbN = floor_log2(n)
        # [flbN >= 0]
        if 0 == flbN&1 and n == (1<<flbN):
            # perfect square
            # [n==2**(2*e)]
            fsqrtN = (1<<(flbN>>1))
            break
        assert n >= 2
        # [n >= 2][flbN >= 1][flbN == floor_log2(n)]
        ls = [(n, flbN)]
            # [@[(n, flbN) :<- ls] -> [[n >= 1][flbN >= 0][flbN == floor_log2(n)]]]
            #
        while 1:
            (n, flbN) = ls[-1]
            # [n >= 1][flbN >= 0][flbN == floor_log2(n)]

            #bug:if flbN == 1:break
            #if n < 4:break
            if flbN < 2:
                # [1 <= n < 4][0 <= flbN < 2][flbN == floor_log2(n)]
                # [1 <= ls[-1][0] < 4]
                # [0 <= ls[-1][1] < 2]
                break
            # [n >= 4][flbN >= 2]
            e = (flbN+2)//4
            # [e >= 1]
            # [4 <= 4*e <= flbN+2]
            _2e = e << 1
            # [2 <= 2*e <= (flbN+2)/2 <= flbN]
            # [4 == 2**2 <= 2**(2*e) <= 2**flbN <= n]
            q = n >> _2e
            # [q == n//2**(2*e) >= 1]
            # [q >= 1]
            flbQ = flbN -_2e
            # [flbQ >= 0]
            # !! [flbN == floor_log2(n)]
            # [flbQ == flbN -2*e == floor_log2(n) -2*e == floor_log2(n//2**(2*e)) == floor_log2(q)]
            # [flbQ == floor_log2(q)]
            #assert q >= 1
            #assert flbQ >= 0
            ls.append((q, flbQ))
                # [q >= 1][flbQ >= 0][flbQ == floor_log2(q)]

            ######################
            # !! [e := (flbN+2)//4]
            # !! [flbQ := flbN -2*e]
            # [flbQ == flbN -(flbN+2)//4*2]
            # [flbQ >= flbN -(flbN+2)/4*2 == flbN/2 -1]
            # [flbQ <= flbN -(flbN+2-3)/4*2 == flbN/2 +1/2]
            # [flbN >= 2*flbQ-1]
            # [flbN+1 >= 2*flbQ]
            # [(flbN+1)/2 >= flbQ]
            # [flbQ <= ceil_div(flbN,2)]
            ######################
        #end-while 1:
        # [1 <= ls[-1][0] < 4]
        # [0 <= ls[-1][1] < 2]
        # [[i :<- [0..=len(ls)-2]] -> [(q, flbQ) := ls[i]] -> [(n, flbN) := ls[i+1]] -> [[flbQ <= ceil_div(flbN,2)][flbN >= 2*flbQ-1]]]
        # [O(len(ls)) == O(log2(flbN))]

        (n, flbN) = ls.pop()
        # [1 <= n < 4][0 <= flbN < 2][flbN == floor_log2(n)]
        assert 1 <= n < 4
        assert 0 <= flbN < 2
        assert flbN == floor_log2(n)

        fsqrtN = 1
        while ls:
            (q, flbQ) = (n, flbN)
            fsqrtQ, fsqrtN = fsqrtN, None
            (n, flbN) = ls.pop()
            _2e = flbN -flbQ
            e = _2e >> 1
            #r = n & ((1<<_2e)-1)
            #####
            if 0:
                # [D == n -(fsqrtQ*2**e)**2 == (q*2**(2*e) + r) -(fsqrtQ*2**e)**2 == ((q-fsqrtQ**2)*2**(2*e) + r)]
                D = n -((fsqrtQ**2) << _2e)
                # [upper_dd := D//2**e //(2*fsqrtQ)]
                upper_dd = (D >> (e+1)) //fsqrtQ
            else:
                D_e1 = (n>>(e+1)) -((fsqrtQ**2) << (e-1))
                upper_dd = D_e1//fsqrtQ
                # ~ O((flbQ/2)**2)
                # ~ O((flbN/4)**2)
                # ~ O(flbN**2)
                '...+O(flbN**2)'

            # [fsqrtN == (fsqrtQ*2**e+dd)]
            upper_fsqrtN = (fsqrtQ<<e)+upper_dd
            # EVAL(upper_fsqrtN**2) ~ O((flbN/2)**2)
            '...+O(flbN**2)'
            if n < upper_fsqrtN**2:
                fsqrtN = upper_fsqrtN -1
            else:
                fsqrtN = upper_fsqrtN
            fsqrtN
        #end-while ls # ls.pop until []
        # O(while ls) ~= O(sum flbN**2 {flbN})
        # !! [O(len(ls)) == O(log2(flbN))]
        # ~= O(sum (2**i)**2 {i :<- [0..=log2(flbN)]})
        # ~<= O((sum 2**i {i :<- [0..=log2(flbN)]})**2)
        # ~<= O((2**log2(flbN)) **2)
        # ~<= O(flbN **2)
        '...+O(flbN**2)'
        fsqrtN
        break
    #end-main-while 1: # not loop indeed, just to use "break" instead of "return"
    assert fsqrtN**2 <= n < (1+fsqrtN)**2
    return fsqrtN

def _t1__floor_sqrt():
    for n in range(10_0001):
        floor_sqrt(n)
def _t2__floor_sqrt():
    for i in range(1001):
        floor_sqrt(2**i)
    for i in range(1001):
        floor_sqrt(5**i)
    for i in range(10_0000, 10_0101):
        floor_sqrt(7**i)
if 0 and __name__ == "__main__":
    _t2__floor_sqrt()
    _t1__floor_sqrt()


def _iter_partial_floor_kth_root__bisearch_(k, n, /):
    'k -> n -> Iter<(partial_lead_bits4fKrtN, num_remain_bits)> # [partial_lead_bits4fKrtN == fKrtN//2**num_remain_bits][num_remain_bits <- reversed[0..=floor_log2_fKrtN]]'
    #bisearch, one bit per round #bisection
    assert k >= 2
    assert n >= 1
    flbN = floor_log2(n)
    #floor_log2_fKrtN = floor_log2_kth_root_(k, n)
    #floor_log2_fKrtN = flbN//k
    (floor_log2_fKrtN, flbQ0) = divmod(flbN, k)
    fKrtQ0 = 1
    num_remain_bits = floor_log2_fKrtN

    yield (fKrtQ0, num_remain_bits)
    for k_e in reversed(range(0, flbN-flbQ0, k)):
        n1 = n>>k_e
        fKrtQ1 = (fKrtQ0<<1)^1
        if n1 < fKrtQ1**k:
            fKrtQ1 ^= 1
        # EVAL(fKrtQ1**k)
        # ~O(last-square)
        # ~O(log2(fKrtQ1**k)**2)
        # ~O(k**2 * log2(fKrtQ1)**2)
        # ~O(k**2 * (loop-round-idx)**2)
        #####
        fKrtQ0 = fKrtQ1
        num_remain_bits -= 1
        yield (fKrtQ0, num_remain_bits)
    assert num_remain_bits == 0
    assert floor_log2(fKrtQ0) == floor_log2_fKrtN
    fKrtN = fKrtQ0
    assert fKrtN**k <= n < (fKrtN+1)**k
    return

def ceil_kth_root_(k, n, /):
    assert k >= 1
    assert n >= 0
    if n == 0:
        return 0
    return 1+floor_kth_root_(k, n-1)
def floor_kth_root_(k, n, /):
    r'''[[[
    [kth_root_(k,n) =[def]= n**(1/k)]
    [floor_kth_root_(k,n) =[def]= floor(kth_root_(k,n))]
    [floor_sqrt === floor_kth_root_<2>]

    ######################
    let [mmm:=min{k*log2(k), log2(n)}]
    let [lbN:=log2(n)][lblbN:=log2(log2(n))]
    let [lbK:=log2(k)]
    ######################
    ~ O(mmm**3 /k + (lbN -mmm)**2)
    ######################
    ~ [0 <= lbN < k]:O(1)
    ~ [k <= lbN < k*lbK]:O(lbN**3 /k)
    ~ worst[lbN == k*lbK][k==lbN/lblbN]:O(lbN**2 *lblbN)
    ~ [k*lbK < lbN < k*lbK**(3/2)][lbN/lblbN**(3/2) < k < lbN/lblbN]:O(k**2 *lbK**3)
    ~ [lbN > k*lbK**(3/2)]:O(lbN**2)
    ######################
    [lbN == k*lbK] => [k==lbN/lblbN]
    [lbN == k*lbK**(3/2)] => [k==lbN/lblbN**(3/2)]
    [k*lbK < lbN < k*lbK**(3/2)] => [lbN/lblbN**(3/2) < k < lbN/lblbN]
    ######################

    [k>=1][n>=0]
[k>=2][e>=1][n>=1]:
    # 前提由来:见下面:不必需囗前提条件:[[k>=2][e>=1] -> [(upper_D1_dd1-lower_D_dd) >= 1]]
    #
    [(q,r) := divmod(n, 2**(k*e))]
    [fKrtN := floor_kth_root_(k,n)]
    [fKrtQ := floor_kth_root_(k,q)]
    #由(e,q,r,fKrtQ)求fKrtN
    [fKrtQ**k <= q < (fKrtQ+1)**k]
    [n == q*2**(k*e) + r >= q*2**(k*e) >= (fKrtQ*2**e)**k]
    [n == q*2**(k*e) + r < (q+1)*2**(k*e) <= ((1+fKrtQ)*2**e)**k]
    [(fKrtQ*2**e) <= fKrtN < ((1+fKrtQ)*2**e)]
    [fKrtQ == fKrtN//2**e]
    [dd := fKrtN - (fKrtQ*2**e)]
    [0 <= dd < 2**e]
    [dd == fKrtN%2**e]
    [fKrtN == (fKrtQ*2**e+dd)]
    #由(e,q,r,fKrtQ)先求dd再求fKrtN

    [f(x) := ((A+x)*k - A**k)/x][x > 0]:
        [Df(x)
        == k*(A+x)**(k-1)/x -((A+x)**k - A**k)/x**2
        == (k*x*(A+x)**(k-1) -((A+x)**k - A**k))/x**2
        == (k*x*(sum{choose_(k-1;i)*A**(k-1-i)*x**i | [i :<- [0..=k-1]]}) -(sum{choose_(k;i)*A**(k-i)*x**i | [i :<- [1..=k]]}))/x**2
        == ((sum{k*choose_(k-1;i)*A**(k-(1+i))*x**(i+1) | [i :<- [0..=k-1]]}) -(sum{choose_(k;i)*A**(k-i)*x**i | [i :<- [1..=k]]}))/x**2
        == ((sum{k*choose_(k-1;j-1)*A**(k-j)*x**j | [j :<- [1..=k]]}) -(sum{choose_(k;j)*A**(k-j)*x**j | [j :<- [1..=k]]}))/x**2
        == (sum{(k*choose_(k-1;j-1)*A**(k-j)*x**j - choose_(k;j)*A**(k-j)*x**j) | [j :<- [1..=k]]})/x**2
        == (sum{(k*choose_(k-1;j-1) - choose_(k;j))*A**(k-j)*x**j | [j :<- [1..=k]]})/x**2
        == (sum{(j*choose_(k;j) - choose_(k;j))*A**(k-j)*x**j | [j :<- [1..=k]]})/x**2
        == (sum{(j-1)*choose_(k;j)*A**(k-j)*x**j | [j :<- [1..=k]]})/x**2
        >= 0
        ]
        !![x>0]
        [f(x)单调递增]
        [f(x) >= limit[f(x) | x --> 0+] == D_<x>((A+x)*k - A**k){x:=0} == (k*(A+x)**(k-1)){x:=0} == (k*A**(k-1))]

    [D := n -(fKrtQ*2**e)**k]
    [D == n -(fKrtQ*2**e)**k == (q*2**(k*e) + r) -(fKrtQ*2**e)**k == ((q-fKrtQ**k)*2**(k*e) + r)]

    [E := 2**e]
    [n >= fKrtN**k == (fKrtQ*E+dd)**k]
    [D == n -(fKrtQ*E)**k
    >= (fKrtQ*E+dd)**k -(fKrtQ*E)**k
    == (k*(fKrtQ*E)**(k-1)*dd +sum{choose_(k,i) *(fKrtQ*E)**i *dd**(k-i) | [i <- [0..=k-2]]})
    == (k*(fKrtQ*E)**(k-1) +sum{choose_(k,i) *(fKrtQ*E)**i *dd**(k-1-i) | [i <- [0..=k-2]]}) *dd
        [>= (k*(fKrtQ*E)**(k-1) +sum{choose_(k,i) *(fKrtQ*E)**i *1**(k-1-i) | [i <- [0..=k-2]]}) *dd
            # 括号内dd用1代替，因为dd==0时括号外的dd起作用
        == (k*(fKrtQ*E)**(k-1) +sum{choose_(k,i) *(fKrtQ*E)**i *1**(k-i) | [i <- [0..=k-2]]}) *dd
        == ((fKrtQ*E+1)**k - (fKrtQ*E)**k) *dd
        ]
    == (k*fKrtQ**(k-1) +sum{choose_(k,i) *fKrtQ**i *(dd/E)**(k-1-i) | [i <- [0..=k-2]]}) *E**(k-1) *dd
    ]
    !![0 <= dd < E]
    !![f(x)单调递增]
    [D >= ((fKrtQ*E+dd)**k - (fKrtQ*E)**k) == if dd==0 then 0 else ((fKrtQ*E+dd)**k - (fKrtQ*E)**k)/dd *dd >= ((fKrtQ*E+1)**k - (fKrtQ*E)**k)/1 *dd]
    [D >= ((fKrtQ*E+1)**k - (fKrtQ*E)**k) *dd]


    [n < (1+fKrtN)**k == (fKrtQ*E+dd+1)**k]
    [D == n -(fKrtQ*E)**k
    < (fKrtQ*E+dd+1)**k -(fKrtQ*E)**k
    == (k*(fKrtQ*E)**(k-1)*(dd+1) +sum{choose_(k,i) *(fKrtQ*E)**i *(dd+1)**(k-i) | [i <- [0..=k-2]]})
    == (k*(fKrtQ*E)**(k-1) +sum{choose_(k,i) *(fKrtQ*E)**i *(dd+1)**(k-1-i) | [i <- [0..=k-2]]}) *(dd+1)
    == (k*fKrtQ**(k-1) +sum{choose_(k,i) *fKrtQ**i *((dd+1)/E)**(k-1-i) | [i <- [0..=k-2]]}) *E**(k-1) *(dd+1)
    ]
    [D < ((fKrtQ*E+dd+1)**k - (fKrtQ*E)**k)
    == ((fKrtQ*E+dd+1)**k - (fKrtQ*E)**k)/(dd+1) *(dd+1)
    !![0 <= dd < E]
    !![f(x)单调递增]
    <= ((fKrtQ*E+E)**k - (fKrtQ*E)**k)/E *(dd+1)
    == ((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1) *(dd+1)
    ]
    [D < ((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1) *(dd+1)]
    [D <= -1 +((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1) *(dd+1)]

    [lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
    [upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))]
    [lower_D_dd *dd <= D < D+1 <= upper_D1_dd1 *(dd+1)]


    [dd <= D/lower_D_dd]
    [dd+1 > D/upper_D1_dd1]
    [-1 +D/upper_D1_dd1 < dd <= D/lower_D_dd]
        #true_div
    [-1 +D//upper_D1_dd1 < dd <= D//lower_D_dd]
        #floor_div
    [D//upper_D1_dd1 <= dd <= D//lower_D_dd]

    [lower_dd := D//upper_D1_dd1]
    [upper_dd := D//lower_D_dd]
    [lower_dd <= dd <= upper_dd]

    #view others/数学/divmod加速.txt
    !![[[d>=1][d_>=1][u<=v]] -> [[u*d*d_ -(d-1) <= (d-d_)*n <= (d_-1) +v*d*d_] -> [u <= (n//d_ - n//d) <= v]]]
    #   [outer_txt.n := D]
    #   [outer_txt.d := upper_D1_dd1]
    #   [outer_txt.d_ := lower_D_dd]
    #   [outer_txt.dd := .d - ._d = (upper_D1_dd1-lower_D_dd)]
    #

    [[0 <= (upper_D1_dd1-lower_D_dd)*D <= upper_D1_dd1 *lower_D_dd +(lower_D_dd-1)] -> [upper_dd-lower_dd == (D//lower_D_dd - D//upper_D1_dd1) <- {0,1}][dd <- {D//lower_D_dd,D//lower_D_dd-1}]]
        # [(u,v) := (0,1)]
        # used when [(upper_D1_dd1-lower_D_dd) >= 0]

    [[-upper_D1_dd1 *lower_D_dd -(upper_D1_dd1-1) <= (upper_D1_dd1-lower_D_dd)*D <= 0] -> [upper_dd-lower_dd == (D//lower_D_dd - D//upper_D1_dd1) <- {-1,0}]]
        # [(u,v) := (-1,0)]
        # used when [(upper_D1_dd1-lower_D_dd) <= 0]

    !![lower_dd <= dd <= upper_dd]
    [upper_dd-lower_dd >= 0]
    [[-upper_D1_dd1 *lower_D_dd -(upper_D1_dd1-1) <= (upper_D1_dd1-lower_D_dd)*D <= 0] -> [dd==upper_dd==lower_dd == D//lower_D_dd == D//upper_D1_dd1]]

    !![D >= 0]
    * [(upper_D1_dd1-lower_D_dd) > 0]:
        [[D <= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)] -> [dd <- {D//lower_D_dd,D//lower_D_dd-1}]]

    * [(upper_D1_dd1-lower_D_dd) < 0]:
        [[D <= (upper_D1_dd1 *lower_D_dd +(upper_D1_dd1-1))//(-(upper_D1_dd1-lower_D_dd))] -> [dd == D//lower_D_dd]]
    * [(upper_D1_dd1-lower_D_dd) == 0]:
        [dd == D//lower_D_dd]

    #综上:
    [[D <= (upper_D1_dd1 *lower_D_dd +(min(upper_D1_dd1,lower_D_dd)-1))//max(1,abs(upper_D1_dd1-lower_D_dd))] -> [dd <- {D//lower_D_dd,D//lower_D_dd-1}]]






    # 下面寻找满足 上面 命题 的 充分条件
    [[必需:前提条件
    ??? [lower_D_dd >= 1] ???
        # <<== [outer_txt._d >= 1]
    ??? [upper_D1_dd1 >= 1] ???
        # <<== [outer_txt.d >= 1]
    ]]

    [[不必需:前提条件
    ??? [upper_D1_dd1 - lower_D_dd > 0] ???
        # <<== [outer_txt.dd > 0]
    ??? [1 <= lower_D_dd < upper_D1_dd1] ???
    ]]

    [[[证明:必需:前提条件[lower_D_dd >= 1][upper_D1_dd1 >= 1]
    !![lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
    [k == 1]:
        [lower_D_dd == 1]
    !![k >= 2]
    [lower_D_dd >= k*(fKrtQ*E)**(k-1)+1]
    [fKrtQ >= 0][e >= 0]:
        [lower_D_dd >= 1]
    [fKrtQ >= 1][e >= 1]:
        [lower_D_dd >= 2*(1*2**1)**(2-1)+1 == 5]
    [lower_D_dd >= 1] # for [k>=1]

    !![upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))]
    [k == 1]:
        [upper_D1_dd1 == E**(k-1) == 1]
    !![k >= 2]
    [upper_D1_dd1 >= ((k*fKrtQ**(k-1)+1)*E**(k-1))]
    [upper_D1_dd1 >= 1] # for [k>=1]
    ]]]

    [[证明:不必需:前提条件[upper_D1_dd1 - lower_D_dd > 0]
    !![D//upper_D1_dd1 <= dd <= D//lower_D_dd]
    [D//upper_D1_dd1 <= D//lower_D_dd]

    !![lower_D_dd *dd <= D < D+1 <= upper_D1_dd1 *(dd+1)]
    [lower_D_dd *dd < upper_D1_dd1 *(dd+1)]
    !![0 <= dd < E]
    [lower_D_dd *(E-1) < upper_D1_dd1 *E]

    !![lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
    !![upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))]
    [(upper_D1_dd1-lower_D_dd) #==outer_txt.dd
    == (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1)) -((fKrtQ*E+1)**k - (fKrtQ*E)**k)
    == (fKrtQ+1)**k*E**(k-1) -(fKrtQ)**k*E**(k-1) -(fKrtQ*E+1)**k +(fKrtQ*E)**k
    == (fKrtQ+1)**k*E**(k-1) -(fKrtQ*E+1)**k +(fKrtQ)**k*E**(k-1)*(E-1)
    ]
    [g(k) := (fKrtQ+1)**k*E**(k-1) -(fKrtQ*E+1)**k +(fKrtQ)**k*E**(k-1)*(E-1)]
    [g(k) == (upper_D1_dd1-lower_D_dd)]

    [g(1)
    == (fKrtQ+1)**1*E**(1-1) -(fKrtQ*E+1)**1 +(fKrtQ)**1*E**(1-1)*(E-1)
    == (fKrtQ+1) -(fKrtQ*E+1) +(fKrtQ)*(E-1)
    == 0
    ]
    [g(2)
    == (fKrtQ+1)**2*E**(2-1) -(fKrtQ*E+1)**2 +(fKrtQ)**2*E**(2-1)*(E-1)
    == (fKrtQ+1)**2*E -(fKrtQ*E+1)**2 +(fKrtQ)**2*E*(E-1)
    == (fKrtQ**2*E+2*fKrtQ*E+E) -(fKrtQ**2*E**2 +2*fKrtQ*E +1) +(fKrtQ**2*E**2-fKrtQ**2*E)
    == E-1
    == 2**e-1
    >= e
    >= 0
    ]

    [E*g(k) == (fKrtQ*E+E)**k +(fKrtQ*E)**k*(E-1) -E*(fKrtQ*E+1)**k]

    [E*g(k)
    == 1*(fKrtQ*E+1+(E-1))**k +(E-1)*(fKrtQ*E+1-1)**k -E*(fKrtQ*E+1)**k
    == 1*sum{(choose_(k;i)*(fKrtQ*E+1)**i*(E-1)**(k-i)) | [i :<-[0..=k]]} +(E-1)*sum{(choose_(k;i)*(fKrtQ*E+1)**i*(-1)**(k-i)) | [i :<-[0..=k]]} -E*(fKrtQ*E+1)**k
    == sum{(choose_(k;i)*(fKrtQ*E+1)**i*((E-1)**(k-i)+(E-1)*(-1)**(k-i))) | [i :<-[0..=k]]} -E*(fKrtQ*E+1)**k
    !![k>=0]
    == sum{(choose_(k;i)*(fKrtQ*E+1)**i*((E-1)**(k-i)+(E-1)*(-1)**(k-i))) | [i :<-[0..<k]]} +(choose_(k;k)*(fKrtQ*E+1)**k*((E-1)**(k-k)+(E-1)*(-1)**(k-k))) -E*(fKrtQ*E+1)**k
    == sum{(choose_(k;i)*(fKrtQ*E+1)**i*((E-1)**(k-i)+(E-1)*(-1)**(k-i))) | [i :<-[0..<k]]} +(1*(fKrtQ*E+1)**k*(1+(E-1)*1)) -E*(fKrtQ*E+1)**k
    == (E-1)*sum{(choose_(k;i)*(fKrtQ*E+1)**i*((E-1)**(k-1-i)+(-1)**(k-i))) | [i :<-[0..<k]]}
        [[
        * [k>=0][e>=0]:[
            [E==2**e>=1]
            [... >= (E-1)*sum{(choose_(k;i)*(fKrtQ*E+1)**i*(1**(k-1-i)-1)) | [i :<-[0..<k]]}
            == 0
            ]
        ]
        * [k>=2][e>=1]:[
            [E==2**e>=2]
            [... >= (2-1)*sum{(choose_(k;i)*(fKrtQ*2+1)**i*((2-1)**(k-1-i)+(-1)**(k-i))) | [i :<-[0..<k]]}
            >= (2-1)*sum{(choose_(k;i)*(fKrtQ*2+1)**i*((2-1)**(k-1-i)+(-1)**(k-i))) | [i == k-2]}
            == (2-1)*(choose_(k;(k-2))*(fKrtQ*2+1)**(k-2)*((2-1)**(k-1-(k-2))+(-1)**(k-(k-2))))
            == (choose_(k;2)*(fKrtQ*2+1)**(k-2)*2)
            >= (choose_(2;2)*(fKrtQ*2+1)**(2-2)*2)
            == 2
            ]
        ]
        ]]
    ]
    [[k>=0][e>=0] -> [E*g(k) >= 0]]
    [[k>=2][e>=1] -> [E*g(k) >= 2]]

    [[k>=0][e>=0] -> [g(k) >= 0]]
    [[k>=2][e>=1] -> [g(k) >= ceil(2/E) == 1]]

    [[k>=0][e>=0] -> [(upper_D1_dd1-lower_D_dd) >= 0]]
    [[k>=2][e>=1] -> [(upper_D1_dd1-lower_D_dd) >= 1]] #不必需囗前提条件
    ]]


    !![k>=2][e>=1]
    [(upper_D1_dd1-lower_D_dd) >= 1]

    !![[D <= (upper_D1_dd1 *lower_D_dd +(min(upper_D1_dd1,lower_D_dd)-1))//max(1,abs(upper_D1_dd1-lower_D_dd))] -> [dd <- {D//lower_D_dd,D//lower_D_dd-1}]]
    [[D <= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)] -> [dd <- {D//lower_D_dd,D//lower_D_dd-1}]]

    [flbN := floor_log2(n)]
    [flbQ := floor_log2(q)]
    !![(q,r) := divmod(n, 2**(k*e))]
    [flbN == flbQ + k*e]
    !![fKrtQ**k <= q < (fKrtQ+1)**k]
    [k*log2(fKrtQ) <= log2(q) < k*log2(fKrtQ+1)]
    [log2(fKrtQ) <= log2(q)/k < log2(fKrtQ+1)]
    [floor_log2(fKrtQ) <= floor(log2(q)/k) <= floor_log2(fKrtQ+1)]
    [floor_log2(fKrtQ) <= floor_log2(q)//k <= floor_log2(fKrtQ+1)]
    [k*floor_log2(fKrtQ) <= flbQ <= k*floor_log2(fKrtQ+1) +k-1]

    # 求max_E(k;flbN): [[1 <= E <= max_E(k;flbN)] -> [D <= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]]
    # 即:求max_E(k;flbN): [[D > (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)] -> [E > max_E(k;flbN)]]
    #
    [not$ [D <= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]]:[[
        [D > (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]


        !![lower_D_dd *dd <= D < D+1 <= upper_D1_dd1 *(dd+1)]
        !![0 <= dd < E]
        #bug:dd并不自由:[lower_D_dd *(E-1) <= D < D+1 <= upper_D1_dd1 *((E-1)+1)]
        [lower_D_dd *0 <= D < D+1 <= upper_D1_dd1 *((E-1)+1)]


        [0 <= D < upper_D1_dd1*E]
        !![D > (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]
        [upper_D1_dd1*E > D > (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]
        [(upper_D1_dd1*E -2) >= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]

        !![(upper_D1_dd1-lower_D_dd) >= 1]
        [(upper_D1_dd1*E -2)*(upper_D1_dd1-lower_D_dd) >= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))]

        # ==>> [E > ???max_E(k;flbN)]
        [0
        <= (upper_D1_dd1*E -2)*(upper_D1_dd1-lower_D_dd) - (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))
        == (upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) -2*(upper_D1_dd1-lower_D_dd) -(upper_D1_dd1*lower_D_dd +(lower_D_dd-1))
        == (upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) -(upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)
        ]
        [(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) >= (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]
        [2**e == E
        >= ceil((upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)/upper_D1_dd1/(upper_D1_dd1-lower_D_dd))
        == ceil((lower_D_dd +2 -(lower_D_dd+1)/upper_D1_dd1)/(upper_D1_dd1-lower_D_dd))
        !![(upper_D1_dd1-lower_D_dd) >= 1]
        >= ceil((lower_D_dd +2 -1)/(upper_D1_dd1-lower_D_dd))
        == ceil_div((lower_D_dd +1), (upper_D1_dd1-lower_D_dd))
        == 1 +lower_D_dd//(upper_D1_dd1-lower_D_dd)
        ]
        [E >= 1 +lower_D_dd//(upper_D1_dd1-lower_D_dd)] #适用于 实时计算，但对于 提取估计[E > max_E(k;flbQ)] 而言，过宽

        #####
        [a,b>=0][k>=2]:
            [(a+b)**k
            == (sum{(choose_(k;i) *a**(k-i) *b**i) | [i :<- [0..=k]]})
            == (sum{(choose_(k;i) *a**(k-i) *b**i) | [i :<- [0..=k-2]]}) +(choose_(k;(k-1)) *a**(k-(k-1)) *b**(k-1)) +(choose_(k;k) *a**(k-k) *b**k)
            == (sum{(choose_(k;i) *a**(k-i) *b**i) | [i :<- [0..=k-2]]}) +(k*a*b**(k-1)) +b**k
            == (sum{(k*(k-1)/(k-i)/(k-1-i) *a**2 *choose_(k-2;i) *a**(k-2-i) *b**i) | [i :<- [0..=k-2]]}) +(k*a*b**(k-1)) +b**k
            * >= (sum{(k*(k-1)/(k-0)/(k-1-0) *a**2 *choose_(k-2;i) *a**(k-2-i) *b**i) | [i :<- [0..=k-2]]}) +(k*a*b**(k-1)) +b**k
                == a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k
            * <= (sum{(k*(k-1)/(k-(k-2))/(k-1-(k-2)) *a**2 *choose_(k-2;i) *a**(k-2-i) *b**i) | [i :<- [0..=k-2]]}) +(k*a*b**(k-1)) +b**k
                == k*(k-1)/2 *a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k
            ]
            [a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k <= (a+b)**k <= k*(k-1)/2 *a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k]
            [a**2 *(a+b)**(k-2) <= ((a+b)**k -(k*a*b**(k-1)) -b**k) <= k*(k-1)/2 *a**2 *(a+b)**(k-2)]
            [not$ [a==0==b]]:
                [1 <= ((a+b)**k -(k*a*b**(k-1)) -b**k)/(a**2 *(a+b)**(k-2)) <= k*(k-1)/2]
        [[a,b>=0][k>=2][not$ [a==0==b]] -> [1 <= ((a+b)**k -(k*a*b**(k-1)) -b**k)/(a**2 *(a+b)**(k-2)) <= k*(k-1)/2]]
        [[a,b>=0][k>=2] -> [a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k <= (a+b)**k <= k*(k-1)/2 *a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k]]
        #####
        !![(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) >= (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]
        [2 -(lower_D_dd+1)/upper_D1_dd1
        <= E*(upper_D1_dd1-lower_D_dd) -lower_D_dd
        == E*upper_D1_dd1-(E+1)*lower_D_dd
        !![lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
        !![upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))]
        == E*(((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1)) -(E+1)*((fKrtQ*E+1)**k - (fKrtQ*E)**k)
        == ((fKrtQ+1)**k - (fKrtQ)**k)*E**k -(E+1)*((fKrtQ*E+1)**k - (fKrtQ*E)**k)
        == (fKrtQ+1)**k*E**k +E*fKrtQ**k*E**k -(E+1)*(fKrtQ*E+1)**k
        # <= ???

        !![[a,b>=0][k>=2] -> [a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k <= (a+b)**k <= k*(k-1)/2 *a**2 *(a+b)**(k-2) +(k*a*b**(k-1)) +b**k]]
        <= (k*(k-1)/2 *1**2 *(fKrtQ+1)**(k-2) +(k*1*fKrtQ**(k-1)) +fKrtQ**k)*E**k +E*fKrtQ**k*E**k -(E+1)*(1**2 *(1+fKrtQ*E)**(k-2) +(k*1*(fKrtQ*E)**(k-1)) +(fKrtQ*E)**k)
        == (k*(k-1)/2 *(fKrtQ+1)**(k-2) +k*fKrtQ**(k-1) +fKrtQ**k)*E**k +E*fKrtQ**k*E**k -(E+1)*((1+fKrtQ*E)**(k-2) +k*fKrtQ**(k-1)*E**(k-1) +fKrtQ**k*E**k)
        == k*(k-1)/2 *(fKrtQ+1)**(k-2)*E**k +k*fKrtQ**(k-1)*E**k +fKrtQ**k*E**k +fKrtQ**k*E**(k+1) -((1+fKrtQ*E)**(k-2)*E +k*fKrtQ**(k-1)*E**k +fKrtQ**k*E**(k+1)) -((1+fKrtQ*E)**(k-2) +k*fKrtQ**(k-1)*E**(k-1) +fKrtQ**k*E**k)
        == k*(k-1)/2 *(fKrtQ+1)**(k-2)*E**k -(1+fKrtQ*E)**(k-2)*E -(1+fKrtQ*E)**(k-2) -k*fKrtQ**(k-1)*E**(k-1)
        == k*(k-1)/2 *(fKrtQ+1)**(k-2)*E**k -(1+1/(fKrtQ*E))**(k-2)*fKrtQ**(k-2)*E**(k-1) -(1+1/(fKrtQ*E))**(k-2)*fKrtQ**(k-2)*E**(k-2) -k*fKrtQ**(k-1)*E**(k-1)
        == (k*(k-1)/2 *(fKrtQ+1)**(k-2)*E**2 -(1+1/(fKrtQ*E))**(k-2)*fKrtQ**(k-2)*E -(1+1/(fKrtQ*E))**(k-2)*fKrtQ**(k-2) -k*fKrtQ**(k-1)*E)*E**(k-2)
        == (k*(k-1)/2 *(fKrtQ+1)**(k-2)*E**2 -(k*fKrtQ +(1+1/(fKrtQ*E))**(k-2))*fKrtQ**(k-2)*E -(1+1/(fKrtQ*E))**(k-2)*fKrtQ**(k-2))*E**(k-2)
        == (k*(k-1)/2 *(1+1/fKrtQ)**(k-2)*E**2 -(k*fKrtQ +(1+1/(fKrtQ*E))**(k-2))*E -(1+1/(fKrtQ*E))**(k-2))*fKrtQ**(k-2)*E**(k-2)
        ]

        !![(upper_D1_dd1-lower_D_dd) >= 1]
        [1 <= 2 -(lower_D_dd+1)/upper_D1_dd1 <= (k*(k-1)/2 *(1+1/fKrtQ)**(k-2)*E**2 -(k*fKrtQ +(1+1/(fKrtQ*E))**(k-2))*E -(1+1/(fKrtQ*E))**(k-2))*fKrtQ**(k-2)*E**(k-2)]
        [1/(fKrtQ**(k-2)*E**(k-2)) <= (k*(k-1)/2 *(1+1/fKrtQ)**(k-2)*E**2 -(k*fKrtQ +(1+1/(fKrtQ*E))**(k-2))*E -(1+1/(fKrtQ*E))**(k-2))]
        [((k*(k-1)/2 *(1+1/fKrtQ)**(k-2)) *E**2 -(k*fKrtQ +(1+1/(fKrtQ*E))**(k-2)) *E -(1+2/(fKrtQ*E))**(k-2)) >= 0]
        !![e>=1][E == 2**e >= 2][fKrtQ>=1]
        # [E >= (+(k*fKrtQ +(1+1/(fKrtQ*E))**(k-2)) +sqrt((k*fKrtQ +(1+1/(fKrtQ*E))**(k-2))**2 +4*(k*(k-1)/2 *(1+1/fKrtQ)**(k-2))*(1+2/(fKrtQ*E))**(k-2)))/(2*(k*(k-1)/2 *(1+1/fKrtQ)**(k-2)))]
        [((k*(k-1)/2 *2**(k-2)) *E**2 -(k*fKrtQ +1) *E -1) >= 0]
        [E
        >= ((k*fKrtQ +1) +sqrt((k*fKrtQ +1)**2 +4*(k*(k-1)/2 *2**(k-2))*1))/(2*(k*(k-1)/2 *2**(k-2)))
        >= ((k*fKrtQ +1) +sqrt((k*fKrtQ +1)**2 +(2*k*(k-1) *2**(k-2))))/(k*(k-1) *2**(k-2))
        > 2*(k*fKrtQ +1)/(k*(k-1) *2**(k-2))
        == (fKrtQ +1/k)/((k-1) *2**(k-3))
        ]
        [e == log2(E)
        > log2((fKrtQ +1/k)/((k-1) *2**(k-3)))
        == log2(fKrtQ +1/k) -log2(k-1) -(k-3)
        > floor_log2(fKrtQ) -ceil_log2(k-1) -k +3
        ]
        [e > floor_log2(fKrtQ) -ceil_log2(k-1) -k +3] #预估用，近乎翻倍

        [[实时用:
        # ==>> [e > ???max_e(k;flbQ)]
        [e == ceil_log2(2**e)
        == ceil_log2(E)
        >= ceil_log2(1 +lower_D_dd//(upper_D1_dd1-lower_D_dd))
        == ceil_log2((lower_D_dd +1)/(upper_D1_dd1-lower_D_dd))
        ] #适用于 实时计算，但对于 提取估计[E > max_E(k;flbQ)] 而言，过宽
        ]]


        [e
        > floor_log2(fKrtQ) -ceil_log2(k-1) -k +3
        !![k*floor_log2(fKrtQ) <= flbQ <= k*floor_log2(fKrtQ+1) +k-1]
        >= floor_log2(fKrtQ+1) -1 -ceil_log2(k-1) -k +3
        >= flbQ//k -ceil_log2(k-1) -k +2
        !![flbN == flbQ + k*e]
        >= (flbN-k*e)//k -ceil_log2(k-1) -k +2
        == flbN//k -e -ceil_log2(k-1) -k +2
        ]
        [2*e > flbN//k -ceil_log2(k-1) -k +2]
        [e > (flbN//k -ceil_log2(k-1) -k +2)//2]
        [max_e(k;flbN) =[def]= (flbN//k -ceil_log2(k-1) -k +2)//2]
        [e > max_e(k;flbN)]
        [[
        [floor_log2(fKrtQ) -ceil_log2(k-1) -k +3 >= 1]:
            [floor_log2(fKrtQ) >= ceil_log2(k-1) +k -2]
                # {k:rhs}={2:0, 3:2, 4:4, 5:5, 6:7, 7:8, 8:9, 9:10, 10:12, ...}
        ]]
        [max_e(k;flbN) >= 1]:
            [(flbN//k -ceil_log2(k-1) -k +2)//2 >= 1]
            [(flbN//k -ceil_log2(k-1) -k +2) >= 2]
            [flbN//k >= (ceil_log2(k-1) +k)]
            [flbN >= k*(ceil_log2(k-1) +k)]
                # {k:rhs}={2:4, 3:12, 4:24, 5:35, 6:54, 7:70, 8:88, 9:108, 10:140, ...}
        [min_flbN(k) =[def]= k*(ceil_log2(k-1) +k)]
            #这也太大了...
        算了，还是直接用脚本枚举...
            e script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py
            直接检查:[not$ [(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) >= (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]]
                [lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
                [upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))]
                [E == 2**e]
                求:max_E(k;flbQ), max_e(k;flbN)
        view script/seed.math.floor_ceil-floor_kth_root_--E-flbQ.py
        [[
            [is_e_ok__k__fKrtQ(k, fKrtQ, e) =[def]= [[k>=2][fKrtQ>=1][E:=2**e][lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)][upper_D1_dd1 := (((fKrtQ+1)**k - (fKrtQ)**k)*E**(k-1))][(upper_D1_dd1*E)*(upper_D1_dd1-lower_D_dd) < (upper_D1_dd1*lower_D_dd +2*upper_D1_dd1 -lower_D_dd-1)]]]
            [is_e_ok__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, e) =[def]= [[k>=2][floor_log2_fKrtQ>=0][@[fKrtQ :<- [2**floor_log2_fKrtQ..<2**(1+floor_log2_fKrtQ)]] -> [is_e_ok__k__fKrtQ(k, fKrtQ, e)]]]]
            [find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ) =[def]= (-1+min({0}\-/{bad_e <- [1..] | [not$ [is_e_ok__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, bad_e)]]}))]
                # [find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ) =[def]= (max({-1}\-/{max_e <- [0..] | [@[e <- [0..=max_e]] -> [is_e_ok__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ, e)]]}))]
            [第一猜想:= [@[k>=2] -> [i:=ceil_log2(k-1)-1] -> @[floor_log2_fKrtQ>=0] -> [[max(0, floor_log2_fKrtQ-i)<=find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)<=max(0, 1+floor_log2_fKrtQ-i)][?[threshold>=i] -> [floor_log2_fKrtQ >= threshold] -> [find_max_e__k__floor_log2_fKrtQ(k, floor_log2_fKrtQ)==floor_log2_fKrtQ-i]]]]] #候选的粗略定义:[max_e<k{>=2},floor_log2_fKrtQ{>=0}> =[def]= max(0, 1+floor_log2_fKrtQ-ceil_log2(k-1))]

        ]]

        [第一猜想]:[[
            [max_e__k__floor_log2_fKrtQ(k,floor_log2_fKrtQ) =[def]= max(0, 1+floor_log2_fKrtQ-ceil_log2(k-1))]
            !![flbN == flbQ + k*e]
            !![floor_log2_fKrtQ == flbQ//k *k == flbQ-flbQ%k]
            [floor_log2_fKrtQ
            == flbQ-flbQ%k
            == (flbN-k*e -flbN%k)
            ]
            [(1+floor_log2_fKrtQ-ceil_log2(k-1)) >= 0]:
                [e
                <= max_e__k__floor_log2_fKrtQ(k,floor_log2_fKrtQ)
                == max(0, 1+floor_log2_fKrtQ-ceil_log2(k-1))
                == (1+floor_log2_fKrtQ-ceil_log2(k-1))
                == (1+(flbN-k*e -flbN%k)-ceil_log2(k-1))
                ]
                [(flbN -flbN%k) >= ceil_log2(k-1) -1 +(k+1)*e]
                [(k+1)*e <= (flbN -flbN%k) -ceil_log2(k-1) +1]
                [e <= ((flbN -flbN%k) -ceil_log2(k-1) +1)//(k+1)]
            [max_e(k,flbN) =[def]= ((flbN -flbN%k) -ceil_log2(k-1) +1)//(k+1)]
            [max_e(k,flbN) <= 0]:
                [((flbN -flbN%k) -ceil_log2(k-1) +1)//(k+1) <= 0]
                [((flbN -flbN%k) -ceil_log2(k-1) +1) <= k]
                [flbN//k *k == (flbN -flbN%k) <= (k-1 +ceil_log2(k-1))]
                [flbN//k <= (k-1 +ceil_log2(k-1))//k]
                [flbN <= (k-1 +ceil_log2(k-1))//k *k +k-1]
                [flbN < (k-1 +ceil_log2(k-1))//k *k +k]
                * [k==2]:
                    [ceil_log2(k-1) == 0]
                    [flbN < (2-1 +0)//2 *2 +2 == 2 == 1*k]
                * [k>=3]:
                    [ceil_log2(k-1) == 1+floor_log2(k-2) <= 1+(k-2)-1 == k-2]
                    [ceil_log2(k-1) >= ceil_log2(3-1) == 1]
                    [flbN < (k-1 +ceil_log2(k-1))//k *k +k == 1*k +k == 2*k]
                [flbN < (2-[k==2])*k]
            [[max_e(k,flbN) <= 0] -> [flbN < (2-[k==2])*k]]
            [[flbN >= (2-[k==2])*k] -> [max_e(k,flbN) >= 1]]
        ]]

        !![e > max_e(k;flbN)]
        [not$ [e <= max_e(k;flbN)]]
        ]]
    [[not$ [D <= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]] -> [not$ [e <= max_e(k;flbN)]]]
    [[e <= max_e(k;flbN)] -> [D <= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)]]
    !![[D <= (upper_D1_dd1*lower_D_dd +(lower_D_dd-1))//(upper_D1_dd1-lower_D_dd)] -> [dd <- {D//lower_D_dd,D//lower_D_dd-1}]]
    [[e <= max_e(k;flbN)] -> [dd <- {D//lower_D_dd,D//lower_D_dd-1}]]
    # ==>> [???max_e(k;flbN)]
    其中[[
        [dd := fKrtN - (fKrtQ*2**e)]
        [D := n -(fKrtQ*2**e)**k]
        [E := 2**e]
        [lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
        [第一猜想]:[[
            [max_e__k__floor_log2_fKrtQ(k,floor_log2_fKrtQ) =[def]= max(0, 1+floor_log2_fKrtQ-ceil_log2(k-1))]
            [max_e(k,flbN) =[def]= ((flbN -flbN%k) -ceil_log2(k-1) +1)//(k+1)]
            [[flbN >= (2-[k==2])*k] -> [max_e(k,flbN) >= 1]]
        ]]
    ]]





[[
>>> from seed.math.floor_ceil import floor_kth_root_
>>> floor_kth_root_(7, 1<<1000)
10099156328514439423684435017530967657253776

>>> floor_kth_root_(207, 1<<10000)
348748114132194

]]






    #]]]'''
    fKrtN = _floor_kth_root__impl_(k, n)
    assert fKrtN**k <= n < (fKrtN+1)**k
    return fKrtN
def _floor_kth_root__impl_(k, n, /):
    r'''[[[
    ######################
    let [mmm:=min{k*log2(k), log2(n)}]
    let [lbN:=log2(n)][lblbN:=log2(log2(n))]
    ~ O(mmm**3 /k + (lbN -mmm)**2)
    ~ worst[k==lbN/lblbN]:O(lbN**2 *lblbN)
    ######################
    ######################
    ######################
    ######################
    ######################
    ######################
    #xxx '...+O(log2(n)**2)'
    '...+O(1/k * min{k*log2(k), log2(n)}**3)'
        'or:  ...+O(log2(n)**2 *log2(log2(n)))'
    '...+O((log2(n) -min{k*log2(k), log2(n)})**2)'
    ######################
    let [mmm:=min{k*log2(k), log2(n)}]
    #xxx total ~= O(log2(n)**2 + (1/k * mmm**3) + ((log2(n) -mmm)**2))
    total ~= O((1/k * mmm**3) + ((log2(n) -mmm)**2))

    let [lbN:=log2(n)]
    ~ O(mmm**3 /k + (lbN -mmm)**2)

    let [lblbN:=log2(log2(n))]
    let [lbK:=log2(k)]
    !! [max(mmm**3 /k) == (mmm**3 /k){k:=lbN/lblbN} == (lbN**2*lblbN)]
    ~ worst[lbN == k*lbK][k==lbN/lblbN]:O(lbN**2 *lblbN)
    ######################
    ~ [0 <= lbN < k]:O(1)
    ~ [k <= lbN < k*lbK]:O(lbN**3 /k)
    ~ worst[lbN == k*lbK][k==lbN/lblbN]:O(lbN**2 *lblbN)
    ~ [k*lbK < lbN < k*lbK**(3/2)][lbN/lblbN**(3/2) < k < lbN/lblbN]:O(k**2 *lbK**3)
    ~ [lbN > k*lbK**(3/2)]:O(lbN**2)
    ######################
    [lbN == k*lbK] => [k==lbN/lblbN]
    [lbN == k*lbK**(3/2)] => [k==lbN/lblbN**(3/2)]
    [k*lbK < lbN < k*lbK**(3/2)] => [lbN/lblbN**(3/2) < k < lbN/lblbN]
    ######################



    #]]]'''
    assert k >= 1
    assert n >= 0
    if k == 1 or n < 2:
        return n
    # [k >= 2]
    # [n >= 2]
    flbN = floor_log2(n)
    if flbN < k:
        return 1
    # [n >= 2**k]
    # [n**(1/k) >= 2]
    # [2 <= k <= log2(n)]


    # [k >= 2][n >= 2**k >= 4]
    floor_log2_fKrtN = floor_log2_kth_root_(k, n)
    assert floor_log2_fKrtN >= 1
    if 0:
        fKrtN = 1<<floor_log2_fKrtN
        # [fKrtN == 2**floor_log2_fKrtN >= 2]
        # [fKrtN^1 == fKrtN+1]
        if n < (fKrtN^1)**k:
            return fKrtN
        # EVAL((fKrtN^1)**k)
        # ~ O(sum (2**i*(log2(n)/k))**2 {i :<- [0..=log2(k)]})
        # ~ O(log2(n)**2)
        '...+O(log2(n)**2)'
        fKrtN = (1<<(floor_log2_fKrtN+1))-1
        if fKrtN**k <= n:
            return fKrtN
        del fKrtN
        '...+O(log2(n)**2)'

    r'''[[[
    [[e <= max_e(k;flbN)] -> [dd <- {D//lower_D_dd,D//lower_D_dd-1}]]
        [dd := fKrtN - (fKrtQ*2**e)]
        [D := n -(fKrtQ*2**e)**k]
        [E := 2**e]
        [lower_D_dd := ((fKrtQ*E+1)**k - (fKrtQ*E)**k)]
        [第一猜想]:[[
            [max_e__k__floor_log2_fKrtQ(k,floor_log2_fKrtQ) =[def]= max(0, 1+floor_log2_fKrtQ-ceil_log2(k-1))]
            [max_e(k,flbN) =[def]= ((flbN -flbN%k) -ceil_log2(k-1) +1)//(k+1)]
            [[flbN >= (2-[k==2])*k] -> [max_e(k,flbN) >= 1]]
        ]]

    #]]]'''
    t = ceil_log2(k-1) -1
    #k1 = k+1
    #min_flbN = k if k==2 else 2*k
    min_floor_log2_fKrtQ = t+1

    #for floor_log2_partial_lead_bits4fKrtN, (partial_lead_bits4fKrtN, num_remain_bits) in enumerate(_iter_partial_floor_kth_root__bisearch_(k, n)):
    for floor_log2_fKrtQ, (fKrtQ, num_remain_bits) in enumerate(_iter_partial_floor_kth_root__bisearch_(k, n)):
        # ~O(k**2 * (loop-round-idx)**2)
        # ~O(k**2 * floor_log2_fKrtQ**2)
        if floor_log2_fKrtQ == min_floor_log2_fKrtQ:
            break
    # O(for-loop)
    # * [num_remain_bits =!= 0]:
    #   # [floor_log2_fKrtQ == min_floor_log2_fKrtQ < floor_log2_fKrtN]
    #   # ~O(sum k**2 * floor_log2_fKrtQ**2 {floor_log2_fKrtQ :<- [1..=min_floor_log2_fKrtQ]})
    #   # ~O(k**2 * min_floor_log2_fKrtQ**3)
    #   # ~O(k**2 * log2(k)**3)
    #   #   # !! [min_floor_log2_fKrtQ < floor_log2_fKrtN]
    #   #   # [log2(k) < log2(n)/k]
    #   #   # [k*log2(k) < log2(n)]
    #   #   # ~<=O(log2(k) * log2(n)**2)
    #   #   #    # bisearch，效率确实低 #bisection
    #   # ~O(1/k * (k*log2(k))**3)
    # * [num_remain_bits == 0]:
    #   # [floor_log2_fKrtQ == floor_log2_fKrtN <= min_floor_log2_fKrtQ]
    #   # ~O(sum k**2 * floor_log2_fKrtQ**2 {floor_log2_fKrtQ :<- [1..=floor_log2_fKrtN]})
    #   # ~O(k**2 * floor_log2_fKrtN**3)
    #   # ~O(k**2 * (log2(n)/k)**3)
    #   # ~O(1/k * log2(n)**3)
    '...+O(1/k * min{k*log2(k), log2(n)}**3)'
    'or:  ...+O(log2(n)**2 *log2(log2(n)))'
        # [k*log2(k) == log2(n)] -> [k ~= log2(n)/log2(log2(n))]
        #   O((lbN/lblbN)**2 * lblbN**3)
        #   O(lbN**2 * lblbN)
    # [2 <= k <= log2(n)]
    assert floor_log2_fKrtQ == floor_log2(fKrtQ)
    assert floor_log2_fKrtN == floor_log2_fKrtQ+num_remain_bits
    pow_fKrtQ_k = fKrtQ**k
    pow_1fKrtQ_k = (fKrtQ+1)**k
    assert pow_fKrtQ_k <= (n>>(num_remain_bits*k)) < pow_1fKrtQ_k
    while num_remain_bits:
        num_remain_bits, fKrtQ, pow_fKrtQ_k, floor_log2_fKrtQ
            #循环变量
        #####
        max_e = floor_log2_fKrtQ -t
        e = min(num_remain_bits, max_e)
        num_remain_bits -= e
        n_ = (n>>(num_remain_bits*k))

        assert e >= 1
        E = 1 << e
        k_e = k*e
        E_fKrtQ = (fKrtQ<<e)
        pow_EfKrtQ_k = pow_fKrtQ_k << k_e
        pow_1EfKrtQ_k = (E_fKrtQ^1)**k
            # EVAL(pow_1EfKrtQ_k) ~ EVAL(pow_fKrtN__k)
            # 计算量等价合并
        D = n_ -pow_EfKrtQ_k
        lower_D_dd = pow_1EfKrtQ_k -pow_EfKrtQ_k
        dd = D//lower_D_dd
        assert 0 <= dd <= E
        dd_ = dd-1 if dd == E else dd
        assert 0 <= dd_ < E

        fKrtN_ = E_fKrtQ^dd_
        pow_fKrtN__k = fKrtN_**k
            # ~O(last-square)
            # ~O(log2(fKrtN_**k)**2)
            # ~O(k**2 * log2(fKrtN_)**2)
            # ~O(k**2 * log2(E_fKrtQ)**2)
            # ~O(k**2 * log2(2**e*fKrtQ)**2)
            # ~O(k**2 * (e+log2(fKrtQ))**2)
            # ~O(k**2 * (floor_log2_fKrtQ*2-t)**2)
            # ~O(k**2 * (floor_log2_fKrtQ*2-log2(k))**2)
            # ~O(k**2 * floor_log2_fKrtQ**2)
        if n_ < pow_fKrtN__k:
            assert 1 <= dd_==dd < E
            fKrtN_ -= 1
            pow_fKrtN__k = fKrtN_**k
        else:
            assert 0 <= dd_ < E
        assert pow_fKrtN__k <= n_
        #####
        fKrtQ = fKrtN_
        pow_fKrtQ_k = pow_fKrtN__k
        floor_log2_fKrtQ += e
    fKrtN = fKrtQ
    # [ttrn := total rounds]
    # * [floor_log2_fKrtN > t]:
    #   # [floor_log2_fKrtN -t == sum e<i> {i :<- [0..<ttrn]} == e<0> * sum 2**i {i :<- [0..<ttrn-1]} + e<-1> >= 2**(ttrn-1)]
    #   # [ttrn <= log2(floor_log2_fKrtN -t)]
    #   # [ttrn ~= log2(log2(n)/k -log(k))]
    #   # O(loop) ~ O(sum (k**2 * floor_log2_fKrtQ**2) {i :<- [0..<ttrn]})
    #   # ~ O(sum (k**2 * (t+2**i)**2) {i :<- [0..<ttrn]})
    #   # ~ O(k**2 * (2**ttrn)**2)
    #   # ~ O(k**2 * (log2(n)/k -log(k))**2)
    #   # ~ O((log2(n) -k*log(k))**2)
    # * [floor_log2_fKrtN <= t]:
    #   # [ttrn == 0]
    '...+O(max{0,log2(n) -k*log(k)}**2)'
    'or:  ...+O((log2(n) -min{k*log2(k), log2(n)})**2)'
    return fKrtN

def floor_lshift_kth_root_(e, k, n, /):
    '[floor_lshift_kth_root_(e, k, n) =[def]= floor(kth_root_(k;n) *2**e) = floor_kth_root_(k;n*2**(k*e))]'
    return floor_kth_root_(k, n<<(k*e))
def floor_lshift_sqrt_(e, n, /):
    r'''[[[
    [floor_lshift_sqrt_(e,n) =[def]= floor(2**e * sqrt(n))]

    see:floor_lshift_kth_root_
    #]]]'''
    assert n >= 0
    assert e >= 0
    return floor_sqrt(n<<(2*e))

__all__
from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt, ceil_sqrt, floor_kth_root_, ceil_kth_root_
from seed.math.floor_ceil_tools.fc_kth_root import floor_lshift_sqrt_, floor_lshift_kth_root_
from seed.math.floor_ceil_tools.fc_kth_root import *
