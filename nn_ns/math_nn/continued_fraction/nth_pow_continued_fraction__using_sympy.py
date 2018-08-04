

'''
nth_pow_continued_fraction(x, n, L) = continued_fraction(x**(1/n))[:L]



x = [a0; a1, a2, ...]
x = [x.] + {.x} = floor(x) + 1/(1/(x-floor(x)))
x[0] = x; x[i] = 1/(x[i-1]-floor(x[i-1])) = 1/(x[i-1]-a[i-1]) for [NN i>0]
a[i] = floor(x[i])






'''

from sand import unzip, to_names
from sand import top_level_import
assert top_level_import(__name__, 'sand.forgot_import', args=('logic error',))

from .continued_fraction import calc_Xs_from_NDs, \
     continued_fraction_pack_to_ND_pairs, \
     continued_fraction_expand as _continued_fraction_expand, \
     continued_fraction_expand_with_Xi as _continued_fraction_expand_with_Xi
from .smalls import gcds, lcms, \
     prime2exp_to_frac, rational2int, rational2pair, signs
from nn_ns.sympy_util.factor_frac import factor_frac


from itertools import islice#, chain#, count, accumulate, groupby, starmap
import itertools
from fractions import Fraction
import fractions
from numbers import Integral, Rational
from collections import namedtuple, deque

##from sympy import LC, N, Poly, Q, ceiling, count_roots, degree, floor, \
##     fraction, intervals, oo, real_roots, refine_root, symbols, together, var,\
##     radsimp, ratsimp, sympify, simplify, nsimplify, factorint as factor_int, \
##     count_roots
from sympy import Poly, floor, fraction, intervals, \
     nsimplify, radsimp, simplify, symbols, sympify, \
     factorint as factor_int



##
##from sympy import *
##from nn_ns.math_nn import *

'''
sympy bugs from nth_pow_continued_fraction.py
bug1 from continued_fraction_dc:
    cf, xs = nth_pow_continued_fraction(2,3,102)
    assert 0 in cf

    that is:
    one = sympify(1)
    N = (-18946643396438422418200496503661148314139229271682874349*2**(one/3)
         + 23871274840024462774930909433822752859720888716067576820
         )
    D = (-133450479581198331510402510274281177418327310779117149571
         + 105919715836427477757469402582631193698068222179903783354*2**(one/3)
         )
    # assert xs[101] == N/D
    assert floor(N/D) == 0 # should be 1
    assert N > D
    assert D > N
    assert N-D > 0
    assert not (D-N < 0)
    assert str((N-D).evalf(10)) == '1.690148127e-57'

bug2 from root-finding/intervals:
    var('W')
    A, B = 1,2
    x = A+B*W
    A, B = map(Wild, 'A, B'.split(', '))
    X = A+B*W
    m = X.matches(x)
    assert m == {A: 2*W, B: 1/W}

bug3 or not: from __to_std_args_for_NthPow:
    cannot simplify: '-18**(1/3)/3 + 2**(1/3)*3**(2/3)/3' to 0
    
'''


'''
std lib bugs from nth_pow_continued_fraction__using_sympy.py
bug1 argparse - from main:
    group = parser.add_mutually_exclusive_group()#required=True)
    group.add_argument('-d', '--cf_digits', type=int,
                        nargs = '+')
    group.add_argument('-f', '--from_file', type=argparse.FileType())

    run with: "-d 1 3 1  -f afsaf" # no such file
        error: argument -f/--from_file:
        can't open 'afsaf': [Errno 2] No such file or directory: 'afsaf'
    run with: "-d 1 3 1  -f r.bat" # file exist
        error: argument -f/--from_file:
        not allowed with argument -d/--cf_digits
    I think it is a bug, you cannot open a file first before parsing args.
    
'''





__all__ = to_names('''
nth_pow_continued_fraction, continued_fraction_expand\
, continued_fraction_expand_with_Xi
''')



one = sympify(1)
two = 2*one
zero = one-one





def rsimplify(x):
    y = simplify(x)
    while y != x:
        x = y
        y = simplify(x)
    return y


def calc_until(pred_calc_at_prec, factor=2):
    prec = 4
    enough = False
    while not enough:
        prec *= factor
        # 1000 is too large for python or sympy
        if prec >= 1000:
            raise OverflowError()
        #print(prec)
        enough, result = pred_calc_at_prec(prec)
    return result
    
