

from sand import get_data_attrs, show_data_attrs, show_data_attrs__func
from types import CodeType

def f0():
    pass
def f1(a):
    pass
def f2(*a):
    pass
def f3(*,a):
    pass
def f4(**a):
    pass

def f5(a,b='b', *c:'c_', d, e='e', **f_:'f_'):
    g = 3
    h = f2



def get_func_flags(f):
    return f.__code__.co_flags

def show_f(f):
    c = f.__code__
    print(c.co_argcount, c.co_nlocals, c.co_names, c.co_varnames)

    print('code:')
    show_data_attrs(c)
    print('\n'*2)
    show_data_attrs__func(f)
    print('\n'*4)


if 0:
    for n in range(6):
        fn = 'f{}'.format(n)
        f = globals()[fn]
        print(fn, bin(get_func_flags(f)))
        show_f(f)

    
class C:
    def f(a=1):
        pass
fs = C.f, C().f
print(C.f.__defaults__, C().f.__defaults__)
for f in fs:
    show_f(f)










