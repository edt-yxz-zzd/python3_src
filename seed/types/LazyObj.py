#__all__:goto
r'''[[[
e ../../python3_src/seed/types/LazyObj.py
    ++__repr__
vs:
view ../../python3_src/seed/tiny_/funcs.py
    from seed.tiny_.funcs import lazy
        #lambda
        #   => "<function <lambda> at 0x...>"

seed.types.LazyObj
py -m nn_ns.app.debug_cmd   seed.types.LazyObj -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.LazyObj:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> Lazy(999)
Lazy(999)
>>> Lazy(999).the_obj
999
>>> Lazy(999)()
999

>>> f = LazyX(repr, 999)
>>> f
LazyX(<built-in function repr>, 999)
>>> f.func_and_args
(<built-in function repr>, (999,))
>>> f.tmay_result
()
>>> f()
'999'
>>> f.tmay_result
('999',)
>>> f.func_and_args
(<built-in function repr>, (999,))
>>> f
LazyX(<built-in function repr>, 999, tmay_result = ('999',))

>>> f = LazyX(print, 999, 666)
>>> f
LazyX(<built-in function print>, 999, 666)
>>> f()
999 666
>>> f
LazyX(<built-in function print>, 999, 666, tmay_result = (None,))
>>> f() is None
True
>>> f
LazyX(<built-in function print>, 999, 666, tmay_result = (None,))


>>> mk_lazy5obj_(999)
Lazy(999)
>>> mk_lazy5func_(print, 999, 666)
LazyX(<built-in function print>, 999, 666)
>>> mk_lazy_(-1, 999)
Lazy(999)
>>> mk_lazy_(..., print, 999, 666)
LazyX(<built-in function print>, 999, 666)
>>> mk_lazy_(2, print, 999, 666)
LazyX(<built-in function print>, 999, 666)
>>> mk_lazy_(1, print, 999, 666)
LazyX(<built-in function print>, 666)
>>> mk_lazy_(0, print, 999, 666)
LazyX(<built-in function print>)
>>> mk_lazy_(3, print, 999, 666)
Traceback (most recent call last):
...
TypeError: 3
>>> mk_lazy_(-2, print, 999, 666)
Traceback (most recent call last):
...
TypeError: -2




>>> @mk_lazy_attrs_
... def values():
...     a = 111
...     b = hex(a)
...     return dict(locals())
>>> values  #doctest: +ELLIPSIS
LazyAttrs(<function values at 0x...>)
>>> values.a
111
>>> values.b
'0x6f'
>>> values.c
Traceback (most recent call last):
    ...
AttributeError: c
>>> del values.a
Traceback (most recent call last):
    ...
AttributeError: a
>>> values.a = 999
Traceback (most recent call last):
    ...
AttributeError: a
>>> values.a
111
>>> values.c = 999
Traceback (most recent call last):
    ...
AttributeError: c
>>> dir(values)
['a', 'b']
>>> 'a' in values
True
>>> 'c' in values
False
>>> len(values)
2
>>> sorted(iter(values))
['a', 'b']
>>> values()
{'a': 111, 'b': '0x6f'}
>>> values['a']
111
>>> values['c']
Traceback (most recent call last):
    ...
KeyError: 'c'


>>> from operator import call
>>> from functools import cached_property
>>> from seed.for_libs.for_functools.cached_property import cached_property
>>> @call
... class values:
...     @cached_property
...     def a(sf, /):
...         return 111
...     @cached_property
...     def b(sf, /):
...         return hex(sf.a)
...     c = cached_property(lambda sf:sf.a*4)
>>> values.b
'0x6f'
>>> values.a
111
>>> values.c
444
>>> vars(values)['c']
444
>>> values.c = 55
Traceback (most recent call last):
    ...
AttributeError: c
>>> vars(values)['c']
444
>>> vars(values)['c'] = 555
>>> values.c
555

e ../../python3_src/seed/types/CachedProperty.py
@20260316
e ../lots/NOTE/Python/python-bug/cached_property-bug.txt
>>> from functools import cached_property
>>> class C:
...     @cached_property
...     def a(sf, /):
...         return 111
>>> x = C()
>>> vars(x)
{}
>>> x.a
111
>>> vars(x)['a']
111
>>> x.a = 222  #???why not raise AttributeError?
>>> x.a
222
>>> vars(x)['a']
222

py_adhoc_call   seed.types.LazyObj   @f
]]]'''#'''
__all__ = r'''
mk_lazy_
    mk_lazy5obj_
    mk_lazy5func_
mk_lazy_attrs_

Lazy
LazyX
LazyAttrs
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_callable, check_tmay, check_int_ge_le
    from seed.helper.repr_input import repr_helper
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def mk_lazy_(emay_imay_num_args, obj_or_func, /, *args):
    imay_num_args = len(args) if emay_imay_num_args is ... else emay_imay_num_args
    check_int_ge_le(-1, len(args), imay_num_args)
    if not imay_num_args == -1:
        num_args = imay_num_args
        f = obj_or_func
        check_callable(f)
        args = args[len(args)-num_args:]
        return mk_lazy5func_(f, *args)
    else:
        x = obj_or_func
        return mk_lazy5obj_(x)
def mk_lazy5obj_(x, /):
    return Lazy(x)
def mk_lazy5func_(f, /, *args):
    return LazyX(f, *args)

class Lazy:
    def __new__(cls, x, /):
        sf = super(__class__, cls).__new__(cls)
        sf._x = x
        return sf
    @property
    def the_obj(sf, /):
        return sf._x
    def __call__(sf, /):
        return sf.the_obj
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_obj)
class LazyX:
    def __new__(cls, f, /, *args, tmay_result=()):
        check_callable(f)
        check_tmay(tmay_result)
        sf = super(__class__, cls).__new__(cls)
        sf._f_args = (f, args)
        sf._tm = tmay_result
        return sf
    @property
    def func_and_args(sf, /):
        return sf._f_args
    @property
    def tmay_result(sf, /):
        return sf._tm
    def __call__(sf, /):
        match sf.tmay_result:
            case (x,):
                return x
            case ():
                pass
            case _:
                raise 000
            #
        (f, args) = sf.func_and_args
        x = f(*args)
        sf._tm = (x,)
        return sf()
    def __repr__(sf, /):
        (f, args) = sf.func_and_args
        if sf.tmay_result:
            return repr_helper(sf, f, *args, tmay_result=sf.tmay_result)
        return repr_helper(sf, f, *args)

_get = object.__getattribute__
_set = object.__setattr__
_del = object.__delattr__
class LazyAttrs:
    r'''[[[
    LazyAttrs:batch eval
        @mk_lazy_attrs_
        def values():
            a = 111
            b = hex(a)
            return dict(locals())
    vs:
        solo eval:
        from operator import call
        from functools import cached_property
        from seed.for_libs.for_functools.cached_property import cached_property
        @call
        class values:
            @cached_property
            def a(sf, /):
                return 111
            @cached_property
            def b(sf, /):
                return hex(sf.a)
            c = cached_property(lambda sf:sf.a*4)

    ]]]'''#'''
    def __new__(cls, lazy_nm2v, /):
        check_callable(lazy_nm2v)
        sf = super(__class__, cls).__new__(cls)
        _set(sf, '_f', lazy_nm2v)
        _set(sf, '_m', None)
        return sf
    def __dir__(sf, /):
        nm2v = sf()
        return nm2v.keys()
    def __contains__(sf, nm, /):
        nm2v = sf()
        return nm in nm2v.keys()
    def __len__(sf, /):
        nm2v = sf()
        return len(nm2v)
    def __iter__(sf, /):
        nm2v = sf()
        return iter(nm2v)
    def __getitem__(sf, nm, /):
        nm2v = sf()
        return nm2v[nm]
    def __getattribute__(sf, nm, /):
        try:
            return sf[nm]
        except LookupError:
            raise AttributeError(nm)
    def __setattr__(sf, nm, v, /):
        raise AttributeError(nm)
    def __delattr__(sf, nm, /):
        raise AttributeError(nm)

    def __call__(sf, /):
        match _get(sf, '_m'):
            case None:
                pass
            case nm2v:
                return nm2v
            #
        lazy_nm2v = _get(sf, '_f')
        nm2v = lazy_nm2v()
        _set(sf, '_m', nm2v)
        return sf()
    def __repr__(sf, /):
        lazy_nm2v = _get(sf, '_f')
        return repr_helper(sf, lazy_nm2v)

def mk_lazy_attrs_(lazy_nm2v, /):
    return LazyAttrs(lazy_nm2v)

__all__
from seed.types.LazyObj import mk_lazy_, mk_lazy5obj_, mk_lazy5func_, mk_lazy_attrs_
from seed.types.LazyObj import Lazy, LazyX, LazyAttrs
from seed.types.LazyObj import *
