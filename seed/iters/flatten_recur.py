
r"""
see also:
    seed.iters.flatten_recur
        view ../../python3_src/seed/iters/flatten_recur.py
    seed.func_tools.recur5yield
        view ../../python3_src/seed/func_tools/recur5yield.py
see also:
    view ../../python3_src/seed/iters/generator_iterator_mock_asif_at_initial_state.py

######################
flatten_recur

to avoid stack-overflow when calling recur func

from seed.iters.flatten_recur import flatten_recur

seed.iters.flatten_recur
py -m nn_ns.app.debug_cmd   seed.iters.flatten_recur -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.flatten_recur:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.iters.flatten_recur:_test_exc -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.iters.flatten_recur:_test_boxed_tail_gi -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.iters.flatten_recur:_test_pack_gi_with_xval -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.iters.flatten_recur:_old_test -ht # -ff -df


######################
==========================
collections.abc.Generator
6.2.9.1. Generator-iterator methods

==========================
must start with g.send(None)
next(g) <==> g.send(None)
return_value is StopIteration.value



"""#"""



######################


__all__ = r"""
    flatten_recur
    """.split()#"""

from collections.abc import Generator

def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
    '[flatten_recur :: recur_GI -> final_result][recur_GI == GI{yield{recur_GI}; return{final_result if not boxed else (Either recur_GI final_result)}}]'
    assert isinstance(g, Generator)
    #assert iter(g) is g
    ls = [g]
    while ls:
        g = ls[-1]
        try:
            next_ = g.throw if is_exc else g.send
        except AttributeError as e:
            if is_exc or not value is None:
                raise
            # expecting send None
            # asif starting
            # allow starting with specified value
            match g:
                case (gi, (is_val, xval)):
                    if not hasattr(gi, 'send'):
                        raise
                case _:
                    raise
            #view ../../python3_src/seed/iters/generator_iterator_mock_asif_at_initial_state.py
            g = ls[-1] = gi
            is_exc = not is_val
            value = xval
            continue
        try:
            child_g = next_(value)
        except StopIteration as e:
            #print(e)
            #raise
            value = e.value #return_value
            777;is_exc = False
            ls.pop()
            if boxed:
                # (is_val, gi|v)
                # Either gi v
                match value:
                    case (True, value):
                        #assert not is_exc
                        #777;is_exc = False
                        pass
                    case (False, tail_gi):
                        #assert isinstance(tail_gi, Generator)
                        ls.append(tail_gi)
                        value = None
                        #777;is_exc = False
                    case _:
                        raise TypeError(('not Either', value))
        except BaseException as e:
            value = e
            777;is_exc = True
            ls.pop()
        else:
            #assert isinstance(child_g, Generator)
            ls.append(child_g)
            value = None
            777;is_exc = False
    if is_exc:
        raise value
    return value


_test_pack_gi_with_xval = r'''
>>> def h(n, /):
...     n1 = (n, 111)
...     n19 = yield n1
...     n196 = (n19, 666)
...     return n196
>>> def t(n, /):
...     gi = h(n)
...     n1 = next(gi)
...     n19 = (n1,999)
...     n196 = yield (gi, (True, n19))
...     n1967 = (n196,777)
...     return n1967
>>> flatten_recur(t(333))
((((333, 111), 999), 666), 777)

'''#'''


_test_boxed_tail_gi = r'''
>>> def f(n, /):
...     if n > 0:
...         return (False, f(n-1)); yield
...     raise Exception

>>> from sys import stdout
>>> from traceback import print_exc, format_exc
>>> try:
...     flatten_recur(f(10), boxed=True)
... except Exception as e:
...     assert 4 == (n:=format_exc().count('File')), n
...     print_exc(file=stdout) #doctest: +ELLIPSIS
Traceback (most recent call last):
  File "<doctest seed.iters.flatten_recur:_test_boxed_tail_gi[3]>", line 2, in <module>
    flatten_recur(f(10), boxed=True)
  File "/sdcard/0my_files/git_repos/python3_src/seed/iters/flatten_recur.py", line 108, in flatten_recur
    raise value
  File "/sdcard/0my_files/git_repos/python3_src/seed/iters/flatten_recur.py", line 76, in flatten_recur
    child_g = next_(value)
              ^^^^^^^^^^^^
  File "<doctest seed.iters.flatten_recur:_test_boxed_tail_gi[0]>", line 4, in f
    raise Exception
Exception


>>> def g(n, r, /):
...     if n > 0:
...         return (False, g(n-1,2+r)); yield
...     return (True, r)

>>> flatten_recur(g(10,1), boxed=True)
21
>>> flatten_recur(g(100000,1), boxed=True)
200001


'''#'''



















_test_exc = r'''

>>> def f(n, /):
...     if n > 0:
...         yield f(n-1)
...     raise Exception
>>> flatten_recur(f(10))
Traceback (most recent call last):
  ...
  ...
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 4, in f
    raise Exception
Exception
>>> from sys import stdout
>>> from traceback import print_exc
>>> try:
...     flatten_recur(f(10))
... except Exception as e:
...     print_exc(file=stdout) #doctest: +ELLIPSIS
Traceback (most recent call last):
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 3, in f
    yield f(n-1)
  ...
  File "<doctest seed.iters.flatten_recur:_test_exc[0]>", line 4, in f
    raise Exception
Exception




'''#'''



_old_test = r"""
example

>>> def bin_recur(max_depth, t, depth, d):
...     #print(depth, d)
...     if depth >= max_depth:
...         return 1
...         return depth
...     depth += d
...     a = yield bin_recur(max_depth, t, depth, d)
...     b = yield bin_recur(max_depth, t, depth, d*t)
...     return a+b
>>> def main_bin_recur(max_depth=2**13, t=4, depth=0, d=1):
...     return flatten_recur(bin_recur(max_depth, t, depth, d))
>>> main_bin_recur(64, 2)
27338
>>> main_bin_recur(2**13, 2**16) == 2**14
True

"""#"""




# from seed.iters.generator_iterator_mock_asif_at_initial_state import pack_generator_iterator__with_value_

#.flatten_recur = lazy_import4func_('seed.iters.flatten_recur', 'flatten_recur', __name__)
from seed.iters.flatten_recur import flatten_recur
# def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#
# [flatten_recur :: recur_GI -> final_result]
#   [recur_GI == GI{yield{recur_GI}; return{final_result if not boxed else (Either recur_GI final_result)}}]





from seed.iters.flatten_recur import *
