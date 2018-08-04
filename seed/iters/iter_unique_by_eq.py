
__all__ = '''
    unique_by_eq
    iter_unique_by_eq
    '''.split()

import operator
from seed.tiny import echo



def unique_by_eq(iterable, *, key=None, __eq__=None):
    '''Eq k => Iter a -> (a -> k) -> [a]

time: O(n^2)
assume: [a is b] ==>> [a == b]

left_biased objects, keeps the original order


example:
    >>> unique_by_eq([])
    []
    >>> unique_by_eq([1])
    [1]
    >>> unique_by_eq('122013021493')
    ['1', '2', '0', '3', '4', '9']
    >>> unique_by_eq('122013021493', key=int)
    ['1', '2', '0', '3', '4', '9']
    >>> unique_by_eq('122013021493', key=lambda _:None)
    ['1']
    >>> unique_by_eq('122013021493', __eq__=lambda a,b:True)
    ['1']
'''
    return [*iter_unique_by_eq(iterable, key=key, __eq__=__eq__)]

def iter_unique_by_eq(iterable, *, key=None, __eq__=None):
    '''Eq k => Iter a -> (a -> k) -> Iterator a

time: O(n^2)
assume: [a is b] ==>> [a == b]

left_biased objects, keeps the original order
'''
    if key is None:
        key = echo
    if __eq__ is None:
        __eq__ = operator.__eq__

    obj_id_set = set()
    keys = []
    if key is echo:
        #key_id_set = obj_id_set
        #keys = objs
        def put(key, obj):
            obj_id_set.add(id(obj))
            keys.append(key)
        def exist1(key, obj):
            return id(obj) in obj_id_set
    else:
        key_id_set = set()
        def put(key, obj):
            key_id_set.add(id(key))
            obj_id_set.add(id(obj))
            keys.append(key)
        def exist1(key, obj):
            return id(obj) in obj_id_set or id(key) in key_id_set

    if __eq__ is operator.__eq__:
        def exist2(k):
            return any(k==t for t in reversed(keys))
            return k in keys
    else:
        def exist2(k):
            return any(__eq__(k,t) for t in reversed(keys))
            return any(__eq__(k,t) for t in keys)

    for x in iterable:
        k = key(x)
        if exist1(k, x) or exist2(k): continue

        yield x
        put(k, x)
    return


if __name__ == "__main__":
    import doctest
    doctest.testmod()


