#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/FFT/Walsh_transform.py

seed.algo.FFT.Walsh_transform
py -m nn_ns.app.debug_cmd   seed.algo.FFT.Walsh_transform -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.FFT.Walsh_transform:__doc__ -ht # -ff -df

[[
view others/数学/FFT-Walsh_transform.txt
===

Walsh_transform 长度固定为二幂，只使用加减法
FFT ==>> cyclic convolution
Walsh_transform ==>> XOR (dyadic) convolution

[len(X)==len(Y)==L][Z := IFFT(FFT(X) .* FFT(Y))]:
    [Z[k] == sum [X[i]*Y[j] | [i+j=[%L]=k]]] # +%L
[len(X)==len(Y)==L==2**ez][Z := IW(W(X) .* W(Y))]:
    [Z[k] == sum [X[i]*Y[j] | [i^j==k]]] # xor

[Walsh_transform[L][i,j] == (-1)**(i&j).bit_count()]
  验证于:view ../../python3_src/seed/algo/FFT/Walsh_transform.py
  #我推导出来的
  <<==:
(right) Kronecker product (or tensor product)
[A :: matrix{m,n}][B :: matrix{s,t}]:
    #bug: [A *< B =[def]= matrix(m*s,n*t; \i,j->A[i//m,j//n]*B[i%s,j%t])]
    [A *< B =[def]= matrix(m*s,n*t; \i,j->A[i//s,j//t]*B[i%s,j%t])]
      right_Kronecker_product(A,B)
      tensor_product(A,B)
      B注入到A
不满足交换律
结合律:
[(A*<B)*<C == A*<(B*<C)]
分配律:
[(A+B)*<C == (A*<C)+(B*<C)]
[A*<(B+C) == (A*<B)+(A*<C)]

交互:(*)(*<)
[(A*B)*<(C*D) == (A*<C)*(B*<D)]
    rA_cB*<rC_cD --> rArC_cAcC*rBrD_cBcD
    !! [cA==rB][cC==rD]
    [cA*cC == rB*rD]
  ==>>:
  [A*<C == (A*In)*<(Is*D) == (A*<Is)*(In*<D)]
  [A*<C == (Im*A)*<(D*It) == (Im*<D)*(A*<It)]
  [(Im*<D)*(A*<It) == A*<C == (A*<Is)*(Im*<D)]
==>>:
[@[n :: int] -> [(A**n)*<(B**n) == (A*<B)**n]]
  !! [(A*B)*<(C*D) == (A*<C)*(B*<D)]
  !! [(A**-1)*<(B**-1) == (A*<B)**-1]
<<==:
倒数:
[(A**-1)*<(B**-1) == (A*<B)**-1]

转置:
[(A.transpose)*<(B.transpose) == (A*<B).transpose]

[det(Amm*<Bnn) == det(Amm)**n*det(Bnn)**m]




[ez <- [0..]]:
  [Walsh_transform[1] =[def]= [+1;]]
  [Walsh_transform[2] =[def]= [+1,+1;+1,-1;]]
  [Walsh_transform[2**(1+ez)] =[def]= Walsh_transform[2] *< Walsh_transform[2**ez]]
  [Walsh_transform[2**ez] =[def]= foldl (*<) Walsh_transform[1] [Walsh_transform[2]]*ez]
      ==>> 类似FFT算法:
        [X == [$X0;$X1;]]
        [W[2*L]*X == [$(W[L]*(X0+X1));$(W[L]*(X0-X1));]]
            That is, a length-n transform can be computed by two length-n/2 transforms of the sum and difference of the first and second half of x.
        <<==:
        [W[2*L]*X
        == (W[2]*<W[L])*[$X0;$X1;]
        == [$+W[L],$+W[L];$+W[L],$-W[L];]*[$X0;$X1;]
        == [$(W[L]*X0+W[L]*X1);$(W[L]*X0-W[L]*X1);]
        == [$(W[L]*(X0+X1));$(W[L]*(X0-X1));]
        ]
[ez <- [0..]]:
  !! [@[n :: int] -> [(A**n)*<(B**n) == (A*<B)**n]]
  !! [IW[2] == W[2]/2]
  [IW[2**ez] == W[2**ez]/2**ez]
  [W[2**ez]**2 == 2**ez*IdentityMatrix{2**ez}]


]]



>>> f = lambda A, B:matrix_right_Kronecker_product_(tuple, int.__mul__, A,B)
>>> g = lambda A, B:matrix_product_(tuple, int.__add__, int.__mul__, A,B)
>>> f([[1, 2]], [[3,4,5], [6,7,8]])
((3, 4, 5, 6, 8, 10), (6, 7, 8, 12, 14, 16))

>>> A = [[666,999],[777,888], [444,555]]
>>> B = [[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]]
>>> C = [[1, 2]]
>>> D = [[3,4,5], [6,7,8]]
>>> g(A,B)
((8658, 10323, 11988, 13653, 15318, 16983, 18648), (7881, 9546, 11211, 12876, 14541, 16206, 17871), (4884, 5883, 6882, 7881, 8880, 9879, 10878))
>>> g(C,D)
((15, 18, 21),)

# (1x2*2x3)*<(3x2*2x7) --> 1x3*<3x7 --> 3x21
# (1x2*<2x7)*(3x2*<2x3) --> 2x14*6x6 --> err
>>> f(g(C,D), g(A,B)) == g(f(C,B), f(A,D))
Traceback (most recent call last):
    ...
TypeError: ('matrix_product_', (2, 14), (6, 6))

# (1x2*2x3)*<(3x2*2x7) --> 1x3*<3x7 --> 3x21
# (1x2*<3x2)*(2x3*<2x7) --> 3x4*4x21 --> 3x21
>>> f(g(C,D), g(A,B)) == g(f(C,A), f(D,B))
True

>>> W1 = mk_matrix4Walsh_transform__naive_(tuple, 0)
>>> W2 = mk_matrix4Walsh_transform__naive_(tuple, 1)
>>> W4 = mk_matrix4Walsh_transform__naive_(tuple, 2)
>>> W8 = mk_matrix4Walsh_transform__naive_(tuple, 3)
>>> W1
((1,),)
>>> W2
((1, 1), (1, -1))
>>> W4
((1, 1, 1, 1), (1, -1, 1, -1), (1, 1, -1, -1), (1, -1, -1, 1))
>>> W8
((1, 1, 1, 1, 1, 1, 1, 1), (1, -1, 1, -1, 1, -1, 1, -1), (1, 1, -1, -1, 1, 1, -1, -1), (1, -1, -1, 1, 1, -1, -1, 1), (1, 1, 1, 1, -1, -1, -1, -1), (1, -1, 1, -1, -1, 1, -1, 1), (1, 1, -1, -1, -1, -1, 1, 1), (1, -1, -1, 1, -1, 1, 1, -1))
>>> matrix_slice_(tuple, W8, range(4), range(4)) == W4
True
>>> matrix_slice_(tuple, W8, range(2), range(2)) == W2
True
>>> matrix_slice_(tuple, W8, range(1), range(1)) == W1
True
>>> W1 == mk_matrix4Walsh_transform__fancy_(tuple, 0)
True
>>> W2 == mk_matrix4Walsh_transform__fancy_(tuple, 1)
True
>>> W4 == mk_matrix4Walsh_transform__fancy_(tuple, 2)
True
>>> W8 == mk_matrix4Walsh_transform__fancy_(tuple, 3)
True


>>> mul = int.__mul__
>>> add = int.__add__
>>> sub = int.__sub__
>>> xs = [2, 7, 666, 999]
>>> ys = perform_Walsh_transform__naive_(add, sub, xs)
>>> zs = perform_Walsh_transform__naive_(add, sub, ys)
>>> [zs] == matrix_scaleL_(list, mul, len(xs), [xs])
True

>>> xs
[2, 7, 666, 999]
>>> ys
[1674, -338, -1656, 328]
>>> zs
[8, 28, 2664, 3996]

>>> _ys = perform_Walsh_transform_(add, sub, xs)
>>> _zs = perform_Walsh_transform_(add, sub, ys)
>>> _ys == ys
True
>>> _zs == zs
True

>>> rshift = int.__rshift__
>>> _xs = perform_inv_Walsh_transform_(rshift, add, sub, ys)
>>> _xs == xs
True

>>> uint_xmul__via_Walsh_transform_(999, 666)
15029895168
>>> uint_xmul__via_Walsh_transform_(55553, 57777)
62269583197791584256

py_adhoc_call   seed.algo.FFT.Walsh_transform   @f
]]]'''#'''
__all__ = r'''
perform_inv_Walsh_transform_
    uint_xmul__via_Walsh_transform_
perform_Walsh_transform_
mk_matrix4Walsh_transform__fancy_
mk_matrix4Walsh_transform__naive_
perform_Walsh_transform__naive_


matrix_shape_
mk_matrix_
matrix_scaleL_
matrix_scaleR_
matrix_slice_
matrix_product_
matrix_right_Kronecker_product_     matrix_tensor_product_


matrix_dyadic_product_
vector_dyadic_product_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.func_tools.func_pow_ import func_pow_, func_powT_, partial_ex
from functools import reduce, partial
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

def matrix_shape_(A, /):
    rA = num_rows4A = len(A)
    assert rA
    cA = num_columns4A = len(A[0])
    assert cA
    return (rA, cA)
def mk_matrix_(T, rA, cA, ij2v, /):
    check_int_ge(1, rA)
    check_int_ge(1, cA)
    if not callable(ij2v):
        return T(T(ij2v[i][j] for j in range(cA)) for i in range(rA))
    return T(T(ij2v(i,j) for j in range(cA)) for i in range(rA))
def matrix_scaleL_(T, mul, a, B, /):
    (rB, cB) = matrix_shape_(B)
    def ij2v(i, j, /):
        return mul(a, B[i][j])
    return mk_matrix_(T, rB, cB, ij2v)
def matrix_scaleR_(T, mul, B, a, /):
    (rB, cB) = matrix_shape_(B)
    def ij2v(i, j, /):
        return mul(B[i][j], a)
    return mk_matrix_(T, rB, cB, ij2v)
def matrix_slice_(T, A, jrows, jcolumns, /):
    jrows = tuple(jrows)
    jcolumns = tuple(jcolumns)
    rB = len(jrows)
    cB = len(jcolumns)
    def ij2v(i, j, /):
        return A[jrows[i]][jcolumns[j]]
    return mk_matrix_(T, rB, cB, ij2v)
def matrix_product_(T, add, mul, A, B, /):
    #vs:matrix_dyadic_product_
    (rA, cA) = matrix_shape_(A)
    (rB, cB) = matrix_shape_(B)
    if not cA == rB:raise TypeError('matrix_product_', (rA, cA), (rB, cB))
    ks = range(cA)
    def ij2v(i, j, /):
        return reduce(add, (mul(A[i][k], B[k][j]) for k in ks))
    return mk_matrix_(T, rA, cB, ij2v)


def matrix_right_Kronecker_product_(T, mul, A, B, /):
    'A -> B -> (A*<B)'
    (rA, cA) = matrix_shape_(A)
    (rB, cB) = matrix_shape_(B)
    def ij2v(i, j, /):
        qI, rI = divmod(i, rB)
        qJ, rJ = divmod(j, cB)
        return mul(A[qI][qJ], B[rI][rJ])
    return mk_matrix_(T, rA*rB, cA*cB, ij2v)

matrix_tensor_product_ = matrix_right_Kronecker_product_
def mk_matrix4Walsh_transform__naive_(T, log2_len, /):
    check_int_ge(0, log2_len)
    ez = log2_len
    L = 1<<ez
    W1 = mk_matrix_(T, 1, 1, lambda i, j, /:1)
    W2 = mk_matrix_(T, 2, 2, lambda i, j, /: -1 if i==1==j else 1)
    W = W1
    f = func_powT_(ez, matrix_right_Kronecker_product_, (T, int.__mul__, W2))
    return f(W1)

def mk_matrix4Walsh_transform__fancy_(T, log2_len, /):
    check_int_ge(0, log2_len)
    ez = log2_len
    L = 1<<ez
    def ij2v(i, j, /):
        return -1 if (i&j).bit_count()&1 else +1
    return mk_matrix_(T, L, L, ij2v)



def perform_Walsh_transform__naive_(add, sub, xs, /):
    'O(L**2)'
    L = len(xs)
    ez = L.bit_length() - 1
    if ez < 0 or not L == 1<<ez:raise ValueError(L)
    W = mk_matrix4Walsh_transform__fancy_(tuple, ez)
    def _mul(sgn, x, /):
        return (sgn, x)
    def _mul(x, sgn, /):
        return (sgn, x)
    def _add(sa, sb, /):
        (sa, a) = sa
        (sb, b) = sb
        assert sa == 1, (sa, a)
        op = sub if not sa == sb else add
        return (sa, op(a,b))

    [sy_ls] = matrix_product_(tuple, _add, _mul, [xs], W)
    assert all(s == 1 for s, y in sy_ls)
    ys = [y for s, y in sy_ls]
    return ys
def perform_Walsh_transform_(add, sub, xs, /):
    'O(L*log2(L))'
    L = len(xs)
    ez = L.bit_length() - 1
    if ez < 0 or not L == 1<<ez:raise ValueError(L)
    xs = [*xs]
    sz4blk = L
    num_blks = 1
    for _ in range(ez):
        # [sz4blk*num_blks == L]
        gap = sz4blk >> 1
        # [gap == sz4blk/2]
        for offset in range(0, L, sz4blk):
            for i, j in zip(range(offset, offset+gap), range(offset+gap, offset+sz4blk)):
                a = xs[i]
                b = xs[j]
                xs[i] = add(a, b)
                xs[j] = sub(a, b)

        # !! [sz4blk*num_blks == L]
        # !! [gap == sz4blk/2]
        num_blks <<= 1
        sz4blk = gap
        # [sz4blk*num_blks == L]
    return xs

#@20250223
def matrix_dyadic_product_(T, mul, A, B, /):
    #vs:matrix_product_
    #vs:vector_dyadic_product_
    sA = (rA, cA) = matrix_shape_(A)
    sB = (rB, cB) = matrix_shape_(B)
    if not sA == sB:raise TypeError('matrix_dyadic_product_', (rA, cA), (rB, cB))
    def ij2v(i, j, /):
        return mul(A[i][j], B[i][j])
    return mk_matrix_(T, rA, cA, ij2v)
#@20250223
def vector_dyadic_product_(T, mul, A, B, /):
    #vs:matrix_dyadic_product_
    szA = len(A)
    szB = len(B)
    if not szA == szB:raise TypeError('vector_dyadic_product_', szA, szB)
    return T(map(mul, A, B))
#@20250223
def perform_inv_Walsh_transform_(rshift, add, sub, xs, /):
    'O(L*log2(L))'
    # [IW[2**ez] == W[2**ez]/2**ez]
    L = len(xs)
    ez = L.bit_length() - 1
    if ez < 0 or not L == 1<<ez:raise ValueError(L)
    _zs = perform_Walsh_transform_(add, sub, xs)
    zs = [rshift(z, ez) for z in _zs]
    return zs

#@20250223
#e ../../python3_src/seed/algo/rho_method.py
def uint_xmul__via_Walsh_transform_(x, y, /):
    check_int_ge(0, x)
    check_int_ge(0, y)
    flb1_ = int.bit_length
    bsz = flb1_(x) + flb1_(y)
    ez = flb1_(bsz)
    bbsz = 1<<ez
    assert bbsz >= bsz
    xs = _list_bits5uint(bbsz, x)
    ys = _list_bits5uint(bbsz, y)
    if 0b0000:
        assert _bits2uint(xs) == x
        assert _bits2uint(ys) == y
        assert _wbits2uint(xs) == x
        assert _wbits2uint(ys) == y
    _rshift = int.__rshift__
    add = int.__add__
    sub = int.__sub__
    def perfect_rshift(x, ez, /):
        y = x >> ez
        if not x == (y<<ez):raise ValueError(x, ez)
        return y
    def xor_not(x, y, /):
        return x ^ ~y
        # x ^ ~y ^ y == x ^ 111... == ~x
        # ~(~x ^ ~y) ^ y == x ^ 111... == ~x
    _xs = perform_Walsh_transform_(add, sub, xs)
    _ys = perform_Walsh_transform_(add, sub, ys)
    mul = int.__mul__
    xor = int.__xor__
    #mul = xor
    _zs = vector_dyadic_product_(list, mul, _xs, _ys)
    if 0b0000:
        from seed.tiny import print_err
        print_err(xs, ys)
        print_err(_xs, _ys)
        print_err(_zs)
    if 0b0000:
        assert xs == perform_inv_Walsh_transform_(perfect_rshift, add, sub, _xs)
        assert ys == perform_inv_Walsh_transform_(perfect_rshift, add, sub, _ys)
    zs = perform_inv_Walsh_transform_(perfect_rshift, add, sub, _zs)
    assert len(zs) == bbsz
    z = _wbits2uint(zs)
    return z
    return zs
    z = _bits2uint(zs)
        #IndexError: string index out of range
    return z
def _wbits2uint(ws, /):
    it = iter(ws)
    for w in it:
        if w:break
    else:
        return 0
    u = w
    for w in it:
        u <<= 1
        u += w
    return u
def _bits2uint(bs, /):
    s = ''.join(map('01'.__getitem__, bs))
    return int(s, 2)
def _list_bits5uint(sz, x, /):
    xs = _iter_bits5uint(sz, x)
    xs = list(xs)
    assert min(xs, default=0) >= 0
    assert max(xs, default=0) <= 1
    return xs
def _iter_bits5uint(sz, x, /):
    bs = f'{x:0>{sz}b}'
    assert len(bs) == sz
    return map(ord('0').__rsub__, map(ord, bs))
    ######################
    #old:
    bs = bin(x).remove_prefix('0b')
    if sz >= 0:
        pad = sz -len(bs)
        if not pad >= 0:raise ValueError(sz, x)
        bs = '0'*pad + bs
        assert len(bs) == sz
    return map(ord('0').__rsub__, map(ord, bs))


__all__

from seed.algo.FFT.Walsh_transform import uint_xmul__via_Walsh_transform_
from seed.algo.FFT.Walsh_transform import perform_inv_Walsh_transform_
from seed.algo.FFT.Walsh_transform import perform_Walsh_transform_, mk_matrix4Walsh_transform__fancy_
from seed.algo.FFT.Walsh_transform import mk_matrix4Walsh_transform__naive_, perform_Walsh_transform__naive_

from seed.algo.FFT.Walsh_transform import matrix_shape_, mk_matrix_, matrix_scaleL_, matrix_scaleR_, matrix_slice_, matrix_product_, matrix_right_Kronecker_product_#matrix_tensor_product_

from seed.algo.FFT.Walsh_transform import *