def pred_divmod1(prec, x):
    _x = x.evalf(prec)
    int_part = floor(_x)
    r = x - int_part

    # 0 <= r < 1
    _r = r.evalf(prec)
    enough = bool(0 <= _r < 1)
##    if enough:
##        _r2 = r.evalf(prec**2)
##        if _r.evalf(5) != _r2.evalf(5):
##            print(pred_divmod1, _r, _r2)
##            enough = False
    return enough, (int_part, r)

def divmod1(x):
    pred_x_divmod1 = lambda prec: pred_divmod1(prec, x)
    int_part, r = calc_until(pred_x_divmod1)
    return int_part, r


# try ratsimp error
# try radsimp yeah! only for sqrt
def continued_fraction_dc(x):
    '''return (floor(x), None if [INT x] else 1/(x-floor(x)))'''
    
    int_part, r = divmod1(x)
    
    r = radsimp(rsimplify(r))
    next_x = None if r == 0 else 1/r
    return int_part, next_x

def continued_fraction_expand(x, continued_fraction_next=continued_fraction_dc):
    return _continued_fraction_expand(x, continued_fraction_next)
def continued_fraction_expand_with_Xi(x, continued_fraction_next=continued_fraction_dc):
    return _continued_fraction_expand_with_Xi(x, continued_fraction_next)




x2NDs = lambda x, L=10:list(islice(
    continued_fraction_pack_to_ND_pairs(
        continued_fraction_expand(x)),
    L))





##################################################





def __to_std_args_for_NthPow__base_n(base, n):
    assert isinstance(base, Rational)
    assert isinstance(n, Rational)
    base, n = map(Fraction, [base, n])
    if n < 0:
        base = 1/base
        n = -n
    base = base ** n.denominator
    n = n.numerator
    return base, n

def __to_std_args_for_NthPow__ABCD(A, B, C, D):
    Ds = denominators = [rational2pair(x)[-1] for x in [A, B, C, D]]
    M = lcms(*Ds)
    A, B, C, D = (rational2int(x*M) for x in [A, B, C, D])
    return A, B, C, D
    
