
from .helper.str2__all__ import str2__all__
__all__ = str2__all__('''
    no_op               # :: (*args, **kwargs) -> None
    echo_args_kwargs    # :: (*args, **kwargs) -> (args, kwargs)
    echo_args           # :: *args -> args
    echo_kwargs         # :: (**kwargs) -> kwargs
    echo                # :: a -> a
    theEcho             # .__getattribute__ :: str -> str
    ifNone              # :: (None|a) -> default -> (a|default)
    ifNonef             # :: (None|a) -> (()->default) -> (a|default)
    expectError         # :: Error -> (()->...) -> bool
    assert_eq           # :: lhs -> rhs -> (_fmt=...) -> **vars -> ()
    null_iter           # :: iter([])
    null_tuple          # == ()

    fst                 # :: (a, ...) -> a
    snd                 # :: (a, b, ...) -> b
    at                  # at[k](m) := m[k]
    const               # :: a -> b -> a
    eq                  # :: a -> (a -> bool)
    lazy                # :: a -> (() -> a)
    lazy_raise          # get_fdefault(d, key, lazy_raise(KeyError, ...))
    str2__all__         # :: str -> [word]

    print_err           # file=sys.stderr; see: no_op/print_ferr
    print_ferr          # file=sys.stderr; see: no_op/print_err
    fprint              # force/require 'file='
    __not__             # :: Testable a => a -> bool
    not_dot             # :: (a->bool) -> (a->bool)
    xor, nxor           # :: bool -> bool -> bool
    with_if

    with_key            # :: (a->k) -> Iter a -> Iter (k, a)

    py_cmp              # :: Ord a => a -> a -> -> (-1|0|+1)
    int2cmp             # :: int -> (-1|0|+1)

    does_run_as_main    # :: String -> Bool
                        # does_run_as_main(__name__)
                        # does_run_as_main.alter_main_name :: String

    MapView             # mapping -> MappingProxyType
    kwargs2Attrs        # (**kwargs) -> SimpleNamespace
    is_iterable         # a -> Bool
    is_iterator         # a -> Bool
    is_reiterable       # a -> Bool
    ''')

from .helper.ifNone import ifNone, ifNonef
from .helper.Echo import echo, theEcho
from .helper.with_if import with_if
from .debug.expectError import expectError
from .debug.print_err import print_err, print_ferr
from .debug.assert_eq import assert_eq
from .debug.lazy_raise import lazy_raise
from .func_tools.not_dot import __not__, not_dot
from types import MappingProxyType as MapView, SimpleNamespace as kwargs2Attrs
  #SimpleNamespace(**kw)
from collections.abc import Iterable, Iterator


class _At:
    def __new__(cls):
        try:
            return at
        except NameError:
            return super().__new__(cls)
    def __getitem__(sf, k):
        return At(k)
    def __call__(sf, k):
        return At(k)
    def __repr__(sf):
        return f'at'
class At:
    def __init__(sf, i):
        sf.__i = i
    def __call__(sf, x):
        return x[sf.__i]
    def __repr__(sf):
        return f'At({sf.__i!r})'
at = _At()
assert at is _At()
assert at[1]('ab') == 'b'
assert at(1)('ab') == 'b'
assert {at}
assert {at[0]}



no_op = lambda *args, **kwargs:None
echo_args_kwargs = lambda *args, **kwargs:(args, kwargs)
echo_kwargs = lambda **kwargs:kwargs
echo_args = lambda *args: args
echo = lambda x:x
null_iter = iter(())
null_tuple = ()
def fst(seq): return seq[0]
def snd(seq): return seq[1]
def const(a): return lambda _:a
def lazy(a): return lambda:a
def eq(a): return lambda b: a==b


def xor(a, b):
    return bool(a) != bool(b)
def nxor(a, b):
    return bool(a) == bool(b)

def with_key(key, iterable):
    ''':: (a->k) -> Iter a -> Iter (k, a)'''
    # key at first as dict(...)
    for x in iterable:
        yield key(x), x


def fprint(*args, file, **kw):
    print(*args, file=file, **kw)

def py_cmp(a, b):
    # Ord a => a -> a -> -> (-1|0|+1)
    if a == b: return 0
    return -1 if a < b else +1

def int2cmp(i):
    # int -> (-1|0|+1)
    if not i:
        return 0
    return -1 if i < 0 else +1

def is_iterable(x):
    if not isinstance(x, Iterable): return False
    return iter(x) is not None
def is_iterator(x):
    if not isinstance(x, Iterator): return False
    return iter(x) is x
def is_reiterable(x):
    return is_iterable(x) and not is_iterator(x)

def does_run_as_main(__name__):
    '''to replace '__name__ == "__main__"'

usage:
    if __name__ == '__main__':
        ...
    # now become:
    if does_run_as_main(__name__):
        ...
why?
    # is this valid?: runpy.run_path(py_fname, run_name = '__main__')
    runpy.run_path(py_fname, run_name = '<runpy>.__run_as_main__')

why '.__run_as_main__' instead of '.__main__'
    since '__main__.py' exists
    and we assume __run_as_main__ does not exist
'''
    #return (__name__ in ('__main__', '__run_as_main__')
    return (__name__ == '__main__'
            or (__name__.endswith('.__run_as_main__')
                and '<' in __name__
                and '>' in __name__
                )
            )
does_run_as_main.alter_main_name = '__run_as_main__'





r'''see: seed.ECHO

ECHO = theEcho
def __register(qname, pseudo_module):
    import sys
    m = sys.modules.setdefault(qname, pseudo_module)
    if m is not pseudo_module:
        raise ImportError('qname: {qname!r} already exists')

def __register_ECHO():
    qname_ECHO = '.'.join([__name__, 'ECHO'])
    __register(qname_ECHO, theEcho)

    #from seed.tiny.theEcho import x, y, z # ERROR
    from seed.tiny.ECHO import x, y, z
    assert x == 'x'

    E = __import__(qname_ECHO, fromlist='xyz')
    assert E.x == 'x'
    assert E is ECHO
__register_ECHO()
del __register_ECHO, __register

    # seed.tiny.ECHO is a virtual module
    # from seed.tiny.ECHO import x,y,z
#'''
