
__all__ = '''
    unjust
    
    nothing
    just
    is_maybe
    is_just
    is_nothing

'''.split()

'''
not export:
    Nothing
    Just
    
    Just
    Nothing
    is_Nothing
    is_Just
    is_Maybe
'''

from ._unjust import unjust

nothing = ()
def just(x):
    return (x,)

def is_maybe(obj):
    return type(obj) is tuple and len(obj) < 2

def is_just(obj):
    'obj == nothing??'
    return is_maybe(obj) and len(obj) == 1
def is_nothing(obj):
    return is_maybe(obj) and len(obj) == 0

def unjust(just_x):
    if not is_maybe(x):
        raise TypeError('not maybe_x')

    x, = just_x
    return x


Just = just
Nothing = nothing
is_Nothing = is_nothing
is_Just = is_just
is_Maybe = is_maybe

