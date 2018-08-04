
'''
for not sort unique:
    see:
        seed.iters.iter_unique_by_eq
        seed.iters.neighbor_unique
'''

__all__ = '''
    sorted_ex
'''.split()


from seed.iters.neighbor_unique import neighbor_unique
#from functools import cmp_to_key
#from seed.tiny import echo, py_cmp
from seed.tiny import int2cmp
from .sorted_ex import sorted_ex




def sort_then_unique(iterable, *
        , key=None, cmp=None, __eq__=None, reverse=False):
    '''
input:
    iterable :: Iter a
    key :: None | (a->k)
    cmp :: None | (k -> k -> (-1|0|+1))
    __eq__ :: k -> k -> bool
        [__eq__ a b] <==> [cmp a b == 0]
        but __eq__ faster
    reverse :: bool
        reverse when sort
output:
    result :: Iter a
        unique


example:
    >>> this = sort_then_unique
    >>> list_this = lambda *args, **kwargs: [*this(*args, **kwargs)]
    >>> list_this([])
    []
    >>> list_this([3,5,3,3,2,1,5,3])
    [1, 2, 3, 5]
    >>> list_this([3,5,3,3,2,1,5,3], reverse=True)
    [5, 3, 2, 1]
    >>> list_this([3,5,3,3,2,1,5,3], key=int.__neg__)
    [5, 3, 2, 1]
    >>> list_this([3,5,3,3,2,1,5,3], cmp=lambda a, b: int2cmp(a%3-b%3))
    [3, 1, 5]
    >>> list_this([3,5,3,3,2,1,5,3], key=lambda i:i+1, cmp=lambda a, b: int2cmp(a%3-b%3))
    [5, 3, 1]

'''
    if cmp is None and __eq__ is not None: raise TypeError
    if cmp is not None and __eq__ is None:
        def __eq__(a, b):
            return not cmp(a, b)
    assert (cmp is None) == (__eq__ is None)

    ls = sorted_ex(iterable, key=key, cmp=cmp, reverse=reverse)
    return neighbor_unique(ls, key=key, __eq__=__eq__)



if __name__ == "__main__":
    import doctest
    doctest.testmod()





