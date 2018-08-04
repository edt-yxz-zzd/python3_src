
'''
example:
    >>> sort = make_tpl_key_lexicographical_bucket_sort([3, 7]);
    >>> data = [(1,5), [2,3], (0,6,None)];
    >>> sort(data)
    [(0, 6, None), (1, 5), [2, 3]]
'''


__all__ = '''
    TplKeyLexicographicalBucketSort
    make_tpl_key_lexicographical_bucket_sort

    '''.split()
from operator import itemgetter
from .unoffseted_bucket_sort__objs import UnoffsetedBucketSort__Objs
from .super_sort import make_super_sort
from .ISortBase import ISortBase

class TplKeyLexicographicalBucketSort(ISortBase):
    def __init__(self, idx_upper_bound_pairs, *, key=None, reverse=False):
        # key :: obj -> uints@[uint]
        #   where 0 <= uints[idx] < upper_bound
        #           for idx, upper_bound in idx_upper_bound_pairs
        sort_factory = UnoffsetedBucketSort__Objs
        key_sort_factory_args_ls = [
            (itemgetter(idx), sort_factory, upper_bound)
            for idx, upper_bound in idx_upper_bound_pairs
            ]
        self.sort = make_super_sort(key_sort_factory_args_ls, key=key, reverse=reverse)
    def __call__(self, __objs):
        return self.sort(__objs)

def make_tpl_key_lexicographical_bucket_sort(upper_bounds, idx_offset=0, *, key=None, reverse=False):
    idx_upper_bound_pairs = enumerate(upper_bounds, idx_offset)
    return TplKeyLexicographicalBucketSort(idx_upper_bound_pairs, key=key, reverse=reverse)

if __name__ == "__main__":
    import doctest
    doctest.testmod()



