
__all__ = '''
    divs
    is_even
    is_odd

    even
    odd
    '''.split()

def divs(d, n):
    '''divs d n = n%d == 0

example:
    >>> divs(2, 7)
    False
    >>> divs(3, 6)
    True

'''
    return not(n%d)

def is_even(n):
    return not odd(n)
def is_odd(n):
    return bool(n&1)

even = is_even
odd = is_odd



