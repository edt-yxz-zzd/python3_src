r'''
sum_pow_X_I_pow_I_K
Sum[x^i i^k, {i, 0, n}]

see:
    "NOTE/wolframalpha.com/sum2.txt"

[n <- ZZ][k <- NN]
[x != 1][x != 0][k>0]:
    let S(x,j) = (sum x^e * Eulerian_1st(j,e) {e=0..j})
        Eulerian_1st(n,k)
            = Eulerian<n,k> = Eulerian<n-1,k-1>*(n-k) + Eulerian<n-1,k>*(k+1)
            Eulerian<0,k> = [k==0]
    Sum[x^i i^k, {i, 0, n}]
        = (x^(n + 1) sum (-1)^j C(k,j) n^(k-j) (x - 1)^(k-j) S(x,j) {j=0..k}
          - x (-1)^k S(x,k)
          )/(x - 1)^(k + 1)
[x != 1][k == 0]:
    Sum[x^i i^k, {i, 0, n}]
        = Sum[x^i i^0, {i, 0, n}]
        = Sum[x^i, {i, 0, n}]
        = (x^(n + 1) - 1)/(x - 1)

[x == 1]:
    # B = Bernoulli numbers
    let B[d] = [d=0] - 1/(d+1) * sum C(d+1,k) B[k] {k=0..d-1}
        C(n,k) = binomial(n,k) = n!/(k!*(n-k)!)
    Sum[x^i i^k, {i, 0, n}] = Sum[i^k, {i, 0, n}]
        = 1/(k+1) * sum C(k+1,j)*B[j]* (n+1)^(k+1-j) {j=0..k}

[x == 0]:
    Sum[x^i i^k, {i, 0, n}] = Sum[0^i i^k, {i, 0, n}]
        = Sum[[i==0] i^k, {i, 0, n}]
        = Sum[[i==0] 0^k, {i, 0, n}]
        = Sum[[i==0][k==0], {i, 0, n}]
        = [n>=0][k==0]

'''

__all__ = '''
    sum_pow_X_I_pow_I_K
    sum_pow_X_I_pow_I_K__def

    sum_pow_X_I_pow_I_K__x_eq_1
    sum_pow_X_I_pow_I_K__x_eq_0
    sum_pow_X_I_pow_I_K__x_ne_1__k_eq_1
    sum_pow_X_I_pow_I_K__x_ne_01__k_ge_1
    '''.split()

from nn_ns.math_nn.numbers.Bernoulli_number import bernoulli
from nn_ns.math_nn.numbers.choose import choose
from nn_ns.math_nn.numbers.Eulerian_number import eulerian_1st
from fractions import Fraction
import itertools

B = bernoulli
C = choose
E = eulerian_1st

'''
sum_pow_X_I_pow_I_K__def(x=?,k=0,n=0)
    = x^0 * 0^k
    = ?^0 * 0^0
    = 1
'''
def sum_pow_X_I_pow_I_K__def(x, k, n):
    'Sum[x^i i^k, {i, 0, n}]'
    assert k >= 0
    return sum(x**i * i**k for i in range(0, n+1))
def sum_pow_X_I_pow_I_K(x, k, n):
    assert k >= 0
    if n < 0:
        return zero
    if x == 1:
        return sum_pow_X_I_pow_I_K__x_eq_1(k, n)
    elif x == 0:
        return sum_pow_X_I_pow_I_K__x_eq_0(k, n)
    elif k == 0:
        return sum_pow_X_I_pow_I_K__x_ne_1__k_eq_1(x, n)
    else:
        return sum_pow_X_I_pow_I_K__x_ne_01__k_ge_1(x, k, n)
def reverse_powers(base, begin, end):
    powers = list_powers(base, end+1, begin+1)
    powers.reverse()
    return powers
def list_powers(base, begin, end):
    assert 0 <= begin <= end
    L = end - begin
    assert L >= 0
    if L == 0:
        powers = []
    else:
        power = base**begin
        powers = [power]
        for _ in range(L-1):
            power *= base
            powers.append(power)
    assert len(powers) == L
    return powers

