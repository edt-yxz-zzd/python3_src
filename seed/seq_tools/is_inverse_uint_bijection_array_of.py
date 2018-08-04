


__all__ = '''
    is_inverse_uint_bijection_array_of
    '''.split()
from seed.tiny import echo



def is_inverse_uint_bijection_array_of(
        old2new, new2old, *, key0=None, key1=None):
    '''

input:
    old2new :: [a]
    new2old :: [b]
    key0 :: a -> UInt
    key1 :: b -> UInt
see:
    is_inverse_uint_bijection_array
    inverse_uint_bijection_array
'''
    if key0 is None: key0 = echo
    if key1 is None: key1 = echo

    L = len(old2new)
    if not L == len(new2old): return False
    for old, new_a in enumerate(old2new):
        new = key0(new_a)
        if not 0 <= new < L: return False
        old_b = new2old[new]
        old2 = key1(old_b)
        if not old2 == old: return False

    return True

