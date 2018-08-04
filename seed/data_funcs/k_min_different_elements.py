

__all__ = ['k_min_different_elements']
from seed.special_funcs import identity as eye_key
from data_structure import KMinSet, MapPair

def k_min_different_elements(k, elements, *, key=None):
    '''O(nlogk)

heapq.nsmallest(n, iterable, key=None)
1) not different elements
2) O(nlogk), the same
'''
    if k < 0:
        raise ValueError('k < 0')
    if key == None:
        decode = encode = eye_key
    else:
        encode = lambda e: MapPair(key(e), e)
        decode = lambda pair: pair.value

    # not stdlib.OrderedDict!!, it works like C++ set<>
    mins = KMinSet(k) #OrderedSet()

    mins.update(encode(e) for e in elements)
    assert len(mins) <= k
    return list(decode(pair) for pair in mins)
        