def S(x,j):
    'S(x,j) = (sum x^e * Eulerian_1st(j,e) {e=0..j})'
    x_powers = list_powers(x, 0, j1)
    return S_ex(x_powers,j)
def S_ex(x_powers,j):
    Es = eulerian_1st.get_row(j)
    j1 = j+1
    assert len(Es) == j1
    assert len(x_powers) >= j1
    return sum(x_power*e for x_power, e in zip(x_powers, Es))

one = Fraction(1)
zero = Fraction(0)
def sum_pow_X_I_pow_I_K__x_ne_1__k_eq_1(x, n):
    '(x^(n + 1) - 1)/(x - 1)'
    return (x**(n+1) - 1)*one/(x-1)
def sum_pow_X_I_pow_I_K__x_ne_01__k_ge_1(x, k, n):
    '''
Sum[x^i i^k, {i, 0, n}]
    = (x^(n + 1) sum (-1)^j C(k,j) n^(k-j) (x - 1)^(k-j) S(x,j) {j=0..k}
      - x (-1)^k S(x,k)
      )/(x - 1)^(k + 1)
'''
    assert x != 1
    assert x != 0
    assert k >= 1
    assert n >= 0
    #Cs = C.get_row(k)
    Cs = get_C_row(k)
    k1 = k+1
    x1 = x-1
    n_powers = reverse_powers(n, k, -1)
    x1_powers = reverse_powers(x1, k, -1)
    x_powers = list_powers(x, 0, k1)
    iter_Js = range(0, k1)
    Ss = [S_ex(x_powers, j) for j in iter_Js]
    assert len(Cs) == k1
    assert len(n_powers) == k1
    assert len(x1_powers) == k1
    assert len(x_powers) == k1
    assert len(Ss) == k1
    iter_sign_powers = itertools.cycle([1,-1])
    sum1 = sum(sign_power*c*n_power*x1_power*s
                for sign_power, c, n_power, x1_power, s
                    in zip(iter_sign_powers, Cs, n_powers, x1_powers, Ss)
                )
    x_power = x**(n+1)
    '''
    print(f'x1_powers={x1_powers}')
    print(f'Cs={Cs}')
    print(f'Ss={Ss}')
    print(f'sum1={sum1}')
    print(f'x_power={x_power}')
    '''

    return (x_power*sum1 - x* (-1)**k * Ss[k])*one/x1**k1

def get_C_row(i):
    assert i >= 0
    half_Cs = C.get_row(i)
    Cs = half_Cs + half_Cs[::-1] if i&1 == 1 else half_Cs[:-1] + half_Cs[::-1]
    return Cs
def sum_pow_X_I_pow_I_K__x_eq_1(k, n):
    '''
Sum[x^i i^k, {i, 0, n}] = Sum[i^k, {i, 0, n}]
    = 1/(k+1) * sum C(k+1,j)*B[j]* (n+1)^(k+1-j) {j=0..k}
'''
    assert k >= 0
    assert n >= 0
    k1 = k+1
    #Cs = C.get_row(k1)
    Cs = get_C_row(k1)
    Bs = B.get_first(k1)

    n1 = n+1
    n1_powers = reverse_powers(n1, k1, 0)

    assert len(Cs)-1 == k1
    assert len(Bs) == k1
    assert len(n1_powers) == k1
    assert n1_powers[-1] == n1

    s = sum(c*b*n1_power for c, b, n1_power in zip(Cs, Bs, n1_powers))
    return s*one/k1

def sum_pow_X_I_pow_I_K__x_eq_0(k, n):
    '''
Sum[x^i i^k, {i, 0, n}] = Sum[0^i i^k, {i, 0, n}]
    = [n>=0][k==0]
'''
    assert k >= 0
    assert n >= 0
    return one if k == 0 else zero
def _test():
    for x in range(-1, 3):
     for k in range(0, 6):
      for n in range(-1, 5):
        s = sum_pow_X_I_pow_I_K(x,k,n)
        s_def = sum_pow_X_I_pow_I_K__def(x,k,n)
        try:
            assert s == s_def
        except:
            print(f'x={x}')
            print(f'k={k}')
            print(f'n={n}')
            print(f's={s}')
            print(f's_def={s_def}')
            raise


if __name__ == '__main__':
    _test()


