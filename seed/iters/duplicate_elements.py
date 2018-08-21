
'''
key(element) should be hashable
'''


__all__ = '''
    iter_element_groups
    iter_duplicate_element_groups
    find_duplicate_element_groups
    iter_duplicate_representative_elements
    find_maybe_duplicate_element1
'''.split()


from collections import Counter, defaultdict
#from seed.special_funcs import identity as eye_key
from seed.tiny import echo


def iter_element_groups(iterable, *, key = None):
    '''iter_element_groups([1,2,2]) == iter(shuffle([[1], [2,2]]))'''
    key = echo if key is None else key
    d = defaultdict(list)
    for k in iterable:
        d[key(k)].append(k)

    return d.values()


def iter_duplicate_element_groups(iterable, *, key = None):
    '''iter_duplicate_element_groups([1,2,2, 3,3,3]) == iter(shuffle([[2,2], [3,3,3]]))'''
    #Counter(iterable)

    return filter(lambda ls: len(ls) > 1,
                  iter_element_groups(iterable, key))

def find_duplicate_element_groups(iterable, *, key = None):
    return tuple(iter_duplicate_element_groups(iterable, key))
def iter_duplicate_representative_elements(iterable, *, key = None):
    'find all duplicated elements and return one elem per class'
    return map(lambda ls: ls[0],
               iter_duplicate_element_groups(iterable, key))

def find_maybe_duplicate_element1(iterable, *, key = None):
    'find one duplicate_element; returm () or (elem,)'
    key = echo if key is None else key
    s = set()
    for i, x in enumerate(1, iterable):
        s.add(key(x))
        if i != len(s):
            return (x,)
    return ()

























