
'''
sum f i {~i=a->b} = sum f i {i=a..b-1} - sum f i {i=b..a-1}


B = Bernoulli numbers
[NN d>=0]:
    sum i**d {~i=0->n} = 1/(d+1) sum C(d+1,k) B[k] n**(d+1-k) {k=0..d}

    [n=1]: left = 0**d = [d=0] = right = 1/(d+1) sum C(d+1,k) B[k] {k=0..d}
    sum C(d+1,k) B[k] {k=0..d} = [d=0](d+1) = [d=0]
    C(d+1,d) B[d] = [d=0](d+1) - sum C(d+1,k) B[k] {k=0..d-1}
    B[d] = [d=0] - 1/(d+1) * sum C(d+1,k) B[k] {k=0..d-1}


    [n=-1]: left = -(-1)**d = right = 1/(d+1) sum C(d+1,k) B[k] (-1)**(d+1-k) {k=0..d}
    1 = 1/(d+1) sum C(d+1,k) B[k] (-1)**k {k=0..d}
    1 + [d=0] = 1/(d+1) sum C(d+1,k) B[k] (1+(-1)**k) {k=0..d}
        = 1/(d+1) sum C(d+1,2k) B[2k] 2 {k=0..d//2}
    [d=2K]: 1+[K=0] = 2/(2K+1) sum C(2K+1,2k) B[2k] {k=0..K}
    B[2K] = (1+[K=0])/2 - 1/(2K+1)sum C(2K+1,2k) B[2k] {k=0..K-1}

T = tangent numbers
tan z = sum T[i] z**i/i! {NN i}
T[2*i] = 0 # B[2*i+1] = 0 except B[2*0+1] = -1/2
T[2*i-1] = (-4)**i (1-4**i) B[2*i]/2/i is in PZ # 1 2 16 272 7936 353792 22368256
[i>0]: T[i] = (2I)**(i+1) (1-2**(i+1)) B[i+1]/(i+1)
let U[i] = (2I)**i (1-2**i) B[i]/i
let U[0]=lim U[i] {i->0} = -ln2 B[0]
U[1] = -(2I) B[1]
tan z = sum U[i+1] z**i/i! {NN i} - U[0+1]+T[0]
DD \z:sum U[i]z**i/i! {NN i} z = tan z + U[1]

[i>0]: B[2*i] = T[2*i-1] 2*i/(-4)**i/(1-4**i)

def tf d z =
    tf 0 z = z
    [d>0]: tf d z = (1+z**2) DD (tf (d-1))
    # tf -1 z = SS z/(1+z**2) {~z} = 1/2 ln (1+z**2) + C

    T[i] = tf i 0

'''



from .numberss import NumberList
from .choose import choose as C
from fractions import Fraction

one = Fraction(1)

class BernoulliNumber(NumberList):
    def _calc_neg(self, n, nums):
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        if n == 0:
            return one

        B = nums
        S = sum(C(n+1,k)*B[k] for k in range(n) if B[k])
        Bn = - S/(n+1)
        if n % 2:   # 2k+1
            assert n == 1 or Bn == 0
        elif n % 4: # 4k+2
            assert Bn > 0
        else:       # 4k
            assert n == 0 or Bn < 0
        return Bn
        raise NotImplementedError()
    def direct_calc(self, n):
        raise NotImplementedError()

    
    def __init__(self):
        super().__init__([one])
    
bernoulli = BernoulliNumber()
#print(bernoulli.get_first(6))
assert bernoulli.get_first(6) == \
       [Fraction(1, 1), Fraction(-1, 2), Fraction(1, 6),
        Fraction(0, 1), Fraction(-1, 30), Fraction(0, 1)]











