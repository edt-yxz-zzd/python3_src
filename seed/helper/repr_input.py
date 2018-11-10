
__all__ = r'''
    repr_helper_ex

    repr_helper
    repr_helper__str

    repr_input_ex
    repr_input

    repr_args
    repr_kwargs
    repr_kwargs__ordered_pairs
    '''.split()

def get_class_name(obj):
    return type(obj).__name__
def repr_args(args):
    return ', '.join(map(repr, args))

def repr_kwargs(kwargs):
    return repr_kwargs__ordered_pairs(sorted(kwargs.items()))
def repr_kwargs__ordered_pairs(pairs):
    return ', '.join('{!s} = {!r}'.format(name, value) for name, value in pairs)

def repr_input_ex(args, ordered_kwarg_pairs, kwargs):
    a = repr_args(args)
    o = repr_kwargs__ordered_pairs(ordered_kwarg_pairs)
    k = repr_kwargs(kwargs)

    return ', '.join(filter(None, [a, o, k]))

def repr_helper_ex(self, args, ordered_kwarg_pairs, kwargs
    , *, self_is_name=False
    ):
    if self_is_name:
        assert isinstance(self, str)
        constructor_name = self
    else:
        constructor_name = get_class_name(self)
    s = repr_input_ex(args, ordered_kwarg_pairs, kwargs)
    return '{}({})'.format(constructor_name, s)




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







