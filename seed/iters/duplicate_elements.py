
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
    'Hashable k => Iter x -> (key::x->k) -> Iter([x]{per k})/Iter<list<x>> # iter_element_groups([1,2,2]) == iter(shuffle([[1], [2,2]]))'
    key = echo if key is None else key
    d = defaultdict(list)
    for k in iterable:
        d[key(k)].append(k)

    return iter(d.values())


def iter_duplicate_element_groups(iterable, *, key = None):
    'Hashable k => Iter x -> (key::x->k) -> Iter([x]{per k}{len>=2})/Iter<list<x>> # iter_duplicate_element_groups([1,2,2, 3,3,3]) == iter(shuffle([[2,2], [3,3,3]]))'
    #Counter(iterable)

    return filter(lambda ls: len(ls) > 1,
                  iter_element_groups(iterable, key=key))

def find_duplicate_element_groups(iterable, *, key = None):
    'Hashable k => Iter x -> (key::x->k) -> [[x]{per k}{len>=2}]/tuple<tuple<x>>'
    return tuple(map(tuple, iter_duplicate_element_groups(iterable, key=key)))
def iter_duplicate_representative_elements(iterable, *, key = None):
    'Hashable k => Iter x -> (key::x->k) -> Iter(x{per k}{eqvcls.len>=2})/Iter<x>' ' #find all duplicated elements and return one elem per class'
    return map(lambda ls: ls[0],
               iter_duplicate_element_groups(iterable, key=key))

def find_maybe_duplicate_element1(iterable, *, key = None):
    'Hashable k => Iter x -> (key::x->k) -> tmay (x{per k}{eqvcls.len>=2})/(()|(x,))' ' #find one duplicate_element; returm () or (elem,)'
    key = echo if key is None else key
    s = set()
    for sz, x in enumerate(iterable, 1):
        s.add(key(x))
        if len(s) != sz:
            return (x,)
    return ()











from seed.iters.duplicate_elements import \
(iter_element_groups
,iter_duplicate_element_groups
,find_duplicate_element_groups
,iter_duplicate_representative_elements
,find_maybe_duplicate_element1
)
from seed.iters.duplicate_elements import *

