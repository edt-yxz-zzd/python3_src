#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/with_many.py


seed.helper.with_many
py -m nn_ns.app.debug_cmd   seed.helper.with_many -x
py -m nn_ns.app.doctest_cmd seed.helper.with_many:__doc__ -ff -v
python -m unittest seed.helper.with_many

from seed.helper.with_many import with_many


object.__exit__(sf, exc_type, exc_value, traceback)

py_help :Exception
 ... ...
 |  with_traceback(...)
 |      Exception.with_traceback(tb) --
 |      set sf.__traceback__ to tb and return sf.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |
 |  __cause__
 |      exception cause
 |
 |  __context__
 |      exception context
 |
 |  __dict__
 |
 |  __suppress_context__
 |
 |  __traceback__
 |
 |  args

$ py_help contextlib:ExitStack
Help on class ExitStack in module contextlib:

class ExitStack(_BaseExitStack, AbstractContextManager)
 |  Context manager for dynamic management of a stack of exit callbacks.
 |
 |  For example:
 |      with ExitStack() as stack:
 |          files = [stack.enter_context(open(fname)) for fname in filenames]
 |          # All opened files will automatically be closed at the end of
 |          # the with statement, even if attempts to open files later
 |          # in the list raise an exception.
 |

cp ~/../usr/lib/python3.10/contextlib.py /sdcard/0my_files/tmp/out4py/py_src/
view /sdcard/0my_files/tmp/out4py/py_src/contextlib.py
with_many__using_contextmanager__using_ExitStack


>>> from seed.helper.with_many import with_many
>>> from seed.helper.with_many import with_many__using_contextmanager__using_ExitStack
>>> from seed.helper.with_many import with_many__using_contextmanager

>>> xs = []
>>> @contextlib.contextmanager
... def stop_raise(ErrT, x, /):
...     print(f'stop_raise enter: {x}')
...     xs.append(x)
...     try:
...         yield x
...     except ErrT:pass
...     finally:
...         print(f'stop_raise exit: {x}')
...         xs.append(-x)
>>> @contextlib.contextmanager
... def ok(x, /):
...     print(f'ok enter: {x}')
...     xs.append(x)
...     try:
...         yield x
...     finally:
...         print(f'ok exit: {x}')
...         xs.append(-x)
>>> @contextlib.contextmanager
... def bad(x, /):
...     print(f'bad enter: {x}')
...     xs.append(x)
...     raise BaseException(f'bad({x})')
...     yield x
...     print(f'bad exit: {x}')
...     xs.append(-x)


>>> xs = []
>>> with stop_raise(Exception, 333), bad(111):pass
Traceback (most recent call last):
    ...
BaseException: bad(111)
>>> xs
[333, 111, -333]
>>> xs = []
>>> with stop_raise(Exception, 333):
...     with bad(111):pass
Traceback (most recent call last):
    ...
BaseException: bad(111)
>>> xs
[333, 111, -333]
>>> xs = []
>>> with stop_raise(BaseException, 333), bad(111):pass
stop_raise enter: 333
bad enter: 111
stop_raise exit: 333
>>> xs
[333, 111, -333]
>>> xs = []
>>> with stop_raise(BaseException, 333):
...     with bad(111):pass
stop_raise enter: 333
bad enter: 111
stop_raise exit: 333
>>> xs
[333, 111, -333]



>>> print('with_many__using_contextmanager')
with_many__using_contextmanager
>>> xs = []
>>> with with_many__using_contextmanager() as ls:
...     ls
()
>>> xs
[]
>>> xs = []
>>> with with_many__using_contextmanager([ok, 999]) as ls:
...     ls
ok enter: 999
(999,)
ok exit: 999
>>> xs
[999, -999]
>>> xs = []
>>> with with_many__using_contextmanager([ok, 999, ok, 777]) as ls:
...     ls
Traceback (most recent call last):
    ...
