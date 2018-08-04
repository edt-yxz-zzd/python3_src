'module'



from types import *
import types
import inspect
from sand import bind_self
from functools import wraps


#print(dir(types))
['BuiltinFunctionType', 'BuiltinMethodType', 'CodeType', 'FrameType',
 'FunctionType', 'GeneratorType', 'GetSetDescriptorType', 'LambdaType',
 'MappingProxyType', 'MemberDescriptorType', 'MethodType', 'ModuleType',
 'SimpleNamespace', 'TracebackType', '__builtins__', '__cached__',
 '__doc__', '__file__', '__initializing__', '__loader__', '__name__',
 '__package__', '_calculate_meta', 'new_class', 'prepare_class']

def f(a,b='b', *c:'c', d, e='e', **f_:'f_'):
    print('f')

def m(*args, **kwargs):
    print('m', locals())

f.__call__ = m # useless
# f() ==>> type(f).__call__(f, ...)

f.__code__ = m.__code__
f(2,4,6, a=4)
help(f)
# f(*args, **kwargs)


# fail
##def g(a,b):
##    print(__doc__)
##    print(c)
##
##g.__doc__ = 'dddddd'
##g.c = 'afasf'
##g(1,2)


#help(FunctionType)
#function(code, globals[, name[, argdefs[, closure]]])
#print(dir(f))
#print(sorted(set(dir(f)) - set(dir(type(f)))))
#print(sorted(vars(type(f))))

def get_data_attrs(obj):
    for attr, x in vars(type(obj)).items():
        if inspect.isdatadescriptor(x):
            yield attr
#print(sorted(get_data_attrs(f)))

def show_func(f):
    for name in sorted(get_data_attrs(f)):
        if name not in ['__globals__']:
            print(name, getattr(f, name))

def f(a,b='b', *c:'c', d, e='e', **f_:'f_'):
    print('f')
    #nonlocal __this_func__
    print(__this_func__)
def insert_closure(f, closure):
    g = FunctionType(f.__code__, f.__globals__, f.__name__,
                     (1,2, 3), closure)
    return g
help(f)
show_func(f)
g = insert_closure(f, (f,))
help(g)
show_func(g)







##
##
##class FuncMeta(type):
##    def __init__(self, name, bases, namespace, *, api, **kwargs):
##        self.api = api
##        
##        
##class FuncXX(metaclass=FuncMeta):
##    def __new__(cls, f):
##        self = super().__new__(cls)
##        self._wrapper = wraps(f)
##        return self
##    def __call__(self, *args, **kwargs):
##        print(__class__, args, kwargs)
##
##
##t = FuncXX(f)
##print(t, type(t))
##help(t)
##t('afaf')


















