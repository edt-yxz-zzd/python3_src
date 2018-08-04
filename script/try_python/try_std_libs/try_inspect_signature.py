
'''
code remembers signature except defaults and annotations
function contains defaults and annotations
'''

def f(a, b=1, *args:'vararg', k, h=3, **kwargs)->'ret':pass
#print(dir(f))
for attr in ['__annotations__', '__closure__', '__code__', '__defaults__',
             '__dict__', '__kwdefaults__', '__module__', '__name__', '__qualname__',
             ]:
    print(attr, getattr(f, attr))

#print(dir(f.__code__))
for attr in ['co_argcount', 'co_cellvars', 'co_code', 'co_consts',
             #'co_filename', 'co_firstlineno',
             'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab',
             'co_name', 'co_names', 'co_nlocals',
             'co_stacksize', 'co_varnames']:
    print(attr, getattr(f.__code__, attr))

from inspect import signature, Signature, Parameter
import inspect

class GroupTemplate:
    def __init__(self, template):
        pass
sig = signature(GroupTemplate)
s = str(sig)
print(sig.bind('f').arguments)
# fail: print(inspect.getcallargs(GroupTemplate, 'f'))
# fail: print(inspect.getfullargspec(GroupTemplate))


import functools
def my_decorator(f):
    @functools.wraps(f)
    def g(*arg, **kwargs):pass
    return g

g = my_decorator(f)
print(signature(g)) # success
#not as expected: print(inspect.getcallargs(g, 'f')) # fail!!!!!!


g = my_decorator(GroupTemplate)
print(signature(g)) # success
#not as expected: print(inspect.getcallargs(g, 'f'))