TypeError: ok() takes 1 positional argument but 3 were given
>>> xs
[]
>>> xs = []
>>> with with_many__using_contextmanager([ok, 999], [ok]) as ls:
...     ls
Traceback (most recent call last):
    ...
TypeError: ok() missing 1 required positional argument: 'x'
>>> xs
[999, -999]
>>> xs = []
>>> with with_many__using_contextmanager([ok, 999], [ok, 777]) as ls:
...     ls
ok enter: 999
ok enter: 777
(999, 777)
ok exit: 777
ok exit: 999
>>> xs
[999, 777, -777, -999]
>>> xs = []
>>> with with_many__using_contextmanager([ok, 999], [ok, 777], [bad, 555]) as ls:
...     ls
Traceback (most recent call last):
    ...
BaseException: bad(555)
>>> xs
[999, 777, 555, -777, -999]
>>> xs = []
>>> with with_many__using_contextmanager([stop_raise, BaseException, 999], [ok, 777], [bad, 555]) as ls:
...     ls is None #???
stop_raise enter: 999
ok enter: 777
bad enter: 555
ok exit: 777
stop_raise exit: 999
True
>>> xs
[999, 777, 555, -777, -999]







>>> print('with_many__using_contextmanager__using_ExitStack')
with_many__using_contextmanager__using_ExitStack
>>> xs = []
>>> with with_many__using_contextmanager__using_ExitStack() as ls:
...     ls
()
>>> xs
[]
>>> xs = []
>>> with with_many__using_contextmanager__using_ExitStack([ok, 999]) as ls:
...     ls
ok enter: 999
(999,)
ok exit: 999
>>> xs
[999, -999]
>>> xs = []
>>> with with_many__using_contextmanager__using_ExitStack([ok, 999, ok, 777]) as ls:
...     ls
Traceback (most recent call last):
    ...
TypeError: ok() takes 1 positional argument but 3 were given
>>> xs
[]
>>> xs = []
>>> with with_many__using_contextmanager__using_ExitStack([ok, 999], [ok]) as ls:
...     ls
Traceback (most recent call last):
    ...
TypeError: ok() missing 1 required positional argument: 'x'
>>> xs
[999, -999]
>>> xs = []
>>> with with_many__using_contextmanager__using_ExitStack([ok, 999], [ok, 777]) as ls:
...     ls
ok enter: 999
ok enter: 777
(999, 777)
ok exit: 777
ok exit: 999
>>> xs
[999, 777, -777, -999]
>>> xs = []
>>> with with_many__using_contextmanager__using_ExitStack([ok, 999], [ok, 777], [bad, 555]) as ls:
...     ls
Traceback (most recent call last):
    ...
BaseException: bad(555)
>>> xs
[999, 777, 555, -777, -999]

>>> xs
[999, 777, 555, -777, -999]
>>> xs = []
>>> with with_many__using_contextmanager__using_ExitStack([stop_raise, BaseException, 999], [ok, 777], [bad, 555]) as ls:
...     ls is None #???
stop_raise enter: 999
ok enter: 777
bad enter: 555
ok exit: 777
stop_raise exit: 999
True
>>> xs
[999, 777, 555, -777, -999]

#vs
>>> xs = []
>>> with _buggy___with_many__using_contextmanager__using_ExitStack([stop_raise, BaseException, 999], [ok, 777], [bad, 555]) as ls:
...     ls #bug!!
Traceback (most recent call last):
    ...
RuntimeError: generator didn't yield

# '



>>> print('hard code')
hard code
>>> xs = []
>>> with ok(999) as u0:
...     (u0,)
ok enter: 999
(999,)
ok exit: 999
>>> xs
[999, -999]
>>> xs = []
>>> with ok(999) as u0, ok() as u1:
...     (u0, u1)
Traceback (most recent call last):
    ...
