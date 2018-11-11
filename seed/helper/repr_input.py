
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
    ordered_kwarg_pairs = tuple(ordered_kwarg_pairs)
    #len(args)
    #len(ordered_kwarg_pairs)
    len(kwargs)
    duplicate_keys = {attr for attr, _ in ordered_kwarg_pairs} & set(kwargs)
    if duplicate_keys:
        raise Exception(f'repr_input_ex: duplicate_keys: {duplicate_keys}')

    a = repr_args(args)
    o = repr_kwargs__ordered_pairs(ordered_kwarg_pairs)
    k = repr_kwargs(kwargs)

    return ', '.join(filter(None, [a, o, k]))

def repr_helper_ex(
    self_or_name
    , args
    , ordered_kwarg_pairs_or_ordered_attrs
    , kwargs_or_unordered_attrs
    , *
    , name_only=False
    , ordered_attrs_only=False
    , unordered_attrs_only=False
    ):
    '''

input:
    self_or_name :: object | name
        see: name_only
    args :: [object]
    ordered_kwarg_pairs_or_ordered_attrs :: [(attr, object)] | [attr]
        see: ordered_attrs_only
    kwargs_or_unordered_attrs :: {attr:object} | {attr}
        see: unordered_attrs_only
    name_only :: bool
    ordered_attrs_only :: bool
    unordered_attrs_only :: bool
output:
    formatted_string :: str
        {name}({args}, {ordered_kwarg_pairs}, {kwargs})

>>> class C:
...     def __init__(self, __1, __2, name1, name2, *, kw1, kw2):
...         self.__1 = __1
...         self.__2 = __2
...         self.name1 = name1
...         self.name2 = name2
...         self.kw1 = kw1
...         self.kw2 = kw2
...     def get_args(self):
...         args = self.__1, self.__2
...         return args
...     def get_o_attrs(self):
...         o_attrs = 'name1 name2'.split()
...         return o_attrs
...     def get_u_attrs(self):
...         u_attrs = 'kw1 kw2'.split()
...         return u_attrs
...     def __repr__(self):
...         args = self.get_args()
...         o_attrs = self.get_o_attrs()
...         u_attrs = self.get_u_attrs()
...         return repr_helper_ex(self, args, o_attrs, u_attrs, ordered_attrs_only=True, unordered_attrs_only=True)
>>> c = C(1, 2, name1='n1', name2='n2', kw1='k1', kw2='k2')
>>> c
C(1, 2, name1 = 'n1', name2 = 'n2', kw1 = 'k1', kw2 = 'k2')

>>> repr_helper_ex('T', c.get_args(), c.get_o_attrs(), c.get_u_attrs(), name_only=True, ordered_attrs_only=True, unordered_attrs_only=True)
Traceback (most recent call last):
    ...
Exception: cannot turn on "name_only" and "ordered_attrs_only" at same time
>>> repr_helper_ex(c, c.get_args(), [('name3', 'n3'), ('name4', 'n4')], c.get_u_attrs(), name_only=False, ordered_attrs_only=False, unordered_attrs_only=True)
"C(1, 2, name3 = 'n3', name4 = 'n4', kw1 = 'k1', kw2 = 'k2')"
>>> repr_helper_ex(c, (3, 4), [('name3', 'n3'), ('name4', 'n4')], c.get_u_attrs(), name_only=False, ordered_attrs_only=False, unordered_attrs_only=True)
"C(3, 4, name3 = 'n3', name4 = 'n4', kw1 = 'k1', kw2 = 'k2')"
>>> repr_helper_ex(c, (3, 4), [('name3', 'n3'), ('name4', 'n4')], {'kw3':'k3', 'kw4':'k4'}, name_only=False, ordered_attrs_only=False, unordered_attrs_only=False)
"C(3, 4, name3 = 'n3', name4 = 'n4', kw3 = 'k3', kw4 = 'k4')"
>>> repr_helper_ex('T', (3, 4), [('name3', 'n3'), ('name4', 'n4')], {'kw3':'k3', 'kw4':'k4'}, name_only=True, ordered_attrs_only=False, unordered_attrs_only=False)
"T(3, 4, name3 = 'n3', name4 = 'n4', kw3 = 'k3', kw4 = 'k4')"

'''
    name_only = bool(name_only)
    ordered_attrs_only = bool(ordered_attrs_only)
    unordered_attrs_only = bool(unordered_attrs_only)

    if name_only:
        name = self_or_name
        assert isinstance(name, str)
        constructor_name = name

        if ordered_attrs_only:
            raise Exception('cannot turn on "name_only" and "ordered_attrs_only" at same time')
        if unordered_attrs_only:
            raise Exception('cannot turn on "name_only" and "unordered_attrs_only" at same time')

        ordered_kwarg_pairs = ordered_kwarg_pairs_or_ordered_attrs
        kwargs = kwargs_or_unordered_attrs
    else:
        self = self_or_name
        constructor_name = get_class_name(self)

        if ordered_attrs_only:
            ordered_attrs = ordered_kwarg_pairs_or_ordered_attrs
            ordered_kwarg_pairs = [(attr, getattr(self, attr)) for attr in ordered_attrs]
        else:
            ordered_kwarg_pairs = ordered_kwarg_pairs_or_ordered_attrs
        if unordered_attrs_only:
            unordered_attrs = kwargs_or_unordered_attrs
            kwargs = {attr: getattr(self, attr) for attr in unordered_attrs}
        else:
            kwargs = kwargs_or_unordered_attrs

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







