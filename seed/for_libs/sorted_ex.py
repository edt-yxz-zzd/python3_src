
__all__ = '''
    sorted_ex
'''.split()

from functools import cmp_to_key
from seed.tiny import echo, py_cmp

def sorted_ex(iterable, *, key=None, cmp=None, reverse=False):
    '''
input:
    iterable :: Iter a
    key :: None | (a->k)
    cmp :: None | (k -> k -> (-1|0|+1))
    reverse :: bool
        reverse when sort
output:
    result :: [a]
'''
    if key is echo:
        key = None
    if cmp is py_cmp:
        cmp = None

    if cmp is not None:
        if key is not None:
            old_cmp = cmp
            old_key = key
            def new_cmp(a, b):
                return old_cmp(old_key(a), old_key(b))
            cmp = new_cmp
        new_key = cmp_to_key(cmp)
        key = new_key

    ls = sorted(iterable, key=key, reverse=reverse)
    return ls