def to_std_args_for_NthPow(base, n, A, B, C, D):
    if not all(isinstance(x, Rational) for x in [base, n, A, B, C, D]):
        raise TypeError('not all Rational: [base, n, A, B, C, D]')
    base, n = __to_std_args_for_NthPow__base_n(base, n)
    A, B, C, D = __to_std_args_for_NthPow__ABCD(A, B, C, D)
    base_N, base_D = rational2pair(base)
    
    base, n, A, B, C, D = __to_std_args_for_NthPow(base_N, base_D, n, A, B, C, D)
    g = gcds(A, B, C, D)
    if B < 0 or B==0 and A<0:
        g = -g
    A, B, C, D = map(lambda x:x//g, [A, B, C, D])
    assert not (B < 0 or B==0 and A<0)

    if signs(A)== 0 ==signs(B, base):
        # zero
        base = 0
        n = 1
        B, D = A, C = 0, 1
    return base, n, A, B, C, D

def __to_std_args_for_NthPow(base_N, base_D, n, A, B, C, D):
    r'''x = (A+B*W)/(C+D*W); W = base**(1/n); base=base_N/base_D
[INT A, B, C, D, base_N, base_D, n][base_D, n > 0]
[C*D != 0][A/C==B/D] or [base >= 0 or ODD n][C+D*W != 0]
[C+D*W != 0] ==>> [C*D*W > 0]
    or [C*D*W < 0][C**n != (-D)**n * base]
    or [C*D*W == 0][C+D*base != 0]'''
    if not all(type(i) is int for i in [A, B, C, D, base_N, base_D, n]):
        raise TypeError('not [INT A, B, C, D, base_N, base_D, n]')
    if not all(i > 0 for i in [base_D, n]):
        raise ValueError('not [base_D, n > 0]')

    def rational2args(A, C):
        base = 0
        base_N, base_D, n = 0, 1, 1
        W = 0
        A_C = Fraction(A,C)
        A, C = rational2pair(A_C)
        B, D = A, C
        new = (base, n, A, B, C, D)
        return new
    
    base = Fraction(base_N, base_D)
    old = (base, n, A, B, C, D)
    if (signs(C, D) != 0) and (A*D==B*C):
        # rational, I donot what W is
        return rational2args(A, C)

    new = None
    try:
        sign_base = signs(base_N, base_D)
        if not (sign_base >= 0 or n % 2):
            raise ValueError('not [base >= 0 or ODD n]')
        sign_W = sign_base

        if signs(C, D, sign_W) > 0:
            pass
        elif signs(C, D, sign_W) < 0:
            if not (C**n != (-D)**n * base):
                raise ValueError('not [C+D*W != 0]')
        else:
            if signs(C) == 0 == signs(D, base): #not (C+D*base != 0):
                raise ValueError('not [C+D*W != 0]')

        if sign_base == 0:
            new = rational2args(A, C)
            return new
        if sign_base < 0:
            base *= sign_base
            B *= sign_base
            D *= sign_base
            sign_W = sign_base = sign_base*sign_base

        assert base > 0
        prime2exp = factor_frac(base)
        prime2divmod_exp_n = {p:divmod(exp, n)
                              for p, exp in prime2exp.items()}
        prime2exp_out_nth_pow = {p:q for p, (q,r) in
                                 prime2divmod_exp_n.items()}
        prime2exp_in_nth_pow = {p:r for p, (q,r) in
                                 prime2divmod_exp_n.items()}
        coeff_new_base = prime2exp_to_frac(prime2exp_out_nth_pow)
        _new_base = prime2exp_to_frac(prime2exp_in_nth_pow)
        new_base = _new_base.numerator
        assert new_base == _new_base
        assert coeff_new_base**n * new_base == base


        cN, cD = rational2pair(coeff_new_base)
        # W_ = new_base**(1/n); W == cN/cD*W_
        A, C = A*cD, C*cD
        B, D = B*cN, D*cN
        base = new_base

        if base == 1:
            new = rational2args(A+B, C+D)
            return new
        assert n >= 2
        assert base >= 2

        new = (base, n, A, B, C, D)
        return new
        
    finally:
        def calc_x(base, n, A, B, C, D):
            W = (one*base)**(one/n)
            x = (A+B*W)/(C+D*W)
            return x
        
        if new is not None:
            try:
                # tolerance=0 is the same as None
                #assert sympify('1e-10000000000000000').nsimplify(tolerance=0) == 0
                #assert rsimplify((calc_x(*old) - calc_x(*new)).nsimplify(tolerance=0)) == 0

                # how to simplify : '-18**(1/3)/3 + 2**(1/3)*3**(2/3)/3'
                assert nsimplify((calc_x(*old) - calc_x(*new))) == 0
            except Exception as e:
                print('{} =?= {}'.format(old, new))
                print((calc_x(*old) - calc_x(*new)).simplify())
                assert nsimplify((calc_x(*old) - calc_x(*new))) == 0
                raise
    raise logic-error

class NthPow(namedtuple('NthPowBase', 'base, n, A, B, C, D'.split(', '))):
    #__slots__ = ('__one',)
    def __new__(subclass, base_N, base_D, n, A, B, C, D):
        base = Fraction(base_N, base_D)
        base, n, A, B, C, D = to_std_args_for_NthPow(base, n, A, B, C, D)
        assert all(type(i) is int for i in [base, n, A, B, C, D])
        assert base >= 0
        assert n >= 1
        
        this_class = __class__
        self = super(this_class, subclass).__new__(
            subclass, base, n, A, B, C, D)
        #self.__one = 
        return self

    def __bool__(self):
        return not self.A == 0 == self.B
    def is_rational(self):
        return self.base == 0
    def to_rational(self):
        if not self.is_rational():
            return ValueError('self is not rational')
        return Fraction(self.A, self.C)

    def __floor__(self):
        base, n, A, B, C, D = self
        try:
            return self.__floor_x(base, n, A, B, C, D)
        except:
            print(base, n, A, B, C, D)
            raise

    def floor(self):
        return self.__floor__()

    def divmod1(self):
        q = self.floor()
        r = self - q
        return q, r

    def inv(self):
        if not self:
            raise ZeroDivisionError('self.inv() but self==0')
        base, n, A, B, C, D = self
        A, B, C, D = C, D, A, B
        return __class__(base, 1, n, A, B, C, D)

    @staticmethod
    def __to_rational_or_raise_NotImplemented(other):
        if isinstance(other, Rational):
            return other
        if isinstance(other, __class__) and other.is_rational():
            return other.to_rational()
        raise NotImplemented
    def __rtruediv__(self, other):
        other = self.__to_rational_or_raise_NotImplemented(other)
        return self.inv() * other
    def __truediv__(self, other):
        if isinstance(other, Rational):
            other = 1/other
        elif isinstance(other, __class__):
            other = other.inv()
        else:
            raise NotImplemented
        
        return self * other

    def __mul_try_reduce(self, other):
        assert isinstance(other, __class__)
        #print(self.__mul_try_reduce)
        if (self.base, self.n) != (other.base, other.n):
            raise NotImplemented
        for self, other in [(self, other), (other, self)]:
            self_gD = gcds(self.C, self.D)
            other_gN = gcds(other.A, other.B)
            C, D = self.C//self_gD, self.D//self_gD
            A, B = other.A//other_gN, other.B//other_gN
            if (C,D) == (A,B):
                break
            if (C,D) == (-A,-B):
                other_gN = -other_gN
                break
            
        else:
            raise NotImplemented

        # self.Nu/self_gD * other_gN/other.De
        base, n = self.base, self.n
        A, B = self.A, self.B
        C, D = other.C, other.D
        fr = Fraction(other_gN, self_gD)
        return __class__(base, 1, n, A, B, C, D) * fr
            
            
    def __mul__(self, other):
        if isinstance(other, Rational):
            pass
        elif isinstance(other, __class__):
            #print(self.__mul__)
            if other.is_rational():
                pass
            elif self.is_rational():
                other, self = self, other
            else:
                return self.__mul_try_reduce(other)
                raise NotImplemented
            other = other.to_rational()
        else:
            raise NotImplemented
        #other = self.__to_rational_or_raise_NotImplemented(other)

        N_, D_ = rational2pair(other)
        base, n, A, B, C, D = self
        base, n, A, B, C, D = base, n, A*N_, B*N_, C*D_, D*D_
        return NthPow(base, 1, n, A, B, C, D)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pos__(self):
        return self
    def __neg__(self):
        base, n, A, B, C, D = self
        C = -C
        D = -D
        return NthPow(base, 1, n, A, B, C, D)

    def __add__(self, other):
        return (self).__sub__(-other)
    def __radd__(self, other):
        return (self).__sub__(-other)
    def __rsub__(self, other):
        return (-self).__sub__(-other)
    def __sub__(self, other):
        if isinstance(other, Rational):
            if isinstance(other, Integral):
                return self.__sub_Integral(other)
            return self.__sub_Rational(other)
        if isinstance(other, __class__):
            return self.__sub_this_class(other)
        raise NotImplemented
    def __sub_Rational(self, other):
        #other = Fraction(other)
        other_N, other_D = rational2pair(other)
        base, n, A, B, C, D = self
        C, D = C*other_D, D*other_D
        A, B = A*other_D, B*other_D
        A_, B_ = self.C*other_N, self.D*other_N
        A -= A_
        B -= B_
        return NthPow(base, 1, n, A, B, C, D)
        
    def __sub_Integral(self, other):
        other = int(other)
        base, n, A, B, C, D = self
        A_, B_ = C*other, D*other
        A -= A_
        B -= B_
        return NthPow(base, 1, n, A, B, C, D)
    def __sub_this_class(self, other):
        base, n, A, B, C, D = self
        base_, n_, A_, B_, C_, D_ = other
        if (base, n) != (base_, n_):
            if other.is_rational():
                return self - other.to_rational()
            if self.is_rational():
                return (-other) - (-self.to_rational())
            raise ValueError('sub: not the same base**(1/n)')
        if (C, D) != (C_, D_):
            raise ... # to fixed me; gcds(denominator..)....
            raise ValueError('sub: not the same denominator')

        A -= A_
        B -= B_
        return NthPow(base, 1, n, A, B, C, D)

    def to_sympy(self):
        base, n, A, B, C, D = self
        W = (one*base)**(one/n)
        x = (A+B*W)/(C+D*W)
        return x
    @staticmethod
    def __floor_x(base, n, A, B, C, D):
        if base == 0:
            return __class__.__floor_x__base_eq0(base, n, A, B, C, D)
        else:
            return __class__.__floor_x__base_gt0(base, n, A, B, C, D)
    @staticmethod
    def __floor_x__base_eq0(base, n, A, B, C, D):
        return Fraction(A, C).__floor__()

    @staticmethod
    def __floor_x__base_gt0(base, n, A, B, C, D):
        '''x = (A+B*W)/(C+D*W); W = base**(1/n);
    [INT A, B, C, D, base, n]

    q = floor(x)
    x (C+D*W) = (A+B*W)
    (x C+x D*W) = (A+B*W)
    (x*C - A) = (B - x*D)*W
    (x*C - A)**n = (B - x*D)**n * base
        (x*C - A)**n = (B - x*D)**n * (W * e**(2pi*k/n))**n for k=0..n-1
        roots of above = (A+B*W'[k])/(C+D*W'[k]) where W' = W * e**(2pi*k/n)
        root is not real unless A/C = B/D or k = 0
        in both case, x is the ONLY real root.

    use intervals to calc floor(x)
    '''
        assert all(type(i) is int for i in [base, n, A, B, C, D])
        assert all(i > 0 for i in [base, n])

        
        x = symbols('x', real=True)
        f = (x*C - A)**n - (B - x*D)**n * base
        f = Poly(f, x)

        '''any x > X: f(x) holds sign:
let M = max(map(abs, [A, C, B, D])), LC = (C**n - (-D)**n * base)
assert LC != 0
f = x**n (C**n - (-D)**n * base)
    + sum x**d C(n,d) (C**d*(-A)**(n-d) -base*((-D)**d*B**(n-d)) {d=0..n-1}
x > 0:
f/LC >= x**n - sum x**d C(n,d) (M**n+base*M**n) {d=0..n-1}/LC
    = x**n - M**n (1+base)/abs(LC) sum x**d C(n,d)  {d=0..n-1}
    = x**n - M**n (1+base)/abs(LC) ((x+1)**n - x**n)
    = (1+M**n (1+base)/abs(LC))x**n - M**n (1+base)/abs(LC) (x+1)**n
    >= 0
    0 < abs(LC) <= M**n (1+base)
<<== (abs(LC)+M**n (1+base))x**n >= M**n (1+base) (x+1)**n
    abs(LC)/(M**n (1+base)) + 1 >= (1+1/x)**n

f/LC >= x**n - M**n (1+base)/abs(LC) sum x**d C(n,d)  {d=0..n-1}
    > x**n - M**n (1+base)/abs(LC) sum x**d 2**n  {d=0..n-1}
    = x**n - 2**n M**n (1+base)/abs(LC) (x**n-1)/(x-1)
    >= 0
<<== [x>1]: 0 <= x**n (x-1)abs(LC) - 2**n M**n (1+base) (x**n-1)
    = x**(n+1)abs(LC) - x**n abs(LC) - 2**n M**n (1+base) x**n + 2**n M**n (1+base)
    > x**(n+1)abs(LC) - (abs(LC) + 2**n M**n (1+base)) x**n
    <<== x abs(LC) - (abs(LC) + 2**n M**n (1+base)) >= 0
    <<== x >= (1 + 2**n M**n (1+base)/abs(LC))
'''
##        M = max(map(abs, [A, C, B, D]))
##        LC = (C**n - (-D)**n * base)
##        K = M**n * (1+base)
##        abs_LC = abs(LC)
##        assert K >= abs_LC > 0
##        SUP = 2 + (2**n * M**n * (1+base))//abs(LC)
####        print()
####        r = refine_root(f, -SUP, SUP)
####
##        assert 1 == count_roots(f, inf=-SUP, sup=SUP)
##        _rs = intervals(f, inf=-SUP, sup=SUP)
        _rs = intervals(f)
        #print(__class__.__floor_x, _rs)
        rs = []
        for (low, up), _ in _rs:
            if low.is_real and up.is_real:
                rs.append(((low, up), _))
        if len(rs) != 1:
            print(rs)
        r, = rs
        (low, up), M = r

        assert low.is_integer
        assert up.is_integer
        assert up <= low+1
        if low.is_integer and (low == up or low + 1 == up):
            return int(low)
        raise logic-error

    
# version1

def nth_pow_continued_fraction__using_sympy_float(x, n, L,
        continued_fraction_next=continued_fraction_dc):
    x0 = x**(one/n)
    return itertools.islice(
        continued_fraction_expand(x0, continued_fraction_next), L)

def continued_fraction_next__for_nth_pow(nth_pow_obj):
    q, r = nth_pow_obj.divmod1()
    assert type(q) is int
    next_x = None if not r else r.inv()
    return q, next_x

def nth_pow_continued_fraction(x, n, L,
        continued_fraction_next=continued_fraction_next__for_nth_pow,
        *, A=0, B=1, C=1, D=0):
    xN, xD = rational2pair(x)
    x0 = NthPow(xN, xD, n, A, B, C, D)
    return itertools.islice(
        continued_fraction_expand(x0, continued_fraction_next), L)


    


#cf, xs = nth_pow_continued_fraction(2,3,102)
#cf, xs = nth_pow_continued_fraction(2,3,116)
##cf = nth_pow_continued_fraction(2,3,12)
##cf, xs = unzip(2, continued_fraction_expand_with_Xi(2**(one/3)), 200)
##



def main(args = None):
    import argparse, sys
    from operator import attrgetter

    top_parser = argparse.ArgumentParser(
        description=r'continued_fraction')
    subparsers = top_parser.add_subparsers(dest='cmd_name')#, required=True)

    #########################  expand   ######################
    parser = expand = subparsers.add_parser(
        'expand', aliases=['ex'],
        description=
        r'continued_fraction of x = (A+B*W)/(C+D*W) '
        'where W = base**(1/n);')
    parser.add_argument('base', type=Fraction, help='base::rational')
    parser.add_argument('n', type=Fraction, help='1/exp::rational')
    parser.add_argument('L', type=int, help='expanded length. -1 stands for inf')
    parser.add_argument('A', type=Fraction,
                        help='coeff : A::rational : default=0',
                        nargs='?', default=0)
    parser.add_argument('B', type=Fraction,
                        help='coeff : B::rational : default=1',
                        nargs='?', default=1)
    parser.add_argument('C', type=Fraction,
                        help='coeff : C::rational : default=1',
                        nargs='?', default=1)
    parser.add_argument('D', type=Fraction,
                        help='coeff : D::rational : default=0',
                        nargs='?', default=0)
    parser.add_argument('-b', '--show_x0', action='store_true',
                        help='show x[0] at beginning', default=False)
    parser.add_argument('-a', '--show_all_xs', action='store_true',
                        help='show x[i] for i=0..L-1', default=False)
    parser.add_argument('-t', '--show_xt', action='store_true',
                        help='show x[L] at the end or 1/0 if NaN; '
                        'actual L may be less than the input one',
                        default=False)

    #########################  pack   ######################
    parser = pack = subparsers.add_parser(
        'pack', aliases=['pk'],
        description=
        r'1) pack continued_fraction into rational; or '
        '2) given the original x (=x[0]) and the first L continued_fraction '
        'digits to calc x[L]; '
        'x is in form of (A+B*W)/(C+D*W) where W = base**(1/n);')
    group = parser.add_mutually_exclusive_group()#required=True)
    group.add_argument('-d', '--cf_digits', type=int,
                        nargs = '+', #default=[],
                        help='continued fraction digits::[int]')
    group.add_argument('-f', '--from_file', type=argparse.FileType(),
                        help='get digits from file; if no [-d, -f] then read from stdin')

    
    parser.add_argument('-W', '--base_n', type=Fraction,
                        nargs = 2, default=None,
                        help='set value: base, n; if set, perform 2) else 1)')
    parser.add_argument('-K', '--ABCD', type=Fraction,
                        nargs = 4, default=(0,1,1,0),
                        help='set value: A, B, C, D; default = (0,1,1,0)')

    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-a', '--show_all', action='store_true',
                        default=None,
                        help='show all fractions or x[i]')
    group.add_argument('-t', '--show_last', type=int, default=None,
                        help='show some last fractions or x[i]; (default=2)')
    group.add_argument('-b', '--show_first', type=int, default=None,
                        help='show some first fractions or x[i]')
    
    

    
    #############################    switch    ####################
    


    
    parser = top_parser
    args = parser.parse_args(args)
    cmd = args.cmd_name
    cmd2subparser = subparsers.choices
    if cmd is None:
        #raise TypeError('missing a required subcommand')
        err = sys.__stderr__
        print('missing a required subcommand', file = err)
        print(list(cmd2subparser.keys()), file = err)
        parser.exit(1)
    using = cmd2subparser[cmd]
    if using is expand:
        return __main_expand(parser, args)
    if using is pack:
        return __main_pack(parser, args)
    parser.exit(0)
    raise logic-error
    
