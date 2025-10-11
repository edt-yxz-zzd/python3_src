r'''
e ../../python3_src/seed/debug/print_exc.py

源起:view ../../python3_src/seed/iters/flatten_recur.py
    doctest 并不认真对比 异常信息
    自己使用『print_exc(file=stdout) #doctest: +ELLIPSIS』才能更仔细确认 异常信息

>>> from seed.iters.flatten_recur import flatten_recur
>>> try:
...     flatten_recur(f(10))
... except Exception as e:
...     print_exc(file=stdout) #doctest: +ELLIPSIS

'''#'''

#from sys import stdout
from traceback import print_exc, format_exc
# print_exc(limit=None, file=None, chain=True)
#   Shorthand for 'print_exception(*sys.exc_info(), limit, file)'.

# format_exc(limit=None, chain=True)
#   Like print_exc() but return a string.