TypeError: ok() missing 1 required positional argument: 'x'
>>> xs
[999, -999]
>>> xs = []
>>> with ok(999) as u0, ok(777) as u1:
...     (u0, u1)
ok enter: 999
ok enter: 777
(999, 777)
ok exit: 777
ok exit: 999
>>> xs
[999, 777, -777, -999]
>>> xs = []
>>> with ok(999) as u0, ok(777) as u1, bad(555) as u2:
...     (u0, u1, u2)
Traceback (most recent call last):
    ...
BaseException: bad(555)
>>> xs
[999, 777, 555, -777, -999]
>>> xs = []
>>> with stop_raise(BaseException, 999) as u0, ok(777) as u1, bad(555) as u2:
...     (u0, u1, u2)
stop_raise enter: 999
ok enter: 777
bad enter: 555
ok exit: 777
stop_raise exit: 999
>>> xs
[999, 777, 555, -777, -999]



#]]]'''
__all__ = r'''
    with_many__using_contextmanager


save_exc_cxt_
restore_exc_cxt_
reraise_with_cxt_
reraise_with_old_cxt_
exc_details4exit__5may_exc

with_many__using_contextmanager__using_ExitStack

Test____with_many__using_contextmanager
Test____with_many__using_contextmanager__using_ExitStack
'''.split()#'''
__all__

import contextlib
#from operator import __enter__, __exit__
from seed.tiny import fst, check_callable
from seed.tiny import nmay5tmay_, nmay2tmay_

@contextlib.contextmanager
#def buggy___with_many__using_contextmanager__using_ExitStack(*f_args_ls):
#    'bug ??<<=[why]=?? using contextmanager && using ExitStack && raise before yield'
#   no bug!!!
#   bug at testing code: def ok()
#       forgot catch 『yield x』
def _buggy___with_many__using_contextmanager__using_ExitStack(*f_args_ls):
    f_args_ls = tuple((f, args)  for f, *args in f_args_ls)
    if not all(map(callable, map(fst, f_args_ls))): raise TypeError
    with contextlib.ExitStack() as stack:
        ls = tuple(stack.enter_context(f(*args)) for f, args in f_args_ls)
        yield ls
    #bug: [[f0(...) stop_raise][f1(...) raise]] ==>> [[skip 『yield ls』][RuntimeError: generator didn't yield]]

@contextlib.contextmanager
def with_many__using_contextmanager__using_ExitStack(*f_args_ls):
    f_args_ls = tuple((f, args)  for f, *args in f_args_ls)
    if not all(map(callable, map(fst, f_args_ls))): raise TypeError
    with contextlib.ExitStack() as stack:
        ls = tuple(stack.enter_context(f(*args)) for f, args in f_args_ls)
        yield ls
        return
    #bug: [[f0(...) stop_raise][f1(...) raise]] ==>> [[skip 『yield ls』][RuntimeError: generator didn't yield]]
    yield None





_nms4save_exc_cxt = r'''
__cause__
__context__
__suppress_context__
__traceback__
'''.split()#'''
def save_exc_cxt_(exc, /):
    cxt = {nm:getattr(exc, nm) for nm in _nms4save_exc_cxt}
    exc_cxt = (exc, cxt)
    return exc_cxt
def restore_exc_cxt_(exc_cxt, exc, /):
    (exc_, cxt) = exc_cxt
    if not exc is exc_: raise ValueError
    for nm, v in cxt.items():
        setattr(exc, nm, v)
def reraise_with_cxt_(exc_cxt, exc, /):
    try:
        raise exc
            # set new cxt
    except BaseException:
        restore_exc_cxt_(exc_cxt, exc)
            # set old cxt
        raise
def reraise_with_old_cxt_(exc, /):
    exc_cxt = save_exc_cxt_(exc)
    reraise_with_cxt_(exc_cxt, exc)
    raise 000


def _ty_call_(nm, sf, *args):
    cls = type(sf)
    f = getattr(cls, nm)
    return f(sf, *args)

def __enter__(sf, /):
    '-> target'
    target = _ty_call_('__enter__', sf)
    return target
