

def get_class_name(obj):
    return type(obj).__name__
def repr_args(args):
    return ', '.join(map(repr, args))

def repr_kwargs(kwargs):
    return ', '.join('{!s} = {!r}'.format(key, val)
                     for key, val in sorted(kwargs.items()))


def repr_helper(self, *args, **kwargs):
    return repr_helper__str(get_class_name(self), *args, **kwargs)
def repr_helper__str(constructor_name, *args, **kwargs):
    assert type(constructor_name) is str
    return '{}({})'.format(constructor_name, repr_input(*args, **kwargs))
def repr_input(*args, **kwargs):
    '''\
aid __repr__ implement

usage:
    class XX:
        def __repr__(self):
            return '{}({})'.format(get_class_name(self),
                                   repr_input(...))
e.g.:
    >>> repr_input()
    ''
    >>> repr_input(1)
    '1'
    >>> repr_input(1,'a')
    "1, 'a'"
    >>> repr_input(a=1)
    'a = 1'
    >>> repr_input(a=1, b='b')
    "a = 1, b = 'b'"
    >>> repr_input(1, a=1)
    '1, a = 1'
'''
    a = repr_args(args)
    k = repr_kwargs(kwargs)
    
    return ', '.join(filter(None, [a, k]))


assert repr_input() == ''
assert repr_input(1) == '1'
assert repr_input(1,'a') == "1, 'a'"
assert repr_input(a=1) == 'a = 1'
assert repr_input(a=1, b='b') == "a = 1, b = 'b'"
assert repr_input(1, a=1) == '1, a = 1'



if __name__ == "__main__":
    import doctest
    doctest.testmod()







