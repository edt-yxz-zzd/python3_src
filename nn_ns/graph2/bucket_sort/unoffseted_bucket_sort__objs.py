

'''
example:
    >>> unoffseted_bucket_sort__objs_easy([{},[3],(),[1,3]], key=len)
    [{}, (), [3], [1, 3]]
    >>> unoffseted_bucket_sort__objs_easy([], key=len)
    []
'''


__all__ = '''
    unoffseted_bucket_sort__objs
    unoffseted_bucket_sort__objs_easy

    calc_upper_bound_of_objs
    calc_upper_bound_of_objs_ex

    IUnoffsetedBucketSort__Objs
    UnoffsetedBucketSort__Objs
    UnoffsetedBucketSort__ObjsEasy
    '''.split()


from abc import ABC, abstractmethod
from itertools import repeat, chain, starmap
from .reiterable import make_reiterable
from .unoffseted_bucket_sort__uints import calc_upper_bound_of_uints
from .ISortBase import ISortBase__ConvertNoneKey

def calc_upper_bound_of_objs(__objs, key):
    # upper_bound = max (map(key, objs), default=-1) + 1
    return calc_upper_bound_of_uints(map(key, __objs))
def calc_upper_bound_of_objs_ex(__objs, key):
    # input: iterable<obj>, obj->key
    # output: (reiterable<obj>, upper_bound)
    objs = make_reiterable(__objs)
    upper_bound = calc_upper_bound_of_objs(objs, key)
    return objs, upper_bound

class IUnoffsetedBucketSort__Objs(ISortBase__ConvertNoneKey):
    @abstractmethod
    def _upper_bound_(self, __objs):
        # get or calc upper_bound
        # output: (__objs, upper_bound)
        raise NotImplementedError

    def __call__(self, __objs):
        return self.unoffseted_bucket_sort__objs(__objs)
    def unoffseted_bucket_sort__objs(self, __objs):
        return list(self.iter_unoffseted_bucket_sort__objs(__objs))
    def iter_unoffseted_bucket_sort__objs(self, __objs, __lsls=None, where=None):
        # __lsls :: [[obj]]
        # where :: [idx] # increase; tell where to collect objs; should be reverable
        if __lsls is not None and where is None: raise TypeError('need "where" to clean __lsls')

        def calc_ordered_where(L):
            ordered_where = range(L) if where is None else where
            if self.reverse:
                ordered_where = reversed(ordered_where)
            return ordered_where

        if __lsls is None:
            groups = self.unoffseted_bucket_group(__objs)
        else:
            groups = __lsls
            self.unoffseted_bucket_group(__objs, groups)

        L = len(groups)
        ordered_where = calc_ordered_where(L)

        if __lsls is None:
            return chain.from_iterable(groups[i] for i in ordered_where)

        # clean __lsls/groups
        gs = []
        for idx in ordered_where:
            gs.append(__lsls[idx])
            groups[idx] = []
        return chain.from_iterable(gs)


    def unoffseted_bucket_group(self, __objs, __lsls=None):
        # output: key2objs :: [[obj]]
        #   or None if __lsls is not None
        objs, upper_bound = self._upper_bound_(__objs)
        key = self.key

        if __lsls is None:
            lsls = [[] for _ in range(upper_bound)]
            result = lsls
        else:
            assert len(__lsls) >= upper_bound
            lsls = __lsls
            result = None

        for obj in objs:
            i = key(obj)
            assert 0 <= i < upper_bound
            lsls[i].append(obj)
        return result
class UnoffsetedBucketSort__Objs(IUnoffsetedBucketSort__Objs):
    def __init__(self, upper_bound, *, key, reverse=False):
        assert upper_bound >= 0
        self.__upper_bound = upper_bound
        IUnoffsetedBucketSort__Objs.__init__(self, key=key, reverse=reverse)
    def _upper_bound_(self, __objs):
        return (__objs, self.__upper_bound)
class UnoffsetedBucketSort__ObjsEasy(IUnoffsetedBucketSort__Objs):
    def _upper_bound_(self, __objs):
        return calc_upper_bound_of_objs_ex(__objs, self.key)

def unoffseted_bucket_sort__objs_easy(__objs, *, key, reverse=False):
    u = UnoffsetedBucketSort__ObjsEasy(key=key, reverse=reverse)
    return u.unoffseted_bucket_sort__objs(__objs)

def unoffseted_bucket_sort__objs(__objs, upper_bound, *, key, reverse=False):
    # input: objs
    #   objs :: iter<obj>
    #   key :: obj -> uint
    #   upper_bound :: uint
    # precondition: all(0 <= key(obj) < upper_bound for obj in objs)
    # precondition: 0 <= upper_bound
    # O(len(objs) + upper_bound)
    # output: [obj] # stable sorted
    #
    u = UnoffsetedBucketSort__Objs(upper_bound, key=key, reverse=reverse)
    return u.unoffseted_bucket_sort__objs(__objs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