def __exit__(sf, exc_type, exc_value, traceback, /):
    '-> b_stop_reraise/bool'
    b_stop_reraise = _ty_call_('__exit__', sf, exc_type, exc_value, traceback)
    return bool(b_stop_reraise)
def __exit__tmay__(sf, /, *tmay_exc):
    may_exc = nmay5tmay_(tmay_exc)
    (exc_type, exc_value, traceback) = exc_details4exit__5may_exc(may_exc)
    b_stop_reraise = __exit__(sf, exc_type, exc_value, traceback)
    return b_stop_reraise
def exc_details4exit__5may_exc(may_exc, /):
    if may_exc is None:
        return None, None, None
    e = may_exc
    ty = type(e)
    tb = e.__traceback__
    return (ty, e, tb)
class _X:
    def __init__(sf, /, *f_args_ls, ErrT):
        if ErrT is None:
            ErrT = BaseException
        if not issubclass(ErrT, BaseException):raise TypeError(ErrT)

        f_args_ls = tuple((f, args)  for f, *args in f_args_ls)
        if not all(map(callable, map(fst, f_args_ls))): raise TypeError
        sf.args = ErrT, f_args_ls

    def init(sf, zs, /):
        ErrT, f_args_ls = sf.args
        #######
        assert not zs
        xs = []
        if 1:
            for f, args in f_args_ls:
                z = f(*args)
                x = __enter__(z)
                zs.append(z)
                xs.append(x)
            xs = (*xs,)
        return xs
    def clean(sf, zs, tmay_e, /):
        ErrT, f_args_ls = sf.args
        b_stop_reraise = _on_exit(ErrT, zs, tmay_e)
        return b_stop_reraise
    def do(sf, /):
        raise NotImplementedError


def _on_exit(ErrT, zs, tmay_e, /):
    old = tmay_e
    for z in reversed(zs):
        try:
            b_stop_reraise = __exit__tmay__(z, *tmay_e)
        except ErrT as e:
            tmay_e = (e,)
        else:
            if b_stop_reraise:
                tmay_e = ()
    new = tmay_e
    b_stop_reraise = not new
    if b_stop_reraise:
        return b_stop_reraise#True
    #should raise
    if new is old:
        #reraise
        return b_stop_reraise#False
    #raise new
    [e] = new
    reraise_with_old_cxt_(e)
    raise 000


class _X_with_many__using_contextmanager(_X):
    @contextlib.contextmanager
    def do(sf, /):
        ErrT, f_args_ls = sf.args
        #
        zs = []
        tmay_e = ()
        try:
            xs = sf.init(zs)
            yield xs
        except ErrT as e:
            tmay_e = (e,)
            b_stop_reraise = sf.clean(zs, tmay_e)
            if b_stop_reraise:
                yield None
            else:
                raise
            assert b_stop_reraise
        else:
            b_stop_reraise = sf.clean(zs, tmay_e)
            assert b_stop_reraise
        #finally:
        #    return _on_exit(ErrT, zs, tmay_e)


def with_many__using_contextmanager(*f_args_ls, ErrT=None):
    sf = _X_with_many__using_contextmanager(*f_args_ls, ErrT=ErrT)
    return sf.do()




import unittest
#from contextlib import redirect_stdout

