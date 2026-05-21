
r'''[[[
seed.algo.bucket_sort.all_unique
py -m nn_ns.app.debug_cmd   seed.algo.bucket_sort.all_unique -x
py -m nn_ns.app.doctest_cmd seed.algo.bucket_sort.all_unique:__doc__ -ht #  -ff -v -df
#]]]'''#'''



__all__ = '''
    all_unique
    '''.split()



___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import echo
___end_mark_of_excluded_global_names__0___ = ...


def all_unique(alphabet_size, iterable, *, key=None):
    ''':: (a->UInt) -> UInt -> [a] -> Bool


input:
    alphabet_size :: UInt
    iterable :: Iter a
    key :: a -> UInt[0..alphabet_size-1]
output:
    are_all_unique :: Bool
        =[def]= len(set(map(key, iterable))) == len(iterable)
see:
    seed.iters.all_the_same
    bucket_unique
    inverse_uint_bijection_array
    is_uint_bijection_array
        if all_unique and len(iterable) == alphabet_size, then is a uint_bijection_array

example:
    >>> all_unique(0, [])
    True
    >>> all_unique(2, [1])
    True
    >>> all_unique(2, [1, 0])
    True
    >>> all_unique(2, [1, 1])
    False
'''
    if not alphabet_size >= 0: raise ValueError
    if key is not None:
        iterable = map(key, iterable)
    del key

    Nothing = None
    table = [Nothing]*alphabet_size

    for k in iterable:
        if not 0 <= k < alphabet_size: raise ValueError
        if table[k] is not Nothing: return False
        table[k] = ...

    return True


from seed.algo.bucket_sort.all_unique import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()


from seed.algo.bucket_sort.all_unique import all_unique
