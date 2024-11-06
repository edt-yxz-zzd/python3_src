#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_inspect.py
[[
see:
    seed.tiny_.bmk_pairs
        bracket-make-pairs
        using __getitem__, not __call__

    seed.types.MakeDict
        baseclass
        using "class"

    seed.for_libs.for_inspect
        @decorator
        using api-signature #inspect.getfullargspec

    seed.helper.mk_pairs
        asm above
]]

seed.for_libs.for_inspect
py -m nn_ns.app.debug_cmd   seed.for_libs.for_inspect -x
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.for_libs.for_inspect   @f
py -m nn_ns.app.doctest_cmd seed.for_libs.for_inspect:__doc__ -v

from seed.for_libs.for_inspect import get_signature_of__py3_

from seed.for_libs.for_inspect import pairs5api_, pairs5api__zdefault_
from seed.for_libs.for_inspect import pairs5api__raise, pairs5api__Nothing_, pairs5api__None

from seed.for_libs.for_inspect import triples5api_, triples5api__zdefault_
from seed.for_libs.for_inspect import triples5api__raise, triples5api__Nothing_, triples5api__None



from inspect import signature as _get_signature_of__py3 #py2/py3 api diff, py3/py4 may be diff too.
from py3_8_1__doc_html
    inspect.signature(callable, *, follow_wrapped=True) -> Signature
    inspect.getfullargspec::Note ==>> getfullargspec()只用于py2代码维护，不如signature()
    inspect.getargspec::Deprecated声明==>> getargspec@py2  vs  getfullargspec@py3_0

Deprecated since version 3.0:inspect.getargspec(func) -> ArgSpec(args, varargs, keywords, defaults)
  # *varargs, **keywords
  args :: [name]
      no POSITIONAL_ONLY
      all POSITIONAL_OR_KEYWORD
  varargs :: may name
      no KEYWORD_ONLY
  keywords :: may name
  defaults :: may tuple<py_obj>
      for .args[len(.args)-len(defaults):]
      no any for .keywords
        <<== no KEYWORD_ONLY



Signature:
    -> return_annotation
    -> Signature.empty
    ===
    .parameters :: OrderedDict<name,Parameter>
    .return_annotation :: Signature.empty|object
    .bind(*args, **kwargs) -> BoundArguments
    .bind_partial(*args, **kwargs) -> BoundArguments
    ===

Parameter:
    name:annotation=default
    name:Parameter.empty=Parameter.empty
    kind <- def _(POSITIONAL_ONLY:0, /, POSITIONAL_OR_KEYWORD:1, *VAR_POSITIONAL:2, KEYWORD_ONLY:3, **VAR_KEYWORD:4)
    ===
    .kind : str
    .name : str
    .annotation :: Parameter.empty|object
    .default :: Parameter.empty|object
    ===

BoundArguments:
    # .arguments <==> (*.args, **.kwargs)
    ===
    .signature : Signature
    .args : tuple
    .kwargs : dict
    .arguments : OrderedDict<name,arg>
         args4calling_api
         func.locals at start except defaults
            vs: getcallargs()
    ===












>>> from seed.for_libs.for_inspect import get_signature_of__py3_, get_signature_of__py2_
>>> def f(_0,_1:11,_2=222,_3:33=333, /, a, b:'bb', c='ccc', d:'dd'='ddd', *ls, w, x:'xx', y='yyy', z:'zz'='zzz', **kwargs):pass
Traceback (most recent call last):
    def f(_0,_1:11,_2=222,_3:33=333, /, a, b:'bb', c='ccc', d:'dd'='ddd', *ls, w, x:'xx', y='yyy', z:'zz'='zzz', **kwargs):pass
                                        ^
SyntaxError: non-default argument follows default argument

>>> def f(_0,_1:11,_2=222,_3:33=333, /, a=999, b:'bb'=666, c='ccc', d:'dd'='ddd', *args:'`args`', w, x:'xx', y='yyy', z:'zz'='zzz', **kwargs:'`kwargs`'):pass
>>> get_signature_of__py3_(f)
(((('_0', (), ()), ('_1', (11,), ()), ('_2', (), (222,)), ('_3', (33,), (333,))), (('a', (), (999,)), ('b', ('bb',), (666,)), ('c', (), ('ccc',)), ('d', ('dd',), ('ddd',))), (('args', ('`args`',), ()),), (('w', (), ()), ('x', ('xx',), ()), ('y', (), ('yyy',)), ('z', ('zz',), ('zzz',))), (('kwargs', ('`kwargs`',), ()),)), ())
>>> get_signature_of__py2_(f)
Traceback (most recent call last):
    ...
