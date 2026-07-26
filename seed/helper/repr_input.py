#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/repr_input.py
    view ../../python3_src/seed/helper/repr_input.py
    view ../../python3_src/seed/types/NamedTupleBase.py
    view ../../python3_src/seed/helper/stable_repr.py
    view ../../python3_src/seed/types/HistorySaver.py
        @20260721
        => ++kw:compact6kwargs
        => ++kw:vars4self
        => ++mk_ordered_kwarg_pairs_()

seed.helper.repr_input
py -m nn_ns.app.debug_cmd   seed.helper.repr_input -x
py -m nn_ns.app.doctest_cmd seed.helper.repr_input:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.helper.repr_input:repr_helper_ex,mk_ordered_kwarg_pairs_ -v
py -m nn_ns.app.doctest_cmd 'seed.helper.repr_input!' -ht
py -m seed.helper.repr_input
py -m nn_ns.app.doctest_cmd seed.types.NamedTupleBase:__doc__


py_adhoc_call   seed.helper.repr_input   @f
#]]]'''#'''

__all__ = r'''
mk_ordered_kwarg_pairs_
repr_helper_ex
    repr_helper
    repr_helper__str

repr_input_ex
    repr_input

    repr_args
    repr_kwargs
    repr_kwargs__ordered_pairs




ReprError
get_class_name

mk_ordered_kwarg_pairs_
    mk_ordered_kwarg_pair_
    dummy_self
    parse4item6specification_
    get_attr6self_or_vars_
'''.split()#'''

___begin_mark_of_excluded_global_names__0___ = ...
from seed.lang.is_valid_python_id import is_valid_python_id
from keyword import iskeyword
___end_mark_of_excluded_global_names__0___ = ...

class ReprError(Exception):pass

def get_class_name(obj):
    return type(obj).__name__
def repr_args(args):
    return ', '.join(map(repr, args))

def repr_kwargs(kwargs, *, special4py_kw, compact6kwargs):
    return repr_kwargs__ordered_pairs(sorted(kwargs.items()), special4py_kw=special4py_kw, compact6kwargs=compact6kwargs)
def repr_kwargs__ordered_pairs(pairs, *, special4py_kw, compact6kwargs):
    special4py_kw = bool(special4py_kw)
    compact6kwargs = bool(compact6kwargs)
    return ', '.join(_repr_kwarg_pair_(name, value, special4py_kw=special4py_kw, compact6kwargs=compact6kwargs) for name, value in pairs)
    return ', '.join('{!s} = {!r}'.format(name, value) for name, value in pairs)
def _repr_kwarg_pair_(nm, v, *, special4py_kw, compact6kwargs):
    if special4py_kw and iskeyword(nm):
        if not compact6kwargs:
            fmt = '**{{{!r}: {!r}}}'
        else:
            fmt = '**{{{!r}:{!r}}}'
    else:
        if not compact6kwargs:
            fmt = '{!s} = {!r}'
        else:
            fmt = '{!s}={!r}'
    return fmt.format(nm, v)

def repr_input_ex(args, ordered_kwarg_pairs, kwargs, *, special4py_kw, compact6kwargs):
    ordered_kwarg_pairs = tuple(ordered_kwarg_pairs)
    #len(args)
    #len(ordered_kwarg_pairs)
    len(kwargs)
    duplicate_keys = {attr for attr, _ in ordered_kwarg_pairs} & set(kwargs)
    if duplicate_keys:
        raise ReprError(f'repr_input_ex: duplicate_keys: {duplicate_keys}')

    a = repr_args(args)
    o = repr_kwargs__ordered_pairs(ordered_kwarg_pairs, special4py_kw=special4py_kw, compact6kwargs=compact6kwargs)
    k = repr_kwargs(kwargs, special4py_kw=special4py_kw, compact6kwargs=compact6kwargs)

    return ', '.join(filter(None, [a, o, k]))

class _DummySelf:
    def __getattribute__(sf, nm, /):
        raise AttributeError(nm)
dummy_self = _DummySelf()
def _test_dummy_self():
    try:
        dummy_self.__class__
    except AttributeError:
        pass
    else:
        raise 000