def __main_pack(parser, args):
    import argparse, sys
    from operator import attrgetter
    cf_digits, from_file, base_n, ABCD, show_all, show_last, show_first = \
          attrgetter(*'cf_digits, from_file, base_n, ABCD'
                     ', show_all, show_last, show_first'
                     .split(', '))(args)
    

    # set x0
    if base_n:
        base, n = base_n
        if int(n) != n:
            raise ValueError('n should be integer')
        n = int(n)
        A, B, C, D = ABCD
        xN, xD = rational2pair(base)
        x0 = NthPow(xN, xD, n, A, B, C, D)
    else:
        x0 = None



    # set cf_digits
    if cf_digits is not None and from_file is not None:
        raise logic-error

    def read_digits(file):
        with file as fin:
            for line in file:
                # remove comment
                i = line.find('#')
                if i != -1:
                    line = line[:i]

                # read number
                for word in line.replace(',', ' ').split():
                    yield int(word)
                    
        
    if from_file is not None:
        cf_digits = read_digits(from_file)
    elif cf_digits is None:
        cf_digits = read_digits(sys.__stdin__)

    NDs = continued_fraction_pack_to_ND_pairs(cf_digits)
            
    if x0 is not None:
        it = calc_Xs_from_NDs(x0, NDs)
        T = lambda xi, i: 'x[{}] = {} = {}'.format(i, xi, xi.to_sympy())
    else:
        it = NDs
        T = lambda ND, i: 'N[{i}]/D[{i}] = {fr}'.format(fr = Fraction(*ND), i=i)
        
        
    start = 0
    if show_all is not None:
        it = it
    elif show_first is not None:
        it = islice(it, show_first)
    else:
        if show_last is None:
            show_last = 2
        #it = iter(deque(it, show_last))
        d = deque((), show_last)
        i = -1
        for i, e in enumerate(it):
            d.append(e)
        LEN = i+1
        start = max(LEN - show_last, 0)
        it = iter(d)

    for i, data in enumerate(it, start):
        string = T(data, i)
        print(string)

    parser.exit(0)
    raise logic-error
        
    
