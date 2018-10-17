


r"""
see:
    ./__startup__register__exe_py__.py
see:
    "NOTE\Python\howto\python startup configuration.txt"
"""


def _f():
    #import site
    #print(f'sitecustomize.py:\n\t{__file__!r}')
    import warnings
    import importlib.machinery
    suffix = '.exe_py'
    warnings.warn(f'register {suffix!r} as importlib.machinery.SOURCE_SUFFIXES', ImportWarning)
    suffixes = importlib.machinery.SOURCE_SUFFIXES
    if suffix not in suffixes:
        suffixes.append(suffix)
#_f() # deprecated # see: __README__.txt
del _f