class _Mixin4Test____with_many:#(unittest.TestCase):
    @property
    def _with_many_(sf, /):
        raise NotImplementedError

    @contextlib.contextmanager
    def _stop(sf, ErrT, u, /):
        sf.xs.append(u)
        try:
            yield u
        except ErrT:
            pass
        finally:
            sf.xs.append(-u)

    @contextlib.contextmanager
    def _trans(sf, ErrT_out, ErrT_in, u, /):
        sf.xs.append(u)
        try:
            yield u
        except ErrT_in as e:
            raise ErrT_out('trans', u, type(e), e.args)
        finally:
            sf.xs.append(-u)

    @contextlib.contextmanager
    def _ok(sf, u, /):
        sf.xs.append(u)
        try:
            yield u
        finally:
            sf.xs.append(-u)

    @contextlib.contextmanager
    def _bad(sf, u, /):
        sf.xs.append(u)
        raise BaseException('bad', u)
        try:
            yield u
        finally:
            sf.xs.append(-u)

    def setUp(sf, /):
        sf.xs = []
    def tearDown(sf, /):
        pass

    def test_sz0(sf, /):
        with sf._with_many_() as ls:
            pass
        sf.assertEqual(ls, ())
        sf.assertEqual(sf.xs, [])
    def test_sz1(sf, /):
        with sf._with_many_([sf._ok, 999]) as ls:
            pass
        sf.assertEqual(ls, (999,))
        sf.assertEqual(sf.xs, [999, -999])
    def test_sz2(sf, /):
        with sf._with_many_([sf._ok, 999], [sf._ok, 777]) as ls:
            pass
        sf.assertEqual(ls, (999, 777))
        sf.assertEqual(sf.xs, [999, 777, -777, -999])

    def test_sz2__raise(sf, /):
        with sf.assertRaises(TypeError) as cm:
            with sf._with_many_([sf._ok, 999], [sf._ok]) as ls:
                pass
        e = cm.exception
        sf.assertEqual(e.args, ("_Mixin4Test____with_many._ok() missing 1 required positional argument: 'u'",))
        sf.assertEqual(sf.xs, [999, -999])

    def test_sz3__raise(sf, /):
        with sf.assertRaises(BaseException) as cm:
            with sf._with_many_([sf._ok, 999], [sf._ok, 777], [sf._bad, 555]) as ls:
                pass
        e = cm.exception
        sf.assertIs(type(e), BaseException)
        sf.assertEqual(e.args, ('bad', 555))
        sf.assertEqual(sf.xs, [999, 777, 555, -777, -999])



    def test_sz3__stop_raise(sf, /):
        with sf._with_many_([sf._stop, BaseException, 999], [sf._ok, 777], [sf._bad, 555]) as ls:
            pass
        sf.assertIsNone(ls)

    def test_sz3__stop_raise_but_miss(sf, /):
        with sf.assertRaises(BaseException) as cm:
            with sf._with_many_([sf._stop, Exception, 999], [sf._ok, 777], [sf._bad, 555]) as ls:
                pass
        e = cm.exception
        sf.assertIs(type(e), BaseException)
        sf.assertEqual(e.args, ('bad', 555))
        sf.assertEqual(sf.xs, [999, 777, 555, -777, -999])

    def test_sz3__stop_traned_raise(sf, /):
        with sf._with_many_([sf._stop, Exception, 999], [sf._trans, Exception, BaseException, 777], [sf._bad, 555]) as ls:
            pass
        sf.assertIsNone(ls)

    def test_sz3__traned_missstop_raise(sf, /):
        with sf.assertRaises(BaseException) as cm:
            with sf._with_many_([sf._trans, Exception, BaseException, 999], [sf._stop, Exception, 777], [sf._bad, 555]) as ls:
                pass
        e = cm.exception
        sf.assertIs(type(e), Exception)
        sf.assertEqual(e.args, ('trans', 999, BaseException, ('bad', 555)))
        sf.assertEqual(sf.xs, [999, 777, 555, -777, -999])




#class Test____with_many(_Mixin4Test____with_many, unittest.TestCase):
class Test____with_many__using_contextmanager(_Mixin4Test____with_many, unittest.TestCase):
    @property
    def _with_many_(sf, /):
        return with_many__using_contextmanager
class Test____with_many__using_contextmanager__using_ExitStack(_Mixin4Test____with_many, unittest.TestCase):
    @property
    def _with_many_(sf, /):
        return with_many__using_contextmanager__using_ExitStack




with_many = with_many__using_contextmanager
with_many = with_many__using_contextmanager__using_ExitStack

from seed.helper.with_many import with_many


from seed.helper.with_many import with_many__using_contextmanager__using_ExitStack
from seed.helper.with_many import with_many__using_contextmanager
from seed.helper.with_many import *