if 0:_test_dummy_self()
def parse4item6specification_(item6specification, /):
    nm7dst, _, smay_nm7src = item6specification.partition(':')
    nm7dst = nm7dst.strip()
    smay_nm7src = smay_nm7src.strip()
    nm7src = smay_nm7src if smay_nm7src else nm7dst
    if 0:
        assert nm7dst.isidentifier()
        assert nm7src.isidentifier()
    return (nm7dst, nm7src)
def get_attr6self_or_vars_(self, vars4self, nm7src, /):
    try:
        return vars4self[nm7src]
    except KeyError:
        pass
    return getattr(self, nm7src)
def mk_ordered_kwarg_pair_(self, vars4self, item6specification, /):
    (nm7dst, nm7src) = parse4item6specification_(item6specification)
    value = get_attr6self_or_vars_(self, vars4self, nm7src)
    return (nm7dst, value)
def mk_ordered_kwarg_pairs_(may_self, may_vars4self, specification, /):
    r'''[[[
    may self -> may vars4self/{nm:v} -> str -> [(nm,v)]

    [specification : eg: "", "x", "x:_y,z,a:_b,c"]
    [specification == regex"({<item6specification>}(,{<item6specification>})*)?\s*"]
    [item6specification == regex"\s*{<nm7dst>}(:{<nm7src>})?\s*"]
    [nm7dst == regex"{<nm7xxx>}"]
    [nm7src == regex"{<nm7xxx>}"]
    [nm7xxx == regex"\s*\w+\s*"]


>>> dummy_self.__getattribute__
Traceback (most recent call last):
    ...
AttributeError: __getattribute__
>>> object().__getattribute__  #doctest: +ELLIPSIS
<method-wrapper '__getattribute__' of object object at 0x...>
>>> class C:
...     x = 'xxx'
...     _a = 'aaa'
>>> sf = C()
>>> d = dict(_z='zzz', c='ccc')
>>> mk_ordered_kwarg_pairs_(None, None, '')
[]
>>> mk_ordered_kwarg_pairs_(None, None, '   ')
[]
>>> mk_ordered_kwarg_pairs_(None, None, 'c')
Traceback (most recent call last):
    ...
AttributeError: c
>>> mk_ordered_kwarg_pairs_(None, d, 'c')
[('c', 'ccc')]
>>> mk_ordered_kwarg_pairs_(None, d, 'x,c')
Traceback (most recent call last):
    ...
AttributeError: x
>>> mk_ordered_kwarg_pairs_(sf, d, 'x,c')
[('x', 'xxx'), ('c', 'ccc')]
>>> mk_ordered_kwarg_pairs_(sf, d, 'x,z:_z,a:_a,c')
[('x', 'xxx'), ('z', 'zzz'), ('a', 'aaa'), ('c', 'ccc')]
>>> mk_ordered_kwarg_pairs_(sf, d, ' x , z : _z , a : _a , c ')
[('x', 'xxx'), ('z', 'zzz'), ('a', 'aaa'), ('c', 'ccc')]








    #]]]'''#'''
    if not type(specification) is str:raise TypeError(type(specification))
    self = may_self if not may_self is None else dummy_self
    vars4self = may_vars4self if not may_vars4self is None else {}
    specification = specification.strip()
    if not specification:
        ordered_kwarg_pairs = []
    else:
        ss = specification.split(',')
        ordered_kwarg_pairs = [mk_ordered_kwarg_pair_(self, vars4self, item6specification) for item6specification in ss]
    return ordered_kwarg_pairs
