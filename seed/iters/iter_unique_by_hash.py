
__all__ = '''
    iter_unique_by_hash
    remove_duplicates_by_hash
    '''.split()

from seed.tiny import echo

def remove_duplicates_by_hash(iterable, *, key=None, container=tuple):
    '''Hashable k => Iter a -> (a -> k) -> [a]

O(n)
'''
    return container(iter_unique_by_hash(iterable, key=key))
def iter_unique_by_hash(iterable, *, key=None):
    '''Hashable k => Iter a -> (a -> k) -> Iter a

O(n)
'''
    if key is None:
        key = echo

    s = set()
    for a in iterable:
        k = key(a)
        if k not in s:
            yield a
            s.add(k)


