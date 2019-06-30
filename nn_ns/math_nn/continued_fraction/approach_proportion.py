r'''
逼近比例 approach proportion
包络 envelop

type Angle = Real
calc_angle :: (len<-PInt) -> Vector len a -> Vector len a -> Angle
calc_square_sin_angle :: (len<-PInt) -> Vector len a -> Vector len a -> Real
calc_square_sin_angle len v u
    = 1 - ((dot_product v u)/(calc_len v)/(calc_len u))^2
    = 1 - (sum $ map (*) v u)^2/(sum $ map square v)/(sum $ map square u)
calc_angle ~ calc_square_sin_angle

problem:
    given Vector len v, PInt b, find vector u, s.t.
        (sum u < b) # or ((sum $ square u) < b)
        min (calc_square_sin_angle len v u)


problem refinement:
    given Vector len v, PInt b, find vector u, s.t.
        (sum u < b) # or ((sum $ square u) < b)
        min (calc_square_sin_angle len v u)
        ----
        sorted v
        min v > 0
        gcd_many v == 1
    ??????
        sorted_strictly v # duplcated elements make no effect??

'''


__all__ = '''
    VectorEnvelopABC
    VectorEnvelop__sum
    VectorEnvelop__square_len
    '''.split()

from seed.tiny import fst, snd
from seed.math.gcd import gcd_many

from abc import ABC, abstractmethod
from fractions import Fraction
from math import floor, ceil
from operator import __mul__
import itertools # product

def dot_product(v, u):
    assert len(v) == len(u)
    return sum(map(__mul__, v, u))
def calc_square_len(vector):
    return sum(x**2 for x in vector)
def calc_square_cos_angle(v, u):
    return dot_product(v,u)**2/Fraction(calc_square_len(v)*calc_square_len(u))
def calc_square_sin_angle(v, u):
    return 1-calc_square_cos_angle(v,u)


def iter_neighbors_of_fraction_vector(fraction_vector):
    r'''Iter Fraction -> Iter [int]

>>> one = Fraction(1)
>>> _4_3 = Fraction(4,3)
>>> _9_2 = Fraction(9,2)
>>> list(iter_neighbors_of_fraction_vector([one, _4_3, _9_2]))
[(1, 1, 4), (1, 1, 5), (1, 2, 4), (1, 2, 5)]
'''
    it = map(iter_neighbors_of_fraction, fraction_vector)
    return itertools.product(*it)
def iter_neighbors_of_fraction(fraction):
    r'''Fraction -> Iter int

>>> list(iter_neighbors_of_fraction(Fraction(4)))
[4]
>>> list(iter_neighbors_of_fraction(Fraction(4, 3)))
[1, 2]
'''
    if fraction.denominator == 1:
        yield fraction.numerator
    else:
        yield floor(fraction)
        yield ceil(fraction)