ValueError: Function has keyword-only parameters or annotations, use inspect.signature() API which can support them
>>> def f(a, b='bbb', *args, **kwargs):pass
>>> get_signature_of__py3_(f)
(((), (('a', (), ()), ('b', (), ('bbb',))), (('args', (), ()),), (), (('kwargs', (), ()),)), ())
>>> get_signature_of__py2_(f)
((('a', ()), ('b', ('bbb',))), 'args', 'kwargs')
>>> def f(a, b='bbb'):pass
>>> get_signature_of__py3_(f)
(((), (('a', (), ()), ('b', (), ('bbb',))), (), (), ()), ())
>>> get_signature_of__py2_(f)
((('a', ()), ('b', ('bbb',))), None, None)
>>> f = bool
>>> get_signature_of__py3_(f)
Traceback (most recent call last):
    ...
ValueError: no signature found for builtin type <class 'bool'>
>>> f = set.add
>>> get_signature_of__py3_(f)
Traceback (most recent call last):
    ...
ValueError: no signature found for builtin <method 'add' of 'set' objects>
>>> get_signature_of__py2_(f)
Traceback (most recent call last):
    ...
TypeError: unsupported callable
>>> f = set().add
>>> get_signature_of__py3_(f) #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
ValueError: no signature found for builtin <built-in method add of set object at 0x...>
>>> get_signature_of__py2_(f)
Traceback (most recent call last):
    ...
TypeError: unsupported callable
>>> f = int.from_bytes
>>> get_signature_of__py3_(f)
(((), (('bytes', (), ()), ('byteorder', (), ())), (), (('signed', (), (False,)),), ()), ())
>>> get_signature_of__py2_(f)
Traceback (most recent call last):
    ...
ValueError: Function has keyword-only parameters or annotations, use inspect.signature() API which can support them








>>> from seed.for_libs.for_inspect import pairs5api_, pairs5api__zdefault_
>>> from seed.for_libs.for_inspect import pairs5api__raise, pairs5api__Nothing_, pairs5api__None
>>> from seed.tiny import echo

>>> class ok(Exception):pass
>>> class bad(Exception):pass
>>> ok.__module__ = '__main__'
>>> bad.__module__ = '__main__'



>>> @pairs5api__raise
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @pairs5api__raise
... def ps(a='aaa', b='bbb'):pass
>>> ps
[('a', 'aaa'), ('b', 'bbb')]
>>> @pairs5api__Nothing_(999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api__None
... def ps(a, b='bbb'):pass
>>> ps
[('a', None), ('b', 'bbb')]




>>> @pairs5api_
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @pairs5api_(None, 1, echo)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 'a'), ('b', 'bbb')]
>>> @pairs5api_(None, 999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api_
... def ps(a='aaa', b='bbb'):pass
>>> ps
[('a', 'aaa'), ('b', 'bbb')]
>>> @pairs5api_
... def ps(_0=999, /, a='aaa', b='bbb'):pass
>>> ps
[('_0', 999), ('a', 'aaa'), ('b', 'bbb')]
>>> @pairs5api__zdefault_(999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api__zdefault_(-1, 999)
... def ps(a, b='bbb'):pass
>>> ps
[('a', 999), ('b', 'bbb')]
>>> @pairs5api__zdefault_(0, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok()), ('b', 'bbb')]
>>> @pairs5api__zdefault_(1, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok(111)), ('b', 'bbb')]
>>> @pairs5api__zdefault_(2, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok(222, 111)), ('b', 'bbb')]
>>> @pairs5api__zdefault_(4, ok, 333, 222, 111)
... def ps(a, b='bbb'):pass
>>> ps
[('a', ok('a', 333, 222, 111)), ('b', 'bbb')]


