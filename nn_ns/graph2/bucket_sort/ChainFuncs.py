
'''
example:
    >>> mul = lambda x:x*2
    >>> add = lambda x:x+2
    >>> funcs = [mul, add]
    >>> ChainFuncs(funcs)(3)
    10
    >>> apply(3, funcs)
    8
    >>> may_apply(3, [mul, None, add])
    8
'''

__all__ = '''
    ChainFuncs
    apply
    may_apply

    filterout_None
    '''.split()

def filterout_None(iterable):
    return (x for x in iterable if x is not None)
class ChainFuncs:
    # call in reversed order
    def __init__(self, __mayfuncs):
        self.funcs = tuple(filterout_None(__mayfuncs))
    def __call__(self, __obj):
        return apply(__obj, reversed(self.funcs))

def may_apply(__obj, __mayfuncs):
    # __mayfuncs :: iter<callable|None>
    # apply from left to right
    return apply(__obj, filterout_None(__mayfuncs))
def apply(__obj, __funcs):
    # __funcs :: iter<callable>
    # apply from left to right
    x = __obj
    for f in __funcs:
        x = f(x)
    return x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