def repr_helper_ex(
    self_or_name
    , args
    , ordered_kwarg_pairs_or_ordered_attrs
    , kwargs_or_unordered_attrs
    , *
    , name_only=False
    , ordered_attrs_only=False
    , unordered_attrs_only=False
    , special4py_kw=True # is_valid_python_id/iskeyword
    , compact6kwargs=False
    , vars4self=None
    ):
    r'''

input:
    self_or_name :: object | name
        see: name_only
    args :: [object]
    ordered_kwarg_pairs_or_ordered_attrs :: [(attr, object)] | [attr]
        see: ordered_attrs_only
        see: mk_ordered_kwarg_pairs_()
    kwargs_or_unordered_attrs :: {attr:object} | {attr}
        see: unordered_attrs_only

    name_only :: bool
        if name_only:
            name = self_or_name
        else:
            self = self_or_name

    ordered_attrs_only :: bool
        if ordered_attrs_only:
            ordered_attrs = ordered_kwarg_pairs_or_ordered_attrs
            ordered_kwarg_pairs = [...getattr(self, ...)...]
        else:
            ordered_kwarg_pairs = ordered_kwarg_pairs_or_ordered_attrs

    unordered_attrs_only :: bool
        if unordered_attrs_only:
            unordered_attrs = kwargs_or_unordered_attrs
            kwargs = {...getattr(self, ...)...}
        else:
            kwargs = kwargs_or_unordered_attrs

    special4py_kw :: bool
        if special4py_kw and iskeyword(nm):
            f'**{{nm!r}: {v!r}'
        else:
            f'{nm!s} = {v!r}'
    compact6kwargs :: bool
        if compact6kwargs:
            f'{nm!s}={v!r}'
        else:
            f'{nm!s} = {v!r}'

    vars4self :: (None|{attr:val})
        see:ordered_attrs_only
        see:unordered_attrs_only

output:
    formatted_string :: str
        {name}({args}, {ordered_kwarg_pairs}, {kwargs})


>>> from seed.helper.repr_input import repr_helper, repr_helper_ex
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
seed.helper.repr_input.ReprError: cannot turn on "name_only" and "ordered_attrs_only" at same time
>>> repr_helper_ex(c, c.get_args(), [('name3', 'n3'), ('name4', 'n4')], c.get_u_attrs(), name_only=False, ordered_attrs_only=False, unordered_attrs_only=True)
"C(1, 2, name3 = 'n3', name4 = 'n4', kw1 = 'k1', kw2 = 'k2')"
>>> repr_helper_ex(c, (3, 4), [('name3', 'n3'), ('name4', 'n4')], c.get_u_attrs(), name_only=False, ordered_attrs_only=False, unordered_attrs_only=True)
"C(3, 4, name3 = 'n3', name4 = 'n4', kw1 = 'k1', kw2 = 'k2')"
>>> repr_helper_ex(c, (3, 4), [('name3', 'n3'), ('name4', 'n4')], {'kw3':'k3', 'kw4':'k4'}, name_only=False, ordered_attrs_only=False, unordered_attrs_only=False)
"C(3, 4, name3 = 'n3', name4 = 'n4', kw3 = 'k3', kw4 = 'k4')"
>>> repr_helper_ex('T', (3, 4), [('name3', 'n3'), ('name4', 'n4')], {'kw3':'k3', 'kw4':'k4'}, name_only=True, ordered_attrs_only=False, unordered_attrs_only=False)
"T(3, 4, name3 = 'n3', name4 = 'n4', kw3 = 'k3', kw4 = 'k4')"

>>> repr_helper_ex('T', (3, 4), [('name3', 'n3'), ('def', 'n4')], {'kw3':'k3', 'def':'k4'}, name_only=True, ordered_attrs_only=False, unordered_attrs_only=False)
Traceback (most recent call last):
    ...
seed.helper.repr_input.ReprError: repr_input_ex: duplicate_keys: {'def'}

>>> repr_helper_ex('T', (3, 4), [('name3', 'n3'), ('def', 'n4')], {'kw3':'k3', 'class':'k4', 'import':'k5', 'from':'k6'}, name_only=True, ordered_attrs_only=False, unordered_attrs_only=False)
"T(3, 4, name3 = 'n3', **{'def': 'n4'}, **{'class': 'k4'}, **{'from': 'k6'}, **{'import': 'k5'}, kw3 = 'k3')"

>>> repr_helper_ex('T', (3, 4), [('name3', 'n3'), ('def', 'n4')], {'kw3':'k3', 'class':'k4', 'import':'k5', 'from':'k6'}, name_only=True, ordered_attrs_only=False, unordered_attrs_only=False, special4py_kw=False)
"T(3, 4, name3 = 'n3', def = 'n4', class = 'k4', from = 'k6', import = 'k5', kw3 = 'k3')"

>>> repr_helper_ex('T', (3, 4), [('name3', 'n3'), ('def', 'n4')], {'kw3':'k3', 'class':'k4', 'import':'k5', 'from':'k6'}, name_only=True, ordered_attrs_only=False, unordered_attrs_only=False, special4py_kw=False, compact6kwargs=True)
"T(3, 4, name3='n3', def='n4', class='k4', from='k6', import='k5', kw3='k3')"
>>> repr_helper_ex('T', (3, 4), ['name3', 'def'], {'kw3', 'class', 'import', 'from'}, name_only=True, ordered_attrs_only=True, unordered_attrs_only=True, special4py_kw=False, compact6kwargs=True, vars4self={'name3':'n3', 'def':'n4', 'kw3':'k3', 'class':'k4', 'import':'k5', 'from':'k6'})
"T(3, 4, name3='n3', def='n4', class='k4', from='k6', import='k5', kw3='k3')"

'''#'''
    name_only = bool(name_only)
    ordered_attrs_only = bool(ordered_attrs_only)
    unordered_attrs_only = bool(unordered_attrs_only)
    special4py_kw = bool(special4py_kw)
    if not vars4self is None:
        #if not hasattr(vars4self, '__getitem__'):raise TypeError(type(vars4self))
        if not hasattr(type(vars4self), '__getitem__'):raise TypeError(type(vars4self))
    else:
        vars4self = {}

    if name_only:
        name = self_or_name
        assert isinstance(name, str)
        constructor_name = name
        _self = dummy_self

        if not vars4self:
            if ordered_attrs_only:
                raise ReprError('cannot turn on "name_only" and "ordered_attrs_only" at same time')
            if unordered_attrs_only:
                raise ReprError('cannot turn on "name_only" and "unordered_attrs_only" at same time')

    else:
        self = self_or_name
        constructor_name = get_class_name(self)
        _self = self

    constructor_name
    _self
    vars4self
    if ordered_attrs_only or unordered_attrs_only:
        def get_attr6self_(nm, /):
            try:
                return vars4self[nm]
            except KeyError:
                pass
            return getattr(_self, nm)
        get_attr6self_

    #mk_ordered_kwarg_pairs_():goto
    if ordered_attrs_only:
        ordered_attrs = ordered_kwarg_pairs_or_ordered_attrs
        #ordered_kwarg_pairs = [(attr, getattr(self, attr)) for attr in ordered_attrs]
        ordered_kwarg_pairs = [(attr, get_attr6self_(attr)) for attr in ordered_attrs]
    else:
        ordered_kwarg_pairs = ordered_kwarg_pairs_or_ordered_attrs
    if unordered_attrs_only:
        unordered_attrs = kwargs_or_unordered_attrs
        #kwargs = {attr: getattr(self, attr) for attr in unordered_attrs}
        kwargs = {attr: get_attr6self_(attr) for attr in unordered_attrs}
    else:
        kwargs = kwargs_or_unordered_attrs

    s = repr_input_ex(args, ordered_kwarg_pairs, kwargs, special4py_kw=special4py_kw, compact6kwargs=compact6kwargs)
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
    k = repr_kwargs(kwargs, special4py_kw=True, compact6kwargs=False)

    return ', '.join(filter(None, [a, k]))


assert repr_input() == ''
assert repr_input(1) == '1'
assert repr_input(1,'a') == "1, 'a'"
assert repr_input(a=1) == 'a = 1'
assert repr_input(a=1, b='b') == "a = 1, b = 'b'"
assert repr_input(1, a=1) == '1, a = 1'



from seed.helper.repr_input import repr_helper, repr_helper__str, repr_helper_ex, mk_ordered_kwarg_pairs_
#def repr_helper(self, *args, **kwargs):
#def repr_helper__str(constructor_name, *args, **kwargs):
#def repr_helper_ex(self_or_name, args, ordered_kwarg_pairs_or_ordered_attrs, kwargs_or_unordered_attrs, *, name_only=False, ordered_attrs_only=False, unordered_attrs_only=False, special4py_kw=True, compact6kwargs=False, vars4self=None)
#def mk_ordered_kwarg_pairs_(may_self, may_vars4self, specification, /):
#   [specification : eg: "", "x", "x:_y,z,a:_b,c"]
from seed.helper.repr_input import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()
