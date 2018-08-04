
'''
[tree isomorphism][linear time]The design and analysis of computer algorithms (1974)(Hopcroft)(Addison-Wesley).djvu
    [page 81]

example:
    >>> data = [[], [1], (3,4,5), (3,4), [3], (1,), ()];
    >>> sort = UIntSeqSort(6);
    >>> sort(data)
    [[], (), [1], (1,), [3], (3, 4), (3, 4, 5)]
'''

__all__ = '''
    UIntSeqSort
    '''.split()

from itertools import repeat, chain, starmap
from operator import attrgetter, itemgetter, methodcaller, __not__

from .echo import echo, fst, snd
from .reiterable import make_reiterable, make_seq, make_tuple
from .tpl_key_lexicographical_bucket_sort import make_tpl_key_lexicographical_bucket_sort
from .unoffseted_bucket_sort__objs import UnoffsetedBucketSort__Objs

from .GroupBy import GroupBy, unique_keys
from .ChainFuncs import ChainFuncs
from .ISortBase import ISortBase__ConvertNoneKey




class UIntSeqSort:
    # donot distinguish tuple/list/...
    # O(upper_bound + num_uints)
    # varying length sequence
    # see also: shadow_key
    def __init__(self, upper_bound, *, key=None, reverse=False):
        # key :: obj -> [uint] where 0 <= uint < upper_bound
        assert upper_bound >= 0
        self.upper_bound = upper_bound
        ISortBase__ConvertNoneKey.__init__(self, key=key, reverse=reverse)
    def __call__(self, __objs):
        return self.sort__uintss(__objs)

    def sort__uintss(self, __objs):
        objs = make_reiterable(__objs)
        #objs = make_seq(__objs)
        key = self.key
        upper_bound = self.upper_bound

        len_key = ChainFuncs([len, key])
        max_seq_len = max(map(len_key, objs), default=0)
        L = max_seq_len


        def calc_level_idx2sorted_unique_uints():
            # to build:
            #   level_idx2sorted_uints = [[] for _ in range(L)]
                # level_idx
                # uint = key(obj)[level_idx]
                # uints = [key(obj)[level_idx] for obj in objs]
            level_idx_uint_pairs = chain.from_iterable(
                            enumerate(key(obj)) for obj in objs)
            # L not L+1
            sort = make_tpl_key_lexicographical_bucket_sort([L, upper_bound])
            level_idx_uint_pairs = sort(level_idx_uint_pairs); del sort
            level_idx2sorted_uints = GroupBy(key=fst, value=snd).groups(level_idx_uint_pairs)
            assert len(level_idx2sorted_uints) == L

            level_idx2sorted_unique_uints = list(map(unique_keys, level_idx2sorted_uints))

            # used to collect data
            return level_idx2sorted_unique_uints
        level_idx2sorted_unique_uints = calc_level_idx2sorted_unique_uints()



        ################
        def calc_len2objs(objs):
            # L+1 not L
            sort = UnoffsetedBucketSort__Objs(L+1, key=len_key)
            pairs = GroupBy(key=len_key).iter_keyed_groups(sort(objs))

            len2objs = []
            for length, group in pairs:
                len2objs.extend(repeat((), length-len(len2objs)))
                assert len(len2objs) == length
                len2objs.append(group)
            assert len(len2objs) == L+1
            return len2objs
        len2objs = calc_len2objs(objs); del objs


        ############
        def sort():
            partial_sorted_objs = iter(()) # len > length; level > length-1
            lsls = [[] for _ in range(upper_bound)] # buffer

            for level_idx, objs in zip(range(L-1, -1, -1), reversed(len2objs)):
                # level_idx = length - 1
                objs = chain(objs, partial_sorted_objs)
                where = level_idx2sorted_unique_uints[level_idx]

                k = ChainFuncs([itemgetter(level_idx), key])
                sort = UnoffsetedBucketSort__Objs(upper_bound, key=k)
                partial_sorted_objs = sort.iter_unoffseted_bucket_sort__objs(
                        objs, lsls, where)
            else:
                # length == 0; level_idx == -1
                objs = len2objs[0]
                sorted_objs = chain(objs, partial_sorted_objs)
                sorted_objs = list(sorted_objs)
            return sorted_objs
        return sort()
    pass



if __name__ == "__main__":
    import sys
    import doctest
    doctest.testmod()




