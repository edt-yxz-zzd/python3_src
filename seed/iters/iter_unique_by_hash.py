r'''[[[
seed.iters.iter_unique_by_hash
py -m seed.iters.iter_unique_by_hash
py -m nn_ns.app.debug_cmd   seed.iters.iter_unique_by_hash -x
py -m nn_ns.app.doctest_cmd seed.iters.iter_unique_by_hash:__doc__ -ht #  -ff -v -df
#]]]'''#'''

__all__ = '''
    iter_unique_by_hash
    remove_duplicates_by_hash
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import echo
___end_mark_of_excluded_global_names__0___ = ...

def remove_duplicates_by_hash(iterable, *, key=None, container=tuple):
    '''Hashable k => Iter a -> (a -> k) -> [a]

O(n)
'''
    return container(iter_unique_by_hash(iterable, key=key))
def iter_unique_by_hash(iterable, *, key=None):
    '''Hashable k => Iter a -> (a -> k) -> Iter a

O(n)
'''
    if key is None:
        key = echo

    s = set()
    for a in iterable:
        k = key(a)
        if k not in s:
            yield a
            s.add(k)


from seed.iters.iter_unique_by_hash import iter_unique_by_hash, remove_duplicates_by_hash
from seed.iters.iter_unique_by_hash import *
