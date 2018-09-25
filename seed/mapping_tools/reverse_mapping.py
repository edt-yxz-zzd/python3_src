

__all__ = '''
    reverse_mapping
    make_iter_singleton
    '''.split()
from collections import defaultdict


def make_iter_singleton(x):
    yield x
def reverse_mapping(mapping, value2iter_new_keys=None):
    r'''
reverse_mapping(mapping, value2iter_new_keys=None)
    mapping :: Map k v
    value2iter_new_keys :: Maybe (v -> Iter k')
    result :: Map k' [k]

def make_iter_singleton(x):
    yield x

reverse_mapping(mapping)
    <==> reverse_mapping(mapping, None)
    <==> reverse_mapping(mapping, make_iter_singleton)

#####################################
reverse_mapping
    :: Ord k, Ord k' => (v -> Iter k') -> Map k v -> Map k' [k]
reverse_mapping make_iter_singleton
    :: Ord k, Ord k' => Map k k' -> Map k' [k]

reverse_mapping iter
    :: Ord k, Ord a => Map k [k'] -> Map k' [k]
#####################################

example:
    >>> reverse_mapping({1:2, 2:3, 3:0, 4:3}) == {0:[3], 2:[1], 3:[2,4]}
    True

    >>> reverse_mapping({1:[2], 2:[3], 3:[0], 4:[3]}, iter) == {0:[3], 2:[1], 3:[2,4]}
    True

'''
    d = defaultdict(list)
    if value2iter_new_keys is None:
        value2iter_new_keys = make_iter_singleton
    for k, v in mapping.items():
        for _k in value2iter_new_keys(v):
            d[_k].append(k)

    d = dict(d)
    return d




if __name__ == "__main__":
    import doctest
    doctest.testmod()


