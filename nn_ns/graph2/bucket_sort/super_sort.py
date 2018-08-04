
'''
sort_factory(..., *, key, reverse=False, ...) -> sort_func
bare_sort_factory(*, key, reverse=False) -> sort_func


example:
    >>> data = [(1,2),(2,1),(1,1,2), (1,1),(2,2)];
    >>> make_super_sort([(fst, PySort), (snd, PySort)])(data)
    [(1, 1, 2), (1, 1), (1, 2), (2, 1), (2, 2)]

'''

__all__ = '''
    make_super_sort
    SuperSort
    '''.split()

from itertools import repeat, chain, starmap

from operator import attrgetter, itemgetter, methodcaller, __not__
from functools import partial
from .Caller import Caller, Partial
from .ChainFuncs import ChainFuncs, apply
from .echo import echo
from .PySort import PySort
from .echo import fst, snd
from .ISortBase import ISortBase



def make_super_sort(__key_sort_factory_args_ls, *, key=None, reverse=False):
    # this is a sort_factory
    # key_sort_factory_args_ls :: iter<(key, sort_factory, *args)>
    it = ((key, False, Partial(sort_factory, *args))
            for key, sort_factory, *args in __key_sort_factory_args_ls)
    return SuperSort(it, key=key, reverse=reverse)

class SuperSort(ISortBase):
    # this is a sort_factory
    def __init__(self, __key_reverse_bare_sort_factory_triples
                , *, key=None, reverse=False):
        # bare_sort_factory(*, key, reverse=False) -> sort_func
        #   we can use Caller/Partial to wrap sort_factory -> bare_sort_factory
        # key_reverse_sort_factory_triples :: iter<(key, reverse, sort_factory)>
        #
        # use sort_methods from right to left
        #   for lexicographical sort
        #
        # sort_methods :: iter<callable>
        #   are all sort methods
        #   see Caller/Partial/ChainFuncs/apply
        #   see attrgetter/itemgetter/methodcaller/partial
        reverse_f = __not__ if reverse else echo
        pre_key = key
        key_f = echo if pre_key is None else lambda key: ChainFuncs(key, pre_key)
        triples = __key_reverse_bare_sort_factory_triples

        sorts = (bare_sort_factory(key = key_f(key), reverse = reverse_f(reverse))
                    for key, reverse, bare_sort_factory in triples)
        self.sort = ChainFuncs(sorts)

    def __call__(self, __objs):
        return self.sort(__objs)


'''
def lexicographical_sort(__objs, __sort_and_args_ls):
    # sort_and_args_ls :: iter<(sort_func, *args)>
    sorts = starmap(Caller, __sort_and_args_ls)
    sort = ChainFuncs(sorts)
    return sort(__objs)
'''

if __name__ == "__main__":
    import doctest
    doctest.testmod()



