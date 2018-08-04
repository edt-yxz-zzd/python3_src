

'''

derangement = permutation which moves every item
subfactorial[n] = numbers of all derangements of n objects, int n>=0
subfactorial[0] = 1
subfactorial[1] = 0
subfactorial[2] = 1
subfactorial[3] = 2

n! = sum C(n,i)subfactorial[i] {i} // subfactorial is Newton series of n!  !!!!!
factorial = G.subfactorial
==>> subfactorial = H.factorial
    subfactorial[n] = sum C(n,i)(-1)**(n-i) i! {i>=0}
        = sum fall(n,i)(-1)**(n-i) {i>=0}
        = n! sum 1/(n-i)! (-1)**(n-i) {i>=0, n-i>=0}
        = n! sum (-1)**i / i! {i=0..n}
    [n>=0] ==>> subfactorial[n+1] = sum fall(n+1,i)(-1)**(n+1-i) {i>=0}
        = sum (n+1)fall(n,i-1)(-1)**(n-(i-1)) {i>0} + (-1)**(n+1)
        = (n+1)subfactorial[n] + (-1)**(n+1)
    subfactorial[n] =  n subfactorial[n-1] + (-1)**n, for n>=1


subfactorial[n] = n! sum (-1)**i / i! {i=0..n}
    = n! sum (-1)**i / i! {i>=0} - n! sum (-1)**i / i! {i>n}
    = n!/e + (-1)**n (1/(n+1) - 1/(n+1)/(n+2) + ...)
    = n!/e + (-1)**n * (t which 1/(n+2) < t < 1/(n+1))
    = n!/e + 1/2   +   (-1)**n * t - 1/2
    // [n>=1] ==>> -1/2 < (-1)**n * t < 1/3 ==>> -1<tail<-1/6
    = floor(n!/e + 1/2) + [n=0]
subfactorial[n]/n! ~=~ 1/e = 0.36787944117144233 ~=~ 36.8%


'''




from .numberss import NumberList
from .subfactorial_more import subfactorial_by_floor_mul_invE

_data = [1, 0, 1, 2, 9, 44, 265, 1854, 14833, 133496]

def SUB_P(n):
    return subfactorial_by_floor_mul_invE(n)


class Subfactorial(NumberList):
    def _calc_neg(self, n, nums):
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        return nums[-1]*n + (-1)**n
        raise NotImplementedError()
    def direct_calc(self, n):
        return SUB_P(n)
        raise NotImplementedError()

    
    def __init__(self):
        super().__init__([1])

subfactorial = Subfactorial()


#print(subfactorial.get_first(10))
assert subfactorial.get_first(len(_data)) == _data
assert all(subfactorial.direct_calc(n) == subfactorial(n) for n in range(5))






