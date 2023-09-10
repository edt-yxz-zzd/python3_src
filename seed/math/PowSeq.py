#__all__:goto
r'''[[[
e ../../python3_src/seed/math/PowSeq.py


seed.math.PowSeq
py -m nn_ns.app.debug_cmd   seed.math.PowSeq -x
py -m nn_ns.app.doctest_cmd seed.math.PowSeq:__doc__ -ff -v
py_adhoc_call   seed.math.PowSeq   @f

from seed.math.PowSeq import PowSeq

#]]]'''
__all__ = r'''
PowSeq
'''.split()#'''
__all__
from seed.helper.repr_input import repr_helper
from seed.math.II import II
from itertools import compress

class PowSeq:
    def get_args(sf, /):
        pows = sf._pows
        base = pows[0]
        I = sf._I
        return (base, pows, I)
    def __repr__(sf, /):
        args = sf.get_args()
        return repr_helper(sf, *args)
    def __init__(sf, base, pows=None, I=1, /):
        #assert base >= 2 #may be Fraction
        if pows is None:
            pows = [base]
            # [pows[i] == base**(2**i)]
        else:
            if not pows[0] is base:raise TypeError
        sf._pows = pows
        sf._I = I
    def fill__len_ge_(sf, sz, /):
        assert sz >= 0
        pows = sf._pows
        L = len(pows)
        if not sz <= L:
            for _ in range(sz-L):
                pows.append(pows[-1]**2)
            L = len(pows)
        assert sz <= L
        return
    def get_pow_2_pow_(sf, ee, /):
        assert ee >= 0
        sf.fill__len_ge_(ee+1)
        pows = sf._pows
        return pows[ee]
    def get_pow_(sf, e, /):
        assert e >= 0
        pows = sf._pows
        if e < 2:
            if e == 0:
                return sf._I #1
            return pows[0] # neednot fill
        bs = bin(e)[2:]
        assert bs[0] == '1'
        sf.fill__len_ge_(len(bs))
        assert len(bs) <= len(pows)
        bs = [b == '1' for b in bs]
        #bug:return II(pows[i] for i in reversed(range(len(bs))) if bs[i])
        return II(compress(pows, bs[::-1]), one=sf._I)



__all__


from seed.math.PowSeq import PowSeq
from seed.math.PowSeq import *
