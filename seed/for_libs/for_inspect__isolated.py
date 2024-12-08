#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_inspect__isolated.py
moved from:
    view ../../python3_src/seed/for_libs/for_inspect.py
    <<==:
since:
    view ../../python3_src/seed/for_libs/for_inspect.py
        triples5api__zdefault_/pairs5api__zdefault_/_mk_nm2default depends on mk_fdefault
    view ../../python3_src/seed/tiny_/mk_fdefault.py
        ++check4mk_default__len_() which depends on check_num_args_ok_()



seed.for_libs.for_inspect__isolated
py -m nn_ns.app.debug_cmd   seed.for_libs.for_inspect__isolated -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_inspect__isolated:__doc__ -ht # -ff -df
py_adhoc_call   seed.for_libs.for_inspect__isolated   @f
]]]'''#'''
__all__ = r'''
check_num_args_ok_
    is_num_args_ok_





_get_signature_of__py3
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.debug.expectError import expectError
from seed.debug.print_err import print_err
#from inspect import signature as _get_signature_of__py3 #py2/py3 api diff, py3/py4 may be diff too.

___end_mark_of_excluded_global_names__0___ = ...

from inspect import signature as _get_signature_of__py3 #py2/py3 api diff, py3/py4 may be diff too.
    #inspect.signature(callable, *, follow_wrapped=True) -> Signature
    #.__wrapped__=f
    #_test4follow_wrapped():goto
try:
    _get_signature_of__py3(TypeError)
except ValueError:
    #@py3_11_9:ValueError: no signature found for builtin type <class 'TypeError'>
    _ty2f = (
    {#bool:lambda x=False, /:x
    })
    _0_get_signature_of__py3 = _get_signature_of__py3
    import re
    _rex = re.compile(r"no signature found for builtin (?:type )?<class '\w+(?:\.\w+)*'>")
    def _get_signature_of__py3(f, /, *args, **kwds):
        try:
            return _0_get_signature_of__py3(f, *args, **kwds)
        except ValueError as e:
            #if 0b0001:print_err(str(e))
                # no signature found for builtin type <class 'TypeError'>
                # no signature found for builtin type <class 'bool'>
            # (s := str(e))
            if isinstance(f, type):
                #if issubclass(f, Exception) or (len(e.args) == 1 and (s := e.args[0]) and type(s) is str and s.endswith(r"'>") and s.startswith(r"no signature found for builtin <class '")):
                if f in _ty2f:
                    f = _ty2f[f]
                    return _0_get_signature_of__py3(f, *args, **kwds)
                if issubclass(f, Exception) or (len(e.args) == 1 and (s := e.args[0]) and type(s) is str and _rex.fullmatch(s)):
                    return _0_get_signature_of__py3(f.__new__, *args, **kwds)
                    return _0_get_signature_of__py3(f.__init__, *args, **kwds)
            raise
_get_signature_of__py3(TypeError)


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
if 0:
    assert expectError(ValueError, lambda:is_num_args_ok_(1, bool))
    assert expectError(ValueError, lambda:check_num_args_ok_(1, bool))
else:
    assert is_num_args_ok_(1, bool)
    assert is_num_args_ok_(0, bool)
assert is_num_args_ok_(1, bool, ok_if_no_signature=True)
assert not is_num_args_ok_(1, 0)
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




__all__
from seed.for_libs.for_inspect__isolated import check_num_args_ok_, is_num_args_ok_
from seed.for_libs.for_inspect__isolated import _get_signature_of__py3
from seed.for_libs.for_inspect__isolated import *
