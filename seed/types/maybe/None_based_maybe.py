
# sometimes, we knows that: the obj can not be None


__all__ = '''
    unjust
    
    nothing
    just
    is_maybe
    is_just
    is_nothing

'''.split()

def unjust(x):
    if x is None:
        raise ValueError('unjust nothing')
    return x

nothing = None
def just(x):
    if x is None:
        raise ValueError('can not just None; this is None_based_maybe')
    return x

def is_maybe(x):
    return True
def is_just(x):
    return x is not None
def is_nothing(x):
    return x is None



















