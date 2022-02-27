
r'''

py -m script.try_python.try_dict_init

e ../../python3_src/script/try_python/try_dict_init.py


>>> dict([1, 0])
Traceback (most recent call last):
    ...
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> dict([(1, 0), (0, 1)]) == {1: 0, 0: 1}
True
>>> dict({(1, 0): 2, (0, 1): 3}) == {(1, 0): 2, (0, 1): 3}
True

>>> {1:2, 1:3}
{1: 3}
>>> dict({1:2, 1:3})
{1: 3}
>>> dict(a=1, a=1)
Traceback (most recent call last):
    ...
SyntaxError: keyword argument repeated


>>> class D:
...   def __len__(sf, /):
...     return 3
...   def __iter__(sf, /):
...     yield slice(0, 0, None)
...     yield from (1, 0)
...   def __getitem__(sf, k, /):
...     return (1, 0)[k]
>>> d = D()
>>> {**d}
Traceback (most recent call last):
    ...
TypeError: 'D' object is not a mapping
>>> dict(d)
Traceback (most recent call last):
    ...
TypeError: cannot convert dictionary update sequence element #0 to a sequence

>>> class D:
...   def __getitem__(sf, k, /):
...     return (1, 0)[k]
...   def keys(sf, /):
...     yield 1
...     return;yield
>>> d = D()
>>> {**d}
{1: 0}
>>> dict(d)
{1: 0}


#'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):



