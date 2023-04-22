#__all__:goto
r'''[[[
e ../../python3_src/seed/func_tools/detect_depth4fail.py

[[
used in: py_adhoc_call
    view ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py
    ==>>
    to mimic:『py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd』
        view ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py
        i.e. show py_help when args mismatch func.signature

===>>:
py_adhoc_call builtins @hex
Traceback (most recent call last):
    ...
TypeError: hex() takes exactly one argument (0 given)
Help on built-in function hex in module builtins:

hex(number, /)
    Return the hexadecimal representation of an integer.

    >>> hex(12648430)
    '0xc0ffee'

]]



seed.func_tools.detect_depth4fail
py -m nn_ns.app.debug_cmd   seed.func_tools.detect_depth4fail -x
py -m nn_ns.app.doctest_cmd seed.func_tools.detect_depth4fail:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.func_tools.detect_depth4fail!
py_adhoc_call   seed.func_tools.detect_depth4fail   @f


[[

>>> from seed.func_tools.detect_depth4fail import detect_depth4fail__exc_, detect_depth4fail__call_, decorator4show_py_help

>>> @decorator4show_py_help
... def h(a,/): return 444
>>> h(1)
444
>>> h()
Traceback (most recent call last):
    ...
TypeError: h() missing 1 required positional argument: 'a'
Help on function h in module seed.func_tools.detect_depth4fail:
<BLANKLINE>
h(a, /)
<BLANKLINE>
<BLANKLINE>
>>> def h(a,/): return 444
>>> @decorator4show_py_help
... def h2(): return h()
>>> h2()
Traceback (most recent call last):
    ...
TypeError: h() missing 1 required positional argument: 'a'


]]



[[
TypeError: f() missing 1 required positional argument: 'a'

try:
    def f(a,/):0
    def g():f()
    g()
except TypeError as e:
    for nm in dir(e):print(nm)
    print(e.__cause__)
    print(e.__context__)
    print(e.__suppress_context__)
    print(e.__traceback__)
    for nm in dir(e.__traceback__):print(nm)
    print(e.__traceback__.tb_frame)
    print(e.__traceback__.tb_lasti)
    print(e.__traceback__.tb_lineno)
    print(e.__traceback__.tb_next)
    print(e.__traceback__.tb_next.tb_next)
    assert None is (e.__traceback__.tb_next.tb_next)

__cause__
__context__
__suppress_context__
__traceback__
args
with_traceback

tb_frame
tb_lasti
tb_lineno
tb_next


]]





#]]]'''
__all__ = r'''
    detect_depth4fail__exc_
    detect_depth4fail__call_
    decorator4show_py_help
'''.split()#'''
__all__

from seed.for_libs.for_builtins.py_help import py_help_, py_help
from seed.tiny import check_type_le, check_uint, print_err, ifNone
from functools import wraps

def detect_depth4fail__exc_(may_max_depth, exc, /):
    'may max_depth/uint -> exc/BaseException -> imay depth/uint # 0 => [not be raised yet] # -1 => [depth > max_depth]'
    check_type_le(BaseException, exc)
    if not may_max_depth is None:
        max_depth = may_max_depth
        check_uint(max_depth)

    if may_max_depth is None:
        def is_good(depth, /):
            return True
    else:
        max_depth
        def is_good(depth, /):
            return depth <= max_depth

    depth = 0
    tb = exc.__traceback__
    while is_good(depth) and not tb is None:
        depth += 1
        tb = tb.tb_next
    imay_depth = depth if is_good(depth) else -1
    return imay_depth

def detect_depth4fail__call_(to_reraise_, may_max_depth, may_ErrorT, f, /, *args, **kwds):
    'to_reraise_/(exc->imay_depth->bool) -> may max_depth -> may E -> f -> *args -> **kwds -> (is_ok, ((exc,imay_depth)|result))'
    ErrorT = ifNone(may_ErrorT, Exception)
    try:
        r = f(*args, **kwds)
    #except BaseException as exc:
    #except Exception as exc:
    except ErrorT as exc:
        imay_depth = detect_depth4fail__exc_(may_max_depth, exc)
        if to_reraise_(exc, imay_depth):
            raise
        is_ok = False
        return is_ok, (exc, imay_depth)
    is_ok = True

    return is_ok, r

__max_depth = 1
def decorator4show_py_help(f, /):
    def to_reraise_(exc, imay_depth, /):
        if imay_depth == __max_depth:
            help4f = py_help_(f)
            [err_msg] = exc.args
            err_msg = f'{err_msg}\n{help4f}'
            if 0b0:print_err(err_msg)
            raise TypeError(err_msg) from exc
        #raise
        return True
    @wraps(f)
    def g(*args, **kwds):
        (is_ok, x) = detect_depth4fail__call_(to_reraise_, __max_depth, TypeError, f, *args, **kwds)
        if is_ok:
            result = x
            return result
        raise logic-err
    return g


from seed.func_tools.detect_depth4fail import detect_depth4fail__exc_, detect_depth4fail__call_, decorator4show_py_help
from seed.func_tools.detect_depth4fail import *
