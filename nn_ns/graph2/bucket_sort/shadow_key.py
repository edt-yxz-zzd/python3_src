'''
>>> shadow_key(PySort, reverse=True)([1,3,2])
[3, 2, 1]
>>> shadow_key(PySort, key=fst, reverse=True)([(1,0),(3,0),(2,0)])
[(3, 0), (2, 0), (1, 0)]

'''


__all__ = '''
    shadow_key

    ShadowKey
    '''.split()

from .ISortBase import ISortBase
from .PySort import PySort
from .echo import fst, snd, echo

def with_key(obj, key):
    return (key(obj), obj)
def pair_obj(obj):
    return (obj, obj)
def shadow(iterable, key=None):
    if key is None:
        f = pair_obj
    else:
        f = lambda obj: with_key(obj, key)
    return map(f, iterable)

class ShadowKey(ISortBase):
    def __init__(self, bare_sort_factory, *, key, reverse=False):
        assert key is not None
        self.key = key
        self.base_sort = bare_sort_factory(key=fst, reverse=reverse)
    def __call__(self, __objs):
        return self.sort(__objs)
    def cached_sort(self, __objs):
        # iter<obj> -> sorted [(key, obj)]
        pairs = shadow(__objs, self.key)
        pairs = self.base_sort(pairs)
        return pairs
    def sort(self, __objs):
        # iter<obj> -> sorted [obj]
        pairs = self.cached_sort(__objs)
        return list(map(snd, pairs))

def shadow_key(bare_sort_factory, *, key=None, reverse=False):
    if key is None:
        return bare_sort_factory(key=echo, reverse=reverse)
    return ShadowKey(bare_sort_factory, key=key, reverse=reverse)



if __name__ == "__main__":
    import doctest
    doctest.testmod()