>>> @pairs5api__zdefault_()
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @pairs5api__zdefault_(-3- -1, bad(999))
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
bad: 999




>>> @pairs5api_
... def ps(a, b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @pairs5api_
... def ps(a='aaa', b='bbb', *_):pass
Traceback (most recent call last):
    ...
TypeError: varargs occur
>>> @pairs5api_
... def ps(a='aaa', b='bbb', **_):pass
Traceback (most recent call last):
    ...
TypeError: varkwargs occur
>>> @pairs5api_
... def ps(a='aaa', b='bbb', *, _):pass
Traceback (most recent call last):
    ...
ValueError: Function has keyword-only parameters or annotations, use inspect.signature() API which can support them
>>> @pairs5api_
... def ps(a='aaa', b='bbb', *, _=999):pass
Traceback (most recent call last):
    ...
ValueError: Function has keyword-only parameters or annotations, use inspect.signature() API which can support them
>>> @pairs5api_
... def ps(_0, /, a='aaa', b='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value




>>> class TEST:
...     def f(sf, /, a='aaa'):pass
...     @classmethod
...     def g(cls, /, a='aaa'):pass
>>> pairs5api_(TEST.g)
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> pairs5api_(TEST.f)
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> pairs5api_(TEST().f)
Traceback (most recent call last):
    ...
TypeError: miss default value








>>> from seed.for_libs.for_inspect import triples5api_, triples5api__zdefault_
>>> from seed.for_libs.for_inspect import triples5api__raise, triples5api__Nothing_, triples5api__None

>>> @triples5api__raise
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__raise
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__raise
... def ts(a:'aa'='aaa', b:'bb'='bbb'):pass
>>> ts
[('a', 'aa', 'aaa'), ('b', 'bb', 'bbb')]
>>> @triples5api__Nothing_(999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api__None
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', None, None), ('b', 'bb', 'bbb')]




>>> @triples5api_
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api_
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api_(None, 1, echo)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 'a', 'a'), ('b', 'bb', 'bbb')]
>>> @triples5api_(None, 999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api_
... def ts(a:'aa'='aaa', b:'bb'='bbb'):pass
>>> ts
[('a', 'aa', 'aaa'), ('b', 'bb', 'bbb')]

>>> @triples5api__zdefault_(999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(-1, 999)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', 999, 999), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(0, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok(), ok()), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(1, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok(111), ok(111)), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(2, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok(222, 111), ok(222, 111)), ('b', 'bb', 'bbb')]
>>> @triples5api__zdefault_(4, ok, 333, 222, 111)
... def ts(a, b:'bb'='bbb'):pass
>>> ts
[('a', ok('a', 333, 222, 111), ok('a', 333, 222, 111)), ('b', 'bb', 'bbb')]

>>> @triples5api__zdefault_()
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__zdefault_()
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> @triples5api__zdefault_(-3- -1, bad(999))
... def ts(a='aaa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
bad: 999
>>> @triples5api__zdefault_(-3- -1, bad(999))
... def ts(a:'aa', b:'bb'='bbb'):pass
Traceback (most recent call last):
    ...
bad: 999







#]]]'''
__all__ = r'''
    check_num_args_ok_
        is_num_args_ok_

    extract_info5parameter__py3_
    get_signature_of__py3_
    get_signature_of__py2_

    pairs5api_
        pairs5api__zdefault_
        pairs5api__raise
        pairs5api__Nothing_
        pairs5api__None

    triples5api_
        triples5api__zdefault_
        triples5api__raise
        triples5api__Nothing_
        triples5api__None

'''.split()#'''
__all__


import inspect
try:
    from inspect import getargspec as _getargspec__py2
        #Deprecated since version 3.0:inspect.getargspec(func) -> ArgSpec(args, varargs, keywords, defaults)
except ImportError:
    #fail@py3_11_9
    _getargspec__py2 = None
from inspect import signature as _get_signature_of__py3 #py2/py3 api diff, py3/py4 may be diff too.
    #inspect.signature(callable, *, follow_wrapped=True) -> Signature
    #.__wrapped__=f
    #_test4follow_wrapped():goto
from inspect import Parameter as _Parameter__py3, Signature as _Signature__py3 # py3/py4 may has diff Parameter, Signature
from seed.helper.get4may import nmay2tmay__Nothing
    #nmay2tmay__Nothing(Nothing, nmay)
from seed.debug.expectError import expectError
from seed.tiny import check_type_is
from seed.tiny_.mk_fdefault import eliminate_tmay, eliminate_tmay__cased, eliminate_tmay__mix, eliminate_tmay_or_raise, eliminate_tmay_or_raise__simple
from seed.tiny_.mk_fdefault import mk_default__easy#, mk_default, mk_default_or_raise
    #def mk_default__easy(*tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    #def mk_default(imay_xdefault_rank, xdefault, /, *args4xdefault):
    #def mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    #   imay_xdefault_ranks = (-3)-mirror_imay_xedefault_rank if mirror_imay_xedefault_rank < -1 else mirror_imay_xedefault_rank
    #   mirrored = (mirror_imay_xedefault_rank < -1) ^ bool(mirror)
    #





def is_num_args_ok_(num_args, f, /, *, imay_num_ok=False, follow_wrapped=True, ok_if_no_signature=False):
    '-> bool | ^TypeError | ^ValueError'
    return _check_num_args_ok_(_ask=True, **locals())
def check_num_args_ok_(num_args, f, /, *, imay_num_ok=False, follow_wrapped=True, ok_if_no_signature=False):
    '-> None | ^TypeError | ^ValueError'
    return _check_num_args_ok_(_ask=False, **locals())
def _check_num_args_ok_(*, num_args, f, imay_num_ok, _ask, follow_wrapped, ok_if_no_signature):
    '-> None | bool | ^TypeError | ^ValueError'
    if num_args < 0:
        if imay_num_ok and num_args == -1:
            #non_callable
            x = f
            if _ask:
                return not callable(x)
                    # -> bool
            if callable(x):raise TypeError(type(x))
                    # ^TypeError
            return
                    # -> None
        raise TypeError(num_args)
                    # ^TypeError

    ######################
    assert num_args >= 0
    if _ask and not callable(f):
        # !! get_: ^TypeError
        return False
                    # -> bool
    def get_():
        return _get_signature_of__py3(f, follow_wrapped=follow_wrapped)
            #ValueError: no signature found for builtin type <class 'bool'>
            #TypeError: 0 is not a callable object
    if ok_if_no_signature:
        try:
            sig = get_()
        except ValueError:
            #ok@no signature
            if _ask:
                return callable(f)
                    # -> bool
            if not callable(f):raise TypeError(type(f))
                    # ^TypeError
            return
                    # -> None
        sig
    else:
        sig = get_()
                    # ^ValueError
    sig
    bind_ = lambda:sig.bind(*range(num_args))
    if _ask:
        return not expectError(TypeError, bind_)
                    # -> bool
    bind_()
                    # ^TypeError
    return
                    # -> None

assert is_num_args_ok_(-1, 0, imay_num_ok=True)
assert not is_num_args_ok_(-1, lambda:0, imay_num_ok=True)
assert is_num_args_ok_(0, lambda:0)
assert not is_num_args_ok_(1, lambda:0)
assert is_num_args_ok_(1, lambda x:0)
assert expectError(ValueError, lambda:is_num_args_ok_(1, bool))
assert is_num_args_ok_(1, bool, ok_if_no_signature=True)
assert not is_num_args_ok_(1, 0)
assert expectError(ValueError, lambda:check_num_args_ok_(1, bool))
assert expectError(TypeError, lambda:check_num_args_ok_(1, lambda:0))
assert not expectError(TypeError, lambda:check_num_args_ok_(1, lambda x:0))
assert expectError(TypeError, lambda:check_num_args_ok_(1, 0))
assert expectError(TypeError, lambda:check_num_args_ok_(-1, 0))
assert not expectError(TypeError, lambda:check_num_args_ok_(-1, 0, imay_num_ok=True))

def _test4follow_wrapped():
    #inspect.signature(callable, *, follow_wrapped=True) -> Signature
    #.__wrapped__=f
    class F:
        def __call__(sf, /):
            pass
    fff = F()
    ######################
    assert is_num_args_ok_(0, fff)
    assert not is_num_args_ok_(1, fff)
    assert not is_num_args_ok_(2, fff)
    ######################
    def g(a, b):
        pass
    fff = F()
    fff.__wrapped__ = g #ok
    ######################
    assert not is_num_args_ok_(0, fff) #ok
    assert not is_num_args_ok_(1, fff)
    assert is_num_args_ok_(2, fff) #ok
    ######################
    assert is_num_args_ok_(0, fff, follow_wrapped=False)
    assert not is_num_args_ok_(1, fff, follow_wrapped=False)
    assert not is_num_args_ok_(2, fff, follow_wrapped=False)
    ######################
    ######################
    from functools import update_wrapper
    f = F()
    h = update_wrapper(f, g)
    assert h is f, h
    assert f.__wrapped__ is g
    assert not is_num_args_ok_(0, f)
    assert is_num_args_ok_(2, f)
    assert is_num_args_ok_(0, f, follow_wrapped=False)
    assert not is_num_args_ok_(2, f, follow_wrapped=False)
    #print(dir(f))
_test4follow_wrapped()

#def pairs5api__xdefault_(imay_xdefault_rank, xdefault, /, *args4xdefault):
def _mk_nm2default(*tmay_Nothing___or___args4mk_default_or_raise):
    L = len(tmay_Nothing___or___args4mk_default_or_raise)
    if L == 0:
        tmay_Nothing___or___args4mk_default_or_raise = (-3- 1, TypeError, 'miss default value')
    else:pass
    #####
    if L >= 2:
        #to insert "nm"
        args4mk_default_or_raise = tmay_Nothing___or___args4mk_default_or_raise
        (mirror_imay_xedefault_rank, xedefault, *args4xedefault) = args4mk_default_or_raise
        def nm2default(nm, /):
            default = mk_default__easy(mirror_imay_xedefault_rank, xedefault, nm, *args4xedefault)
            return default
    else:
        tmay_Nothing = tmay_Nothing___or___args4mk_default_or_raise
        def nm2default(nm, /):
            default = mk_default__easy(*tmay_Nothing)
            return default
    del tmay_Nothing___or___args4mk_default_or_raise, L
    nm2default
    return nm2default

def pairs5api__zdefault_(*tmay_Nothing___or___args4mk_default_or_raise):
    nm2default = _mk_nm2default(*tmay_Nothing___or___args4mk_default_or_raise)
    def pairs5api(f, /):
        (_infos4idx_nm_both, may_nm4varargs, may_nm4varkwargs) = get_signature_of__py2_(f)
        if not may_nm4varkwargs is None:raise TypeError('varkwargs occur')
        if not may_nm4varargs is None:raise TypeError('varargs occur')
        pairs = [(nm, eliminate_tmay__mix(tm, 1, nm2default, nm)) for nm, tm in _infos4idx_nm_both]
        return pairs
    return pairs5api
#pairs5api__raise = pairs5api__xdefault_(0, raise4mk_default_or_raise, 0, TypeError, 'miss default value')
pairs5api__raise = pairs5api__zdefault_()
def pairs5api__Nothing_(Nothing, /):
    pairs5api__Nothing = pairs5api__zdefault_(Nothing)
    return pairs5api__Nothing
pairs5api__None = pairs5api__Nothing_(None)

#pairs5api__ = pairs5api__zdefault_
def pairs5api_(may_f, /, *tmay_Nothing___or___args4mk_default_or_raise):
    'may_f -> (pairs5api if may_f is None else pairs)'
    #if not len(tmay_Nothing) < 2: raise TypeError
    pairs5api = pairs5api__zdefault_(*tmay_Nothing___or___args4mk_default_or_raise)

    if may_f is None:
        return pairs5api
    else:
        f = may_f
        pairs = pairs5api(f)
        return pairs

















def triples5api__zdefault_(*tmay_Nothing___or___args4mk_default_or_raise, follow_wrapped=True):
    nm2default = _mk_nm2default(*tmay_Nothing___or___args4mk_default_or_raise)
    def triples5api(f, /):
        (infoss4input, tmay_return_annotation) = get_signature_of__py3_(f, follow_wrapped=follow_wrapped)
        (infos4idx_only, infos4idx_nm_both, tmay_info4varargs, infos4nm_only, tmay_info4varkwds) = infoss4input
        if tmay_info4varkwds:raise TypeError('varkwargs occur')
        if tmay_info4varargs:raise TypeError('varargs occur')
        if infos4nm_only:raise TypeError('KEYWORD_ONLY occur')
        if infos4idx_only:raise TypeError('POSITIONAL_ONLY occur')
        if tmay_return_annotation:raise TypeError('return_annotation occur')
        triples = [(nm, eliminate_tmay__mix(tmay_annotation, 1, nm2default, nm), eliminate_tmay__mix(tmay_default, 1, nm2default, nm)) for nm, tmay_annotation, tmay_default in infos4idx_nm_both]
        return triples
    return triples5api
triples5api__raise = triples5api__zdefault_()
def triples5api__Nothing_(Nothing, /):
    triples5api__Nothing = triples5api__zdefault_(Nothing)
    return triples5api__Nothing
triples5api__None = triples5api__Nothing_(None)

def triples5api_(may_f, /, *tmay_Nothing___or___args4mk_default_or_raise):
    'may_f -> (triples5api if may_f is None else triples)'
    triples5api = triples5api__zdefault_(*tmay_Nothing___or___args4mk_default_or_raise)

    if may_f is None:
        return triples5api
    else:
        f = may_f
        triples = triples5api(f)
        return triples






































































































if not _getargspec__py2 is None:
  def get_signature_of__py2_(f, /):
    '-> (_infos4idx_nm_both/[(nm,tmay_default)], may_nm4varargs, may_nm4varkwargs) #only used for mk_pairs()/pairs5api_()'
    '-> ([nm], [(nm,default)], may_nm4varargs, may_nm4varkwargs)'
    'follow_wrapped=False'
    #ignores __wrapped__ attributes and includes the already bound first parameter in the signature output for bound methods.
    (nms4args, may_nm4varargs, may_nm4varkwargs, may_defaults) = _getargspec__py2(f)
    if may_defaults is None:
        defaults = ()
    else:
        defaults = may_defaults
    i = len(nms4args)-len(defaults)
    ps0 = [(nm, ()) for nm in nms4args[:i]]
    ps1 = [(nm, (v,)) for nm, v in zip(nms4args[i:], defaults)]
    _infos4idx_nm_both = (*ps0, *ps1)
    return (_infos4idx_nm_both, may_nm4varargs, may_nm4varkwargs)
else:
    #using:get_signature_of__py3_
  def get_signature_of__py2_(f, /):
    '-> (_infos4idx_nm_both/[(nm,tmay_default)], may_nm4varargs, may_nm4varkwargs) #only used for mk_pairs()/pairs5api_()'
    (infoss4input, tmay_return_annotation) = get_signature_of__py3_(f, follow_wrapped=False)
    (infos4idx_only, infos4idx_nm_both, tmay_info4varargs, infos4nm_only, tmay_info4varkwds) = infoss4input
    #5+1-3==3
    if 1:
        if infos4nm_only:raise TypeError('KEYWORD_ONLY occur')
        if infos4idx_only:raise TypeError('POSITIONAL_ONLY occur')
        if tmay_return_annotation:raise TypeError('return_annotation occur')
    # info4parameter = (name, tmay_annotation, tmay_default)
    #.parameter_infoss :: (infos4idx_only/[info4parameter], '/', infos4idx_nm_both/[info4parameter], '*', tmay_info4varargs/(tmay info4parameter), infos4nm_only/[info4parameter], '**', tmay_info4varkwds/(tmay info4parameter))
    #5+1-3==3
    (infos4idx_nm_both, tmay_info4varargs, tmay_info4varkwds)
    if any(tmay_annotation for (name, tmay_annotation, tmay_default) in infos4idx_nm_both):raise TypeError('param_annotation occur')
    _infos4idx_nm_both = tuple((name, tmay_default) for (name, tmay_annotation, tmay_default) in infos4idx_nm_both)
    #may_nm4varargs
    for (name, tmay_annotation, tmay_default) in tmay_info4varargs:
        if tmay_annotation:raise TypeError('vararg_annotation occur')
        if tmay_default:raise TypeError('vararg_default occur')
        may_nm4varargs = name
        break
    else:
        may_nm4varargs = None
    may_nm4varargs
    #may_nm4varkwargs
    for (name, tmay_annotation, tmay_default) in tmay_info4varkwargs:
        if tmay_annotation:raise TypeError('varkwarg_annotation occur')
        if tmay_default:raise TypeError('varkwarg_default occur')
        may_nm4varkwargs = name
        break
    else:
        may_nm4varkwargs = None
    may_nm4varkwargs
    return (_infos4idx_nm_both, may_nm4varargs, may_nm4varkwargs)



def _mk_tmay_from_nmay4Signature__py3(nmay_x, /, *, Nothing = _Signature__py3.empty):
    tmay_x = nmay2tmay__Nothing(Nothing, nmay_x)
    return tmay_x
def _mk_tmay_from_nmay4Parameter__py3(nmay_x, /, *, Nothing = _Parameter__py3.empty):
    tmay_x = nmay2tmay__Nothing(Nothing, nmay_x)
    return tmay_x

def extract_info5parameter__py3_(parameter, /):
    '-> (kind, name, nmay_annotation, nmay_default)'
    check_type_is(_Parameter__py3, parameter)
    return (parameter.kind, parameter.name, parameter.annotation, parameter.default)
def get_signature_of__py3_(f, /, follow_wrapped=True):
    r'''-> (infoss4input/(infos4idx_only, infos4idx_nm_both, tmay_info4varargs, infos4nm_only, tmay_info4varkwds), tmay_return_annotation)

    ===
    infos4xxx :: [info4parameter]
    tmay_info4xxx :: tmay info4parameter
    tmay_return_annotation :: tmay py_obj
    ===
    info4parameter = (name, tmay_annotation, tmay_default)
    ===

    '''#'''
    #inspect.signature(callable, *, follow_wrapped=True) -> Signature
    #
    #===maybe:
    #.parameter_infos :: [(kind, name, tmay_annotation, tmay_default)]
    #.tmay_return_annotation :: tmay py_obj
    #   where:  kind <- def _(POSITIONAL_ONLY:0, /, POSITIONAL_OR_KEYWORD:1, *VAR_POSITIONAL:2, KEYWORD_ONLY:3, **VAR_KEYWORD:4)
    #
    #===maybe:
    # info4parameter = (name, tmay_annotation, tmay_default)
    #.parameter_infoss :: (infos4idx_only/[info4parameter], '/', infos4idx_nm_both/[info4parameter], '*', tmay_info4varargs/(tmay info4parameter), infos4nm_only/[info4parameter], '**', tmay_info4varkwds/(tmay info4parameter))
    #.tmay_return_annotation :: tmay py_obj
    #
    sig = _get_signature_of__py3(f, follow_wrapped=follow_wrapped)
    tmay_return_annotation = _mk_tmay_from_nmay4Signature__py3(sig.return_annotation)
    infoss4input = [[] for _ in range(5)]
    #for parameter in sig.parameters:
    for parameter in sig.parameters.values():
        (kind, name, nmay_annotation, nmay_default) = extract_info5parameter__py3_(parameter)
        tmay_annotation = _mk_tmay_from_nmay4Parameter__py3(nmay_annotation)
        tmay_default = _mk_tmay_from_nmay4Parameter__py3(nmay_default)
        info4parameter = (name, tmay_annotation, tmay_default)
        infos = infoss4input[kind]
        infos.append(info4parameter)
    infoss4input = (*map(tuple, infoss4input),)
    return (infoss4input, tmay_return_annotation)
#end-def get_signature_of__py3_(f, /, follow_wrapped=True):




from seed.for_libs.for_inspect import check_num_args_ok_, is_num_args_ok_
from seed.for_libs.for_inspect import get_signature_of__py3_
from seed.for_libs.for_inspect import pairs5api_, pairs5api__zdefault_
from seed.for_libs.for_inspect import pairs5api__raise, pairs5api__Nothing_, pairs5api__None
from seed.for_libs.for_inspect import triples5api_, triples5api__zdefault_
from seed.for_libs.for_inspect import triples5api__raise, triples5api__Nothing_, triples5api__None
from seed.for_libs.for_inspect import *
