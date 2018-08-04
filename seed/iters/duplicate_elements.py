
__all__ = '''
    iter_group_elements
    iter_duplicate_elements
    duplicate_elements
    duplicate_representative_elements
    duplicate_element1
'''.split()


from collections import Counter, defaultdict
from seed.special_funcs import identity as eye_key


def iter_group_elements(iterable, hashable_key = None):
    '''iter_group_elements([1,2,2]) == iter(shuffle([[1], [2,2]]))'''
    hashable_key = eye_key if hashable_key is None else hashable_key
    d = defaultdict(list)
    for k in iterable:
        d[hashable_key(k)].append(k)

    return d.values()
    

def iter_duplicate_elements(iterable, hashable_key = None):
    '''iter_duplicate_elements([1,2,2, 3,3,3]) == iter(shuffle([[2,2], [3,3,3]]))'''
    #Counter(iterable)

    return filter(lambda ls: len(ls) > 1,
                  iter_group_elements(iterable, hashable_key))

def duplicate_elements(iterable, hashable_key = None):
    return tuple(iter_duplicate_elements(iterable, hashable_key))
def duplicate_representative_elements(iterable, hashable_key = None):
    'find all duplicated elements and return one elem per class'
    return map(lambda ls: ls[0],
               iter_duplicate_elements(iterable, hashable_key))

def duplicate_element1(iterable, hashable_key = None):
    'find one duplicate_element; returm maybe_elem'
    hashable_key = eye_key if hashable_key is None else hashable_key
    s = set()
    for i, x in enumerate(1, iterable):
        s.add(hashable_key(x))
        if i != len(s):
            return (x,)
    return ()

