class VectorEnvelopABC(ABC):
    def __init__(self, vector, bound):
        assert type(vector) is tuple
        assert all(type(x) is int for x in vector)
        assert sorted(vector) == list(vector)
        assert vector
        assert vector[0] > 0
        assert gcd_many(vector) == 1

        if bound is None:
            bound = type(self).__calc_vector_order__(vector)+1
        assert type(bound) is int
        assert bound > 0

        self.vector = vector
        self.bound = bound
    @classmethod
    @abstractmethod
    def __calc_vector_order__(cls, vector):
        raise NotImplementedError
    def is_bounded_envelop_vector(self, vector):
        order = type(self).__calc_vector_order__(vector)
        assert order >= 0
        return order < self.bound
    def iter_bounded_envelop_vectors(self):
        f = self.is_bounded_envelop_vector
        it = self.iter_envelop_vectors()
        return filter(f, it)

    def iter_envelop_vectors(self):
        v = self.vector
        last = v[-1]
        #init = v[:-1]
        f = iter_neighbors_of_fraction_vector
        for z in range(1, last+1):
            r = Fraction(z, last)
            #fr_v = (x*r for x in init)
            fr_v = (x*r for x in v)
            yield from f(fr_v)

    def sorted_bounded_approach_proportions(self):
        c_ord = type(self).__calc_vector_order__
        u = self.vector
        def key(v):
            return calc_square_sin_angle(v, u)

        vectors = self.iter_bounded_envelop_vectors()
        vectors = sorted(vectors)
        vectors = sorted(vectors, key=c_ord)
        max_order = c_ord(vectors[-1]) if vectors else None
        vectors = sorted(vectors, key=key)

        keys = []
        groups = []
        for k, g in itertools.groupby(vectors, key=key):
            keys.append(k)
            groups.append(list(g))

        pre_order = max_order+1
        new_groups = []
        for g in groups:
            min_order = c_ord(g[0])
            if min_order < pre_order:
                new_g = tuple(v for v in g if c_ord(v) == min_order)
                new_groups.append(new_g)
                pre_order = min_order
            else:
                # drop whole group
                pass
        return new_groups

    @classmethod
    def make_VectorEnvelop(cls, vector, bound):
        return cls(vector, bound)
    @classmethod
    def approach_proportion(cls, int_vector, maybe_bound):
        triples = tuple((abs(x), i, x<0) for i, x in enumerate(int_vector))
        triples = sorted(triples, key=fst)

        #new_idx2old_idx = tuple(old_idx for x, old_idx, neg in triples)
        old_idx2new_idx = [None]*len(triples)
        negs = []
        for new_idx, (x, old_idx, neg) in enumerate(triples):
            old_idx2new_idx[old_idx] = new_idx
            negs.append(neg)

        for i, (x, _, neg) in enumerate(triples):
            if x: break
        else:
            i = len(triples)
        zeros = (0,)*i
        vector = tuple(map(fst, triples[i:]))
        if not vector:
            int_vectorss = []
            return int_vectorss
        GCD = gcd_many(vector)
        assert GCD
        if GCD != 1:
            vector = tuple(x//GCD for x in vector)
        L = len(vector)
        def vector_goback(vector):
            # -> int_vector
            assert L == len(vector)
            #bug: if GCD != 1: vector = tuple(x*GCD for x in vector)

            # new_idx, abs
            long_vector__newI_abs = zeros + vector

            # old_idx, abs
            long_vector__oldI_abs = map(long_vector__newI_abs.__getitem__, old_idx2new_idx)

            # old_idx, int
            long_vector__old_int = tuple((-x if neg else x)
                for neg, x in zip(negs, long_vector__oldI_abs))
            int_vector = long_vector__old_int
            return int_vector




        self = cls.make_VectorEnvelop(vector, maybe_bound)
        vectorss = groups = self.sorted_bounded_approach_proportions()
        int_vectorss = [list(map(vector_goback, vectors))
                        for vectors in vectorss]
        return int_vectorss

class VectorEnvelop__sum(VectorEnvelopABC):
    @classmethod
    def __calc_vector_order__(cls, vector):
        return sum(vector)
class VectorEnvelop__square_len(VectorEnvelopABC):
    @classmethod
    def __calc_vector_order__(cls, vector):
        return calc_square_len(vector)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


def main(args=None):
    import argparse
    parser = argparse.ArgumentParser(
        description='approach_proportion'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('proportion', type=int, nargs='+'
                        , help='input proportion vector :: [int]')
    parser.add_argument('-b', '--bound', type=int
                        , default=None
                        , help='bound for output proportion')
    parser.add_argument('-m', '--mode', choices=['both', 'sum', 'sq_len']
                        , default = 'both'
                        , help='output mode')

    args = parser.parse_args(args)
    mode = args.mode
    maybe_bound = args.bound
    int_vector = args.proportion

    def f_mode(cls):
        int_vectorss = cls.approach_proportion(int_vector, maybe_bound)
        return int_vectorss

    if mode in ('sum', 'both'):
        int_vectorss = f_mode(VectorEnvelop__sum)
        print('sum:', int_vectorss)
    if mode in ('sq_len', 'both'):
        int_vectorss = f_mode(VectorEnvelop__square_len)
        print('sq_len:', int_vectorss)

if __name__ == "__main__":
    main()