def __main_expand(parser, args):
    import argparse, sys
    from operator import attrgetter
    base, n, L, A, B, C, D, show_x0, show_xt, show_all_xs = \
          attrgetter(*'base, n, L, A, B, C, D, show_x0, show_xt, show_all_xs'
                     .split(', '))(args)

    try:
        #print('here')
        if L == -1:
            L = None
        elif L < 0:
            raise ValueError('L < 0 but not -1 (inf)')
##        n = sympify(n)
##        x = sympify(x)
##        assert n.is_positive
##        #assert x.is_positive
##        assert x.is_real
        #print('here')

        #n, x = map(Fraction, [n, x])
        
    except Exception as e:
        print(type(e), e, sep='\n', file=sys.__stderr__)
        raise
        parser.exit(1)
        raise logic-error

    xN, xD = rational2pair(base)
    x0 = NthPow(xN, xD, n, A, B, C, D)
    #it = nth_pow_continued_fraction(base, n, L, A=A, B=B, C=C, D=D)
    it = itertools.islice(continued_fraction_expand_with_Xi(
        x0, continued_fraction_next__for_nth_pow), L)

    show_x = lambda x, i:print('# x[{}] = {!r} = {}'.format(i, x, x.to_sympy()))

    x0_will_be_showed_in_loop = show_all_xs and (L is None or L > 0)
    if show_x0 and not x0_will_be_showed_in_loop:
        show_x(x0, 0)
    i = -1
    xi = None
    for i, (c, xi) in enumerate(it):
        if show_all_xs:
            show_x(xi, i)
        print(c)
    else:
        assert L is None or -1 <= i <= L-1
        t = L = i + 1
        
    x0_showed = show_x0 or show_all_xs and i >= 0
    t = i + 1
    if show_xt and not (x0_showed and t == 0):
        # x[i] == x[t-1]
        t = i + 1
        if xi is None:
            xt = x0
            assert L == 0 == t
            assert not x0_showed
        else:
            ct, xt = continued_fraction_next__for_nth_pow(xi)

        if xt is None:
            print('# x[{}] = 1/0 = 1/0'.format(t))
        else:
            show_x(xt, t)
            
        

    parser.exit(0)
    raise logic-error
    


if __name__ == "__main__":
    main()












    







