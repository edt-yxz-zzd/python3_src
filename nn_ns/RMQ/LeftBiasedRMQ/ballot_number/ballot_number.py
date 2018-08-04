
'''
NOTE:
    ballot_number__by_direct_calc(p,q) ~ time O(q^2 * log(q))
    ballot_number__by_table(p,q) ~ time O(q^3)
    very slow!!!

see: "ballot_number - ?????.txt"

'''

__all__ = '''
    ballot_number__by_direct_calc
    ballot_number__by_table
    '''.split()
from itertools import accumulate
from nn_ns.math_nn.numbers.choose import choose
from nn_ns.math_nn.numbers.ballot_number import xballot_number as _xballot_number


def ballot_number__by_direct_calc(p, q):
    '''ballot_number(p,q) :: UInt

time O(q^2 * log(q))
ballot(p,q)
    | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
    | otherwise = 0

see: math_nn.numbers/"time and space complexity.txt"::choose
    choose(n,i) ~ time O(n^2 * log(n))

example:
    >>> this = ballot_number__by_direct_calc
    >>> Q = 20
    >>> xballot = Xballot(Q+1)
    >>> all(this(p,q) == xballot(q,p) for q in range(Q+1) for p in range(q+1))
    True
'''
    if not (0 <= p <= q):
        return 0
    return choose.direct_calc(q+p,p)*(q-p+1)//(q+1)


def ballot_number__by_table(p, q):
    '''ballot_number(p,q) :: UInt

time O(q^3)
    why?
        table size O(q^2)
        bit_size_of(ballot_number(p,q)) = O(q)
ballot(p,q)
    | 0 <= p <= q = C(q+p,p)*(q-p+1)/(q+1)
    | otherwise = 0

example:
    >>> this = ballot_number__by_table
    >>> Q = 20
    >>> xballot = Xballot(Q+1)
    >>> all(this(p,q) == xballot(q,p) for q in range(Q+1) for p in range(q+1))
    True

'''

    return _xballot_number(q,p)














####################### Xballot




class Xballot:
    '''calc Xballot table: Xballot(Q)(q,p) = xballot(q,p) if 0<=p<=q<Q

time O(Q^3)

xballot(q, p) =[def]= ballot(p,q)
xballot(q>=0, p=0) = 1
xballot(q>p, p>0) = xballot(q-1, p) + xballot(q, p-1)
xballot(q=p, p>0) = xballot(q, p-1)
xballot(q,p) = 0, otherwise


example:
    >>> from .Catalan_number import Catalan_numbers
    >>> Q = 20
    >>> table = Xballot(Q)
    >>> Catalan_numbers(Q) == [table(q,q) for q in range(Q)]
    True
    >>> [1]*Q == [table(q,0) for q in range(Q)]
    True
    >>> [*range(Q)] == [table(q,1) for q in range(Q)]
    True
'''
    def __init__(self, Q):
        '''Q - calc xballot(q,p) for 0<=p<=q<Q'''
        self.table = xballot_numberss(Q)
    def __call__(self, q, p):
        if not 0 <= p <= q:
            return 0
        # assert q < Q
        return self.table[q][p]


def xballot_numberss_definition(Q):
    '''xballot(q, p) = ballot(p, q)
    xballot_numberss_definition :: uint -> [[uint]]

time O(Q^3)
output[q][p] = xballot(q,p) for 0<=p<=q<Q


xballot(q, p) =[def]= ballot(p,q)
xballot(q>=0, p=0) = 1
xballot(q>p, p>0) = xballot(q-1, p) + xballot(q, p-1)
xballot(q=p, p>0) = xballot(q, p-1)
xballot(q,p) = 0, otherwise


fix q
note that accumulate pre row + ones
xballot(q,p) = sum (C(p+1, i) for all i) for p in [0..q]
= 2**(p+1) for p in [0..q]
'''
    xballot = [[None]*(q+1) for q in range(Q)]
    if Q <= 0:
        return xballot

    for q in range(Q):
        xballot[q][0] = 1

    for q in range(Q):
        for p in range(1, q):
            assert 0 < p < q
            xballot[q][p] = xballot[q-1][p] + xballot[q][p-1]
        xballot[q][q] = xballot[q][q-1]

    assert all(x > 0 for xs in xballot for x in xs)
    return xballot


def xballot_numberss_by_accumulate(Q):
    ''':: uint -> [[uint]]

time O(Q^3)
output[q][p] = xballot(q,p) for 0<=p<=q<Q
'''
    if Q <= 0:
        return []

    pre = [1]
    xballot = [pre]
    for q in range(1, Q):
        xqp = list(accumulate(pre))
        xqp.append(xqp[-1])
        pre = xqp
        xballot.append(pre)
    return xballot

def xballot_numberss(Q):
    ''':: uint -> [[uint]]

time O(Q^3)
output[q][p] = xballot(q,p) for 0<=p<=q<Q
'''
    return xballot_numberss_by_accumulate(Q)


def test_xballot_numberss():
    for n in range(10):
        if not xballot_numberss(n) == xballot_numberss_by_accumulate(n) \
               == xballot_numberss_definition(n):
            print(xballot_numberss(n), xballot_numberss_by_accumulate(n),
                  xballot_numberss_definition(n))
        assert xballot_numberss(n) == xballot_numberss_by_accumulate(n) \
               == xballot_numberss_definition(n)






def _t():
    this = ballot_number__by_table
    Q = 20
    xballot = Xballot(Q+1)
    #all(this(p,q) == xballot(q,p) for q in range(Q+1) for p in range(q+1))
    for q in range(Q+1):
        for p in range(q+1):
            if this(p,q) != xballot(q,p):
                print(p, q)
                print(this(p,q), xballot(q,p))
                break






if __name__ == "__main__":
    test_xballot_numberss()
    _t()
    import doctest
    doctest.testmod()










