
__all__ = '''
    empty_set
    set_union
    is_Set

    is_TupleLen
    is_Pair
    swap_pairs
    
    group_pairs2dict
    group_pairs2dict_seq
    group_pairs2dict_seq_nub
    flip_dict
'''.split()

from collections import defaultdict
from sand import nub

empty_set = frozenset()

def set_union(iterable):
    return empty_set.union(*iterable)
def is_Set(obj):
    return type(obj) == frozenset


def is_TupleLen(obj, n):
    return type(obj) == tuple and len(obj) == n

def is_Pair(obj):
    return is_TupleLen(obj, 2)



#print(set_union([]))

def swap_pairs(dedges):
    return ((v, u) for (u, v) in dedges)

def group_pairs2dict(pairs):
    ':: Iter (Key, Val) -> Map Key (Set Val)'
    d = defaultdict(set)
    for key, val in pairs:
        d[key].add(val)
        # d[val] # no such op; differ from dedges2unoriented_dgraph
    return {k : frozenset(vs) for k, vs in d.items()}
def group_pairs2dict_seq(pairs):
    ':: Iter (Key, Val) -> Map Key [Val]'
    d = defaultdict(list)
    for key, val in pairs:
        d[key].append(val)
        # d[val] # no such op; differ from dedges2unoriented_dgraph
    return {k : tuple(vs) for k, vs in d.items()}
def group_pairs2dict_seq_nub(pairs):
    ':: Iter (Key, Val) -> Map Key [Val]; differ from "dedges2oriented_dgraph"'
    d = group_pairs2dict_seq(pairs)
    for key, seq in list(d.items()):
        d[key] = tuple(nub(seq))
    return d



def flip_dict(d):
    ':: Map K V -> Map V (Set K)'
    # bug: d = dedges2unoriented_dgraph(swap_pairs(d.items()))
    #      since graph need every vtx in keys and ns may be empty
    d = group_pairs2dict(swap_pairs(d.items()))
    
    assert all(d.values())
    return d











