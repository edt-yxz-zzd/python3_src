

'''
example:
    >>> unoffseted_bucket_sort__uints_easy([5,3,7,5])
    [3, 5, 5, 7]
    >>> unoffseted_bucket_sort__uints_easy([])
    []
'''


__all__ = '''
    unoffseted_bucket_sort__uints
    unoffseted_bucket_sort__uints_easy

    calc_upper_bound_of_uints
    calc_upper_bound_of_uints_ex

    IUnoffsetedBucketSort__UInts
    UnoffsetedBucketSort__UInts
    UnoffsetedBucketSort__UIntsEasy
    '''.split()

from .ISortBase import ISortBase

from abc import ABC, abstractmethod
from itertools import repeat, chain, starmap
from .reiterable import make_reiterable

def calc_upper_bound_of_uints(uints):
    # upper_bound = max (*uints, default=-1) + 1
    return max(uints, default=-1) + 1
def calc_upper_bound_of_uints_ex(uints):
    # input: iterable<int>
    # output: (reiterable<int>, upper_bound)
    uints = make_reiterable(uints)
    upper_bound = calc_upper_bound_of_uints(uints)
    return uints, upper_bound


def offer_upper_bound(f):
    # input: f :: (uints, upper_bound) -> result
    # output: g :: (uints) -> result
    def g(uints):
        uints, upper_bound = calc_upper_bound_of_uints_ex(uints)
        return f(uints, upper_bound)
    return g

def unoffseted_bucket_sort__uints_easy(uints):
    # input: iterable<int>
    # output: a sorted list # not tuple!
    u = UnoffsetedBucketSort__UIntsEasy()
    return u.unoffseted_bucket_sort__uints(uints)
    return offer_upper_bound(unoffseted_bucket_sort__uints)(uints)
def unoffseted_bucket_sort__uints(uints, upper_bound):
    # input: iterable<int>
    # assert all(0<=i<upper_bound for i in uints)
    # output: a sorted list # not tuple!
    u = UnoffsetedBucketSort__UInts(upper_bound)
    return u.unoffseted_bucket_sort__uints(uints)


######################

class IUnoffsetedBucketSort__UInts(ISortBase):
    @abstractmethod
    def _upper_bound_(self, uints):
        # get or calc upper_bound
        # output: (uints, upper_bound)
        raise NotImplementedError

    def __call__(self, __uints):
        return self.unoffseted_bucket_sort__uints(__uints)
    def unoffseted_bucket_sort__uints(self, __uints):
        # input: iterable<int>
        # assert all(0<=i<upper_bound for i in uints)
        # output: a sorted list # not tuple!
        return list(self.iter_unoffseted_bucket_sort__uints(__uints))

    def iter_unoffseted_bucket_sort__uints(self, __uints):
        # input: iterable<int>
        # assert all(0<=i<upper_bound for i in uints)
        # output: iterator of a sorted uints
        int2count = self.unoffseted_bucket_count(__uints)
        return chain.from_iterable(starmap(repeat, enumerate(int2count)))

    def unoffseted_bucket_count(self, __uints):
        # input: iterable<int>
        # assert all(0<=i<upper_bound for i in uints)
        # output: count_list # int2count # not tuple!
        uints, upper_bound = self._upper_bound_(__uints)

        ls = [0]*upper_bound
        for i in uints:
            assert 0 <= i < upper_bound
            ls[i] += 1
        return ls

class UnoffsetedBucketSort__UInts(IUnoffsetedBucketSort__UInts):
    def __init__(self, upper_bound):
        assert upper_bound >= 0
        self.__upper_bound = upper_bound
    def _upper_bound_(self, uints):
        return uints, self.__upper_bound

class UnoffsetedBucketSort__UIntsEasy(IUnoffsetedBucketSort__UInts):
    def _upper_bound_(self, uints):
        return calc_upper_bound_of_uints_ex(uints)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

