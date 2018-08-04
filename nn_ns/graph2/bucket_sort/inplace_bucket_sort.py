
'''
we have a collection of uint sequences, and we want to sort each sequence inplace in one bucket sort
    NOTE: sort each seq in seqs instead of sort seqs

example:
    >>> data = ([], [4,3,5], [], [2,1,0])
    >>> inplace_bucket_sort__easy(data, key=echo)
    >>> data
    ([], [3, 4, 5], [], [0, 1, 2])
'''


__all__ = '''
    inplace_bucket_sort
    inplace_bucket_sort__easy

    IInplaceBucketSort
    InplaceBucketSort
    InplaceBucketSort__Easy

    calc_upper_bound_of_seqs
    calc_upper_bound_of_seqs_ex
    '''.split()


from abc import ABC, abstractmethod
from itertools import repeat, chain, starmap
from collections.abc import Sequence, MutableSequence

from .ISortBase import ISortBase__ConvertNoneKey
from .reiterable import make_reiterable
from .unoffseted_bucket_sort__objs import calc_upper_bound_of_objs
from .are_instances import are_instances
from .echo import echo

def clear_seq(seq):
    del seq[:]
    return
    seq.clear()


def calc_upper_bound_of_seqs(__seqs, key):
    # upper_bound = max (map(key, chain.from_iterable(seqs)), default=-1) + 1
    return calc_upper_bound_of_objs(chain.from_iterable(__seqs), key)
def calc_upper_bound_of_seqs_ex(__seqs, key):
    # input: iterable<reiterable<obj>>, obj->uint
    # output: (reiterable<reiterable<obj>>, upper_bound)
    seqs = make_reiterable(__seqs)
    upper_bound = calc_upper_bound_of_seqs(seqs, key)
    return seqs, upper_bound

class IInplaceBucketSort(ISortBase__ConvertNoneKey):
    # O(len(seqs) + sum(map(len, seqs)) + ?)
    #   ? = upper_bound if __lsls is None
    #   ? = len(where) if __lsls is not None
    def __init__(self, *, key, reverse=False):
        ISortBase__ConvertNoneKey.__init__(self, key=key, reverse=reverse)

    @abstractmethod
    def _upper_bound_(self, __seqs):
        # get or calc upper_bound
        # output: (__seqs, upper_bound)
        raise NotImplementedError

    def __call__(self, __seqs):
        self.inplace_bucket_sort(__seqs)
    def inplace_bucket_sort(self, __seqs, __lsls=None, where=None):
        # __seqs :: iter<mutable_seq>
        # __lsls :: [[obj]]
        # where :: [idx] # increase; tell where to collect objs; should be reverable
        # return None
        seqs = make_reiterable(__seqs)
        if not are_instances(seqs, MutableSequence): raise TypeError

        if __lsls is not None and where is None: raise TypeError('need "where" to clean __lsls')

        def calc_ordered_where(L):
            ordered_where = range(L) if where is None else where
            if self.reverse:
                ordered_where = reversed(ordered_where)
            return ordered_where

        if __lsls is None:
            groups = self.inplace_bucket_group(seqs)
        else:
            groups = __lsls
            self.inplace_bucket_group(seqs, groups)

        L = len(groups)
        ordered_where = calc_ordered_where(L)

        if __lsls is None:
            pairs = chain.from_iterable(groups[i] for i in ordered_where)
        else:
            # clean __lsls/groups
            gs = []
            for idx in ordered_where:
                gs.append(__lsls[idx])
                groups[idx] = []
            pairs = chain.from_iterable(gs)
        # pairs :: iter<[(obj, clean_seq)]>
        for obj, seq in pairs:
            seq.append(obj)
        return None

    def inplace_bucket_group(self, __seqs, __lsls=None):
        # output: key2obj_seq_pairs :: [[(obj, clean_seq)]]
        #   or None if __lsls is not None
        seqs, upper_bound = self._upper_bound_(__seqs)
        key = self.key

        if __lsls is None:
            lsls = [[] for _ in range(upper_bound)]
            result = lsls
        else:
            assert len(__lsls) >= upper_bound
            lsls = __lsls
            result = None

        for seq in seqs:
            for obj in seq:
                i = key(obj)
                assert 0 <= i < upper_bound
                lsls[i].append((obj, seq))
            #seq.clear()
            clear_seq(seq)
        return result

class InplaceBucketSort(IInplaceBucketSort):
    def __init__(self, upper_bound, *, key, reverse=False):
        assert upper_bound >= 0
        self.__upper_bound = upper_bound
        IInplaceBucketSort.__init__(self, key=key, reverse=reverse)
    def _upper_bound_(self, __seqs):
        return (__seqs, self.__upper_bound)
class InplaceBucketSort__Easy(IInplaceBucketSort):
    def _upper_bound_(self, __seqs):
        return calc_upper_bound_of_seqs_ex(__seqs, self.key)

def inplace_bucket_sort__easy(__seqs, *, key, reverse=False):
    u = InplaceBucketSort__Easy(key=key, reverse=reverse)
    u.inplace_bucket_sort(__seqs)
    return None

def inplace_bucket_sort(__seqs, upper_bound, *, key, reverse=False):
    # input: objs
    #   objs :: iter<obj>
    #   key :: obj -> uint
    #   upper_bound :: uint
    # precondition: all(0 <= key(obj) < upper_bound for obj in objs)
    # precondition: 0 <= upper_bound
    # O(len(objs) + upper_bound)
    # output: [obj] # stable sorted
    #
    u = InplaceBucketSort(upper_bound, key=key, reverse=reverse)
    u.inplace_bucket_sort(__seqs)
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()

