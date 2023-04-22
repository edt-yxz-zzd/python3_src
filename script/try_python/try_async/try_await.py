#__all__:goto
r'''[[[
e ../../python3_src/script/try_python/try_async/try_await.py

script.try_python.try_async.try_await
py -m nn_ns.app.debug_cmd script.try_python.try_async.try_await
py -m script.try_python.try_async.try_await
py -m nn_ns.app.adhoc_argparser__main__call8module script.try_python.try_async.try_await
from script.try_python.try_async.try_await import 

>>> class C(int):
...   def __await__(sf, /):
...     yield from range(sf)
...     return (sf, 999)
>>> async def f(i):
...   if i:
...     print(await C(i))
...   return (i, 888)
>>> x = f(5)
>>> print(x.send(None))
0
>>> for k in range(-1, -777, -1):
...   print(k, x.send(k))
Traceback (most recent call last):
    ...
AttributeError: 'range_iterator' object has no attribute 'send'


>>> from seed.tiny import print_err
>>> print_err = print
>>> class M(type):
...   def __getattribute__(sf, nm, /):
...       print_err(type, nm)
...       return type.__getattribute__(sf, nm)
>>> class It(metaclass=M):
...   def __getattribute__(sf, nm, /):
...       print_err(object, nm)
...       return object.__getattribute__(sf, nm)
...   def __init__(sf, i, /):
...     sf.i = i
...     sf.j = i
...   def __iter__(sf, /):
...     return sf
...   def __next__(sf, /):
...     if sf.i:
...         sf.i -= 1
...         return sf.i
...     raise StopIteration((sf.j, 666))
...   def send(sf, v=None, /):
...       print_err('send', v)
...       return next(sf)
...   def throw(sf, E, /, *args):
...       print_err('throw', E, args)
...       raise E(args)
...   def close(sf, /, *args):
...       print_err('close', args)
>>> class C(int):
...   def __await__(sf, /):
...     yield from It(sf)
...     return (sf, 999)
>>> async def f(i):
...   if i:
...     print('f await C():begin')
...     print('f await C()', await C(i))
...     print('f await C():end')
...   return (i, 888)
>>> x = f(5)
>>> print(x.send(None))
f await C():begin
<class 'object'> i
<class 'object'> i
<class 'object'> i
4
>>> for k in range(-1, -5, -1):
...   print(k, x.send(k))
<class 'object'> send
send -1
<class 'object'> i
<class 'object'> i
<class 'object'> i
-1 3
<class 'object'> send
send -2
<class 'object'> i
<class 'object'> i
<class 'object'> i
-2 2
<class 'object'> send
send -3
<class 'object'> i
<class 'object'> i
<class 'object'> i
-3 1
<class 'object'> send
send -4
<class 'object'> i
<class 'object'> i
<class 'object'> i
-4 0
>>> print(k, x.send(k))
Traceback (most recent call last):
    ...
StopIteration: (5, 888)
>>> print(k, x.send(k))
Traceback (most recent call last):
    ...
RuntimeError: cannot reuse already awaited coroutine


f await C():end 不见！！！

await ~=~ yield from
__await__ :: sf -> Generator

#]]]'''
__all__ = r'''
'''.split()#'''
__all__



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

